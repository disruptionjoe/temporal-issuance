#!/usr/bin/env python3
"""Candidate audit for measurement-induced phase transition claims.

The candidate is physically serious because monitored quantum dynamics can
appear to change the reachable entanglement or purification phase. This
fixture asks whether that transition is source-owned issuance or whether it
factors through a fixed dynamics family plus measurement schedule, stochastic
trajectory, and observer-access choices.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_MONITORED_DYNAMICS"
COMPLETION_WITNESS_ID = "fixed_monitored_dynamics_completion"
COMPLETION_FAMILIES = (
    "fixed_source",
    "stochastic_seed",
    "resource_capability",
    "observer_information_access",
    "completed_history",
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
    transition_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            "fixed monitored quantum circuit, Hamiltonian, or tensor-network family",
            "The physical context is real but already contains the dynamics family.",
        ),
        AdapterField(
            "Adm_n",
            False,
            "entanglement or purification phase predicate over trajectories",
            (
                "The predicate is supplied by ensemble analysis, access to "
                "measurement records, or a parameterized protocol, not generated "
                "as a new source-side admissibility law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            "measurement-induced phase transition or trajectory-class event",
            "The candidate has a concrete before/after transition signal.",
        ),
        AdapterField(
            "w_n",
            True,
            "measurement record, entropy diagnostic, or trajectory ensemble statistic",
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            "same monitored source family under a different measurement/access regime",
            (
                "The successor context is a selected or conditioned member of a "
                "fixed monitored dynamics family, not a new source law."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "preserved trajectory log and fixed-protocol comparison record",
            "Record preservation is available and is not the blocking field.",
        ),
    )


def witness_gates() -> tuple[WitnessGate, ...]:
    return (
        WitnessGate(
            "W1_non_isomorphic_source_law",
            False,
            True,
            (
                "The transition signal is real, but it is not shown to create a "
                "non-isomorphic source law rather than select among phases of a "
                "fixed monitored dynamics family."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            False,
            (
                "The admissibility predicate comes from the measurement protocol, "
                "trajectory conditioning, entropy diagnostic, or modeler's phase "
                "classification."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            False,
            (
                "The construction space is the fixed circuit or Hamiltonian plus "
                "a predeclared measurement/control schedule."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through measurement rate, random trajectory, "
                "postselection, finite-size scaling, or the fixed dynamics family."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            "Measurement outcomes and entropy/phase diagnostics can be preserved.",
        ),
        WitnessGate(
            "W6_access_history_absorption",
            False,
            False,
            (
                "Changed access to records, stochastic branches, and completed "
                "trajectory history absorbs the claimed novelty."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_monitored_dynamics_with_random_tape",
        "fixed_dynamics_family": True,
        "fixed_measurement_or_control_schedule": True,
        "stochastic_trajectory_or_born_random_tape": True,
        "postselection_or_observer_access_channel": True,
        "completed_trajectory_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_transition_law": False,
        "reason": (
            "The phase signal is reproduced by a fixed monitored dynamics family "
            "plus measurement schedule, stochastic trajectory, access/postselection, "
            "and completed-history description."
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
    nonfactorized = tuple(
        family_id
        for family_id in cc.PRIMITIVE_FAMILY_IDS
        if family_id not in set(COMPLETION_FAMILIES)
    )
    return cc.CompletionCase(
        case_id="measurement_induced_phase_transition_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=nonfactorized,
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_monitoring_transition_law",
        "required": (
            "A native physical source law in which monitoring creates a new "
            "observable, instrument, or admissibility algebra that is not "
            "representable by the fixed dynamics family, random tape, "
            "measurement schedule, postselection/access channel, finite-size "
            "scaling, or completed trajectory history."
        ),
        "also_required": (
            "A W4 perturbation non-factorization certificate under the same "
            "preserved measurement records and intervention budget."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "measurement_induced_phase_transition_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "explorations/E182-emergent-gauge-sector-candidate-v0-2026-07-16.md",
        ],
        "candidate_domain": "measurement_induced_phase_transition_monitored_quantum_dynamics",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "transition_signal_present": True,
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
            "transition law, or a theorem target showing monitored-dynamics "
            "candidates cannot supply the missing source-owned transition law"
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
            "tests/artifacts/measurement_induced_phase_transition_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
