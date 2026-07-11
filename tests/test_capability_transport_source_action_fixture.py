#!/usr/bin/env python3
"""Tests for tools/capability_transport_source_action_fixture.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import capability_transport_source_action_fixture as fixture  # noqa: E402


class CapabilityTransportSourceActionFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.by_id = {case["case_id"]: case for case in self.result["cases"]}

    def test_bare_and_identity_cases_have_no_capability_delta(self) -> None:
        bare = self.by_id["bare_loop_no_transport"]
        identity = self.by_id["identity_transport_trivial_capability"]

        self.assertEqual(bare["verdict"], fixture.NO_CAPABILITY_DELTA)
        self.assertEqual(identity["verdict"], fixture.NO_CAPABILITY_DELTA)
        self.assertFalse(bare["capability_delta"])
        self.assertFalse(identity["capability_delta"])

    def test_e160_parity_transport_is_taf_expressible_readout(self) -> None:
        parity = self.by_id["c_typed_parity_sector_readout"]

        self.assertEqual(parity["verdict"], fixture.TAF_EXPRESSIBLE_READOUT)
        self.assertTrue(parity["derived_from_c"])
        self.assertTrue(parity["nontrivial_transport"])
        self.assertEqual(parity["capability_delta"], ["distinguish_loop_sector"])
        self.assertFalse(parity["source_action_candidate"])
        self.assertTrue(self.result["e160_transport_has_capability_delta"])
        self.assertFalse(self.result["e160_transport_becomes_source_action"])

    def test_fixed_access_and_imported_transport_are_rejected(self) -> None:
        fixed = self.by_id["fixed_access_reveals_sector"]
        imported = self.by_id["imported_transport_sector_task"]

        self.assertEqual(fixed["verdict"], fixture.FIXED_SOURCE_DISCLOSURE)
        self.assertEqual(imported["verdict"], fixture.IMPORTED_STRUCTURE_REJECTION)
        self.assertTrue(fixed["terminal"])
        self.assertTrue(imported["terminal"])

    def test_singleton_absorbed_prefix_family_is_formal_residue(self) -> None:
        prefix = self.by_id["c_typed_prefix_family_singleton_absorbed"]

        self.assertEqual(prefix["verdict"], fixture.CLASS_RELATIVE_FORMAL_RESIDUE)
        self.assertTrue(prefix["capability_delta"])
        self.assertFalse(prefix["source_action_candidate"])

    def test_positive_source_action_shape_is_stateable_but_not_found(self) -> None:
        positive = self.by_id["anti_after_naming_source_action_shape"]

        self.assertEqual(
            positive["verdict"],
            fixture.SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P,
        )
        self.assertTrue(positive["source_action_candidate"])
        self.assertFalse(positive["terminal"])
        self.assertTrue(self.result["positive_source_action_shape_stateable"])
        self.assertFalse(self.result["real_source_action_found"])

    def test_inconsistent_transport_is_blocked(self) -> None:
        inconsistent = self.by_id["inconsistent_c_transport_labels"]

        self.assertEqual(
            inconsistent["verdict"], fixture.BLOCKED_INCONSISTENT_TRANSPORT
        )
        self.assertFalse(inconsistent["source_action_candidate"])

    def test_fixture_does_not_move_claim_or_trigger_state(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(self.result["active_trigger_change"], "none")
        self.assertIn(fixture.TAF_EXPRESSIBLE_READOUT, self.result["verdicts_seen"])
        self.assertIn(
            fixture.SOURCE_ACTION_CANDIDATE_REQUIRES_FULL_ADAPTER_P,
            self.result["verdicts_seen"],
        )

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
