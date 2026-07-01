#!/usr/bin/env python3
"""Tests for tools/record_table_no_fixed_schema_gauntlet.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import record_table_no_fixed_schema_gauntlet as gauntlet  # noqa: E402


class RecordTableNoFixedSchemaGauntletTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = gauntlet.run_gauntlet()
        self.target = self.result["target_signature"]
        self.comparisons = self.result["comparisons"]
        self.absorbers = self.result["absorbers"]

    def test_formation_records_are_first_class(self) -> None:
        self.assertTrue(self.comparisons["formation_records_first_class"])
        self.assertEqual(
            self.comparisons["formation_kinds_present"],
            ["form_candidate", "form_compat", "form_schema", "form_witness"],
        )
        self.assertEqual(len(self.target["formation_records"]), 4)

    def test_taf_trace_and_rows_are_preserved(self) -> None:
        self.assertTrue(self.comparisons["taf_trace_preserved_by_absorbers"])
        self.assertTrue(self.comparisons["row_records_preserved_by_absorbers"])
        self.assertEqual(
            self.target["taf_reconstruction"]["incomparable_pairs"],
            [["e_alpha_lock", "e_beta_lock"]],
        )
        self.assertFalse(self.target["time_is_column"])

    def test_witness_dependencies_and_prefix_availability_are_preserved(self) -> None:
        self.assertTrue(self.comparisons["witness_dependencies_preserved_by_absorbers"])
        self.assertTrue(self.comparisons["prefix_availability_preserved_by_absorbers"])
        self.assertFalse(
            self.comparisons["fixed_precontainment_needs_to_make_prior_objects_available"]
        )
        self.assertEqual(
            self.target["witness_dependencies"]["w_join_from_two_locked_inputs"],
            [
                "f_candidate_join",
                "f_compat_join",
                "r_alpha_locked",
                "r_beta_locked",
            ],
        )

    def test_all_four_fixed_precontainment_absorbers_succeed(self) -> None:
        self.assertEqual(self.comparisons["absorber_count"], 4)
        self.assertEqual(self.comparisons["absorbing_count"], 4)
        self.assertTrue(self.comparisons["all_fixed_precontainment_absorbers_succeed"])
        for absorber in self.absorbers:
            self.assertTrue(absorber["precontains_all_objects"])
            self.assertTrue(absorber["absorbs"])

    def test_result_demotes_independent_record_table_source_route(self) -> None:
        self.assertFalse(self.comparisons["source_side_residue_found"])
        self.assertFalse(self.result["verdict"]["Issue[S]"])
        self.assertTrue(
            self.result["verdict"]["demote_record_table_ti_as_independent_source_route"]
        )
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "record_table_online_issuance_lift_or_demote",
        )


if __name__ == "__main__":
    unittest.main()
