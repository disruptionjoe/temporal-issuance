#!/usr/bin/env python3
"""Tests for tools/q_obl_001_quorum_validity_grounding.py (Q-OBL-001)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import q_obl_001_quorum_validity_grounding as fixture  # noqa: E402


class QGroundingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_stratified_trace()

    def test_non_circular_stratified_grounding(self) -> None:
        nc = self.result["non_circularity"]
        self.assertTrue(nc["holds"])
        self.assertFalse(nc["A_Sn_references_Q"])
        self.assertTrue(nc["Q_reads_only_history_fixed_A"])
        self.assertTrue(nc["dependency_is_dag_over_stages"])

    def test_additive_under_independence(self) -> None:
        val = self.result["valuation"]
        self.assertTrue(val["additive_under_independence"])

    def test_sub_additive_under_correlation(self) -> None:
        val = self.result["valuation"]
        self.assertTrue(val["sub_additive_under_correlation"])
        self.assertGreater(val["correlation_correction"], 0.0)

    def test_godelian_residue_is_finite_per_morphism(self) -> None:
        res = self.result["godelian_residue"]
        self.assertTrue(res["per_realized_morphism_Q_finite"])
        self.assertFalse(res["global_option_map_computable"])

    def test_obligation_discharged_without_claim_movement(self) -> None:
        self.assertTrue(self.result["obligation_discharged"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
