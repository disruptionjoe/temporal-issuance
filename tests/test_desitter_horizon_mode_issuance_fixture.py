#!/usr/bin/env python3
"""Tests for tools/desitter_horizon_mode_issuance_fixture.py (RUN-0124 big swing)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import desitter_horizon_mode_issuance_fixture as fixture  # noqa: E402


class DeSitterHorizonModeIssuanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()

    def test_fixed_background_is_absorbed_as_disclosure(self) -> None:
        fixed = self.result["fixed_background"]
        self.assertEqual(fixed["verdict"], "absorbed_as_fixed_source_disclosure")
        self.assertFalse(fixed["W_gate"]["W1_non_isomorphic_algebra_growth"])
        self.assertFalse(fixed["W_gate"]["W4_perturbation_non_factorization"])
        # W5 (record preservation) is the one physically-real property, and it does not by
        # itself supply source issuance.
        self.assertTrue(fixed["W_gate"]["W5_record_preservation"])

    def test_fixed_source_nulls_absorb_fixed_background(self) -> None:
        nulls = self.result["fixed_background"]["fixed_source_nulls_absorb"]
        for key in ("fixed_H_infty", "bounded_access_to_Mu_infty",
                    "fixed_stochastic_or_collapse_law",
                    "fixed_boundary_or_holographic_completion"):
            self.assertTrue(nulls[key], f"{key} should absorb the fixed-background candidate")

    def test_generated_lattice_matches_online_issuance_ceiling(self) -> None:
        gen = self.result["generated_lattice"]
        # Finite-prefix freshness survives (like OnlineIssuance^LC finite non-disclosure)...
        self.assertTrue(gen["finite_prefix_freshness_survives"])
        # ...but the whole family is absorbed by singleton enumeration (the E127 c.e. ceiling).
        self.assertTrue(gen["whole_family_absorbed_by_singleton"])
        self.assertEqual(
            gen["verdict"], "reduces_to_OnlineIssuance_LC_class_relative_residue")

    def test_no_new_physical_surplus_and_ti_c020_stays_parked(self) -> None:
        summary = self.result["summary"]
        self.assertFalse(summary["new_physical_surplus_over_formal_residue"])
        self.assertFalse(summary["physical_question_separable_from_D_FORK"])
        self.assertFalse(summary["Issue[S]^physical"])
        self.assertFalse(summary["TI_C020_reopened"])
        self.assertEqual(summary["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
