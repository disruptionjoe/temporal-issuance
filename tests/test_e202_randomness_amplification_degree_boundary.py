import unittest

from tools.e202_randomness_amplification_degree_boundary import assess_protocol, result


class E202RandomnessAmplificationDegreeBoundary(unittest.TestCase):
    def test_named_theorem_model_earns_operational_entropy_only(self):
        finding = result()["theorem_model"]
        self.assertTrue(finding["operational_entropy_conclusion"])
        self.assertFalse(finding["all_stage_zero_side_information_typed"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_entropy_and_degree_require_distinct_conclusions(self):
        finding = assess_protocol(
            explicit_quantum_adversary=True, sv_source=True,
            composable_security=True, finite_entropy_conclusion=True,
            all_stage_zero_oracles=True, turing_nonreducibility=False,
        )
        self.assertTrue(finding["operational_entropy_conclusion"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_only_explicit_universal_degree_guard_can_clear_e199(self):
        finding = assess_protocol(
            explicit_quantum_adversary=True, sv_source=True,
            composable_security=True, finite_entropy_conclusion=True,
            all_stage_zero_oracles=True, turing_nonreducibility=True,
        )
        self.assertTrue(finding["e199_degree_guard_established"])


if __name__ == "__main__":
    unittest.main()
