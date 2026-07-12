#!/usr/bin/env python3
"""Bounded OSAG pre-action family noncompletion constructor.

This Wave 2 artifact answers the H2 question left by the H1 classifier. It
constructs only a formal/local bounded OSAG shape. It does not establish
physical source issuance and it does not move claim status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BOUNDED_OSAG_CONSTRUCTED = "BOUNDED_OSAG_CONSTRUCTED"
FAMILY_COMPLETION_ABSORPTION = "FAMILY_COMPLETION_ABSORPTION"
AFTER_FACT_SINGLETON_REJECTION = "AFTER_FACT_SINGLETON_REJECTION"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE = "OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE"
NEEDS_CONCRETE_ADMISSION_CONTRACT = "NEEDS_CONCRETE_ADMISSION_CONTRACT"

ADAPTER_FIELDS = (
    "Gamma_n",
    "Adm_n",
    "Cand_n",
    "Gen_n",
    "a_n",
    "w_n",
    "Gamma_n_plus_1",
    "DeltaCap_n",
    "tau_n",
    "Preserve_n",
    "AAN_family",
)


@dataclass(frozen=True)
class CompletionFamily:
    family_id: str
    channel: str
    represented_at_stage: bool
    covers_candidate_preaction: bool
    covers_candidate_after_action: bool
    imported_oracle: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "family_id": self.family_id,
            "channel": self.channel,
            "represented_at_stage": self.represented_at_stage,
            "covers_candidate_preaction": self.covers_candidate_preaction,
            "covers_candidate_after_action": self.covers_candidate_after_action,
            "imported_oracle": self.imported_oracle,
        }


@dataclass(frozen=True)
class OSAGCase:
    case_id: str
    description: str
    adapter_fields: dict[str, bool]
    gamma_n: tuple[str, ...]
    adm_n: tuple[str, ...]
    cand_n: tuple[str, ...]
    gen_n: str
    action_token: str
    witness_token: str
    gamma_n_plus_1: tuple[str, ...]
    delta_cap_n: tuple[str, ...]
    tau_n_preserved: bool
    preserve_n: tuple[str, ...]
    completion_families: tuple[CompletionFamily, ...]
    preaction_family_rule: bool
    internal_generator: bool
    hidden_completed_oracle: bool
    imported_law: bool
    after_fact_singleton: bool
    finite_prefix_non_precontained: bool
    source_growth_witness: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class OSAGResult:
    case_id: str
    verdict: str
    terminal: bool
    adapter_fields_mapped: bool
    tau_n_preserved: bool
    preaction_family_rule: bool
    internally_generated: bool
    family_noncompletion_holds: bool
    finite_prefix_non_precontained: bool
    source_growth_witness: bool
    real_physical_candidate: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "adapter_fields_mapped": self.adapter_fields_mapped,
            "tau_n_preserved": self.tau_n_preserved,
            "preaction_family_rule": self.preaction_family_rule,
            "internally_generated": self.internally_generated,
            "family_noncompletion_holds": self.family_noncompletion_holds,
            "finite_prefix_non_precontained": self.finite_prefix_non_precontained,
            "source_growth_witness": self.source_growth_witness,
            "real_physical_candidate": self.real_physical_candidate,
            "reason": self.reason,
        }


def _fields(all_mapped: bool = True, **overrides: bool) -> dict[str, bool]:
    fields = {field: all_mapped for field in ADAPTER_FIELDS}
    fields.update(overrides)
    return fields


def all_adapter_fields_mapped(case: OSAGCase) -> bool:
    return all(case.adapter_fields.get(field, False) for field in ADAPTER_FIELDS)


def represented_preaction_completion(case: OSAGCase) -> list[CompletionFamily]:
    return [
        family
        for family in case.completion_families
        if family.represented_at_stage and family.covers_candidate_preaction
    ]


def imported_completion_source(case: OSAGCase) -> bool:
    return case.imported_law or case.hidden_completed_oracle or any(
        family.imported_oracle for family in case.completion_families
    )


def family_noncompletion_holds(case: OSAGCase) -> bool:
    return (
        case.preaction_family_rule
        and case.internal_generator
        and not represented_preaction_completion(case)
        and not imported_completion_source(case)
        and not case.after_fact_singleton
    )


def classify_case(case: OSAGCase) -> OSAGResult:
    adapter_ok = all_adapter_fields_mapped(case)
    noncompletion = family_noncompletion_holds(case)

    if not adapter_ok or not case.tau_n_preserved:
        verdict = OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
        terminal = False
        reason = "The candidate does not preserve tau_n and map all OSAG/Adapter_P fields."
    elif imported_completion_source(case):
        verdict = IMPORTED_STRUCTURE_REJECTION
        terminal = True
        reason = (
            "The apparent AAN_family rule is imported from a hidden completion "
            "oracle, external law, or externally supplied family table."
        )
    elif case.after_fact_singleton:
        verdict = AFTER_FACT_SINGLETON_REJECTION
        terminal = True
        reason = (
            "The family exclusion is created after the action by singleton naming, "
            "so it is not a pre-action family noncompletion rule."
        )
    elif represented_preaction_completion(case):
        verdict = FAMILY_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "At least one represented completion family already covers the "
            "candidate before the alleged source action."
        )
    elif (
        noncompletion
        and case.finite_prefix_non_precontained
        and case.source_growth_witness
    ):
        verdict = BOUNDED_OSAG_CONSTRUCTED
        terminal = False
        reason = (
            "The bounded formal/local OSAG shape constructs the candidate from "
            "present rules while excluding all represented pre-action completion "
            "families. This is not a physical-source claim."
        )
    else:
        verdict = NEEDS_CONCRETE_ADMISSION_CONTRACT
        terminal = False
        reason = (
            "The case is not absorbed by a terminal control, but it lacks a "
            "complete internal OSAG preservation/admission contract."
        )

    return OSAGResult(
        case_id=case.case_id,
        verdict=verdict,
        terminal=terminal,
        adapter_fields_mapped=adapter_ok,
        tau_n_preserved=case.tau_n_preserved,
        preaction_family_rule=case.preaction_family_rule,
        internally_generated=case.internal_generator and not imported_completion_source(case),
        family_noncompletion_holds=noncompletion,
        finite_prefix_non_precontained=case.finite_prefix_non_precontained,
        source_growth_witness=case.source_growth_witness,
        real_physical_candidate=case.real_physical_candidate,
        reason=reason,
    )


def osag_cases() -> list[OSAGCase]:
    fixed_value_family = CompletionFamily(
        family_id="fixed_value_completion",
        channel="value",
        represented_at_stage=True,
        covers_candidate_preaction=True,
        covers_candidate_after_action=True,
    )
    after_fact_name_family = CompletionFamily(
        family_id="after_fact_name_completion",
        channel="name",
        represented_at_stage=True,
        covers_candidate_preaction=False,
        covers_candidate_after_action=True,
    )
    preformed_action_family = CompletionFamily(
        family_id="preformed_action_completion",
        channel="provenance_action",
        represented_at_stage=True,
        covers_candidate_preaction=True,
        covers_candidate_after_action=True,
    )
    capability_schedule_family = CompletionFamily(
        family_id="capability_schedule_completion",
        channel="capability",
        represented_at_stage=True,
        covers_candidate_preaction=True,
        covers_candidate_after_action=True,
    )
    imported_oracle_family = CompletionFamily(
        family_id="hidden_global_completion_oracle",
        channel="imported",
        represented_at_stage=True,
        covers_candidate_preaction=False,
        covers_candidate_after_action=True,
        imported_oracle=True,
    )
    represented_noncovering_families = (
        CompletionFamily(
            family_id="value_family_checked",
            channel="value",
            represented_at_stage=True,
            covers_candidate_preaction=False,
            covers_candidate_after_action=False,
        ),
        CompletionFamily(
            family_id="name_family_checked",
            channel="name",
            represented_at_stage=True,
            covers_candidate_preaction=False,
            covers_candidate_after_action=True,
        ),
        CompletionFamily(
            family_id="provenance_action_family_checked",
            channel="provenance_action",
            represented_at_stage=True,
            covers_candidate_preaction=False,
            covers_candidate_after_action=False,
        ),
        CompletionFamily(
            family_id="capability_family_checked",
            channel="capability",
            represented_at_stage=True,
            covers_candidate_preaction=False,
            covers_candidate_after_action=False,
        ),
    )

    common = {
        "gamma_n": ("stage_n", "adm_family_index", "generator_rule"),
        "adm_n": ("candidate_from_present_rules", "no_hidden_oracle"),
        "cand_n": ("diag_candidate_family_rule",),
        "gen_n": "present_family_diagonal_generator",
        "action_token": "a_osag",
        "witness_token": "w_family_noncompletion",
        "gamma_n_plus_1": (
            "stage_n",
            "adm_family_index",
            "generator_rule",
            "diag_candidate_family_rule",
        ),
        "delta_cap_n": ("distinguish_preaction_family_noncompletion",),
        "preserve_n": (
            "tau_n",
            "represented_completion_family_index",
            "candidate_provenance",
        ),
        "preaction_family_rule": True,
        "internal_generator": True,
        "hidden_completed_oracle": False,
        "imported_law": False,
        "after_fact_singleton": False,
        "finite_prefix_non_precontained": True,
        "source_growth_witness": True,
        "real_physical_candidate": False,
    }

    return [
        OSAGCase(
            case_id="bounded_internal_osag",
            description=(
                "A finite represented family index is checked before action, and "
                "the candidate is generated from present rules with no pre-action "
                "family coverage."
            ),
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=represented_noncovering_families,
            **common,
        ),
        OSAGCase(
            case_id="fixed_value_precompletion",
            description="A fixed value family already contains the candidate.",
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=(fixed_value_family,),
            **common,
        ),
        OSAGCase(
            case_id="preformed_action_completion",
            description="The action and witness are already preformed.",
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=(preformed_action_family,),
            **common,
        ),
        OSAGCase(
            case_id="capability_schedule_completion",
            description="The capability delta is already scheduled by fixed source plus access.",
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=(capability_schedule_family,),
            **common,
        ),
        OSAGCase(
            case_id="after_fact_singleton_name",
            description="The apparent exclusion is created after the action by naming the result.",
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=(after_fact_name_family,),
            after_fact_singleton=True,
            **{key: value for key, value in common.items() if key != "after_fact_singleton"},
        ),
        OSAGCase(
            case_id="hidden_completion_oracle",
            description="A hidden global oracle supplies the family table.",
            adapter_fields=_fields(),
            tau_n_preserved=True,
            completion_families=(imported_oracle_family,),
            hidden_completed_oracle=True,
            **{key: value for key, value in common.items() if key != "hidden_completed_oracle"},
        ),
        OSAGCase(
            case_id="missing_preserve_field",
            description="The candidate omits Preserve_n and cannot be evaluated as OSAG.",
            adapter_fields=_fields(Preserve_n=False),
            tau_n_preserved=True,
            completion_families=represented_noncovering_families,
            **common,
        ),
    ]


def run_constructor() -> dict[str, Any]:
    cases = osag_cases()
    results = [classify_case(case) for case in cases]
    by_id = {result.case_id: result for result in results}
    constructed = by_id["bounded_internal_osag"]
    return {
        "fixture_id": "osag_preaction_family_noncompletion",
        "kind": "h2_bounded_formal_local_osag_constructor",
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "adapter_fields": list(ADAPTER_FIELDS),
        "osag_tuple": list(ADAPTER_FIELDS),
        "h2_result": "bounded_osag_shape_constructed_formal_local",
        "bounded_osag_constructed": constructed.verdict == BOUNDED_OSAG_CONSTRUCTED,
        "preaction_family_noncompletion_rule_generated_internal": (
            constructed.preaction_family_rule
            and constructed.internally_generated
            and constructed.family_noncompletion_holds
        ),
        "fixed_completion_absorbed": any(
            result.verdict == FAMILY_COMPLETION_ABSORPTION for result in results
        ),
        "after_fact_singleton_rejected": (
            by_id["after_fact_singleton_name"].verdict
            == AFTER_FACT_SINGLETON_REJECTION
        ),
        "imported_oracle_rejected": (
            by_id["hidden_completion_oracle"].verdict == IMPORTED_STRUCTURE_REJECTION
        ),
        "adapter_preservation_checked": (
            by_id["missing_preserve_field"].verdict == OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
        ),
        "honest_current_result": (
            "A bounded formal/local OSAG shape can be constructed over a finite "
            "represented completion-family index. The result only shows how H1's "
            "pre-action family noncompletion target can be represented without "
            "after-fact singleton naming or hidden global completion. It does not "
            "establish a physical source action."
        ),
        "next_track_1_recommendation": (
            "H7 completion-aware Adapter_P admission contract, then H9/H5 "
            "calibration against concrete physical and multi-holder cases"
        ),
        "cases": [
            {
                "case_id": case.case_id,
                "description": case.description,
                "completion_families": [
                    family.as_dict() for family in case.completion_families
                ],
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
        default=Path("tests/artifacts/osag_preaction_family_noncompletion_result.json"),
    )
    args = parser.parse_args()
    result = run_constructor()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
