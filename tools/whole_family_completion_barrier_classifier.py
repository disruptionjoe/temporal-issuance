#!/usr/bin/env python3
"""Whole-family completion barrier classifier for Adapter_P traces.

This Wave 1 artifact narrows H1 to an executable classifier. It is not a
universal theorem about all physics and it does not move claim status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE = "OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE"
VALUE_COMPLETION_ABSORPTION = "VALUE_COMPLETION_ABSORPTION"
NAME_COMPLETION_ABSORPTION = "NAME_COMPLETION_ABSORPTION"
PROVENANCE_ACTION_COMPLETION_ABSORPTION = (
    "PROVENANCE_ACTION_COMPLETION_ABSORPTION"
)
CAPABILITY_COMPLETION_ABSORPTION = "CAPABILITY_COMPLETION_ABSORPTION"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
POTENTIAL_ESCAPE_REQUIRES_OSAG = "POTENTIAL_ESCAPE_REQUIRES_OSAG"
NEEDS_CONCRETE_TRACE = "NEEDS_CONCRETE_TRACE"

COMPLETION_ABSORPTION_CLASSES = (
    VALUE_COMPLETION_ABSORPTION,
    NAME_COMPLETION_ABSORPTION,
    PROVENANCE_ACTION_COMPLETION_ABSORPTION,
    CAPABILITY_COMPLETION_ABSORPTION,
)

ADAPTER_FIELDS = (
    "Gamma_n",
    "Adm_n",
    "e_n",
    "w_n",
    "Gamma_n_plus_1",
    "tau_n",
)


@dataclass(frozen=True)
class CompletionBarrierCase:
    candidate_id: str
    description: str
    adapter_fields: dict[str, bool]
    tau_preserved: bool
    finite_prefix_non_precontained: bool
    source_growth_core_witness: bool
    absorber_controls_supplied: bool
    value_in_fixed_completion: bool
    name_available_after_fact: bool
    provenance_action_preformed: bool
    capability_delta_precomputed: bool
    factors_through_fixed_completion_access: bool
    taf_readout_or_finality_only: bool
    imports_external_structure: bool
    hidden_completed_oracle: bool
    experimenter_added_schema: bool
    preaction_family_noncompletion_rule: bool
    concrete_trace_supplied: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class CompletionBarrierResult:
    candidate_id: str
    verdict: str
    terminal: bool
    completion_channels: dict[str, bool]
    preaction_family_noncompletion_rule: bool
    source_growth_core_witness: bool
    finite_prefix_non_precontained: bool
    absorber_controls_supplied: bool
    concrete_trace_supplied: bool
    real_physical_candidate: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "completion_channels": self.completion_channels,
            "preaction_family_noncompletion_rule": (
                self.preaction_family_noncompletion_rule
            ),
            "source_growth_core_witness": self.source_growth_core_witness,
            "finite_prefix_non_precontained": self.finite_prefix_non_precontained,
            "absorber_controls_supplied": self.absorber_controls_supplied,
            "concrete_trace_supplied": self.concrete_trace_supplied,
            "real_physical_candidate": self.real_physical_candidate,
            "reason": self.reason,
        }


def _fields(all_mapped: bool = True, **overrides: bool) -> dict[str, bool]:
    fields = {field: all_mapped for field in ADAPTER_FIELDS}
    fields.update(overrides)
    return fields


def completion_channels(case: CompletionBarrierCase) -> dict[str, bool]:
    return {
        "value_completion": case.value_in_fixed_completion
        and not case.source_growth_core_witness,
        "name_completion": case.name_available_after_fact
        and not case.preaction_family_noncompletion_rule,
        "provenance_action_completion": case.provenance_action_preformed
        and not case.preaction_family_noncompletion_rule,
        "capability_completion": (
            case.capability_delta_precomputed
            or case.factors_through_fixed_completion_access
        ),
    }


def all_adapter_fields_mapped(case: CompletionBarrierCase) -> bool:
    return all(case.adapter_fields.get(field, False) for field in ADAPTER_FIELDS)


def classify_case(case: CompletionBarrierCase) -> CompletionBarrierResult:
    channels = completion_channels(case)

    if not all_adapter_fields_mapped(case) or not case.tau_preserved:
        verdict = OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
        terminal = False
        reason = (
            "The trace does not map every Adapter_P field while preserving tau_n."
        )
    elif (
        case.imports_external_structure
        or case.hidden_completed_oracle
        or case.experimenter_added_schema
    ):
        verdict = IMPORTED_STRUCTURE_REJECTION
        terminal = True
        reason = (
            "The apparent escape depends on an imported law, hidden completed "
            "oracle, or modeler-added schema."
        )
    elif (
        case.taf_readout_or_finality_only
        and not case.source_growth_core_witness
        and not case.preaction_family_noncompletion_rule
    ):
        verdict = TAF_EXPRESSIBLE_READOUT
        terminal = True
        reason = "The task delta is finality or readout without source growth."
    elif channels["capability_completion"]:
        verdict = CAPABILITY_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "The capability or task delta is already determined by fixed source "
            "plus access, schedule, finality, or readout."
        )
    elif channels["provenance_action_completion"]:
        verdict = PROVENANCE_ACTION_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "The action, witness, provenance, and task delta are preformed before "
            "the alleged source action."
        )
    elif channels["name_completion"]:
        verdict = NAME_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "The finite-prefix novelty is absorbed by after-fact whole-family "
            "naming without a pre-action family noncompletion rule."
        )
    elif channels["value_completion"]:
        verdict = VALUE_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "The candidate only discloses a value from a fixed completed value "
            "space and supplies no source-growth core witness."
        )
    elif (
        case.preaction_family_noncompletion_rule
        and case.finite_prefix_non_precontained
        and case.source_growth_core_witness
        and not any(channels.values())
    ):
        verdict = POTENTIAL_ESCAPE_REQUIRES_OSAG
        terminal = False
        reason = (
            "This is the only non-absorbed shape in the bounded classifier: it "
            "requires an internal pre-action rule that blocks family completion, "
            "then needs OSAG or a full physical fixture."
        )
    else:
        verdict = NEEDS_CONCRETE_TRACE
        terminal = False
        reason = (
            "The case is not absorbed by a named channel, but it lacks the "
            "pre-action family noncompletion rule or source-growth witness needed "
            "to count as the H1 escape shape."
        )

    return CompletionBarrierResult(
        candidate_id=case.candidate_id,
        verdict=verdict,
        terminal=terminal,
        completion_channels=channels,
        preaction_family_noncompletion_rule=(
            case.preaction_family_noncompletion_rule
        ),
        source_growth_core_witness=case.source_growth_core_witness,
        finite_prefix_non_precontained=case.finite_prefix_non_precontained,
        absorber_controls_supplied=case.absorber_controls_supplied,
        concrete_trace_supplied=case.concrete_trace_supplied,
        real_physical_candidate=case.real_physical_candidate,
        reason=reason,
    )


def barrier_cases() -> list[CompletionBarrierCase]:
    return [
        CompletionBarrierCase(
            candidate_id="missing_adapter_field",
            description="A partial trace omits w_n while preserving a narrative record.",
            adapter_fields=_fields(w_n=False),
            tau_preserved=True,
            finite_prefix_non_precontained=False,
            source_growth_core_witness=False,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="value_completed_payload_only",
            description="A fixed value space contains the alleged future value.",
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=False,
            source_growth_core_witness=False,
            absorber_controls_supplied=False,
            value_in_fixed_completion=True,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="after_fact_family_name",
            description="Finite-prefix novelty is named by the completed realized family.",
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=True,
            source_growth_core_witness=True,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=True,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="preformed_provenance_action",
            description=(
                "The selected action, witness, and task delta are already formed "
                "before the alleged source action."
            ),
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=True,
            source_growth_core_witness=True,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=True,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="precomputed_capability_delta",
            description=(
                "The observed task-menu change is already determined by fixed "
                "source plus access or schedule."
            ),
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=False,
            source_growth_core_witness=False,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=True,
            factors_through_fixed_completion_access=True,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="taf_finality_readout_only",
            description="Finality changes readout or undo without source growth.",
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=False,
            source_growth_core_witness=False,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=True,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=False,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="imported_law_or_oracle",
            description="A hidden global table supplies the alleged source step.",
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=True,
            source_growth_core_witness=True,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=True,
            hidden_completed_oracle=True,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=True,
            concrete_trace_supplied=True,
            real_physical_candidate=False,
        ),
        CompletionBarrierCase(
            candidate_id="preaction_family_noncompletion_shape",
            description=(
                "A schematic source-growth trace has finite-prefix novelty and "
                "an internal pre-action rule excluding all admitted completion "
                "families. No concrete physical instance is supplied."
            ),
            adapter_fields=_fields(),
            tau_preserved=True,
            finite_prefix_non_precontained=True,
            source_growth_core_witness=True,
            absorber_controls_supplied=False,
            value_in_fixed_completion=False,
            name_available_after_fact=False,
            provenance_action_preformed=False,
            capability_delta_precomputed=False,
            factors_through_fixed_completion_access=False,
            taf_readout_or_finality_only=False,
            imports_external_structure=False,
            hidden_completed_oracle=False,
            experimenter_added_schema=False,
            preaction_family_noncompletion_rule=True,
            concrete_trace_supplied=False,
            real_physical_candidate=False,
        ),
    ]


def run_classifier() -> dict[str, Any]:
    cases = barrier_cases()
    results = [classify_case(case) for case in cases]
    by_id = {result.candidate_id: result for result in results}
    completion_verdicts_seen = sorted(
        {
            result.verdict
            for result in results
            if result.verdict in COMPLETION_ABSORPTION_CLASSES
        }
    )
    escape = by_id["preaction_family_noncompletion_shape"]
    return {
        "fixture_id": "whole_family_completion_barrier_classifier",
        "kind": "h1_executable_classifier_not_universal_theorem",
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "bounded_candidate_class": (
            "record-preserving Adapter_P traces with value, name, "
            "provenance/action, and capability completion channels represented"
        ),
        "adapter_fields": list(ADAPTER_FIELDS),
        "completion_absorption_classes": list(COMPLETION_ABSORPTION_CLASSES),
        "completion_absorption_classes_seen": completion_verdicts_seen,
        "all_completion_channels_exercised": (
            tuple(completion_verdicts_seen)
            == tuple(sorted(COMPLETION_ABSORPTION_CLASSES))
        ),
        "preaction_family_noncompletion_required_for_escape": (
            escape.verdict == POTENTIAL_ESCAPE_REQUIRES_OSAG
            and escape.preaction_family_noncompletion_rule
            and escape.source_growth_core_witness
            and escape.finite_prefix_non_precontained
            and not any(escape.completion_channels.values())
        ),
        "h1_result": (
            "narrowed_to_executable_classifier_and_preaction_family_"
            "noncompletion_target"
        ),
        "next_track_1_recommendation": (
            "H2 operative source-action generator with pre-action family "
            "noncompletion rule"
        ),
        "next_trigger": "research_steering_wave2_osag_preaction_family_noncompletion",
        "honest_current_result": (
            "Within the bounded Adapter_P trace class, value, name, "
            "provenance/action, and capability completion each absorb the "
            "candidate unless a pre-action family noncompletion rule is part of "
            "the source action. The only non-absorbed shape is schematic and "
            "routes to OSAG, not to a physical-source claim."
        ),
        "cases": [
            {
                "candidate_id": case.candidate_id,
                "description": case.description,
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
        default=Path(
            "tests/artifacts/"
            "whole_family_completion_barrier_classifier_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_classifier()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
