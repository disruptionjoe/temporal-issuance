#!/usr/bin/env python3
"""Self-contained tests for tools/cech_sheaf_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import cech_sheaf_fixture as fixture  # noqa: E402


class CechSheafFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture_suite()
        self.main = self.result["main_case"]

    def test_main_fixture_is_conditional_nontrivial(self) -> None:
        self.assertEqual(self.main["outcome_class"], "D_prime")
        self.assertEqual(self.main["outcome_label"], "D'")
        self.assertEqual(self.main["fixture_verdict"], "DERIVED_NONTRIVIAL_COCYCLE")
        self.assertEqual(self.main["forced_cochain"], {"I_plus": "+1", "I_minus": "-1"})
        self.assertEqual(self.main["holonomy"], "-1")
        self.assertFalse(self.main["coboundary"])

    def test_transition_values_are_derived_not_stipulated(self) -> None:
        self.assertEqual(
            self.main["transition_provenance"],
            {"I_plus": "derived_from_C", "I_minus": "derived_from_C"},
        )
        self.assertEqual(self.main["forbidden_inputs_used"], [])
        for transition in self.main["overlap_transition_candidates"]:
            self.assertFalse(transition["external_input_used"])

    def test_tc_1_through_tc_11_are_satisfied_for_main_case(self) -> None:
        summary = self.main["tc_summary"]
        self.assertEqual(set(summary), {f"TC-{index}" for index in range(1, 12)})
        for tc_id, tc_result in summary.items():
            self.assertEqual(tc_result["status"], "pass", tc_id)

    def test_control_cases_cover_A_B_C(self) -> None:
        controls = self.result["control_cases"]
        self.assertEqual(
            controls["bare_sections_no_transition_rule"]["outcome_class"],
            "A",
        )
        self.assertEqual(
            controls["stipulated_nontrivial_transition_table"]["outcome_class"],
            "B",
        )
        self.assertEqual(
            controls["equality_only_compatibility"]["outcome_class"],
            "C",
        )

    def test_chsh_transfer_assessed_without_berry_input(self) -> None:
        chsh = self.result["chsh_transfer"]
        self.assertTrue(chsh["assessed"])
        self.assertEqual(chsh["holonomy"], "-1")
        self.assertFalse(chsh["coboundary"])
        self.assertFalse(chsh["berry_phase_input_used"])
        self.assertTrue(
            all(edge["provenance"] == "derived_from_C" for edge in chsh["edges"])
        )


if __name__ == "__main__":
    unittest.main()
