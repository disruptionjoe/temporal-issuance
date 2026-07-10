#!/usr/bin/env python3
"""Tests for tools/holonomy_transport_functor_derivation_fixture.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import holonomy_transport_functor_derivation_fixture as fixture  # noqa: E402


class HolonomyTransportFunctorDerivationFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()
        self.by_id = {case["case_id"]: case for case in self.result["cases"]}

    def test_bare_loop_does_not_derive_transport(self) -> None:
        bare = self.by_id["bare_loop_word"]
        self.assertEqual(bare["verdict"], fixture.NOT_DERIVABLE_BARE_LOOP)
        self.assertFalse(bare["derived_transport"])
        self.assertIsNone(bare["loop_holonomy_z2"])
        self.assertFalse(self.result["bare_loop_derives_transport"])

    def test_identity_forced_consistency_is_trivial_only(self) -> None:
        identity = self.by_id["identity_forced_consistency"]
        self.assertEqual(identity["verdict"], fixture.TRIVIAL_TRANSPORT_ONLY)
        self.assertTrue(identity["derived_transport"])
        self.assertEqual(identity["loop_holonomy_z2"], 0)
        self.assertFalse(identity["nontrivial_loop_holonomy"])

    def test_c_typed_parity_rule_derives_nontrivial_toy_transport(self) -> None:
        parity = self.by_id["c_typed_parity_rule"]
        self.assertEqual(parity["verdict"], fixture.DERIVED_NONTRIVIAL_TRANSPORT)
        self.assertTrue(parity["derived_transport"])
        self.assertTrue(parity["nontrivial_loop_holonomy"])
        self.assertFalse(parity["imported_transport_used"])
        self.assertTrue(self.result["source_rule_positive_shape_found"])

    def test_imported_table_is_rejected_as_derivation(self) -> None:
        imported = self.by_id["imported_transport_table"]
        self.assertEqual(imported["verdict"], fixture.IMPORTED_TRANSPORT_REJECTION)
        self.assertFalse(imported["derived_transport"])
        self.assertTrue(imported["imported_transport_used"])
        self.assertFalse(self.result["imported_table_counts_as_derivation"])

    def test_inconsistent_c_labels_are_blocked(self) -> None:
        inconsistent = self.by_id["inconsistent_c_typed_labels"]
        self.assertEqual(
            inconsistent["verdict"], fixture.BLOCKED_INCONSISTENT_TRANSPORT
        )
        self.assertFalse(inconsistent["derived_transport"])
        self.assertIn("expects 0, got 1", inconsistent["reason"])

    def test_fixture_does_not_move_claim_or_trigger_state(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(self.result["active_trigger_change"], "none")
        self.assertIn(fixture.NOT_DERIVABLE_BARE_LOOP, self.result["verdicts_seen"])
        self.assertIn(
            fixture.DERIVED_NONTRIVIAL_TRANSPORT,
            self.result["verdicts_seen"],
        )

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
