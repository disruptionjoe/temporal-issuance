#!/usr/bin/env python3
"""Tests for tools/h9_physical_calibration_batch.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import h9_physical_calibration_batch as h9  # noqa: E402


class H9PhysicalCalibrationBatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = h9.run_calibration()
        self.by_id = {
            result["case_id"]: result for result in self.result["results"]
        }

    def test_crispr_near_miss_is_fixed_sequence_absorbed(self) -> None:
        case = self.by_id["crispr_spacer_acquisition_near_miss"]

        self.assertEqual(case["final_verdict"], h9.CRISPR_FIXED_SEQUENCE_SPACE_ABSORBED)
        self.assertTrue(case["terminal"])
        self.assertFalse(case["h7_admitted"])
        self.assertFalse(case["physical_adapter_p_passed"])

    def test_floquet_negative_control_is_fixed_platform_absorbed(self) -> None:
        case = self.by_id["dynamic_floquet_code_negative_control"]

        self.assertEqual(
            case["final_verdict"],
            h9.FLOQUET_FIXED_PLATFORM_SCHEDULE_ABSORBED,
        )
        self.assertTrue(case["terminal"])
        self.assertFalse(case["h7_admitted"])
        self.assertFalse(case["physical_adapter_p_passed"])

    def test_h7_formal_support_control_stays_formal_local(self) -> None:
        case = self.by_id["h7_boundary_osag_support_control"]

        self.assertEqual(
            case["final_verdict"],
            h9.H7_ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT,
        )
        self.assertFalse(case["terminal"])
        self.assertTrue(case["h7_admitted"])
        self.assertFalse(case["physical_adapter_p_passed"])

    def test_differential_routes_agree_and_no_claim_movement(self) -> None:
        self.assertTrue(self.result["h7_floor_satisfied"])
        self.assertTrue(self.result["physical_near_misses_absorbed"])
        self.assertTrue(self.result["differential_routes_agree"])
        self.assertEqual(self.result["physical_adapter_p_passed_case_ids"], [])
        self.assertEqual(
            self.result["h7_admitted_case_ids"],
            ["h7_boundary_osag_support_control"],
        )
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            h9.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
