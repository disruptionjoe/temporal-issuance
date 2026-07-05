#!/usr/bin/env python3
"""Executable negative-half fixture for the Cech/H3 functor obligation.

The older Cech fixture proves a narrow positive result: finite SBP parity data
can force a nontrivial flat Z/2 local-system witness. This fixture tests the
larger overclaim: whether that finite filtered witness is enough to discharge a
total GU/H3 bridge or C3 spacelike/correspondence geometry obligation.

It intentionally models the missing bridge data as explicit requirements so a
future run can see exactly what would have to change to resurrect the route.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


TOTAL_FUNCTOR_REQUIREMENTS = (
    "cover_localization_rule",
    "parity_functional",
    "non_parity_extension_rule",
)

FULL_BRIDGE_REQUIREMENTS = TOTAL_FUNCTOR_REQUIREMENTS + (
    "h3_comparison_theorem",
    "c3_geometry_model",
)


@dataclass(frozen=True)
class BridgeAttempt:
    attempt_id: str
    description: str
    cover_localization_rule: bool
    parity_functional: bool
    non_parity_extension_rule: bool
    h3_comparison_theorem: bool
    c3_geometry_model: bool
    hidden_global_table: bool = False
    external_stipulations: tuple[str, ...] = ()


def _as_bool_map(attempt: BridgeAttempt) -> dict[str, bool]:
    return {
        "cover_localization_rule": attempt.cover_localization_rule,
        "parity_functional": attempt.parity_functional,
        "non_parity_extension_rule": attempt.non_parity_extension_rule,
        "h3_comparison_theorem": attempt.h3_comparison_theorem,
        "c3_geometry_model": attempt.c3_geometry_model,
    }


def missing(requirements: tuple[str, ...], attempt: BridgeAttempt) -> list[str]:
    facts = _as_bool_map(attempt)
    return [name for name in requirements if not facts[name]]


def evaluate_attempt(attempt: BridgeAttempt) -> dict[str, Any]:
    total_missing = missing(TOTAL_FUNCTOR_REQUIREMENTS, attempt)
    full_missing = missing(FULL_BRIDGE_REQUIREMENTS, attempt)
    imported = bool(attempt.external_stipulations) or attempt.hidden_global_table

    if imported:
        verdict = "STIPULATED_OR_HIDDEN_BRIDGE"
        passes_negative_half = True
        reason = (
            "The bridge exists only by imported comparison, geometry, or hidden "
            "global table data, so it cannot count as source-derived from the finite "
            "parity witness."
        )
    elif not total_missing and full_missing:
        verdict = "FINITE_FUNCTOR_ONLY"
        passes_negative_half = True
        reason = (
            "The attempt has enough data for the finite parity subcategory but "
            "does not discharge the GU/H3 comparison or C3 geometry obligations."
        )
    elif total_missing:
        verdict = "NO_CANONICAL_TOTAL_FUNCTOR"
        passes_negative_half = True
        reason = (
            "The attempt lacks data needed to extend Phi_par beyond the finite "
            "SBP-parity subcategory."
        )
    else:
        verdict = "UNEXPECTED_FULL_BRIDGE"
        passes_negative_half = False
        reason = (
            "All full-bridge requirements appear source-derived; this would "
            "resurrect the route and should stop the negative-half verdict."
        )

    return {
        "attempt_id": attempt.attempt_id,
        "description": attempt.description,
        "facts": _as_bool_map(attempt),
        "hidden_global_table": attempt.hidden_global_table,
        "external_stipulations": list(attempt.external_stipulations),
        "missing_total_functor_requirements": total_missing,
        "missing_full_bridge_requirements": full_missing,
        "verdict": verdict,
        "passes_negative_half": passes_negative_half,
        "reason": reason,
    }


def fixture_attempts() -> tuple[BridgeAttempt, ...]:
    return (
        BridgeAttempt(
            attempt_id="finite_sbp_parity_subcategory",
            description=(
                "RUN-0055 style Phi_par: finite cover, localization, and SBP "
                "parity functional preserve the E054 flat Z/2 witness."
            ),
            cover_localization_rule=True,
            parity_functional=True,
            non_parity_extension_rule=False,
            h3_comparison_theorem=False,
            c3_geometry_model=False,
        ),
        BridgeAttempt(
            attempt_id="all_compat_without_non_parity_rule",
            description=(
                "Attempt to extend Compat_G^MLTT to all morphisms while only "
                "carrying the finite parity rule."
            ),
            cover_localization_rule=True,
            parity_functional=True,
            non_parity_extension_rule=False,
            h3_comparison_theorem=False,
            c3_geometry_model=False,
        ),
        BridgeAttempt(
            attempt_id="preselected_h3_comparison",
            description=(
                "Attach a comparison from the finite Z/2 class to the intended "
                "GU/H3 object as input rather than as a source-derived theorem."
            ),
            cover_localization_rule=True,
            parity_functional=True,
            non_parity_extension_rule=False,
            h3_comparison_theorem=True,
            c3_geometry_model=False,
            external_stipulations=("preselected_h3_comparison_theorem",),
        ),
        BridgeAttempt(
            attempt_id="imported_c3_geometry",
            description=(
                "Supply spacelike/correspondence geometry independently of the "
                "finite Cech witness."
            ),
            cover_localization_rule=True,
            parity_functional=True,
            non_parity_extension_rule=False,
            h3_comparison_theorem=False,
            c3_geometry_model=True,
            external_stipulations=("independent_spacelike_geometry_model",),
        ),
        BridgeAttempt(
            attempt_id="hidden_global_transition_table",
            description=(
                "Use a completed future table of transitions to force totality "
                "over future schema states."
            ),
            cover_localization_rule=True,
            parity_functional=True,
            non_parity_extension_rule=True,
            h3_comparison_theorem=True,
            c3_geometry_model=True,
            hidden_global_table=True,
        ),
    )


def run_fixture_suite() -> dict[str, Any]:
    attempts = [evaluate_attempt(attempt) for attempt in fixture_attempts()]
    by_id = {attempt["attempt_id"]: attempt for attempt in attempts}
    unexpected_positive = [
        attempt["attempt_id"]
        for attempt in attempts
        if attempt["verdict"] == "UNEXPECTED_FULL_BRIDGE"
    ]

    result = {
        "fixture_id": "cech_h3_functor_obl_001_negative_half",
        "claim_status_change": "none",
        "finite_cech_parity_residue_preserved": (
            by_id["finite_sbp_parity_subcategory"]["verdict"] == "NO_CANONICAL_TOTAL_FUNCTOR"
        ),
        "total_compat_g_mltt_functor_constructed": False,
        "gu_h3_bridge_discharged": False,
        "c3_geometry_derived": False,
        "unexpected_positive_attempts": unexpected_positive,
        "negative_half_passed": not unexpected_positive,
        "path_kill_reaffirmed": (
            "finite_filtered_Z2_local_system_as_sufficient_full_GU_H3_or_C3_geometry_bridge"
        ),
        "attempts": attempts,
        "next_pressure_route": "d_fork_expressiveness_threshold_fixture_or_w010_rerank",
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
        default=Path("tests/artifacts/cech_h3_functor_negative_half_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture_suite()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
