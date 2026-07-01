"""Assembly source-index absorber fixture for OnlineIssuance^LC.

The fixture tests the E112 candidate witness:

    AI_src,n undefined -> AI_src,n+1 defined

against projection access, fixed complete assembly space, modeler-added schema,
and fixed stochastic/search absorbers. A local source win here is still not a
physical Adapter_P win.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from online_issuance_physical_adapter_contract import ADAPTER_FIELDS


TARGET = "ABC"
NEXT_GATE = "oi_lc_assembly_w4_w6_physical_protocol_fixture"


@dataclass(frozen=True)
class Constructor:
    name: str
    inputs: tuple[str, ...]
    output: str
    introduced_by: str


@dataclass(frozen=True)
class AssemblyState:
    state_id: str
    seeds: tuple[str, ...]
    constructors: tuple[Constructor, ...]


@dataclass(frozen=True)
class AssemblyTrace:
    trace_id: str
    description: str
    target: str
    source_before: AssemblyState
    source_after: AssemblyState
    projection_before: AssemblyState
    projection_after: AssemblyState
    fixed_complete_source: AssemblyState | None
    source_generated_extension: bool
    modeler_added_schema: bool
    access_changed_only: bool
    fixed_search_process: bool
    no_hidden_oracle: bool
    record_preserved: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class TraceEvaluation:
    trace_id: str
    source_index_before: int | None
    source_index_after: int | None
    projection_index_before: int | None
    projection_index_after: int | None
    fixed_complete_index: int | None
    source_d4: bool
    projection_d4: bool
    absorber_results: dict[str, bool]
    source_generated_extension: bool
    no_hidden_oracle: bool
    record_preserved: bool
    assembly_source_gate_passed: bool
    adapter_witness_status: dict[str, bool]
    adapter_contract_passed: bool
    physical_source_issuance_established: bool
    verdict: str
    reason: str


def assembly_index(state: AssemblyState, target: str) -> int | None:
    """Return a minimal construction cost for target, or None if unavailable."""
    costs = {seed: 0 for seed in state.seeds}
    changed = True
    while changed:
        changed = False
        for constructor in state.constructors:
            if constructor.output in costs:
                continue
            if all(item in costs for item in constructor.inputs):
                costs[constructor.output] = 1 + sum(costs[item] for item in constructor.inputs)
                changed = True
    return costs.get(target)


def base_state(state_id: str) -> AssemblyState:
    return AssemblyState(
        state_id=state_id,
        seeds=("A", "B", "C"),
        constructors=(
            Constructor(
                name="join_ab",
                inputs=("A", "B"),
                output="AB",
                introduced_by="source_prefix",
            ),
        ),
    )


def with_source_constructor(state_id: str) -> AssemblyState:
    return AssemblyState(
        state_id=state_id,
        seeds=("A", "B", "C"),
        constructors=(
            Constructor(
                name="join_ab",
                inputs=("A", "B"),
                output="AB",
                introduced_by="source_prefix",
            ),
            Constructor(
                name="bind_c",
                inputs=("AB", "C"),
                output=TARGET,
                introduced_by="source_generated",
            ),
        ),
    )


def with_modeler_macro(state_id: str) -> AssemblyState:
    return AssemblyState(
        state_id=state_id,
        seeds=("A", "B", "C"),
        constructors=(
            Constructor(
                name="join_ab",
                inputs=("A", "B"),
                output="AB",
                introduced_by="source_prefix",
            ),
            Constructor(
                name="declare_abc",
                inputs=("A", "B", "C"),
                output=TARGET,
                introduced_by="modeler_schema",
            ),
        ),
    )


def fixture_traces() -> list[AssemblyTrace]:
    prefix = base_state("Gamma_n")
    source_plus = with_source_constructor("Gamma_n_plus_1")
    modeler_plus = with_modeler_macro("Gamma_n_plus_1_modeler")
    return [
        AssemblyTrace(
            trace_id="projection_access_negative",
            description=(
                "The projection assembly index becomes defined because access exposes an "
                "already source-constructible target."
            ),
            target=TARGET,
            source_before=source_plus,
            source_after=source_plus,
            projection_before=prefix,
            projection_after=source_plus,
            fixed_complete_source=source_plus,
            source_generated_extension=False,
            modeler_added_schema=False,
            access_changed_only=True,
            fixed_search_process=False,
            no_hidden_oracle=False,
            record_preserved=True,
            real_physical_candidate=True,
        ),
        AssemblyTrace(
            trace_id="fixed_complete_assembly_space_negative",
            description=(
                "The local prefix looks undefined, but a fixed complete assembly space "
                "already contains the target constructor."
            ),
            target=TARGET,
            source_before=prefix,
            source_after=source_plus,
            projection_before=prefix,
            projection_after=source_plus,
            fixed_complete_source=source_plus,
            source_generated_extension=True,
            modeler_added_schema=False,
            access_changed_only=False,
            fixed_search_process=False,
            no_hidden_oracle=False,
            record_preserved=True,
            real_physical_candidate=True,
        ),
        AssemblyTrace(
            trace_id="experimenter_added_schema_negative",
            description=(
                "The target becomes constructible only because the modeler introduces a "
                "macro constructor into the schema."
            ),
            target=TARGET,
            source_before=prefix,
            source_after=modeler_plus,
            projection_before=prefix,
            projection_after=modeler_plus,
            fixed_complete_source=None,
            source_generated_extension=False,
            modeler_added_schema=True,
            access_changed_only=False,
            fixed_search_process=False,
            no_hidden_oracle=True,
            record_preserved=True,
            real_physical_candidate=True,
        ),
        AssemblyTrace(
            trace_id="fixed_search_process_negative",
            description=(
                "The target is already constructible at the source layer, but a fixed search "
                "or stochastic process discovers it later."
            ),
            target=TARGET,
            source_before=source_plus,
            source_after=source_plus,
            projection_before=source_plus,
            projection_after=source_plus,
            fixed_complete_source=source_plus,
            source_generated_extension=False,
            modeler_added_schema=False,
            access_changed_only=False,
            fixed_search_process=True,
            no_hidden_oracle=False,
            record_preserved=True,
            real_physical_candidate=True,
        ),
        AssemblyTrace(
            trace_id="local_source_generated_constructor_candidate",
            description=(
                "A local source prefix lacks a construction path for the target; the successor "
                "prefix records a source-generated constructor that makes the target constructible."
            ),
            target=TARGET,
            source_before=prefix,
            source_after=source_plus,
            projection_before=prefix,
            projection_after=source_plus,
            fixed_complete_source=None,
            source_generated_extension=True,
            modeler_added_schema=False,
            access_changed_only=False,
            fixed_search_process=False,
            no_hidden_oracle=True,
            record_preserved=True,
            real_physical_candidate=False,
        ),
    ]


def evaluate_trace(trace: AssemblyTrace) -> TraceEvaluation:
    source_before = assembly_index(trace.source_before, trace.target)
    source_after = assembly_index(trace.source_after, trace.target)
    projection_before = assembly_index(trace.projection_before, trace.target)
    projection_after = assembly_index(trace.projection_after, trace.target)
    fixed_complete = (
        assembly_index(trace.fixed_complete_source, trace.target)
        if trace.fixed_complete_source is not None
        else None
    )
    source_d4 = source_before is None and source_after is not None
    projection_d4 = projection_before is None and projection_after is not None

    absorber_results = {
        "fixed_complete_assembly_space": fixed_complete is not None and source_before is None,
        "bounded_access_to_Mu_infty": (
            trace.access_changed_only
            or (projection_d4 and source_before is not None)
        ),
        "experimenter_added_schema": trace.modeler_added_schema,
        "fixed_stochastic_or_search_process": trace.fixed_search_process,
    }
    targeted_absorbers_defeated = not any(absorber_results.values())
    assembly_source_gate_passed = (
        source_d4
        and trace.source_generated_extension
        and trace.no_hidden_oracle
        and trace.record_preserved
        and targeted_absorbers_defeated
    )
    adapter_witness_status = {
        "W1_non_isomorphic_algebra": False,
        "W2_new_admissibility_predicate": assembly_source_gate_passed,
        "W3_construction_space_growth": assembly_source_gate_passed,
        "W4_perturbation_non_factorization": False,
        "W5_record_preservation": trace.record_preserved,
        "W6_gauge_access_language_absorption": targeted_absorbers_defeated
        and not trace.modeler_added_schema,
    }
    adapter_contract_passed = (
        assembly_source_gate_passed
        and adapter_witness_status["W1_non_isomorphic_algebra"]
        and adapter_witness_status["W4_perturbation_non_factorization"]
        and adapter_witness_status["W5_record_preservation"]
        and adapter_witness_status["W6_gauge_access_language_absorption"]
        and trace.real_physical_candidate
    )
    physical_source_issuance_established = adapter_contract_passed

    if assembly_source_gate_passed:
        verdict = "formal_local_source_candidate"
        reason = (
            "AI_src is undefined at n and defined at n+1 through a source-generated "
            "constructor, while the targeted assembly absorbers fail."
        )
    elif absorber_results["bounded_access_to_Mu_infty"]:
        verdict = "absorbed_projection_access"
        reason = "the novelty is projection/access disclosure from a fixed richer source"
    elif absorber_results["fixed_complete_assembly_space"]:
        verdict = "absorbed_fixed_complete_assembly_space"
        reason = "a fixed complete source already contains the target construction"
    elif absorber_results["experimenter_added_schema"]:
        verdict = "absorbed_experimenter_added_schema"
        reason = "the construction becomes available only by modeler-added schema"
    elif absorber_results["fixed_stochastic_or_search_process"]:
        verdict = "absorbed_fixed_search_process"
        reason = "the target was already constructible and was only discovered later"
    else:
        verdict = "rejected_incomplete_source_trace"
        reason = "the trace fails source D4, source generation, record preservation, or no-hidden-oracle gates"

    return TraceEvaluation(
        trace_id=trace.trace_id,
        source_index_before=source_before,
        source_index_after=source_after,
        projection_index_before=projection_before,
        projection_index_after=projection_after,
        fixed_complete_index=fixed_complete,
        source_d4=source_d4,
        projection_d4=projection_d4,
        absorber_results=absorber_results,
        source_generated_extension=trace.source_generated_extension,
        no_hidden_oracle=trace.no_hidden_oracle,
        record_preserved=trace.record_preserved,
        assembly_source_gate_passed=assembly_source_gate_passed,
        adapter_witness_status=adapter_witness_status,
        adapter_contract_passed=adapter_contract_passed,
        physical_source_issuance_established=physical_source_issuance_established,
        verdict=verdict,
        reason=reason,
    )


def run_fixture() -> dict[str, object]:
    traces = fixture_traces()
    evaluations = [evaluate_trace(trace) for trace in traces]
    by_id = {evaluation.trace_id: evaluation for evaluation in evaluations}
    local = by_id["local_source_generated_constructor_candidate"]
    absorber_negative_ids = [
        "projection_access_negative",
        "fixed_complete_assembly_space_negative",
        "experimenter_added_schema_negative",
        "fixed_search_process_negative",
    ]

    return {
        "fixture": "oi_lc_assembly_source_adapter_fixture_v0_1",
        "source_artifacts": [
            "explorations/E064-assembly-theory-d4-source-projection-operationalization-2026-06-24.md",
            "explorations/E069-fixed-source-bounded-access-negative-control-2026-06-24.md",
            "explorations/E070-source-shadow-finality-positive-fixture-2026-06-24.md",
            "explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md",
        ],
        "adapter_fields": sorted(ADAPTER_FIELDS),
        "assembly_index_definition": (
            "AI(state, x) is the minimal finite constructor cost for x from the state's "
            "seeds and constructors; None means undefined in that prefix."
        ),
        "traces": [asdict(trace) for trace in traces],
        "evaluations": [asdict(evaluation) for evaluation in evaluations],
        "adapter_mapping_for_local_candidate": {
            "Gamma_n": "source_before = local source assembly context before bind_c",
            "Adm_n": "target ABC not constructible at prefix n; bind_c admissibility is not present",
            "e_n": "source-generated constructor bind_c: (AB, C) -> ABC",
            "w_n": "computed witness AI_src,n(ABC)=undefined and AI_src,n+1(ABC)=2",
            "Gamma_n_plus_1": "source_after = successor context containing bind_c",
            "tau_n": "constructor provenance record for bind_c and computed assembly index change",
        },
        "targeted_absorber_map": {
            "fixed_complete_assembly_space": "fixed_boundary_or_holographic_completion / fixed richer source",
            "bounded_access_to_Mu_infty": "bounded_access_to_Mu_infty",
            "experimenter_added_schema": "experimenter_added_schema",
            "fixed_stochastic_or_search_process": "fixed_stochastic_or_collapse_law generalized to fixed search",
        },
        "comparisons": {
            "trace_count": len(traces),
            "assembly_index_computed": True,
            "projection_access_negative_rejected": by_id[
                "projection_access_negative"
            ].verdict
            == "absorbed_projection_access",
            "fixed_complete_assembly_space_negative_rejected": by_id[
                "fixed_complete_assembly_space_negative"
            ].verdict
            == "absorbed_fixed_complete_assembly_space",
            "experimenter_added_schema_negative_rejected": by_id[
                "experimenter_added_schema_negative"
            ].verdict
            == "absorbed_experimenter_added_schema",
            "fixed_search_process_negative_rejected": by_id[
                "fixed_search_process_negative"
            ].verdict
            == "absorbed_fixed_search_process",
            "all_negative_controls_rejected": all(
                not by_id[trace_id].assembly_source_gate_passed
                for trace_id in absorber_negative_ids
            ),
            "local_source_candidate_source_d4": local.source_d4,
            "local_source_candidate_targeted_absorbers_defeated": not any(
                local.absorber_results.values()
            ),
            "local_source_candidate_passes_assembly_source_gate": local.assembly_source_gate_passed,
            "local_source_candidate_adapter_contract_passed": local.adapter_contract_passed,
            "physical_source_issuance_established": any(
                evaluation.physical_source_issuance_established
                for evaluation in evaluations
            ),
            "TI_C020_reopened": False,
            "next_gate": NEXT_GATE,
        },
        "verdict": {
            "assembly_source_fixture_passed_formally": local.assembly_source_gate_passed,
            "selected_candidate": "assembly_theory_source_assembly_index",
            "selected_scope": "formal/local source trace, not physical evidence",
            "Issue[S]^assembly_local": local.assembly_source_gate_passed,
            "Issue[S]^physical": False,
            "TI_C020_reopened": False,
            "claim_status_change": "none",
            "best_result": (
                "The source assembly-index witness survives the targeted local absorbers: "
                "projection disclosure, fixed complete assembly space, modeler-added schema, "
                "and fixed search are rejected by controls. The surviving trace is formal/local "
                "only and lacks W1 plus W4 physical perturbation non-factorization."
            ),
            "next_gate": NEXT_GATE,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the Assembly source-index Adapter_P absorber fixture."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_fixture()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
