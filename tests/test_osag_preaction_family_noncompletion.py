#!/usr/bin/env python3
"""Tests for tools/osag_preaction_family_noncompletion.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import osag_preaction_family_noncompletion as osag  # noqa: E402


class OSAGPreactionFamilyNoncompletionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = osag.run_constructor()
        self.by_id = {
            result["case_id"]: result for result in self.result["results"]
        }

    def test_bounded_internal_osag_constructs_formal_local_shape(self) -> None:
        constructed = self.by_id["bounded_internal_osag"]

        self.assertEqual(constructed["verdict"], osag.BOUNDED_OSAG_CONSTRUCTED)
        self.assertFalse(constructed["terminal"])
        self.assertTrue(constructed["adapter_fields_mapped"])
        self.assertTrue(constructed["tau_n_preserved"])
        self.assertTrue(constructed["preaction_family_rule"])
        self.assertTrue(constructed["internally_generated"])
        self.assertTrue(constructed["family_noncompletion_holds"])
        self.assertTrue(constructed["finite_prefix_non_precontained"])
        self.assertTrue(constructed["source_growth_witness"])
        self.assertFalse(constructed["real_physical_candidate"])
        self.assertTrue(self.result["bounded_osag_constructed"])

    def test_completion_controls_remain_terminal_absorbers(self) -> None:
        self.assertEqual(
            self.by_id["fixed_value_precompletion"]["verdict"],
            osag.FAMILY_COMPLETION_ABSORPTION,
        )
        self.assertEqual(
            self.by_id["preformed_action_completion"]["verdict"],
            osag.FAMILY_COMPLETION_ABSORPTION,
        )
        self.assertEqual(
            self.by_id["capability_schedule_completion"]["verdict"],
            osag.FAMILY_COMPLETION_ABSORPTION,
        )
        self.assertTrue(self.result["fixed_completion_absorbed"])

    def test_after_fact_and_imported_rules_are_rejected(self) -> None:
        self.assertEqual(
            self.by_id["after_fact_singleton_name"]["verdict"],
            osag.AFTER_FACT_SINGLETON_REJECTION,
        )
        self.assertEqual(
            self.by_id["hidden_completion_oracle"]["verdict"],
            osag.IMPORTED_STRUCTURE_REJECTION,
        )
        self.assertTrue(self.result["after_fact_singleton_rejected"])
        self.assertTrue(self.result["imported_oracle_rejected"])

    def test_missing_preservation_field_is_out_of_scope(self) -> None:
        self.assertEqual(
            self.by_id["missing_preserve_field"]["verdict"],
            osag.OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE,
        )
        self.assertTrue(self.result["adapter_preservation_checked"])

    def test_no_claim_or_physical_source_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            osag.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
