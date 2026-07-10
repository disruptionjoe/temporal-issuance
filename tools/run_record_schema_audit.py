#!/usr/bin/env python3
"""Observation-only schema audit for Temporal Issuance run records.

The repo has useful historical records that predate the current frontmatter
shape, so this tool reports legacy drift without making old files fail by
default. New structured records should carry enough metadata and closeout
sections to be recoverable by a later steward.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_FRONTMATTER_FIELDS = (
    "artifact_type",
    "status",
    "run_id",
)

RECOMMENDED_FRONTMATTER_FIELDS = (
    "created",
    "trigger",
)

FIELD_ALIASES = {
    "created": ("created", "date"),
}

RECOMMENDED_SECTIONS = (
    "Objective",
    "Method",
    "Result",
    "Files Changed",
    "Boundaries",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "path": self.path,
            "message": self.message,
        }


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, []

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, text, ["frontmatter block is not closed"]

    metadata: dict[str, str] = {}
    errors: list[str] = []
    for line_number, raw_line in enumerate(lines[1:end_index], start=2):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if raw_line[:1].isspace() or line.startswith("- "):
            continue
        if ":" not in line:
            errors.append(f"line {line_number} is not a simple key/value pair")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if not key:
            errors.append(f"line {line_number} has an empty key")
            continue
        metadata[key] = value

    body = "\n".join(lines[end_index + 1 :])
    return metadata, body, errors


def has_heading(body: str, heading: str) -> bool:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    return re.search(pattern, body, flags=re.MULTILINE) is not None


def audit_run_record(path: Path, base: Path | None = None) -> list[Finding]:
    resolved_path = path.resolve()
    if base is None:
        display_path = str(path)
    else:
        try:
            display_path = str(resolved_path.relative_to(base.resolve()))
        except ValueError:
            display_path = str(resolved_path)

    text = resolved_path.read_text(encoding="utf-8")
    metadata, body, parse_errors = parse_frontmatter(text)
    findings: list[Finding] = []

    if metadata is None:
        return [
            Finding(
                severity="warning",
                code="legacy_no_frontmatter",
                path=display_path,
                message="record has no frontmatter; tolerate as legacy, but do not copy for new runs",
            )
        ]

    if metadata.get("artifact_type") != "agent_run":
        code = "legacy_malformed_frontmatter" if parse_errors else "not_agent_run_frontmatter"
        message = (
            "record is not tagged artifact_type: agent_run; treat as legacy or non-run markdown"
        )
        if parse_errors:
            message = (
                "frontmatter-like opening is not a valid agent_run metadata block; "
                "tolerate as legacy, but do not copy for new runs"
            )
        return [
            Finding(
                severity="warning",
                code=code,
                path=display_path,
                message=message,
            )
        ]

    for error in parse_errors:
        findings.append(
            Finding(
                severity="error",
                code="malformed_frontmatter",
                path=display_path,
                message=error,
            )
        )

    for field in REQUIRED_FRONTMATTER_FIELDS:
        aliases = FIELD_ALIASES.get(field, (field,))
        if not any(metadata.get(alias) for alias in aliases):
            findings.append(
                Finding(
                    severity="error",
                    code="missing_frontmatter_field",
                    path=display_path,
                    message=f"missing required frontmatter field: {field}",
                )
            )

    for field in RECOMMENDED_FRONTMATTER_FIELDS:
        aliases = FIELD_ALIASES.get(field, (field,))
        if not any(metadata.get(alias) for alias in aliases):
            if field == "trigger" and has_heading(body, "Trigger"):
                findings.append(
                    Finding(
                        severity="warning",
                        code="trigger_in_body_only",
                        path=display_path,
                        message="trigger is documented in the body but missing from frontmatter",
                    )
                )
                continue
            findings.append(
                Finding(
                    severity="warning",
                    code="missing_recommended_frontmatter_field",
                    path=display_path,
                    message=f"missing recommended frontmatter field: {field}",
                )
            )

    run_id = metadata.get("run_id")
    if run_id and run_id not in path.name:
        findings.append(
            Finding(
                severity="warning",
                code="run_id_filename_mismatch",
                path=display_path,
                message=f"run_id {run_id} does not appear in filename",
            )
        )

    for section in RECOMMENDED_SECTIONS:
        if not has_heading(body, section):
            findings.append(
                Finding(
                    severity="warning",
                    code="missing_recommended_section",
                    path=display_path,
                    message=f"missing recommended closeout section: {section}",
                )
            )

    return findings


def iter_markdown_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        path = path.resolve()
        if path.is_dir():
            files.extend(
                file
                for file in sorted(path.glob("*.md"))
                if file.name != "README.md"
            )
        else:
            files.append(path)
    return files


def audit_paths(paths: Iterable[Path]) -> dict[str, object]:
    root = repo_root()
    files = iter_markdown_files(paths)
    findings: list[Finding] = []
    for path in files:
        findings.extend(audit_run_record(path, base=root))

    error_count = sum(1 for finding in findings if finding.severity == "error")
    warning_count = sum(1 for finding in findings if finding.severity == "warning")
    return {
        "audit_complete": True,
        "files_audited": len(files),
        "errors": error_count,
        "warnings": warning_count,
        "findings": [finding.as_dict() for finding in findings],
    }


def default_paths() -> list[Path]:
    return [repo_root() / "agent-runs"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Run record files or directories to audit; defaults to agent-runs/",
    )
    parser.add_argument("--json", action="store_true", help="write machine-readable JSON")
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="return nonzero when malformed structured records are found",
    )
    args = parser.parse_args(argv)

    summary = audit_paths(args.paths or default_paths())

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(
            "Run record schema audit: "
            f"{summary['files_audited']} files, "
            f"{summary['errors']} errors, "
            f"{summary['warnings']} warnings"
        )
        for finding in summary["findings"]:
            print(
                f"{finding['severity'].upper()} {finding['path']}: "
                f"{finding['code']} - {finding['message']}"
            )

    return 1 if args.fail_on_error and summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
