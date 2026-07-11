#!/usr/bin/env python3
"""Tests for tools/full_adapter_p_diagonal_trace_pressure.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import full_adapter_p_diagonal_trace_pressure as pressure  # noqa: E402


class FullAdapterPDiagonalTracePressureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = pressure.run_pressure()
        self.by_id = {
            result["case_id"]: result for result in self.result["results"]
        }

    def test_stage_trace_maps_adapter_fields_and_local_controls(self) -> None:
        stage = self.by_id["stage_stratified_diagonal_trace_full_pressure"]

        self.assertEqual(stage["verdict"], pressure.FORMAL_LOCAL_ADAPTER_SHAPE_SURVIVES)
        self.assertTrue(stage["all_adapter_fields_mapped"])
        self.assertTrue(stage["source_growth_core_supplied"])
        self.assertTrue(stage["local_controls_defeated"])
        self.assertFalse(stage["physical_adapter_p_passed"])
        self.assertTrue(self.result["formal_local_adapter_shape_survives"])

    def test_standard_controls_reject(self) -> None:
        self.assertEqual(
            self.by_id["taf_readout_control"]["verdict"],
            pressure.TAF_EXPRESSIBLE_READOUT,
        )
        self.assertEqual(
            self.by_id["fixed_source_access_control"]["verdict"],
            pressure.FIXED_SOURCE_DISCLOSURE,
        )
        self.assertEqual(
            self.by_id["imported_oracle_control"]["verdict"],
            pressure.IMPORTED_STRUCTURE_REJECTION,
        )
        self.assertEqual(
            self.by_id["unguarded_after_fact_singleton_control"]["verdict"],
            pressure.SINGLETON_AFTER_NAMING_ABSORBED,
        )

    def test_whole_family_completion_still_absorbs_physical_reading(self) -> None:
        whole_family = self.by_id["whole_family_completion_control"]

        self.assertEqual(
            whole_family["verdict"],
            pressure.WHOLE_FAMILY_COMPLETION_ABSORPTION,
        )
        self.assertFalse(whole_family["whole_family_completion_defeated"])
        self.assertFalse(whole_family["physical_adapter_p_passed"])
        self.assertTrue(self.result["whole_family_completion_control_absorbs"])

    def test_physical_adapter_p_remains_unpassed(self) -> None:
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(
            self.result["next_trigger_recommendation"],
            "compact_no_worthy_work_until_real_physical_candidate_or_sharper_theorem_target",
        )
        self.assertFalse(
            self.result["stage_trace_supplies_physical_absorber_controls"]
        )
        self.assertFalse(self.result["stage_trace_defeats_whole_family_completion"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            pressure.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
