#!/usr/bin/env python3
"""Tests for tools/h6_completion_boundary_audit.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import h6_completion_boundary_audit as h6  # noqa: E402


class H6CompletionBoundaryAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = h6.run_boundary_audit()
        self.by_id = {
            decision["case_id"]: decision for decision in self.result["decisions"]
        }

    def test_formal_osag_support_is_bounded_conditional(self) -> None:
        case = self.by_id["formal_local_osag_support"]

        self.assertEqual(
            case["boundary_verdict"],
            h6.BOUNDED_INTERNAL_OSAG_CONDITIONAL,
        )
        self.assertEqual(case["boundary_class"], "bounded_conditional_form")
        self.assertFalse(case["terminal"])
        self.assertTrue(case["h7_admitted"])
        self.assertFalse(case["physical_adapter_p_passed"])

    def test_external_completion_readout_and_physical_near_misses_are_terminal(self) -> None:
        self.assertEqual(
            self.by_id["neighbor_completion_table"]["boundary_verdict"],
            h6.EXTERNAL_COMPLETION_LANGUAGE,
        )
        self.assertEqual(
            self.by_id["cross_repo_readout_language"]["boundary_verdict"],
            h6.READOUT_FINALITY_COMPLETION,
        )
        self.assertEqual(
            self.by_id["split_holder_reversal_cost"]["boundary_verdict"],
            h6.READOUT_FINALITY_COMPLETION,
        )
        self.assertEqual(
            self.by_id["crispr_spacer_acquisition_near_miss"]["boundary_verdict"],
            h6.PHYSICAL_NEAR_MISS_ABSORBED,
        )
        self.assertEqual(
            self.by_id["dynamic_floquet_code_negative_control"]["boundary_verdict"],
            h6.PHYSICAL_NEAR_MISS_ABSORBED,
        )

        for case_id, case in self.by_id.items():
            if case_id != "formal_local_osag_support":
                self.assertTrue(case["terminal"])

    def test_boundary_is_set_without_claim_movement(self) -> None:
        self.assertTrue(self.result["completion_boundary_set"])
        self.assertEqual(
            self.result["formal_local_support_boundary"],
            "bounded_conditional_form",
        )
        self.assertFalse(
            self.result["formal_local_support_is_external_completion_language"]
        )
        self.assertFalse(self.result["formal_local_support_is_full_internal_source_structure"])
        self.assertTrue(self.result["bounded_internal_support_conditional"])
        self.assertEqual(self.result["physical_adapter_p_passed_case_ids"], [])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            h6.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
