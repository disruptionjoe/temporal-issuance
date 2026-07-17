#!/usr/bin/env python3
"""Candidate audit for turbulent cascade issuance claims.

Turbulence is physically serious because a driven flow develops coherent
vortices, intermittent bursts, and scale-to-scale energy transfer not visible
in a smooth initial state. This fixture asks whether that cascade is
source-owned issuance or whether it factors through fixed fluid equations,
fluid parameters, forcing, boundary and initial conditions, Reynolds-number
regime, closure family, stochastic perturbation tape, measurement protocol, and
completed flow history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_NAVIER_STOKES_CASCADE"
COMPLETION_WITNESS_ID = "fixed_fluid_cascade_completion"
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
    turbulence_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed Navier-Stokes or Euler equations, fluid density, "
                "viscosity, domain geometry, boundary conditions, initial "
                "velocity and vorticity field, forcing schedule, Reynolds "
                "number regime, injection scale, dissipation scale, closure "
                "family, and measurement protocol"
            ),
            (
                "The physical context is real, but the equations, parameters, "
                "driving, and admissible state space are fixed before the "
                "claimed turbulent cascade event."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            (
                "allowed eddy modes, triad interactions, inertial-range "
                "transfer paths, coherent vortices, intermittency structures, "
                "and dissipation channels"
            ),
            (
                "The admissibility predicate is supplied by the fixed fluid "
                "law, forcing, boundary data, and closure assumptions rather "
                "than generated as a new source-side rule."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "vortex stretching, energy cascade, inertial-range spectrum, "
                "coherent structures, intermittency bursts, and dissipation "
                "anomaly"
            ),
            (
                "The candidate has a concrete physical formation signal and "
                "is a useful negative control for emergent-structure language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "velocity field snapshots, vorticity records, pressure "
                "records, energy spectrum, structure functions, dissipation "
                "rate, forcing record, and boundary measurements"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed fluid phase space after nonlinear cascade, "
                "coherent-structure identification, measurement, or "
                "retrospective access"
            ),
            (
                "The successor context is an evolved state of the same "
                "predeclared fluid law, not a source-owned expansion of the "
                "admissible dynamics."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            (
                "time-ordered velocity, vorticity, pressure, forcing, "
                "energy-transfer, and dissipation records"
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
                "A turbulent field develops new visible structures, but the "
                "phase space, variables, symmetries, and governing operators "
                "remain the fixed fluid source specified in advance."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Admissible eddy interactions and cascade paths are determined "
                "by fixed equations, forcing, boundary data, viscosity, "
                "Reynolds regime, and closure assumptions."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The realized multiscale structure grows, but the construction "
                "space is already present in the fixed nonlinear state space "
                "and its whole-family completion."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through initial and boundary conditions, "
                "forcing, viscosity, Reynolds number, closure choice, "
                "stochastic fluctuations, measurement access, or completed "
                "flow history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Velocity, vorticity, pressure, spectrum, structure-function, "
                "dissipation, forcing, and boundary records can be preserved "
                "under the fixed rival."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-source, hidden-state, initial/boundary condition, "
                "stochastic perturbation, name/provenance, access, relabeling, "
                "whole-family, and completed-history absorbers are not "
                "defeated from inside the candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_fluid_dynamics_cascade_model",
        "fixed_governing_equations": True,
        "fixed_fluid_parameters": True,
        "fixed_domain_and_boundary_conditions": True,
        "fixed_initial_conditions": True,
        "fixed_forcing_and_energy_injection": True,
        "fixed_reynolds_regime_and_scale_window": True,
        "fixed_subgrid_or_closure_family": True,
        "stochastic_perturbation_tape": True,
        "completed_flow_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_cascade_law": False,
        "reason": (
            "The turbulent cascade trace is reproduced by fixed fluid "
            "equations, fluid parameters, domain and boundary conditions, "
            "initial state, forcing and energy injection, Reynolds regime, "
            "scale window, closure family, measurement access, stochastic "
            "perturbations, and completed flow history."
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
        case_id="turbulent_cascade_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_cascade_rule_generation_law",
        "required": (
            "A native physical source law in which turbulence creates a new "
            "eddy-mode algebra, admissibility predicate, transfer operator, "
            "or construction space not representable as fixed fluid equations, "
            "fixed fluid parameters, fixed forcing, fixed boundary and initial "
            "conditions, fixed Reynolds regime, fixed closure family, "
            "stochastic perturbation, observer access, or completed history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved velocity, vorticity, "
            "pressure, spectrum, structure-function, dissipation, forcing, "
            "and boundary records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "turbulent_cascade_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "agent-runs/RUN-0173-r-process-nucleosynthesis-candidate-v0.md",
        ],
        "candidate_domain": "turbulent_cascade",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "turbulence_signal_present": True,
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
        default=Path("tests/artifacts/turbulent_cascade_candidate_v0_result.json"),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
