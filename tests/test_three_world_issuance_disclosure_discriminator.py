#!/usr/bin/env python3
"""Tests for tools/three_world_issuance_disclosure_discriminator.py."""

from __future__ import annotations

from dataclasses import replace
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import t2_bounded_completion_barrier_theorem_contract as t2  # noqa: E402
import three_world_issuance_disclosure_discriminator as e177  # noqa: E402


class ThreeWorldIssuanceDisclosureDiscriminatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = e177.run_discriminator()
        self.decisions = {
            decision["world_id"]: decision for decision in self.result["decisions"]
        }

    def test_protocol_is_pinned_and_imports_live_t2_obligations(self) -> None:
        self.assertEqual(
            self.result["protocol_version"],
            "three_world_issuance_disclosure_discriminator_v1",
        )
        self.assertEqual(len(self.result["protocol_digest"]), 64)
        self.assertEqual(
            self.result["protocol_digest"],
            "c098b51fcacd7c191319f573a0d0891eb28cdbbd6698c042a626aab131119042",
        )
        self.assertEqual(self.result["protocol_digest"], e177.protocol_digest())
        self.assertEqual(
            self.result["counterexample_obligation_ids"],
            t2.run_theorem_contract()["counterexample_obligations"],
        )
        self.assertEqual(len(self.result["counterexample_obligation_ids"]), 19)

    def test_worlds_classify_exactly(self) -> None:
        self.assertEqual(self.result["world_a"], e177.FIXED_SOURCE_DISCLOSURE)
        self.assertEqual(
            self.result["world_b"],
            e177.DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE,
        )
        self.assertEqual(self.result["world_c"], e177.CANDIDATE_C_INCOMPLETE)
        self.assertFalse(self.result["world_c_positive_allowed"])
        self.assertFalse(self.result["real_revision_trigger_found"])

    def test_a_and_b_exercise_all_completion_channels(self) -> None:
        for world_id in ("world_a", "world_b"):
            decision = self.decisions[world_id]
            self.assertEqual(
                set(decision["completion_channels"]),
                {
                    "value_completion",
                    "name_completion",
                    "provenance_action_completion",
                    "capability_completion",
                },
            )
            self.assertTrue(
                all(
                    result == e177.ABSORBED
                    for result in decision["completion_channels"].values()
                )
            )
            self.assertEqual(
                decision["whole_family_result"],
                e177.FACTORS_THROUGH_FIXED_FAMILY,
            )
            self.assertIsNotNone(decision["whole_family_factorization_witness"])
            self.assertFalse(decision["w1_non_isomorphic_physical_algebra"])
            self.assertFalse(decision["w4_perturbation_non_factorization"])
            self.assertFalse(decision["W5_TI_record_preservation"])
            self.assertFalse(decision["revision_trigger"])

    def test_a_and_b_run_all_six_perturbations_with_fixed_matches(self) -> None:
        for world_id in ("world_a", "world_b"):
            perturbations = self.decisions[world_id]["perturbation_results"]
            self.assertEqual(
                [row["perturbation_id"] for row in perturbations],
                list(e177.PERTURBATION_IDS),
            )
            self.assertTrue(
                all(row["absorber_family_complete"] for row in perturbations)
            )
            self.assertTrue(
                all(row["exact_match_absorber_ids"] for row in perturbations)
            )
            comparison = self.decisions[world_id]["record_comparison"]
            self.assertEqual(comparison["candidate_growth_error"], 0)
            self.assertIn(0, [row[1] for row in comparison["fixed_source_errors"]])

    def test_world_c_is_fail_closed_and_ignores_desired_booleans(self) -> None:
        decision = self.decisions["world_c"]
        self.assertTrue(decision["desired_boolean_inputs_ignored"])
        self.assertEqual(
            decision["missing_required_fields"],
            sorted(e177.WORLD_C_REQUIRED_FIELDS),
        )
        self.assertTrue(decision["missing_obligations"])
        self.assertTrue(
            all(
                result == e177.UNRESOLVED
                for result in decision["completion_channels"].values()
            )
        )
        self.assertEqual(
            decision["whole_family_result"], e177.WHOLE_FAMILY_UNRESOLVED
        )
        self.assertEqual(decision["w4_perturbation_non_factorization"], e177.W4_INCOMPLETE)
        self.assertEqual(decision["W5_TI_record_preservation"], e177.W5_INCOMPLETE)
        self.assertFalse(decision["positive_allowed"])
        self.assertFalse(decision["revision_trigger"])

    def test_h7_separates_hidden_reveal_from_internal_completed_dynamics(self) -> None:
        self.assertFalse(self.decisions["world_a"]["h7_admitted"])
        self.assertEqual(
            self.decisions["world_a"]["admission_gate_verdict"],
            e177.IMPORTED_STRUCTURE_REJECTED,
        )
        self.assertTrue(self.decisions["world_b"]["h7_admitted"])
        self.assertEqual(
            self.decisions["world_b"]["admission_gate_verdict"],
            e177.ADMITTED_FOR_BOUNDED_TEST,
        )

    def test_terminal_shortcuts_do_not_trigger_revision(self) -> None:
        readout = replace(
            e177.world_b(),
            world_id="readout_control",
            control_only=False,
            readout_finality_status="ONLY",
        )
        h8 = replace(
            e177.world_b(),
            world_id="h8_shortcut_control",
            control_only=False,
            h8_used_as_decision=True,
        )
        self.assertEqual(
            e177.classify_world(readout)["admission_gate_verdict"],
            e177.READOUT_FINALITY_REJECTED,
        )
        self.assertEqual(
            e177.classify_world(h8)["admission_gate_verdict"],
            e177.H8_DECISION_SHORTCUT_REJECTED,
        )
        self.assertFalse(e177.classify_world(readout)["revision_trigger"])
        self.assertFalse(e177.classify_world(h8)["revision_trigger"])

    def test_cross_repo_firewall_never_infers_taf_capability(self) -> None:
        self.assertFalse(self.result["taf_capability_evaluated"])
        self.assertFalse(self.result["cross_repo_implication_allowed"])
        for decision in self.result["decisions"]:
            self.assertFalse(decision["identity_between_them"])
            self.assertFalse(decision["cross_repo_implication_allowed"])
            self.assertEqual(decision["capability_C_R_taf"], e177.NOT_EVALUATED)
            self.assertEqual(decision["taf_interface_verdict"], e177.NOT_EVALUATED)
            self.assertEqual(
                decision["W5_TAF_same_shadow_capability"], e177.NOT_EVALUATED
            )
            self.assertFalse(decision["physically_forced_boundary_established"])
        self.assertEqual(
            self.decisions["world_a"]["taf_interface"][
                "access_complete_equality_certificate"
            ],
            "FAIL_HIDDEN_REVEALED_ACCESS_CHANGED",
        )

    def test_task_and_resource_ledgers_remain_separate(self) -> None:
        task_fields = {
            "inputs",
            "allowed_operations",
            "target_transformation",
            "success_predicate",
            "before_result",
            "after_result",
            "cost",
            "provenance",
        }
        resource_fields = {
            "work",
            "memory",
            "control",
            "transport",
            "storage",
            "external_resource",
            "causal_path",
            "boundary_forcing",
        }
        for decision in self.result["decisions"]:
            self.assertEqual(set(decision["task_interface"]), task_fields)
            self.assertEqual(set(decision["resource_ledgers"]), resource_fields)

    def test_no_claim_or_physical_movement(self) -> None:
        self.assertEqual(self.result["claim_status_change"], "none")
        self.assertFalse(self.result["physical_source_issuance_established"])
        self.assertFalse(self.result["TI_C020_reopened"])
        self.assertFalse(self.result["physically_forced_boundary_established"])

    def test_checked_artifact_matches_and_json_writer_is_stable(self) -> None:
        artifact = (
            REPO_ROOT
            / "tests"
            / "artifacts"
            / "three_world_issuance_disclosure_discriminator_result.json"
        )
        self.assertEqual(json.loads(artifact.read_text(encoding="utf-8")), self.result)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            e177.write_json(self.result, output)
            self.assertEqual(
                output.read_text(encoding="utf-8"),
                json.dumps(self.result, indent=2, sort_keys=True) + "\n",
            )


if __name__ == "__main__":
    unittest.main()
