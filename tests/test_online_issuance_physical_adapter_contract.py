#!/usr/bin/env python3
"""Tests for tools/online_issuance_physical_adapter_contract.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import online_issuance_physical_adapter_contract as contract  # noqa: E402


class OnlineIssuancePhysicalAdapterContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = contract.run_contract()
        self.comparisons = self.result["comparisons"]
        self.evaluations = {
            evaluation["candidate_id"]: evaluation
            for evaluation in self.result["candidate_evaluations"]
        }

    def test_adapter_fields_are_defined(self) -> None:
        self.assertTrue(self.comparisons["contract_well_formed"])
        self.assertTrue(self.comparisons["all_required_adapter_fields_defined"])
        self.assertEqual(
            self.comparisons["adapter_fields_defined"],
            ["Adm_n", "Gamma_n", "Gamma_n_plus_1", "e_n", "tau_n", "w_n"],
        )

    def test_w1_w6_gate_and_absorbers_are_defined(self) -> None:
        self.assertEqual(
            self.comparisons["w1_w6_gate_ids"],
            ["W1", "W2", "W3", "W4", "W5", "W6"],
        )
        self.assertTrue(self.comparisons["w1_w6_gate_defined"])
        self.assertTrue(self.comparisons["source_growth_core_requires_w1_or_w2_or_w3"])
        self.assertTrue(self.comparisons["absorber_control_requires_w4_w5_w6"])
        self.assertTrue(self.comparisons["fixed_source_absorber_nulls_defined"])

    def test_negative_fixed_h_control_is_rejected(self) -> None:
        negative = self.evaluations["negative_fixed_h_readout"]
        self.assertTrue(self.comparisons["negative_fixed_h_control_rejected"])
        self.assertFalse(negative["adapter_contract_passed"])
        self.assertFalse(negative["source_growth_core_supplied"])
        self.assertEqual(
            self.comparisons["negative_fixed_h_reason"],
            "no W1-W3 source-growth core witness supplied",
        )

    def test_schematic_positive_shape_passes_but_is_not_real_candidate(self) -> None:
        schematic = self.evaluations["schematic_positive_adapter_shape"]
        self.assertTrue(self.comparisons["schematic_positive_shape_admitted"])
        self.assertTrue(schematic["adapter_contract_passed"])
        self.assertFalse(self.comparisons["schematic_positive_is_real_candidate"])
        self.assertFalse(schematic["physical_source_issuance_established"])

    def test_contract_does_not_reopen_ti_c020_without_candidate(self) -> None:
        self.assertFalse(self.comparisons["physical_source_issuance_established"])
        self.assertFalse(self.comparisons["candidate_selected_for_fixture"])
        self.assertFalse(self.result["verdict"]["Issue[S]^physical"])
        self.assertFalse(self.result["verdict"]["TI_C020_reopened"])
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "oi_lc_candidate_scout_w1_w6_table",
        )


if __name__ == "__main__":
    unittest.main()
