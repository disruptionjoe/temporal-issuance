#!/usr/bin/env python3
"""Candidate audit for crossed-product gravitational algebra claims.

The candidate is physically serious because observer or gravitational
crossed-product constructions can make algebraic structure appear to change.
This fixture asks whether that change is source-owned issuance or whether it
factors through a fixed theory plus observer frame, dressing, modular flow,
constraint, boundary, or representation bookkeeping.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


CANDIDATE_STATUS = "CANDIDATE_KILLED_FIXED_GRAVITATIONAL_BOOKKEEPING"
COMPLETION_WITNESS_ID = "fixed_gravitational_algebra_bookkeeping_completion"
COMPLETION_FAMILIES = (
    "fixed_source",
    "boundary_condition",
    "observer_information_access",
    "relabel_gauge",
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
    algebra_signal: bool
    finding: str


def adapter_fields() -> tuple[AdapterField, ...]:
    return (
        AdapterField(
            "Gamma_n",
            True,
            "fixed gravitational QFT, observer algebra, dressing, and boundary context",
            "The source context is real but already contains the fixed theory and comparison frame.",
        ),
        AdapterField(
            "Adm_n",
            False,
            "trace/type/admissibility predicate over a chosen crossed-product or observer algebra",
            (
                "The predicate is supplied by the observer frame, modular-flow "
                "choice, dressing, constraint handling, regulator, or algebraic "
                "completion, not generated as a new source-side law."
            ),
        ),
        AdapterField(
            "e_n",
            True,
            "algebra-type, trace, or observer-subalgebra transition signal",
            "The candidate has a concrete before/after algebraic signal.",
        ),
        AdapterField(
            "w_n",
            True,
            "preserved entropy, charge, correlation, modular, or boundary diagnostic",
            "The witness can be preserved without granting source issuance.",
        ),
        AdapterField(
            "Gamma_n_plus_1",
            False,
            "same fixed theory viewed through crossed-product, observer, or boundary completion",
            (
                "The successor context is a represented or completed view of "
                "the fixed theory rather than a source-owned algebra transition."
            ),
        ),
        AdapterField(
            "tau_n",
            True,
            "preserved algebra-comparison record and observer-frame trace",
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
                "A changed algebraic presentation or trace can appear, but it "
                "is not shown to create a non-isomorphic source algebra rather "
                "than a crossed-product, observer, modular, or boundary "
                "representation of the fixed theory."
            ),
        ),
        WitnessGate(
            "W2_new_admissibility_predicate",
            False,
            False,
            (
                "The admissibility predicate is chosen by the observer algebra, "
                "constraint implementation, dressing, regulator, or comparison "
                "construction."
            ),
        ),
        WitnessGate(
            "W3_construction_space_growth",
            False,
            False,
            (
                "The construction space is the fixed theory plus an algebraic "
                "completion recipe, not a source-generated construction grammar."
            ),
        ),
        WitnessGate(
            "W4_perturbation_non_factorization",
            False,
            False,
            (
                "Perturbations still factor through reference-frame choice, "
                "boundary data, gauge/dressing convention, modular flow, "
                "regulator, or completed-history description."
            ),
        ),
        WitnessGate(
            "W5_record_preservation",
            True,
            True,
            "Entropy, charge, algebraic, and boundary records can be preserved.",
        ),
        WitnessGate(
            "W6_observer_algebra_bookkeeping_absorption",
            False,
            False,
            (
                "Observer-access, gauge/relabeling, crossed-product, and "
                "completed-history absorbers are not defeated."
            ),
        ),
    )


def fixed_source_rival() -> dict[str, Any]:
    return {
        "rival_id": "fixed_gravitational_theory_with_observer_algebra_completion",
        "fixed_global_theory_or_hamiltonian": True,
        "fixed_state_or_path_integral_family": True,
        "fixed_observer_frame_or_dressing": True,
        "fixed_crossed_product_or_modular_flow_recipe": True,
        "fixed_boundary_or_constraint_data": True,
        "completed_history_available": True,
        "record_trace_preserved": True,
        "reproduces_candidate_shape": True,
        "source_owned_new_algebra_law": False,
        "reason": (
            "The algebraic change is reproduced by a fixed gravitational or "
            "QFT source plus observer frame, dressing, crossed-product or "
            "modular-flow construction, boundary/constraint data, and preserved "
            "comparison records."
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
        case_id="crossed_product_gravitational_algebra_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=nonfactorized,
        witnesses=(witness,),
        composition_closure_declared=True,
    )


def missing_source_object() -> dict[str, Any]:
    return {
        "missing_object_id": "source_owned_gravitational_algebra_transition_law",
        "required": (
            "A native physical source law in which gravitational dynamics "
            "forms a new observable, instrument, or admissibility algebra that "
            "is not representable by a fixed global theory, observer algebra, "
            "crossed-product or modular-flow construction, boundary condition, "
            "gauge/dressing convention, regulator, or completed history."
        ),
        "also_required": (
            "A W4 perturbation non-factorization certificate under the same "
            "preserved observer, boundary, charge, entropy, and correlation records."
        ),
    }


def run_candidate() -> dict[str, Any]:
    completion_decision = cc.classify_case(completion_case())
    source_fields = adapter_fields()
    gates = witness_gates()

    return {
        "fixture_id": "crossed_product_gravitational_algebra_candidate_v0",
        "source_artifacts": [
            "explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md",
            "explorations/E139-desitter-horizon-mode-issuance-adapter-p-2026-07-03.md",
            "COMPLETION-CLASS.md",
        ],
        "candidate_domain": "crossed_product_gravitational_observer_algebra",
        "candidate_status": CANDIDATE_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "adapter_fields": [asdict(field) for field in source_fields],
        "blocking_adapter_fields": [
            field.field_id for field in source_fields if not field.supplied
        ],
        "witness_gates": [asdict(gate) for gate in gates],
        "algebra_signal_present": True,
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
            "transition law, or a bounded no-go target for observer-algebra "
            "bookkeeping candidates that avoids universal physical overclaim"
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
            "tests/artifacts/crossed_product_gravitational_algebra_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_candidate()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
