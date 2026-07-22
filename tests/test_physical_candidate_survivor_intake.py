"""Tests for the post-tournament physical-candidate intake gate."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import physical_candidate_survivor_intake as gate


def complete_candidate() -> gate.Candidate:
    rows = {
        name: gate.Criterion(True, f"source#{name}", f"falsify {name}")
        for name in gate.CRITERIA
    }
    return gate.Candidate("synthetic-control", "native-construction", "fixed-rival", rows)


class SurvivorIntakeTests(unittest.TestCase):
    def test_complete_shape_admits_only_for_adjudication(self) -> None:
        result = gate.classify(complete_candidate())
        self.assertEqual(result["verdict"], "ADMIT_FOR_ADJUDICATION_ONLY")
        self.assertFalse(result["physical_source_issuance_established"])

    def test_missing_w4_fails_closed(self) -> None:
        candidate = complete_candidate()
        rows = dict(candidate.criteria)
        rows["w4_perturbation_nonfactorization"] = gate.Criterion(False, "", "")
        result = gate.classify(gate.Candidate(candidate.candidate_id, candidate.construction_id, candidate.strongest_fixed_rival_id, rows))
        self.assertEqual(result["verdict"], "REJECT_INCOMPLETE")
        self.assertIn("w4_perturbation_nonfactorization", result["missing"])

    def test_label_only_claim_fails_closed(self) -> None:
        rows = {name: gate.Criterion(True, "", "") for name in gate.CRITERIA}
        result = gate.classify(gate.Candidate("labels-only", "native", "rival", rows))
        self.assertEqual(set(result["missing"]), set(gate.CRITERIA))


if __name__ == "__main__":
    unittest.main()
