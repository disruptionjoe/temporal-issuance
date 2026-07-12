#!/usr/bin/env python3
"""Tests for tools/completion_aware_adapter_p_admission_contract.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import completion_aware_adapter_p_admission_contract as h7  # noqa: E402


class CompletionAwareAdapterPAdmissionContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = h7.run_admission_contract()
        self.by_id = {
            decision["packet_id"]: decision for decision in self.result["decisions"]
        }

    def test_h1_h2_floor_is_preserved(self) -> None:
        self.assertTrue(self.result["h1_h2_floor_satisfied"])
        self.assertEqual(
            self.result["h1_h2_floor"]["h1_result"],
            "narrowed_to_executable_classifier_and_preaction_family_noncompletion_target",
        )
        self.assertEqual(
            self.result["h1_h2_floor"]["h2_result"],
            "bounded_osag_shape_constructed_formal_local",
        )

    def test_boundary_osag_support_is_admitted_formal_local_only(self) -> None:
        admitted = self.by_id["boundary_osag_support"]

        self.assertEqual(admitted["verdict"], h7.ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT)
        self.assertTrue(admitted["admitted"])
        self.assertFalse(admitted["terminal"])
        self.assertEqual(admitted["missing_requirements"], [])
        self.assertEqual(self.result["admitted_packet_ids"], ["boundary_osag_support"])

    def test_imported_completion_and_readout_are_rejected(self) -> None:
        self.assertEqual(
            self.by_id["neighbor_completion_table"]["verdict"],
            h7.IMPORTED_COMPLETION_REJECTION,
        )
        self.assertEqual(
            self.by_id["cross_repo_readout_language"]["verdict"],
            h7.READOUT_ONLY_REJECTION,
        )

    def test_missing_preservation_and_provenance_are_rejected(self) -> None:
        missing = self.by_id["boundary_missing_preserve_n"]
        shortcut = self.by_id["physical_source_claim_shortcut"]

        self.assertEqual(missing["verdict"], h7.MISSING_PRESERVATION_REJECTION)
        self.assertIn("Preserve_n", missing["missing_requirements"])
        self.assertEqual(shortcut["verdict"], h7.IMPORTED_COMPLETION_REJECTION)
        self.assertIn("candidate_provenance", shortcut["missing_requirements"])
        self.assertIn("no_claim_status_movement", shortcut["missing_requirements"])

    def test_no_claim_or_physical_source_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            h7.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
