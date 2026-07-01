#!/usr/bin/env python3
"""Tests for tools/online_issuance_witness_checker.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import online_issuance_witness_checker as checker  # noqa: E402


class OnlineIssuanceWitnessCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = checker.run_check()
        self.comparisons = self.result["comparisons"]
        self.effect_typing = self.result["effect_typing"]

    def test_present_enumerator_and_diagonal_are_formed(self) -> None:
        self.assertTrue(self.comparisons["present_enumerator_valid"])
        self.assertTrue(self.comparisons["diagonal_candidate_formed"])
        self.assertTrue(self.comparisons["diagonal_candidate_not_in_present_enumeration"])
        self.assertEqual(self.result["diagonal_candidate"]["name"], "Diag(Enum_n)")

    def test_diagonal_separation_and_witness_are_recorded(self) -> None:
        self.assertTrue(self.comparisons["all_checked_values_separate"])
        self.assertTrue(self.comparisons["symbolic_for_all_k_separation_recorded"])
        self.assertTrue(self.comparisons["witness_formed"])
        self.assertEqual(self.result["witness"]["proposition"], "Adm_n(Diag(Enum_n))")

    def test_successor_and_source_trace_are_recorded(self) -> None:
        self.assertTrue(self.comparisons["successor_issued"])
        self.assertTrue(self.comparisons["trace_recorded"])
        self.assertEqual(self.result["source_trace"]["trace_id"], "tau_diag")
        self.assertEqual(self.result["source_trace"]["target_context"], "Gamma_n_plus_1")

    def test_hidden_oracle_is_rejected_internally_but_external_absorber_remains(self) -> None:
        self.assertTrue(self.comparisons["internal_future_oracle_rejected"])
        self.assertTrue(self.comparisons["external_platonist_absorber_still_available"])
        self.assertTrue(self.comparisons["fixed_oracle_invalid_internally_valid_externally"])

    def test_comparator_and_verdict_scope(self) -> None:
        self.assertTrue(self.comparisons["finite_type_context_absorbed"])
        self.assertTrue(self.comparisons["computable_context_absorbed"])
        self.assertTrue(self.comparisons["local_constructive_witness_passes"])
        self.assertFalse(self.comparisons["physical_source_issuance_established"])
        self.assertTrue(self.effect_typing["Issue[S]^LC"])
        self.assertFalse(self.effect_typing["Issue[S]^physical"])
        self.assertFalse(self.comparisons["full_theorem_prover_verification"])
        self.assertEqual(self.result["verdict"]["claim_status_change"], "none")


if __name__ == "__main__":
    unittest.main()
