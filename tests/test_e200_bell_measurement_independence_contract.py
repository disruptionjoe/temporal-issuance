"""Focused tests for the E200 Bell measurement-independence pressure."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import e200_bell_measurement_independence_contract as fixture


class E200BellMeasurementIndependenceTests(unittest.TestCase):
    def test_target_transcript_wins_each_chsh_row(self) -> None:
        self.assertTrue(all(row.chsh_win for row in fixture.target_transcript()))

    def test_fixed_measurement_dependent_schedule_reproduces_transcript(self) -> None:
        trials = fixture.target_transcript()
        schedule = fixture.fixed_measurement_dependent_schedule(trials)
        self.assertTrue(fixture.reproduce(trials, schedule))

    def test_fixed_rival_is_local_without_post_setting_communication(self) -> None:
        row = fixture.result()["rows"][0]
        self.assertEqual(row["verdict"], "FIXED_MEASUREMENT_DEPENDENT_COMPLETION")
        self.assertTrue(row["local_response"])
        self.assertFalse(row["post_setting_communication"])
        self.assertFalse(row["measurement_independent"])

    def test_independent_local_family_is_the_bell_test_target(self) -> None:
        row = fixture.result()["rows"][1]
        self.assertEqual(
            row["verdict"], "BELL_LOCAL_INDEPENDENT_FAMILY_PRESSURED_BY_CHSH"
        )
        self.assertTrue(row["measurement_independent"])

    def test_summary_preserves_e199_and_governance_ceilings(self) -> None:
        result = fixture.result()
        self.assertTrue(result["causal_source_separation_supported"])
        self.assertFalse(result["degree_access_bound_established"])
        self.assertFalse(result["future_independence_established"])
        self.assertFalse(result["finite_transcript_proves_turing_nonreducibility"])
        self.assertFalse(result["physical_source_issuance_established"])
        self.assertIsNone(result["claim_status_change"])


if __name__ == "__main__":
    unittest.main()
