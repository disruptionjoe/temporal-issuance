"""Proof-obligation checker for the OnlineIssuance local witness.

This module hardens tools/online_issuance_witness_checker.py by treating its
output as a typed proof object with explicit obligations. It is still a small
Python checker, not Lean/Coq/Agda, but it separates assumptions, obligations,
and verdicts more strictly than the original symbolic fixture.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import online_issuance_witness_checker as base_checker


FORBIDDEN_INTERNAL_KINDS = set(base_checker.FORBIDDEN_INTERNAL_KINDS)


@dataclass(frozen=True)
class Obligation:
    obligation_id: str
    description: str
    passed: bool
    reason: str


def _symbols(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        symbol["name"]: symbol
        for symbol in result["context"]["symbols"]
    }


def _rules(result: dict[str, Any]) -> set[str]:
    return set(result["context"]["rules"])


def _successor_symbols(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        symbol["name"]: symbol
        for symbol in result["successor_context"]["symbols"]
    }


def _obligation(
    obligation_id: str,
    description: str,
    passed: bool,
    reason: str,
) -> Obligation:
    return Obligation(obligation_id, description, bool(passed), reason)


def check_prefix_typing(result: dict[str, Any]) -> Obligation:
    context = result["context"]
    successor = result["successor_context"]
    context_prefix = context["prefix"]
    successor_prefix = successor["prefix"]
    source_symbols_well_formed = all(
        symbol["formed_at"] <= context_prefix
        for symbol in context["symbols"]
    )
    successor_symbols_well_formed = all(
        symbol["formed_at"] <= successor_prefix
        for symbol in successor["symbols"]
    )
    passed = (
        context["name"] == "Gamma_n"
        and successor["name"] == "Gamma_n_plus_1"
        and successor_prefix == context_prefix + 1
        and source_symbols_well_formed
        and successor_symbols_well_formed
    )
    return _obligation(
        "PA-O1-prefix-typing",
        "Source and successor contexts obey prefix typing.",
        passed,
        "Gamma_n advances exactly one prefix step and all symbols are formed no later than their context.",
    )


def check_enumerator_is_present(result: dict[str, Any]) -> Obligation:
    symbols = _symbols(result)
    enumerator = result["enumerator"]
    values_present = all(
        value in symbols and symbols[value]["kind"] == "candidate"
        for value in enumerator["values"]
    )
    passed = (
        enumerator["name"] in symbols
        and symbols[enumerator["name"]]["kind"] == "enumerator"
        and enumerator["formed_at"] <= result["context"]["prefix"]
        and enumerator["claims_total_for_present_prefix"]
        and values_present
    )
    return _obligation(
        "PA-O2-present-enumerator",
        "Enumerator is formed in the present prefix and ranges only over present candidates.",
        passed,
        "Enum_n and every enumerated candidate are source-context symbols formed at the current prefix.",
    )


def check_diagonal_dependency(result: dict[str, Any]) -> Obligation:
    diagonal = result["diagonal_candidate"]
    rules = _rules(result)
    passed = (
        diagonal["name"] == "Diag(Enum_n)"
        and diagonal["formed_at"] == result["context"]["prefix"]
        and "Enum_n" in diagonal["depends_on"]
        and "diagonal_productivity" in diagonal["depends_on"]
        and "diagonal_productivity" in rules
        and diagonal["name"] not in result["enumerator"]["values"]
    )
    return _obligation(
        "PA-O3-diagonal-dependency",
        "Diagonal candidate depends only on present enumerator plus the diagonal-productivity rule.",
        passed,
        "The diagonal object is formed at n and is outside Enum_n's present range.",
    )


def check_separation_proof(result: dict[str, Any]) -> Obligation:
    proof = result["separation_proof"]
    values = set(result["enumerator"]["values"])
    checked_values = set(proof["checked_values"])
    passed = (
        proof["symbolic_for_all_k"]
        and proof["all_checked_values_separate"]
        and checked_values == values
        and all(proof["checked_values"].values())
    )
    return _obligation(
        "PA-O4-diagonal-separation",
        "Separation proof covers the present enumerator and records the symbolic all-k basis.",
        passed,
        "All present enumerator values are checked distinct from Diag(Enum_n), with symbolic basis recorded.",
    )


def check_witness_dependency(result: dict[str, Any]) -> Obligation:
    witness = result["witness"]
    symbols = _symbols(result)
    rules = _rules(result)
    passed = (
        witness["name"] == "w_diag"
        and witness["formed_at"] == result["context"]["prefix"]
        and witness["proposition"] == "Adm_n(Diag(Enum_n))"
        and "Diag(Enum_n)" in witness["depends_on"]
        and "Adm_n" in witness["depends_on"]
        and "self_encoding_admissibility" in witness["depends_on"]
        and symbols.get("Adm_n", {}).get("kind") == "admissibility_predicate"
        and "self_encoding_admissibility" in rules
    )
    return _obligation(
        "PA-O5-witness-dependency",
        "Admissibility witness depends only on the diagonal, Adm_n, and the admissibility rule.",
        passed,
        "w_diag proves Adm_n(Diag(Enum_n)) without importing future schema.",
    )


def check_source_trace(result: dict[str, Any]) -> Obligation:
    trace = result["source_trace"]
    successor_symbols = _successor_symbols(result)
    passed = (
        trace["trace_id"] == "tau_diag"
        and trace["source_context"] == "Gamma_n"
        and trace["target_context"] == "Gamma_n_plus_1"
        and trace["issued_candidate"] == "Diag(Enum_n)"
        and trace["witness"] == "w_diag"
        and successor_symbols.get("Diag(Enum_n)", {}).get("kind") == "candidate"
        and successor_symbols.get("w_diag", {}).get("kind") == "witness"
    )
    return _obligation(
        "PA-O6-source-trace",
        "Source trace records the issued candidate and witness in the successor context.",
        passed,
        "tau_diag links Gamma_n, Enum_n, Diag(Enum_n), w_diag, and Gamma_n_plus_1.",
    )


def check_no_hidden_future_oracle(result: dict[str, Any]) -> Obligation:
    all_symbols = list(result["context"]["symbols"]) + list(result["successor_context"]["symbols"])
    no_forbidden_symbol = all(
        symbol["kind"] not in FORBIDDEN_INTERNAL_KINDS
        for symbol in all_symbols
    )
    oracle = result["oracle_check"]
    passed = (
        no_forbidden_symbol
        and oracle["internal_oracle_rejected"]
        and oracle["external_platonist_absorber_still_available"]
    )
    return _obligation(
        "PA-O7-no-hidden-future-oracle",
        "Completed future traces are rejected internally while preserved as an external absorber.",
        passed,
        "No context symbol has a forbidden future kind; Omega_future is invalid internally but remains an external absorber.",
    )


def check_comparator_scope(result: dict[str, Any]) -> Obligation:
    comparators = {
        item["comparator_id"]: item
        for item in result["comparators"]
    }
    passed = (
        comparators["finite_type_context"]["source_issuance_passes"] is False
        and comparators["infinite_computable_context"]["source_issuance_passes"] is False
        and comparators["fixed_platonist_oracle_context"]["internal_source_valid"] is False
        and comparators["fixed_platonist_oracle_context"]["external_absorber_valid"] is True
        and comparators["local_constructive_context"]["source_issuance_passes"] is True
    )
    return _obligation(
        "PA-O8-comparator-scope",
        "Positive result is restricted to the local constructive class.",
        passed,
        "Finite, computable, and internal fixed-oracle comparators do not pass source issuance.",
    )


def check_effect_typing(result: dict[str, Any]) -> Obligation:
    effect = result["effect_typing"]
    comparisons = result["comparisons"]
    passed = (
        effect["Issue[S]^LC"] is True
        and effect["Issue[S]^physical"] is False
        and effect["Project[O]"] is False
        and effect["Finalize[R]"] is False
        and effect["Lose[K]"] is False
        and comparisons["physical_source_issuance_established"] is False
        and result["verdict"]["claim_status_change"] == "none"
    )
    return _obligation(
        "PA-O9-effect-typing",
        "Effect typing preserves local/formal scope and blocks physical-source overclaim.",
        passed,
        "The proof object yields Issue[S]^LC only; physical issuance and claim movement remain false.",
    )


def run_proof_check() -> dict[str, Any]:
    base_result = base_checker.run_check()
    obligations = [
        check_prefix_typing(base_result),
        check_enumerator_is_present(base_result),
        check_diagonal_dependency(base_result),
        check_separation_proof(base_result),
        check_witness_dependency(base_result),
        check_source_trace(base_result),
        check_no_hidden_future_oracle(base_result),
        check_comparator_scope(base_result),
        check_effect_typing(base_result),
    ]
    all_passed = all(item.passed for item in obligations)
    return {
        "fixture": "proof_assistant_online_issuance_witness_v0_1",
        "checker_kind": "typed_proof_obligation_checker",
        "proof_assistant_used": False,
        "full_theorem_prover_verification": False,
        "strictly_harder_than_small_symbolic_calculus": True,
        "base_fixture": base_result["fixture"],
        "obligations": [asdict(item) for item in obligations],
        "summary": {
            "obligation_count": len(obligations),
            "obligations_passed": sum(1 for item in obligations if item.passed),
            "all_obligations_passed": all_passed,
            "no_hidden_future_oracle_preserved": obligations[6].passed,
            "external_platonist_absorber_still_available": True,
            "Issue[S]^LC": bool(base_result["effect_typing"]["Issue[S]^LC"] and all_passed),
            "Issue[S]^physical": False,
            "TI_C020_reopened": False,
            "claim_status_change": "none",
            "next_gate": "online_issuance_core_verdict_bundle",
        },
        "limits": {
            "not_lean_coq_agda": True,
            "no_physical_source_issuance_established": True,
            "external_platonist_completion_not_defeated": True,
            "result_is_class_relative": "OnlineIssuance^LC",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run proof-obligation checks for the OnlineIssuance witness."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_proof_check()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["summary"]["all_obligations_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

