#!/usr/bin/env python3
"""Capability-transport source-action fixture.

This bounded toy fixture follows E160's transport derivation result into the
E119 capability burden. It asks whether a C-derived transport value changes a
region-indexed task menu in a way that is not already TaF-style capability
readout, fixed-source disclosure, imported structure, or class-relative formal
residue.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


NO_CAPABILITY_DELTA = "NO_CAPABILITY_DELTA"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
FIXED_SOURCE_DISCLOSURE = "FIXED_SOURCE_DISCLOSURE"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
CLASS_RELATIVE_FORMAL_RESIDUE = "CLASS_RELATIVE_FORMAL_RESIDUE"
SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P = (
    "SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P"
)
BLOCKED_INCONSISTENT_TRANSPORT = "BLOCKED_INCONSISTENT_TRANSPORT"
NEEDS_CONCRETE_TRACE = "NEEDS_CONCRETE_TRACE"


@dataclass(frozen=True)
class CapabilityTransportCase:
    case_id: str
    description: str
    transport_origin: str
    functorial_transport: bool
    derived_from_c: bool
    nontrivial_transport: bool
    region_supported: bool
    task_menu_before: tuple[str, ...]
    task_menu_after: tuple[str, ...]
    taf_can_express_task_delta: bool
    factors_through_fixed_completion_access: bool
    imported_structure: bool
    singleton_after_naming_absorbs: bool
    internal_anti_after_naming_principle: bool
    source_growth_core_witness: bool
    schematic_only: bool = False


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    verdict: str
    terminal: bool
    capability_delta: tuple[str, ...]
    derived_from_c: bool
    nontrivial_transport: bool
    source_action_candidate: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "capability_delta": list(self.capability_delta),
            "derived_from_c": self.derived_from_c,
            "nontrivial_transport": self.nontrivial_transport,
            "source_action_candidate": self.source_action_candidate,
            "reason": self.reason,
        }


def task_delta(case: CapabilityTransportCase) -> tuple[str, ...]:
    before = set(case.task_menu_before)
    return tuple(sorted(task for task in case.task_menu_after if task not in before))


def classify_case(case: CapabilityTransportCase) -> CaseResult:
    delta = task_delta(case)

    if not case.functorial_transport:
        return CaseResult(
            case_id=case.case_id,
            verdict=BLOCKED_INCONSISTENT_TRANSPORT,
            terminal=True,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "The transport labels do not respect extension composition, so "
                "there is no functorial action to test."
            ),
        )

    if case.imported_structure:
        return CaseResult(
            case_id=case.case_id,
            verdict=IMPORTED_STRUCTURE_REJECTION,
            terminal=True,
            capability_delta=delta,
            derived_from_c=False,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "The task delta depends on a transport table, boundary datum, "
                "or law supplied outside C-typed admissibility."
            ),
        )

    if case.factors_through_fixed_completion_access:
        return CaseResult(
            case_id=case.case_id,
            verdict=FIXED_SOURCE_DISCLOSURE,
            terminal=True,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "The task delta is modeled as fixed completed source plus a "
                "changed access/readout aperture."
            ),
        )

    if not case.derived_from_c or not case.nontrivial_transport or not delta:
        return CaseResult(
            case_id=case.case_id,
            verdict=NO_CAPABILITY_DELTA,
            terminal=True,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "The case supplies no nontrivial C-derived transport that changes "
                "the region-indexed task menu."
            ),
        )

    if not case.region_supported:
        return CaseResult(
            case_id=case.case_id,
            verdict=NEEDS_CONCRETE_TRACE,
            terminal=False,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "A transport value is present, but the changed task is not tied "
                "to a supported region or observer."
            ),
        )

    if case.taf_can_express_task_delta:
        return CaseResult(
            case_id=case.case_id,
            verdict=TAF_EXPRESSIBLE_READOUT,
            terminal=True,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "The nontrivial C-derived transport creates a task-menu handle, "
                "but the handle is expressible as a capability/readout fact "
                "rather than a TI source-crossing action."
            ),
        )

    if (
        case.singleton_after_naming_absorbs
        and not case.internal_anti_after_naming_principle
    ):
        return CaseResult(
            case_id=case.case_id,
            verdict=CLASS_RELATIVE_FORMAL_RESIDUE,
            terminal=True,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=False,
            reason=(
                "Finite-prefix nontriviality survives, but the realized family "
                "is absorbed by after-the-fact singleton naming."
            ),
        )

    if (
        case.source_growth_core_witness
        and case.internal_anti_after_naming_principle
        and not case.singleton_after_naming_absorbs
    ):
        return CaseResult(
            case_id=case.case_id,
            verdict=SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P,
            terminal=False,
            capability_delta=delta,
            derived_from_c=case.derived_from_c,
            nontrivial_transport=case.nontrivial_transport,
            source_action_candidate=True,
            reason=(
                "This is the positive shape: a nontrivial C-derived transport "
                "changes a supported task menu while carrying an internal "
                "anti-after-naming principle. It still needs a full Adapter_P "
                "trace before any claim movement."
            ),
        )

    return CaseResult(
        case_id=case.case_id,
        verdict=NEEDS_CONCRETE_TRACE,
        terminal=False,
        capability_delta=delta,
        derived_from_c=case.derived_from_c,
        nontrivial_transport=case.nontrivial_transport,
        source_action_candidate=False,
        reason=(
            "The case has a transport/capability interaction, but it lacks the "
            "structure needed to decide source action versus readout."
        ),
    )


def fixture_cases() -> list[CapabilityTransportCase]:
    base_menu = ("read_base_record",)
    return [
        CapabilityTransportCase(
            case_id="bare_loop_no_transport",
            description="A bare extension loop supplies no transport value.",
            transport_origin="none",
            functorial_transport=True,
            derived_from_c=False,
            nontrivial_transport=False,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        CapabilityTransportCase(
            case_id="identity_transport_trivial_capability",
            description="A consistency rule derives only identity transport.",
            transport_origin="c_consistency_identity",
            functorial_transport=True,
            derived_from_c=True,
            nontrivial_transport=False,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        CapabilityTransportCase(
            case_id="c_typed_parity_sector_readout",
            description=(
                "E160-style C-typed parity derives a nontrivial sector label "
                "that lets the holder distinguish the loop sector."
            ),
            transport_origin="c_delta_z2",
            functorial_transport=True,
            derived_from_c=True,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("distinguish_loop_sector",),
            taf_can_express_task_delta=True,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        CapabilityTransportCase(
            case_id="fixed_access_reveals_sector",
            description=(
                "The same sector task appears because access to a fixed richer "
                "source widens."
            ),
            transport_origin="fixed_source_access",
            functorial_transport=True,
            derived_from_c=False,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("distinguish_loop_sector",),
            taf_can_express_task_delta=True,
            factors_through_fixed_completion_access=True,
            imported_structure=False,
            singleton_after_naming_absorbs=True,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        CapabilityTransportCase(
            case_id="imported_transport_sector_task",
            description=(
                "A nontrivial sector task is obtained from an imported transport "
                "table."
            ),
            transport_origin="imported_transport_table",
            functorial_transport=True,
            derived_from_c=False,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("distinguish_loop_sector",),
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=True,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        CapabilityTransportCase(
            case_id="c_typed_prefix_family_singleton_absorbed",
            description=(
                "C-derived finite-prefix transport affects continuation choice, "
                "but the completed realized family is singleton-absorbed."
            ),
            transport_origin="c_delta_prefix_family",
            functorial_transport=True,
            derived_from_c=True,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("select_sector_conditioned_continuation",),
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=True,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=True,
        ),
        CapabilityTransportCase(
            case_id="anti_after_naming_source_action_shape",
            description=(
                "Schematic positive shape with C-derived transport, source "
                "growth, and an internal anti-after-naming principle."
            ),
            transport_origin="c_delta_z2_with_internal_anti_after_naming",
            functorial_transport=True,
            derived_from_c=True,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu
            + (
                "select_unprecontained_continuation",
                "certify_not_after_named",
            ),
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=True,
            source_growth_core_witness=True,
            schematic_only=True,
        ),
        CapabilityTransportCase(
            case_id="inconsistent_c_transport_labels",
            description="C labels exist but fail functorial transport composition.",
            transport_origin="inconsistent_c_delta_z2",
            functorial_transport=False,
            derived_from_c=True,
            nontrivial_transport=True,
            region_supported=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("distinguish_loop_sector",),
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imported_structure=False,
            singleton_after_naming_absorbs=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
    ]


def run_fixture() -> dict[str, Any]:
    results = [classify_case(case) for case in fixture_cases()]
    by_id = {result.case_id: result for result in results}
    e160_case = by_id["c_typed_parity_sector_readout"]
    positive_shape = by_id["anti_after_naming_source_action_shape"]

    return {
        "fixture_id": "capability_transport_source_action_fixture",
        "kind": "bounded_toy_fixture_not_claim_movement",
        "claim_status_change": "none",
        "active_trigger_change": "none",
        "central_question": (
            "Does E160-style C-derived transport become an E119-style "
            "capability-changing source action?"
        ),
        "e160_transport_has_capability_delta": bool(e160_case.capability_delta),
        "e160_transport_becomes_source_action": e160_case.source_action_candidate,
        "e160_transport_verdict": e160_case.verdict,
        "positive_source_action_shape_stateable": (
            positive_shape.verdict
            == SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P
        ),
        "real_source_action_found": False,
        "honest_current_result": (
            "The E160 C-derived parity transport creates a task-menu handle, "
            "but the concrete handle is still expressible as capability/readout. "
            "A real TI source-action trace would additionally need source growth "
            "and an internal anti-after-naming principle."
        ),
        "next_action": (
            "Do not promote holonomy or TI-C019. Future work should only proceed "
            "if a concrete trace fills the positive anti-after-naming source-action "
            "shape, or if the schematic shape is turned into a full Adapter_P fixture."
        ),
        "verdicts_seen": sorted({result.verdict for result in results}),
        "cases": [result.as_dict() for result in results],
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
            "capability_transport_source_action_fixture_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
