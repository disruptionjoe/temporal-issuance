#!/usr/bin/env python3
"""Tests for tools/whole_family_completion_barrier_classifier.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import whole_family_completion_barrier_classifier as barrier  # noqa: E402


class WholeFamilyCompletionBarrierClassifierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = barrier.run_classifier()
        self.by_id = {
            result["candidate_id"]: result for result in self.result["results"]
        }

    def test_four_completion_channels_absorb(self) -> None:
        self.assertEqual(
            self.by_id["value_completed_payload_only"]["verdict"],
            barrier.VALUE_COMPLETION_ABSORPTION,
        )
        self.assertEqual(
            self.by_id["after_fact_family_name"]["verdict"],
            barrier.NAME_COMPLETION_ABSORPTION,
        )
        self.assertEqual(
            self.by_id["preformed_provenance_action"]["verdict"],
            barrier.PROVENANCE_ACTION_COMPLETION_ABSORPTION,
        )
        self.assertEqual(
            self.by_id["precomputed_capability_delta"]["verdict"],
            barrier.CAPABILITY_COMPLETION_ABSORPTION,
        )
        self.assertTrue(self.result["all_completion_channels_exercised"])

    def test_noncompletion_shape_is_only_nonabsorbed_h1_escape(self) -> None:
        escape = self.by_id["preaction_family_noncompletion_shape"]

        self.assertEqual(escape["verdict"], barrier.POTENTIAL_ESCAPE_REQUIRES_OSAG)
        self.assertFalse(escape["terminal"])
        self.assertTrue(escape["preaction_family_noncompletion_rule"])
        self.assertTrue(escape["source_growth_core_witness"])
        self.assertTrue(escape["finite_prefix_non_precontained"])
        self.assertFalse(any(escape["completion_channels"].values()))
        self.assertTrue(
            self.result["preaction_family_noncompletion_required_for_escape"]
        )

    def test_controls_do_not_create_physical_claim(self) -> None:
        self.assertEqual(
            self.by_id["missing_adapter_field"]["verdict"],
            barrier.OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE,
        )
        self.assertEqual(
            self.by_id["taf_finality_readout_only"]["verdict"],
            barrier.TAF_EXPRESSIBLE_READOUT,
        )
        self.assertEqual(
            self.by_id["imported_law_or_oracle"]["verdict"],
            barrier.IMPORTED_STRUCTURE_REJECTION,
        )
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            barrier.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
