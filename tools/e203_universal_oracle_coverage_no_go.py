"""E203: unrestricted oracle coverage cannot yield the E199 degree guard."""
from __future__ import annotations
import json
from pathlib import Path

def assess(*, all_stage_zero_oracles_admitted: bool, degree_exclusion_supplied: bool) -> dict[str, bool]:
    reflexive_rival_admitted = all_stage_zero_oracles_admitted and not degree_exclusion_supplied
    return {
        "all_stage_zero_oracles_admitted": all_stage_zero_oracles_admitted,
        "independent_degree_exclusion_supplied": degree_exclusion_supplied,
        "reflexive_jh_oracle_admitted": reflexive_rival_admitted,
        "universal_jh_nonreducibility_possible": not reflexive_rival_admitted,
    }

def result() -> dict[str, object]:
    return {
        "result": "UNRESTRICTED_ORACLE_COVERAGE_REFUTED_AS_E199_ROUTE",
        "unrestricted_stage_zero_class": assess(all_stage_zero_oracles_admitted=True, degree_exclusion_supplied=False),
        "physically_restricted_class": assess(all_stage_zero_oracles_admitted=False, degree_exclusion_supplied=True),
        "boundary": "If the admitted class includes O = J_H, then J_H <=_T O by identity. A positive route needs a named physical access or degree restriction; entropy alone is not that restriction.",
        "physical_realizability_established": False,
        "physical_source_issuance_established": False,
        "claim_status_change": None,
    }

if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "tests/artifacts/e203_universal_oracle_coverage_no_go_result.json"
    output.write_text(json.dumps(result(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(result(), indent=2, sort_keys=True))
