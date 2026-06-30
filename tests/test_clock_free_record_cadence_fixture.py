#!/usr/bin/env python3
"""Tests for tools/clock_free_record_cadence_fixture.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import clock_free_record_cadence_fixture as fixture  # noqa: E402


class ClockFreeRecordCadenceFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.systems = self.result["systems"]

    def test_c_beats_after_the_fact_reconciliation(self) -> None:
        self.assertFalse(self.systems["A"]["coherence_without_revision"])
        self.assertTrue(self.systems["C"]["coherence_without_revision"])
        self.assertTrue(self.result["comparisons"]["C_beats_A"])
        self.assertIn("p3", self.systems["A"]["revised_final_records"])

    def test_c_does_not_use_hidden_tick(self) -> None:
        self.assertEqual(self.systems["C"]["global_ticks_used"], 0)
        self.assertFalse(self.systems["C"]["hidden_total_order_used"])
        self.assertTrue(self.result["comparisons"]["C_avoids_B"])

    def test_hidden_tick_absorber_reproduces_coherence_but_is_flagged(self) -> None:
        self.assertTrue(self.systems["B"]["coherence_without_revision"])
        self.assertGreater(self.systems["B"]["global_ticks_used"], 0)
        self.assertTrue(self.systems["B"]["hidden_total_order_used"])
        self.assertEqual(self.systems["B"]["absorber_verdict"], "hidden_clock_absorber")

    def test_hostile_proposal_is_rejected_by_clock_free_constraint(self) -> None:
        self.assertIn("p3", self.systems["C"]["rejected_records"])
        self.assertIn("p4", self.systems["C"]["admitted_records"])
        self.assertEqual(self.systems["C"]["parity_obstructions"], 1)

    def test_no_source_claim_is_promoted(self) -> None:
        self.assertFalse(self.result["verdict"]["Issue[S]"])
        self.assertEqual(self.result["verdict"]["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
