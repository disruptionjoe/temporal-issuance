#!/usr/bin/env python3
"""Focused tests for Bose-Einstein condensation candidate v0."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import bose_einstein_condensation_candidate_v0 as candidate  # noqa: E402
import completion_class_v1 as cc  # noqa: E402


class BoseEinsteinCondensationCandidateV0Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = candidate.run_candidate()
        self.gates = {row["gate_id"]: row for row in self.result["witness_gates"]}

    def test_candidate_is_killed_by_fixed_many_body_hamiltonian(self) -> None:
        self.assertEqual(self.result["candidate_status"], candidate.CANDIDATE_STATUS)
        self.assertFalse(self.result["packet_admitted"])
        self.assertFalse(self.result["typed_action_2_packet"])
        self.assertFalse(self.result["native_source_law_supplied"])

    def test_condensation_signal_is_not_source_growth(self) -> None:
        self.assertTrue(self.result["condensation_signal_present"])
        self.assertTrue(
            self.gates["W1_non_isomorphic_source_algebra"][
                "condensation_signal"
            ]
        )
        self.assertTrue(
            self.gates["W2_new_admissibility_predicate"]["condensation_signal"]
        )
        self.assertTrue(
            self.gates["W3_construction_space_growth"]["condensation_signal"]
        )
        self.assertFalse(
            self.gates["W1_non_isomorphic_source_algebra"]["source_passed"]
        )
        self.assertFalse(self.result["source_growth_core_passed"])

    def test_w4_and_w6_absorber_controls_fail_while_w5_survives(self) -> None:
        self.assertFalse(
            self.gates["W4_perturbation_non_factorization"]["source_passed"]
        )
        self.assertTrue(self.gates["W5_record_preservation"]["source_passed"])
        self.assertFalse(
            self.gates["W6_fixed_family_after_naming_absorption"]["source_passed"]
        )
        self.assertFalse(self.result["absorber_controls_passed"])

    def test_completion_class_records_physical_predictive_absorption(self) -> None:
        self.assertEqual(
            self.result["completion_class_verdict"],
            cc.PHYSICAL_PREDICTIVE_ABSORPTION,
        )
        self.assertEqual(
            self.result["valid_completion_witness_ids"],
            [candidate.COMPLETION_WITNESS_ID],
        )
        self.assertEqual(self.result["unresolved_family_ids"], [])
        self.assertEqual(self.result["missing_family_ids"], [])

    def test_fixed_source_rival_preserves_trace_without_source_law(self) -> None:
        rival = self.result["fixed_source_rival"]
        self.assertTrue(rival["fixed_many_body_hamiltonian"])
        self.assertTrue(rival["fixed_bosonic_field_algebra"])
        self.assertTrue(rival["fixed_particle_species_and_fock_space"])
        self.assertTrue(rival["fixed_trap_geometry"])
        self.assertTrue(rival["fixed_interaction_strength"])
        self.assertTrue(rival["fixed_cooling_trajectory_and_reservoir"])
        self.assertTrue(rival["stochastic_seed_or_thermal_fluctuation_tape"])
        self.assertTrue(rival["completed_condensation_history_available"])
        self.assertTrue(rival["record_trace_preserved"])
        self.assertTrue(rival["reproduces_candidate_shape"])
        self.assertFalse(rival["source_owned_condensate_law"])

    def test_missing_source_object_names_resurrection_burden(self) -> None:
        missing = self.result["exact_missing_source_object"]
        self.assertEqual(
            missing["missing_object_id"],
            "source_owned_condensate_mode_generation_law",
        )
        self.assertIn("native physical source law", missing["required"])
        self.assertIn("fixed many-body", missing["required"])
        self.assertIn("internal anti-after-naming", missing["also_required"])
        self.assertIn("W4 perturbation", missing["also_required"])

    def test_protected_surfaces_do_not_move(self) -> None:
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["E177_modified"])
        self.assertFalse(self.result["cross_repo_implication"])

    def test_runner_writes_byte_stable_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            candidate.write_json(self.result, first)
            candidate.write_json(candidate.run_candidate(), second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(json.loads(first.read_text(encoding="utf-8")), self.result)


if __name__ == "__main__":
    unittest.main()
