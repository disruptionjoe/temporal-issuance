#!/usr/bin/env python3
"""T3 validator for the T2 bounded completion-barrier counterexample gate.

This Wave 9 fixture tests the E173/T2 contract gate with adversarial packet
rows. It validates the gate logic, but it does not supply real evidence for
source issuance, move claims, decide D-FORK, or reopen TI-C020.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import t2_bounded_completion_barrier_theorem_contract as t2


CONTRACT_REVISION_TRIGGERED = "CONTRACT_REVISION_TRIGGERED"
BOUNDED_CONDITIONAL_NOT_COUNTEREXAMPLE = (
    "BOUNDED_CONDITIONAL_NOT_COUNTEREXAMPLE"
)
PHYSICAL_NEAR_MISS_NOT_COUNTEREXAMPLE = "PHYSICAL_NEAR_MISS_NOT_COUNTEREXAMPLE"
IMPORTED_STRUCTURE_REJECTED = "IMPORTED_STRUCTURE_REJECTED"
READOUT_FINALITY_REJECTED = "READOUT_FINALITY_REJECTED"
D_FORK_DECISION_SHORTCUT_REJECTED = "D_FORK_DECISION_SHORTCUT_REJECTED"
COUNTEREXAMPLE_OBLIGATIONS_INCOMPLETE = (
    "COUNTEREXAMPLE_OBLIGATIONS_INCOMPLETE"
)


@dataclass(frozen=True)
class PacketRow:
    packet_id: str
    description: str
    control_only: bool
    new_concrete_packet: bool
    h7_admitted: bool
    maps_all_adapter_p_fields: bool
    preserves_tau_n: bool
    preserves_preserve_n: bool
    preserves_represented_family_index: bool
    preserves_candidate_provenance: bool
    no_hidden_completion_oracle: bool
    no_imported_law_or_schema: bool
    not_readout_or_finality_only: bool
    defeats_value_completion: bool
    defeats_name_completion: bool
    defeats_provenance_action_completion: bool
    defeats_capability_completion: bool
    supplies_w1_non_isomorphic_physical_algebra: bool
    supplies_w4_perturbation_non_factorization: bool
    supplies_w5_record_preservation_comparison: bool
    defeats_whole_family_completion: bool
    does_not_treat_h8_as_d_fork_decision: bool
    bounded_formal_local_only: bool = False
    physical_near_miss: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    verdict: str
    revision_trigger: bool
    terminal: bool
    missing_obligations: tuple[str, ...]
    control_only: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "packet_id": self.packet_id,
            "verdict": self.verdict,
            "revision_trigger": self.revision_trigger,
            "terminal": self.terminal,
            "missing_obligations": list(self.missing_obligations),
            "control_only": self.control_only,
            "reason": self.reason,
        }


def _obligation_fields() -> tuple[str, ...]:
    contract = t2.run_theorem_contract()
    return tuple(contract["counterexample_obligations"])


def _field_value(packet: PacketRow, obligation: str) -> bool:
    return bool(getattr(packet, obligation))


def missing_obligations(packet: PacketRow) -> tuple[str, ...]:
    return tuple(
        obligation
        for obligation in _obligation_fields()
        if not _field_value(packet, obligation)
    )


def packet_rows() -> tuple[PacketRow, ...]:
    all_true = {
        obligation: True for obligation in _obligation_fields()
    }
    base_false = {
        obligation: False for obligation in _obligation_fields()
    }
    h7_formal = {
        **base_false,
        "new_concrete_packet": False,
        "h7_admitted": True,
        "maps_all_adapter_p_fields": True,
        "preserves_tau_n": True,
        "preserves_preserve_n": True,
        "preserves_represented_family_index": True,
        "preserves_candidate_provenance": True,
        "no_hidden_completion_oracle": True,
        "no_imported_law_or_schema": True,
        "not_readout_or_finality_only": True,
        "defeats_value_completion": True,
        "defeats_name_completion": True,
        "defeats_provenance_action_completion": True,
        "defeats_capability_completion": True,
        "does_not_treat_h8_as_d_fork_decision": True,
    }
    physical_near_miss = {
        **h7_formal,
        "new_concrete_packet": True,
        "h7_admitted": False,
        "supplies_w1_non_isomorphic_physical_algebra": False,
        "supplies_w4_perturbation_non_factorization": False,
        "supplies_w5_record_preservation_comparison": False,
        "defeats_whole_family_completion": False,
    }
    return (
        PacketRow(
            packet_id="bounded_formal_local_osag_support",
            description=(
                "The known H6 bounded formal/local OSAG support row. It is "
                "internal to the bounded construction but not physical."
            ),
            control_only=False,
            bounded_formal_local_only=True,
            **h7_formal,
        ),
        PacketRow(
            packet_id="crispr_like_fixed_sequence_near_miss",
            description=(
                "A physical-looking near miss absorbed by fixed sequence space "
                "and missing H7 plus W1/W4/W5."
            ),
            control_only=False,
            physical_near_miss=True,
            **physical_near_miss,
        ),
        PacketRow(
            packet_id="imported_completion_oracle_packet",
            description="A packet with a hidden global completion oracle.",
            control_only=False,
            **{
                **all_true,
                "no_hidden_completion_oracle": False,
            },
        ),
        PacketRow(
            packet_id="readout_finality_packet",
            description="A packet whose surplus is readout or finality only.",
            control_only=False,
            **{
                **all_true,
                "not_readout_or_finality_only": False,
            },
        ),
        PacketRow(
            packet_id="h8_decision_shortcut_packet",
            description="A packet that treats H8 as a D-FORK decision.",
            control_only=False,
            **{
                **all_true,
                "does_not_treat_h8_as_d_fork_decision": False,
            },
        ),
        PacketRow(
            packet_id="partial_physical_packet_missing_w4",
            description=(
                "A mostly physical packet that still lacks W4 perturbation "
                "non-factorization."
            ),
            control_only=False,
            **{
                **all_true,
                "supplies_w4_perturbation_non_factorization": False,
            },
        ),
        PacketRow(
            packet_id="synthetic_full_counterexample_control",
            description=(
                "A synthetic control row satisfying every counterexample "
                "obligation. It validates that the gate is killable, but is "
                "not repo evidence that such a packet exists."
            ),
            control_only=True,
            **all_true,
        ),
    )


def classify_packet(packet: PacketRow) -> PacketDecision:
    missing = missing_obligations(packet)
    if not missing:
        return PacketDecision(
            packet_id=packet.packet_id,
            verdict=CONTRACT_REVISION_TRIGGERED,
            revision_trigger=True,
            terminal=False,
            missing_obligations=missing,
            control_only=packet.control_only,
            reason=(
                "The packet satisfies every T2 counterexample obligation. "
                "Because this row is a control, it validates gate falsifiability "
                "without supplying real source evidence."
            ),
        )
    if packet.bounded_formal_local_only:
        verdict = BOUNDED_CONDITIONAL_NOT_COUNTEREXAMPLE
        reason = (
            "Bounded formal/local support remains conditional and nonphysical; "
            "it lacks the physical W1/W4/W5 and whole-family defeat obligations."
        )
        terminal = False
    elif packet.physical_near_miss:
        verdict = PHYSICAL_NEAR_MISS_NOT_COUNTEREXAMPLE
        reason = (
            "The physical-looking row is not H7-admitted and lacks W1/W4/W5 "
            "plus whole-family completion defeat."
        )
        terminal = True
    elif "no_hidden_completion_oracle" in missing or "no_imported_law_or_schema" in missing:
        verdict = IMPORTED_STRUCTURE_REJECTED
        reason = "The packet imports completion structure."
        terminal = True
    elif "not_readout_or_finality_only" in missing:
        verdict = READOUT_FINALITY_REJECTED
        reason = "The packet is readout or finality only."
        terminal = True
    elif "does_not_treat_h8_as_d_fork_decision" in missing:
        verdict = D_FORK_DECISION_SHORTCUT_REJECTED
        reason = "The packet attempts to upgrade H8 into a D-FORK decision."
        terminal = True
    else:
        verdict = COUNTEREXAMPLE_OBLIGATIONS_INCOMPLETE
        reason = "The packet leaves at least one T2 counterexample obligation unmet."
        terminal = False

    return PacketDecision(
        packet_id=packet.packet_id,
        verdict=verdict,
        revision_trigger=False,
        terminal=terminal,
        missing_obligations=missing,
        control_only=packet.control_only,
        reason=reason,
    )


def run_gate_validator() -> dict[str, Any]:
    contract = t2.run_theorem_contract()
    rows = packet_rows()
    decisions = [classify_packet(row) for row in rows]
    revision_triggers = [decision for decision in decisions if decision.revision_trigger]
    real_revision_triggers = [
        decision for decision in revision_triggers if not decision.control_only
    ]
    terminal_control_ids = [
        decision.packet_id for decision in decisions if decision.terminal
    ]

    return {
        "fixture_id": "t3_t2_counterexample_gate_validator",
        "kind": "t2_contract_counterexample_gate_validator",
        "depends_on_fixture_id": contract["fixture_id"],
        "theorem_contract_id": contract["theorem_contract_id"],
        "contract_ready": contract["contract_ready"],
        "counterexample_obligations": contract["counterexample_obligations"],
        "counterexample_gate_validated": (
            contract["counterexample_gate_active"]
            and len(revision_triggers) == 1
            and revision_triggers[0].packet_id
            == "synthetic_full_counterexample_control"
            and not real_revision_triggers
        ),
        "synthetic_revision_control_id": (
            revision_triggers[0].packet_id if revision_triggers else None
        ),
        "real_counterexample_packet_found": bool(real_revision_triggers),
        "terminal_control_ids": terminal_control_ids,
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "t3_result": (
            "t2_counterexample_gate_validated_no_real_packet_found"
        ),
        "next_track_1_recommendation": (
            "Do not repeat T3. Resume material work only with a real concrete "
            "H7-admitted packet or a distinct deliberate gate that tests the "
            "T2 contract without broadening it."
        ),
        "honest_current_result": (
            "T3 validates that the T2 counterexample gate is falsifiable and "
            "rejects current near-miss classes. The only revision trigger is a "
            "synthetic control row, so no source claim moves."
        ),
        "packets": [
            {
                "packet_id": row.packet_id,
                "description": row.description,
                "control_only": row.control_only,
            }
            for row in rows
        ],
        "decisions": [decision.as_dict() for decision in decisions],
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
            "tests/artifacts/t3_t2_counterexample_gate_validator_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_gate_validator()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
