#!/usr/bin/env python3
"""Tests for tools/h8_d_fork_regime_signature_bundle.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import h8_d_fork_regime_signature_bundle as h8  # noqa: E402


class H8DForkRegimeSignatureBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = h8.run_signature_bundle()
        self.rows = {
            row["row_id"]: row for row in self.result["signature_rows"]
        }

    def test_bundle_reports_d_fork_boundary_without_deciding_it(self) -> None:
        self.assertTrue(self.result["d_fork_boundary_reportable"])
        self.assertIn("not_decision_procedure", self.result["kind"])
        self.assertEqual(
            self.result["fixed_inputs"]["d_fork_status"],
            "non_computable_structural_bit_not_decided",
        )

    def test_track_1_signatures_are_present(self) -> None:
        self.assertEqual(
            set(self.result["track_1_signature_row_ids"]),
            {
                "fts_depleting_curvature",
                "godelian_sustained_curvature",
                "h6_formal_local_osag_boundary",
            },
        )
        self.assertEqual(
            self.rows["fts_depleting_curvature"]["signature"],
            h8.FTS_SIGNATURE,
        )
        self.assertEqual(
            self.rows["godelian_sustained_curvature"]["signature"],
            h8.GODELIAN_SIGNATURE,
        )
        self.assertEqual(
            self.rows["h6_formal_local_osag_boundary"]["signature"],
            h8.BOUNDED_OSAG_SIGNATURE,
        )

    def test_terminal_controls_do_not_move_physical_or_claim_status(self) -> None:
        self.assertGreaterEqual(len(self.result["terminal_stop_row_ids"]), 5)
        for row in self.result["signature_rows"]:
            self.assertFalse(row["claim_movement_allowed"])
            self.assertFalse(row["physical_source_allowed"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            h8.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
