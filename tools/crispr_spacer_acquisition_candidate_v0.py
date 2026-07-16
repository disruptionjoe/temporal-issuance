#!/usr/bin/env python3
"""Candidate audit for native CRISPR spacer acquisition claims.

The candidate is physically serious because a host lineage acquires a durable
genomic spacer record through endogenous Cas adaptation machinery. This
fixture asks whether that event is source-owned issuance or whether it factors
through fixed biochemical law, sequence space, environmental boundary input,
stochastic encounter, and completed-history description.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_BIOCHEMICAL_SEQUENCE_SPACE"
COMPLETION_WITNESS_ID = "fixed_biochemical_sequence_space_completion"
COMPLETION_FAMILIES = (
    "initial_condition",
    "boundary_condition",
    "fixed_source",
    "stochastic_seed",
    "name_provenance",
    "whole_family",
    "completed_history",
    "observer_information_access",
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
    formation_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "host lineage genome, CRISPR array, Cas adaptation machinery, "
                "nucleotide chemistry, and phage/plasmid exposure context"
            ),
            "The physical context is real but already contains the adaptation machinery.",
        ),
        AdapterField(
            "Adm_n",
            False,
            "protospacer, PAM, processing, integration, and survival predicate",
            (
                "The admissibility predicate is supplied by fixed Cas machinery, "
                "sequence chemistry, and environmental encounter conditions rather "
                "than generated as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            "new spacer insertion into the CRISPR array",
            "The candidate has a concrete before/after genomic formation trace.",
        ),
        AdapterField(
            "w_n",
            True,
            "sequenced spacer record, integration locus, and immunity phenotype",
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            "same biochemical source with one additional nucleotide record",
            (
                "The successor context is an occupied member of a fixed sequence "
                "and recombination family, not a source-owned new construction grammar."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "lineage before/after sequence trace and exposure record",
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
                "A new spacer record appears, but the source algebra remains fixed "
                "nucleotide chemistry plus fixed CRISPR/Cas adaptation operations."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Spacer admissibility is governed by pre-existing protospacer, PAM, "
                "processing, integration, and selection predicates."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The occupied sequence is new to the lineage record, but the larger "
                "nucleotide sequence and insertion family is fixed in advance."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through protospacer availability, Cas expression, "
                "integration bias, repair chemistry, selection, and stochastic encounter."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            "The spacer insertion and downstream immunity record can be preserved.",
        ),
        WitnessGate(
            "W6_fixed_sequence_space_after_naming_absorption",
            False,
            False,
            (
                "Fixed sequence-space, whole-family, boundary-input, and after-naming "
                "absorbers are not defeated from inside the biology."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_crispr_biochemical_sequence_space",
        "fixed_nucleotide_sequence_space": True,
        "fixed_cas_adaptation_machinery": True,
        "fixed_recombination_and_repair_chemistry": True,
        "environmental_boundary_sequence_input": True,
        "stochastic_encounter_or_integration_seed": True,
        "selection_or_survival_filter": True,
        "completed_lineage_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_transition_law": False,
        "reason": (
            "The acquired spacer is reproduced by fixed biochemical law and Cas "
            "machinery over a fixed nucleotide sequence space, with environmental "
            "boundary input, stochastic encounter/integration, selection, and a "
            "completed lineage trace."
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
        case_id="crispr_spacer_acquisition_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=nonfactorized,
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_biochemical_admissibility_expansion_law",
        "required": (
            "A native physical source law in which the biological source creates a "
            "new admissibility predicate or construction grammar not representable "
            "as fixed nucleotide sequence space, fixed Cas adaptation machinery, "
            "environmental boundary input, stochastic encounter, selection, or "
            "completed lineage history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved sequence, exposure, "
            "lineage, and immunity records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "crispr_spacer_acquisition_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md",
            "explorations/E184-crossed-product-gravitational-algebra-candidate-v0-2026-07-16.md",
        ],
        "candidate_domain": "native_crispr_spacer_acquisition",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "formation_record_signal_present": True,
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
            "transition law, or a bounded no-go target for biological sequence "
            "acquisition candidates under fixed sequence-space completion"
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
        default=Path("tests/artifacts/crispr_spacer_acquisition_candidate_v0_result.json"),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
