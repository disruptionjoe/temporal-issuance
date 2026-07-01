"""Physical-protocol fixture for the Assembly source-index route.

The prior Assembly fixture produced a formal/local W2-W3 witness. This fixture
asks whether any real physical or empirical assembly-domain trace can add W1 and
W4-W6 strongly enough to pass Adapter_P.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from online_issuance_physical_adapter_contract import ADAPTER_FIELDS, witness_gates


NEXT_GATE = "proof_assistant_online_issuance_witness"

PHYSICAL_ABSORBERS = [
    "fixed_chemistry_or_reaction_network",
    "bounded_sampling_or_database_access",
    "experimenter_or_instrument_schema",
    "fixed_stochastic_or_search_process",
    "fixed_observable_algebra",
]


@dataclass(frozen=True)
class ProtocolAttempt:
    attempt_id: str
    domain: str
    trace_claim: str
    adapter_mapping: dict[str, str]
    witness_claims: dict[str, bool]
    absorber_results: dict[str, bool]
    no_hidden_oracle: bool
    source_generated: bool
    real_physical_candidate: bool
    record_trace: str


@dataclass(frozen=True)
class ProtocolEvaluation:
    attempt_id: str
    all_adapter_fields_mapped: bool
    source_growth_core_supplied: bool
    w1_supplied: bool
    w2_w3_supplied: bool
    w4_physical_protocol_supplied: bool
    w5_record_preservation_supplied: bool
    w6_absorber_control_supplied: bool
    targeted_absorbers_defeated: bool
    no_hidden_oracle: bool
    source_generated: bool
    real_physical_candidate: bool
    adapter_gate_shape_passed: bool
    adapter_contract_passed_by_real_candidate: bool
    physical_source_issuance_established: bool
    verdict: str
    reason: str


def _adapter_mapping(**overrides: str) -> dict[str, str]:
    mapping = {field: "missing" for field in ADAPTER_FIELDS}
    mapping.update(overrides)
    return mapping


def _witness_claims(**overrides: bool) -> dict[str, bool]:
    claims = {gate.gate_id: False for gate in witness_gates()}
    claims.update(overrides)
    return claims


def _absorbers(**overrides: bool) -> dict[str, bool]:
    results = {absorber: False for absorber in PHYSICAL_ABSORBERS}
    results.update(overrides)
    return results


def protocol_attempts() -> list[ProtocolAttempt]:
    return [
        ProtocolAttempt(
            attempt_id="chemistry_reaction_network_trace",
            domain="chemical synthesis / molecular assembly records",
            trace_claim=(
                "A molecule with higher assembly index appears after a reagent, catalyst, "
                "temperature, or pathway perturbation."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: current physical reaction context, reagents, catalysts, and instrument records",
                Adm_n="partial: admissible products are determined by fixed chemistry and protocol constraints",
                e_n="partial: observed product class or synthesis step",
                w_n="partial: lab trace showing product detection and assembly-index assignment",
                Gamma_n_plus_1="partial: updated reaction state or record set after product formation",
                tau_n="supplied: reaction log, spectra, product identity, and assembly-index record",
            ),
            witness_claims=_witness_claims(
                W2=False,
                W3=False,
                W5=True,
            ),
            absorber_results=_absorbers(
                fixed_chemistry_or_reaction_network=True,
                fixed_observable_algebra=True,
            ),
            no_hidden_oracle=False,
            source_generated=False,
            real_physical_candidate=True,
            record_trace="reaction log plus spectra preserve the observed product, but not source issuance",
        ),
        ProtocolAttempt(
            attempt_id="high_throughput_search_trace",
            domain="automated discovery / high-throughput assembly search",
            trace_claim=(
                "A previously unknown high-assembly object is found after many trials, giving "
                "an apparent undefined-to-defined transition."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: current sample library, search protocol, and scoring rule",
                Adm_n="partial: admissibility is fixed by the search objective and detection threshold",
                e_n="partial: newly found object or synthesis recipe",
                w_n="partial: search run record and detection certificate",
                Gamma_n_plus_1="partial: expanded discovered set",
                tau_n="supplied: search log, hit record, and analysis output",
            ),
            witness_claims=_witness_claims(
                W2=False,
                W3=False,
                W5=True,
            ),
            absorber_results=_absorbers(
                bounded_sampling_or_database_access=True,
                fixed_stochastic_or_search_process=True,
                fixed_observable_algebra=True,
            ),
            no_hidden_oracle=False,
            source_generated=False,
            real_physical_candidate=True,
            record_trace="search logs preserve discovery but factor through fixed search space",
        ),
        ProtocolAttempt(
            attempt_id="evolutionary_biosynthesis_trace",
            domain="biological or evolutionary molecular assembly",
            trace_claim=(
                "A lineage evolves a new biosynthetic capability or high-assembly molecule "
                "after mutation and selection."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: lineage state, genome/regulatory machinery, environment, and records",
                Adm_n="partial: viability and biosynthetic admissibility under existing chemistry",
                e_n="partial: new pathway, enzyme activity, or product class",
                w_n="partial: phylogenetic, genomic, and product-trace evidence",
                Gamma_n_plus_1="partial: lineage state after pathway/product appears",
                tau_n="supplied: sequence records, phenotype records, and product assays",
            ),
            witness_claims=_witness_claims(
                W2=False,
                W3=False,
                W5=True,
            ),
            absorber_results=_absorbers(
                fixed_chemistry_or_reaction_network=True,
                fixed_stochastic_or_search_process=True,
                fixed_observable_algebra=True,
            ),
            no_hidden_oracle=False,
            source_generated=False,
            real_physical_candidate=True,
            record_trace="evolutionary records preserve novelty but fit mutation/search over fixed chemistry",
        ),
        ProtocolAttempt(
            attempt_id="instrument_schema_update_trace",
            domain="measurement pipeline / assembly-index annotation",
            trace_claim=(
                "The assembly index becomes defined after a new decomposition grammar, mass-spec "
                "method, database entry, or annotation rule is introduced."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="partial: current instrument, decomposition grammar, and database schema",
                Adm_n="partial: admissibility is the modeler's current analysis rule",
                e_n="absorbed: new annotation or decomposition macro",
                w_n="partial: analysis output showing index now defined",
                Gamma_n_plus_1="absorbed: schema/database state after update",
                tau_n="supplied: instrument output and annotation history",
            ),
            witness_claims=_witness_claims(
                W2=False,
                W3=False,
                W5=True,
            ),
            absorber_results=_absorbers(
                bounded_sampling_or_database_access=True,
                experimenter_or_instrument_schema=True,
                fixed_observable_algebra=True,
            ),
            no_hidden_oracle=True,
            source_generated=False,
            real_physical_candidate=True,
            record_trace="annotation history preserves the change as schema update, not source growth",
        ),
        ProtocolAttempt(
            attempt_id="formal_local_assembly_trace_from_e113",
            domain="formal/local assembly source trace",
            trace_claim=(
                "The E113 source-generated constructor trace makes AI_src,n undefined and "
                "AI_src,n+1 defined while targeted local absorbers fail."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="supplied: formal source assembly prefix before bind_c",
                Adm_n="supplied: target ABC not constructible at prefix n",
                e_n="supplied: source-generated bind_c(AB, C) -> ABC",
                w_n="supplied: computed AI_src,n undefined and AI_src,n+1 = 2",
                Gamma_n_plus_1="supplied: successor prefix with bind_c",
                tau_n="supplied: constructor provenance and index computation",
            ),
            witness_claims=_witness_claims(
                W2=True,
                W3=True,
                W5=True,
                W6=True,
            ),
            absorber_results=_absorbers(),
            no_hidden_oracle=True,
            source_generated=True,
            real_physical_candidate=False,
            record_trace="formal provenance trace from E113",
        ),
        ProtocolAttempt(
            attempt_id="strict_positive_physical_protocol_shape",
            domain="schematic positive control",
            trace_claim=(
                "A counterfactual real protocol where the physical source generates a new "
                "observable/instrument algebra and perturbations cannot factor through any fixed "
                "chemistry, search, access, or schema model."
            ),
            adapter_mapping=_adapter_mapping(
                Gamma_n="supplied: physical source context before new algebra/instrument type",
                Adm_n="supplied: admissibility predicate not decidable by prior source",
                e_n="supplied: source-generated physical construction class",
                w_n="supplied: witness of new admissibility and non-factorizing perturbation",
                Gamma_n_plus_1="supplied: successor source context with new type",
                tau_n="supplied: preserved empirical and provenance records",
            ),
            witness_claims=_witness_claims(
                W1=True,
                W2=True,
                W3=True,
                W4=True,
                W5=True,
                W6=True,
            ),
            absorber_results=_absorbers(),
            no_hidden_oracle=True,
            source_generated=True,
            real_physical_candidate=False,
            record_trace="schematic only; no real empirical trace supplied",
        ),
    ]


def evaluate_attempt(attempt: ProtocolAttempt) -> ProtocolEvaluation:
    all_adapter_fields_mapped = all(
        not attempt.adapter_mapping.get(field, "missing").startswith("missing")
        for field in ADAPTER_FIELDS
    )
    source_growth_core_supplied = any(
        attempt.witness_claims.get(gate_id, False) for gate_id in ("W1", "W2", "W3")
    )
    w1_supplied = attempt.witness_claims.get("W1", False)
    w2_w3_supplied = all(
        attempt.witness_claims.get(gate_id, False) for gate_id in ("W2", "W3")
    )
    w4_supplied = attempt.witness_claims.get("W4", False)
    w5_supplied = attempt.witness_claims.get("W5", False)
    w6_supplied = attempt.witness_claims.get("W6", False)
    targeted_absorbers_defeated = not any(attempt.absorber_results.values())
    adapter_gate_shape_passed = (
        all_adapter_fields_mapped
        and source_growth_core_supplied
        and w4_supplied
        and w5_supplied
        and w6_supplied
        and targeted_absorbers_defeated
        and attempt.no_hidden_oracle
        and attempt.source_generated
    )
    adapter_contract_passed_by_real_candidate = (
        adapter_gate_shape_passed and attempt.real_physical_candidate
    )
    physical_source_issuance_established = adapter_contract_passed_by_real_candidate

    if physical_source_issuance_established:
        verdict = "physical_adapter_passed"
        reason = "real physical protocol passes Adapter_P"
    elif adapter_gate_shape_passed:
        verdict = "schematic_or_formal_only"
        reason = "Adapter_P shape passes, but no real physical candidate is supplied"
    elif attempt.absorber_results.get("experimenter_or_instrument_schema", False):
        verdict = "absorbed_experimenter_or_instrument_schema"
        reason = "the change is introduced by analysis, instrument, or modeler schema"
    elif attempt.absorber_results.get("fixed_stochastic_or_search_process", False):
        verdict = "absorbed_fixed_search_or_evolutionary_process"
        reason = "the trace factors through fixed search, sampling, stochastic, or evolutionary dynamics"
    elif attempt.absorber_results.get("fixed_chemistry_or_reaction_network", False):
        verdict = "absorbed_fixed_chemistry"
        reason = "the trace factors through fixed chemistry or a fixed reaction network"
    elif attempt.absorber_results.get("bounded_sampling_or_database_access", False):
        verdict = "absorbed_bounded_access"
        reason = "the trace is later sampling, database, or aperture access to a fixed source"
    elif not w4_supplied:
        verdict = "rejected_no_w4_physical_protocol"
        reason = "no perturbation protocol defeats fixed chemistry/search/schema factorizations"
    elif not w1_supplied:
        verdict = "rejected_no_w1_algebra_growth"
        reason = "no non-isomorphic observable or instrument algebra growth is supplied"
    else:
        verdict = "rejected_incomplete_adapter_witness"
        reason = "the attempt misses an Adapter_P gate"

    return ProtocolEvaluation(
        attempt_id=attempt.attempt_id,
        all_adapter_fields_mapped=all_adapter_fields_mapped,
        source_growth_core_supplied=source_growth_core_supplied,
        w1_supplied=w1_supplied,
        w2_w3_supplied=w2_w3_supplied,
        w4_physical_protocol_supplied=w4_supplied,
        w5_record_preservation_supplied=w5_supplied,
        w6_absorber_control_supplied=w6_supplied,
        targeted_absorbers_defeated=targeted_absorbers_defeated,
        no_hidden_oracle=attempt.no_hidden_oracle,
        source_generated=attempt.source_generated,
        real_physical_candidate=attempt.real_physical_candidate,
        adapter_gate_shape_passed=adapter_gate_shape_passed,
        adapter_contract_passed_by_real_candidate=adapter_contract_passed_by_real_candidate,
        physical_source_issuance_established=physical_source_issuance_established,
        verdict=verdict,
        reason=reason,
    )


def run_fixture() -> dict[str, object]:
    attempts = protocol_attempts()
    evaluations = [evaluate_attempt(attempt) for attempt in attempts]
    by_id = {evaluation.attempt_id: evaluation for evaluation in evaluations}
    real_attempts = [
        evaluation for evaluation in evaluations if evaluation.real_physical_candidate
    ]
    physical_protocol_candidates = [
        "chemistry_reaction_network_trace",
        "high_throughput_search_trace",
        "evolutionary_biosynthesis_trace",
        "instrument_schema_update_trace",
    ]
    schematic = by_id["strict_positive_physical_protocol_shape"]
    formal_local = by_id["formal_local_assembly_trace_from_e113"]

    return {
        "fixture": "oi_lc_assembly_w4_w6_physical_protocol_fixture_v0_1",
        "source_artifacts": [
            "explorations/E109-online-issuance-big-swing-campaign-2026-07-01.md",
            "explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md",
            "explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md",
            "explorations/E113-oi-lc-assembly-source-adapter-fixture-2026-07-01.md",
        ],
        "protocol_attempts": [asdict(attempt) for attempt in attempts],
        "evaluations": [asdict(evaluation) for evaluation in evaluations],
        "physical_absorbers": PHYSICAL_ABSORBERS,
        "comparisons": {
            "attempt_count": len(attempts),
            "real_physical_attempt_count": len(real_attempts),
            "physical_protocol_candidate_ids": physical_protocol_candidates,
            "all_attempts_have_adapter_mapping": all(
                evaluation.all_adapter_fields_mapped for evaluation in evaluations
            ),
            "all_real_physical_attempts_absorbed": all(
                not evaluation.adapter_contract_passed_by_real_candidate
                for evaluation in real_attempts
            ),
            "w1_real_physical_candidate_found": any(
                evaluation.w1_supplied and evaluation.real_physical_candidate
                for evaluation in evaluations
            ),
            "w4_real_physical_protocol_found": any(
                evaluation.w4_physical_protocol_supplied
                and evaluation.real_physical_candidate
                for evaluation in evaluations
            ),
            "w5_record_preservation_available_for_real_attempts": all(
                evaluation.w5_record_preservation_supplied for evaluation in real_attempts
            ),
            "w6_real_physical_absorber_defeat_found": any(
                evaluation.w6_absorber_control_supplied
                and evaluation.targeted_absorbers_defeated
                and evaluation.real_physical_candidate
                for evaluation in evaluations
            ),
            "formal_local_w2_w3_preserved": formal_local.w2_w3_supplied,
            "formal_local_is_not_physical": not formal_local.real_physical_candidate,
            "schematic_positive_shape_passes_adapter_gate": schematic.adapter_gate_shape_passed,
            "schematic_positive_is_real_candidate": schematic.real_physical_candidate,
            "assembly_physical_bridge_currently_closed": True,
            "assembly_current_scope": "formal_local_w2_w3_only",
            "physical_source_issuance_established": any(
                evaluation.physical_source_issuance_established
                for evaluation in evaluations
            ),
            "TI_C020_reopened": False,
            "next_gate": NEXT_GATE,
        },
        "verdict": {
            "Issue[S]^assembly_local": True,
            "Issue[S]^physical": False,
            "TI_C020_reopened": False,
            "claim_status_change": "none",
            "assembly_can_carry_current_evidence": "formal_local_W2_W3_only",
            "all_real_physical_protocol_attempts_absorbed": True,
            "best_result": (
                "Assembly supplies a formal/local W2-W3 witness, but every real empirical "
                "assembly protocol attempted here factors through fixed chemistry, fixed search "
                "or stochastic exploration, bounded access, instrument/modeler schema, or fixed "
                "observable algebra. No W1 or W4 physical witness is found."
            ),
            "next_gate": NEXT_GATE,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the Assembly W4-W6 physical protocol fixture."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_fixture()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
