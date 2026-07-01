#!/usr/bin/env python3
"""Tests for tools/proof_assistant_online_issuance_witness.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import proof_assistant_online_issuance_witness as proof_checker  # noqa: E402


class ProofAssistantOnlineIssuanceWitnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = proof_checker.run_proof_check()
        self.summary = self.result["summary"]
        self.obligations = {
            item["obligation_id"]: item
            for item in self.result["obligations"]
        }

    def test_all_proof_obligations_pass(self) -> None:
        self.assertEqual(self.summary["obligation_count"], 9)
        self.assertEqual(self.summary["obligations_passed"], 9)
        self.assertTrue(self.summary["all_obligations_passed"])

    def test_core_typing_and_dependency_obligations_pass(self) -> None:
        for obligation_id in (
            "PA-O1-prefix-typing",
            "PA-O2-present-enumerator",
            "PA-O3-diagonal-dependency",
            "PA-O4-diagonal-separation",
            "PA-O5-witness-dependency",
            "PA-O6-source-trace",
        ):
            self.assertTrue(self.obligations[obligation_id]["passed"], obligation_id)

    def test_no_hidden_oracle_and_external_absorber_are_preserved(self) -> None:
        self.assertTrue(self.obligations["PA-O7-no-hidden-future-oracle"]["passed"])
        self.assertTrue(self.summary["no_hidden_future_oracle_preserved"])
        self.assertTrue(self.summary["external_platonist_absorber_still_available"])

    def test_scope_remains_local_constructive_only(self) -> None:
        self.assertTrue(self.obligations["PA-O8-comparator-scope"]["passed"])
        self.assertTrue(self.obligations["PA-O9-effect-typing"]["passed"])
        self.assertTrue(self.summary["Issue[S]^LC"])
        self.assertFalse(self.summary["Issue[S]^physical"])
        self.assertFalse(self.summary["TI_C020_reopened"])
        self.assertEqual(self.summary["claim_status_change"], "none")
        self.assertEqual(self.summary["next_gate"], "online_issuance_core_verdict_bundle")

    def test_limits_are_explicit(self) -> None:
        self.assertTrue(self.result["limits"]["not_lean_coq_agda"])
        self.assertTrue(self.result["limits"]["no_physical_source_issuance_established"])
        self.assertTrue(self.result["limits"]["external_platonist_completion_not_defeated"])
        self.assertEqual(self.result["limits"]["result_is_class_relative"], "OnlineIssuance^LC")


if __name__ == "__main__":
    unittest.main()

