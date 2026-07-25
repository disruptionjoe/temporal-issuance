"""Focused tests for E201's quantified Cosmic Bell boundary."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import e201_cosmic_bell_excess_predictability_bound as fixture


class E201CosmicBellExcessPredictabilityTests(unittest.TestCase):
    def test_excess_predictability_uses_worst_port_on_each_side(self) -> None:
        self.assertAlmostEqual(
            fixture.excess_predictability([0.01, 0.04], [0.02, 0.05]),
            0.09,
        )

    def test_fixture_passes_declared_visibility_budget(self) -> None:
        quantitative = fixture.result()["quantitative_fixture"]
        self.assertTrue(quantitative["fixture_not_experimental_data"])
        self.assertTrue(quantitative["epsilon_below_threshold"])
        self.assertLess(
            quantitative["epsilon"], quantitative["visibility_threshold"]
        )

    def test_fixed_common_cause_oracle_reproduces_finite_rows(self) -> None:
        rival = fixture.result()["strongest_fixed_rival"]
        self.assertTrue(rival["stage_zero_fixed"])
        self.assertTrue(rival["finite_transcript_reproduced"])
        self.assertFalse(rival["inside_declared_corrupt_trial_model"])

    def test_quantitative_bound_does_not_change_logical_type(self) -> None:
        result = fixture.result()
        self.assertTrue(result["corrupt_trial_family_quantitatively_bounded"])
        self.assertFalse(
            result["unrestricted_initial_state_independence_established"]
        )
        self.assertFalse(result["future_independence_established"])
        self.assertFalse(result["finite_bound_proves_turing_nonreducibility"])

    def test_governance_ceilings_remain_closed(self) -> None:
        result = fixture.result()
        self.assertFalse(result["physical_source_issuance_established"])
        self.assertIsNone(result["claim_status_change"])


if __name__ == "__main__":
    unittest.main()
