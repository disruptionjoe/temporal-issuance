#!/usr/bin/env python3
"""Tests for tools/adapter_p_no_go_preflight.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import adapter_p_no_go_preflight as preflight  # noqa: E402


class AdapterPNoGoPreflightTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = preflight.run_preflight()
        self.by_id = {
            classification["candidate_id"]: classification
            for classification in self.result["classifications"]
        }

    def test_all_three_terminal_classes_are_exercised(self) -> None:
        self.assertTrue(self.result["all_terminal_classes_exercised"])
        self.assertEqual(
            set(self.result["terminal_classes_seen"]),
            {
                preflight.FIXED_SOURCE_DISCLOSURE,
                preflight.CLASS_RELATIVE_FORMAL_RESIDUE,
                preflight.IMPORTED_STRUCTURE_REJECTION,
            },
        )

    def test_fixed_completion_access_is_disclosure(self) -> None:
        fixed = self.by_id["fixed_completion_access_trace"]
        self.assertEqual(fixed["terminal_class"], preflight.FIXED_SOURCE_DISCLOSURE)
        self.assertTrue(fixed["terminal"])

    def test_generated_uv_shape_is_class_relative_residue(self) -> None:
        generated = self.by_id["generated_uv_singleton_absorbed"]
        self.assertEqual(
            generated["terminal_class"],
            preflight.CLASS_RELATIVE_FORMAL_RESIDUE,
        )
        self.assertTrue(generated["terminal"])

    def test_imported_boundary_structure_is_rejected(self) -> None:
        imported = self.by_id["imported_boundary_category"]
        self.assertEqual(
            imported["terminal_class"],
            preflight.IMPORTED_STRUCTURE_REJECTION,
        )
        self.assertTrue(imported["terminal"])

    def test_boundary_polarity_cases_are_separated(self) -> None:
        taf = self.by_id["taf_denied_readout_only"]
        gu = self.by_id["gu_boundary_supply_without_ti_map"]
        positive_shape = self.by_id["anti_after_naming_positive_shape"]

        self.assertEqual(taf["terminal_class"], preflight.FIXED_SOURCE_DISCLOSURE)
        self.assertEqual(gu["terminal_class"], preflight.IMPORTED_STRUCTURE_REJECTION)
        self.assertEqual(
            positive_shape["terminal_class"],
            preflight.POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE,
        )
        self.assertTrue(self.result["boundary_polarity_separated"])

    def test_preflight_does_not_reopen_physical_claims(self) -> None:
        self.assertFalse(self.result["real_counterexample_found"])
        self.assertFalse(self.result["theorem_ready"])
        self.assertFalse(self.result["lean_target_ready"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            preflight.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
