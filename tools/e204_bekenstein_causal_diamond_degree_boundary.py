"""E204: a bounded-system entropy limit is not yet an E199 degree bound."""
from __future__ import annotations

import json
from pathlib import Path


def assess(*, bounded_region: bool, finite_energy: bool, complete_discloser_contained: bool,
           external_or_adaptive_oracle_admitted: bool) -> dict[str, bool]:
    """Keep the local capacity claim separate from global oracle exclusion."""
    local_capacity_bound = bounded_region and finite_energy
    fixed_history_rival_survives = external_or_adaptive_oracle_admitted or not complete_discloser_contained
    return {
        "bounded_system_entropy_bound_applies": local_capacity_bound,
        "complete_static_discloser_contained": complete_discloser_contained,
        "external_or_adaptive_oracle_admitted": external_or_adaptive_oracle_admitted,
        "fixed_history_rival_survives": fixed_history_rival_survives,
        "e199_degree_guard_ready_for_derivation": local_capacity_bound and complete_discloser_contained
        and not external_or_adaptive_oracle_admitted,
        "e199_degree_guard_established": False,
    }


def result() -> dict[str, object]:
    local_diamond = assess(
        bounded_region=True,
        finite_energy=True,
        complete_discloser_contained=False,
        external_or_adaptive_oracle_admitted=True,
    )
    return {
        "result": "LOCAL_CAPACITY_BOUND_WITH_GLOBAL_CLOSURE_RESIDUE",
        "bekenstein_scope": "finite-energy system in a bounded region; not an asserted global source-degree theorem",
        "local_causal_diamond": local_diamond,
        "required_positive_packet": [
            "a physically warranted complete-discloser containment statement",
            "a static, not adaptive, disclosure model",
            "an exclusion of external fixed-history or branch-family access",
            "a derivation connecting that closure to J_H not <=_T O",
        ],
        "falsifiable_consequence": "A proposed physical degree guard fails if its declared bounded region permits an external or adaptive oracle reproducing the same accessible transcript.",
        "physical_degree_exclusion_established": False,
        "physical_source_issuance_established": False,
        "claim_status_change": None,
    }


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "tests/artifacts/e204_bekenstein_causal_diamond_degree_boundary_result.json"
    output.write_text(json.dumps(result(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(result(), indent=2, sort_keys=True))
