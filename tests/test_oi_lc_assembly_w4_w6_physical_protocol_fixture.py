#!/usr/bin/env python3
"""Tests for tools/oi_lc_assembly_w4_w6_physical_protocol_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import oi_lc_assembly_w4_w6_physical_protocol_fixture as fixture  # noqa: E402


class OILCAssemblyW4W6PhysicalProtocolFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.comparisons = self.result["comparisons"]
        self.evaluations = {
            evaluation["attempt_id"]: evaluation
            for evaluation in self.result["evaluations"]
        }

    def test_fixture_has_bigger_physical_protocol_scope(self) -> None:
        self.assertEqual(self.comparisons["attempt_count"], 6)
        self.assertEqual(self.comparisons["real_physical_attempt_count"], 4)
        self.assertTrue(self.comparisons["all_attempts_have_adapter_mapping"])
        self.assertEqual(
            self.result["physical_absorbers"],
            [
                "fixed_chemistry_or_reaction_network",
                "bounded_sampling_or_database_access",
                "experimenter_or_instrument_schema",
                "fixed_stochastic_or_search_process",
                "fixed_observable_algebra",
            ],
        )

    def test_real_physical_attempts_are_absorbed(self) -> None:
        self.assertTrue(self.comparisons["all_real_physical_attempts_absorbed"])
        self.assertEqual(
            self.evaluations["chemistry_reaction_network_trace"]["verdict"],
            "absorbed_fixed_chemistry",
        )
        self.assertEqual(
            self.evaluations["high_throughput_search_trace"]["verdict"],
            "absorbed_fixed_search_or_evolutionary_process",
        )
        self.assertEqual(
            self.evaluations["evolutionary_biosynthesis_trace"]["verdict"],
            "absorbed_fixed_search_or_evolutionary_process",
        )
        self.assertEqual(
            self.evaluations["instrument_schema_update_trace"]["verdict"],
            "absorbed_experimenter_or_instrument_schema",
        )

    def test_w1_and_w4_are_not_found_in_real_physical_attempts(self) -> None:
        self.assertFalse(self.comparisons["w1_real_physical_candidate_found"])
        self.assertFalse(self.comparisons["w4_real_physical_protocol_found"])
        self.assertTrue(
            self.comparisons["w5_record_preservation_available_for_real_attempts"]
        )
        self.assertFalse(self.comparisons["w6_real_physical_absorber_defeat_found"])

    def test_formal_local_w2_w3_survives_but_is_not_physical(self) -> None:
        formal = self.evaluations["formal_local_assembly_trace_from_e113"]
        self.assertTrue(self.comparisons["formal_local_w2_w3_preserved"])
        self.assertTrue(formal["w2_w3_supplied"])
        self.assertFalse(formal["w1_supplied"])
        self.assertFalse(formal["w4_physical_protocol_supplied"])
        self.assertFalse(formal["real_physical_candidate"])
        self.assertFalse(formal["adapter_gate_shape_passed"])

    def test_schematic_positive_shape_does_not_reopen_physics(self) -> None:
        schematic = self.evaluations["strict_positive_physical_protocol_shape"]
        self.assertTrue(self.comparisons["schematic_positive_shape_passes_adapter_gate"])
        self.assertFalse(self.comparisons["schematic_positive_is_real_candidate"])
        self.assertTrue(schematic["adapter_gate_shape_passed"])
        self.assertFalse(schematic["real_physical_candidate"])
        self.assertFalse(schematic["physical_source_issuance_established"])

    def test_ti_c020_remains_parked_and_routes_to_proof_assistant(self) -> None:
        self.assertTrue(self.comparisons["assembly_physical_bridge_currently_closed"])
        self.assertEqual(
            self.comparisons["assembly_current_scope"],
            "formal_local_w2_w3_only",
        )
        self.assertFalse(self.comparisons["physical_source_issuance_established"])
        self.assertFalse(self.comparisons["TI_C020_reopened"])
        self.assertFalse(self.result["verdict"]["Issue[S]^physical"])
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "proof_assistant_online_issuance_witness",
        )


if __name__ == "__main__":
    unittest.main()
