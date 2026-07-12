#!/usr/bin/env python3
"""Tests for tools/h5_multi_holder_h7_separator.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import h5_multi_holder_h7_separator as h5  # noqa: E402


class H5MultiHolderH7SeparatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = h5.run_separator()
        self.by_id = {
            result["case_id"]: result for result in self.result["results"]
        }

    def test_h7_gate_is_active_and_has_admitted_packet(self) -> None:
        self.assertTrue(self.result["h7_floor_satisfied"])
        self.assertEqual(self.result["h7_admitted_packet_ids"], ["boundary_osag_support"])

    def test_single_holder_bundle_is_capability_completion(self) -> None:
        case = self.by_id["single_holder_bundle"]

        self.assertEqual(case["verdict"], h5.CAPABILITY_COMPLETION_ABSORPTION)
        self.assertTrue(case["terminal"])
        self.assertTrue(case["measures"]["CanReverse"])
        self.assertTrue(case["measures"]["CanFork"])
        self.assertEqual(case["measures"]["mu_HOLDER"], 0)

    def test_split_holder_cost_is_taf_readout_under_fixed_controls(self) -> None:
        case = self.by_id["multi_holder_split_fixed_source"]

        self.assertEqual(case["verdict"], h5.TAF_EXPRESSIBLE_READOUT)
        self.assertTrue(case["terminal"])
        self.assertFalse(case["measures"]["CanReverse"])
        self.assertFalse(case["measures"]["CanFork"])
        self.assertEqual(case["measures"]["mu_HOLDER"], 1)
        self.assertTrue(self.result["matched_physical_and_thermodynamic_controls"])
        self.assertTrue(self.result["multi_holder_cost_absorbed_as_taf_readout"])

    def test_h7_admitted_osag_support_remains_formal_local(self) -> None:
        case = self.by_id["h7_boundary_osag_holder_support"]

        self.assertEqual(case["verdict"], h5.H7_ADMITTED_FORMAL_LOCAL_SUPPORT)
        self.assertFalse(case["terminal"])
        self.assertTrue(case["h7_admitted"])
        self.assertTrue(case["source_growth_core_witness"])
        self.assertTrue(case["preaction_family_noncompletion_rule"])
        self.assertTrue(self.result["formal_local_osag_support_admitted"])

    def test_readout_shortcut_is_rejected_by_h7(self) -> None:
        case = self.by_id["cross_repo_readout_holder_claim"]

        self.assertEqual(case["verdict"], h5.H7_GATE_REJECTION)
        self.assertTrue(case["terminal"])
        self.assertFalse(case["h7_admitted"])

    def test_no_claim_or_physical_source_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            h5.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
