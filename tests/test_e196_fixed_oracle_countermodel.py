"""Focused tests for the E196 fixed-oracle correction."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import e196_fixed_oracle_countermodel as fixture


class E196FixedOracleCountermodelTests(unittest.TestCase):
    def test_fixed_realized_history_oracle_is_a_countermodel(self) -> None:
        row = fixture.classify(fixture.fixture_rows()[0])
        self.assertEqual(row["verdict"], "FIXED_PRECORRELATED_ORACLE_COUNTERMODEL")
        self.assertTrue(row["oracle_fixed_at_stage_zero"])
        self.assertFalse(row["oracle_reselected_after_stage_zero"])
        self.assertTrue(row["reproduces_realized_trace"])

    def test_one_fixed_oracle_can_cover_counterfactual_branches(self) -> None:
        row = fixture.classify(fixture.fixture_rows()[1])
        self.assertEqual(row["verdict"], "FIXED_PRECORRELATED_ORACLE_COUNTERMODEL")
        self.assertTrue(row["counterfactual_family_covered"])

    def test_option_set_without_path_fails(self) -> None:
        row = fixture.classify(fixture.fixture_rows()[2])
        self.assertEqual(row["verdict"], "CORRECTED_DEGREE_GUARD_DEFEATS_DISCLOSER")
        self.assertIn("realized_path", row["missing_requirements"])

    def test_path_without_option_set_fails(self) -> None:
        row = fixture.classify(fixture.fixture_rows()[3])
        self.assertEqual(row["verdict"], "CORRECTED_DEGREE_GUARD_DEFEATS_DISCLOSER")
        self.assertIn("option_set_join", row["missing_requirements"])

    def test_adaptive_read_is_copy_not_static_disclosure(self) -> None:
        row = fixture.classify(fixture.fixture_rows()[4])
        self.assertEqual(row["verdict"], "ADAPTIVE_SOURCE_COPY_NOT_STATIC_DISCLOSURE")
        self.assertTrue(row["reproduces_realized_trace"])

    def test_summary_preserves_governance_ceiling(self) -> None:
        result = fixture.result()
        self.assertFalse(result["stage_zero_fixedness_sufficient_for_defeat"])
        self.assertFalse(result["oracle_reselection_required_for_escape"])
        self.assertFalse(result["physical_realizability_established"])
        self.assertFalse(result["source_issuance_established"])
        self.assertIsNone(result["claim_status_change"])


if __name__ == "__main__":
    unittest.main()
