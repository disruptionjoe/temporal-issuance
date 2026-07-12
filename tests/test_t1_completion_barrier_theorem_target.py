#!/usr/bin/env python3
"""Tests for tools/t1_completion_barrier_theorem_target.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import t1_completion_barrier_theorem_target as t1  # noqa: E402


class T1CompletionBarrierTheoremTargetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = t1.run_theorem_target()
        self.decisions = {
            decision["target_id"]: decision for decision in self.result["decisions"]
        }

    def test_bounded_theorem_target_is_ready(self) -> None:
        bounded = self.decisions["bounded_adapter_p_completion_barrier"]

        self.assertTrue(self.result["fixed_floor_satisfied"])
        self.assertTrue(self.result["theorem_contract_ready"])
        self.assertEqual(bounded["verdict"], t1.BOUNDED_THEOREM_TARGET_READY)
        self.assertTrue(bounded["theorem_target_ready"])
        self.assertTrue(bounded["supports_track_1"])

    def test_overclaims_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["universal_physical_no_go"]["verdict"],
            t1.UNIVERSAL_PHYSICAL_NO_GO_NOT_READY,
        )
        self.assertEqual(
            self.decisions["physical_source_from_bounded_osag"]["verdict"],
            t1.PHYSICAL_SOURCE_THEOREM_BLOCKED,
        )
        self.assertEqual(
            self.decisions["d_fork_decision_from_h8"]["verdict"],
            t1.D_FORK_DECISION_THEOREM_BLOCKED,
        )
        self.assertEqual(
            set(self.result["terminal_overclaim_ids"]),
            {
                "universal_physical_no_go",
                "physical_source_from_bounded_osag",
                "d_fork_decision_from_h8",
            },
        )

    def test_counterexample_contract_is_explicit(self) -> None:
        counterexample = self.decisions["new_packet_counterexample_contract"]

        self.assertEqual(
            counterexample["verdict"], t1.COUNTEREXAMPLE_CONTRACT_READY
        )
        self.assertTrue(self.result["counterexample_contract_ready"])
        for obligation in (
            "h7_admitted",
            "defeats_whole_family_completion",
            "supplies_w1_non_isomorphic_physical_algebra",
            "supplies_w4_perturbation_non_factorization",
            "supplies_w5_record_preservation_comparison",
            "does_not_treat_h8_as_d_fork_decision",
        ):
            self.assertIn(obligation, self.result["counterexample_obligations"])

    def test_no_claim_or_physical_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            t1.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
