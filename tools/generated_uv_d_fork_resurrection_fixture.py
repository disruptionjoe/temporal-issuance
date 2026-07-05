#!/usr/bin/env python3
"""Generated-UV D-FORK resurrection fixture.

This is a toy discriminator, not a physics simulation. It tests the E139
resurrection trigger: can a dynamically generated UV / degree-of-freedom model
produce a mode that is not merely fixed-completion disclosure, while also
escaping the E127 singleton after-the-fact enumerator ceiling?
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


STAGES = 6
FIXED_UV_WIDTH = 24
LOCAL_BASIS_WIDTH = 4


@dataclass(frozen=True)
class CandidateResult:
    candidate_id: str
    description: str
    new_mode_not_formable_at_stage_n: bool
    factors_through_fixed_completion_access_decoherence: bool
    fixed_decoherence_law: bool
    hidden_global_mode_table: bool
    imported_law_change: bool
    singleton_enumerator_absorbs_whole_family: bool
    verdict: str
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "description": self.description,
            "new_mode_not_formable_at_stage_n": self.new_mode_not_formable_at_stage_n,
            "factors_through_fixed_completion_access_decoherence": (
                self.factors_through_fixed_completion_access_decoherence
            ),
            "fixed_decoherence_law": self.fixed_decoherence_law,
            "hidden_global_mode_table": self.hidden_global_mode_table,
            "imported_law_change": self.imported_law_change,
            "singleton_enumerator_absorbs_whole_family": (
                self.singleton_enumerator_absorbs_whole_family
            ),
            "verdict": self.verdict,
            "reason": self.reason,
        }


def fixed_uv_algebra() -> list[str]:
    return [f"uv_fixed_{i:02d}" for i in range(FIXED_UV_WIDTH)]


def fixed_access_window(stage: int) -> list[str]:
    width = min(FIXED_UV_WIDTH, (stage + 1) * LOCAL_BASIS_WIDTH)
    return fixed_uv_algebra()[:width]


def evaluate_fixed_cutoff_candidate() -> CandidateResult:
    algebra = set(fixed_uv_algebra())
    disclosed_by_stage = [set(fixed_access_window(stage)) for stage in range(STAGES)]
    all_accessible_inside_fixed = all(stage_set <= algebra for stage_set in disclosed_by_stage)
    fixed_law = True
    factorizes = all_accessible_inside_fixed and fixed_law

    return CandidateResult(
        candidate_id="fixed_uv_cutoff_disclosure",
        description=(
            "A fixed UV algebra is progressively disclosed by a changing access "
            "window and fixed decoherence law."
        ),
        new_mode_not_formable_at_stage_n=False,
        factors_through_fixed_completion_access_decoherence=factorizes,
        fixed_decoherence_law=fixed_law,
        hidden_global_mode_table=False,
        imported_law_change=False,
        singleton_enumerator_absorbs_whole_family=True,
        verdict="ABSORBED_FIXED_COMPLETION_ACCESS",
        reason=(
            "Every recorded mode is already in the fixed completed UV algebra; "
            "growth is aperture disclosure, not source-side issuance."
        ),
    )


def local_basis(stage: int) -> list[str]:
    return [f"uv_basis_{stage}_{i}" for i in range(LOCAL_BASIS_WIDTH)]


def diagonal_mode(stage: int, context: list[str]) -> str:
    context_set = set(context)
    index = 0
    while True:
        candidate = f"uv_diag_{stage}_{len(context)}_{index}"
        if candidate not in context_set:
            return candidate
        index += 1


def generated_uv_trace() -> dict[str, Any]:
    issued: list[str] = []
    contexts: list[list[str]] = []
    for stage in range(STAGES):
        context = []
        for prior_stage in range(stage + 1):
            context.extend(local_basis(prior_stage))
        context.extend(issued)
        contexts.append(context)
        issued.append(diagonal_mode(stage, context))
    return {"issued": issued, "contexts": contexts}


def evaluate_dynamical_diagonal_candidate() -> CandidateResult:
    trace = generated_uv_trace()
    issued = trace["issued"]
    contexts = trace["contexts"]

    finite_prefix_fresh = all(
        mode not in set(contexts[stage])
        for stage, mode in enumerate(issued)
    )

    fixed_stage0_completion = set(local_basis(0))
    factors_through_stage0_completion = set(issued) <= fixed_stage0_completion

    singleton_enumerator = set(issued)
    singleton_absorbs = all(mode in singleton_enumerator for mode in issued)

    if finite_prefix_fresh and singleton_absorbs:
        verdict = "CLASS_RELATIVE_ONLY_SINGLETON_ABSORBED"
        reason = (
            "The diagonal mode is fresh relative to each finite prefix context, "
            "but the realized whole family is absorbed by an after-the-fact "
            "singleton enumerator. This matches OnlineIssuance^LC, not a new "
            "physical surplus."
        )
    elif finite_prefix_fresh and not singleton_absorbs:
        verdict = "UNEXPECTED_WHOLE_FAMILY_ESCAPE"
        reason = (
            "The candidate escaped the singleton ceiling. This would require "
            "governance review before any claim movement."
        )
    else:
        verdict = "NOT_FRESH"
        reason = "The candidate failed even finite-prefix freshness."

    return CandidateResult(
        candidate_id="dynamical_diagonal_uv_modes",
        description=(
            "Each stage forms a UV mode label by diagonalizing the present "
            "stage context, modeling staged degree-of-freedom formation."
        ),
        new_mode_not_formable_at_stage_n=finite_prefix_fresh,
        factors_through_fixed_completion_access_decoherence=factors_through_stage0_completion,
        fixed_decoherence_law=True,
        hidden_global_mode_table=False,
        imported_law_change=False,
        singleton_enumerator_absorbs_whole_family=singleton_absorbs,
        verdict=verdict,
        reason=reason,
    )


def evaluate_imported_law_change_candidate() -> CandidateResult:
    return CandidateResult(
        candidate_id="imported_dynamical_law_change",
        description=(
            "A modeler supplies a new stage law or hidden global table that "
            "declares future UV modes available."
        ),
        new_mode_not_formable_at_stage_n=False,
        factors_through_fixed_completion_access_decoherence=True,
        fixed_decoherence_law=False,
        hidden_global_mode_table=True,
        imported_law_change=True,
        singleton_enumerator_absorbs_whole_family=True,
        verdict="REJECTED_AS_IMPORTED_STRUCTURE",
        reason=(
            "The new mode table or law is supplied from outside the stage-local "
            "source. It is an absorber/control, not a generated source witness."
        ),
    )


def run_fixture_suite() -> dict[str, Any]:
    candidates = [
        evaluate_fixed_cutoff_candidate(),
        evaluate_dynamical_diagonal_candidate(),
        evaluate_imported_law_change_candidate(),
    ]
    by_id = {candidate.candidate_id: candidate for candidate in candidates}
    diagonal = by_id["dynamical_diagonal_uv_modes"]

    unexpected_positive = [
        candidate.candidate_id
        for candidate in candidates
        if candidate.verdict == "UNEXPECTED_WHOLE_FAMILY_ESCAPE"
    ]

    result = {
        "fixture_id": "d_fork_generated_uv_resurrection_fixture",
        "kind": "toy_discriminator_not_physics_simulation",
        "stages": STAGES,
        "claim_status_change": "none",
        "fixed_completed_algebra_access_decoherence_null_built": True,
        "finite_prefix_generated_uv_freshness_survives": (
            diagonal.new_mode_not_formable_at_stage_n
        ),
        "finite_fixed_completion_absorbs_dynamical_candidate": (
            diagonal.factors_through_fixed_completion_access_decoherence
        ),
        "whole_family_singleton_absorbs_dynamical_candidate": (
            diagonal.singleton_enumerator_absorbs_whole_family
        ),
        "unexpected_positive_candidates": unexpected_positive,
        "new_physical_surplus_over_formal_residue": bool(unexpected_positive),
        "Issue[S]^physical": False,
        "TI_C020_reopened": False,
        "physical_frontier_status": "still_reduces_to_D_FORK_class_relative_residue",
        "candidate_results": [candidate.as_dict() for candidate in candidates],
        "next_trigger": "compact_no_worthy_work_until_gate_changes",
    }
    return result


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/generated_uv_d_fork_resurrection_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture_suite()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
