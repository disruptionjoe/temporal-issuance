"""E202: keep composable DI entropy distinct from source-degree separation."""

import json
from pathlib import Path


PAPER = "Kessler and Arnon-Friedman, arXiv:1705.04148"


def assess_protocol(*, explicit_quantum_adversary, sv_source, composable_security,
                    finite_entropy_conclusion, all_stage_zero_oracles,
                    turing_nonreducibility):
    """Classify exactly what the declared theorem conclusion can support."""
    operational_entropy = all(
        [explicit_quantum_adversary, sv_source, composable_security,
         finite_entropy_conclusion]
    )
    degree_bridge = all_stage_zero_oracles and turing_nonreducibility
    return {
        "operational_entropy_conclusion": operational_entropy,
        "all_stage_zero_side_information_typed": all_stage_zero_oracles,
        "turing_nonreducibility_proved": turing_nonreducibility,
        "e199_degree_guard_established": degree_bridge,
        "physical_source_issuance_established": degree_bridge,
    }


def result():
    theorem_model = assess_protocol(
        explicit_quantum_adversary=True,
        sv_source=True,
        composable_security=True,
        finite_entropy_conclusion=True,
        all_stage_zero_oracles=False,
        turing_nonreducibility=False,
    )
    fixed_oracle_rival = assess_protocol(
        explicit_quantum_adversary=False,
        sv_source=False,
        composable_security=False,
        finite_entropy_conclusion=False,
        all_stage_zero_oracles=False,
        turing_nonreducibility=False,
    )
    return {
        "result": "COMPOSABLE_ENTROPY_BOUND_WITH_DEGREE_RESIDUE",
        "primary_source": PAPER,
        "theorem_model": theorem_model,
        "stage_zero_fixed_oracle_rival": fixed_oracle_rival,
        "boundary": (
            "A composable smooth/min-entropy conclusion against the stated "
            "quantum adversary model is an operational secrecy result; it does "
            "not quantify over every stage-0 oracle or imply Turing-degree "
            "non-reducibility of the realized history."
        ),
        "claim_status_change": "none",
    }


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "tests/artifacts/e202_randomness_amplification_degree_boundary_result.json"
    output.write_text(json.dumps(result(), indent=2) + "\n")
    print(json.dumps(result(), indent=2))
