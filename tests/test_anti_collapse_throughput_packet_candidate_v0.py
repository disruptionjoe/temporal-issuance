#!/usr/bin/env python3
"""Focused tests for anti-collapse throughput packet candidate v0."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import anti_collapse_throughput_packet_candidate_v0 as packet  # noqa: E402
import completion_class_v1 as cc  # noqa: E402


class AntiCollapseThroughputPacketCandidateV0Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = packet.run_packet()

    def test_candidate_fails_closed_not_admitted(self) -> None:
        self.assertEqual(
            self.result["packet_status"], packet.PACKET_STATUS
        )
        self.assertFalse(self.result["packet_admitted"])
        self.assertFalse(self.result["typed_action_2_packet"])
        self.assertFalse(self.result["native_source_law_supplied"])

    def test_all_completion_families_are_represented_and_unresolved(self) -> None:
        assessments = self.result["completion_family_assessments"]
        self.assertEqual(len(assessments), 11)
        self.assertEqual(
            {row["family_id"] for row in assessments},
            set(cc.PRIMITIVE_FAMILY_IDS),
        )
        self.assertTrue(all(row["represented"] for row in assessments))
        self.assertEqual(
            set(self.result["unresolved_family_ids"]),
            set(cc.PRIMITIVE_FAMILY_IDS),
        )
        self.assertEqual(self.result["missing_family_ids"], [])

    def test_completion_class_v1_fails_closed(self) -> None:
        self.assertEqual(
            self.result["completion_class_verdict"],
            cc.INCOMPLETE_NULL_CLASS,
        )
        self.assertFalse(self.result["composition_closure_declared"])

    def test_required_source_fields_block_admission(self) -> None:
        source_fields = self.result["required_source_fields"]
        self.assertTrue(source_fields)
        self.assertTrue(
            all(not row["supplied"] and row["blocks_admission"] for row in source_fields)
        )
        self.assertIn(
            "native_source_law",
            self.result["blocking_missing_fields"],
        )
        self.assertIn("adapter_p", self.result["blocking_missing_fields"])
        self.assertIn("w1_w4_w5", self.result["blocking_missing_fields"])

    def test_counting_residual_is_not_source_evidence(self) -> None:
        residual = self.result["residual_assessment"]
        self.assertEqual(residual["candidate_shape"], "1/sqrt(N)")
        self.assertEqual(
            residual["residual_location"], "observer_counting_artifact"
        )
        self.assertFalse(residual["source_residual_established"])
        self.assertTrue(residual["observer_counting_artifact_established"])

    def test_sign_correction_preserves_killed_reading(self) -> None:
        sign = self.result["sign_correction"]
        self.assertEqual(sign["gu_krein_sign_reading"], "forced_internal")
        self.assertFalse(sign["out_of_band_sign_reading_allowed"])
        self.assertFalse(sign["used_as_undecidability_evidence"])
        self.assertFalse(sign["used_as_external_observer_evidence"])

    def test_protected_surfaces_do_not_move(self) -> None:
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertFalse(self.result["E177_modified"])
        self.assertFalse(self.result["cross_repo_implication"])

    def test_runner_writes_byte_stable_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            packet.write_json(self.result, first)
            packet.write_json(packet.run_packet(), second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(
                json.loads(first.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
