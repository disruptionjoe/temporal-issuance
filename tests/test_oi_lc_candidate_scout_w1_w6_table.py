#!/usr/bin/env python3
"""Tests for tools/oi_lc_candidate_scout_w1_w6_table.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import oi_lc_candidate_scout_w1_w6_table as scout  # noqa: E402


class OILCCandidateScoutW1W6TableTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = scout.run_scout()
        self.comparisons = self.result["comparisons"]
        self.rows = {
            row["candidate_id"]: row for row in self.result["candidate_table"]
        }

    def test_table_is_structured_adapter_p_scout(self) -> None:
        self.assertEqual(self.comparisons["candidate_count"], 7)
        self.assertTrue(self.comparisons["expected_candidates_present"])
        self.assertTrue(self.comparisons["structured_adapter_scoring_table"])
        self.assertEqual(
            self.result["adapter_fields"],
            ["Adm_n", "Gamma_n", "Gamma_n_plus_1", "e_n", "tau_n", "w_n"],
        )
        self.assertEqual(
            self.result["w1_w6_gate_ids"],
            ["W1", "W2", "W3", "W4", "W5", "W6"],
        )
        self.assertEqual(len(self.result["fixed_source_null_ids"]), 7)

    def test_assembly_theory_is_fixture_candidate_only(self) -> None:
        assembly = self.rows["assembly_theory_source_assembly_index"]
        self.assertTrue(self.comparisons["assembly_source_index_selected_for_fixture"])
        self.assertEqual(assembly["stop_rule_verdict"], "fixture_candidate")
        self.assertTrue(assembly["concrete_witness_obligation"])
        self.assertFalse(assembly["physical_source_issuance_established"])
        self.assertEqual(
            self.comparisons["selected_fixture_candidate"],
            "assembly_theory_source_assembly_index",
        )
        self.assertFalse(self.comparisons["selected_fixture_candidate_is_evidence"])

    def test_obvious_shortcuts_are_killed(self) -> None:
        self.assertTrue(self.comparisons["quantum_contextuality_shortcut_killed"])
        self.assertTrue(self.comparisons["holographic_boundary_shortcut_killed"])
        self.assertTrue(self.comparisons["orch_or_substrate_shortcut_killed"])
        self.assertTrue(self.comparisons["dual_record_current_form_shortcut_killed"])
        self.assertEqual(
            self.rows["holographic_boundary_encoding"]["fixed_source_nulls"][
                "fixed_boundary_or_holographic_completion"
            ],
            "undefeated",
        )
        self.assertEqual(
            self.rows["quantum_measurement_contextuality"]["fixed_source_nulls"][
                "fixed_H_infty"
            ],
            "undefeated",
        )

    def test_promising_but_under_typed_routes_are_parked(self) -> None:
        self.assertTrue(self.comparisons["causal_set_route_parked"])
        self.assertTrue(self.comparisons["gu_missing_piece_route_parked"])
        self.assertEqual(
            self.rows["causal_set_sequential_growth"]["stop_rule_verdict"],
            "parked",
        )
        self.assertEqual(
            self.rows["gu_missing_piece_adapter_language"]["stop_rule_verdict"],
            "parked",
        )

    def test_ti_c020_remains_parked_and_routes_to_absorber_fixture(self) -> None:
        self.assertFalse(self.comparisons["physical_source_issuance_established"])
        self.assertFalse(self.comparisons["TI_C020_reopened"])
        self.assertFalse(self.result["verdict"]["Issue[S]^physical"])
        self.assertFalse(self.result["verdict"]["TI_C020_reopened"])
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "oi_lc_assembly_source_adapter_fixture",
        )


if __name__ == "__main__":
    unittest.main()
