#!/usr/bin/env python3
"""Scoped Adapter_P no-go preflight classifier.

This is a small operational preflight, not a theorem about all physics. It
checks whether the current Adapter_P convergence pattern can be represented as
terminal classes before a more formal proof target is attempted.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


FIXED_SOURCE_DISCLOSURE = "FIXED_SOURCE_DISCLOSURE"
CLASS_RELATIVE_FORMAL_RESIDUE = "CLASS_RELATIVE_FORMAL_RESIDUE"
IMPORTED_STRUCTURE_REJECTION = "IMPORTED_STRUCTURE_REJECTION"
POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE = (
    "POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE"
)
OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE = "OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE"
NEEDS_CONCRETE_TRACE = "NEEDS_CONCRETE_TRACE"

TERMINAL_CLASSES = {
    FIXED_SOURCE_DISCLOSURE,
    CLASS_RELATIVE_FORMAL_RESIDUE,
    IMPORTED_STRUCTURE_REJECTION,
}


@dataclass(frozen=True)
class AdapterTraceCase:
    candidate_id: str
    description: str
    adapter_fields_total: bool
    tau_preserved: bool
    factors_through_fixed_completion_access: bool
    finite_prefix_non_precontained: bool
    singleton_after_naming_absorbs: bool
    imports_external_structure: bool
    boundary_supplied_without_ti_preservation: bool
    denied_readout_or_finality_only: bool
    internal_anti_after_naming_principle: bool
    source_growth_core_witness: bool


@dataclass(frozen=True)
class Classification:
    candidate_id: str
    terminal_class: str
    terminal: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "terminal_class": self.terminal_class,
            "terminal": self.terminal,
            "reason": self.reason,
        }


def classify_trace(case: AdapterTraceCase) -> Classification:
    if not case.adapter_fields_total or not case.tau_preserved:
        return Classification(
            candidate_id=case.candidate_id,
            terminal_class=OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE,
            terminal=False,
            reason=(
                "The trace does not supply all Adapter_P fields while preserving "
                "the record trace tau_n, so it is outside the no-go class."
            ),
        )

    if case.imports_external_structure or case.boundary_supplied_without_ti_preservation:
        return Classification(
            candidate_id=case.candidate_id,
            terminal_class=IMPORTED_STRUCTURE_REJECTION,
            terminal=True,
            reason=(
                "The candidate wins by importing a global table, external law, "
                "boundary category, or neighbor-repo datum without a TI-side "
                "source-crossing preservation map."
            ),
        )

    if (
        case.factors_through_fixed_completion_access
        or (
            case.denied_readout_or_finality_only
            and not case.source_growth_core_witness
            and not case.finite_prefix_non_precontained
        )
    ):
        return Classification(
            candidate_id=case.candidate_id,
            terminal_class=FIXED_SOURCE_DISCLOSURE,
            terminal=True,
            reason=(
                "The record can be modeled as fixed completed source plus access, "
                "readout, finality, schedule, or withholding. No W1-W3 source "
                "growth witness is doing work."
            ),
        )

    if (
        case.finite_prefix_non_precontained
        and case.singleton_after_naming_absorbs
        and not case.internal_anti_after_naming_principle
    ):
        return Classification(
            candidate_id=case.candidate_id,
            terminal_class=CLASS_RELATIVE_FORMAL_RESIDUE,
            terminal=True,
            reason=(
                "Finite-prefix freshness survives, but the realized whole family "
                "is absorbed by after-the-fact singleton enumeration."
            ),
        )

    if (
        case.finite_prefix_non_precontained
        and case.source_growth_core_witness
        and case.internal_anti_after_naming_principle
        and not case.singleton_after_naming_absorbs
        and not case.factors_through_fixed_completion_access
    ):
        return Classification(
            candidate_id=case.candidate_id,
            terminal_class=POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE,
            terminal=False,
            reason=(
                "This shape is not absorbed by the scoped terminal classes. A "
                "real physical instance would need a dedicated fixture before "
                "any claim or frontier movement."
            ),
        )

    return Classification(
        candidate_id=case.candidate_id,
        terminal_class=NEEDS_CONCRETE_TRACE,
        terminal=False,
        reason=(
            "The trace lacks enough structure to classify. It should not be used "
            "as evidence for or against source issuance yet."
        ),
    )


def preflight_cases() -> list[AdapterTraceCase]:
    return [
        AdapterTraceCase(
            candidate_id="fixed_completion_access_trace",
            description=(
                "A record-preserving trace through a fixed completed source and "
                "stage-indexed access/readout schedule."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=True,
            finite_prefix_non_precontained=False,
            singleton_after_naming_absorbs=True,
            imports_external_structure=False,
            boundary_supplied_without_ti_preservation=False,
            denied_readout_or_finality_only=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        AdapterTraceCase(
            candidate_id="generated_uv_singleton_absorbed",
            description=(
                "A generated-UV style diagonal trace that is fresh at each finite "
                "prefix but absorbed by the completed realized family."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=False,
            finite_prefix_non_precontained=True,
            singleton_after_naming_absorbs=True,
            imports_external_structure=False,
            boundary_supplied_without_ti_preservation=False,
            denied_readout_or_finality_only=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=True,
        ),
        AdapterTraceCase(
            candidate_id="imported_boundary_category",
            description=(
                "A boundary object or law is added by the modeler and then used "
                "as if it were generated by the TI source."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=False,
            finite_prefix_non_precontained=True,
            singleton_after_naming_absorbs=False,
            imports_external_structure=True,
            boundary_supplied_without_ti_preservation=True,
            denied_readout_or_finality_only=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        AdapterTraceCase(
            candidate_id="taf_denied_readout_only",
            description=(
                "Denied undo or withheld readout changes finality vocabulary but "
                "does not add a TI source-growth witness."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=False,
            finite_prefix_non_precontained=False,
            singleton_after_naming_absorbs=True,
            imports_external_structure=False,
            boundary_supplied_without_ti_preservation=False,
            denied_readout_or_finality_only=True,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        AdapterTraceCase(
            candidate_id="gu_boundary_supply_without_ti_map",
            description=(
                "A GU-side missing boundary datum is supplied, but no TI-side "
                "source-crossing preservation map is provided."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=False,
            finite_prefix_non_precontained=False,
            singleton_after_naming_absorbs=True,
            imports_external_structure=False,
            boundary_supplied_without_ti_preservation=True,
            denied_readout_or_finality_only=False,
            internal_anti_after_naming_principle=False,
            source_growth_core_witness=False,
        ),
        AdapterTraceCase(
            candidate_id="anti_after_naming_positive_shape",
            description=(
                "A schematic positive shape with source-growth witness, finite "
                "prefix non-precontainment, and an internal anti-after-naming "
                "principle. No real physical instance is supplied here."
            ),
            adapter_fields_total=True,
            tau_preserved=True,
            factors_through_fixed_completion_access=False,
            finite_prefix_non_precontained=True,
            singleton_after_naming_absorbs=False,
            imports_external_structure=False,
            boundary_supplied_without_ti_preservation=False,
            denied_readout_or_finality_only=False,
            internal_anti_after_naming_principle=True,
            source_growth_core_witness=True,
        ),
    ]


def run_preflight() -> dict[str, Any]:
    classifications = [classify_trace(case) for case in preflight_cases()]
    classes_by_id = {
        classification.candidate_id: classification.terminal_class
        for classification in classifications
    }
    terminal_classes_seen = sorted(
        {
            classification.terminal_class
            for classification in classifications
            if classification.terminal
        }
    )
    nonterminal_cases = [
        classification.candidate_id
        for classification in classifications
        if not classification.terminal
    ]

    result = {
        "fixture_id": "adapter_p_no_go_preflight",
        "kind": "scoped_classifier_not_physics_theorem",
        "claim_status_change": "none",
        "candidate_class": (
            "record-preserving Adapter_P traces with fixed-completion/access, "
            "finite-prefix freshness, singleton after-naming, and imported "
            "structure explicitly represented"
        ),
        "terminal_classes": sorted(TERMINAL_CLASSES),
        "terminal_classes_seen": terminal_classes_seen,
        "all_terminal_classes_exercised": set(terminal_classes_seen) == TERMINAL_CLASSES,
        "boundary_polarity_separated": (
            classes_by_id["taf_denied_readout_only"] == FIXED_SOURCE_DISCLOSURE
            and classes_by_id["gu_boundary_supply_without_ti_map"]
            == IMPORTED_STRUCTURE_REJECTION
            and classes_by_id["anti_after_naming_positive_shape"]
            == POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE
        ),
        "real_counterexample_found": False,
        "theorem_ready": False,
        "selected_proof_target": "small_python_classifier_then_counterexample_fixture",
        "lean_target_ready": False,
        "TI_C020_reopened": False,
        "next_trigger": "compact_no_worthy_work_until_gate_changes",
        "activation_condition": (
            "Resume material work only if a concrete Adapter_P trace fills the "
            "potential-counterexample shape with an internal anti-after-naming "
            "principle, or if a sharper theorem target is supplied."
        ),
        "nonterminal_cases": nonterminal_cases,
        "classifications": [
            classification.as_dict() for classification in classifications
        ],
    }
    return result


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/adapter_p_no_go_preflight_result.json"),
    )
    args = parser.parse_args()
    result = run_preflight()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
