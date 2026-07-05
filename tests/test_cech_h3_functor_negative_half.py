#!/usr/bin/env python3
"""Tests for tools/cech_h3_functor_negative_half.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import cech_h3_functor_negative_half as fixture  # noqa: E402


class CechH3FunctorNegativeHalfTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture_suite()
        self.by_id = {
            attempt["attempt_id"]: attempt for attempt in self.result["attempts"]
        }

    def test_negative_half_passes_without_claim_movement(self) -> None:
        self.assertTrue(self.result["negative_half_passed"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(self.result["unexpected_positive_attempts"], [])
        self.assertFalse(self.result["gu_h3_bridge_discharged"])
        self.assertFalse(self.result["c3_geometry_derived"])

    def test_finite_parity_residue_is_preserved_but_not_total(self) -> None:
        attempt = self.by_id["finite_sbp_parity_subcategory"]
        self.assertEqual(attempt["verdict"], "NO_CANONICAL_TOTAL_FUNCTOR")
        self.assertTrue(attempt["facts"]["cover_localization_rule"])
        self.assertTrue(attempt["facts"]["parity_functional"])
        self.assertIn(
            "non_parity_extension_rule",
            attempt["missing_total_functor_requirements"],
        )
        self.assertTrue(self.result["finite_cech_parity_residue_preserved"])

    def test_preselected_h3_comparison_is_rejected_as_stipulated(self) -> None:
        attempt = self.by_id["preselected_h3_comparison"]
        self.assertEqual(attempt["verdict"], "STIPULATED_OR_HIDDEN_BRIDGE")
        self.assertIn(
            "preselected_h3_comparison_theorem",
            attempt["external_stipulations"],
        )
        self.assertTrue(attempt["passes_negative_half"])

    def test_c3_geometry_is_not_derived_from_finite_witness(self) -> None:
        attempt = self.by_id["imported_c3_geometry"]
        self.assertEqual(attempt["verdict"], "STIPULATED_OR_HIDDEN_BRIDGE")
        self.assertTrue(attempt["facts"]["c3_geometry_model"])
        self.assertIn(
            "independent_spacelike_geometry_model",
            attempt["external_stipulations"],
        )

    def test_hidden_global_table_is_an_absorber_not_a_source_witness(self) -> None:
        attempt = self.by_id["hidden_global_transition_table"]
        self.assertEqual(attempt["verdict"], "STIPULATED_OR_HIDDEN_BRIDGE")
        self.assertTrue(attempt["hidden_global_table"])
        self.assertTrue(attempt["passes_negative_half"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
