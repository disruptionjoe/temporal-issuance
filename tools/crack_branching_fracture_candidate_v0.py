#!/usr/bin/env python3
"""Candidate audit for crack branching fracture issuance claims.

Dynamic fracture is physically serious because a loaded body can create new
crack branches, fracture surfaces, acoustic emissions, and roughness patterns
that were not present as macroscopic surfaces in the initial specimen. This
fixture asks whether that branch formation is source-owned issuance or whether
it factors through fixed elastodynamics, material microstructure, initial
defects, fracture criteria, loading, boundary conditions, stochastic disorder,
measurement access, and completed fracture history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_FRACTURE_MECHANICS"
COMPLETION_WITNESS_ID = "fixed_fracture_mechanics_completion"
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
    fracture_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed elastodynamic or phase-field fracture law, material "
                "microstructure, flaw distribution, specimen geometry, loading "
                "history, boundary conditions, initial crack, toughness and "
                "energy-release parameters, process-zone model, dissipation "
                "law, and measurement protocol"
            ),
            (
                "The physical context is real, but the law, material, flaws, "
                "loading, and admissible damage state space are fixed before "
                "the claimed crack-branching event."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            (
                "allowed crack paths, branch angles, microcrack coalescence, "
                "process-zone states, fracture-surface morphologies, and "
                "acoustic-emission events"
            ),
            (
                "The admissibility predicate is supplied by fixed fracture "
                "mechanics, material disorder, geometry, loading, and boundary "
                "data rather than generated as a new source-side rule."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "dynamic crack branching, new free-surface formation, branching "
                "network topology, acoustic emission burst, and rough fracture "
                "morphology"
            ),
            (
                "The candidate has a concrete physical formation signal and is "
                "a useful negative control for new-interface language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "crack-tip trajectory, branch map, fracture surface, stress and "
                "strain fields, load-displacement trace, acoustic emissions, "
                "high-speed images, and boundary/load records"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed fracture phase space after branch formation, "
                "damage evolution, surface exposure, measurement, or "
                "retrospective access"
            ),
            (
                "The successor context is an evolved damage state under the "
                "same predeclared fracture law, not a source-owned expansion "
                "of admissible mechanics."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            (
                "time-ordered stress-intensity, energy-release, crack-velocity, "
                "branching, acoustic-emission, fracture-surface, and loading "
                "records"
            ),
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
                "New crack surfaces and branches appear, but the state space, "
                "damage variables, material model, and governing operators "
                "remain the fixed fracture source specified in advance."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Admissible branch paths are determined by fixed material "
                "microstructure, flaws, fracture criterion, loading, boundary "
                "conditions, process-zone model, and disorder."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The realized crack network grows, but its construction space "
                "is already present in the fixed damage/fracture model and its "
                "whole-family completion."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through initial defects, material "
                "heterogeneity, loading rate, boundary conditions, toughness, "
                "process-zone parameters, stochastic disorder, measurement "
                "access, or completed fracture history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Crack-tip, branch, fracture-surface, stress, strain, load, "
                "acoustic-emission, image, and boundary records can be "
                "preserved under the fixed rival."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-source, hidden-state, initial/boundary condition, "
                "stochastic disorder, name/provenance, access, relabeling, "
                "whole-family, and completed-history absorbers are not "
                "defeated from inside the candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_fracture_mechanics_branching_model",
        "fixed_elastodynamic_or_phase_field_law": True,
        "fixed_material_microstructure": True,
        "fixed_initial_flaw_distribution": True,
        "fixed_specimen_geometry_and_boundaries": True,
        "fixed_loading_history_and_rate": True,
        "fixed_toughness_and_energy_release_criterion": True,
        "fixed_process_zone_and_dissipation_model": True,
        "stochastic_disorder_tape": True,
        "completed_fracture_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_fracture_law": False,
        "reason": (
            "The crack-branching trace is reproduced by fixed elastodynamics "
            "or phase-field fracture mechanics, material microstructure, flaw "
            "distribution, geometry, boundary conditions, loading history, "
            "fracture criterion, toughness, process-zone and dissipation "
            "model, stochastic disorder, measurement access, and completed "
            "fracture history."
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
        case_id="crack_branching_fracture_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_fracture_interface_generation_law",
        "required": (
            "A native physical source law in which fracture creates a new "
            "interface algebra, admissibility predicate, branch-selection "
            "operator, or construction space not representable as fixed "
            "elastodynamics, fixed material microstructure, fixed flaws, "
            "fixed geometry, fixed loading, fixed boundary conditions, fixed "
            "fracture criterion, stochastic disorder, observer access, or "
            "completed history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved crack-tip, branch, "
            "fracture-surface, stress, strain, load, acoustic-emission, image, "
            "and boundary records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "crack_branching_fracture_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "agent-runs/RUN-0174-turbulent-cascade-candidate-v0.md",
        ],
        "candidate_domain": "crack_branching_fracture",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "fracture_signal_present": True,
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
            "tests/artifacts/crack_branching_fracture_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
