#!/usr/bin/env python3
"""Candidate audit for autocatalytic chemical reaction-network claims.

The candidate is physically serious because autocatalytic closure can make a
chemical system look as if new productive possibilities have appeared inside
the process. This fixture asks whether that network-emergence signal is
source-owned issuance or whether it factors through a fixed reaction graph,
fixed rate laws, feedstock boundary, catalyst inventory, stochastic collision
tape, and completed reaction history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_REACTION_NETWORK"
COMPLETION_WITNESS_ID = "fixed_reaction_network_completion"
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
    network_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed molecular species alphabet, reaction graph, catalyst "
                "inventory, rate laws, feedstock reservoir, and reactor boundary"
            ),
            (
                "The chemical context is real, but the candidate's species, "
                "reaction rules, catalysis map, rates, and boundary are fixed "
                "before the claimed autocatalytic closure."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            "admissible reactions induced by the fixed graph and rate-law table",
            (
                "The admissibility predicate is supplied by the predeclared "
                "reaction grammar, catalysts, feedstock, and kinetic law rather "
                "than generated as a new source-side chemical law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "threshold crossing where a catalyst-supported subset becomes "
                "self-sustaining under the fixed feedstock and rate laws"
            ),
            (
                "The candidate has a concrete formation signal and is a useful "
                "negative control for adjacent-possible or origin-of-life language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "species abundance trace, reaction events, catalytic closure "
                "certificate, flux record, and perturbation response"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed reaction network after concentration threshold, "
                "path selection, or observer-visible catalytic closure"
            ),
            (
                "The successor context is a realized attractor or subset of the "
                "fixed reaction system, not a source-owned new reaction grammar."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "time-ordered reaction and abundance history",
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
                "A self-sustaining catalytic subset appears, but it is a subgraph "
                "or attractor of the fixed species and reaction algebra."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Reaction admissibility is defined by the frozen molecular "
                "alphabet, catalyst map, rate-law table, feedstock, and boundary."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The autocatalytic set may be absent below threshold and present "
                "above it, but the construction space is the fixed reaction graph "
                "plus concentrations and stochastic collision history."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through feedstock, boundary flux, rate "
                "constants, catalyst seeding, random collision tape, or completed "
                "reaction history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Abundance traces, flux records, closure certificates, and "
                "perturbation responses can be preserved under the frozen "
                "comparison contract."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-network, initial-condition, boundary, stochastic, "
                "name/provenance, access, relabeling, whole-family, and "
                "completed-history absorbers are not defeated from inside the "
                "candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_reaction_network",
        "fixed_species_alphabet": True,
        "fixed_reaction_graph": True,
        "fixed_catalyst_inventory": True,
        "fixed_rate_law_table": True,
        "fixed_feedstock_and_boundary_flux": True,
        "seed_concentrations_as_initial_condition": True,
        "stochastic_collision_or_reaction_tape": True,
        "completed_reaction_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_reaction_law": False,
        "reason": (
            "The autocatalytic closure trace is reproduced by one fixed molecular "
            "alphabet, reaction graph, catalyst inventory, rate-law table, feedstock "
            "and boundary flux, initial concentrations, stochastic collision tape, "
            "and completed reaction history."
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
        case_id="autocatalytic_reaction_network_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_reaction_grammar_expansion_law",
        "required": (
            "A native physical source law in which the chemistry creates a new "
            "admissibility predicate, species algebra, reaction rule, or catalysis "
            "grammar not representable as fixed species alphabet, fixed reaction "
            "graph, fixed rate law, feedstock or boundary input, seed concentration, "
            "stochastic collision tape, observer naming, or completed reaction "
            "history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved abundance, flux, closure, "
            "and perturbation records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "autocatalytic_reaction_network_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md",
            "agent-runs/RUN-0169-p2cw1-whole-family-adjudication.md",
        ],
        "candidate_domain": "autocatalytic_chemical_reaction_network_emergence",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "autocatalytic_signal_present": True,
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
            "tests/artifacts/autocatalytic_reaction_network_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
