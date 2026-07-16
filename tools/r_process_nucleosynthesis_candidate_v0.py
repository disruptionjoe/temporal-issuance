#!/usr/bin/env python3
"""Candidate audit for r-process nucleosynthesis issuance claims.

R-process nucleosynthesis is physically serious because neutron-rich ejecta can
realize heavy nuclei and abundance peaks that were not present in the seed
material. This fixture asks whether that realization is source-owned issuance
or whether it factors through a fixed nuclear reaction network, nuclear mass
table, beta-decay and neutron-capture rates, neutron flux, thermodynamic
trajectory, seed abundance, astrophysical ejecta context, fission recycling,
measurement protocol, and completed abundance history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_NUCLEAR_REACTION_NETWORK"
COMPLETION_WITNESS_ID = "fixed_nuclear_r_process_completion"
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
    nucleosynthesis_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            (
                "fixed nuclear species graph, nuclear mass table, neutron-"
                "capture cross sections, beta-decay rates, fission channels, "
                "seed abundance, neutron flux, entropy, electron fraction, "
                "expansion trajectory, and ejecta context"
            ),
            (
                "The physical context is real, but the candidate's species "
                "graph, rates, astrophysical trajectory, and resource budget "
                "are fixed before the claimed heavy-element formation event."
            ),
        ),
        AdapterField(
            "Adm_n",
            False,
            (
                "allowed isotope occupations, abundance-flow paths, waiting "
                "points, freeze-out states, and fission recycling products"
            ),
            (
                "The admissibility predicate is supplied by the fixed nuclear "
                "network and thermodynamic trajectory rather than generated as "
                "a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            (
                "rapid neutron-capture flow, beta-decay laddering, heavy-"
                "element abundance peaks, actinide production, or kilonova "
                "spectral signatures"
            ),
            (
                "The candidate has a concrete physical formation signal and is "
                "a useful negative control for new-material language."
            ),
        ),
        AdapterField(
            "w_n",
            True,
            (
                "abundance pattern, isotope ratios, decay-chain records, "
                "kilonova light curve, spectral lines, ejecta temperature, "
                "neutron density, and expansion records"
            ),
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            (
                "same fixed nuclear reaction network after abundance flow, "
                "freeze-out, decay, measurement, or retrospective access"
            ),
            (
                "The successor context is an occupied region of a predeclared "
                "nuclear species graph, not a source-owned expansion of the "
                "nuclear admissibility law."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            (
                "time-ordered neutron capture, beta decay, fission recycling, "
                "freeze-out, decay-chain, and measurement history"
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
                "Heavy nuclei appear, but the isotope graph, conserved quantum "
                "numbers, nuclear mass table, and reaction channels remain the "
                "fixed source specified in advance."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            True,
            (
                "Nuclear admissibility is defined by the fixed mass table, "
                "reaction rates, seed distribution, neutron flux, entropy, "
                "electron fraction, and expansion trajectory."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            True,
            (
                "The realized abundance pattern grows, but the construction "
                "space is already present in the fixed reaction network and "
                "its whole-family completion."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations factor through seed abundances, neutron density, "
                "electron fraction, entropy, expansion time, mass model, rate "
                "table, fission recycling, stochastic ejecta variation, "
                "measurement access, or completed abundance history."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            (
                "Abundance, isotope-ratio, decay-chain, spectral, light-curve, "
                "temperature, neutron-density, and expansion records can be "
                "preserved under the fixed rival."
            ),
        ),
        WitnessGate(
            "W6_fixed_family_after_naming_absorption",
            False,
            False,
            (
                "Fixed-source, hidden-state, initial/boundary condition, "
                "stochastic ejecta, name/provenance, access, relabeling, "
                "whole-family, and completed-history absorbers are not "
                "defeated from inside the candidate."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_r_process_network_model",
        "fixed_nuclear_species_graph": True,
        "fixed_nuclear_mass_and_rate_tables": True,
        "fixed_seed_abundance": True,
        "fixed_neutron_flux_and_electron_fraction": True,
        "fixed_thermodynamic_expansion_trajectory": True,
        "fixed_astrophysical_ejecta_context": True,
        "fixed_fission_recycling_channels": True,
        "stochastic_ejecta_or_rate_uncertainty_tape": True,
        "completed_abundance_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_species_law": False,
        "reason": (
            "The r-process trace is reproduced by a fixed nuclear species "
            "graph, nuclear mass and rate tables, seed abundance, neutron "
            "flux, electron fraction, thermodynamic expansion trajectory, "
            "astrophysical ejecta context, fission recycling channels, "
            "measurement access, and completed abundance history."
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
        case_id="r_process_nucleosynthesis_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_nuclear_species_generation_law",
        "required": (
            "A native physical source law in which nucleosynthesis creates a "
            "new nuclear species graph, admissibility predicate, reaction "
            "grammar, or construction space not representable as fixed nuclear "
            "mass and rate tables, fixed seed abundance, fixed neutron flux, "
            "fixed electron fraction, fixed expansion trajectory, fixed ejecta "
            "context, fission recycling, stochastic variation, observer "
            "access, or completed history."
        ),
        "also_required": (
            "An internal anti-after-naming principle plus W4 perturbation "
            "non-factorization under the same preserved abundance, isotope-"
            "ratio, decay-chain, spectral, light-curve, temperature, neutron-"
            "density, and expansion records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "r_process_nucleosynthesis_candidate_v0",
        "source_artifacts": [
            "COMPLETION-CLASS.md",
            "steward/research-portfolio.json",
            "agent-runs/RUN-0172-bose-einstein-condensation-candidate-v0.md",
        ],
        "candidate_domain": "r_process_nucleosynthesis",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "nucleosynthesis_signal_present": True,
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
            "tests/artifacts/r_process_nucleosynthesis_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
