"""Adapter_P candidate scout for OnlineIssuance^LC.

This is a scouting table, not a positive physics fixture. It asks which
candidate families can state a concrete W1-W6 obligation worth a later
absorber test.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from online_issuance_physical_adapter_contract import (
    ADAPTER_FIELDS,
    absorber_nulls,
    witness_gates,
)


EXPECTED_CANDIDATES = [
    "quantum_measurement_contextuality",
    "causal_set_sequential_growth",
    "holographic_boundary_encoding",
    "gu_missing_piece_adapter_language",
    "assembly_theory_source_assembly_index",
    "quantum_biological_orch_or_substrate",
    "dual_record_adjacent_possible_graphs_current_form",
]

NEXT_GATE = "oi_lc_assembly_source_adapter_fixture"


@dataclass(frozen=True)
class CandidateScoutRow:
    candidate_id: str
    family: str
    claim_form: str
    adapter_mapping: dict[str, str]
    w1_w6_scores: dict[str, str]
    fixed_source_nulls: dict[str, str]
    concrete_witness_obligation: bool
    physical_source_issuance_established: bool
    stop_rule_verdict: str
    reason: str
    next_obligation: str


def _adapter_mapping(**overrides: str) -> dict[str, str]:
    mapping = {field: "missing" for field in ADAPTER_FIELDS}
    mapping.update(overrides)
    return mapping


def _w_scores(**overrides: str) -> dict[str, str]:
    scores = {gate.gate_id: "missing" for gate in witness_gates()}
    scores.update(overrides)
    return scores


def _nulls(**overrides: str) -> dict[str, str]:
    statuses = {absorber.absorber_id: "undefeated_or_not_targeted" for absorber in absorber_nulls()}
    statuses.update(overrides)
    return statuses


def candidate_rows() -> list[CandidateScoutRow]:
    return [
        CandidateScoutRow(
            candidate_id="quantum_measurement_contextuality",
            family="quantum measurement / contextuality",
            claim_form=(
                "Outcomes and record facts depend on measurement context, so physics may already "
                "contain issuance-like record formation."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: fixed Hilbert state, measurement context, and prior record map can be named",
                Adm_n="partial: admissible measurements are normally fixed by a cover or instrument family",
                e_n="missing: no source-generated new observable or instrument class is supplied",
                w_n="missing: contextuality proofs do not witness Adm_n(e_n) as a new source class",
                Gamma_n_plus_1="absorbed: successor is state update, branch, or readout inside fixed theory",
                tau_n="supplied: outcome records and protocol traces are available",
            ),
            w1_w6_scores=_w_scores(
                W1="missing: fixed H_infty / A_infty absorbs the algebraic structure",
                W2="missing: no newly formed admissibility predicate",
                W3="missing: no source-generated construction term",
                W4="partial: perturbation protocols exist but factor through fixed instruments",
                W5="partial: records are preserved as ordinary readout traces",
                W6="absorbed: AB/contextuality fixed-cover language remains available",
            ),
            fixed_source_nulls=_nulls(
                fixed_H_infty="undefeated",
                fixed_A_infty="undefeated",
                fixed_instrument_family="undefeated",
                bounded_access_to_Mu_infty="undefeated",
                experimenter_added_schema="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="killed_shortcut",
            reason=(
                "As a TI-C020 shortcut, contextuality collapses into fixed-H/fixed-A/context "
                "bookkeeping unless a future candidate supplies a genuinely new source class."
            ),
            next_obligation="Do not use contextuality alone as evidence; only revisit with non-fixed observable algebra growth.",
        ),
        CandidateScoutRow(
            candidate_id="causal_set_sequential_growth",
            family="causal-set or sequential-growth models",
            claim_form=(
                "A growing causal order looks like physical record issuance because new elements "
                "are born into a partially ordered history."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: finite causal-set prefix can be treated as source context",
                Adm_n="partial: admissibility is usually a fixed birth or transition law",
                e_n="partial: next element or relation is a candidate extension",
                w_n="missing: no proof object separates source growth from fixed stochastic law",
                Gamma_n_plus_1="partial: successor prefix is available",
                tau_n="partial: birth history is recordable but not yet tied to observer records",
            ),
            w1_w6_scores=_w_scores(
                W1="missing: order growth is not yet non-isomorphic observable-algebra growth",
                W2="partial: possible only if admissibility itself changes, not if the law is fixed",
                W3="partial: new elements arrive, but the birth rule may precontain the construction space",
                W4="missing: no perturbation non-factorization protocol",
                W5="missing: observer-record preservation is not supplied",
                W6="missing: gauge/label absorption is not defeated",
            ),
            fixed_source_nulls=_nulls(
                fixed_stochastic_or_collapse_law="undefeated",
                fixed_boundary_or_holographic_completion="undefeated_or_not_targeted",
                bounded_access_to_Mu_infty="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="parked",
            reason=(
                "The family has real growth vocabulary, but current forms usually import a fixed "
                "stochastic law rather than proving source-generated admissibility."
            ),
            next_obligation="State a witness that the growth law/admissibility is not precontained in a fixed source.",
        ),
        CandidateScoutRow(
            candidate_id="holographic_boundary_encoding",
            family="holographic / boundary encodings",
            claim_form=(
                "Bulk record formation could be a projection from a richer boundary or external "
                "encoding."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: boundary/source state can be named",
                Adm_n="absorbed: admissibility is supplied by the fixed boundary completion",
                e_n="missing: no new source extension outside the boundary completion",
                w_n="missing: no non-precontainment witness",
                Gamma_n_plus_1="absorbed: successor is re-expression or reconstruction from boundary data",
                tau_n="partial: boundary/bulk reconstruction traces can be recorded",
            ),
            w1_w6_scores=_w_scores(
                W1="absorbed: fixed richer boundary can precontain the algebra",
                W2="missing: no new admissibility predicate",
                W3="missing: no source-generated construction term",
                W4="missing: no non-factorization beyond boundary dynamics",
                W5="partial: record preservation is compatible with the null",
                W6="absorbed: boundary/bulk translation remains a language/access change",
            ),
            fixed_source_nulls=_nulls(
                fixed_boundary_or_holographic_completion="undefeated",
                bounded_access_to_Mu_infty="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="killed_shortcut",
            reason=(
                "As currently stated, this is the fixed-boundary absorber, not a defeat of it."
            ),
            next_obligation="Do not use fixed boundary completion as issuance evidence; require a boundary non-precontainment proof.",
        ),
        CandidateScoutRow(
            candidate_id="gu_missing_piece_adapter_language",
            family="GU missing-piece adapter language",
            claim_form=(
                "The GU 14D-to-4D interface plus a missing external adapter may point to a stable "
                "record structure outside the rendered 4D shadow."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: GU carrier and observer-rendered interface can be named",
                Adm_n="missing: exact admissibility predicate for the missing piece is not specified",
                e_n="missing: candidate source extension is not yet typed",
                w_n="missing: no witness term exists",
                Gamma_n_plus_1="missing: successor source context is not defined",
                tau_n="partial: projected 4D record traces are conceptually available",
            ),
            w1_w6_scores=_w_scores(
                W1="partial: may supply a geometric invariant after exact GU/TI typing",
                W2="missing: no new admissibility predicate yet",
                W3="missing: no construction provenance",
                W4="missing: no intervention protocol",
                W5="partial: historical records are part of the motivation, not a fixture",
                W6="missing: 14D/4D language has not defeated gauge/access relabeling",
            ),
            fixed_source_nulls=_nulls(
                fixed_boundary_or_holographic_completion="undefeated_or_not_targeted",
                bounded_access_to_Mu_infty="undefeated",
                experimenter_added_schema="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="parked",
            reason=(
                "This is promising adapter language, but it lacks the exact typed mapping and "
                "witness object required before a fixture can be executable."
            ),
            next_obligation="Produce a GU/TI adapter inventory before running W1-W6 as physics evidence.",
        ),
        CandidateScoutRow(
            candidate_id="assembly_theory_source_assembly_index",
            family="Assembly Theory source assembly index",
            claim_form=(
                "A source assembly index could witness that a construction class becomes newly "
                "defined rather than merely newly observed."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: source construction universe, objects, and constructors at prefix n",
                Adm_n="partial: admissibility predicate for source assembly class formation",
                e_n="partial: candidate new construction class or object",
                w_n="partial: source trace where AI_src,n is undefined and AI_src,n+1 is defined",
                Gamma_n_plus_1="partial: source context after the assembly class is admitted",
                tau_n="supplied: assembly/provenance trace can be recorded",
            ),
            w1_w6_scores=_w_scores(
                W1="missing: not yet a non-isomorphic observable algebra witness",
                W2="obligation_stated: prove the new assembly predicate was not decidable before n+1",
                W3="obligation_stated: prove source construction-space growth by AI_src undefined-to-defined",
                W4="missing: no perturbation non-factorization fixture yet",
                W5="partial: provenance trace gives a record-preservation target",
                W6="partial: must defeat modeler-added vocabulary and bounded-access absorbers",
            ),
            fixed_source_nulls=_nulls(
                bounded_access_to_Mu_infty="undefeated",
                experimenter_added_schema="undefeated",
                fixed_stochastic_or_collapse_law="undefeated_or_not_targeted",
            ),
            concrete_witness_obligation=True,
            physical_source_issuance_established=False,
            stop_rule_verdict="fixture_candidate",
            reason=(
                "This is the only surveyed family that can state a concrete executable W2/W3 "
                "obligation: show a source assembly index becomes defined without fixed-source "
                "precontainment or modeler-added schema."
            ),
            next_obligation=(
                "Build an absorber fixture for AI_src,n undefined -> AI_src,n+1 defined against "
                "fixed-source, bounded-access, and experimenter-schema nulls."
            ),
        ),
        CandidateScoutRow(
            candidate_id="quantum_biological_orch_or_substrate",
            family="quantum-biological / Orch-OR substrate",
            claim_form=(
                "Conscious observers may depend on quantum-biological collapse or substrate-level "
                "events that issue records."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: physical/biological substrate context can be named",
                Adm_n="missing: no source admissibility predicate",
                e_n="missing: no new source extension class",
                w_n="missing: no W1-W3 witness term",
                Gamma_n_plus_1="absorbed: dynamics fit fixed quantum/collapse/biochemical law",
                tau_n="partial: neural or biochemical traces may be recordable",
            ),
            w1_w6_scores=_w_scores(
                W1="missing: no non-isomorphic algebra growth",
                W2="missing: no new admissibility predicate",
                W3="missing: no source construction-space growth",
                W4="missing: perturbations factor through substrate parameters or collapse law",
                W5="partial: records can be preserved as biological traces",
                W6="absorbed: substrate naming does not defeat fixed-H/fixed-law absorbers",
            ),
            fixed_source_nulls=_nulls(
                fixed_H_infty="undefeated",
                fixed_stochastic_or_collapse_law="undefeated",
                bounded_access_to_Mu_infty="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="killed_shortcut",
            reason=(
                "As a substrate shortcut, it supplies a possible implementation story but no "
                "Adapter_P source-growth witness."
            ),
            next_obligation="Do not promote substrate claims without a separate W1-W6 source-growth witness.",
        ),
        CandidateScoutRow(
            candidate_id="dual_record_adjacent_possible_graphs_current_form",
            family="dual-record adjacent-possible opportunity graphs",
            claim_form=(
                "Opportunity graphs describe newly available moves, so source issuance might be "
                "the growth of the adjacent possible."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: current opportunity graph can be source context",
                Adm_n="partial: admissible next moves are graph edges",
                e_n="partial: new opportunity edge or node",
                w_n="missing: no no-hidden-oracle witness defeats fixed latent graph",
                Gamma_n_plus_1="partial: graph after opportunity update",
                tau_n="supplied: dual-record traces can be emitted",
            ),
            w1_w6_scores=_w_scores(
                W1="missing: opportunity graph change is not observable-algebra growth",
                W2="partial: admissible moves change, but may be fixed latent graph access",
                W3="partial: construction-space growth is stated but not protected",
                W4="missing: no perturbation non-factorization protocol",
                W5="partial: dual records preserve traces",
                W6="absorbed: exact fixed latent graph/access relabeling remains available",
            ),
            fixed_source_nulls=_nulls(
                bounded_access_to_Mu_infty="undefeated",
                experimenter_added_schema="undefeated",
            ),
            concrete_witness_obligation=False,
            physical_source_issuance_established=False,
            stop_rule_verdict="killed_shortcut",
            reason=(
                "The current form is absorbed by an exact fixed latent opportunity graph plus "
                "changing access, so it cannot be used as source evidence."
            ),
            next_obligation="Only revisit if a no-hidden-oracle opportunity-edge witness is supplied.",
        ),
    ]


def _all_candidate_structures_complete(rows: list[CandidateScoutRow]) -> bool:
    expected_fields = set(ADAPTER_FIELDS)
    expected_gates = {gate.gate_id for gate in witness_gates()}
    expected_nulls = {absorber.absorber_id for absorber in absorber_nulls()}
    return all(
        set(row.adapter_mapping) == expected_fields
        and set(row.w1_w6_scores) == expected_gates
        and set(row.fixed_source_nulls) == expected_nulls
        and row.stop_rule_verdict in {"fixture_candidate", "parked", "killed_shortcut"}
        for row in rows
    )


def run_scout() -> dict[str, object]:
    rows = candidate_rows()
    row_dicts = [asdict(row) for row in rows]
    verdicts = {row.candidate_id: row.stop_rule_verdict for row in rows}
    fixture_candidates = [
        row for row in rows if row.stop_rule_verdict == "fixture_candidate"
    ]
    parked = [row for row in rows if row.stop_rule_verdict == "parked"]
    killed = [row for row in rows if row.stop_rule_verdict == "killed_shortcut"]
    selected = fixture_candidates[0].candidate_id if fixture_candidates else None

    return {
        "fixture": "oi_lc_candidate_scout_w1_w6_table_v0_1",
        "source_artifacts": [
            "explorations/E057-ti-c020-fixed-h-vs-h-growing-six-axis-fixture-2026-06-24.md",
            "explorations/E064-assembly-theory-d4-source-projection-operationalization-2026-06-24.md",
            "explorations/E094-dual-record-fixture-effect-gate-2026-06-25.md",
            "explorations/E108-online-issuance-witness-machine-check-2026-07-01.md",
            "explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md",
            "explorations/E111-adapter-p-missing-piece-63-persona-pass-2026-07-01.md",
        ],
        "scoring_key": {
            "fixture_candidate": (
                "Candidate has not passed Adapter_P, but states a concrete W1-W6 obligation "
                "worth an executable absorber fixture."
            ),
            "parked": (
                "Candidate has useful language but lacks enough typed adapter fields or witness "
                "objects for the next fixture."
            ),
            "killed_shortcut": (
                "Current shortcut collapses into an already named fixed-source/null absorber and "
                "must not be used as evidence."
            ),
        },
        "adapter_fields": sorted(ADAPTER_FIELDS),
        "w1_w6_gate_ids": [gate.gate_id for gate in witness_gates()],
        "fixed_source_null_ids": [absorber.absorber_id for absorber in absorber_nulls()],
        "candidate_table": row_dicts,
        "comparisons": {
            "candidate_count": len(rows),
            "expected_candidates_present": [row.candidate_id for row in rows] == EXPECTED_CANDIDATES,
            "structured_adapter_scoring_table": _all_candidate_structures_complete(rows),
            "fixture_candidate_count": len(fixture_candidates),
            "parked_count": len(parked),
            "killed_shortcut_count": len(killed),
            "selected_fixture_candidate": selected,
            "assembly_source_index_selected_for_fixture": selected
            == "assembly_theory_source_assembly_index",
            "selected_fixture_candidate_is_evidence": False,
            "physical_source_issuance_established": any(
                row.physical_source_issuance_established for row in rows
            ),
            "TI_C020_reopened": False,
            "stop_rule_verdicts": verdicts,
            "quantum_contextuality_shortcut_killed": verdicts[
                "quantum_measurement_contextuality"
            ]
            == "killed_shortcut",
            "holographic_boundary_shortcut_killed": verdicts[
                "holographic_boundary_encoding"
            ]
            == "killed_shortcut",
            "orch_or_substrate_shortcut_killed": verdicts[
                "quantum_biological_orch_or_substrate"
            ]
            == "killed_shortcut",
            "dual_record_current_form_shortcut_killed": verdicts[
                "dual_record_adjacent_possible_graphs_current_form"
            ]
            == "killed_shortcut",
            "causal_set_route_parked": verdicts["causal_set_sequential_growth"] == "parked",
            "gu_missing_piece_route_parked": verdicts[
                "gu_missing_piece_adapter_language"
            ]
            == "parked",
            "next_gate": NEXT_GATE,
        },
        "verdict": {
            "candidate_selected_for_fixture": selected is not None,
            "selected_candidate": selected,
            "selected_scope": "executable absorber fixture target, not evidence",
            "Issue[S]^physical": False,
            "Issue[S]^LC": True,
            "TI_C020_reopened": False,
            "claim_status_change": "none",
            "best_result": (
                "Assembly Theory source-assembly index is the only surveyed family that can "
                "state a concrete W2/W3 witness obligation worth testing. It has not defeated "
                "bounded-access or experimenter-schema nulls, so it is a fixture target only."
            ),
            "next_gate": NEXT_GATE,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the OnlineIssuance^LC Adapter_P candidate scout table."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_scout()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
