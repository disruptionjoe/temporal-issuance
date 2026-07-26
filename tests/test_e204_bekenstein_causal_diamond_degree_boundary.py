import unittest

from tools.e204_bekenstein_causal_diamond_degree_boundary import assess, result


class E204BekensteinCausalDiamondDegreeBoundaryTests(unittest.TestCase):
    def test_local_bound_does_not_exclude_external_fixed_rival(self):
        finding = result()["local_causal_diamond"]
        self.assertTrue(finding["bounded_system_entropy_bound_applies"])
        self.assertTrue(finding["fixed_history_rival_survives"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_only_complete_static_closure_can_clear_interface_obstruction(self):
        finding = assess(
            bounded_region=True,
            finite_energy=True,
            complete_discloser_contained=True,
            external_or_adaptive_oracle_admitted=False,
        )
        self.assertTrue(finding["e199_degree_guard_ready_for_derivation"])
        self.assertFalse(finding["e199_degree_guard_established"])

    def test_uncontained_discloser_fails_even_without_adaptive_access(self):
        finding = assess(
            bounded_region=True,
            finite_energy=True,
            complete_discloser_contained=False,
            external_or_adaptive_oracle_admitted=False,
        )
        self.assertTrue(finding["fixed_history_rival_survives"])
        self.assertFalse(finding["e199_degree_guard_established"])


if __name__ == "__main__":
    unittest.main()
