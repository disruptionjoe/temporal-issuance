#!/usr/bin/env python3
"""Focused tests for emergent gauge sector candidate v0."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import completion_class_v1 as cc  # noqa: E402
import emergent_gauge_sector_candidate_v0 as candidate  # noqa: E402


class EmergentGaugeSectorCandidateV0Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = candidate.run_candidate()
        self.gates = {
            row["gate_id"]: row for row in self.result["witness_gates"]
        }

    def test_candidate_is_killed_by_fixed_platform_completion(self) -> None:
        self.assertEqual(
            self.result["candidate_status"], candidate.CANDIDATE_STATUS
        )
        self.assertFalse(self.result["packet_admitted"])
        self.assertFalse(self.result["typed_action_2_packet"])
        self.assertFalse(self.result["native_source_law_supplied"])

    def test_effective_algebra_signal_is_not_source_growth(self) -> None:
        self.assertTrue(self.result["effective_algebra_signal_present"])
        self.assertTrue(self.gates["W1_non_isomorphic_algebra"]["effective_signal"])
        self.assertFalse(self.gates["W1_non_isomorphic_algebra"]["source_passed"])
        self.assertFalse(self.result["source_growth_core_passed"])

    def test_w4_and_w6_absorber_controls_fail_while_w5_survives(self) -> None:
        self.assertFalse(
            self.gates["W4_perturbation_non_factorization"]["source_passed"]
        )
        self.assertTrue(self.gates["W5_record_preservation"]["source_passed"])
        self.assertFalse(
            self.gates["W6_gauge_access_language_absorption"]["source_passed"]
        )
        self.assertFalse(self.result["absorber_controls_passed"])

    def test_completion_class_records_physical_predictive_absorption(self) -> None:
        self.assertEqual(
            self.result["completion_class_verdict"],
            cc.PHYSICAL_PREDICTIVE_ABSORPTION,
        )
        self.assertEqual(
            self.result["valid_completion_witness_ids"],
            [candidate.COMPLETION_WITNESS_ID],
        )
        self.assertEqual(self.result["unresolved_family_ids"], [])
        self.assertEqual(self.result["missing_family_ids"], [])

    def test_fixed_source_rival_preserves_trace_without_new_source_algebra(self) -> None:
        rival = self.result["fixed_source_rival"]
        self.assertTrue(rival["fixed_microscopic_platform"])
        self.assertTrue(rival["fixed_control_or_measurement_schedule"])
        self.assertTrue(rival["fixed_low_energy_or_effective_projection"])
        self.assertTrue(rival["record_trace_preserved"])
        self.assertTrue(rival["reproduces_candidate_shape"])
        self.assertFalse(rival["source_owned_new_algebra"])

    def test_missing_source_object_names_resurrection_burden(self) -> None:
        missing = self.result["exact_missing_source_object"]
        self.assertEqual(
            missing["missing_object_id"], "source_owned_non_isomorphic_gauge_algebra"
        )
        self.assertIn("native source law", missing["required"])
        self.assertIn("anti-after-naming", missing["also_required"])

    def test_protected_surfaces_do_not_move(self) -> None:
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["E177_modified"])
        self.assertFalse(self.result["cross_repo_implication"])

    def test_runner_writes_byte_stable_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            candidate.write_json(self.result, first)
            candidate.write_json(candidate.run_candidate(), second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(
                json.loads(first.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
