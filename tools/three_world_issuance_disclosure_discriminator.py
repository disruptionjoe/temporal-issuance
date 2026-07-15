#!/usr/bin/env python3
"""E177 three-world issuance/disclosure discriminator.

This fixture freezes Worlds A and B as deterministic completion controls and
keeps World C fail-closed until evidence, rather than desired booleans, satisfies
the existing E172/E173 counterexample contract.  It does not establish physical
source issuance, decide D-FORK, evaluate Time as Finality capability, move claim
status, or reopen TI-C020.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import t2_bounded_completion_barrier_theorem_contract as t2


PROTOCOL_VERSION = "three_world_issuance_disclosure_discriminator_v1"

FIXED_SOURCE_DISCLOSURE = "FIXED_SOURCE_DISCLOSURE"
DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE = (
    "DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE"
)
COMPLETION_ABSORBED_NEAR_MISS = "COMPLETION_ABSORBED_NEAR_MISS"
CANDIDATE_C_INCOMPLETE = "CANDIDATE_C_INCOMPLETE"
CANDIDATE_SURVIVES_BOUNDED_DISCRIMINATOR = (
    "CANDIDATE_SURVIVES_BOUNDED_DISCRIMINATOR"
)

ADMITTED_FOR_BOUNDED_TEST = "ADMITTED_FOR_BOUNDED_TEST"
IMPORTED_STRUCTURE_REJECTED = "IMPORTED_STRUCTURE_REJECTED"
READOUT_FINALITY_REJECTED = "READOUT_FINALITY_REJECTED"
H8_DECISION_SHORTCUT_REJECTED = "H8_DECISION_SHORTCUT_REJECTED"
OBLIGATIONS_INCOMPLETE = "OBLIGATIONS_INCOMPLETE"
BOUNDED_CONTRACT_REVIEW_TRIGGERED = "BOUNDED_CONTRACT_REVIEW_TRIGGERED"

ABSORBED = "ABSORBED"
DEFEATED_VERIFIED = "DEFEATED_VERIFIED"
UNRESOLVED = "UNRESOLVED"
FACTORS_THROUGH_FIXED_FAMILY = "FACTORS_THROUGH_FIXED_FAMILY"
NONFACTORIZATION_VERIFIED = "NONFACTORIZATION_VERIFIED"
WHOLE_FAMILY_UNRESOLVED = "WHOLE_FAMILY_UNRESOLVED"
W4_INCOMPLETE = "W4_INCOMPLETE"
W5_INCOMPLETE = "W5_INCOMPLETE"
NOT_EVALUATED = "NOT_EVALUATED"
ABSENT = "ABSENT"

ADAPTER_P_FIELDS = (
    "Gamma_n",
    "Adm_n",
    "e_n",
    "w_n",
    "Gamma_n_plus_1",
    "tau_n",
)

SCHEMA_FIELDS = (
    "world_id",
    "generation_mode",
    *ADAPTER_P_FIELDS,
    "Cand_n",
    "Gen_n",
    "a_n",
    "DeltaCap_n",
    "Preserve_n",
    "represented_family_index",
    "candidate_provenance",
    "boundary_access_readout_schedule",
    "completion_family_index",
    "perturbation_evidence",
    "record_comparison",
    "noncompletion_certificates",
    "h8_shortcut_detection",
    "source_minus",
    "source_plus",
    "region_minus",
    "region_plus",
    "taf_interface",
)

PERTURBATION_IDS = (
    "P0_IDENTITY",
    "P1_INITIAL_STATE",
    "P2_GENERATOR_PARAMETER",
    "P3_ACCESS_SCHEDULE",
    "P4_OUTPUT_CHANNEL",
    "P5_NAME_PROVENANCE",
)

HOLDOUT_PERTURBATION_IDS = (
    "P3_ACCESS_SCHEDULE",
    "P4_OUTPUT_CHANNEL",
    "P5_NAME_PROVENANCE",
)

VERDICT_PRECEDENCE = (
    "SCHEMA_INVALID_OR_OUT_OF_SCOPE",
    "TERMINAL_SAFETY_REJECTION",
    FIXED_SOURCE_DISCLOSURE,
    DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE,
    COMPLETION_ABSORBED_NEAR_MISS,
    CANDIDATE_C_INCOMPLETE,
    CANDIDATE_SURVIVES_BOUNDED_DISCRIMINATOR,
)

WORLD_C_REQUIRED_FIELDS = (
    "candidate_provenance",
    "verified_adapter_p_trace",
    "verified_noncompletion_certificates",
    "w1_non_isomorphic_algebra_certificate",
    "w4_non_factorization_result",
    "w5_record_preservation_comparison",
    "whole_family_nonfactorization_certificate",
)

TAF_INTERFACE_FIELDS = (
    "region_id",
    "observer_id",
    "access_complete_shadow_fields",
    "causal_domain",
    "horizon",
    "detector_cadence",
    "M_R",
    "M_ext",
    "task_records",
    "resource_budgets",
    "external_record_holdings",
    "boundary_mode",
    "structural_equality_certificate",
    "access_complete_equality_certificate",
    "all_intervention_equality_certificate",
)

TAF_ABSORBER_IDS = (
    "readout_state",
    "description",
    "joint_record",
    "finality_state",
    "causal_domain",
    "transition_menu",
    "resource",
    "law_sector",
    "fixed_source",
)


@dataclass(frozen=True)
class AdapterPTrace:
    Gamma_n: tuple[str, ...] | None
    Adm_n: str | None
    e_n: int | None
    w_n: str | None
    Gamma_n_plus_1: tuple[str, ...] | None
    tau_n: tuple[str, ...] | None


@dataclass(frozen=True)
class SourceActionTrace:
    Cand_n: tuple[int, ...] | None
    Gen_n: str | None
    a_n: str | None
    DeltaCap_n: tuple[str, ...] | None
    Preserve_n: tuple[bool, ...] | None
    represented_family_index: str | None
    candidate_provenance: tuple[str, ...] | None


@dataclass(frozen=True)
class CompletionFamilyRow:
    row_id: str
    value: int
    name: str
    action: str
    witness: str
    tau: tuple[str, ...]
    delta_cap: tuple[str, ...]
    perturbation_traces: tuple[tuple[str, str], ...]

    def perturbation_map(self) -> dict[str, str]:
        return dict(self.perturbation_traces)


@dataclass(frozen=True)
class CompletionIndex:
    family_id: str
    rows: tuple[CompletionFamilyRow, ...]
    domain_closed: bool
    exhaustive_certificate_id: str | None


@dataclass(frozen=True)
class PerturbationResult:
    perturbation_id: str
    candidate_trace: str
    fixed_absorber_traces: tuple[tuple[str, str], ...]
    absorber_family_complete: bool
    predicted_before_readout: bool

    def exact_match_absorber_ids(self) -> tuple[str, ...]:
        return tuple(
            absorber_id
            for absorber_id, trace in self.fixed_absorber_traces
            if trace == self.candidate_trace
        )


@dataclass(frozen=True)
class RecordComparison:
    same_pre_boundary_records: bool
    candidate_growth_error: int
    fixed_source_errors: tuple[tuple[str, int], ...]
    absorber_family_complete: bool
    holdouts_predicted_before_readout: bool
    tau_n_verified: bool
    preserve_n_verified: bool


@dataclass(frozen=True)
class WorldEvidence:
    world_id: str
    declared_world_kind: str
    control_only: bool
    generation_mode: str
    adapter_p: AdapterPTrace | None
    source_action: SourceActionTrace | None
    candidate_name: str | None
    boundary_access_readout_schedule: tuple[str, ...] | None
    completion_index: CompletionIndex | None
    perturbation_evidence: tuple[PerturbationResult, ...]
    record_comparison: RecordComparison | None
    noncompletion_certificate_ids: tuple[str, ...]
    w1_certificate_id: str | None
    w4_certificate_id: str | None
    w5_certificate_id: str | None
    whole_family_nonfactorization_certificate_id: str | None
    hidden_completion_status: str
    imported_law_status: str
    readout_finality_status: str
    h8_used_as_decision: bool
    source_minus: str
    source_plus: str
    region_minus: str
    region_plus: str
    desired_boolean_inputs: tuple[tuple[str, bool], ...] = ()


def ordered_t2_obligations() -> tuple[str, ...]:
    """Import the live ordered contract instead of copying its obligations."""

    contract = t2.run_theorem_contract()
    return tuple(contract["counterexample_obligations"])


def _trace(world_id: str, perturbation_id: str, value: int) -> str:
    return f"{world_id}:{perturbation_id}:value={value}"


def _family_rows(
    world_id: str,
    generation_mode: str,
    selected_value: int,
    selected_action: str,
    selected_witness: str,
    selected_tau: tuple[str, ...],
    selected_delta_cap: tuple[str, ...],
) -> tuple[CompletionFamilyRow, ...]:
    rows: list[CompletionFamilyRow] = []
    for value in range(5):
        is_selected = value == selected_value
        action = selected_action if is_selected else f"{generation_mode}:value={value}"
        witness = selected_witness if is_selected else f"witness:value={value}"
        tau = selected_tau if is_selected else (world_id, "family", str(value))
        delta_cap = (
            selected_delta_cap if is_selected else (f"access_value_{value}",)
        )
        rows.append(
            CompletionFamilyRow(
                row_id=f"{world_id}_fixed_family_value_{value}",
                value=value,
                name=f"value_{value}",
                action=action,
                witness=witness,
                tau=tau,
                delta_cap=delta_cap,
                perturbation_traces=tuple(
                    (perturbation_id, _trace(world_id, perturbation_id, value))
                    for perturbation_id in PERTURBATION_IDS
                ),
            )
        )
    return tuple(rows)


def _perturbations(
    world_id: str,
    selected_value: int,
    rows: tuple[CompletionFamilyRow, ...],
) -> tuple[PerturbationResult, ...]:
    return tuple(
        PerturbationResult(
            perturbation_id=perturbation_id,
            candidate_trace=_trace(world_id, perturbation_id, selected_value),
            fixed_absorber_traces=tuple(
                (row.row_id, row.perturbation_map()[perturbation_id]) for row in rows
            ),
            absorber_family_complete=True,
            predicted_before_readout=True,
        )
        for perturbation_id in PERTURBATION_IDS
    )


def world_a() -> WorldEvidence:
    selected_value = 4
    action = "reveal_hidden_table_index_1"
    witness = "hidden_table[1]=4"
    tau = ("world_a", "reveal", "1", "4")
    delta_cap = ("access_value_4",)
    rows = _family_rows(
        "world_a", "reveal_preexisting", selected_value, action, witness, tau, delta_cap
    )
    return WorldEvidence(
        world_id="world_a",
        declared_world_kind="fixed_hidden_revealed_source",
        control_only=True,
        generation_mode="reveal_preexisting",
        adapter_p=AdapterPTrace(
            Gamma_n=("U=Z/5Z", "hidden_table=(1,4,2)", "visible_prefix=(1)"),
            Adm_n="membership_in_Z5",
            e_n=selected_value,
            w_n=witness,
            Gamma_n_plus_1=("U=Z/5Z", "visible_prefix=(1,4)"),
            tau_n=tau,
        ),
        source_action=SourceActionTrace(
            Cand_n=tuple(range(5)),
            Gen_n="fixed_hidden_table_reveal",
            a_n=action,
            DeltaCap_n=delta_cap,
            Preserve_n=(True, True, True),
            represented_family_index="world_a_fixed_Z5_completion_family",
            candidate_provenance=("modeler_fixed_hidden_table", "reveal_index_1"),
        ),
        candidate_name="value_4",
        boundary_access_readout_schedule=(
            "hidden_before_boundary",
            "reveal_at_step_1",
            "readout_after_boundary",
        ),
        completion_index=CompletionIndex(
            family_id="world_a_fixed_Z5_completion_family",
            rows=rows,
            domain_closed=True,
            exhaustive_certificate_id="enumerated_Z5_values_0_through_4",
        ),
        perturbation_evidence=_perturbations("world_a", selected_value, rows),
        record_comparison=RecordComparison(
            same_pre_boundary_records=True,
            candidate_growth_error=0,
            fixed_source_errors=(("world_a_fixed_source", 0),),
            absorber_family_complete=True,
            holdouts_predicted_before_readout=True,
            tau_n_verified=True,
            preserve_n_verified=True,
        ),
        noncompletion_certificate_ids=(),
        w1_certificate_id=None,
        w4_certificate_id=None,
        w5_certificate_id=None,
        whole_family_nonfactorization_certificate_id=None,
        hidden_completion_status="PRESENT",
        imported_law_status="PRESENT",
        readout_finality_status="NOT_ONLY",
        h8_used_as_decision=False,
        source_minus="fixed_source_before_reveal",
        source_plus="same_fixed_source_after_reveal",
        region_minus="observer_without_hidden_value_access",
        region_plus="observer_with_revealed_value_access",
    )


def world_b() -> WorldEvidence:
    selected_value = 2
    action = "apply_Gen_n_to_1"
    witness = "Gen_n(1)=(1^2+1)_mod_5=2"
    tau = ("world_b", "dynamic_step", "1", "2")
    delta_cap = ("access_generated_value_2",)
    rows = _family_rows(
        "world_b",
        "fixed_family_dynamics",
        selected_value,
        action,
        witness,
        tau,
        delta_cap,
    )
    return WorldEvidence(
        world_id="world_b",
        declared_world_kind="internal_dynamics_fixed_completed_family",
        control_only=True,
        generation_mode="fixed_family_dynamics",
        adapter_p=AdapterPTrace(
            Gamma_n=("U=Z/5Z", "x_n=1", "Gen_n(x)=(x^2+1)_mod_5"),
            Adm_n="membership_in_Z5_and_Gen_n_defined",
            e_n=selected_value,
            w_n=witness,
            Gamma_n_plus_1=("U=Z/5Z", "x_n_plus_1=2", "Gen_n_fixed"),
            tau_n=tau,
        ),
        source_action=SourceActionTrace(
            Cand_n=tuple(range(5)),
            Gen_n="(x^2+1)_mod_5",
            a_n=action,
            DeltaCap_n=delta_cap,
            Preserve_n=(True, True, True),
            represented_family_index="world_b_fixed_Z5_transition_family",
            candidate_provenance=("internal_rule_Gen_n", "input_1", "output_2"),
        ),
        candidate_name="value_2",
        boundary_access_readout_schedule=(
            "state_before_dynamic_step",
            "apply_Gen_n",
            "readout_after_dynamic_step",
        ),
        completion_index=CompletionIndex(
            family_id="world_b_fixed_Z5_transition_family",
            rows=rows,
            domain_closed=True,
            exhaustive_certificate_id="enumerated_Z5_transition_graph",
        ),
        perturbation_evidence=_perturbations("world_b", selected_value, rows),
        record_comparison=RecordComparison(
            same_pre_boundary_records=True,
            candidate_growth_error=0,
            fixed_source_errors=(("world_b_fixed_dynamics", 0),),
            absorber_family_complete=True,
            holdouts_predicted_before_readout=True,
            tau_n_verified=True,
            preserve_n_verified=True,
        ),
        noncompletion_certificate_ids=(),
        w1_certificate_id=None,
        w4_certificate_id=None,
        w5_certificate_id=None,
        whole_family_nonfactorization_certificate_id=None,
        hidden_completion_status="VERIFIED_ABSENT",
        imported_law_status="VERIFIED_ABSENT",
        readout_finality_status="NOT_ONLY",
        h8_used_as_decision=False,
        source_minus="fixed_dynamic_source_at_x=1",
        source_plus="same_fixed_dynamic_source_at_x=2",
        region_minus="observer_before_dynamic_step",
        region_plus="observer_after_dynamic_step",
    )


def world_c() -> WorldEvidence:
    return WorldEvidence(
        world_id="world_c",
        declared_world_kind="source_extension_candidate_interface",
        control_only=False,
        generation_mode="source_extension_candidate",
        adapter_p=None,
        source_action=None,
        candidate_name=None,
        boundary_access_readout_schedule=None,
        completion_index=None,
        perturbation_evidence=(),
        record_comparison=None,
        noncompletion_certificate_ids=(),
        w1_certificate_id=None,
        w4_certificate_id=None,
        w5_certificate_id=None,
        whole_family_nonfactorization_certificate_id=None,
        hidden_completion_status=ABSENT,
        imported_law_status=ABSENT,
        readout_finality_status=ABSENT,
        h8_used_as_decision=False,
        source_minus=ABSENT,
        source_plus=ABSENT,
        region_minus=ABSENT,
        region_plus=ABSENT,
        desired_boolean_inputs=tuple(
            (obligation, True) for obligation in ordered_t2_obligations()
        ),
    )


def adapter_fields_complete(world: WorldEvidence) -> bool:
    trace = world.adapter_p
    if trace is None:
        return False
    return all(getattr(trace, field) is not None for field in ADAPTER_P_FIELDS)


def h7_admitted(world: WorldEvidence) -> bool:
    action = world.source_action
    index = world.completion_index
    return bool(
        adapter_fields_complete(world)
        and action is not None
        and action.Preserve_n
        and all(action.Preserve_n)
        and action.represented_family_index
        and action.candidate_provenance
        and world.boundary_access_readout_schedule
        and index is not None
        and index.domain_closed
        and index.exhaustive_certificate_id
        and world.hidden_completion_status == "VERIFIED_ABSENT"
        and world.imported_law_status == "VERIFIED_ABSENT"
        and world.readout_finality_status == "NOT_ONLY"
    )


def candidate_signature(world: WorldEvidence) -> dict[str, Any] | None:
    if world.adapter_p is None or world.source_action is None:
        return None
    return {
        "value": world.adapter_p.e_n,
        "name": world.candidate_name,
        "action": world.source_action.a_n,
        "witness": world.adapter_p.w_n,
        "tau": world.adapter_p.tau_n,
        "delta_cap": world.source_action.DeltaCap_n,
        "perturbation_traces": {
            result.perturbation_id: result.candidate_trace
            for result in world.perturbation_evidence
        },
    }


def row_matches_candidate(row: CompletionFamilyRow, world: WorldEvidence) -> bool:
    signature = candidate_signature(world)
    if signature is None:
        return False
    return bool(
        row.value == signature["value"]
        and row.name == signature["name"]
        and row.action == signature["action"]
        and row.witness == signature["witness"]
        and row.tau == signature["tau"]
        and row.delta_cap == signature["delta_cap"]
        and row.perturbation_map() == signature["perturbation_traces"]
    )


def whole_family_result(world: WorldEvidence) -> tuple[str, str | None]:
    index = world.completion_index
    if index is None or not index.domain_closed or not index.exhaustive_certificate_id:
        return WHOLE_FAMILY_UNRESOLVED, None
    for row in index.rows:
        if row_matches_candidate(row, world):
            return FACTORS_THROUGH_FIXED_FAMILY, row.row_id
    if world.whole_family_nonfactorization_certificate_id:
        return (
            NONFACTORIZATION_VERIFIED,
            world.whole_family_nonfactorization_certificate_id,
        )
    return WHOLE_FAMILY_UNRESOLVED, None


def completion_channel_results(world: WorldEvidence) -> dict[str, str]:
    signature = candidate_signature(world)
    index = world.completion_index
    if signature is None or index is None or not index.domain_closed:
        return {
            "value_completion": UNRESOLVED,
            "name_completion": UNRESOLVED,
            "provenance_action_completion": UNRESOLVED,
            "capability_completion": UNRESOLVED,
        }
    rows = index.rows
    certificate_ids = set(world.noncompletion_certificate_ids)
    return {
        "value_completion": (
            ABSORBED
            if any(row.value == signature["value"] for row in rows)
            else (
                DEFEATED_VERIFIED
                if "value_completion" in certificate_ids
                else UNRESOLVED
            )
        ),
        "name_completion": (
            ABSORBED
            if any(row.name == signature["name"] for row in rows)
            else (
                DEFEATED_VERIFIED
                if "name_completion" in certificate_ids
                else UNRESOLVED
            )
        ),
        "provenance_action_completion": (
            ABSORBED
            if any(
                row.action == signature["action"]
                and row.witness == signature["witness"]
                and row.tau == signature["tau"]
                for row in rows
            )
            else (
                DEFEATED_VERIFIED
                if "provenance_action_completion" in certificate_ids
                else UNRESOLVED
            )
        ),
        "capability_completion": (
            ABSORBED
            if any(
                row.delta_cap == signature["delta_cap"]
                and row.perturbation_map() == signature["perturbation_traces"]
                for row in rows
            )
            else (
                DEFEATED_VERIFIED
                if "capability_completion" in certificate_ids
                else UNRESOLVED
            )
        ),
    }


def w4_result(world: WorldEvidence) -> bool | str:
    results = world.perturbation_evidence
    if (
        tuple(result.perturbation_id for result in results) != PERTURBATION_IDS
        or not results
        or not all(result.absorber_family_complete for result in results)
        or not all(result.predicted_before_readout for result in results)
    ):
        return W4_INCOMPLETE
    if any(result.exact_match_absorber_ids() for result in results):
        return False
    if not world.w4_certificate_id:
        return W4_INCOMPLETE
    return True


def w5_result(world: WorldEvidence) -> bool | str:
    comparison = world.record_comparison
    if comparison is None:
        return W5_INCOMPLETE
    if not comparison.fixed_source_errors:
        return W5_INCOMPLETE
    if (
        comparison.candidate_growth_error != 0
        or min(error for _, error in comparison.fixed_source_errors)
        <= comparison.candidate_growth_error
    ):
        return False
    if not world.w5_certificate_id:
        return W5_INCOMPLETE
    return bool(
        comparison.same_pre_boundary_records
        and comparison.candidate_growth_error == 0
        and comparison.absorber_family_complete
        and min(error for _, error in comparison.fixed_source_errors)
        > comparison.candidate_growth_error
        and comparison.holdouts_predicted_before_readout
        and comparison.tau_n_verified
        and comparison.preserve_n_verified
    )


def world_c_missing_fields(world: WorldEvidence) -> tuple[str, ...]:
    present = {
        "candidate_provenance": bool(
            world.source_action and world.source_action.candidate_provenance
        ),
        "verified_adapter_p_trace": adapter_fields_complete(world),
        "verified_noncompletion_certificates": len(
            world.noncompletion_certificate_ids
        )
        == 4,
        "w1_non_isomorphic_algebra_certificate": bool(world.w1_certificate_id),
        "w4_non_factorization_result": w4_result(world) is True,
        "w5_record_preservation_comparison": w5_result(world) is True,
        "whole_family_nonfactorization_certificate": bool(
            world.whole_family_nonfactorization_certificate_id
        ),
    }
    return tuple(sorted(field for field in WORLD_C_REQUIRED_FIELDS if not present[field]))


def obligation_values(world: WorldEvidence) -> dict[str, bool]:
    channels = completion_channel_results(world)
    whole_result, _ = whole_family_result(world)
    action = world.source_action
    values = {
        "new_concrete_packet": bool(
            not world.control_only and adapter_fields_complete(world)
        ),
        "h7_admitted": h7_admitted(world),
        "maps_all_adapter_p_fields": adapter_fields_complete(world),
        "preserves_tau_n": bool(world.adapter_p and world.adapter_p.tau_n),
        "preserves_preserve_n": bool(
            action and action.Preserve_n and all(action.Preserve_n)
        ),
        "preserves_represented_family_index": bool(
            action
            and action.represented_family_index
            and world.completion_index
            and action.represented_family_index == world.completion_index.family_id
        ),
        "preserves_candidate_provenance": bool(
            action and action.candidate_provenance
        ),
        "no_hidden_completion_oracle": (
            world.hidden_completion_status == "VERIFIED_ABSENT"
        ),
        "no_imported_law_or_schema": (
            world.imported_law_status == "VERIFIED_ABSENT"
        ),
        "not_readout_or_finality_only": (
            world.readout_finality_status == "NOT_ONLY"
        ),
        "defeats_value_completion": (
            channels["value_completion"] == DEFEATED_VERIFIED
        ),
        "defeats_name_completion": (
            channels["name_completion"] == DEFEATED_VERIFIED
        ),
        "defeats_provenance_action_completion": (
            channels["provenance_action_completion"] == DEFEATED_VERIFIED
        ),
        "defeats_capability_completion": (
            channels["capability_completion"] == DEFEATED_VERIFIED
        ),
        "supplies_w1_non_isomorphic_physical_algebra": bool(
            world.w1_certificate_id
        ),
        "supplies_w4_perturbation_non_factorization": w4_result(world) is True,
        "supplies_w5_record_preservation_comparison": w5_result(world) is True,
        "defeats_whole_family_completion": (
            whole_result == NONFACTORIZATION_VERIFIED
        ),
        "does_not_treat_h8_as_d_fork_decision": not world.h8_used_as_decision,
    }
    obligations = ordered_t2_obligations()
    if set(values) != set(obligations):
        raise ValueError("E177 obligation map does not match the live T2 contract")
    return {obligation: values[obligation] for obligation in obligations}


def _taf_interface(world: WorldEvidence) -> dict[str, Any]:
    interface = {field: NOT_EVALUATED for field in TAF_INTERFACE_FIELDS}
    if world.world_id == "world_a":
        interface["region_id"] = "world_a_observer_region"
        interface["observer_id"] = "world_a_observer"
        interface["access_complete_shadow_fields"] = (
            "FAIL_HIDDEN_REVEALED_ACCESS_CHANGED"
        )
        interface["access_complete_equality_certificate"] = (
            "FAIL_HIDDEN_REVEALED_ACCESS_CHANGED"
        )
    interface["absorber_statuses"] = {
        absorber_id: NOT_EVALUATED for absorber_id in TAF_ABSORBER_IDS
    }
    interface["capability_C_R_taf"] = NOT_EVALUATED
    interface["taf_interface_verdict"] = NOT_EVALUATED
    return interface


def _task_interface(world: WorldEvidence) -> dict[str, Any]:
    if world.source_action is None:
        return {
            "inputs": ABSENT,
            "allowed_operations": ABSENT,
            "target_transformation": ABSENT,
            "success_predicate": ABSENT,
            "before_result": ABSENT,
            "after_result": ABSENT,
            "cost": ABSENT,
            "provenance": ABSENT,
        }
    return {
        "inputs": list(world.adapter_p.Gamma_n) if world.adapter_p else ABSENT,
        "allowed_operations": [world.source_action.Gen_n],
        "target_transformation": world.source_action.a_n,
        "success_predicate": world.adapter_p.w_n if world.adapter_p else ABSENT,
        "before_result": world.source_minus,
        "after_result": world.source_plus,
        "cost": "dimensionless_fixture_step_1",
        "provenance": list(world.source_action.candidate_provenance or ()),
    }


def _resource_ledgers() -> dict[str, str]:
    return {
        "work": NOT_EVALUATED,
        "memory": NOT_EVALUATED,
        "control": NOT_EVALUATED,
        "transport": NOT_EVALUATED,
        "storage": NOT_EVALUATED,
        "external_resource": NOT_EVALUATED,
        "causal_path": NOT_EVALUATED,
        "boundary_forcing": NOT_EVALUATED,
    }


def classify_world(world: WorldEvidence) -> dict[str, Any]:
    obligations = obligation_values(world)
    missing_obligations = tuple(
        obligation for obligation, satisfied in obligations.items() if not satisfied
    )
    channels = completion_channel_results(world)
    whole_result, factorization_witness = whole_family_result(world)
    missing_c = world_c_missing_fields(world) if world.world_id == "world_c" else ()

    if (
        whole_result == FACTORS_THROUGH_FIXED_FAMILY
        and world.generation_mode == "reveal_preexisting"
    ):
        verdict = FIXED_SOURCE_DISCLOSURE
    elif (
        whole_result == FACTORS_THROUGH_FIXED_FAMILY
        and world.generation_mode == "fixed_family_dynamics"
    ):
        verdict = DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE
    elif any(result == ABSORBED for result in channels.values()):
        verdict = COMPLETION_ABSORBED_NEAR_MISS
    elif missing_c or missing_obligations:
        verdict = CANDIDATE_C_INCOMPLETE
    else:
        verdict = CANDIDATE_SURVIVES_BOUNDED_DISCRIMINATOR

    if world.hidden_completion_status == "PRESENT" or world.imported_law_status == "PRESENT":
        admission_verdict = IMPORTED_STRUCTURE_REJECTED
    elif world.readout_finality_status == "ONLY":
        admission_verdict = READOUT_FINALITY_REJECTED
    elif world.h8_used_as_decision:
        admission_verdict = H8_DECISION_SHORTCUT_REJECTED
    elif not missing_obligations:
        admission_verdict = BOUNDED_CONTRACT_REVIEW_TRIGGERED
    elif h7_admitted(world):
        admission_verdict = ADMITTED_FOR_BOUNDED_TEST
    else:
        admission_verdict = OBLIGATIONS_INCOMPLETE

    revision_trigger = bool(
        not world.control_only
        and not missing_c
        and not missing_obligations
        and verdict == CANDIDATE_SURVIVES_BOUNDED_DISCRIMINATOR
    )
    perturbation_rows = [
        {
            "perturbation_id": result.perturbation_id,
            "absorber_family_complete": result.absorber_family_complete,
            "predicted_before_readout": result.predicted_before_readout,
            "exact_match_absorber_ids": list(result.exact_match_absorber_ids()),
        }
        for result in world.perturbation_evidence
    ]
    comparison = world.record_comparison
    record_result = (
        {
            "same_pre_boundary_records": comparison.same_pre_boundary_records,
            "candidate_growth_error": comparison.candidate_growth_error,
            "fixed_source_errors": [list(item) for item in comparison.fixed_source_errors],
            "absorber_family_complete": comparison.absorber_family_complete,
            "holdouts_predicted_before_readout": (
                comparison.holdouts_predicted_before_readout
            ),
            "tau_n_verified": comparison.tau_n_verified,
            "preserve_n_verified": comparison.preserve_n_verified,
        }
        if comparison
        else ABSENT
    )

    return {
        "world_id": world.world_id,
        "declared_world_kind": world.declared_world_kind,
        "generation_mode": world.generation_mode,
        "verdict": verdict,
        "admission_gate_verdict": admission_verdict,
        "h7_admitted": h7_admitted(world),
        "completion_channels": channels,
        "whole_family_result": whole_result,
        "whole_family_factorization_witness": factorization_witness,
        "w1_non_isomorphic_physical_algebra": bool(world.w1_certificate_id),
        "w4_perturbation_non_factorization": w4_result(world),
        "W5_TI_record_preservation": w5_result(world),
        "W5_TAF_same_shadow_capability": NOT_EVALUATED,
        "perturbation_results": perturbation_rows,
        "record_comparison": record_result,
        "counterexample_obligation_values": obligations,
        "missing_obligations": list(missing_obligations),
        "missing_required_fields": list(missing_c),
        "desired_boolean_inputs_ignored": bool(world.desired_boolean_inputs),
        "positive_allowed": revision_trigger,
        "revision_trigger": revision_trigger,
        "source_minus": world.source_minus,
        "source_plus": world.source_plus,
        "region_minus": world.region_minus,
        "region_plus": world.region_plus,
        "boundary_access_readout_schedule": (
            list(world.boundary_access_readout_schedule)
            if world.boundary_access_readout_schedule
            else ABSENT
        ),
        "delta_cap_ti": (
            list(world.source_action.DeltaCap_n)
            if world.source_action and world.source_action.DeltaCap_n
            else ABSENT
        ),
        "capability_C_R_taf": NOT_EVALUATED,
        "identity_between_them": False,
        "cross_repo_implication_allowed": False,
        "taf_interface": _taf_interface(world),
        "taf_interface_verdict": NOT_EVALUATED,
        "task_interface": _task_interface(world),
        "resource_ledgers": _resource_ledgers(),
        "physically_forced_boundary_established": False,
        "control_only": world.control_only,
    }


def _protocol_payload() -> dict[str, Any]:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "schema_fields": list(SCHEMA_FIELDS),
        "perturbation_ids": list(PERTURBATION_IDS),
        "holdout_perturbation_ids": list(HOLDOUT_PERTURBATION_IDS),
        "counterexample_obligation_ids": list(ordered_t2_obligations()),
        "verdict_precedence": list(VERDICT_PRECEDENCE),
        "world_a_fixture": {
            "U": "Z/5Z",
            "hidden_table": [1, 4, 2],
            "visible_prefix": [1],
            "e_n": 4,
        },
        "world_b_fixture": {
            "U": "Z/5Z",
            "x_n": 1,
            "Gen_n": "(x^2+1)_mod_5",
            "e_n": 2,
        },
        "cross_repo_firewall": {
            "delta_cap_ti": "opaque_adapter_field",
            "capability_C_R_taf": NOT_EVALUATED,
            "identity_between_them": False,
            "cross_repo_implication_allowed": False,
        },
    }


def protocol_digest() -> str:
    canonical = json.dumps(
        _protocol_payload(), sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def run_discriminator() -> dict[str, Any]:
    contract = t2.run_theorem_contract()
    worlds = (world_a(), world_b(), world_c())
    decisions = [classify_world(world) for world in worlds]
    by_id = {decision["world_id"]: decision for decision in decisions}
    real_revision_triggers = [
        decision
        for decision in decisions
        if decision["revision_trigger"] and not decision["control_only"]
    ]
    return {
        "fixture_id": "three_world_issuance_disclosure_discriminator",
        "kind": "e177_fail_closed_three_world_discriminator",
        "protocol_version": PROTOCOL_VERSION,
        "protocol_digest": protocol_digest(),
        "depends_on_fixture_id": contract["fixture_id"],
        "theorem_contract_id": contract["theorem_contract_id"],
        "counterexample_obligation_ids": list(ordered_t2_obligations()),
        "schema_fields": list(SCHEMA_FIELDS),
        "perturbation_ids": list(PERTURBATION_IDS),
        "holdout_perturbation_ids": list(HOLDOUT_PERTURBATION_IDS),
        "verdict_precedence": list(VERDICT_PRECEDENCE),
        "world_a": by_id["world_a"]["verdict"],
        "world_b": by_id["world_b"]["verdict"],
        "world_c": by_id["world_c"]["verdict"],
        "world_c_positive_allowed": by_id["world_c"]["positive_allowed"],
        "real_revision_trigger_found": bool(real_revision_triggers),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "taf_capability_evaluated": False,
        "physically_forced_boundary_established": False,
        "cross_repo_implication_allowed": False,
        "e177_result": (
            "world_a_disclosure_world_b_completed_dynamics_"
            "world_c_fail_closed_incomplete"
        ),
        "honest_current_result": (
            "The implemented finite discriminator classifies the frozen A/B "
            "controls and refuses a positive World C verdict without verified "
            "evidence for every live T2 obligation. It does not establish "
            "physical source issuance or evaluate TaF capability."
        ),
        "decisions": decisions,
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "tests/artifacts/three_world_issuance_disclosure_discriminator_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_discriminator()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
