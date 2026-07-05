#!/usr/bin/env python3
"""Tests for tools/generated_uv_d_fork_resurrection_fixture.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import generated_uv_d_fork_resurrection_fixture as fixture  # noqa: E402


class GeneratedUVDForkResurrectionFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture_suite()
        self.by_id = {
            candidate["candidate_id"]: candidate
            for candidate in self.result["candidate_results"]
        }

    def test_fixed_cutoff_is_absorbed_by_completion_access(self) -> None:
        fixed = self.by_id["fixed_uv_cutoff_disclosure"]
        self.assertEqual(fixed["verdict"], "ABSORBED_FIXED_COMPLETION_ACCESS")
        self.assertFalse(fixed["new_mode_not_formable_at_stage_n"])
        self.assertTrue(fixed["factors_through_fixed_completion_access_decoherence"])
        self.assertTrue(fixed["fixed_decoherence_law"])

    def test_dynamical_diagonal_has_prefix_freshness(self) -> None:
        diagonal = self.by_id["dynamical_diagonal_uv_modes"]
        self.assertTrue(diagonal["new_mode_not_formable_at_stage_n"])
        self.assertFalse(diagonal["factors_through_fixed_completion_access_decoherence"])
        self.assertEqual(
            diagonal["verdict"],
            "CLASS_RELATIVE_ONLY_SINGLETON_ABSORBED",
        )

    def test_singleton_enumerator_blocks_physical_reopen(self) -> None:
        self.assertTrue(self.result["whole_family_singleton_absorbs_dynamical_candidate"])
        self.assertFalse(self.result["new_physical_surplus_over_formal_residue"])
        self.assertFalse(self.result["Issue[S]^physical"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_imported_law_change_is_rejected_as_absorber(self) -> None:
        imported = self.by_id["imported_dynamical_law_change"]
        self.assertEqual(imported["verdict"], "REJECTED_AS_IMPORTED_STRUCTURE")
        self.assertTrue(imported["hidden_global_mode_table"])
        self.assertTrue(imported["imported_law_change"])

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
