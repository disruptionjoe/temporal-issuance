#!/usr/bin/env python3
"""Candidate audit for Schwinger vacuum pair-production claims.

Pair production is physically serious because particle number appears to grow
from the vacuum in a strong external field. This fixture asks whether that
event is source-owned issuance or whether it factors through a fixed QFT
Lagrangian, charged field content, background field profile, boundary
conditions, vacuum state, renormalization scheme, measurement protocol, and
completed field history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_QFT_BACKGROUND"
COMPLETION_WITNESS_ID = "fixed_qft_background_completion"
COMPLETION_FAMILIES = (
    "hidden_state",
    "initial_condition",
    "boundary_condition",
    "fixed_source",
    "stochastic_seed",
    "name_provenance",
    "resource_capability",
    "whole_family",
    "completed_history",
    "observer_information_access",
    "relabel_gauge",
)


@dataclass(frozen=True)
class AdapterField:
    field_id: str
    supplied: bool
    value: str
    finding: str


@dataclass(frozen=True)
class WitnessGate:
    gate_id: str
    source_passed: bool
    pair_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed QFT Lagrangian, charged field content, background "
                "electric-field profile, boundary conditions, vacuum state, "
                "and renormalization scheme"
            ),
            (
                "The physical context is real, but the candidate's field "
                "algebra, couplings, external field, and vacuum preparation "
                "are frozen before the claimed pair-production event."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            "admissible pair modes induced by the fixed QFT and background field",
            (
                "The admissibility predicate is supplied by the fixed field "
                "equations, spectrum, boundary, and external-field profile "
                "rather than generated as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "nonzero pair-production amplitude or occupation-number "
                "transition under a supercritical external field"
            ),
            (
                "The candidate has a concrete physical formation signal and "
                "is a useful negative control for vacuum-production language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "detector counts, mode occupation record, field-strength trace, "
                "energy budget, and retarded response"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed QFT sector after mode occupation, detector access, "
                "or completed field-history naming"
            ),
            (
                "The successor context is a populated state in the fixed theory, "
                "not a source-owned new field algebra or admissibility law."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "time-ordered background-field, occupation, and detector history",
            "Record preservation is available and is not the blocking field.",
        ),
    )


def witness_gates() -> tuple[WitnessGate, ...]:
    return (
        WitnessGate(
            "W1_non_isomorphic_source_algebra",
            False,
            True,
            (
                "Particle number changes, but the field algebra and charged "
                "sector remain the fixed QFT source specified in advance."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Pair modes are admissible because the fixed equations and "
                "background profile already define the allowed transitions."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "Occupation grows from the vacuum, but the construction space "
                "is fixed by the Lagrangian, field content, boundary, and "
                "external field."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through field strength, pulse shape, "
                "boundary conditions, vacuum preparation, coupling constants, "
                "renormalization scheme, measurement access, or completed "
                "field history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Detector counts, occupation records, field profile, and "
                "energy accounting can be preserved under the fixed rival."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-source, hidden-state, initial/boundary condition, "
                "stochastic vacuum amplitude, name/provenance, access, "
                "relabeling, whole-family, and completed-history absorbers "
                "are not defeated from inside the candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_qft_background_field",
        "fixed_lagrangian": True,
        "fixed_charged_field_content": True,
        "fixed_background_field_profile": True,
        "fixed_boundary_conditions": True,
        "fixed_vacuum_state": True,
        "fixed_couplings_and_renormalization": True,
        "stochastic_vacuum_amplitude_or_mode_tape": True,
        "completed_field_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_field_law": False,
        "reason": (
            "The pair-production trace is reproduced by a fixed QFT Lagrangian, "
            "charged field content, external field profile, boundary conditions, "
            "vacuum preparation, coupling and renormalization choices, detector "
            "access, and completed field history."
        ),
    }


def completion_case() -> cc.CompletionCase:
    witness = cc.CompletionWitness(
        witness_id=COMPLETION_WITNESS_ID,
        family_ids=COMPLETION_FAMILIES,
        predeclared=True,
        outcome_independent=True,
        physically_admissible=True,
        reproduces_joint_trace=True,
        preserves_comparison_contract=True,
        quotient_respecting=True,
        certificate_verified=True,
    )
    return cc.CompletionCase(
        case_id="schwinger_pair_production_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_field_algebra_expansion_law",
        "required": (
            "A native physical source law in which the pair-production event "
            "creates a new field algebra, charged sector, admissibility "
            "predicate, or transition grammar not representable as fixed QFT "
            "Lagrangian, fixed background field profile, fixed boundary "
            "condition, fixed vacuum state, stochastic amplitude, observer "
            "access, or completed field history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved detector, occupation, "
            "field-strength, energy, and retarded-response records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "schwinger_pair_production_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "agent-runs/RUN-0170-autocatalytic-reaction-network-candidate-v0.md",
        ],
        "candidate_domain": "schwinger_vacuum_pair_production",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "pair_production_signal_present": True,
        "source_growth_core_passed": any(gate.source_passed for gate in gates[:3]),
        "absorber_controls_passed": all(gate.source_passed for gate in gates[3:]),
        "fixed_source_rival": fixed_source_rival(),
        "completion_class_version": "completion_class_v1",
        "completion_class_verdict": completion_decision["verdict"],
        "valid_completion_witness_ids": completion_decision["valid_witness_ids"],
        "absorbed_family_ids": completion_decision["absorbed_family_ids"],
        "unresolved_family_ids": completion_decision["unresolved_family_ids"],
        "missing_family_ids": completion_decision["missing_family_ids"],
        "composition_closure_declared": completion_decision[
            "composition_closure_declared"
        ],
        "exact_missing_source_object": missing_source_object(),
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "claim_status_change": "none",
        "E177_modified": False,
        "cross_repo_implication": False,
        "next_required_test": (
            "another non-overlapping physical candidate with a source-owned "
            "transition law, or a bounded no-go target only after the tested "
            "candidate families justify a scoped class statement"
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "tests/artifacts/schwinger_pair_production_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
