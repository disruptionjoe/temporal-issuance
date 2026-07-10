#!/usr/bin/env python3
"""Tests for tools/functor_obl_001_n_naturality.py (FUNCTOR-OBL-001)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import functor_obl_001_n_naturality as fixture  # noqa: E402


class NNaturalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()

    def test_strict_naturality_fails(self) -> None:
        strict = self.result["strict_naturality"]
        self.assertFalse(strict["holds"])
        # The D4 predicate flips along the morphism: novel at S, non-novel at S'.
        self.assertTrue(strict["beta_move_is_d4_at_S"])
        self.assertFalse(strict["beta_move_is_d4_at_S_prime"])
        self.assertFalse(strict["d4_predicate_preserved_along_morphism"])
        self.assertFalse(strict["transport_law_well_defined"])

    def test_gauge_naturality_holds(self) -> None:
        gauge = self.result["gauge_naturality"]
        self.assertTrue(gauge["holds"])
        self.assertAlmostEqual(gauge["N_at_S"], gauge["N_at_relabeled_S"], places=12)

    def test_obligation_discharged_without_claim_movement(self) -> None:
        self.assertTrue(self.result["obligation_discharged"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertEqual(
            self.result["resolution"],
            "negative_for_strict_naturality_positive_for_gauge_naturality",
        )

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            fixture.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
