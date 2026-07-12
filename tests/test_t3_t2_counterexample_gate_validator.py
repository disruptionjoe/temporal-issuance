#!/usr/bin/env python3
"""Tests for tools/t3_t2_counterexample_gate_validator.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import t3_t2_counterexample_gate_validator as t3  # noqa: E402


class T3T2CounterexampleGateValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = t3.run_gate_validator()
        self.decisions = {
            decision["packet_id"]: decision for decision in self.result["decisions"]
        }

    def test_gate_is_validated_without_real_counterexample(self) -> None:
        self.assertTrue(self.result["contract_ready"])
        self.assertTrue(self.result["counterexample_gate_validated"])
        self.assertEqual(
            self.result["synthetic_revision_control_id"],
            "synthetic_full_counterexample_control",
        )
        self.assertFalse(self.result["real_counterexample_packet_found"])

    def test_known_formal_and_physical_near_misses_do_not_trigger_revision(self) -> None:
        self.assertEqual(
            self.decisions["bounded_formal_local_osag_support"]["verdict"],
            t3.BOUNDED_CONDITIONAL_NOT_COUNTEREXAMPLE,
        )
        self.assertEqual(
            self.decisions["crispr_like_fixed_sequence_near_miss"]["verdict"],
            t3.PHYSICAL_NEAR_MISS_NOT_COUNTEREXAMPLE,
        )
        self.assertFalse(
            self.decisions["bounded_formal_local_osag_support"]["revision_trigger"]
        )
        self.assertFalse(
            self.decisions["crispr_like_fixed_sequence_near_miss"]["revision_trigger"]
        )

    def test_terminal_controls_reject_imports_readout_and_h8_shortcut(self) -> None:
        self.assertEqual(
            self.decisions["imported_completion_oracle_packet"]["verdict"],
            t3.IMPORTED_STRUCTURE_REJECTED,
        )
        self.assertEqual(
            self.decisions["readout_finality_packet"]["verdict"],
            t3.READOUT_FINALITY_REJECTED,
        )
        self.assertEqual(
            self.decisions["h8_decision_shortcut_packet"]["verdict"],
            t3.D_FORK_DECISION_SHORTCUT_REJECTED,
        )
        for packet_id in (
            "imported_completion_oracle_packet",
            "readout_finality_packet",
            "h8_decision_shortcut_packet",
        ):
            self.assertIn(packet_id, self.result["terminal_control_ids"])

    def test_partial_physical_packet_lists_missing_w4(self) -> None:
        partial = self.decisions["partial_physical_packet_missing_w4"]

        self.assertEqual(
            partial["verdict"], t3.COUNTEREXAMPLE_OBLIGATIONS_INCOMPLETE
        )
        self.assertIn(
            "supplies_w4_perturbation_non_factorization",
            partial["missing_obligations"],
        )
        self.assertFalse(partial["revision_trigger"])

    def test_synthetic_full_control_would_trigger_revision(self) -> None:
        synthetic = self.decisions["synthetic_full_counterexample_control"]

        self.assertEqual(synthetic["verdict"], t3.CONTRACT_REVISION_TRIGGERED)
        self.assertTrue(synthetic["revision_trigger"])
        self.assertTrue(synthetic["control_only"])
        self.assertEqual(synthetic["missing_obligations"], [])

    def test_no_claim_or_physical_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            t3.write_json(self.result, output)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
