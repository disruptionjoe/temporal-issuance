#!/usr/bin/env python3
"""H9 physical calibration batch through H1/H2/H7 gates.

This applies the AI-epistemology wave pattern: constrain by the intersection of
independent gates, then verify by two routes. It does not establish physical
source issuance or move claims.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import completion_aware_adapter_p_admission_contract as h7


CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED = "CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED"
FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED = (
    "FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED"
)
H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT = "H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT"
OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE = "OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
PHYSICAL_ADAPTER_P_NOT_PASSED = "PHYSICAL_ADAPTER_P_NOT_PASSED"


@dataclass(frozen=True)
class CalibrationCase:
    case_id: str
    system_kind: str
    description: str
    maps_adapter_fields: bool
    preserves_tau_n: bool
    preserves_preserve_n: bool
    preserves_represented_family_index: bool
    preserves_candidate_provenance: bool
    uses_h1_completion_channels: bool
    uses_h2_family_checks: bool
    declares_formal_local_only: bool
    claims_physical_source: bool
    source_growth_core_witness: bool
    w1_non_isomorphic_physical_algebra: bool
    w4_perturbation_non_factorization: bool
    w5_record_preservation_comparison: bool
    w6_gauge_absorption_pass: bool
    fixed_sequence_space_absorbs: bool
    fixed_platform_schedule_absorbs: bool
    imported_law_or_schema: bool
    taf_readout_or_finality_only: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class CalibrationResult:
    case_id: str
    system_kind: str
    physical_route_verdict: str
    h7_route_verdict: str
    final_verdict: str
    terminal: bool
    h7_admitted: bool
    physical_adapter_p_passed: bool
    source_growth_core_witness: bool
    absorber_controls_supplied: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "system_kind": self.system_kind,
            "physical_route_verdict": self.physical_route_verdict,
            "h7_route_verdict": self.h7_route_verdict,
            "final_verdict": self.final_verdict,
            "terminal": self.terminal,
            "h7_admitted": self.h7_admitted,
            "physical_adapter_p_passed": self.physical_adapter_p_passed,
            "source_growth_core_witness": self.source_growth_core_witness,
            "absorber_controls_supplied": self.absorber_controls_supplied,
            "reason": self.reason,
        }


def h7_decision_for_case(case: CalibrationCase) -> h7.AdmissionDecision:
    packet = h7.AdmissionPacket(
        packet_id=case.case_id,
        source_kind=case.system_kind,
        preserves_tau_n=case.preserves_tau_n,
        preserves_preserve_n=case.preserves_preserve_n,
        preserves_represented_family_index=case.preserves_represented_family_index,
        preserves_candidate_provenance=case.preserves_candidate_provenance,
        maps_adapter_fields=case.maps_adapter_fields,
        uses_h1_completion_channels=case.uses_h1_completion_channels,
        uses_h2_family_checks=case.uses_h2_family_checks,
        hidden_completion_oracle=False,
        imported_law_or_schema=case.imported_law_or_schema,
        readout_only_language=case.taf_readout_or_finality_only,
        declares_formal_local_only=case.declares_formal_local_only,
        claims_physical_source=case.claims_physical_source,
        moves_claim_status=False,
    )
    return h7.classify_packet(packet)


def physical_route_verdict(case: CalibrationCase) -> str:
    absorber_controls = (
        case.w4_perturbation_non_factorization
        and case.w5_record_preservation_comparison
        and case.w6_gauge_absorption_pass
    )
    physical_passed = (
        case.maps_adapter_fields
        and case.preserves_tau_n
        and case.source_growth_core_witness
        and case.w1_non_isomorphic_physical_algebra
        and absorber_controls
        and not case.fixed_sequence_space_absorbs
        and not case.fixed_platform_schedule_absorbs
        and not case.imported_law_or_schema
        and not case.taf_readout_or_finality_only
        and case.real_physical_candidate
    )

    if not case.maps_adapter_fields or not case.preserves_tau_n:
        return OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
    if case.imported_law_or_schema:
        return IMPORTED_STRUCTURE_REJECTION
    if case.taf_readout_or_finality_only:
        return TAF_EXPRESSIBLE_READOUT
    if case.fixed_sequence_space_absorbs:
        return CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED
    if case.fixed_platform_schedule_absorbs:
        return FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED
    if physical_passed:
        return "PHYSICAL_ADAPTER_P_PASSED"
    if case.declares_formal_local_only and not case.real_physical_candidate:
        return H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT
    return PHYSICAL_ADAPTER_P_NOT_PASSED


def classify_case(case: CalibrationCase) -> CalibrationResult:
    h7_decision = h7_decision_for_case(case)
    physical_verdict = physical_route_verdict(case)
    absorber_controls = (
        case.w4_perturbation_non_factorization
        and case.w5_record_preservation_comparison
        and case.w6_gauge_absorption_pass
    )
    physical_passed = physical_verdict == "PHYSICAL_ADAPTER_P_PASSED"

    if h7_decision.admitted and physical_verdict == H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT:
        final = H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT
        terminal = False
        reason = "The packet is admitted only as formal/local OSAG support."
    elif physical_verdict in (
        CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED,
        FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED,
        IMPORTED_STRUCTURE_REJECTION,
        TAF_EXPRESSIBLE_READOUT,
        OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE,
    ):
        final = physical_verdict
        terminal = True
        reason = "The physical route reaches a terminal absorber before any source claim."
    elif not h7_decision.admitted:
        final = h7_decision.verdict
        terminal = h7_decision.terminal
        reason = "The packet fails the H7 admission gate."
    else:
        final = physical_verdict
        terminal = not physical_passed
        reason = "The packet reaches the residual physical Adapter_P verdict."

    return CalibrationResult(
        case_id=case.case_id,
        system_kind=case.system_kind,
        physical_route_verdict=physical_verdict,
        h7_route_verdict=h7_decision.verdict,
        final_verdict=final,
        terminal=terminal,
        h7_admitted=h7_decision.admitted,
        physical_adapter_p_passed=physical_passed,
        source_growth_core_witness=case.source_growth_core_witness,
        absorber_controls_supplied=absorber_controls,
        reason=reason,
    )


def calibration_cases() -> tuple[CalibrationCase, ...]:
    return (
        CalibrationCase(
            case_id="crispr_spacer_acquisition_near_miss",
            system_kind="crispr",
            description=(
                "Native spacer acquisition maps the Adapter_P vocabulary but "
                "uses fixed sequence space, fixed Cas machinery, and no H2 "
                "family noncompletion rule."
            ),
            maps_adapter_fields=True,
            preserves_tau_n=True,
            preserves_preserve_n=False,
            preserves_represented_family_index=False,
            preserves_candidate_provenance=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=False,
            declares_formal_local_only=True,
            claims_physical_source=False,
            source_growth_core_witness=False,
            w1_non_isomorphic_physical_algebra=False,
            w4_perturbation_non_factorization=False,
            w5_record_preservation_comparison=True,
            w6_gauge_absorption_pass=True,
            fixed_sequence_space_absorbs=True,
            fixed_platform_schedule_absorbs=False,
            imported_law_or_schema=False,
            taf_readout_or_finality_only=False,
            real_physical_candidate=True,
        ),
        CalibrationCase(
            case_id="dynamic_floquet_code_negative_control",
            system_kind="dynamic_floquet_code",
            description=(
                "A dynamic/Floquet code changes effective code language while "
                "remaining inside fixed Hilbert space, instrument family, and "
                "schedule."
            ),
            maps_adapter_fields=True,
            preserves_tau_n=True,
            preserves_preserve_n=False,
            preserves_represented_family_index=False,
            preserves_candidate_provenance=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=False,
            declares_formal_local_only=True,
            claims_physical_source=False,
            source_growth_core_witness=False,
            w1_non_isomorphic_physical_algebra=False,
            w4_perturbation_non_factorization=False,
            w5_record_preservation_comparison=True,
            w6_gauge_absorption_pass=True,
            fixed_sequence_space_absorbs=False,
            fixed_platform_schedule_absorbs=True,
            imported_law_or_schema=False,
            taf_readout_or_finality_only=False,
            real_physical_candidate=True,
        ),
        CalibrationCase(
            case_id="h7_boundary_osag_support_control",
            system_kind="boundary",
            description=(
                "The H7 admitted packet is retained as formal/local OSAG support "
                "and is not upgraded into a physical source candidate."
            ),
            maps_adapter_fields=True,
            preserves_tau_n=True,
            preserves_preserve_n=True,
            preserves_represented_family_index=True,
            preserves_candidate_provenance=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=True,
            declares_formal_local_only=True,
            claims_physical_source=False,
            source_growth_core_witness=True,
            w1_non_isomorphic_physical_algebra=False,
            w4_perturbation_non_factorization=False,
            w5_record_preservation_comparison=False,
            w6_gauge_absorption_pass=True,
            fixed_sequence_space_absorbs=False,
            fixed_platform_schedule_absorbs=False,
            imported_law_or_schema=False,
            taf_readout_or_finality_only=False,
            real_physical_candidate=False,
        ),
    )


def run_calibration() -> dict[str, Any]:
    floor = h7.run_admission_contract()
    results = [classify_case(case) for case in calibration_cases()]
    by_id = {result.case_id: result for result in results}
    physical_passes = [result.case_id for result in results if result.physical_adapter_p_passed]
    admitted = [result.case_id for result in results if result.h7_admitted]
    physical_near_misses = (
        by_id["crispr_spacer_acquisition_near_miss"].final_verdict
        == CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED
        and by_id["dynamic_floquet_code_negative_control"].final_verdict
        == FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED
    )
    differential_routes_agree = (
        not physical_passes
        and admitted == ["h7_boundary_osag_support_control"]
        and physical_near_misses
    )
    return {
        "fixture_id": "h9_physical_calibration_batch",
        "kind": "h9_physical_calibration_through_h1_h2_h7",
        "ai_epistemology_wave_method": {
            "M1_COI": "H9 candidates must satisfy H1 completion channels, H2 OSAG checks, H7 admission, and physical W-gates at once.",
            "M3_differential_verification": "Each case is classified by a physical W-gate route and an H7 admission route.",
            "M6_execution_mode": "H9 is a high-cascade shared-context gate, so it runs as one batched local pass rather than broad fan-out.",
        },
        "h7_floor_satisfied": bool(floor["h1_h2_floor_satisfied"]),
        "h7_admitted_packet_ids": floor["admitted_packet_ids"],
        "physical_near_misses_absorbed": physical_near_misses,
        "differential_routes_agree": differential_routes_agree,
        "physical_adapter_p_passed_case_ids": physical_passes,
        "h7_admitted_case_ids": admitted,
        "h9_result": "physical_calibration_near_misses_absorbed",
        "next_track_1_recommendation": (
            "H6 internal versus external completion boundary, or pause until a "
            "new concrete H7-admitted physical packet exists."
        ),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "honest_current_result": (
            "CRISPR spacer acquisition and dynamic/Floquet code behavior are "
            "useful calibrators, but both are absorbed by fixed sequence space "
            "or fixed platform/schedule before a source-crossing claim. The only "
            "H7-admitted packet remains formal/local OSAG support."
        ),
        "results": [result.as_dict() for result in results],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_json(run_calibration(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
