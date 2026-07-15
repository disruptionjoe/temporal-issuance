#!/usr/bin/env python3
"""Focused tests for CompletionClass v1."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import completion_class_v1 as cc  # noqa: E402


class CompletionClassV1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = cc.run_contract()
        self.cases = {case.case_id: case for case in cc.fixture_cases()}
        self.decisions = {
            case_id: cc.classify_case(case) for case_id, case in self.cases.items()
        }

    def test_inventory_is_exactly_the_requested_eleven_families(self) -> None:
        self.assertEqual(len(cc.PRIMITIVE_FAMILY_IDS), 11)
        self.assertEqual(
            set(cc.PRIMITIVE_FAMILY_IDS),
            {
                "hidden_state",
                "initial_condition",
                "boundary_condition",
                "fixed_source",
                "stochastic_seed",
                "name_provenance",
                "resource_capability",
                "whole_family",
                "completed_history",
                "observer_information_access",
                "relabel_gauge",
            },
        )

    def test_four_conclusion_strengths_are_distinct(self) -> None:
        self.assertEqual(len(cc.CONCLUSION_CLASSES), 4)
        self.assertEqual(len(set(cc.CONCLUSION_CLASSES)), 4)
        observed = {
            self.decisions[f"single_{family_id}_absorber"]["verdict"]
            for family_id in cc.PRIMITIVE_FAMILY_IDS
        }
        self.assertEqual(observed, set(cc.CONCLUSION_CLASSES))

    def test_every_single_family_absorber_is_exercised(self) -> None:
        for family_id in cc.PRIMITIVE_FAMILY_IDS:
            decision = self.decisions[f"single_{family_id}_absorber"]
            self.assertIn(decision["verdict"], cc.CONCLUSION_CLASSES)
            self.assertIn(family_id, decision["absorbed_family_ids"])
        self.assertTrue(self.result["all_primitive_absorbers_exercised"])

    def test_every_omission_mutant_fails_closed(self) -> None:
        for family_id in cc.PRIMITIVE_FAMILY_IDS:
            decision = self.decisions[f"omitted_{family_id}"]
            self.assertEqual(decision["verdict"], cc.INCOMPLETE_NULL_CLASS)
            self.assertEqual(decision["missing_family_ids"], [family_id])
        self.assertTrue(self.result["all_omission_mutants_fail_closed"])

    def test_hybrid_completion_is_load_bearing(self) -> None:
        decision = self.decisions["hybrid_stochastic_seed_plus_access"]
        self.assertEqual(decision["verdict"], cc.PHYSICAL_PREDICTIVE_ABSORPTION)
        self.assertEqual(
            set(decision["absorbed_family_ids"]),
            {"stochastic_seed", "observer_information_access"},
        )
        self.assertTrue(self.result["hybrid_completion_exercised"])

    def test_unverified_and_posthoc_predictive_models_fail_closed(self) -> None:
        self.assertEqual(
            self.decisions["unverified_whole_family_certificate"]["verdict"],
            cc.INCOMPLETE_NULL_CLASS,
        )
        self.assertEqual(
            self.decisions["posthoc_fixed_source_model"]["verdict"],
            cc.INCOMPLETE_NULL_CLASS,
        )
        self.assertTrue(self.result["unverified_certificate_fails_closed"])
        self.assertTrue(self.result["posthoc_predictive_model_fails_closed"])

    def test_bounded_survival_never_becomes_issuance(self) -> None:
        decision = self.decisions["bounded_survivor_control"]
        self.assertEqual(
            decision["verdict"], cc.SURVIVES_BOUNDED_COMPLETION_CLASS
        )
        self.assertFalse(decision["physical_source_issuance_established"])
        self.assertTrue(self.result["bounded_survivor_is_not_issuance"])

    def test_world_controls_preserve_e177_semantics_without_modifying_e177(self) -> None:
        self.assertEqual(
            self.result["world_a"], cc.PHYSICAL_PREDICTIVE_ABSORPTION
        )
        self.assertEqual(
            self.result["world_b"], cc.PHYSICAL_PREDICTIVE_ABSORPTION
        )
        self.assertEqual(self.result["world_c"], cc.INCOMPLETE_NULL_CLASS)
        self.assertFalse(self.result["e177_modified"])

    def test_composition_closure_is_required(self) -> None:
        decision = self.decisions["composition_closure_missing"]
        self.assertEqual(decision["verdict"], cc.INCOMPLETE_NULL_CLASS)

    def test_no_result_path_asserts_physical_source_issuance(self) -> None:
        for decision in self.decisions.values():
            self.assertFalse(decision["physical_source_issuance_established"])
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertEqual(self.result["claim_status_change"], "none")

    def test_runner_writes_byte_stable_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            cc.write_json(self.result, first)
            cc.write_json(cc.run_contract(), second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(
                json.loads(first.read_text(encoding="utf-8")), self.result
            )


if __name__ == "__main__":
    unittest.main()
