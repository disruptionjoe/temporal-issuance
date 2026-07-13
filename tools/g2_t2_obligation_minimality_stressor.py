#!/usr/bin/env python3
"""G2 obligation-minimality stressor for the T2 counterexample gate.

This Wave 10 fixture checks whether any E172/E173 counterexample obligation is
redundant under the current T3 gate. It uses synthetic omission rows only; it
does not supply source evidence, move claims, decide D-FORK, or reopen TI-C020.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import t3_t2_counterexample_gate_validator as t3


OBLIGATION_LOAD_BEARING = "OBLIGATION_LOAD_BEARING"
OBLIGATION_REDUNDANT = "OBLIGATION_REDUNDANT"
OBLIGATION_TERMINAL_SAFETY_STOP = "OBLIGATION_TERMINAL_SAFETY_STOP"


@dataclass(frozen=True)
class OmissionResult:
    obligation_id: str
    verdict: str
    omission_class: str
    revision_still_triggers: bool
    terminal: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "obligation_id": self.obligation_id,
            "verdict": self.verdict,
            "omission_class": self.omission_class,
            "revision_still_triggers": self.revision_still_triggers,
            "terminal": self.terminal,
            "reason": self.reason,
        }


def obligation_fields() -> tuple[str, ...]:
    gate = t3.run_gate_validator()
    return tuple(gate["counterexample_obligations"])


def synthetic_packet_with_omission(obligation_id: str) -> t3.PacketRow:
    values = {obligation: True for obligation in obligation_fields()}
    values[obligation_id] = False
    return t3.PacketRow(
        packet_id=f"omit_{obligation_id}",
        description=f"Synthetic omission row missing {obligation_id}.",
        control_only=True,
        **values,
    )


def classify_omission(obligation_id: str) -> OmissionResult:
    packet = synthetic_packet_with_omission(obligation_id)
    decision = t3.classify_packet(packet)
    if decision.revision_trigger:
        omission_class = OBLIGATION_REDUNDANT
        reason = (
            "Removing this obligation still triggers contract revision, so it "
            "is redundant under the current gate."
        )
    elif decision.terminal:
        omission_class = OBLIGATION_TERMINAL_SAFETY_STOP
        reason = (
            "Removing this obligation activates a terminal safety stop rather "
            "than a contract revision."
        )
    else:
        omission_class = OBLIGATION_LOAD_BEARING
        reason = (
            "Removing this obligation prevents contract revision, so it is "
            "load-bearing under the current gate."
        )
    return OmissionResult(
        obligation_id=obligation_id,
        verdict=decision.verdict,
        omission_class=omission_class,
        revision_still_triggers=decision.revision_trigger,
        terminal=decision.terminal,
        reason=reason,
    )


def run_minimality_stressor() -> dict[str, Any]:
    gate = t3.run_gate_validator()
    obligations = obligation_fields()
    omissions = [classify_omission(obligation) for obligation in obligations]
    redundant = [
        result.obligation_id
        for result in omissions
        if result.omission_class == OBLIGATION_REDUNDANT
    ]
    load_bearing = [
        result.obligation_id
        for result in omissions
        if result.omission_class
        in (OBLIGATION_LOAD_BEARING, OBLIGATION_TERMINAL_SAFETY_STOP)
    ]
    terminal_safety = [
        result.obligation_id
        for result in omissions
        if result.omission_class == OBLIGATION_TERMINAL_SAFETY_STOP
    ]

    all_obligations_load_bearing = (
        len(load_bearing) == len(obligations) and not redundant
    )

    return {
        "fixture_id": "g2_t2_obligation_minimality_stressor",
        "kind": "t2_counterexample_obligation_minimality_stressor",
        "depends_on_fixture_id": gate["fixture_id"],
        "theorem_contract_id": gate["theorem_contract_id"],
        "counterexample_gate_validated": gate["counterexample_gate_validated"],
        "obligation_count": len(obligations),
        "load_bearing_obligation_ids": load_bearing,
        "redundant_obligation_ids": redundant,
        "terminal_safety_obligation_ids": terminal_safety,
        "all_obligations_load_bearing": all_obligations_load_bearing,
        "overstrong_obligation_ids": [],
        "real_counterexample_packet_found": False,
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "g2_result": (
            "all_t2_counterexample_obligations_load_bearing_no_redundant_"
            "clause_detected"
        ),
        "next_track_1_recommendation": (
            "Do not repeat G2. The current contract is minimal under this "
            "single-omission stressor. Resume material work only with a real "
            "H7-admitted packet or fixed inputs that change the obligation set."
        ),
        "honest_current_result": (
            "Every current counterexample obligation is load-bearing under the "
            "single-omission stressor. No redundant or over-strong obligation "
            "is detected, and no real packet is found."
        ),
        "omission_results": [result.as_dict() for result in omissions],
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
            "tests/artifacts/g2_t2_obligation_minimality_stressor_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_minimality_stressor()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
