"""Executable boundary test for the E201 Cosmic Bell contract.

This fixture represents the quantitative *type* of the high-redshift-quasar
Cosmic Bell excess-predictability analysis. It does not reproduce the
experiment's data or claim that a completed-transcript rival is physical.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from math import sqrt
from pathlib import Path


@dataclass(frozen=True)
class Trial:
    trial: int
    a_setting: int
    b_setting: int
    a_outcome: int
    b_outcome: int


def excess_predictability(
    alice_corrupt_fractions: list[float],
    bob_corrupt_fractions: list[float],
) -> float:
    """Paper's conservative joint excess-predictability aggregation."""

    if not alice_corrupt_fractions or not bob_corrupt_fractions:
        raise ValueError("both sides require at least one declared setting port")
    values = alice_corrupt_fractions + bob_corrupt_fractions
    if any(value < 0 or value > 1 for value in values):
        raise ValueError("corrupt fractions must lie in [0, 1]")
    return max(alice_corrupt_fractions) + max(bob_corrupt_fractions)


def visibility_threshold(visibility: float) -> float:
    """Return V*sqrt(2)-1, the Cosmic Bell admissibility threshold."""

    if visibility < 0 or visibility > 1:
        raise ValueError("visibility must lie in [0, 1]")
    return visibility * sqrt(2) - 1


def completed_transcript() -> list[Trial]:
    """A finite fixture, not experimental data."""

    return [
        Trial(0, 0, 0, 0, 0),
        Trial(1, 0, 1, 1, 1),
        Trial(2, 1, 0, 0, 0),
        Trial(3, 1, 1, 0, 1),
    ]


def stage_zero_common_cause_oracle(
    trials: list[Trial],
) -> dict[int, dict[str, int]]:
    """The strongest fixed rival: complete finite rows available at stage 0."""

    return {row.trial: asdict(row) for row in trials}


def oracle_reproduces(
    trials: list[Trial], oracle: dict[int, dict[str, int]]
) -> bool:
    return all(oracle[row.trial] == asdict(row) for row in trials)


def result() -> dict[str, object]:
    # Illustrative preregistered fixture values, deliberately not paper data.
    visibility = 0.93
    alice_corrupt_fractions = [0.03, 0.04]
    bob_corrupt_fractions = [0.04, 0.05]
    epsilon = excess_predictability(
        alice_corrupt_fractions, bob_corrupt_fractions
    )
    threshold = visibility_threshold(visibility)
    trials = completed_transcript()
    oracle = stage_zero_common_cause_oracle(trials)

    return {
        "result": "QUANTIFIED_CORRUPT_TRIAL_BOUND_WITH_ORACLE_DEGREE_RESIDUE",
        "construction": (
            "high-redshift-quasar Cosmic Bell setting protocol with "
            "excess-predictability budget"
        ),
        "initial_state": (
            "entangled-pair preparation plus any local-realist hidden state"
        ),
        "setting_source": (
            "dichroic wavelength classification of high-redshift quasar photons"
        ),
        "side_information": [
            "skyglow and detector noise",
            "atmospheric and instrumental corruption",
            "any selective alteration or preview of quasar wavelengths",
            "any common cause correlating hidden state with the completed settings",
        ],
        "causal_model": (
            "local-realist corrupt-trial model plus explicit no-preview and "
            "no-selective-alteration premises"
        ),
        "quantitative_fixture": {
            "fixture_not_experimental_data": True,
            "visibility": visibility,
            "alice_corrupt_fractions": alice_corrupt_fractions,
            "bob_corrupt_fractions": bob_corrupt_fractions,
            "epsilon": epsilon,
            "visibility_threshold": threshold,
            "epsilon_below_threshold": epsilon < threshold,
            "local_realist_c_bound": epsilon,
        },
        "strongest_fixed_rival": {
            "rival_id": "stage_zero_completed_transcript_common_cause_oracle",
            "stage_zero_fixed": True,
            "finite_transcript_encoded": True,
            "finite_transcript_reproduced": oracle_reproduces(trials, oracle),
            "inside_declared_corrupt_trial_model": False,
            "violated_protocol_premise": (
                "no preview/selective alteration or unrestricted common cause"
            ),
        },
        "causal_lookback_gain": (
            "under the protocol premises, the common-cause window is pushed "
            "back at least about 7.8 Gyr for the strongest quasar pair"
        ),
        "corrupt_trial_family_quantitatively_bounded": True,
        "unrestricted_initial_state_independence_established": False,
        "future_independence_established": False,
        "finite_bound_proves_turing_nonreducibility": False,
        "reason_no_degree_bridge": (
            "epsilon bounds frequencies in a declared finite probabilistic "
            "model; it does not type or upper-bound the Turing degree of all "
            "admissible stage-zero side information"
        ),
        "physical_source_issuance_established": False,
        "claim_status_change": None,
    }


def main() -> None:
    output = result()
    artifact = (
        Path(__file__).resolve().parents[1]
        / "tests"
        / "artifacts"
        / "e201_cosmic_bell_excess_predictability_bound_result.json"
    )
    artifact.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
