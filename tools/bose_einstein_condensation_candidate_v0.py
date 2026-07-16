#!/usr/bin/env python3
"""Candidate audit for Bose-Einstein condensation issuance claims.

Bose-Einstein condensation is physically serious because a macroscopic coherent
mode appears when a bosonic gas crosses a critical regime. This fixture asks
whether that event is source-owned issuance or whether it factors through a
fixed many-body Hamiltonian, bosonic field algebra, Fock-space completion, trap
geometry, interaction strength, cooling path, reservoir, boundary conditions,
symmetry-breaking seed, measurement protocol, and completed condensation
history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_MANY_BODY_HAMILTONIAN"
COMPLETION_WITNESS_ID = "fixed_many_body_condensate_completion"
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
    condensation_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed many-body Hamiltonian, bosonic field algebra, particle "
                "species, trap geometry, interaction strength, cooling "
                "trajectory, reservoir, boundary conditions, and symmetry-"
                "breaking seed"
            ),
            (
                "The physical context is real, but the candidate's field "
                "algebra, Fock-space completion, interactions, reservoir, and "
                "cooling schedule are frozen before the claimed condensation "
                "event."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            (
                "allowed condensate occupation, coherence, and order-parameter "
                "states induced by the fixed Hamiltonian and ensemble"
            ),
            (
                "The admissibility predicate is supplied by the fixed many-body "
                "model, thermodynamic ensemble, particle-number sector, and "
                "cooling path rather than generated as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "macroscopic ground-state occupation, phase coherence, or "
                "off-diagonal long-range-order transition below critical "
                "temperature"
            ),
            (
                "The candidate has a concrete physical formation signal and is "
                "a useful negative control for macroscopic-order language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "density profile, time-of-flight interference, condensate "
                "fraction, coherence function, temperature, and cooling trace"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed bosonic field algebra and Fock-space completion "
                "after occupation, order-parameter selection, or measurement "
                "access"
            ),
            (
                "The successor context is a populated or phase-coherent state "
                "inside the fixed many-body theory, not a source-owned new "
                "mode algebra or admissibility law."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "time-ordered cooling, occupation, coherence, and measurement history",
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
                "Macroscopic occupation appears, but the bosonic field algebra, "
                "Fock space, particle species, and mode basis remain the fixed "
                "source specified in advance."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Condensate admissibility is defined by the fixed Hamiltonian, "
                "ensemble, trap, interaction strength, and cooling protocol."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "Condensate occupation and coherence grow, but the construction "
                "space is already present in the Fock-space or grand-canonical "
                "completion."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through trap geometry, scattering length, "
                "particle number or reservoir, cooling trajectory, finite-size "
                "effects, initial seed, measurement access, stochastic "
                "fluctuation tape, or completed condensation history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Density, interference, coherence, condensate-fraction, "
                "temperature, and cooling records can be preserved under the "
                "fixed rival."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-source, hidden-state, initial/boundary condition, "
                "stochastic fluctuation, name/provenance, access, relabeling, "
                "whole-family, and completed-history absorbers are not "
                "defeated from inside the candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_many_body_bec_model",
        "fixed_many_body_hamiltonian": True,
        "fixed_bosonic_field_algebra": True,
        "fixed_particle_species_and_fock_space": True,
        "fixed_trap_geometry": True,
        "fixed_interaction_strength": True,
        "fixed_cooling_trajectory_and_reservoir": True,
        "stochastic_seed_or_thermal_fluctuation_tape": True,
        "completed_condensation_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_condensate_law": False,
        "reason": (
            "The condensate trace is reproduced by a fixed many-body "
            "Hamiltonian, bosonic field algebra, Fock-space completion, trap "
            "geometry, interaction strength, cooling trajectory, reservoir, "
            "boundary conditions, seed fluctuations, measurement access, and "
            "completed condensation history."
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
        case_id="bose_einstein_condensation_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_condensate_mode_generation_law",
        "required": (
            "A native physical source law in which condensation creates a new "
            "mode algebra, admissibility predicate, transition grammar, or "
            "construction space not representable as fixed many-body "
            "Hamiltonian, fixed Fock-space completion, fixed trap geometry, "
            "fixed interaction strength, fixed reservoir/cooling path, "
            "stochastic fluctuation, observer access, or completed history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved density, interference, "
            "coherence, condensate-fraction, temperature, and cooling records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "bose_einstein_condensation_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "agent-runs/RUN-0171-schwinger-pair-production-candidate-v0.md",
        ],
        "candidate_domain": "bose_einstein_condensation",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "condensation_signal_present": True,
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
            "tests/artifacts/bose_einstein_condensation_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
