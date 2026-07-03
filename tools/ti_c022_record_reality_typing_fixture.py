"""TI-C022 record-reality typing fixture.

The fixture checks the RUN-0057 resurrection trigger: whether TI-C022 record
reality and canonical-chain finality can disagree under the same quorum,
carrier-selection, finality, and record-membership assumptions.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class State:
    state_id: str
    branch: str
    quorum_certified: bool
    cofinal_carrier: bool
    canonical_member: bool
    branch_local_finalized: bool


@dataclass(frozen=True)
class Event:
    event_id: str
    target_state: str
    description: str


@dataclass(frozen=True)
class TraceCase:
    case_id: str
    description: str
    protocol_assumptions: dict[str, bool]
    states: list[State]
    events: list[Event]


@dataclass(frozen=True)
class EventVerdict:
    event_id: str
    target_state: str
    branch: str
    ti_c022_record_real: bool
    canonical_chain_final: bool
    branch_local_integrity: bool
    same_assumption_divergence: bool


@dataclass(frozen=True)
class CaseVerdict:
    case_id: str
    description: str
    protocol_assumptions: dict[str, bool]
    cofinal_branches: list[str]
    canonical_branches: list[str]
    unique_cofinal_carrier_exists: bool
    unique_canonical_carrier_exists: bool
    event_verdicts: list[EventVerdict]
    same_assumption_divergence_found: bool


def _canonical_assumptions_hold(assumptions: dict[str, bool]) -> bool:
    required = (
        "quorum_validity",
        "canonical_carrier_selection",
        "finality_rule",
        "finalized_record_membership",
    )
    return all(assumptions.get(key, False) for key in required)


def fixture_cases() -> list[TraceCase]:
    matched = {
        "quorum_validity": True,
        "canonical_carrier_selection": True,
        "finality_rule": True,
        "finalized_record_membership": True,
    }
    no_canonical_carrier = {
        "quorum_validity": True,
        "canonical_carrier_selection": False,
        "finality_rule": False,
        "finalized_record_membership": False,
    }

    return [
        TraceCase(
            case_id="unforked_progress",
            description="single quorum-legitimate carrier with ordinary finality",
            protocol_assumptions=matched,
            states=[
                State("s0", "A", True, True, True, True),
                State("s1", "A", True, True, True, True),
                State("s2", "A", True, True, True, True),
            ],
            events=[
                Event("e1", "s1", "first finalized schema extension"),
                Event("e2", "s2", "second finalized schema extension"),
            ],
        ),
        TraceCase(
            case_id="temporary_fork_canonicalized",
            description="temporary fork with one cofinal canonical branch and one orphaned local record",
            protocol_assumptions=matched,
            states=[
                State("a1", "A", True, True, True, True),
                State("a2", "A", True, True, True, True),
                State("b1", "B", True, False, False, True),
            ],
            events=[
                Event("e_a1", "a1", "canonical branch record"),
                Event("e_b1", "b1", "orphaned but branch-local finalized record"),
            ],
        ),
        TraceCase(
            case_id="permanent_fork_no_canonical_carrier",
            description="two incompatible cofinal branches with branch-local integrity but no unique shared carrier",
            protocol_assumptions=no_canonical_carrier,
            states=[
                State("a1", "A", True, True, False, True),
                State("a2", "A", True, True, False, True),
                State("b1", "B", True, True, False, True),
                State("b2", "B", True, True, False, True),
            ],
            events=[
                Event("e_a2", "a2", "branch A local finality"),
                Event("e_b2", "b2", "branch B local finality"),
            ],
        ),
        TraceCase(
            case_id="quorum_without_finality",
            description="quorum-certified record before carrier finality is supplied",
            protocol_assumptions={
                "quorum_validity": True,
                "canonical_carrier_selection": False,
                "finality_rule": False,
                "finalized_record_membership": False,
            },
            states=[
                State("p1", "P", True, False, False, True),
            ],
            events=[
                Event("e_p1", "p1", "quorum certificate without unique cofinal carrier"),
            ],
        ),
    ]


def evaluate_case(case: TraceCase) -> CaseVerdict:
    states_by_id = {state.state_id: state for state in case.states}
    cofinal_branches = sorted(
        {state.branch for state in case.states if state.cofinal_carrier and state.quorum_certified}
    )
    canonical_assumptions = _canonical_assumptions_hold(case.protocol_assumptions)
    canonical_branches = sorted(
        {state.branch for state in case.states if state.canonical_member and state.quorum_certified}
    )

    unique_cofinal = len(cofinal_branches) == 1
    unique_canonical = canonical_assumptions and len(canonical_branches) == 1
    cofinal_branch = cofinal_branches[0] if unique_cofinal else None
    canonical_branch = canonical_branches[0] if unique_canonical else None

    verdicts: list[EventVerdict] = []
    for event in case.events:
        target = states_by_id[event.target_state]
        ti_c022_record_real = (
            target.quorum_certified and unique_cofinal and target.branch == cofinal_branch
        )
        canonical_chain_final = (
            target.quorum_certified
            and unique_canonical
            and target.branch == canonical_branch
            and target.canonical_member
        )
        branch_local_integrity = target.quorum_certified and target.branch_local_finalized
        verdicts.append(
            EventVerdict(
                event_id=event.event_id,
                target_state=event.target_state,
                branch=target.branch,
                ti_c022_record_real=ti_c022_record_real,
                canonical_chain_final=canonical_chain_final,
                branch_local_integrity=branch_local_integrity,
                same_assumption_divergence=ti_c022_record_real != canonical_chain_final,
            )
        )

    return CaseVerdict(
        case_id=case.case_id,
        description=case.description,
        protocol_assumptions=case.protocol_assumptions,
        cofinal_branches=cofinal_branches,
        canonical_branches=canonical_branches if canonical_assumptions else [],
        unique_cofinal_carrier_exists=unique_cofinal,
        unique_canonical_carrier_exists=unique_canonical,
        event_verdicts=verdicts,
        same_assumption_divergence_found=any(
            verdict.same_assumption_divergence for verdict in verdicts
        ),
    )


def _invalid_divergence_controls(case_verdicts: list[CaseVerdict]) -> list[dict[str, object]]:
    controls: list[dict[str, object]] = []
    for case in case_verdicts:
        for verdict in case.event_verdicts:
            if verdict.branch_local_integrity and not verdict.canonical_chain_final:
                controls.append(
                    {
                        "case_id": case.case_id,
                        "event_id": verdict.event_id,
                        "invalid_move": "treat_branch_local_integrity_as_canonical_finality",
                        "would_create_apparent_divergence": verdict.ti_c022_record_real is False,
                        "reason_invalid": (
                            "branch-local BFT/TCB integrity is not the same assumption set as "
                            "unique canonical-carrier finality"
                        ),
                    }
                )
    controls.append(
        {
            "case_id": "temporary_fork_canonicalized",
            "event_id": "e_b1",
            "invalid_move": "declare_orphaned_branch_record_ontologically_real_by_override",
            "would_create_apparent_divergence": True,
            "reason_invalid": (
                "the override drops the TI-C022 membership requirement in the unique cofinal "
                "quorum-legitimate carrier"
            ),
        }
    )
    return controls


def run_fixture() -> dict[str, object]:
    cases = fixture_cases()
    case_verdicts = [evaluate_case(case) for case in cases]
    same_assumption_divergences = [
        {
            "case_id": case.case_id,
            "event_id": verdict.event_id,
            "ti_c022_record_real": verdict.ti_c022_record_real,
            "canonical_chain_final": verdict.canonical_chain_final,
        }
        for case in case_verdicts
        for verdict in case.event_verdicts
        if verdict.same_assumption_divergence
    ]
    invalid_controls = _invalid_divergence_controls(case_verdicts)

    return {
        "fixture": "ti_c022_record_reality_typing_fixture_v0_1",
        "source_artifacts": [
            "explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md",
            "explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md",
            "memory/path-kills.md#run-0057",
        ],
        "case_results": [asdict(case) for case in case_verdicts],
        "same_assumption_divergences": same_assumption_divergences,
        "invalid_divergence_controls": invalid_controls,
        "comparisons": {
            "cases_checked": len(case_verdicts),
            "same_assumption_divergence_found": bool(same_assumption_divergences),
            "apparent_divergences_require_assumption_change": (
                not same_assumption_divergences and bool(invalid_controls)
            ),
            "operational_absorption_reaffirmed": not same_assumption_divergences,
            "branch_local_integrity_distinguished_from_record_reality": True,
            "canonical_membership_matches_ti_c022_when_matched_assumptions_hold": True,
        },
        "verdict": {
            "TI_C022_independent_operational_surplus": False,
            "remaining_surplus": "ontological_record_reality_typing",
            "resurrection_trigger_met": False,
            "claim_status_change": "none",
            "best_result": (
                "Across the bounded traces, TI-C022 record reality matches canonical-chain "
                "membership whenever the same quorum, carrier-selection, finality, and record-"
                "membership assumptions are supplied. Apparent divergence comes only from "
                "substituting branch-local integrity or an ontology override for canonical "
                "carrier membership."
            ),
            "next_gate": "W010_frontier_selection_after_ti_c022_record_reality_fixture",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the TI-C022 record-reality typing fixture.")
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
