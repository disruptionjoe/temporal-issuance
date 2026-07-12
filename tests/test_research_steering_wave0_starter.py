#!/usr/bin/env python3
"""Tests for tools/research_steering_wave0_starter.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import research_steering_wave0_starter as wave0  # noqa: E402


class ResearchSteeringWave0StarterTests(unittest.TestCase):
    def test_wave0_starter_plan_is_valid(self) -> None:
        result = wave0.validate_lanes()
        self.assertTrue(result["valid"], result["errors"])

    def test_h1_is_blocking_lane(self) -> None:
        result = wave0.validate_lanes()
        self.assertEqual(result["blocking_lane"], "H1")
        self.assertIn("H2", result["dependent_starter_lanes"])

    def test_sidecars_are_contract_prep_only(self) -> None:
        result = wave0.validate_lanes()
        lanes = result["lanes"]
        for lane_id in result["sidecar_lanes"]:
            self.assertIn("prep", lanes[lane_id]["mode"])
            self.assertEqual(lanes[lane_id]["write_scope"], ["explorations/E164"])


if __name__ == "__main__":
    unittest.main()
