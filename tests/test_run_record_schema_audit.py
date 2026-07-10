#!/usr/bin/env python3
"""Tests for tools/run_record_schema_audit.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import run_record_schema_audit as audit  # noqa: E402


VALID_RECORD = """---
artifact_type: agent_run
status: complete
run_id: RUN-9999
created: 2026-07-10
trigger: fixture
constitutional: false
---

# RUN-9999: Fixture

## Objective

Check a valid structured run record.

## Method

Run the audit.

## Result

No schema issues.

## Files Changed

- None.

## Boundaries

No gated surfaces touched.
"""


class RunRecordSchemaAuditTests(unittest.TestCase):
    def write_temp_record(self, text: str, name: str = "RUN-9999-fixture.md") -> Path:
        root = Path(self.tmp.name)
        path = root / name
        path.write_text(text, encoding="utf-8")
        return path

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_valid_structured_record_has_no_findings(self) -> None:
        path = self.write_temp_record(VALID_RECORD)
        findings = audit.audit_run_record(path)
        self.assertEqual(findings, [])

    def test_legacy_record_without_frontmatter_is_warning_only(self) -> None:
        path = self.write_temp_record("# Legacy\n\nBody\n", name="RUN-0001-legacy.md")
        findings = audit.audit_run_record(path)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].severity, "warning")
        self.assertEqual(findings[0].code, "legacy_no_frontmatter")

    def test_structured_record_missing_required_metadata_is_error(self) -> None:
        path = self.write_temp_record(
            VALID_RECORD.replace("run_id: RUN-9999\n", "").replace("trigger: fixture\n", "")
        )
        findings = audit.audit_run_record(path)
        errors = [finding for finding in findings if finding.severity == "error"]
        warnings = [finding for finding in findings if finding.severity == "warning"]
        self.assertEqual(
            {finding.message for finding in errors},
            {
                "missing required frontmatter field: run_id",
            },
        )
        self.assertIn(
            "missing recommended frontmatter field: trigger",
            {finding.message for finding in warnings},
        )

    def test_missing_recommended_section_is_warning(self) -> None:
        path = self.write_temp_record(VALID_RECORD.replace("## Boundaries\n\nNo gated surfaces touched.\n", ""))
        findings = audit.audit_run_record(path)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].severity, "warning")
        self.assertEqual(findings[0].code, "missing_recommended_section")
        self.assertIn("Boundaries", findings[0].message)

    def test_directory_audit_counts_files_and_findings(self) -> None:
        root = Path(self.tmp.name)
        self.write_temp_record(VALID_RECORD)
        self.write_temp_record("# Legacy\n", name="RUN-0001-legacy.md")
        summary = audit.audit_paths([root])
        self.assertTrue(summary["audit_complete"])
        self.assertEqual(summary["files_audited"], 2)
        self.assertEqual(summary["errors"], 0)
        self.assertEqual(summary["warnings"], 1)

    def test_cli_json_output(self) -> None:
        path = self.write_temp_record(VALID_RECORD)
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "run_record_schema_audit.py"), "--json", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        summary = json.loads(result.stdout)
        self.assertEqual(summary["files_audited"], 1)
        self.assertEqual(summary["errors"], 0)
        self.assertEqual(summary["warnings"], 0)


if __name__ == "__main__":
    unittest.main()
