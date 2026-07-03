#!/usr/bin/env python3
"""Tests for tools/ti_c022_record_reality_typing_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import ti_c022_record_reality_typing_fixture as fixture  # noqa: E402


class TIC022RecordRealityTypingFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.cases = {
            case["case_id"]: case for case in self.result["case_results"]
        }

    def _event(self, case_id: str, event_id: str) -> dict[str, object]:
        case = self.cases[case_id]
        return {
            event["event_id"]: event for event in case["event_verdicts"]
        }[event_id]

    def test_no_same_assumption_divergence_is_found(self) -> None:
        self.assertFalse(self.result["comparisons"]["same_assumption_divergence_found"])
        self.assertEqual(self.result["same_assumption_divergences"], [])
        self.assertTrue(self.result["comparisons"]["operational_absorption_reaffirmed"])

    def test_unforked_and_canonical_branch_records_match(self) -> None:
        e1 = self._event("unforked_progress", "e1")
        e_a1 = self._event("temporary_fork_canonicalized", "e_a1")

        self.assertTrue(e1["ti_c022_record_real"])
        self.assertTrue(e1["canonical_chain_final"])
        self.assertTrue(e_a1["ti_c022_record_real"])
        self.assertTrue(e_a1["canonical_chain_final"])

    def test_orphaned_and_permanent_fork_records_are_not_real(self) -> None:
        orphan = self._event("temporary_fork_canonicalized", "e_b1")
        fork_a = self._event("permanent_fork_no_canonical_carrier", "e_a2")
        fork_b = self._event("permanent_fork_no_canonical_carrier", "e_b2")

        for event in (orphan, fork_a, fork_b):
            self.assertTrue(event["branch_local_integrity"])
            self.assertFalse(event["ti_c022_record_real"])
            self.assertFalse(event["canonical_chain_final"])

    def test_permanent_fork_has_no_unique_carrier(self) -> None:
        case = self.cases["permanent_fork_no_canonical_carrier"]
        self.assertEqual(case["cofinal_branches"], ["A", "B"])
        self.assertFalse(case["unique_cofinal_carrier_exists"])
        self.assertFalse(case["unique_canonical_carrier_exists"])

    def test_apparent_divergence_requires_assumption_change(self) -> None:
        self.assertTrue(
            self.result["comparisons"]["apparent_divergences_require_assumption_change"]
        )
        invalid_moves = {
            control["invalid_move"] for control in self.result["invalid_divergence_controls"]
        }
        self.assertIn("treat_branch_local_integrity_as_canonical_finality", invalid_moves)
        self.assertIn("declare_orphaned_branch_record_ontologically_real_by_override", invalid_moves)

    def test_claim_status_and_next_gate_are_bounded(self) -> None:
        verdict = self.result["verdict"]
        self.assertFalse(verdict["TI_C022_independent_operational_surplus"])
        self.assertEqual(verdict["remaining_surplus"], "ontological_record_reality_typing")
        self.assertFalse(verdict["resurrection_trigger_met"])
        self.assertEqual(verdict["claim_status_change"], "none")
        self.assertEqual(
            verdict["next_gate"],
            "W010_frontier_selection_after_ti_c022_record_reality_fixture",
        )


if __name__ == "__main__":
    unittest.main()
