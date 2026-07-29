import unittest

from tools.e205_quantum_no_cloning_degree_boundary import assess, result


class E205QuantumNoCloningDegreeBoundaryTests(unittest.TestCase):
    def test_no_cloning_does_not_exclude_fixed_classical_history_rival(self):
        finding = result()["no_cloning_case"]
        self.assertTrue(finding["no_cloning_applies"])
        self.assertTrue(finding["fixed_history_rival_survives"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_degree_guard_requires_more_than_no_cloning(self):
        finding = assess(
            unknown_quantum_state_copy_required=True,
            fixed_classical_history_description_admitted=False,
            universal_oracle_degree_exclusion=False,
        )
        self.assertTrue(finding["no_cloning_applies"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_explicit_universal_exclusion_can_make_guard_eligible(self):
        finding = result()["required_positive_case"]
        self.assertTrue(finding["e199_degree_guard_established"])


if __name__ == "__main__":
    unittest.main()
