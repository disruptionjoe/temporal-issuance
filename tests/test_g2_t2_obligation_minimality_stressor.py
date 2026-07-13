#!/usr/bin/env python3
"""Tests for tools/g2_t2_obligation_minimality_stressor.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import g2_t2_obligation_minimality_stressor as g2  # noqa: E402


class G2T2ObligationMinimalityStressorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = g2.run_minimality_stressor()
        self.by_obligation = {
            row["obligation_id"]: row for row in self.result["omission_results"]
        }

    def test_all_obligations_are_load_bearing(self) -> None:
        self.assertTrue(self.result["counterexample_gate_validated"])
        self.assertTrue(self.result["all_obligations_load_bearing"])
        self.assertEqual(self.result["redundant_obligation_ids"], [])
        self.assertEqual(self.result["overstrong_obligation_ids"], [])
        self.assertEqual(
            self.result["obligation_count"],
            len(self.result["load_bearing_obligation_ids"]),
        )

    def test_terminal_safety_obligations_are_named(self) -> None:
        for obligation in (
            "no_hidden_completion_oracle",
            "no_imported_law_or_schema",
            "not_readout_or_finality_only",
            "does_not_treat_h8_as_d_fork_decision",
        ):
            self.assertIn(obligation, self.result["terminal_safety_obligation_ids"])
            self.assertTrue(self.by_obligation[obligation]["terminal"])

    def test_missing_w4_is_load_bearing_not_redundant(self) -> None:
        w4 = self.by_obligation["supplies_w4_perturbation_non_factorization"]

        self.assertEqual(w4["omission_class"], g2.OBLIGATION_LOAD_BEARING)
        self.assertFalse(w4["revision_still_triggers"])
        self.assertFalse(w4["terminal"])

    def test_no_real_packet_or_claim_movement(self) -> None:
        self.assertFalse(self.result["real_counterexample_packet_found"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            g2.write_json(self.result, output)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
