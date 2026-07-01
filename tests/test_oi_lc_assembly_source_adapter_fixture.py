#!/usr/bin/env python3
"""Tests for tools/oi_lc_assembly_source_adapter_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import oi_lc_assembly_source_adapter_fixture as fixture  # noqa: E402


class OILCAssemblySourceAdapterFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.comparisons = self.result["comparisons"]
        self.evaluations = {
            evaluation["trace_id"]: evaluation
            for evaluation in self.result["evaluations"]
        }

    def test_assembly_index_detects_source_undefined_to_defined(self) -> None:
        local = self.evaluations["local_source_generated_constructor_candidate"]
        self.assertTrue(self.comparisons["assembly_index_computed"])
        self.assertIsNone(local["source_index_before"])
        self.assertEqual(local["source_index_after"], 2)
        self.assertTrue(local["source_d4"])
        self.assertTrue(local["adapter_witness_status"]["W2_new_admissibility_predicate"])
        self.assertTrue(local["adapter_witness_status"]["W3_construction_space_growth"])

    def test_projection_access_negative_control_is_rejected(self) -> None:
        projection = self.evaluations["projection_access_negative"]
        self.assertTrue(self.comparisons["projection_access_negative_rejected"])
        self.assertFalse(projection["source_d4"])
        self.assertTrue(projection["projection_d4"])
        self.assertTrue(projection["absorber_results"]["bounded_access_to_Mu_infty"])
        self.assertFalse(projection["assembly_source_gate_passed"])

    def test_fixed_completion_modeler_and_search_absorbers_reject_controls(self) -> None:
        fixed_complete = self.evaluations["fixed_complete_assembly_space_negative"]
        modeler = self.evaluations["experimenter_added_schema_negative"]
        search = self.evaluations["fixed_search_process_negative"]

        self.assertTrue(self.comparisons["fixed_complete_assembly_space_negative_rejected"])
        self.assertTrue(fixed_complete["absorber_results"]["fixed_complete_assembly_space"])
        self.assertFalse(fixed_complete["assembly_source_gate_passed"])

        self.assertTrue(self.comparisons["experimenter_added_schema_negative_rejected"])
        self.assertTrue(modeler["absorber_results"]["experimenter_added_schema"])
        self.assertFalse(modeler["assembly_source_gate_passed"])

        self.assertTrue(self.comparisons["fixed_search_process_negative_rejected"])
        self.assertTrue(search["absorber_results"]["fixed_stochastic_or_search_process"])
        self.assertFalse(search["assembly_source_gate_passed"])
        self.assertTrue(self.comparisons["all_negative_controls_rejected"])

    def test_local_candidate_survives_only_as_formal_source_trace(self) -> None:
        local = self.evaluations["local_source_generated_constructor_candidate"]
        self.assertTrue(self.comparisons["local_source_candidate_source_d4"])
        self.assertTrue(
            self.comparisons["local_source_candidate_targeted_absorbers_defeated"]
        )
        self.assertTrue(
            self.comparisons["local_source_candidate_passes_assembly_source_gate"]
        )
        self.assertFalse(local["adapter_contract_passed"])
        self.assertFalse(
            self.comparisons["local_source_candidate_adapter_contract_passed"]
        )
        self.assertFalse(local["adapter_witness_status"]["W1_non_isomorphic_algebra"])
        self.assertFalse(
            local["adapter_witness_status"]["W4_perturbation_non_factorization"]
        )

    def test_ti_c020_remains_parked_and_routes_to_physical_protocol(self) -> None:
        self.assertFalse(self.comparisons["physical_source_issuance_established"])
        self.assertFalse(self.comparisons["TI_C020_reopened"])
        self.assertTrue(self.result["verdict"]["Issue[S]^assembly_local"])
        self.assertFalse(self.result["verdict"]["Issue[S]^physical"])
        self.assertFalse(self.result["verdict"]["TI_C020_reopened"])
        self.assertEqual(
            self.result["verdict"]["next_gate"],
            "oi_lc_assembly_w4_w6_physical_protocol_fixture",
        )


if __name__ == "__main__":
    unittest.main()
