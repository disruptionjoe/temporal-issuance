#!/usr/bin/env python3
"""T1 completion-barrier theorem target.

This Wave 7 fixture turns the repeated post-H8 completion absorptions into a
bounded theorem contract. It does not prove a universal physics no-go, decide
D-FORK, move claims, or reopen TI-C020.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import h6_completion_boundary_audit as h6
import h8_d_fork_regime_signature_bundle as h8
import whole_family_completion_barrier_classifier as h1


BOUNDED_THEOREM_TARGET_READY = "BOUNDED_THEOREM_TARGET_READY"
CONDITIONAL_FORMAL_THEOREM_TARGET_READY = (
    "CONDITIONAL_FORMAL_THEOREM_TARGET_READY"
)
COUNTEREXAMPLE_CONTRACT_READY = "COUNTEREXAMPLE_CONTRACT_READY"
UNIVERSAL_PHYSICAL_NO_GO_NOT_READY = "UNIVERSAL_PHYSICAL_NO_GO_NOT_READY"
PHYSICAL_SOURCE_THEOREM_BLOCKED = "PHYSICAL_SOURCE_THEOREM_BLOCKED"
D_FORK_DECISION_THEOREM_BLOCKED = "D_FORK_DECISION_THEOREM_BLOCKED"
THEOREM_TARGET_UNSUPPORTED = "THEOREM_TARGET_UNSUPPORTED"


COUNTEREXAMPLE_OBLIGATIONS = (
    "new_concrete_packet",
    "h7_admitted",
    "maps_all_adapter_p_fields",
    "preserves_tau_n",
    "preserves_preserve_n",
    "preserves_represented_family_index",
    "preserves_candidate_provenance",
    "no_hidden_completion_oracle",
    "no_imported_law_or_schema",
    "not_readout_or_finality_only",
    "defeats_value_completion",
    "defeats_name_completion",
    "defeats_provenance_action_completion",
    "defeats_capability_completion",
    "supplies_w1_non_isomorphic_physical_algebra",
    "supplies_w4_perturbation_non_factorization",
    "supplies_w5_record_preservation_comparison",
    "defeats_whole_family_completion",
    "does_not_treat_h8_as_d_fork_decision",
)


@dataclass(frozen=True)
class TheoremTarget:
    target_id: str
    title: str
    scope: str
    conclusion: str
    uses_h1_completion_floor: bool
    uses_h6_boundary: bool
    uses_h8_signature_bundle: bool
    formal_local_only: bool
    depends_on_new_packet: bool
    universal_over_all_physics: bool
    requires_physical_source_claim: bool
    asserts_d_fork_decision: bool
    has_counterexample_contract: bool


@dataclass(frozen=True)
class TargetDecision:
    target_id: str
    verdict: str
    theorem_target_ready: bool
    terminal_overclaim: bool
    supports_track_1: bool
    counterexample_obligations: tuple[str, ...]
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "target_id": self.target_id,
            "verdict": self.verdict,
            "theorem_target_ready": self.theorem_target_ready,
            "terminal_overclaim": self.terminal_overclaim,
            "supports_track_1": self.supports_track_1,
            "counterexample_obligations": list(self.counterexample_obligations),
            "reason": self.reason,
        }


def fixed_input_summary() -> dict[str, Any]:
    h1_result = h1.run_classifier()
    h6_result = h6.run_boundary_audit()
    h8_result = h8.run_signature_bundle()
    return {
        "h1_result": h1_result["h1_result"],
        "h1_all_completion_channels_exercised": (
            h1_result["all_completion_channels_exercised"]
        ),
        "h1_preaction_family_noncompletion_required_for_escape": (
            h1_result["preaction_family_noncompletion_required_for_escape"]
        ),
        "h6_result": h6_result["h6_result"],
        "h6_completion_boundary_set": h6_result["completion_boundary_set"],
        "h6_formal_local_support_boundary": (
            h6_result["formal_local_support_boundary"]
        ),
        "h8_result": h8_result["kind"],
        "h8_d_fork_boundary_reportable": (
            h8_result["d_fork_boundary_reportable"]
        ),
        "h8_curvature_separates_declared_regimes": (
            h8_result["curvature_separates_declared_regimes"]
        ),
        "h8_track_1_signature_row_ids": h8_result["track_1_signature_row_ids"],
        "h8_d_fork_status": h8_result["fixed_inputs"]["d_fork_status"],
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "claim_status_change": "none",
    }


def fixed_floor_satisfied(summary: dict[str, Any]) -> bool:
    return bool(
        summary["h1_all_completion_channels_exercised"]
        and summary["h1_preaction_family_noncompletion_required_for_escape"]
        and summary["h6_completion_boundary_set"]
        and summary["h6_formal_local_support_boundary"]
        == "bounded_conditional_form"
        and summary["h8_d_fork_boundary_reportable"]
        and summary["h8_d_fork_status"]
        == "non_computable_structural_bit_not_decided"
    )


def theorem_targets() -> tuple[TheoremTarget, ...]:
    return (
        TheoremTarget(
            target_id="bounded_adapter_p_completion_barrier",
            title="Bounded Adapter_P completion barrier",
            scope=(
                "post-H8 record-preserving Adapter_P traces that carry H1 "
                "completion channels, H2/H7 preservation fields, the H6 "
                "bounded-conditional boundary, and the H8 signature bundle"
            ),
            conclusion=(
                "A candidate in this bounded class does not establish source "
                "issuance unless it supplies the counterexample contract: a new "
                "concrete H7-admitted packet defeating all completion channels, "
                "the H6/H8 stops, and whole-family completion."
            ),
            uses_h1_completion_floor=True,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=False,
            depends_on_new_packet=False,
            universal_over_all_physics=False,
            requires_physical_source_claim=False,
            asserts_d_fork_decision=False,
            has_counterexample_contract=True,
        ),
        TheoremTarget(
            target_id="formal_local_osag_conditional",
            title="Formal/local OSAG conditional theorem",
            scope="H7-admitted bounded formal/local OSAG support after H6",
            conclusion=(
                "Formal/local OSAG support is internal to the bounded "
                "construction only as conditional form, not as full source "
                "structure or physical Adapter_P passage."
            ),
            uses_h1_completion_floor=True,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=True,
            depends_on_new_packet=False,
            universal_over_all_physics=False,
            requires_physical_source_claim=False,
            asserts_d_fork_decision=False,
            has_counterexample_contract=False,
        ),
        TheoremTarget(
            target_id="universal_physical_no_go",
            title="Universal physical no-go",
            scope="all physical novelty or all future physics candidates",
            conclusion=(
                "No physical system can ever instantiate source issuance."
            ),
            uses_h1_completion_floor=True,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=False,
            depends_on_new_packet=False,
            universal_over_all_physics=True,
            requires_physical_source_claim=False,
            asserts_d_fork_decision=False,
            has_counterexample_contract=False,
        ),
        TheoremTarget(
            target_id="physical_source_from_bounded_osag",
            title="Physical source theorem from bounded OSAG",
            scope="H6 bounded formal/local OSAG support",
            conclusion=(
                "Bounded formal/local OSAG support establishes physical source "
                "issuance."
            ),
            uses_h1_completion_floor=True,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=False,
            depends_on_new_packet=False,
            universal_over_all_physics=False,
            requires_physical_source_claim=True,
            asserts_d_fork_decision=False,
            has_counterexample_contract=False,
        ),
        TheoremTarget(
            target_id="d_fork_decision_from_h8",
            title="D-FORK decision from H8 signatures",
            scope="H8 FTS/Godelian signature bundle",
            conclusion=(
                "The H8 signature bundle decides whether the operative source is "
                "finite-type-space or Godelian."
            ),
            uses_h1_completion_floor=False,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=False,
            depends_on_new_packet=False,
            universal_over_all_physics=False,
            requires_physical_source_claim=False,
            asserts_d_fork_decision=True,
            has_counterexample_contract=False,
        ),
        TheoremTarget(
            target_id="new_packet_counterexample_contract",
            title="New packet counterexample contract",
            scope="future concrete packet intake",
            conclusion=(
                "A future packet can kill the bounded theorem target only by "
                "satisfying every named counterexample obligation."
            ),
            uses_h1_completion_floor=True,
            uses_h6_boundary=True,
            uses_h8_signature_bundle=True,
            formal_local_only=False,
            depends_on_new_packet=True,
            universal_over_all_physics=False,
            requires_physical_source_claim=False,
            asserts_d_fork_decision=False,
            has_counterexample_contract=True,
        ),
    )


def classify_target(
    target: TheoremTarget, summary: dict[str, Any]
) -> TargetDecision:
    floor = fixed_floor_satisfied(summary)
    if target.universal_over_all_physics:
        return TargetDecision(
            target_id=target.target_id,
            verdict=UNIVERSAL_PHYSICAL_NO_GO_NOT_READY,
            theorem_target_ready=False,
            terminal_overclaim=True,
            supports_track_1=False,
            counterexample_obligations=(),
            reason=(
                "The repo has only a bounded Adapter_P trace class, not a "
                "universe of all physical novelty."
            ),
        )
    if target.asserts_d_fork_decision:
        return TargetDecision(
            target_id=target.target_id,
            verdict=D_FORK_DECISION_THEOREM_BLOCKED,
            theorem_target_ready=False,
            terminal_overclaim=True,
            supports_track_1=False,
            counterexample_obligations=(),
            reason=(
                "H8 is a signature bundle and explicitly does not decide the "
                "non-computable FTS/Godelian structural bit."
            ),
        )
    if target.requires_physical_source_claim:
        return TargetDecision(
            target_id=target.target_id,
            verdict=PHYSICAL_SOURCE_THEOREM_BLOCKED,
            theorem_target_ready=False,
            terminal_overclaim=True,
            supports_track_1=False,
            counterexample_obligations=(),
            reason=(
                "H6 bounded formal/local support is not physical Adapter_P "
                "passage and cannot be upgraded into source issuance."
            ),
        )
    if target.depends_on_new_packet and target.has_counterexample_contract:
        return TargetDecision(
            target_id=target.target_id,
            verdict=COUNTEREXAMPLE_CONTRACT_READY,
            theorem_target_ready=False,
            terminal_overclaim=False,
            supports_track_1=True,
            counterexample_obligations=COUNTEREXAMPLE_OBLIGATIONS,
            reason=(
                "The packet route is not a theorem by itself, but it is the "
                "activation contract that would kill or revise the bounded "
                "theorem target."
            ),
        )
    if target.formal_local_only and floor:
        return TargetDecision(
            target_id=target.target_id,
            verdict=CONDITIONAL_FORMAL_THEOREM_TARGET_READY,
            theorem_target_ready=True,
            terminal_overclaim=False,
            supports_track_1=False,
            counterexample_obligations=(),
            reason=(
                "This conditional theorem is ready as Track 2 support: bounded "
                "formal/local OSAG support remains conditional and nonphysical."
            ),
        )
    if (
        floor
        and target.uses_h1_completion_floor
        and target.uses_h6_boundary
        and target.uses_h8_signature_bundle
        and target.has_counterexample_contract
    ):
        return TargetDecision(
            target_id=target.target_id,
            verdict=BOUNDED_THEOREM_TARGET_READY,
            theorem_target_ready=True,
            terminal_overclaim=False,
            supports_track_1=True,
            counterexample_obligations=COUNTEREXAMPLE_OBLIGATIONS,
            reason=(
                "The target is bounded, killable, and supported by H1/H6/H8. "
                "It states the no-escape result for the current Adapter_P "
                "trace class without pretending to be a universal theorem."
            ),
        )
    return TargetDecision(
        target_id=target.target_id,
        verdict=THEOREM_TARGET_UNSUPPORTED,
        theorem_target_ready=False,
        terminal_overclaim=False,
        supports_track_1=False,
        counterexample_obligations=(),
        reason="The target does not preserve the fixed post-H8 floor.",
    )


def run_theorem_target() -> dict[str, Any]:
    summary = fixed_input_summary()
    targets = theorem_targets()
    decisions = [classify_target(target, summary) for target in targets]
    by_id = {decision.target_id: decision for decision in decisions}
    bounded = by_id["bounded_adapter_p_completion_barrier"]
    counterexample = by_id["new_packet_counterexample_contract"]
    ready_target_ids = [
        decision.target_id
        for decision in decisions
        if decision.theorem_target_ready
    ]
    terminal_overclaim_ids = [
        decision.target_id for decision in decisions if decision.terminal_overclaim
    ]

    return {
        "fixture_id": "t1_completion_barrier_theorem_target",
        "kind": "post_h8_completion_barrier_theorem_contract",
        "fixed_inputs": summary,
        "fixed_floor_satisfied": fixed_floor_satisfied(summary),
        "theorem_contract_ready": (
            bounded.verdict == BOUNDED_THEOREM_TARGET_READY
        ),
        "bounded_theorem_target_id": bounded.target_id,
        "ready_target_ids": ready_target_ids,
        "terminal_overclaim_ids": terminal_overclaim_ids,
        "counterexample_contract_ready": (
            counterexample.verdict == COUNTEREXAMPLE_CONTRACT_READY
        ),
        "counterexample_obligations": list(COUNTEREXAMPLE_OBLIGATIONS),
        "t1_result": (
            "bounded_completion_barrier_theorem_target_sharpened_not_"
            "universal_theorem"
        ),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "next_track_1_recommendation": (
            "Mechanize or formally package the bounded completion-barrier "
            "theorem target unless a new concrete H7-admitted packet appears. "
            "If such a packet appears, route it through the counterexample "
            "obligations first."
        ),
        "honest_current_result": (
            "The current post-H8 record supports a bounded theorem target over "
            "the repo's Adapter_P trace class. It does not support a universal "
            "physics no-go, a D-FORK decision, physical source issuance, claim "
            "movement, or TI-C020 reopening."
        ),
        "targets": [
            {
                "target_id": target.target_id,
                "title": target.title,
                "scope": target.scope,
                "conclusion": target.conclusion,
            }
            for target in targets
        ],
        "decisions": [decision.as_dict() for decision in decisions],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "tests/artifacts/t1_completion_barrier_theorem_target_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_theorem_target()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
