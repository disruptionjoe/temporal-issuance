"""Clock-free record-cadence fixture for E096.

The fixture replays one frozen multi-observer trace under three systems:
A. independent local records plus later reconciliation
B. hidden global tick / preferred foliation
C. clock-free shared admissibility over local projections
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


BITS = ("x_AB", "x_BC", "x_CA")


@dataclass(frozen=True)
class Proposal:
    proposal_id: str
    observer: str
    handle: str
    bit: str
    value: int


@dataclass(frozen=True)
class SystemResult:
    system_id: str
    description: str
    global_ticks_used: int
    hidden_total_order_used: bool
    admitted_records: list[str]
    rejected_records: list[str]
    deferred_records: list[str]
    revised_final_records: list[str]
    orphaned_local_records: list[str]
    parity_obstructions: int
    global_completion_checks: int
    max_unsettled_handle_width: int
    coherence_without_revision: bool
    effect_verdict: dict[str, bool]
    absorber_verdict: str


def frozen_trace() -> list[Proposal]:
    return [
        Proposal("p1", "O_A", "h0", "x_AB", 1),
        Proposal("p2", "O_C", "h0", "x_CA", 0),
        Proposal("p3", "O_B", "h0", "x_BC", 0),
        Proposal("p4", "O_B", "h0", "x_BC", 1),
        Proposal("p5", "O_C", "h1", "x_CA", 1),
        Proposal("p6", "O_A", "h1", "x_AB", 0),
        Proposal("p7", "O_B", "h1", "x_BC", 1),
    ]


def parity_ok(assignments: dict[str, int]) -> bool:
    if any(bit not in assignments for bit in BITS):
        return True
    return (assignments["x_AB"] ^ assignments["x_BC"] ^ assignments["x_CA"]) == 0


def has_completion(assignments: dict[str, int]) -> bool:
    if not assignments:
        return True
    missing = [bit for bit in BITS if bit not in assignments]
    if not missing:
        return parity_ok(assignments)
    if len(missing) == 1:
        known_xor = 0
        for bit in BITS:
            if bit in assignments:
                known_xor ^= assignments[bit]
        return known_xor in (0, 1)
    return True


def max_unsettled_width(admitted: list[Proposal]) -> int:
    seen: dict[str, set[str]] = {}
    max_width = 0
    for proposal in admitted:
        seen.setdefault(proposal.handle, set()).add(proposal.bit)
        unsettled = sum(1 for bits in seen.values() if len(bits) < 3)
        max_width = max(max_width, unsettled)
    return max_width


def run_independent_reconciliation(trace: list[Proposal]) -> SystemResult:
    by_handle: dict[str, dict[str, list[Proposal]]] = {}
    for proposal in trace:
        by_handle.setdefault(proposal.handle, {}).setdefault(proposal.bit, []).append(proposal)

    revised: list[str] = []
    orphaned: list[str] = []
    obstructions = 0
    for handle, bits in by_handle.items():
        first_values = {bit: proposals[0].value for bit, proposals in bits.items()}
        if not parity_ok(first_values):
            obstructions += 1
            for bit, proposals in bits.items():
                if len(proposals) > 1:
                    revised.append(proposals[0].proposal_id)
                    orphaned.append(proposals[0].proposal_id)
                    break
        for proposals in bits.values():
            if len(proposals) > 1:
                orphaned.extend(proposal.proposal_id for proposal in proposals[:-1] if proposal.proposal_id not in orphaned)

    return SystemResult(
        system_id="A",
        description="independent local records plus later reconciliation",
        global_ticks_used=0,
        hidden_total_order_used=False,
        admitted_records=[proposal.proposal_id for proposal in trace],
        rejected_records=[],
        deferred_records=[],
        revised_final_records=revised,
        orphaned_local_records=orphaned,
        parity_obstructions=obstructions,
        global_completion_checks=len(by_handle),
        max_unsettled_handle_width=max_unsettled_width(trace),
        coherence_without_revision=not revised and obstructions == 0,
        effect_verdict={"Issue[S]": False, "Project[O]": True, "Finalize[R]": True, "Lose[K]": True},
        absorber_verdict="after_the_fact_reconciliation_control",
    )


def run_hidden_tick(trace: list[Proposal]) -> SystemResult:
    compatible = {
        "h0": {"x_AB": 1, "x_BC": 1, "x_CA": 0},
        "h1": {"x_AB": 0, "x_BC": 1, "x_CA": 1},
    }
    admitted: list[Proposal] = []
    rejected: list[Proposal] = []
    for proposal in trace:
        if compatible[proposal.handle][proposal.bit] == proposal.value:
            admitted.append(proposal)
        else:
            rejected.append(proposal)

    return SystemResult(
        system_id="B",
        description="hidden global tick / preferred foliation",
        global_ticks_used=len(compatible),
        hidden_total_order_used=True,
        admitted_records=[proposal.proposal_id for proposal in admitted],
        rejected_records=[proposal.proposal_id for proposal in rejected],
        deferred_records=[],
        revised_final_records=[],
        orphaned_local_records=[],
        parity_obstructions=len(rejected),
        global_completion_checks=len(trace),
        max_unsettled_handle_width=max_unsettled_width(admitted),
        coherence_without_revision=True,
        effect_verdict={"Issue[S]": False, "Project[O]": True, "Finalize[R]": True, "Lose[K]": False},
        absorber_verdict="hidden_clock_absorber",
    )


def run_clock_free_constraint(trace: list[Proposal]) -> SystemResult:
    partial: dict[str, dict[str, int]] = {}
    admitted: list[Proposal] = []
    rejected: list[Proposal] = []
    checks = 0

    for proposal in trace:
        current = dict(partial.setdefault(proposal.handle, {}))
        if proposal.bit in current and current[proposal.bit] != proposal.value:
            rejected.append(proposal)
            checks += 1
            continue

        current[proposal.bit] = proposal.value
        checks += 1
        if has_completion(current):
            partial[proposal.handle] = current
            admitted.append(proposal)
        else:
            rejected.append(proposal)

    return SystemResult(
        system_id="C",
        description="clock-free shared admissibility constraint",
        global_ticks_used=0,
        hidden_total_order_used=False,
        admitted_records=[proposal.proposal_id for proposal in admitted],
        rejected_records=[proposal.proposal_id for proposal in rejected],
        deferred_records=[],
        revised_final_records=[],
        orphaned_local_records=[],
        parity_obstructions=len(rejected),
        global_completion_checks=checks,
        max_unsettled_handle_width=max_unsettled_width(admitted),
        coherence_without_revision=True,
        effect_verdict={"Issue[S]": False, "Project[O]": True, "Finalize[R]": True, "Lose[K]": True},
        absorber_verdict="clock_free_candidate_absorber_pending",
    )


def run_fixture() -> dict[str, object]:
    trace = frozen_trace()
    systems = [
        run_independent_reconciliation(trace),
        run_hidden_tick(trace),
        run_clock_free_constraint(trace),
    ]
    by_id = {system.system_id: system for system in systems}
    c_beats_a = by_id["C"].coherence_without_revision and not by_id["A"].coherence_without_revision
    c_avoids_b = by_id["C"].global_ticks_used == 0 and not by_id["C"].hidden_total_order_used

    result = {
        "fixture": "clock_free_record_cadence_fixture_v0_1",
        "source_artifact": "explorations/E096-clock-free-record-cadence-fixture-2026-06-30.md",
        "trace": [asdict(proposal) for proposal in trace],
        "systems": {system.system_id: asdict(system) for system in systems},
        "comparisons": {
            "C_beats_A": c_beats_a,
            "C_avoids_B": c_avoids_b,
            "B_reproduces_coherence_with_hidden_tick": by_id["B"].coherence_without_revision,
        },
        "verdict": {
            "comparator_executed": True,
            "positive_scope": "clock_free_coherence_vs_after_the_fact_reconciliation",
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
            "claim_status_change": "none",
            "next_gate": "apply_fixed_site_sheaf_gluing_and_fixed_H_absorbers_before_any_source_claim",
        },
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the E096 clock-free record-cadence fixture.")
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
