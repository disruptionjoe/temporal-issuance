#!/usr/bin/env python3
"""Tests for tools/clock_free_cadence_absorber_gauntlet.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import clock_free_cadence_absorber_gauntlet as gauntlet  # noqa: E402


class ClockFreeCadenceAbsorberGauntletTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = gauntlet.run_gauntlet()
        self.absorbers = self.result["absorbers"]

    def test_fixed_compatibility_absorbers_reproduce_c(self) -> None:
        for absorber_id in (
            "fixed_site_sheaf_gluing",
            "database_constraint_checking",
            "fixed_H_record_update",
            "fixed_latent_source_changing_access",
        ):
            self.assertTrue(self.absorbers[absorber_id]["reproduces_c_exactly"], absorber_id)
            self.assertEqual(self.absorbers[absorber_id]["verdict"], "absorbs_C")

    def test_causal_order_alone_fails(self) -> None:
        causal = self.absorbers["ordinary_causal_order_only"]
        self.assertFalse(causal["reproduces_c_exactly"])
        self.assertEqual(causal["rejected_records"], [])
        self.assertIn("order alone", causal["reason"])

    def test_no_source_side_residue_found(self) -> None:
        self.assertFalse(self.result["summary"]["source_side_residue_found"])
        self.assertFalse(self.result["verdict"]["Issue[S]"])
        self.assertEqual(self.result["verdict"]["claim_status_change"], "none")

    def test_absorber_summary_is_complete(self) -> None:
        self.assertEqual(self.result["summary"]["absorbing_count"], 4)
        self.assertEqual(self.result["summary"]["failing_count"], 1)
        self.assertEqual(
            self.result["summary"]["failing_absorbers"],
            ["ordinary_causal_order_only"],
        )


if __name__ == "__main__":
    unittest.main()
