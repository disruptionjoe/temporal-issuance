#!/usr/bin/env python3
"""H6 internal/external completion boundary audit.

This post-H9 fixture consumes H1, H2, H5, H7, and H9 as fixed inputs. It asks
whether the remaining formal/local OSAG support is internal source structure,
external completion language, or a bounded conditional form. It does not move
claim status or reopen TI-C020.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import completion_aware_adapter_p_admission_contract as h7
import h5_multi_holder_h7_separator as h5
import h9_physical_calibration_batch as h9


BOUNDED_INTERNAL_OSAG_CONDITIONAL = "BOUNDED_INTERNAL_OSAG_CONDITIONAL"
EXTERNAL_COMPLETION_LANGUAGE = "EXTERNAL_COMPLETION_LANGUAGE"
READOUT_FINALITY_COMPLETION = "READOUT_FINALITY_COMPLETION"
PHYSICAL_NEAR_MISS_ABSORBED = "PHYSICAL_NEAR_MISS_ABSORBED"
UNSUPPORTED_BOUNDARY_PACKET = "UNSUPPORTED_BOUNDARY_PACKET"


@dataclass(frozen=True)
class BoundaryCase:
    case_id: str
    source: str
    input_verdict: str
    h7_admitted: bool
    formal_local_osag_support: bool
    h1_h2_floor_satisfied: bool
    h5_holder_cost_absorbed: bool
    h9_physical_passed: bool
    imports_completion: bool
    readout_finality_only: bool
    fixed_source_absorber: bool
    real_physical_candidate: bool
    claims_physical_source: bool
    preserves_boundary_fields: bool


@dataclass(frozen=True)
class BoundaryDecision:
    case_id: str
    source: str
    input_verdict: str
    boundary_verdict: str
    boundary_class: str
    terminal: bool
    h7_admitted: bool
    physical_adapter_p_passed: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "source": self.source,
            "input_verdict": self.input_verdict,
            "boundary_verdict": self.boundary_verdict,
            "boundary_class": self.boundary_class,
            "terminal": self.terminal,
            "h7_admitted": self.h7_admitted,
            "physical_adapter_p_passed": self.physical_adapter_p_passed,
            "reason": self.reason,
        }


def _decision_map(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {decision["packet_id"]: decision for decision in result["decisions"]}


def _h5_result_map(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {case["case_id"]: case for case in result["results"]}


def _h9_result_map(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {case["case_id"]: case for case in result["results"]}


def boundary_cases() -> tuple[BoundaryCase, ...]:
    h7_result = h7.run_admission_contract()
    h5_result = h5.run_separator()
    h9_result = h9.run_calibration()
    h7_by_id = _decision_map(h7_result)
    h5_by_id = _h5_result_map(h5_result)
    h9_by_id = _h9_result_map(h9_result)

    h7_boundary = h7_by_id["boundary_osag_support"]
    h5_boundary = h5_by_id["h7_boundary_osag_holder_support"]
    h9_boundary = h9_by_id["h7_boundary_osag_support_control"]
    split_holder = h5_by_id["multi_holder_split_fixed_source"]
    crispr = h9_by_id["crispr_spacer_acquisition_near_miss"]
    floquet = h9_by_id["dynamic_floquet_code_negative_control"]
    neighbor = h7_by_id["neighbor_completion_table"]
    readout = h7_by_id["cross_repo_readout_language"]

    return (
        BoundaryCase(
            case_id="formal_local_osag_support",
            source="H7/H5/H9",
            input_verdict=h9_boundary["final_verdict"],
            h7_admitted=bool(h7_boundary["admitted"] and h9_boundary["h7_admitted"]),
            formal_local_osag_support=(
                h5_boundary["verdict"] == h5.H7_ADMITTED_FORMAL_LOCAL_SUPPORT
                and h9_boundary["final_verdict"]
                == h9.H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT
            ),
            h1_h2_floor_satisfied=bool(
                h7_result["h1_h2_floor_satisfied"]
                and h5_result["h7_floor_satisfied"]
                and h9_result["h7_floor_satisfied"]
            ),
            h5_holder_cost_absorbed=bool(
                h5_result["multi_holder_cost_absorbed_as_taf_readout"]
            ),
            h9_physical_passed=bool(h9_boundary["physical_adapter_p_passed"]),
            imports_completion=False,
            readout_finality_only=False,
            fixed_source_absorber=False,
            real_physical_candidate=False,
            claims_physical_source=False,
            preserves_boundary_fields=not h7_boundary["missing_requirements"],
        ),
        BoundaryCase(
            case_id="split_holder_reversal_cost",
            source="H5",
            input_verdict=split_holder["verdict"],
            h7_admitted=bool(split_holder["h7_admitted"]),
            formal_local_osag_support=False,
            h1_h2_floor_satisfied=bool(h5_result["h7_floor_satisfied"]),
            h5_holder_cost_absorbed=bool(
                h5_result["multi_holder_cost_absorbed_as_taf_readout"]
            ),
            h9_physical_passed=False,
            imports_completion=False,
            readout_finality_only=True,
            fixed_source_absorber=True,
            real_physical_candidate=False,
            claims_physical_source=False,
            preserves_boundary_fields=True,
        ),
        BoundaryCase(
            case_id="crispr_spacer_acquisition_near_miss",
            source="H9",
            input_verdict=crispr["final_verdict"],
            h7_admitted=bool(crispr["h7_admitted"]),
            formal_local_osag_support=False,
            h1_h2_floor_satisfied=bool(h9_result["h7_floor_satisfied"]),
            h5_holder_cost_absorbed=False,
            h9_physical_passed=bool(crispr["physical_adapter_p_passed"]),
            imports_completion=False,
            readout_finality_only=False,
            fixed_source_absorber=True,
            real_physical_candidate=True,
            claims_physical_source=False,
            preserves_boundary_fields=False,
        ),
        BoundaryCase(
            case_id="dynamic_floquet_code_negative_control",
            source="H9",
            input_verdict=floquet["final_verdict"],
            h7_admitted=bool(floquet["h7_admitted"]),
            formal_local_osag_support=False,
            h1_h2_floor_satisfied=bool(h9_result["h7_floor_satisfied"]),
            h5_holder_cost_absorbed=False,
            h9_physical_passed=bool(floquet["physical_adapter_p_passed"]),
            imports_completion=False,
            readout_finality_only=False,
            fixed_source_absorber=True,
            real_physical_candidate=True,
            claims_physical_source=False,
            preserves_boundary_fields=False,
        ),
        BoundaryCase(
            case_id="neighbor_completion_table",
            source="H7",
            input_verdict=neighbor["verdict"],
            h7_admitted=bool(neighbor["admitted"]),
            formal_local_osag_support=False,
            h1_h2_floor_satisfied=bool(h7_result["h1_h2_floor_satisfied"]),
            h5_holder_cost_absorbed=False,
            h9_physical_passed=False,
            imports_completion=True,
            readout_finality_only=False,
            fixed_source_absorber=True,
            real_physical_candidate=False,
            claims_physical_source=False,
            preserves_boundary_fields=False,
        ),
        BoundaryCase(
            case_id="cross_repo_readout_language",
            source="H7",
            input_verdict=readout["verdict"],
            h7_admitted=bool(readout["admitted"]),
            formal_local_osag_support=False,
            h1_h2_floor_satisfied=bool(h7_result["h1_h2_floor_satisfied"]),
            h5_holder_cost_absorbed=False,
            h9_physical_passed=False,
            imports_completion=False,
            readout_finality_only=True,
            fixed_source_absorber=False,
            real_physical_candidate=False,
            claims_physical_source=False,
            preserves_boundary_fields=True,
        ),
    )


def classify_case(case: BoundaryCase) -> BoundaryDecision:
    if (
        case.formal_local_osag_support
        and case.h7_admitted
        and case.h1_h2_floor_satisfied
        and case.preserves_boundary_fields
        and not case.real_physical_candidate
        and not case.h9_physical_passed
        and not case.claims_physical_source
    ):
        return BoundaryDecision(
            case_id=case.case_id,
            source=case.source,
            input_verdict=case.input_verdict,
            boundary_verdict=BOUNDED_INTERNAL_OSAG_CONDITIONAL,
            boundary_class="bounded_conditional_form",
            terminal=False,
            h7_admitted=case.h7_admitted,
            physical_adapter_p_passed=case.h9_physical_passed,
            reason=(
                "The packet is internal to the bounded formal/local OSAG construction, "
                "but only under the H1/H2/H7 conditions and without physical Adapter_P passage."
            ),
        )
    if case.readout_finality_only:
        return BoundaryDecision(
            case_id=case.case_id,
            source=case.source,
            input_verdict=case.input_verdict,
            boundary_verdict=READOUT_FINALITY_COMPLETION,
            boundary_class="observer_readout_or_finality",
            terminal=True,
            h7_admitted=case.h7_admitted,
            physical_adapter_p_passed=case.h9_physical_passed,
            reason="The packet is observer-side readout, holder finality, or cross-repo language.",
        )
    if case.imports_completion:
        return BoundaryDecision(
            case_id=case.case_id,
            source=case.source,
            input_verdict=case.input_verdict,
            boundary_verdict=EXTERNAL_COMPLETION_LANGUAGE,
            boundary_class="external_completion_or_import",
            terminal=True,
            h7_admitted=case.h7_admitted,
            physical_adapter_p_passed=case.h9_physical_passed,
            reason="The packet imports a completion table, law, oracle, or schema.",
        )
    if case.fixed_source_absorber and case.real_physical_candidate:
        return BoundaryDecision(
            case_id=case.case_id,
            source=case.source,
            input_verdict=case.input_verdict,
            boundary_verdict=PHYSICAL_NEAR_MISS_ABSORBED,
            boundary_class="fixed_source_physical_near_miss",
            terminal=True,
            h7_admitted=case.h7_admitted,
            physical_adapter_p_passed=case.h9_physical_passed,
            reason="The physical near-miss is absorbed by fixed sequence space or fixed platform/schedule.",
        )
    return BoundaryDecision(
        case_id=case.case_id,
        source=case.source,
        input_verdict=case.input_verdict,
        boundary_verdict=UNSUPPORTED_BOUNDARY_PACKET,
        boundary_class="unsupported_boundary_packet",
        terminal=False,
        h7_admitted=case.h7_admitted,
        physical_adapter_p_passed=case.h9_physical_passed,
        reason="The packet lacks enough preserved structure to set the H6 boundary.",
    )


def run_boundary_audit() -> dict[str, Any]:
    cases = boundary_cases()
    decisions = [classify_case(case) for case in cases]
    by_id = {decision.case_id: decision for decision in decisions}
    formal = by_id["formal_local_osag_support"]
    external_controls_terminal = all(
        by_id[case_id].terminal
        for case_id in (
            "neighbor_completion_table",
            "cross_repo_readout_language",
            "split_holder_reversal_cost",
            "crispr_spacer_acquisition_near_miss",
            "dynamic_floquet_code_negative_control",
        )
    )
    completion_boundary_set = (
        formal.boundary_verdict == BOUNDED_INTERNAL_OSAG_CONDITIONAL
        and external_controls_terminal
        and not formal.physical_adapter_p_passed
    )

    return {
        "fixture_id": "h6_completion_boundary_audit",
        "kind": "h6_internal_external_completion_boundary_audit",
        "fixed_inputs": {
            "h1": "whole-family completion channels are exercised",
            "h2": "bounded formal/local OSAG shape is constructed",
            "h5": "multi-holder cost is separated from source crossing",
            "h7": "only formal/local OSAG support is admitted",
            "h9": "current physical near-misses are absorbed",
        },
        "completion_boundary_set": completion_boundary_set,
        "formal_local_support_boundary": formal.boundary_class,
        "formal_local_support_is_external_completion_language": False,
        "formal_local_support_is_full_internal_source_structure": False,
        "bounded_internal_support_conditional": (
            formal.boundary_verdict == BOUNDED_INTERNAL_OSAG_CONDITIONAL
        ),
        "external_completion_controls_terminal": external_controls_terminal,
        "physical_adapter_p_passed_case_ids": [
            decision.case_id for decision in decisions if decision.physical_adapter_p_passed
        ],
        "h6_result": "formal_local_osag_support_bounded_conditional",
        "next_track_1_recommendation": (
            "Run H8 D-FORK regime signature bundle using the H6 boundary; do not "
            "rerun H6 unless a new concrete H7-admitted packet appears."
        ),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "honest_current_result": (
            "Formal/local OSAG support is not merely external completion language, "
            "but H6 only licenses it as a bounded conditional form internal to the "
            "H1/H2/H7 construction. It is not full internal source structure, not "
            "physical Adapter_P passage, and not a claim-status movement."
        ),
        "decisions": [decision.as_dict() for decision in decisions],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_json(run_boundary_audit(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
