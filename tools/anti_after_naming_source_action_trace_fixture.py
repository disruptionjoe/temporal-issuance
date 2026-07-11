#!/usr/bin/env python3
"""Anti-after-naming source-action trace fixture.

This fixture tries to instantiate the positive shape left by E161. It asks
whether a C-derived transport trace can block singleton after-naming internally
by using a stage-stratified diagonal successor rule.

The result is formal/local only. It is not a physical Adapter_P witness and it
does not move claim status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS = (
    "CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS"
)
SCHEMATIC_ONLY_NOT_INSTANTIATED = "SCHEMATIC_ONLY_NOT_INSTANTIATED"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
FIXED_SOURCE_DISCLOSURE = "FIXED_SOURCE_DISCLOSURE"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
SINGLETON_AFTER_NAMING_ABSORBED = "SINGLETON_AFTER_NAMING_ABSORBED"
BLOCKED_INCONSISTENT_TRANSPORT = "BLOCKED_INCONSISTENT_TRANSPORT"


@dataclass(frozen=True)
class TraceCase:
    trace_id: str
    description: str
    stage_names: tuple[str, ...]
    after_fact_names: tuple[str, ...]
    selected_continuation: str | None
    continuation_rule: str
    c_transport_value: int | None
    transport_functorial: bool
    task_menu_before: tuple[str, ...]
    task_menu_after: tuple[str, ...]
    region_supported: bool
    source_growth_witness: bool
    stage_stratified_anti_after_naming: bool
    taf_can_express_task_delta: bool
    factors_through_fixed_completion_access: bool
    imports_external_structure: bool
    schematic_only: bool = False


@dataclass(frozen=True)
class TraceResult:
    trace_id: str
    verdict: str
    terminal: bool
    selected_continuation: str | None
    capability_delta: tuple[str, ...]
    prior_name_absorbs: bool
    after_fact_singleton_absorbs: bool
    internal_diagonal_witness: bool
    source_action_trace_candidate: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "selected_continuation": self.selected_continuation,
            "capability_delta": list(self.capability_delta),
            "prior_name_absorbs": self.prior_name_absorbs,
            "after_fact_singleton_absorbs": self.after_fact_singleton_absorbs,
            "internal_diagonal_witness": self.internal_diagonal_witness,
            "source_action_trace_candidate": self.source_action_trace_candidate,
            "reason": self.reason,
        }


def diagonal_successor(names: tuple[str, ...]) -> str:
    """Return a deterministic name not present in the stage-present names."""

    base = "diag__" + "__".join(sorted(names))
    candidate = base or "diag__empty"
    while candidate in names:
        candidate = candidate + "_next"
    return candidate


def task_delta(case: TraceCase) -> tuple[str, ...]:
    before = set(case.task_menu_before)
    return tuple(sorted(task for task in case.task_menu_after if task not in before))


def has_internal_diagonal_witness(case: TraceCase) -> bool:
    return (
        case.continuation_rule == "stage_diagonal"
        and case.selected_continuation == diagonal_successor(case.stage_names)
    )


def classify_trace(case: TraceCase) -> TraceResult:
    delta = task_delta(case)
    selected = case.selected_continuation
    prior_name_absorbs = selected in case.stage_names if selected is not None else False
    after_fact_contains_selected = (
        selected in case.after_fact_names if selected is not None else False
    )
    internal_diagonal = has_internal_diagonal_witness(case)
    after_fact_absorbs = (
        after_fact_contains_selected
        and not case.stage_stratified_anti_after_naming
    )

    if not case.transport_functorial:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=BLOCKED_INCONSISTENT_TRANSPORT,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason="Transport labels fail functorial composition.",
        )

    if case.imports_external_structure:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=IMPORTED_STRUCTURE_REJECTION,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason="The continuation or transport is supplied by an external oracle/table.",
        )

    if case.factors_through_fixed_completion_access:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=FIXED_SOURCE_DISCLOSURE,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason="The task change factors through fixed completion plus access.",
        )

    if case.taf_can_express_task_delta:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=TAF_EXPRESSIBLE_READOUT,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason="The task delta is readout/capability expressible.",
        )

    if case.schematic_only or selected is None or not delta:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=SCHEMATIC_ONLY_NOT_INSTANTIATED,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason="The positive shape is named but not instantiated as a trace.",
        )

    if prior_name_absorbs or after_fact_absorbs:
        return TraceResult(
            trace_id=case.trace_id,
            verdict=SINGLETON_AFTER_NAMING_ABSORBED,
            terminal=True,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=after_fact_absorbs,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=False,
            reason=(
                "The continuation is available to the stage-present names or "
                "is absorbed by after-fact singleton naming without an internal "
                "stage-stratification guard."
            ),
        )

    if (
        case.c_transport_value == 1
        and case.region_supported
        and case.source_growth_witness
        and case.stage_stratified_anti_after_naming
        and internal_diagonal
    ):
        return TraceResult(
            trace_id=case.trace_id,
            verdict=CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS,
            terminal=False,
            selected_continuation=selected,
            capability_delta=delta,
            prior_name_absorbs=prior_name_absorbs,
            after_fact_singleton_absorbs=False,
            internal_diagonal_witness=internal_diagonal,
            source_action_trace_candidate=True,
            reason=(
                "The trace uses a stage-present-name diagonal successor, a "
                "nontrivial C-derived transport value, and a stage-stratified "
                "anti-after-naming guard. It escapes the E161 local controls, "
                "but remains formal/local and requires full Adapter_P pressure."
            ),
        )

    return TraceResult(
        trace_id=case.trace_id,
        verdict=SCHEMATIC_ONLY_NOT_INSTANTIATED,
        terminal=True,
        selected_continuation=selected,
        capability_delta=delta,
        prior_name_absorbs=prior_name_absorbs,
        after_fact_singleton_absorbs=after_fact_absorbs,
        internal_diagonal_witness=internal_diagonal,
        source_action_trace_candidate=False,
        reason="The trace lacks at least one required E161 positive-shape field.",
    )


def fixture_cases() -> list[TraceCase]:
    base_menu = ("read_base_record",)
    stage_names = ("alpha", "beta")
    diagonal = diagonal_successor(stage_names)
    return [
        TraceCase(
            trace_id="e161_readout_sector",
            description="E161 sector distinction remains a readout/capability fact.",
            stage_names=stage_names,
            after_fact_names=stage_names + ("sector_1",),
            selected_continuation="sector_1",
            continuation_rule="readout_sector",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("distinguish_loop_sector",),
            region_supported=True,
            source_growth_witness=False,
            stage_stratified_anti_after_naming=False,
            taf_can_express_task_delta=True,
            factors_through_fixed_completion_access=False,
            imports_external_structure=False,
        ),
        TraceCase(
            trace_id="fixed_source_access_trace",
            description="The selected continuation is disclosed from fixed access.",
            stage_names=stage_names,
            after_fact_names=stage_names + ("gamma",),
            selected_continuation="gamma",
            continuation_rule="fixed_access",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("select_disclosed_continuation",),
            region_supported=True,
            source_growth_witness=False,
            stage_stratified_anti_after_naming=False,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=True,
            imports_external_structure=False,
        ),
        TraceCase(
            trace_id="imported_oracle_novel_name",
            description="An external oracle supplies a continuation not in stage names.",
            stage_names=stage_names,
            after_fact_names=stage_names + ("oracle_delta",),
            selected_continuation="oracle_delta",
            continuation_rule="imported_oracle",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("select_unprecontained_continuation",),
            region_supported=True,
            source_growth_witness=True,
            stage_stratified_anti_after_naming=True,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imports_external_structure=True,
        ),
        TraceCase(
            trace_id="unguarded_diagonal_singleton_absorbed",
            description="A diagonal-looking continuation lacks the stage guard.",
            stage_names=stage_names,
            after_fact_names=stage_names + (diagonal,),
            selected_continuation=diagonal,
            continuation_rule="stage_diagonal",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("select_unprecontained_continuation",),
            region_supported=True,
            source_growth_witness=True,
            stage_stratified_anti_after_naming=False,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imports_external_structure=False,
        ),
        TraceCase(
            trace_id="stage_stratified_diagonal_trace",
            description=(
                "A concrete formal trace selects the stage-diagonal successor "
                "and blocks after-fact naming by stage stratification."
            ),
            stage_names=stage_names,
            after_fact_names=stage_names + (diagonal,),
            selected_continuation=diagonal,
            continuation_rule="stage_diagonal",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu
            + (
                "certify_stage_prior_unavailability",
                "select_unprecontained_continuation",
            ),
            region_supported=True,
            source_growth_witness=True,
            stage_stratified_anti_after_naming=True,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imports_external_structure=False,
        ),
        TraceCase(
            trace_id="verbal_guard_no_trace",
            description="The anti-after-naming guard is asserted but no continuation is built.",
            stage_names=stage_names,
            after_fact_names=stage_names,
            selected_continuation=None,
            continuation_rule="verbal_guard",
            c_transport_value=1,
            transport_functorial=True,
            task_menu_before=base_menu,
            task_menu_after=base_menu,
            region_supported=True,
            source_growth_witness=False,
            stage_stratified_anti_after_naming=True,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imports_external_structure=False,
            schematic_only=True,
        ),
        TraceCase(
            trace_id="inconsistent_transport_trace",
            description="Transport label composition fails before source action is testable.",
            stage_names=stage_names,
            after_fact_names=stage_names + ("bad_delta",),
            selected_continuation="bad_delta",
            continuation_rule="stage_diagonal",
            c_transport_value=1,
            transport_functorial=False,
            task_menu_before=base_menu,
            task_menu_after=base_menu + ("select_unprecontained_continuation",),
            region_supported=True,
            source_growth_witness=True,
            stage_stratified_anti_after_naming=True,
            taf_can_express_task_delta=False,
            factors_through_fixed_completion_access=False,
            imports_external_structure=False,
        ),
    ]


def run_fixture() -> dict[str, Any]:
    results = [classify_trace(case) for case in fixture_cases()]
    by_id = {result.trace_id: result for result in results}
    positive = by_id["stage_stratified_diagonal_trace"]
    return {
        "fixture_id": "anti_after_naming_source_action_trace_fixture",
        "kind": "formal_local_trace_fixture_not_claim_movement",
        "claim_status_change": "none",
        "active_trigger_change": "recommend_full_adapter_p_pressure",
        "central_question": (
            "Can the E161 positive anti-after-naming source-action shape be "
            "instantiated as a concrete formal/local trace?"
        ),
        "e161_positive_shape_instantiated": positive.source_action_trace_candidate,
        "concrete_formal_source_action_trace_found": positive.source_action_trace_candidate,
        "physical_source_action_found": False,
        "next_trigger_recommendation": (
            "full_adapter_p_pressure_on_stage_stratified_diagonal_trace"
        ),
        "honest_current_result": (
            "A stage-stratified diagonal trace instantiates the E161 positive "
            "shape at the formal/local level and escapes the local readout, "
            "fixed-access, imported-structure, and singleton-after-naming controls. "
            "It is not physical evidence and still needs full Adapter_P pressure."
        ),
        "verdicts_seen": sorted({result.verdict for result in results}),
        "traces": [result.as_dict() for result in results],
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
            "anti_after_naming_source_action_trace_fixture_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
