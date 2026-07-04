#!/usr/bin/env python3
"""Tests for tools/celext_celestial_boundary_fixture.py (RUN-0126/RUN-0127)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import celext_celestial_boundary_fixture as fixture  # noqa: E402


class CelExtCelestialBoundaryFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.summary = self.result["summary"]

    def test_step_1_typed_boundary_objects_pass(self) -> None:
        self.assertTrue(self.summary["step_1_typed_boundary_object"])
        for obj in self.result["positive_fragment"]["objects"]:
            self.assertEqual(obj["sphere"], "S2")
            self.assertTrue(obj["typed_boundary_object"])
            self.assertEqual(obj["forbidden_inputs_used"], [])

    def test_step_2_admissible_boundary_morphism_passes(self) -> None:
        morphism = self.result["positive_fragment"]["morphism"]
        self.assertTrue(self.summary["step_2_admissible_boundary_morphism"])
        self.assertTrue(morphism["target_charge_matches"])
        self.assertTrue(morphism["ward_identity_preserved"])
        self.assertEqual(morphism["forbidden_inputs_used"], [])

    def test_step_3_composition_is_additive_and_admissible(self) -> None:
        composition = self.result["positive_fragment"]["composition"]
        self.assertTrue(self.summary["step_3_additive_composition"])
        self.assertTrue(composition["additive_composition"])
        self.assertEqual(
            composition["composition_trace"],
            ["I_soft_plus_1", "I_soft_plus_2"],
        )
        self.assertEqual(composition["composite"]["soft_shift"], 3)
        self.assertEqual(composition["composite"]["actual_target_charge"], 3)

    def test_controls_reject_mismatch_bulk_import_and_nonadditive_composition(self) -> None:
        controls = self.result["controls"]
        self.assertTrue(controls["target_charge_mismatch_rejected"])
        self.assertTrue(controls["bulk_import_rejected"])
        self.assertTrue(controls["nonadditive_composition_rejected"])

    def test_step_4_supertranslation_action_is_functorial(self) -> None:
        action = self.result["steps_4_6_fragment"]["supertranslation_action"]
        self.assertTrue(self.summary["step_4_supertranslation_functoriality"])
        self.assertTrue(action["identity_preserved"])
        self.assertTrue(action["composition_preserved"])
        self.assertTrue(action["admissibility_preserved"])
        self.assertEqual(action["forbidden_inputs_used"], [])

    def test_step_5_q_f_is_boundary_internal_but_not_ti_derived(self) -> None:
        q_f = self.result["steps_4_6_fragment"]["source_side_soft_charge"]
        self.assertTrue(self.summary["source_side_Q_f_tested"])
        self.assertTrue(self.summary["step_5_source_side_Q_f_relative_to_CelExt"])
        self.assertFalse(self.summary["step_5_source_side_Q_f_relative_to_current_TI"])
        self.assertTrue(q_f["source_side_Q_f"])
        self.assertEqual(q_f["q_value"], 21)
        self.assertEqual(q_f["forbidden_inputs_used"], [])
        self.assertFalse(q_f["uses_bulk_hamiltonian"])
        self.assertFalse(q_f["uses_bulk_s_matrix"])
        self.assertFalse(q_f["uses_precomputed_bms_charge"])

    def test_step_6_absorber_rejects_s_matrix_relabeling_and_imported_charge(self) -> None:
        absorber = self.result["steps_4_6_fragment"]["absorber"]
        self.assertTrue(self.summary["absorber_tested"])
        self.assertTrue(self.summary["step_6_s_matrix_relabeling_absorber_rejected"])
        self.assertTrue(absorber["positive_fragment_not_s_matrix_relabeling"])
        self.assertTrue(absorber["celestial_s_matrix_relabeling_rejected"])
        self.assertTrue(absorber["precomputed_bms_charge_rejected"])
        self.assertFalse(absorber["absorbed_by_celestial_s_matrix_relabeling"])

    def test_ico_prime_caveat_and_claim_movement_are_explicit(self) -> None:
        ico_prime = self.result["steps_4_6_fragment"]["ico_prime"]
        self.assertTrue(self.summary["steps_1_3_complete"])
        self.assertTrue(self.summary["steps_4_6_complete"])
        self.assertTrue(self.summary["steps_1_6_complete"])
        self.assertTrue(self.summary["BMS_functoriality_tested"])
        self.assertTrue(self.summary["ICO_prime_tested"])
        self.assertTrue(ico_prime["target_import_avoided_conditionally"])
        self.assertTrue(ico_prime["insufficient_source_data_unresolved_for_current_TI"])
        self.assertEqual(
            ico_prime["verdict"],
            "conditional_celext_internal_boundary_charge_not_ti_derivation",
        )
        self.assertFalse(self.summary["physics_derived_from_TI"])
        self.assertEqual(self.summary["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
