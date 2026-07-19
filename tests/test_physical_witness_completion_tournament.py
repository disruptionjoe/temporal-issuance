#!/usr/bin/env python3
"""Tests for the physical witness completion tournament."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import completion_class_v1 as cc  # noqa: E402
import physical_witness_completion_tournament as tournament  # noqa: E402


class PhysicalWitnessCompletionTournamentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = tournament.run_tournament()

    def test_tournament_covers_twelve_material_campaign_classes(self) -> None:
        self.assertEqual(self.result["candidate_count"], 12)
        self.assertEqual(
            self.result["candidate_ids"],
            [
                "emergent_gauge_sector",
                "measurement_induced_phase_transition",
                "crossed_product_gravitational_algebra",
                "crispr_spacer_acquisition",
                "dynamic_floquet_code",
                "prion_conformation",
                "autocatalytic_reaction_network",
                "schwinger_pair_production",
                "bose_einstein_condensation",
                "r_process_nucleosynthesis",
                "turbulent_cascade",
                "crack_branching_fracture",
            ],
        )
        self.assertIn("anti-collapse throughput", self.result["excluded_prior_material"])

    def test_panel_represents_all_completion_class_v1_families(self) -> None:
        self.assertEqual(
            self.result["completion_panel_family_ids"], list(cc.PRIMITIVE_FAMILY_IDS)
        )
        self.assertTrue(self.result["all_v1_families_absorbed_somewhere"])
        self.assertEqual(len(self.result["composition_rules_declared"]), 4)

    def test_each_candidate_is_absorbed_without_claim_movement(self) -> None:
        self.assertTrue(self.result["all_candidates_absorbed_by_composed_panel"])
        self.assertEqual(
            self.result["scoped_class_verdict"],
            tournament.SCOPED_CLASS_LEVEL_ABSORPTION,
        )
        for verdict in self.result["candidate_completion_verdicts"].values():
            self.assertEqual(verdict, cc.PHYSICAL_PREDICTIVE_ABSORPTION)
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["e177_modified"])

    def test_survivor_criteria_gate_future_candidate_generation(self) -> None:
        self.assertEqual(
            self.result["survivor_criteria"],
            [
                "source_owned_transition_law",
                "internal_anti_after_naming_rule",
                "w4_perturbation_nonfactorization",
                "native_carrier_or_algebra_growth",
                "matched_intervention_and_resource_budget",
                "observable_difference_from_strongest_fixed_rival",
            ],
        )
        self.assertEqual(
            self.result["next_trigger"],
            "TI-PHYSICAL-WITNESS-GENERATION_READY_AFTER_TOURNAMENT",
        )

    def test_runner_writes_json_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            tournament.write_json(self.result, output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
