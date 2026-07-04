#!/usr/bin/env python3
"""Tests for tools/celext_celestial_boundary_fixture.py (RUN-0126)."""

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

    def test_later_celext_steps_and_claim_movement_are_explicitly_not_done(self) -> None:
        self.assertTrue(self.summary["steps_1_3_complete"])
        self.assertFalse(self.summary["BMS_functoriality_tested"])
        self.assertFalse(self.summary["source_side_Q_f_tested"])
        self.assertFalse(self.summary["ICO_prime_tested"])
        self.assertFalse(self.summary["absorber_tested"])
        self.assertFalse(self.summary["physics_derived_from_TI"])
        self.assertEqual(self.summary["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
