#!/usr/bin/env python3
"""H8 D-FORK regime signature bundle.

This fixture packages the current FTS/Godelian, completion-boundary, and
formal/local OSAG signatures after H6. It reports the boundary; it does not
decide the non-computable D-FORK bit, reopen TI-C020, or move claims.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import h6_completion_boundary_audit as h6
import n_concavity_regime_discriminator as n_regime


FTS_SIGNATURE = "FTS_DEPLETING_CONCAVE_SIGNATURE"
GODELIAN_SIGNATURE = "GODELIAN_SUSTAINED_SIGNATURE"
BOUNDED_OSAG_SIGNATURE = "BOUNDED_FORMAL_LOCAL_OSAG_SIGNATURE"
PHYSICAL_SOURCE_STOP = "PHYSICAL_SOURCE_STOP"
COMPLETION_READOUT_STOP = "COMPLETION_OR_READOUT_STOP"


@dataclass(frozen=True)
class SignatureRow:
    row_id: str
    source: str
    signature: str
    supports_track_1: bool
    terminal: bool
    claim_movement_allowed: bool
    physical_source_allowed: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "row_id": self.row_id,
            "source": self.source,
            "signature": self.signature,
            "supports_track_1": self.supports_track_1,
            "terminal": self.terminal,
            "claim_movement_allowed": self.claim_movement_allowed,
            "physical_source_allowed": self.physical_source_allowed,
            "reason": self.reason,
        }


def build_signature_rows() -> tuple[SignatureRow, ...]:
    boundary = h6.run_boundary_audit()
    curvature = n_regime.run_fixture()

    rows: list[SignatureRow] = []

    rows.append(
        SignatureRow(
            row_id="fts_depleting_curvature",
            source="E156/N-curvature",
            signature=FTS_SIGNATURE,
            supports_track_1=True,
            terminal=False,
            claim_movement_allowed=False,
            physical_source_allowed=False,
            reason=(
                "FTS shows the depleting concave N signature and an interior optimum; "
                "this is a declared-regime signature, not an oracle."
            ),
        )
    )
    rows.append(
        SignatureRow(
            row_id="godelian_sustained_curvature",
            source="E156/N-curvature",
            signature=GODELIAN_SIGNATURE,
            supports_track_1=True,
            terminal=False,
            claim_movement_allowed=False,
            physical_source_allowed=False,
            reason=(
                "The Godelian toy regime sustains novelty and has no forced interior "
                "optimum; this corroborates the D-FORK distinction without deciding it."
            ),
        )
    )

    formal_boundary = boundary["formal_local_support_boundary"]
    rows.append(
        SignatureRow(
            row_id="h6_formal_local_osag_boundary",
            source="H6/H7/H9",
            signature=BOUNDED_OSAG_SIGNATURE,
            supports_track_1=True,
            terminal=False,
            claim_movement_allowed=False,
            physical_source_allowed=False,
            reason=(
                "H6 classifies formal/local OSAG support as bounded conditional form, "
                f"not full source structure ({formal_boundary})."
            ),
        )
    )

    for decision in boundary["decisions"]:
        if decision["case_id"] == "formal_local_osag_support":
            continue
        if decision["boundary_class"] in (
            "external_completion_or_import",
            "observer_readout_or_finality",
        ):
            signature = COMPLETION_READOUT_STOP
        else:
            signature = PHYSICAL_SOURCE_STOP
        rows.append(
            SignatureRow(
                row_id=f"terminal_{decision['case_id']}",
                source=decision["source"],
                signature=signature,
                supports_track_1=False,
                terminal=True,
                claim_movement_allowed=False,
                physical_source_allowed=False,
                reason=decision["reason"],
            )
        )

    return tuple(rows)


def run_signature_bundle() -> dict[str, Any]:
    boundary = h6.run_boundary_audit()
    curvature = n_regime.run_fixture()
    rows = build_signature_rows()
    track_rows = [row for row in rows if row.supports_track_1]
    terminal_rows = [row for row in rows if row.terminal]

    d_fork_boundary_reportable = (
        boundary["completion_boundary_set"]
        and curvature["curvature_separates_regimes"]
        and len(track_rows) == 3
        and all(not row.claim_movement_allowed for row in rows)
        and all(not row.physical_source_allowed for row in rows)
    )

    return {
        "fixture_id": "h8_d_fork_regime_signature_bundle",
        "kind": "d_fork_regime_signature_bundle_not_decision_procedure",
        "fixed_inputs": {
            "h6_result": boundary["h6_result"],
            "n_curvature_result": curvature["resolution"],
            "d_fork_status": "non_computable_structural_bit_not_decided",
        },
        "d_fork_boundary_reportable": d_fork_boundary_reportable,
        "curvature_separates_declared_regimes": curvature["curvature_separates_regimes"],
        "completion_boundary_set": boundary["completion_boundary_set"],
        "formal_local_support_boundary": boundary["formal_local_support_boundary"],
        "track_1_signature_row_ids": [row.row_id for row in track_rows],
        "terminal_stop_row_ids": [row.row_id for row in terminal_rows],
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "next_track_1_recommendation": (
            "Use H8 as a citation bundle for future D-FORK work; material progress now "
            "requires either a new concrete H7-admitted packet, a sharper theorem target, "
            "or an intentionally selected follow-on gate. Do not treat H8 as a D-FORK "
            "decision procedure."
        ),
        "honest_current_result": (
            "H8 packages three usable signatures: FTS depleting curvature, Godelian "
            "sustained curvature, and bounded formal/local OSAG support. The bundle "
            "reports the D-FORK boundary and terminal controls; it does not decide the "
            "non-computable fork, establish physical source issuance, reopen TI-C020, "
            "or move claims."
        ),
        "signature_rows": [row.as_dict() for row in rows],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_json(run_signature_bundle(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
