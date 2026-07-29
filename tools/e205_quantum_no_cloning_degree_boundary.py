"""E205: quantum no-cloning is not by itself an E199 oracle-degree exclusion."""

from __future__ import annotations

import json
from pathlib import Path


PRIMARY_SOURCE = (
    "W. K. Wootters and W. H. Zurek, 'A single quantum cannot be cloned', "
    "Nature 299, 802–803 (1982), doi:10.1038/299802a0"
)


def assess(*, unknown_quantum_state_copy_required: bool,
           fixed_classical_history_description_admitted: bool,
           universal_oracle_degree_exclusion: bool) -> dict[str, bool]:
    """Separate the theorem's copying premise from E199's degree premise."""
    no_cloning_applies = unknown_quantum_state_copy_required
    fixed_history_rival_survives = fixed_classical_history_description_admitted
    return {
        "no_cloning_applies": no_cloning_applies,
        "fixed_classical_history_description_admitted": fixed_classical_history_description_admitted,
        "fixed_history_rival_survives": fixed_history_rival_survives,
        "universal_oracle_degree_exclusion": universal_oracle_degree_exclusion,
        "e199_degree_guard_established": universal_oracle_degree_exclusion
        and not fixed_history_rival_survives,
    }


def result() -> dict[str, object]:
    no_cloning_case = assess(
        unknown_quantum_state_copy_required=True,
        fixed_classical_history_description_admitted=True,
        universal_oracle_degree_exclusion=False,
    )
    required_positive_case = assess(
        unknown_quantum_state_copy_required=True,
        fixed_classical_history_description_admitted=False,
        universal_oracle_degree_exclusion=True,
    )
    return {
        "result": "NO_CLONING_WITH_FIXED_HISTORY_DEGREE_RESIDUE",
        "primary_source": PRIMARY_SOURCE,
        "construction_boundary": (
            "No-cloning excludes a universal copier for an unknown quantum state. "
            "E199's rival can instead be a stage-0 fixed classical description or "
            "schedule; reproducing its accessible transcript need not copy an unknown state."
        ),
        "no_cloning_case": no_cloning_case,
        "required_positive_case": required_positive_case,
        "falsifiable_consequence": (
            "A proposed no-cloning degree guard fails unless it identifies the exact "
            "unknown-state copying operation required by the rival and independently "
            "excludes every fixed classical history description that reproduces the transcript."
        ),
        "physical_source_issuance_established": False,
        "claim_status_change": "none",
    }


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "tests/artifacts/e205_quantum_no_cloning_degree_boundary_result.json"
    output.write_text(json.dumps(result(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(result(), indent=2, sort_keys=True))
