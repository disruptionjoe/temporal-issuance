#!/usr/bin/env python3
"""Tests for tools/record_table_admissibility_taf_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import record_table_admissibility_taf_fixture as fixture  # noqa: E402


class RecordTableAdmissibilityTafFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.models = self.result["models"]
        self.comparisons = self.result["comparisons"]

    def test_no_time_column_in_either_model(self) -> None:
        self.assertTrue(self.comparisons["no_time_column"])
        for model in self.models.values():
            self.assertEqual(model["time_columns_present"], [])

    def test_taf_reconstruction_is_identical(self) -> None:
        self.assertTrue(self.comparisons["external_trace_equal"])
        self.assertTrue(self.comparisons["taf_reconstruction_equal"])
        self.assertTrue(self.comparisons["taF_absorbs_temporal_order"])

    def test_reconstructed_order_has_expected_partial_order_shape(self) -> None:
        order = self.result["taf_reconstruction"]["A_fixed_schema"]
        self.assertIn(["e_alpha_lock", "e_join_lock"], order["order_pairs"])
        self.assertIn(["e_beta_lock", "e_join_lock"], order["order_pairs"])
        self.assertIn(["e_alpha_lock", "e_beta_lock"], order["incomparable_pairs"])
        self.assertFalse(order["uses_time_column"])

    def test_prefix_model_has_nonfixed_admissibility_provenance(self) -> None:
        fixed = self.models["A_fixed_schema"]
        prefix = self.models["B_prefix_formed"]
        self.assertTrue(fixed["join_candidate_available_before_inputs"])
        self.assertTrue(fixed["join_compat_fixed_at_start"])
        self.assertFalse(prefix["join_candidate_available_before_inputs"])
        self.assertFalse(prefix["join_compat_fixed_at_start"])
        self.assertTrue(self.comparisons["ti_owned_admissibility_provenance_difference"])

    def test_fixed_completed_table_absorbs_external_behavior(self) -> None:
        self.assertTrue(self.comparisons["fixed_completed_table_absorbs_external_behavior"])
        self.assertFalse(self.comparisons["source_side_residue_found"])
        self.assertFalse(self.result["verdict"]["Issue[S]"])
        self.assertEqual(self.result["verdict"]["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
