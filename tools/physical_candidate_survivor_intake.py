"""Fail-closed intake gate for post-tournament physical candidates."""

from __future__ import annotations

from dataclasses import dataclass


CRITERIA = (
    "source_owned_transition_law",
    "internal_anti_after_naming_rule",
    "w4_perturbation_nonfactorization",
    "native_carrier_or_algebra_growth",
    "matched_intervention_and_resource_budget",
    "observable_difference_from_strongest_fixed_rival",
    "physical_records_preserved",
)


@dataclass(frozen=True)
class Criterion:
    supplied: bool
    evidence_ref: str
    falsifier: str


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    construction_id: str
    strongest_fixed_rival_id: str
    criteria: dict[str, Criterion]


def classify(candidate: Candidate) -> dict[str, object]:
    missing: list[str] = []
    for name in CRITERIA:
        row = candidate.criteria.get(name)
        if row is None or not row.supplied or not row.evidence_ref.strip() or not row.falsifier.strip():
            missing.append(name)
    if not candidate.construction_id.strip():
        missing.append("construction_id")
    if not candidate.strongest_fixed_rival_id.strip():
        missing.append("strongest_fixed_rival_id")

    return {
        "candidate_id": candidate.candidate_id,
        "verdict": "ADMIT_FOR_ADJUDICATION_ONLY" if not missing else "REJECT_INCOMPLETE",
        "missing": missing,
        "physical_source_issuance_established": False,
    }
