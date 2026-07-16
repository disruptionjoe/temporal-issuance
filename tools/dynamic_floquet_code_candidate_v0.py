#!/usr/bin/env python3
"""Candidate audit for dynamic/Floquet quantum-code logical qubit claims.

The candidate is physically serious because a time-periodic measurement or
gauge schedule can make logical structure appear during the run even when the
instantaneous static code description has no protected logical qubit. This
fixture asks whether that logical-sector appearance is source-owned issuance
or whether it factors through a fixed Hilbert space, stabilizer/gauge family,
control schedule, decoder, boundary data, and completed syndrome history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_CODE_SCHEDULE"
COMPLETION_WITNESS_ID = "fixed_floquet_code_schedule_completion"
COMPLETION_FAMILIES = (
    "boundary_condition",
    "fixed_source",
    "stochastic_seed",
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
    logical_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed physical qubit Hilbert space, stabilizer/gauge checks, "
                "noise model, boundary conditions, and time-periodic measurement schedule"
            ),
            (
                "The physical context is real, but the code family and schedule "
                "are already present before the claimed logical appearance."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            "logical-sector admissibility induced by the predeclared schedule and decoder",
            (
                "The admissibility predicate is supplied by the fixed schedule, "
                "gauge/stabilizer constraints, and decoder rather than generated "
                "as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            "time-scheduled appearance of a logical qubit or protected subsystem",
            (
                "The candidate has a concrete code-dynamics signal and a useful "
                "negative-control shape."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            "syndrome history, logical operator support, decoder transcript, and record trace",
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            "same fixed code family after one period or after decoder-visible access changes",
            (
                "The successor context is a scheduled member of the fixed code "
                "family, not a source-owned new construction grammar."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "period-by-period syndrome and logical-support record",
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
                "A logical algebra appears relative to a time slice or decoder, "
                "but it is represented by the fixed physical algebra plus the "
                "predeclared stabilizer/gauge schedule."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Logical admissibility is defined by the schedule, boundary, "
                "syndrome constraints, and decoder, all of which are fixed in the rival."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The protected subsystem may be absent in an instantaneous static "
                "description and present over a period, but the construction space "
                "is the fixed circuit and measurement family."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through schedule phase, boundary choice, "
                "decoder access, noise seed, gauge fixing, or completed syndrome history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Syndrome histories, logical support, and decoder transcripts can "
                "be preserved under the frozen comparison contract."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-family, schedule, resource/access, relabeling/gauge, and "
                "completed-history absorbers are not defeated from inside the code."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_floquet_code_schedule",
        "fixed_physical_hilbert_space": True,
        "fixed_stabilizer_or_gauge_family": True,
        "fixed_time_periodic_measurement_schedule": True,
        "fixed_boundary_and_initialization_data": True,
        "fixed_decoder_and_logical_readout_rule": True,
        "noise_or_syndrome_random_tape": True,
        "completed_syndrome_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_code_law": False,
        "reason": (
            "The logical-sector appearance is reproduced by one fixed physical "
            "Hilbert space and stabilizer/gauge family under a fixed time-periodic "
            "schedule, boundary data, decoder/readout rule, noise or syndrome tape, "
            "and completed syndrome history."
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
        case_id="dynamic_floquet_code_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=nonfactorized,
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_code_space_generation_law",
        "required": (
            "A native physical source law in which the code source creates a new "
            "admissibility predicate, logical algebra, or construction grammar not "
            "representable as fixed Hilbert space, fixed stabilizer/gauge family, "
            "fixed time-periodic schedule, boundary data, decoder/readout access, "
            "noise or syndrome random tape, or completed syndrome history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved syndrome, logical-support, "
            "boundary, and decoder records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "dynamic_floquet_code_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md",
            "explorations/E185-crispr-spacer-acquisition-candidate-v0-2026-07-16.md",
        ],
        "candidate_domain": "dynamic_floquet_quantum_code_logical_qubit_generation",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "logical_sector_signal_present": True,
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
            "transition law, or a bounded no-go target for scheduled-code "
            "logical-sector candidates under fixed Hilbert-space completion"
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
        default=Path("tests/artifacts/dynamic_floquet_code_candidate_v0_result.json"),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
