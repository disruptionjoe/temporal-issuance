#!/usr/bin/env python3
"""Tests for tools/n_concavity_regime_discriminator.py (E031 II.1 conditional)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import n_concavity_regime_discriminator as fixture  # noqa: E402


class NConcavityRegimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()

    def test_fts_regime_is_concave_and_depletes(self) -> None:
        fts = self.result["fts_regime"]
        self.assertTrue(fts["all_concave"])
        self.assertTrue(fts["declines"])
        self.assertTrue(self.result["fts_shows_concave_depleting_signature"])

    def test_godelian_regime_is_sustained(self) -> None:
        god = self.result["godelian_regime"]
        self.assertTrue(god["sustained"])
        self.assertFalse(god["declines"])
        self.assertTrue(self.result["godelian_shows_sustained_non_depleting_signature"])

    def test_curvature_separates_regimes(self) -> None:
        self.assertTrue(self.result["curvature_separates_regimes"])

    def test_honest_scope_not_a_decision_procedure(self) -> None:
        self.assertIn("not_a_decision_procedure", self.result["kind"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
