#!/usr/bin/env python3
"""Tests for tools/compat_comm_extension_confluence.py (Compat-Comm)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import compat_comm_extension_confluence as fixture  # noqa: E402


class CompatCommTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()

    def test_confluent_on_jointly_admissible_pairs(self) -> None:
        self.assertTrue(self.result["confluent_on_jointly_admissible_pairs"])
        for fam in self.result["results"].values():
            self.assertTrue(fam["compatible_pair"]["compat_comm"])
            self.assertTrue(fam["compatible_pair"]["confluent"])

    def test_forking_pairs_have_no_common_successor(self) -> None:
        self.assertTrue(self.result["forking_pairs_have_no_common_successor"])
        self.assertTrue(self.result["results"]["godelian"]["forking_pair"]["forks"])
        self.assertTrue(self.result["results"]["sbp_forking"]["forking_pair"]["forks"])
        # A fork means each single step is admissible but the pair has no common successor.
        god_fork = self.result["results"]["godelian"]["forking_pair"]
        self.assertTrue(god_fork["c1_admissible_from_s"])
        self.assertTrue(god_fork["c2_admissible_from_s"])
        self.assertIsNone(god_fork["common_successor"])

    def test_size_family_never_forks(self) -> None:
        self.assertTrue(self.result["reccost_size_family_never_forks"])

    def test_obligation_discharged_without_claim_movement(self) -> None:
        self.assertTrue(self.result["obligation_discharged"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
