"""Finite pressure fixture for E199 in a CHSH Bell construction.

The fixture distinguishes causal separation from measurement independence.
It does not model quantum amplitudes or claim that a measurement-dependent
completion is physically true.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class Trial:
    trial: int
    x: int
    y: int
    a: int
    b: int

    @property
    def chsh_win(self) -> bool:
        return (self.a ^ self.b) == (self.x & self.y)


@dataclass(frozen=True)
class BellRival:
    rival_id: str
    stage_zero_fixed: bool
    local_response: bool
    post_setting_communication: bool
    measurement_independent: bool
    encodes_completed_transcript: bool


def target_transcript() -> list[Trial]:
    """One finite all-winning CHSH-game transcript."""

    return [
        Trial(0, 0, 0, 0, 0),
        Trial(1, 0, 1, 1, 1),
        Trial(2, 1, 0, 0, 0),
        Trial(3, 1, 1, 0, 1),
    ]


def fixed_measurement_dependent_schedule(trials: list[Trial]) -> dict[int, dict[str, int]]:
    """Encode each setting/outcome row in a stage-0 hidden schedule."""

    return {
        row.trial: {"x": row.x, "y": row.y, "a": row.a, "b": row.b}
        for row in trials
    }


def reproduce(
    trials: list[Trial], schedule: dict[int, dict[str, int]]
) -> bool:
    for row in trials:
        hidden = schedule[row.trial]
        if hidden["x"] != row.x or hidden["y"] != row.y:
            return False
        if hidden["a"] != row.a or hidden["b"] != row.b:
            return False
    return True


def classify(rival: BellRival, finite_transcript_reproduced: bool) -> dict[str, object]:
    if rival.post_setting_communication:
        verdict = "ADAPTIVE_COMMUNICATION_NOT_STATIC_LOCAL_RIVAL"
    elif (
        rival.stage_zero_fixed
        and rival.local_response
        and not rival.measurement_independent
        and rival.encodes_completed_transcript
        and finite_transcript_reproduced
    ):
        verdict = "FIXED_MEASUREMENT_DEPENDENT_COMPLETION"
    elif rival.measurement_independent and rival.local_response:
        verdict = "BELL_LOCAL_INDEPENDENT_FAMILY_PRESSURED_BY_CHSH"
    else:
        verdict = "INCOMPLETE_RIVAL"

    return {
        **asdict(rival),
        "verdict": verdict,
        "finite_transcript_reproduced": finite_transcript_reproduced,
        "causal_source_separation_supported": (
            rival.local_response and not rival.post_setting_communication
        ),
        "future_independence_established": rival.measurement_independent,
        "turing_nonreducibility_established_from_finite_data": False,
    }


def result() -> dict[str, object]:
    trials = target_transcript()
    schedule = fixed_measurement_dependent_schedule(trials)
    fixed_rival = BellRival(
        rival_id="stage_zero_measurement_dependent_local_schedule",
        stage_zero_fixed=True,
        local_response=True,
        post_setting_communication=False,
        measurement_independent=False,
        encodes_completed_transcript=True,
    )
    independent_rival = BellRival(
        rival_id="measurement_independent_local_hidden_variable_family",
        stage_zero_fixed=True,
        local_response=True,
        post_setting_communication=False,
        measurement_independent=True,
        encodes_completed_transcript=False,
    )
    rows = [
        classify(fixed_rival, reproduce(trials, schedule)),
        classify(independent_rival, False),
    ]
    return {
        "result": "BELL_CAUSAL_SEPARATION_WITH_MEASUREMENT_INDEPENDENCE_RESIDUE",
        "construction": "spacelike-separated CHSH Bell experiment",
        "transcript": [asdict(row) | {"chsh_win": row.chsh_win} for row in trials],
        "all_target_rows_win": all(row.chsh_win for row in trials),
        "rows": rows,
        "degree_access_bound_established": False,
        "causal_source_separation_supported": True,
        "future_independence_established": False,
        "measurement_independence_is_independent_assumption": True,
        "finite_transcript_proves_turing_nonreducibility": False,
        "physical_source_issuance_established": False,
        "claim_status_change": None,
    }


def main() -> None:
    output = result()
    artifact = (
        Path(__file__).resolve().parents[1]
        / "tests"
        / "artifacts"
        / "e200_bell_measurement_independence_contract_result.json"
    )
    artifact.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
