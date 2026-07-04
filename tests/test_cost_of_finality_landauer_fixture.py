#!/usr/bin/env python3
"""Tests for tools/cost_of_finality_landauer_fixture.py (RUN-0125 energy-bridge swing)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import cost_of_finality_landauer_fixture as fixture  # noqa: E402


class CostOfFinalityLandauerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = fixture.run_fixture()

    def test_flow_cost_is_pure_single_bit_landauer(self) -> None:
        flow = self.result["flow_cost"]
        self.assertTrue(flow["equals_single_bit_landauer"])
        self.assertEqual(flow["surplus_over_landauer"], 0.0)
        self.assertTrue(flow["absorbed"])

    def test_stock_limit_is_bekenstein(self) -> None:
        stock = self.result["stock_limit"]
        self.assertTrue(stock["absorbed"])
        self.assertFalse(stock["issuance_specific_content"])

    def test_adversarial_thermal_reduces_to_thermodynamics(self) -> None:
        adver = self.result["adversarial_sizing"]
        self.assertTrue(adver["thermal_adversary"]["depends_only_on_thermodynamics"])
        self.assertTrue(adver["thermal_adversary"]["absorbed"])

    def test_adversarial_agent_needs_imported_agency_no_physical_surplus(self) -> None:
        agent = self.result["adversarial_sizing"]["agent_adversary"]
        self.assertTrue(agent["requires_imported_agency"])
        self.assertTrue(agent["collapses_to_thermal_when_agent_stripped"])
        self.assertFalse(agent["free_params_are_thermodynamic_constants"])
        self.assertFalse(agent["physical_surplus_without_agency"])

    def test_overall_verdict_energy_bridge_absorbed_no_claim_movement(self) -> None:
        v = self.result["verdict"]
        # The energy coupling that exists is the trivial thermodynamic-of-computation one.
        self.assertTrue(v["energy_coupling_exists_but_trivial_thermodynamic"])
        # No NEW non-absorbed physical bridge is produced.
        self.assertFalse(v["new_nonabsorbed_physical_energy_bridge"])
        self.assertTrue(v["energy_bridge_route_closed_on_tested_routes"])
        # The only surviving surplus is agent-relational -> reconstruction layer, not physics.
        self.assertIn("reconstruction_layer", v["surviving_residue_location"])
        # Archives are NOT un-archived as physics; no claim movement.
        self.assertFalse(v["TI_C009_reopened_as_physics"])
        self.assertFalse(v["TI_C010_reopened_as_physics"])
        self.assertEqual(v["claim_status_change"], "none")

    def test_controls(self) -> None:
        ctrl = self.result["controls"]
        self.assertTrue(ctrl["pure_landauer_absorbed"])
        self.assertTrue(ctrl["fundamental_law_claim_flagged_agent_dependent"])
        self.assertFalse(ctrl["new_physical_term_found"])


if __name__ == "__main__":
    unittest.main()
