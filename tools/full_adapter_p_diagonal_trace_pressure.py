#!/usr/bin/env python3
"""Full Adapter_P pressure for the E162 stage-stratified diagonal trace.

This is a formal/local pressure fixture. It does not establish physical source
issuance and it does not move claim status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import anti_after_naming_source_action_trace_fixture as e162


FORMAL_LOCAL_ADAPTER_SHAPE_SURVIVES = "FORMAL_LOCAL_ADAPTER_SHAPE_SURVIVES"
PHYSICAL_ADAPTER_P_NOT_PASSED = "PHYSICAL_ADAPTER_P_NOT_PASSED"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
FIXED_SOURCE_DISCLOSURE = "FIXED_SOURCE_DISCLOSURE"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
SINGLETON_AFTER_NAMING_ABSORBED = "SINGLETON_AFTER_NAMING_ABSORBED"
WHOLE_FAMILY_COMPLETION_ABSORPTION = "WHOLE_FAMILY_COMPLETION_ABSORPTION"
OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE = "OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE"


ADAPTER_FIELDS = (
    "Gamma_n",
    "Adm_n",
    "e_n",
    "w_n",
    "Gamma_n_plus_1",
    "tau_n",
)

W_GATES = (
    "W1_non_isomorphic_algebra",
    "W2_new_admissibility_predicate",
    "W3_construction_space_growth",
    "W4_perturbation_non_factorization",
    "W5_record_preservation",
    "W6_gauge_absorption_pass",
)


@dataclass(frozen=True)
class PressureCase:
    case_id: str
    description: str
    source_trace_id: str
    adapter_fields: dict[str, bool]
    w_gates: dict[str, bool]
    defeats_taf_readout: bool
    defeats_fixed_source_access: bool
    defeats_imported_structure: bool
    defeats_after_fact_singleton: bool
    defeats_whole_family_completion: bool
    no_hidden_oracle: bool
    source_generated_not_experimenter_added: bool
    formal_local_trace: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class PressureResult:
    case_id: str
    verdict: str
    terminal: bool
    all_adapter_fields_mapped: bool
    source_growth_core_supplied: bool
    absorber_controls_supplied: bool
    local_controls_defeated: bool
    whole_family_completion_defeated: bool
    physical_adapter_p_passed: bool
    physical_source_issuance_established: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "all_adapter_fields_mapped": self.all_adapter_fields_mapped,
            "source_growth_core_supplied": self.source_growth_core_supplied,
            "absorber_controls_supplied": self.absorber_controls_supplied,
            "local_controls_defeated": self.local_controls_defeated,
            "whole_family_completion_defeated": self.whole_family_completion_defeated,
            "physical_adapter_p_passed": self.physical_adapter_p_passed,
            "physical_source_issuance_established": self.physical_source_issuance_established,
            "reason": self.reason,
        }


def _fields(all_mapped: bool = True, **overrides: bool) -> dict[str, bool]:
    fields = {field: all_mapped for field in ADAPTER_FIELDS}
    fields.update(overrides)
    return fields


def _gates(**overrides: bool) -> dict[str, bool]:
    gates = {gate: False for gate in W_GATES}
    gates.update(overrides)
    return gates


def e162_positive_trace_id() -> str:
    result = e162.run_fixture()
    positive = next(
        trace
        for trace in result["traces"]
        if trace["trace_id"] == "stage_stratified_diagonal_trace"
    )
    if positive["verdict"] != e162.CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS:
        raise RuntimeError("E162 positive trace no longer has the expected verdict")
    return positive["trace_id"]


def pressure_cases() -> list[PressureCase]:
    positive_trace = e162_positive_trace_id()
    base_positive_gates = _gates(
        W2_new_admissibility_predicate=True,
        W3_construction_space_growth=True,
        W6_gauge_absorption_pass=True,
    )
    return [
        PressureCase(
            case_id="stage_stratified_diagonal_trace_full_pressure",
            description=(
                "The E162 formal/local trace maps Adapter_P fields and defeats "
                "local readout, fixed-access, imported-structure, and singleton "
                "after-naming controls, but it is not a real physical candidate "
                "and does not defeat whole-family completion."
            ),
            source_trace_id=positive_trace,
            adapter_fields=_fields(),
            w_gates=base_positive_gates,
            defeats_taf_readout=True,
            defeats_fixed_source_access=True,
            defeats_imported_structure=True,
            defeats_after_fact_singleton=True,
            defeats_whole_family_completion=False,
            no_hidden_oracle=True,
            source_generated_not_experimenter_added=True,
            formal_local_trace=True,
            real_physical_candidate=False,
        ),
        PressureCase(
            case_id="taf_readout_control",
            description="A task delta expressible as capability/readout.",
            source_trace_id="e161_readout_sector",
            adapter_fields=_fields(),
            w_gates=_gates(W5_record_preservation=True),
            defeats_taf_readout=False,
            defeats_fixed_source_access=True,
            defeats_imported_structure=True,
            defeats_after_fact_singleton=False,
            defeats_whole_family_completion=False,
            no_hidden_oracle=False,
            source_generated_not_experimenter_added=False,
            formal_local_trace=False,
            real_physical_candidate=False,
        ),
        PressureCase(
            case_id="fixed_source_access_control",
            description="A continuation disclosed from fixed completion plus access.",
            source_trace_id="fixed_source_access_trace",
            adapter_fields=_fields(),
            w_gates=_gates(W5_record_preservation=True),
            defeats_taf_readout=True,
            defeats_fixed_source_access=False,
            defeats_imported_structure=True,
            defeats_after_fact_singleton=False,
            defeats_whole_family_completion=False,
            no_hidden_oracle=False,
            source_generated_not_experimenter_added=False,
            formal_local_trace=False,
            real_physical_candidate=False,
        ),
        PressureCase(
            case_id="imported_oracle_control",
            description="A novel-looking continuation supplied by an external oracle/table.",
            source_trace_id="imported_oracle_novel_name",
            adapter_fields=_fields(),
            w_gates=_gates(W2_new_admissibility_predicate=True),
            defeats_taf_readout=True,
            defeats_fixed_source_access=True,
            defeats_imported_structure=False,
            defeats_after_fact_singleton=True,
            defeats_whole_family_completion=False,
            no_hidden_oracle=False,
            source_generated_not_experimenter_added=False,
            formal_local_trace=False,
            real_physical_candidate=False,
        ),
        PressureCase(
            case_id="unguarded_after_fact_singleton_control",
            description="A diagonal-looking name without the stage-stratified guard.",
            source_trace_id="unguarded_diagonal_singleton_absorbed",
            adapter_fields=_fields(),
            w_gates=_gates(
                W2_new_admissibility_predicate=True,
                W3_construction_space_growth=True,
            ),
            defeats_taf_readout=True,
            defeats_fixed_source_access=True,
            defeats_imported_structure=True,
            defeats_after_fact_singleton=False,
            defeats_whole_family_completion=False,
            no_hidden_oracle=True,
            source_generated_not_experimenter_added=False,
            formal_local_trace=False,
            real_physical_candidate=False,
        ),
        PressureCase(
            case_id="whole_family_completion_control",
            description=(
                "The trace is fresh at the stage but the completed realized "
                "family can include the diagonal after the fact."
            ),
            source_trace_id=positive_trace,
            adapter_fields=_fields(),
            w_gates=base_positive_gates,
            defeats_taf_readout=True,
            defeats_fixed_source_access=True,
            defeats_imported_structure=True,
            defeats_after_fact_singleton=True,
            defeats_whole_family_completion=False,
            no_hidden_oracle=True,
            source_generated_not_experimenter_added=True,
            formal_local_trace=True,
            real_physical_candidate=True,
        ),
    ]


def classify_case(case: PressureCase) -> PressureResult:
    all_fields = all(case.adapter_fields.get(field, False) for field in ADAPTER_FIELDS)
    source_growth = any(
        case.w_gates.get(gate, False)
        for gate in (
            "W1_non_isomorphic_algebra",
            "W2_new_admissibility_predicate",
            "W3_construction_space_growth",
        )
    )
    absorber_controls = all(
        case.w_gates.get(gate, False)
        for gate in (
            "W4_perturbation_non_factorization",
            "W5_record_preservation",
            "W6_gauge_absorption_pass",
        )
    )
    local_controls = (
        case.defeats_taf_readout
        and case.defeats_fixed_source_access
        and case.defeats_imported_structure
        and case.defeats_after_fact_singleton
    )
    physical_passed = (
        all_fields
        and source_growth
        and absorber_controls
        and local_controls
        and case.defeats_whole_family_completion
        and case.no_hidden_oracle
        and case.source_generated_not_experimenter_added
        and case.real_physical_candidate
    )

    if not all_fields:
        verdict = OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
        reason = "The case does not map every Adapter_P field."
    elif not case.defeats_imported_structure:
        verdict = IMPORTED_STRUCTURE_REJECTION
        reason = "The apparent source action depends on an imported oracle or table."
    elif not case.defeats_fixed_source_access:
        verdict = FIXED_SOURCE_DISCLOSURE
        reason = "The trace factors through fixed completion plus access."
    elif not case.defeats_taf_readout:
        verdict = TAF_EXPRESSIBLE_READOUT
        reason = "The task delta is expressible as downstream capability/readout."
    elif not case.defeats_after_fact_singleton:
        verdict = SINGLETON_AFTER_NAMING_ABSORBED
        reason = "After-fact singleton naming absorbs the selected continuation."
    elif not case.defeats_whole_family_completion and case.real_physical_candidate:
        verdict = WHOLE_FAMILY_COMPLETION_ABSORPTION
        reason = (
            "The finite-stage trace remains vulnerable to completed-family "
            "absorption, so it fails physical Adapter_P."
        )
    elif case.formal_local_trace and source_growth and local_controls:
        verdict = FORMAL_LOCAL_ADAPTER_SHAPE_SURVIVES
        reason = (
            "The trace survives as a formal/local Adapter_P shape, but it lacks "
            "a real physical W1/W4/W5 path and whole-family completion defeat."
        )
    else:
        verdict = PHYSICAL_ADAPTER_P_NOT_PASSED
        reason = "The case lacks the W-gates or controls needed to pass Adapter_P."

    return PressureResult(
        case_id=case.case_id,
        verdict=verdict,
        terminal=not physical_passed,
        all_adapter_fields_mapped=all_fields,
        source_growth_core_supplied=source_growth,
        absorber_controls_supplied=absorber_controls,
        local_controls_defeated=local_controls,
        whole_family_completion_defeated=case.defeats_whole_family_completion,
        physical_adapter_p_passed=physical_passed,
        physical_source_issuance_established=physical_passed,
        reason=reason,
    )


def run_pressure() -> dict[str, Any]:
    cases = pressure_cases()
    results = [classify_case(case) for case in cases]
    by_id = {result.case_id: result for result in results}
    positive = by_id["stage_stratified_diagonal_trace_full_pressure"]
    whole_family = by_id["whole_family_completion_control"]
    verdicts = sorted({result.verdict for result in results})
    return {
        "fixture_id": "full_adapter_p_diagonal_trace_pressure",
        "kind": "formal_local_adapter_pressure_not_physical_claim",
        "source_trace": "E162 stage_stratified_diagonal_trace",
        "adapter_fields": list(ADAPTER_FIELDS),
        "w_gates": list(W_GATES),
        "claim_status_change": "none",
        "TI_C020_reopened": False,
        "physical_source_issuance_established": False,
        "formal_local_adapter_shape_survives": (
            positive.verdict == FORMAL_LOCAL_ADAPTER_SHAPE_SURVIVES
        ),
        "stage_trace_maps_all_adapter_fields": positive.all_adapter_fields_mapped,
        "stage_trace_supplies_formal_source_growth": positive.source_growth_core_supplied,
        "stage_trace_supplies_physical_absorber_controls": (
            positive.absorber_controls_supplied
        ),
        "stage_trace_defeats_local_controls": positive.local_controls_defeated,
        "stage_trace_defeats_whole_family_completion": (
            positive.whole_family_completion_defeated
        ),
        "whole_family_completion_control_absorbs": (
            whole_family.verdict == WHOLE_FAMILY_COMPLETION_ABSORPTION
        ),
        "active_trigger_change": "return_to_gate_change_wait_state",
        "next_trigger_recommendation": (
            "compact_no_worthy_work_until_real_physical_candidate_or_sharper_theorem_target"
        ),
        "honest_current_result": (
            "Full Adapter_P pressure preserves the E162 trace as a formal/local "
            "shape only. It does not pass physical Adapter_P because it lacks a "
            "real physical W1/W4/W5 path and does not defeat whole-family "
            "completion."
        ),
        "verdicts_seen": verdicts,
        "cases": [
            {
                "case_id": case.case_id,
                "source_trace_id": case.source_trace_id,
                "description": case.description,
                "adapter_fields": case.adapter_fields,
                "w_gates": case.w_gates,
            }
            for case in cases
        ],
        "results": [result.as_dict() for result in results],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/full_adapter_p_diagonal_trace_pressure_result.json"),
    )
    args = parser.parse_args()
    result = run_pressure()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
