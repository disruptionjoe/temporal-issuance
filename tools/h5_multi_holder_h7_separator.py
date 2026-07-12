#!/usr/bin/env python3
"""H5 multi-holder separator through the H7 admission gate.

This post-H7 fixture tests whether multi-holder reversal cost is source
crossing or only fixed-source holder/access/readout completion. It consumes the
H7 admission contract and preserves no-claim-movement posture.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import completion_aware_adapter_p_admission_contract as h7


CAPABILITY_COMPLETION_ABSORPTION = "CAPABILITY_COMPLETION_ABSORPTION"
TAF_EXPRESSIBLE_READOUT = "TAF_EXPRESSIBLE_READOUT"
H7_ADMITTED_FORMAL_LOCAL_SUPPORT = "H7_ADMITTED_FORMAL_LOCAL_SUPPORT"
H7_GATE_REJECTION = "H7_GATE_REJECTION"


@dataclass(frozen=True)
class HolderCase:
    case_id: str
    description: str
    copy_holders: tuple[str, ...]
    values: tuple[int, ...]
    quorum: int
    overwrite_count: int
    holder_maps_predeclared: bool
    operations_predeclared_in_s_inf: bool
    fixed_source_access_model: bool
    h7_packet_id: str
    changed_holder_permissions: bool
    source_growth_core_witness: bool
    preaction_family_noncompletion_rule: bool
    claims_physical_source: bool


@dataclass(frozen=True)
class HolderCaseResult:
    case_id: str
    verdict: str
    terminal: bool
    h7_packet_id: str
    h7_admitted: bool
    measures: dict[str, Any]
    source_growth_core_witness: bool
    preaction_family_noncompletion_rule: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "verdict": self.verdict,
            "terminal": self.terminal,
            "h7_packet_id": self.h7_packet_id,
            "h7_admitted": self.h7_admitted,
            "measures": self.measures,
            "source_growth_core_witness": self.source_growth_core_witness,
            "preaction_family_noncompletion_rule": (
                self.preaction_family_noncompletion_rule
            ),
            "reason": self.reason,
        }


def holder_cases() -> tuple[HolderCase, ...]:
    return (
        HolderCase(
            case_id="single_holder_bundle",
            description="Three physical copies are controlled by one holder.",
            copy_holders=("A", "A", "A"),
            values=(0, 1),
            quorum=2,
            overwrite_count=3,
            holder_maps_predeclared=True,
            operations_predeclared_in_s_inf=True,
            fixed_source_access_model=True,
            h7_packet_id="boundary_osag_support",
            changed_holder_permissions=False,
            source_growth_core_witness=False,
            preaction_family_noncompletion_rule=False,
            claims_physical_source=False,
        ),
        HolderCase(
            case_id="multi_holder_split_fixed_source",
            description=(
                "Three physical copies are split across A, B, and C with quorum "
                "and holder maps already predeclared."
            ),
            copy_holders=("A", "B", "C"),
            values=(0, 1),
            quorum=2,
            overwrite_count=3,
            holder_maps_predeclared=True,
            operations_predeclared_in_s_inf=True,
            fixed_source_access_model=True,
            h7_packet_id="boundary_osag_support",
            changed_holder_permissions=True,
            source_growth_core_witness=False,
            preaction_family_noncompletion_rule=False,
            claims_physical_source=False,
        ),
        HolderCase(
            case_id="h7_boundary_osag_holder_support",
            description=(
                "The split-holder packet carries formal/local OSAG support and "
                "the H7-preserved completion-channel fields."
            ),
            copy_holders=("A", "B", "C"),
            values=(0, 1),
            quorum=2,
            overwrite_count=3,
            holder_maps_predeclared=True,
            operations_predeclared_in_s_inf=True,
            fixed_source_access_model=True,
            h7_packet_id="boundary_osag_support",
            changed_holder_permissions=True,
            source_growth_core_witness=True,
            preaction_family_noncompletion_rule=True,
            claims_physical_source=False,
        ),
        HolderCase(
            case_id="cross_repo_readout_holder_claim",
            description=(
                "A cross-repo holder/finality phrasing tries to count readout "
                "language as source crossing."
            ),
            copy_holders=("A", "B", "C"),
            values=(0, 1),
            quorum=2,
            overwrite_count=3,
            holder_maps_predeclared=True,
            operations_predeclared_in_s_inf=True,
            fixed_source_access_model=True,
            h7_packet_id="cross_repo_readout_language",
            changed_holder_permissions=True,
            source_growth_core_witness=False,
            preaction_family_noncompletion_rule=False,
            claims_physical_source=False,
        ),
    )


def holder_measures(case: HolderCase) -> dict[str, Any]:
    counts = Counter(case.copy_holders)
    max_single_holder_copies = max(counts.values())
    distinct_holder_count = len(counts)
    single_holder_controls_quorum = max_single_holder_copies >= case.quorum
    holder_boundary_gap = max(0, case.quorum - max_single_holder_copies)
    return {
        "holders": sorted(counts),
        "values": list(case.values),
        "quorum": case.quorum,
        "physical_copy_count": len(case.copy_holders),
        "overwrite_count": case.overwrite_count,
        "distinct_holder_count": distinct_holder_count,
        "CanReverse": single_holder_controls_quorum,
        "CanFork": single_holder_controls_quorum,
        "CanPostdict": case.operations_predeclared_in_s_inf,
        "mu_INFO": len(case.values),
        "mu_COMP": case.overwrite_count,
        "mu_HOLDER": holder_boundary_gap,
        "holder_maps_predeclared": case.holder_maps_predeclared,
        "operations_predeclared_in_s_inf": case.operations_predeclared_in_s_inf,
        "fixed_source_access_model": case.fixed_source_access_model,
    }


def classify_case(
    case: HolderCase,
    decisions: dict[str, dict[str, Any]],
) -> HolderCaseResult:
    decision = decisions[case.h7_packet_id]
    measures = holder_measures(case)

    if not decision["admitted"]:
        verdict = H7_GATE_REJECTION
        terminal = True
        reason = (
            "H7 rejects the packet before H5 can count it as holder evidence."
        )
    elif case.claims_physical_source:
        verdict = H7_GATE_REJECTION
        terminal = True
        reason = "H5 cannot assert physical source issuance or move posture."
    elif (
        case.source_growth_core_witness
        and case.preaction_family_noncompletion_rule
    ):
        verdict = H7_ADMITTED_FORMAL_LOCAL_SUPPORT
        terminal = False
        reason = (
            "The packet is admitted only as formal/local OSAG support; it does "
            "not make holder cost a physical source-crossing claim."
        )
    elif (
        case.changed_holder_permissions
        and case.holder_maps_predeclared
        and case.operations_predeclared_in_s_inf
        and case.fixed_source_access_model
    ):
        verdict = TAF_EXPRESSIBLE_READOUT
        terminal = True
        reason = (
            "The higher reversal/fork cost is holder-boundary finality or "
            "readout over a fixed source with predeclared access operations."
        )
    else:
        verdict = CAPABILITY_COMPLETION_ABSORPTION
        terminal = True
        reason = (
            "The case is controlled by a fixed capability/access schedule and "
            "does not supply multi-holder source crossing."
        )

    return HolderCaseResult(
        case_id=case.case_id,
        verdict=verdict,
        terminal=terminal,
        h7_packet_id=case.h7_packet_id,
        h7_admitted=bool(decision["admitted"]),
        measures=measures,
        source_growth_core_witness=case.source_growth_core_witness,
        preaction_family_noncompletion_rule=(
            case.preaction_family_noncompletion_rule
        ),
        reason=reason,
    )


def run_separator() -> dict[str, Any]:
    h7_result = h7.run_admission_contract()
    decisions = {decision["packet_id"]: decision for decision in h7_result["decisions"]}
    results = [classify_case(case, decisions) for case in holder_cases()]
    by_id = {result.case_id: result for result in results}
    first_two = [
        by_id["single_holder_bundle"].measures,
        by_id["multi_holder_split_fixed_source"].measures,
    ]
    controls_matched = (
        first_two[0]["physical_copy_count"] == first_two[1]["physical_copy_count"]
        and first_two[0]["overwrite_count"] == first_two[1]["overwrite_count"]
        and first_two[0]["mu_INFO"] == first_two[1]["mu_INFO"]
        and first_two[0]["mu_COMP"] == first_two[1]["mu_COMP"]
    )

    return {
        "fixture_id": "h5_multi_holder_h7_separator",
        "kind": "h5_multi_holder_separator_through_h7",
        "h7_floor_satisfied": bool(h7_result["h1_h2_floor_satisfied"]),
        "h7_admitted_packet_ids": h7_result["admitted_packet_ids"],
        "matched_physical_and_thermodynamic_controls": controls_matched,
        "results": [result.as_dict() for result in results],
        "h5_result": "multi_holder_cost_separated_from_source_crossing",
        "multi_holder_cost_absorbed_as_taf_readout": (
            by_id["multi_holder_split_fixed_source"].verdict
            == TAF_EXPRESSIBLE_READOUT
        ),
        "formal_local_osag_support_admitted": (
            by_id["h7_boundary_osag_holder_support"].verdict
            == H7_ADMITTED_FORMAL_LOCAL_SUPPORT
        ),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "next_track_1_recommendation": (
            "Run H9 physical calibration or H6 completion-boundary work only "
            "with concrete packets that satisfy H7; H5 alone supplies no "
            "source-crossing claim."
        ),
        "honest_current_result": (
            "H5 separates multi-holder reversal cost from source crossing. "
            "With matched physical copies and overwrites, split-holder cost is "
            "TaF/readout over fixed-source holder maps unless an H7-admitted "
            "formal/local OSAG packet is supplied, and that packet still moves "
            "no claims."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_json(run_separator(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
