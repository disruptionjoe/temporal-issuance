import unittest
from tools.e203_universal_oracle_coverage_no_go import assess, result

class E203UniversalOracleCoverageNoGoTests(unittest.TestCase):
    def test_unrestricted_class_admits_reflexive_countermodel(self):
        finding = result()["unrestricted_stage_zero_class"]
        self.assertTrue(finding["reflexive_jh_oracle_admitted"])
        self.assertFalse(finding["universal_jh_nonreducibility_possible"])
    def test_entropy_cannot_supply_degree_exclusion(self):
        self.assertTrue(assess(all_stage_zero_oracles_admitted=True, degree_exclusion_supplied=False)["reflexive_jh_oracle_admitted"])
    def test_restricted_class_is_not_source_issuance(self):
        self.assertTrue(result()["physically_restricted_class"]["independent_degree_exclusion_supplied"])
        self.assertFalse(result()["physical_source_issuance_established"])

if __name__ == "__main__":
    unittest.main()
