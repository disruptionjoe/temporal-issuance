#!/usr/bin/env python3
"""Tests for tools/t2_bounded_completion_barrier_theorem_contract.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import t2_bounded_completion_barrier_theorem_contract as t2  # noqa: E402


class T2BoundedCompletionBarrierTheoremContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = t2.run_theorem_contract()
        self.clauses = {
            clause["clause_id"]: clause for clause in self.result["clauses"]
        }

    def test_contract_is_packaged_as_bounded_theorem_clause(self) -> None:
        bounded = self.clauses["bounded_completion_barrier_contract"]

        self.assertTrue(self.result["contract_ready"])
        self.assertEqual(
            bounded["verdict"], t2.BOUNDED_THEOREM_CONTRACT_PACKAGED
        )
        self.assertTrue(bounded["theorem_clause"])
        self.assertIn(
            "bounded_completion_barrier_contract",
            self.result["theorem_clause_ids"],
        )

    def test_counterexample_gate_is_active_and_specific(self) -> None:
        gate = self.clauses["counterexample_activation_gate"]

        self.assertTrue(self.result["counterexample_gate_active"])
        self.assertEqual(gate["verdict"], t2.COUNTEREXAMPLE_GATE_ACTIVE)
        for obligation in (
            "new_concrete_packet",
            "h7_admitted",
            "maps_all_adapter_p_fields",
            "defeats_whole_family_completion",
            "does_not_treat_h8_as_d_fork_decision",
        ):
            self.assertIn(obligation, self.result["counterexample_obligations"])

    def test_overclaims_are_terminally_rejected(self) -> None:
        self.assertEqual(
            self.clauses["reject_universal_physical_no_go"]["verdict"],
            t2.UNIVERSAL_PHYSICAL_NO_GO_REJECTED,
        )
        self.assertEqual(
            self.clauses["reject_physical_source_theorem"]["verdict"],
            t2.PHYSICAL_SOURCE_THEOREM_REJECTED,
        )
        self.assertEqual(
            self.clauses["reject_d_fork_decision"]["verdict"],
            t2.D_FORK_DECISION_REJECTED,
        )
        self.assertEqual(
            set(self.result["terminal_overclaim_clause_ids"]),
            {
                "reject_universal_physical_no_go",
                "reject_physical_source_theorem",
                "reject_d_fork_decision",
            },
        )

    def test_scope_limits_prevent_universal_reading(self) -> None:
        self.assertIn(
            "bounded_to_current_adapter_p_trace_class",
            self.result["scope_limit_ids"],
        )
        self.assertIn(
            "not_universal_over_all_physics", self.result["scope_limit_ids"]
        )
        self.assertTrue(self.result["blocks_universal_physical_no_go"])
        self.assertTrue(self.result["blocks_physical_source_theorem"])
        self.assertTrue(self.result["blocks_d_fork_decision"])

    def test_no_claim_or_physical_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            t2.write_json(self.result, output)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
