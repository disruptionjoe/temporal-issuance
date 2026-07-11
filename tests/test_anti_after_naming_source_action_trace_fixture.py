#!/usr/bin/env python3
"""Tests for tools/anti_after_naming_source_action_trace_fixture.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import anti_after_naming_source_action_trace_fixture as fixture  # noqa: E402


class AntiAfterNamingSourceActionTraceFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.by_id = {trace["trace_id"]: trace for trace in self.result["traces"]}

    def test_diagonal_successor_is_not_in_stage_names(self) -> None:
        names = ("alpha", "beta")
        successor = fixture.diagonal_successor(names)

        self.assertNotIn(successor, names)
        self.assertEqual(successor, "diag__alpha__beta")

    def test_readout_fixed_and_imported_controls_reject(self) -> None:
        self.assertEqual(
            self.by_id["e161_readout_sector"]["verdict"],
            fixture.TAF_EXPRESSIBLE_READOUT,
        )
        self.assertEqual(
            self.by_id["fixed_source_access_trace"]["verdict"],
            fixture.FIXED_SOURCE_DISCLOSURE,
        )
        self.assertEqual(
            self.by_id["imported_oracle_novel_name"]["verdict"],
            fixture.IMPORTED_STRUCTURE_REJECTION,
        )

    def test_unguarded_diagonal_is_singleton_absorbed(self) -> None:
        unguarded = self.by_id["unguarded_diagonal_singleton_absorbed"]

        self.assertEqual(unguarded["verdict"], fixture.SINGLETON_AFTER_NAMING_ABSORBED)
        self.assertTrue(unguarded["after_fact_singleton_absorbs"])
        self.assertTrue(unguarded["internal_diagonal_witness"])
        self.assertFalse(unguarded["source_action_trace_candidate"])

    def test_stage_stratified_diagonal_instantiates_positive_shape(self) -> None:
        positive = self.by_id["stage_stratified_diagonal_trace"]

        self.assertEqual(
            positive["verdict"],
            fixture.CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS,
        )
        self.assertTrue(positive["internal_diagonal_witness"])
        self.assertFalse(positive["prior_name_absorbs"])
        self.assertFalse(positive["after_fact_singleton_absorbs"])
        self.assertTrue(positive["source_action_trace_candidate"])
        self.assertTrue(self.result["e161_positive_shape_instantiated"])
        self.assertTrue(self.result["concrete_formal_source_action_trace_found"])
        self.assertFalse(self.result["physical_source_action_found"])

    def test_verbal_guard_and_inconsistent_transport_do_not_pass(self) -> None:
        verbal = self.by_id["verbal_guard_no_trace"]
        inconsistent = self.by_id["inconsistent_transport_trace"]

        self.assertEqual(verbal["verdict"], fixture.SCHEMATIC_ONLY_NOT_INSTANTIATED)
        self.assertEqual(
            inconsistent["verdict"], fixture.BLOCKED_INCONSISTENT_TRANSPORT
        )
        self.assertFalse(verbal["source_action_trace_candidate"])
        self.assertFalse(inconsistent["source_action_trace_candidate"])

    def test_fixture_records_next_adapter_pressure_without_claim_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(
            self.result["active_trigger_change"], "recommend_full_adapter_p_pressure"
        )
        self.assertEqual(
            self.result["next_trigger_recommendation"],
            "full_adapter_p_pressure_on_stage_stratified_diagonal_trace",
        )

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
