#!/usr/bin/env python3
"""Tests for tools/record_table_online_issuance_lift.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import record_table_online_issuance_lift as lift  # noqa: E402


class RecordTableOnlineIssuanceLiftTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = lift.run_lift()
        self.comparisons = self.result["comparisons"]
        self.gates = {gate["gate_id"]: gate for gate in self.result["properness_gates"]}

    def test_all_record_table_components_map_to_online_issuance(self) -> None:
        self.assertTrue(self.comparisons["component_mapping_total"])
        self.assertTrue(self.comparisons["record_table_is_online_issuance_interface"])
        mapped = {
            entry["record_table_component"]: entry["online_issuance_component"]
            for entry in self.result["component_mapping"]
        }
        self.assertEqual(mapped["Schema_n"], "Gamma_n")
        self.assertEqual(mapped["Compat_n"], "Adm_n")
        self.assertEqual(mapped["Witness_n"], "w_n : Adm_n(e_n)")

    def test_no_hidden_oracle_gate_fails_for_record_table_itself(self) -> None:
        self.assertTrue(self.comparisons["fails_no_hidden_oracle_gate"])
        self.assertFalse(self.gates["P4"]["passed_by_record_table"])
        self.assertIn("fixed universal schema", self.gates["P4"]["basis"])

    def test_other_properness_gates_are_only_interface_successes(self) -> None:
        self.assertTrue(self.gates["P1"]["passed_by_record_table"])
        self.assertTrue(self.gates["P2"]["passed_by_record_table"])
        self.assertTrue(self.gates["P3"]["passed_by_record_table"])
        self.assertTrue(self.gates["P5"]["passed_by_record_table"])
        self.assertFalse(self.comparisons["properness_gates_pass_without_extra_axioms"])

    def test_no_productive_self_encoding_witness_or_e091_surplus(self) -> None:
        self.assertFalse(self.comparisons["productive_self_encoding_witness_present"])
        self.assertFalse(self.comparisons["adds_formal_surplus_over_e091"])
        self.assertFalse(self.comparisons["inherits_e091_residue_without_extra_axioms"])

    def test_record_table_is_archived_as_vocabulary(self) -> None:
        self.assertTrue(self.comparisons["record_table_archive_as_vocabulary"])
        self.assertTrue(self.comparisons["physics_adapter_route_closed_for_record_table"])
        self.assertFalse(self.comparisons["source_side_residue_found"])
        self.assertTrue(self.result["verdict"]["demote_record_table_ti"])
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "machine_check_online_issuance_witness_or_frontier_rerank",
        )


if __name__ == "__main__":
    unittest.main()
