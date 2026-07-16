#!/usr/bin/env python3
"""Candidate audit for prion-like conformational templating claims.

The candidate is physically serious because a seed conformer can propagate a
stable strain and create a phenotype-level trace without changing the protein
sequence. This fixture asks whether that conformational branch is source-owned
issuance or whether it factors through a fixed sequence, conformational energy
landscape, environment, seed, stochastic collision tape, and completed folding
history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_CONFORMATIONAL_LANDSCAPE"
COMPLETION_WITNESS_ID = "fixed_conformational_landscape_completion"
COMPLETION_FAMILIES = (
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
    conformation_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed amino-acid sequence, solvent and temperature conditions, "
                "chaperone/proteostasis context, and conformational energy landscape"
            ),
            (
                "The physical context is real, but the sequence, environment, "
                "and folding landscape are fixed before the claimed strain branch."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            "admissible conformers and strain labels induced by the fixed landscape",
            (
                "The admissibility predicate is supplied by the fixed folding "
                "landscape, seed conformer, boundary conditions, and assay labels "
                "rather than generated as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            "seeded templating event that propagates a stable conformational strain",
            (
                "The candidate has a concrete physical formation signal and is a "
                "useful negative control for phenotype-level novelty."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            "folding trajectory, strain assay, aggregate morphology, and lineage record",
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed sequence and conformational landscape after seeded "
                "templating or observer-visible strain selection"
            ),
            (
                "The successor context is a realized basin or branch of the fixed "
                "landscape, not a source-owned new construction grammar."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "time-ordered propagation and phenotype trace",
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
                "A strain algebra appears relative to seeded propagation and "
                "assay labels, but it is represented by the fixed molecular "
                "state space plus conformational landscape."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Admissible conformers are defined by the sequence, environment, "
                "seed, chaperone context, and assay convention already present "
                "in the rival."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The phenotype or strain branch may be absent before seeding and "
                "present after propagation, but the construction space is the "
                "fixed conformational landscape and stochastic folding path."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through seed choice, solvent, temperature, "
                "chaperone access, stochastic collision history, assay readout, "
                "or completed folding lineage."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Propagation records, strain assays, morphology, and lineage "
                "traces can be preserved under the frozen comparison contract."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-landscape, initial-condition, boundary, stochastic, "
                "name/provenance, access, relabeling, whole-family, and "
                "completed-history absorbers are not defeated from inside the "
                "candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_conformational_landscape",
        "fixed_amino_acid_sequence": True,
        "fixed_conformational_energy_landscape": True,
        "fixed_solvent_temperature_and_chaperone_context": True,
        "seed_conformer_as_initial_condition": True,
        "stochastic_collision_or_folding_tape": True,
        "assay_and_strain_labeling_rule": True,
        "completed_folding_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_conformation_law": False,
        "reason": (
            "The strain-branch trace is reproduced by one fixed protein sequence "
            "and conformational landscape under fixed environment/chaperone "
            "conditions, a seed conformer, stochastic folding history, assay "
            "labeling, and completed lineage records."
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
        case_id="prion_conformation_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=nonfactorized,
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_conformational_grammar_expansion_law",
        "required": (
            "A native physical source law in which seeded propagation creates a "
            "new admissibility predicate, conformational grammar, or molecular "
            "state algebra not representable as fixed sequence, fixed "
            "conformational landscape, fixed environment/chaperone context, "
            "seed initial condition, stochastic folding tape, assay label, or "
            "completed folding history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved strain, morphology, "
            "lineage, and phenotype records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "prion_conformation_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md",
            "explorations/E186-dynamic-floquet-code-candidate-v0-2026-07-16.md",
        ],
        "candidate_domain": "prion_like_conformational_templating_and_strain_branching",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "conformation_signal_present": True,
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
        default=Path("tests/artifacts/prion_conformation_candidate_v0_result.json"),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
