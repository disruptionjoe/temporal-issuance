#!/usr/bin/env python3
"""T2 bounded completion-barrier theorem contract.

This Wave 8 fixture packages the E172/T1 theorem target into an explicit
bounded theorem contract. It is a proof contract over the current post-H8
Adapter_P trace class, not a universal physics no-go, physical-source theorem,
D-FORK decision, claim movement, or TI-C020 reopening.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import t1_completion_barrier_theorem_target as t1


BOUNDED_THEOREM_CONTRACT_PACKAGED = "BOUNDED_THEOREM_CONTRACT_PACKAGED"
COUNTEREXAMPLE_GATE_ACTIVE = "COUNTEREXAMPLE_GATE_ACTIVE"
UNIVERSAL_PHYSICAL_NO_GO_REJECTED = "UNIVERSAL_PHYSICAL_NO_GO_REJECTED"
PHYSICAL_SOURCE_THEOREM_REJECTED = "PHYSICAL_SOURCE_THEOREM_REJECTED"
D_FORK_DECISION_REJECTED = "D_FORK_DECISION_REJECTED"
CONTRACT_UNSUPPORTED = "CONTRACT_UNSUPPORTED"


ASSUMPTION_IDS = (
    "post_h8_record_preserving_adapter_p_trace",
    "h1_completion_channels_exercised",
    "h2_h7_preservation_fields_carried",
    "h6_bounded_conditional_boundary",
    "h8_signature_bundle_not_decision_procedure",
    "no_new_concrete_counterexample_packet_supplied",
)

SCOPE_LIMIT_IDS = (
    "bounded_to_current_adapter_p_trace_class",
    "not_universal_over_all_physics",
    "not_physical_source_issuance",
    "not_d_fork_decision",
    "revisable_by_counterexample_contract",
)


@dataclass(frozen=True)
class ContractClause:
    clause_id: str
    verdict: str
    theorem_clause: bool
    terminal_overclaim: bool
    statement: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "clause_id": self.clause_id,
            "verdict": self.verdict,
            "theorem_clause": self.theorem_clause,
            "terminal_overclaim": self.terminal_overclaim,
            "statement": self.statement,
        }


def _decision_by_id(t1_result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {decision["target_id"]: decision for decision in t1_result["decisions"]}


def package_clauses(t1_result: dict[str, Any]) -> tuple[ContractClause, ...]:
    decisions = _decision_by_id(t1_result)
    bounded = decisions["bounded_adapter_p_completion_barrier"]
    counterexample = decisions["new_packet_counterexample_contract"]

    bounded_ready = (
        t1_result["fixed_floor_satisfied"]
        and t1_result["theorem_contract_ready"]
        and bounded["verdict"] == t1.BOUNDED_THEOREM_TARGET_READY
    )
    counterexample_ready = (
        t1_result["counterexample_contract_ready"]
        and counterexample["verdict"] == t1.COUNTEREXAMPLE_CONTRACT_READY
    )

    return (
        ContractClause(
            clause_id="bounded_completion_barrier_contract",
            verdict=(
                BOUNDED_THEOREM_CONTRACT_PACKAGED
                if bounded_ready
                else CONTRACT_UNSUPPORTED
            ),
            theorem_clause=bounded_ready,
            terminal_overclaim=False,
            statement=(
                "Within the current post-H8 record-preserving Adapter_P trace "
                "class, a candidate does not establish source issuance unless "
                "it supplies the named counterexample contract defeating all "
                "completion channels, H6/H8 stops, and whole-family completion."
            ),
        ),
        ContractClause(
            clause_id="counterexample_activation_gate",
            verdict=(
                COUNTEREXAMPLE_GATE_ACTIVE
                if counterexample_ready
                else CONTRACT_UNSUPPORTED
            ),
            theorem_clause=False,
            terminal_overclaim=False,
            statement=(
                "A new concrete H7-admitted packet can revise or kill the "
                "bounded contract only by satisfying every counterexample "
                "obligation inherited from E172/T1."
            ),
        ),
        ContractClause(
            clause_id="reject_universal_physical_no_go",
            verdict=UNIVERSAL_PHYSICAL_NO_GO_REJECTED,
            theorem_clause=False,
            terminal_overclaim=True,
            statement=(
                "The contract is bounded to the current trace class and does "
                "not state that all physical novelty is impossible."
            ),
        ),
        ContractClause(
            clause_id="reject_physical_source_theorem",
            verdict=PHYSICAL_SOURCE_THEOREM_REJECTED,
            theorem_clause=False,
            terminal_overclaim=True,
            statement=(
                "H6 bounded formal/local OSAG support remains conditional and "
                "does not establish physical source issuance."
            ),
        ),
        ContractClause(
            clause_id="reject_d_fork_decision",
            verdict=D_FORK_DECISION_REJECTED,
            theorem_clause=False,
            terminal_overclaim=True,
            statement=(
                "H8 remains a signature bundle and does not decide the "
                "non-computable FTS/Godelian D-FORK bit."
            ),
        ),
    )


def run_theorem_contract() -> dict[str, Any]:
    t1_result = t1.run_theorem_target()
    clauses = package_clauses(t1_result)
    theorem_clause_ids = [
        clause.clause_id for clause in clauses if clause.theorem_clause
    ]
    terminal_overclaim_clause_ids = [
        clause.clause_id for clause in clauses if clause.terminal_overclaim
    ]
    contract_ready = (
        "bounded_completion_barrier_contract" in theorem_clause_ids
        and any(
            clause.verdict == COUNTEREXAMPLE_GATE_ACTIVE for clause in clauses
        )
    )

    return {
        "fixture_id": "t2_bounded_completion_barrier_theorem_contract",
        "kind": "bounded_completion_barrier_theorem_contract_package",
        "depends_on_fixture_id": t1_result["fixture_id"],
        "assumption_ids": list(ASSUMPTION_IDS),
        "scope_limit_ids": list(SCOPE_LIMIT_IDS),
        "contract_ready": contract_ready,
        "theorem_contract_id": "bounded_adapter_p_completion_barrier_v1",
        "bounded_theorem_statement": (
            "For the current post-H8 record-preserving Adapter_P trace class, "
            "source issuance is not established without a new concrete "
            "H7-admitted packet satisfying the E172 counterexample obligations."
        ),
        "counterexample_obligations": t1_result["counterexample_obligations"],
        "counterexample_gate_active": t1_result[
            "counterexample_contract_ready"
        ],
        "theorem_clause_ids": theorem_clause_ids,
        "terminal_overclaim_clause_ids": terminal_overclaim_clause_ids,
        "blocks_universal_physical_no_go": True,
        "blocks_physical_source_theorem": True,
        "blocks_d_fork_decision": True,
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "claim_status_change": "none",
        "t2_result": (
            "bounded_completion_barrier_theorem_contract_packaged_with_"
            "counterexample_gate"
        ),
        "next_track_1_recommendation": (
            "Wait for a new concrete H7-admitted packet or run a deliberately "
            "selected gate only if it tests the T2 contract. Do not repeat T2 "
            "or convert it into universal physical no-go language."
        ),
        "honest_current_result": (
            "T2 packages the bounded theorem contract as a repo-local proof "
            "contract over the current Adapter_P trace class. It creates no "
            "claim movement and no physical-source result."
        ),
        "clauses": [clause.as_dict() for clause in clauses],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "tests/artifacts/"
            "t2_bounded_completion_barrier_theorem_contract_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_theorem_contract()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
