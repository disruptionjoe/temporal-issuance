"""Countermodel and guards for E196's fixed-oracle boundary.

This executable checks the logical shape of the result.  It does not claim
that a completed non-computable oracle is physically realizable.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class OracleAdversary:
    adversary_id: str
    oracle_fixed_at_stage_zero: bool
    oracle_reselected_after_stage_zero: bool
    computes_option_set_join: bool
    computes_realized_path: bool
    schedule_has_oracle_access: bool
    reads_source_after_stage_zero: bool
    covers_counterfactual_branch_family: bool = False


def classify(adversary: OracleAdversary) -> dict[str, object]:
    """Classify whether the declared adversary defeats the corrected guard."""

    missing: list[str] = []
    if not adversary.computes_option_set_join:
        missing.append("option_set_join")
    if not adversary.computes_realized_path:
        missing.append("realized_path")
    if not adversary.schedule_has_oracle_access:
        missing.append("schedule_oracle_access")

    if adversary.reads_source_after_stage_zero:
        verdict = "ADAPTIVE_SOURCE_COPY_NOT_STATIC_DISCLOSURE"
        reproduces_realized_trace = True
    elif adversary.oracle_reselected_after_stage_zero or not adversary.oracle_fixed_at_stage_zero:
        verdict = "ORACLE_RESELECTION_OUTSIDE_FIXED_CLASS"
        reproduces_realized_trace = not missing
    elif not missing:
        verdict = "FIXED_PRECORRELATED_ORACLE_COUNTERMODEL"
        reproduces_realized_trace = True
    else:
        verdict = "CORRECTED_DEGREE_GUARD_DEFEATS_DISCLOSER"
        reproduces_realized_trace = False

    return {
        "adversary_id": adversary.adversary_id,
        "verdict": verdict,
        "missing_requirements": missing,
        "oracle_fixed_at_stage_zero": adversary.oracle_fixed_at_stage_zero,
        "oracle_reselected_after_stage_zero": adversary.oracle_reselected_after_stage_zero,
        "reproduces_realized_trace": reproduces_realized_trace,
        "counterfactual_family_covered": (
            reproduces_realized_trace and adversary.covers_counterfactual_branch_family
        ),
        "physical_realizability_established": False,
        "source_issuance_established": False,
    }


def fixture_rows() -> list[OracleAdversary]:
    return [
        OracleAdversary(
            adversary_id="fixed_realized_history_oracle",
            oracle_fixed_at_stage_zero=True,
            oracle_reselected_after_stage_zero=False,
            computes_option_set_join=True,
            computes_realized_path=True,
            schedule_has_oracle_access=True,
            reads_source_after_stage_zero=False,
        ),
        OracleAdversary(
            adversary_id="fixed_branch_complete_oracle",
            oracle_fixed_at_stage_zero=True,
            oracle_reselected_after_stage_zero=False,
            computes_option_set_join=True,
            computes_realized_path=True,
            schedule_has_oracle_access=True,
            reads_source_after_stage_zero=False,
            covers_counterfactual_branch_family=True,
        ),
        OracleAdversary(
            adversary_id="fixed_option_only_oracle",
            oracle_fixed_at_stage_zero=True,
            oracle_reselected_after_stage_zero=False,
            computes_option_set_join=True,
            computes_realized_path=False,
            schedule_has_oracle_access=True,
            reads_source_after_stage_zero=False,
        ),
        OracleAdversary(
            adversary_id="fixed_path_only_oracle",
            oracle_fixed_at_stage_zero=True,
            oracle_reselected_after_stage_zero=False,
            computes_option_set_join=False,
            computes_realized_path=True,
            schedule_has_oracle_access=True,
            reads_source_after_stage_zero=False,
        ),
        OracleAdversary(
            adversary_id="adaptive_source_reader",
            oracle_fixed_at_stage_zero=True,
            oracle_reselected_after_stage_zero=False,
            computes_option_set_join=False,
            computes_realized_path=False,
            schedule_has_oracle_access=False,
            reads_source_after_stage_zero=True,
        ),
    ]


def result() -> dict[str, object]:
    rows = [classify(row) for row in fixture_rows()]
    return {
        "result": "E196_BOUNDARY_NARROWED_BY_FIXED_ORACLE_COUNTERMODEL",
        "rows": rows,
        "fixed_countermodel_count": sum(
            row["verdict"] == "FIXED_PRECORRELATED_ORACLE_COUNTERMODEL"
            for row in rows
        ),
        "corrected_guard": (
            "Let J be the join of the realized option-set and path-selection "
            "information. An O-computable fixed disclosure schedule is defeated "
            "only when J is not Turing-reducible to O. Stage-0 fixedness alone "
            "does not imply that condition."
        ),
        "stage_zero_fixedness_sufficient_for_defeat": False,
        "oracle_reselection_required_for_escape": False,
        "physical_realizability_established": False,
        "source_issuance_established": False,
        "claim_status_change": None,
    }


def main() -> None:
    output = result()
    artifact = (
        Path(__file__).resolve().parents[1]
        / "tests"
        / "artifacts"
        / "e196_fixed_oracle_countermodel_result.json"
    )
    artifact.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
