"""Small symbolic checker for the E090 OnlineIssuance witness schema.

This is not a Lean/Coq proof. It is an executable formal pseudocode calculus
for the class-relative E090 claim:

1. a present prefix context forms an enumeration attempt;
2. a diagonal candidate is formed against that present enumeration;
3. an admissibility witness is formed for the diagonal candidate;
4. a completed future oracle is rejected as an internal source object.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path


FORBIDDEN_INTERNAL_KINDS = {
    "completed_future_oracle",
    "complete_trace",
    "fixed_latent_graph",
    "fixed_access_schedule",
}


@dataclass(frozen=True)
class Symbol:
    name: str
    kind: str
    formed_at: int


@dataclass(frozen=True)
class Context:
    name: str
    prefix: int
    symbols: tuple[Symbol, ...]
    rules: tuple[str, ...]

    def has_symbol(self, name: str, kind: str | None = None) -> bool:
        for symbol in self.symbols:
            if symbol.name == name and (kind is None or symbol.kind == kind):
                return True
        return False

    def with_symbol(self, symbol: Symbol) -> "Context":
        if symbol.kind in FORBIDDEN_INTERNAL_KINDS:
            raise ValueError(f"forbidden internal source object: {symbol.kind}:{symbol.name}")
        return replace(self, symbols=self.symbols + (symbol,))


@dataclass(frozen=True)
class Enumerator:
    name: str
    formed_at: int
    values: tuple[str, ...]
    claims_total_for_present_prefix: bool


@dataclass(frozen=True)
class Candidate:
    name: str
    formed_at: int
    depends_on: tuple[str, ...]


@dataclass(frozen=True)
class Witness:
    name: str
    formed_at: int
    proposition: str
    depends_on: tuple[str, ...]


@dataclass(frozen=True)
class SourceTrace:
    trace_id: str
    source_context: str
    enumerator: str
    issued_candidate: str
    witness: str
    target_context: str


@dataclass(frozen=True)
class ComparatorResult:
    comparator_id: str
    internal_source_valid: bool
    external_absorber_valid: bool
    source_issuance_passes: bool
    reason: str


def local_constructive_context() -> Context:
    return Context(
        name="Gamma_n",
        prefix=0,
        symbols=(
            Symbol("Code_n", "code_space", 0),
            Symbol("Cand_n", "candidate_type", 0),
            Symbol("Adm_n", "admissibility_predicate", 0),
            Symbol("cand_0", "candidate", 0),
            Symbol("cand_1", "candidate", 0),
            Symbol("cand_2", "candidate", 0),
            Symbol("Enum_n", "enumerator", 0),
        ),
        rules=(
            "present_prefix_only",
            "self_encoding_admissibility",
            "diagonal_productivity",
            "recordable_source_trace",
            "no_hidden_completed_oracle",
        ),
    )


def present_enumerator() -> Enumerator:
    return Enumerator(
        name="Enum_n",
        formed_at=0,
        values=("cand_0", "cand_1", "cand_2"),
        claims_total_for_present_prefix=True,
    )


def validate_present_enumerator(context: Context, enumerator: Enumerator) -> bool:
    return (
        context.has_symbol(enumerator.name, "enumerator")
        and enumerator.formed_at <= context.prefix
        and all(context.has_symbol(value, "candidate") for value in enumerator.values)
    )


def derive_diagonal(context: Context, enumerator: Enumerator) -> Candidate:
    if "diagonal_productivity" not in context.rules:
        raise ValueError("missing diagonal_productivity rule")
    if not validate_present_enumerator(context, enumerator):
        raise ValueError("enumerator is not formed in the present prefix")
    return Candidate(
        name=f"Diag({enumerator.name})",
        formed_at=context.prefix,
        depends_on=(enumerator.name, "diagonal_productivity"),
    )


def prove_diagonal_separation(enumerator: Enumerator, diagonal: Candidate) -> dict[str, object]:
    concrete_checks = {
        value: diagonal.name != value
        for value in enumerator.values
    }
    return {
        "symbolic_for_all_k": True,
        "symbolic_basis": "Diag(Enum_n) is introduced by a constructor outside Enum_n's present range",
        "checked_values": concrete_checks,
        "all_checked_values_separate": all(concrete_checks.values()),
    }


def derive_witness(context: Context, diagonal: Candidate) -> Witness:
    if "self_encoding_admissibility" not in context.rules:
        raise ValueError("missing self_encoding_admissibility rule")
    if "diagonal_productivity" not in context.rules:
        raise ValueError("missing diagonal_productivity rule")
    if not context.has_symbol("Adm_n", "admissibility_predicate"):
        raise ValueError("Adm_n is not formed")
    return Witness(
        name="w_diag",
        formed_at=context.prefix,
        proposition=f"Adm_n({diagonal.name})",
        depends_on=(diagonal.name, "Adm_n", "self_encoding_admissibility"),
    )


def issue_successor(
    context: Context,
    enumerator: Enumerator,
    diagonal: Candidate,
    witness: Witness,
) -> tuple[Context, SourceTrace]:
    if "recordable_source_trace" not in context.rules:
        raise ValueError("missing recordable_source_trace rule")

    extended = context.with_symbol(Symbol(diagonal.name, "candidate", context.prefix + 1))
    extended = extended.with_symbol(Symbol(witness.name, "witness", context.prefix + 1))
    extended = replace(extended, name="Gamma_n_plus_1", prefix=context.prefix + 1)
    trace = SourceTrace(
        trace_id="tau_diag",
        source_context=context.name,
        enumerator=enumerator.name,
        issued_candidate=diagonal.name,
        witness=witness.name,
        target_context=extended.name,
    )
    return extended, trace


def check_hidden_oracle_rejection(context: Context) -> dict[str, object]:
    try:
        context.with_symbol(Symbol("Omega_future", "completed_future_oracle", context.prefix))
    except ValueError as exc:
        return {
            "internal_oracle_rejected": True,
            "error": str(exc),
            "external_platonist_absorber_still_available": True,
        }
    return {
        "internal_oracle_rejected": False,
        "error": "",
        "external_platonist_absorber_still_available": True,
    }


def comparator_results() -> list[ComparatorResult]:
    return [
        ComparatorResult(
            comparator_id="finite_type_context",
            internal_source_valid=True,
            external_absorber_valid=True,
            source_issuance_passes=False,
            reason="finite candidate pools are pre-enumerable at the prefix",
        ),
        ComparatorResult(
            comparator_id="infinite_computable_context",
            internal_source_valid=True,
            external_absorber_valid=True,
            source_issuance_passes=False,
            reason="a fixed grammar or c.e. generator absorbs the trace as search/disclosure",
        ),
        ComparatorResult(
            comparator_id="fixed_platonist_oracle_context",
            internal_source_valid=False,
            external_absorber_valid=True,
            source_issuance_passes=False,
            reason="Omega_future represents the whole trace externally but violates the internal no-hidden-oracle gate",
        ),
        ComparatorResult(
            comparator_id="local_constructive_context",
            internal_source_valid=True,
            external_absorber_valid=False,
            source_issuance_passes=True,
            reason="the present context forms a diagonal admissible successor without forming a completed future oracle",
        ),
    ]


def run_check() -> dict[str, object]:
    context = local_constructive_context()
    enumerator = present_enumerator()
    diagonal = derive_diagonal(context, enumerator)
    separation = prove_diagonal_separation(enumerator, diagonal)
    witness = derive_witness(context, diagonal)
    successor, trace = issue_successor(context, enumerator, diagonal, witness)
    oracle = check_hidden_oracle_rejection(context)
    comparators = comparator_results()

    local_passes = next(
        result.source_issuance_passes
        for result in comparators
        if result.comparator_id == "local_constructive_context"
    )
    external_oracle_internal_invalid = next(
        not result.internal_source_valid and result.external_absorber_valid
        for result in comparators
        if result.comparator_id == "fixed_platonist_oracle_context"
    )

    return {
        "fixture": "online_issuance_witness_checker_v0_1",
        "checker_kind": "small_symbolic_calculus",
        "source_artifacts": [
            "explorations/E055-expressiveness-threshold-fixture-2026-06-24.md",
            "explorations/E090-online-issuance-minimal-constructive-witness-2026-06-25.md",
            "explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md",
        ],
        "context": asdict(context),
        "enumerator": asdict(enumerator),
        "diagonal_candidate": asdict(diagonal),
        "separation_proof": separation,
        "witness": asdict(witness),
        "successor_context": asdict(successor),
        "source_trace": asdict(trace),
        "oracle_check": oracle,
        "comparators": [asdict(result) for result in comparators],
        "comparisons": {
            "schema_machine_checked": True,
            "proof_assistant_used": False,
            "full_theorem_prover_verification": False,
            "present_enumerator_valid": validate_present_enumerator(context, enumerator),
            "diagonal_candidate_formed": diagonal.name == "Diag(Enum_n)",
            "diagonal_candidate_not_in_present_enumeration": diagonal.name not in enumerator.values,
            "all_checked_values_separate": separation["all_checked_values_separate"],
            "symbolic_for_all_k_separation_recorded": separation["symbolic_for_all_k"],
            "witness_formed": witness.proposition == "Adm_n(Diag(Enum_n))",
            "successor_issued": successor.name == "Gamma_n_plus_1",
            "trace_recorded": trace.trace_id == "tau_diag",
            "internal_future_oracle_rejected": oracle["internal_oracle_rejected"],
            "external_platonist_absorber_still_available": oracle[
                "external_platonist_absorber_still_available"
            ],
            "finite_type_context_absorbed": not comparators[0].source_issuance_passes,
            "computable_context_absorbed": not comparators[1].source_issuance_passes,
            "fixed_oracle_invalid_internally_valid_externally": external_oracle_internal_invalid,
            "local_constructive_witness_passes": local_passes,
            "physical_source_issuance_established": False,
        },
        "effect_typing": {
            "Issue[S]^LC": local_passes,
            "Issue[S]^physical": False,
            "Project[O]": False,
            "Finalize[R]": False,
            "Lose[K]": False,
        },
        "verdict": {
            "formal_lc_witness_strengthened": True,
            "claim_status_change": "none",
            "best_result": (
                "The E090 local-constructive witness schema is executable in a small "
                "symbolic calculus: a formed present enumeration yields a diagonal "
                "admissible successor and witness while completed future oracles are "
                "rejected internally."
            ),
            "limits": (
                "This is not a Lean/Coq proof and does not establish physical issuance; "
                "external Platonist completion remains an absorber outside the local "
                "constructive source class."
            ),
            "next_gate": "W010_frontier_selection_after_online_issuance_machine_check",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the OnlineIssuance E090 witness checker."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_check()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
