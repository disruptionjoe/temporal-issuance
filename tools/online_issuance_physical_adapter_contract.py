"""Executable contract for adapting physical traces to OnlineIssuance^LC.

The contract is not a positive physical fixture. It defines what a later
candidate must supply before the repo can treat it as a possible TI-C020
source-side witness rather than fixed-H/readout vocabulary.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


ADAPTER_FIELDS = {
    "Gamma_n": "physical source context available at prefix n",
    "Adm_n": "admissibility predicate formed inside Gamma_n",
    "e_n": "candidate physical source extension",
    "w_n": "witness term for Adm_n(e_n)",
    "Gamma_n_plus_1": "successor source context after accepted extension",
    "tau_n": "recordable source trace sufficient for projection/finality audit",
}


@dataclass(frozen=True)
class WitnessGate:
    gate_id: str
    name: str
    requirement: str
    role: str


@dataclass(frozen=True)
class AbsorberNull:
    absorber_id: str
    null_model: str
    rejection_condition: str


@dataclass(frozen=True)
class CandidateTrace:
    candidate_id: str
    description: str
    mapped_fields: dict[str, bool]
    witness_claims: dict[str, bool]
    absorber_defeats: dict[str, bool]
    no_hidden_oracle: bool
    source_generated: bool
    real_physical_candidate: bool


@dataclass(frozen=True)
class CandidateEvaluation:
    candidate_id: str
    all_adapter_fields_mapped: bool
    source_growth_core_supplied: bool
    absorber_control_supplied: bool
    all_absorbers_defeated: bool
    no_hidden_oracle: bool
    source_generated: bool
    real_physical_candidate: bool
    adapter_contract_passed: bool
    physical_source_issuance_established: bool
    reason: str


def witness_gates() -> list[WitnessGate]:
    return [
        WitnessGate(
            gate_id="W1",
            name="non_isomorphic_algebra",
            requirement=(
                "A_{n+1} is not isomorphic to a restriction, subalgebra, completion, "
                "representation change, or coarse-graining of fixed A_infty while preserving records."
            ),
            role="source_growth_core",
        ),
        WitnessGate(
            gate_id="W2",
            name="new_admissibility_predicate",
            requirement=(
                "Adm_{n+1} decides a new observable, instrument, or construction class "
                "not decidable or pre-enumerable by Adm_infty."
            ),
            role="source_growth_core",
        ),
        WitnessGate(
            gate_id="W3",
            name="construction_space_growth",
            requirement=(
                "The physical source constructs an observable or instrument type whose "
                "construction term was not present in the prior physical/source formalism."
            ),
            role="source_growth_core",
        ),
        WitnessGate(
            gate_id="W4",
            name="perturbation_non_factorization",
            requirement=(
                "Perturbation effects cannot be reproduced by parameter, coupling, channel, "
                "decoherence, collapse-rate, or biochemical changes inside fixed structure."
            ),
            role="absorber_control",
        ),
        WitnessGate(
            gate_id="W5",
            name="record_preservation",
            requirement=(
                "The growing-structure reading preserves the same record maps and observed "
                "perturbation effects better than every fixed-H absorber."
            ),
            role="absorber_control",
        ),
        WitnessGate(
            gate_id="W6",
            name="gauge_absorption_pass",
            requirement=(
                "The claimed growth is not an observer-name change, schema relabeling, "
                "measurement-context bookkeeping, or AB-style fixed-cover contextuality effect."
            ),
            role="absorber_control",
        ),
    ]


def absorber_nulls() -> list[AbsorberNull]:
    return [
        AbsorberNull(
            absorber_id="fixed_H_infty",
            null_model="fixed Hilbert/state space with evolving state or access maps",
            rejection_condition="candidate cannot factor through fixed H_infty while preserving records",
        ),
        AbsorberNull(
            absorber_id="fixed_A_infty",
            null_model="fixed observable algebra with subalgebra, context, or representation changes",
            rejection_condition="candidate supplies non-isomorphic algebra/admissibility not representable in A_infty",
        ),
        AbsorberNull(
            absorber_id="fixed_instrument_family",
            null_model="fixed POVM/channel/instrument family plus protocol selection",
            rejection_condition="candidate's instrument or observable type is source-generated, not selected",
        ),
        AbsorberNull(
            absorber_id="fixed_stochastic_or_collapse_law",
            null_model="fixed stochastic, collapse, or open-system law",
            rejection_condition="candidate cannot be reproduced as sampling or collapse inside a fixed law",
        ),
        AbsorberNull(
            absorber_id="fixed_boundary_or_holographic_completion",
            null_model="fixed richer boundary/source containing the trace",
            rejection_condition="candidate blocks precontainment by a boundary or completed source object",
        ),
        AbsorberNull(
            absorber_id="bounded_access_to_Mu_infty",
            null_model="fixed richer Mu_infty plus changing observer/process access",
            rejection_condition="candidate changes source admissibility rather than access to pre-existing structure",
        ),
        AbsorberNull(
            absorber_id="experimenter_added_schema",
            null_model="new observables introduced by measurement design or modeler vocabulary",
            rejection_condition="candidate shows the physical source forms the new class without experimenter addition",
        ),
    ]


def candidate_controls() -> list[CandidateTrace]:
    absorber_ids = [absorber.absorber_id for absorber in absorber_nulls()]
    mapped = {field: True for field in ADAPTER_FIELDS}
    return [
        CandidateTrace(
            candidate_id="negative_fixed_h_readout",
            description=(
                "A predictive-to-accessible physical trace that maps records but remains fixed-H, "
                "fixed-A, fixed-instrument readout."
            ),
            mapped_fields=mapped,
            witness_claims={
                "W1": False,
                "W2": False,
                "W3": False,
                "W4": False,
                "W5": True,
                "W6": False,
            },
            absorber_defeats={absorber_id: False for absorber_id in absorber_ids},
            no_hidden_oracle=False,
            source_generated=False,
            real_physical_candidate=True,
        ),
        CandidateTrace(
            candidate_id="schematic_positive_adapter_shape",
            description=(
                "A schematic, not-yet-instantiated shape showing the contract is satisfiable "
                "if a future candidate supplies W1-W6 and defeats every fixed-source null."
            ),
            mapped_fields=mapped,
            witness_claims={
                "W1": True,
                "W2": True,
                "W3": True,
                "W4": True,
                "W5": True,
                "W6": True,
            },
            absorber_defeats={absorber_id: True for absorber_id in absorber_ids},
            no_hidden_oracle=True,
            source_generated=True,
            real_physical_candidate=False,
        ),
    ]


def evaluate_candidate(candidate: CandidateTrace) -> CandidateEvaluation:
    all_adapter_fields_mapped = all(candidate.mapped_fields.get(field, False) for field in ADAPTER_FIELDS)
    source_growth_core_supplied = any(
        candidate.witness_claims.get(gate_id, False) for gate_id in ("W1", "W2", "W3")
    )
    absorber_control_supplied = all(
        candidate.witness_claims.get(gate_id, False) for gate_id in ("W4", "W5", "W6")
    )
    all_absorbers_defeated = all(candidate.absorber_defeats.values())
    adapter_contract_passed = (
        all_adapter_fields_mapped
        and source_growth_core_supplied
        and absorber_control_supplied
        and all_absorbers_defeated
        and candidate.no_hidden_oracle
        and candidate.source_generated
    )
    physical_source_issuance_established = (
        adapter_contract_passed and candidate.real_physical_candidate
    )

    if physical_source_issuance_established:
        reason = "real candidate passes Adapter_P and all fixed-source nulls"
    elif adapter_contract_passed:
        reason = "schematic adapter shape passes but is not a real physical candidate"
    elif not source_growth_core_supplied:
        reason = "no W1-W3 source-growth core witness supplied"
    elif not absorber_control_supplied:
        reason = "W4-W6 absorber controls are incomplete"
    elif not all_absorbers_defeated:
        reason = "at least one fixed-source absorber remains undefeated"
    elif not candidate.no_hidden_oracle:
        reason = "hidden completed oracle or fixed latent source remains available"
    else:
        reason = "adapter mapping incomplete or source-generation not established"

    return CandidateEvaluation(
        candidate_id=candidate.candidate_id,
        all_adapter_fields_mapped=all_adapter_fields_mapped,
        source_growth_core_supplied=source_growth_core_supplied,
        absorber_control_supplied=absorber_control_supplied,
        all_absorbers_defeated=all_absorbers_defeated,
        no_hidden_oracle=candidate.no_hidden_oracle,
        source_generated=candidate.source_generated,
        real_physical_candidate=candidate.real_physical_candidate,
        adapter_contract_passed=adapter_contract_passed,
        physical_source_issuance_established=physical_source_issuance_established,
        reason=reason,
    )


def run_contract() -> dict[str, object]:
    gates = witness_gates()
    nulls = absorber_nulls()
    candidates = candidate_controls()
    evaluations = [evaluate_candidate(candidate) for candidate in candidates]
    negative_eval = next(
        evaluation for evaluation in evaluations if evaluation.candidate_id == "negative_fixed_h_readout"
    )
    schematic_eval = next(
        evaluation
        for evaluation in evaluations
        if evaluation.candidate_id == "schematic_positive_adapter_shape"
    )

    return {
        "fixture": "online_issuance_lc_physical_adapter_contract_v0_1",
        "source_artifacts": [
            "explorations/E057-ti-c020-fixed-h-vs-h-growing-six-axis-fixture-2026-06-24.md",
            "explorations/E108-online-issuance-witness-machine-check-2026-07-01.md",
            "explorations/E109-online-issuance-big-swing-campaign-2026-07-01.md",
        ],
        "adapter_contract": {
            "adapter_id": "Adapter_P",
            "source": "physical candidate trace",
            "target": ADAPTER_FIELDS,
            "acceptance_rule": (
                "A real physical candidate passes only if all adapter fields map, at least one "
                "W1-W3 source-growth core witness is supplied, W4-W6 absorber controls are "
                "supplied, every fixed-source absorber is defeated, no hidden oracle remains, "
                "and the new class is source-generated rather than experimenter-added."
            ),
        },
        "witness_gates": [asdict(gate) for gate in gates],
        "absorber_nulls": [asdict(absorber) for absorber in nulls],
        "candidate_controls": [asdict(candidate) for candidate in candidates],
        "candidate_evaluations": [asdict(evaluation) for evaluation in evaluations],
        "comparisons": {
            "contract_well_formed": True,
            "adapter_fields_defined": sorted(ADAPTER_FIELDS),
            "all_required_adapter_fields_defined": len(ADAPTER_FIELDS) == 6,
            "w1_w6_gate_ids": [gate.gate_id for gate in gates],
            "w1_w6_gate_defined": [gate.gate_id for gate in gates] == ["W1", "W2", "W3", "W4", "W5", "W6"],
            "source_growth_core_requires_w1_or_w2_or_w3": True,
            "absorber_control_requires_w4_w5_w6": True,
            "fixed_source_absorber_nulls_defined": len(nulls) == 7,
            "negative_fixed_h_control_rejected": not negative_eval.adapter_contract_passed,
            "negative_fixed_h_reason": negative_eval.reason,
            "schematic_positive_shape_admitted": schematic_eval.adapter_contract_passed,
            "schematic_positive_is_real_candidate": schematic_eval.real_physical_candidate,
            "physical_source_issuance_established": any(
                evaluation.physical_source_issuance_established for evaluation in evaluations
            ),
            "candidate_selected_for_fixture": False,
        },
        "verdict": {
            "adapter_contract_exists": True,
            "Issue[S]^physical": False,
            "Issue[S]^LC": True,
            "TI_C020_reopened": False,
            "claim_status_change": "none",
            "best_result": (
                "A non-circular Adapter_P contract can be stated. It rejects fixed-H/readout "
                "controls and admits only candidates that supply a W1-W3 source-growth core, "
                "W4-W6 absorber controls, no hidden oracle, source generation, and fixed-source "
                "absorber defeat."
            ),
            "next_gate": "oi_lc_candidate_scout_w1_w6_table",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the OnlineIssuance^LC physical Adapter_P contract checker."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_contract()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
