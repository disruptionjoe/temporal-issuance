#!/usr/bin/env python3
"""Bounded CompletionClass v1 contract and adversarial fixtures.

The executable distinguishes four strengths of absorption and fails closed on
omitted or unresolved completion families. It has no code path that establishes
physical source issuance.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PHYSICAL_PREDICTIVE_ABSORPTION = "PHYSICAL_PREDICTIVE_ABSORPTION"
OPERATIONAL_CONTEXT_ABSORPTION = "OPERATIONAL_CONTEXT_ABSORPTION"
REPRESENTATIONAL_SURPLUS_ABSORPTION = "REPRESENTATIONAL_SURPLUS_ABSORPTION"
GLOBAL_ONTOLOGICAL_ABSORPTION = "GLOBAL_ONTOLOGICAL_ABSORPTION"
INCOMPLETE_NULL_CLASS = "INCOMPLETE_NULL_CLASS"
SURVIVES_BOUNDED_COMPLETION_CLASS = "SURVIVES_BOUNDED_COMPLETION_CLASS"

CONCLUSION_CLASSES = (
    PHYSICAL_PREDICTIVE_ABSORPTION,
    OPERATIONAL_CONTEXT_ABSORPTION,
    REPRESENTATIONAL_SURPLUS_ABSORPTION,
    GLOBAL_ONTOLOGICAL_ABSORPTION,
)

PHYSICAL_FAMILIES = (
    "hidden_state",
    "initial_condition",
    "boundary_condition",
    "fixed_source",
    "stochastic_seed",
)
OPERATIONAL_FAMILIES = (
    "resource_capability",
    "observer_information_access",
)
REPRESENTATIONAL_FAMILIES = (
    "name_provenance",
    "relabel_gauge",
)
GLOBAL_FAMILIES = (
    "whole_family",
    "completed_history",
)
PRIMITIVE_FAMILY_IDS = (
    "hidden_state",
    "initial_condition",
    "boundary_condition",
    "fixed_source",
    "stochastic_seed",
    "name_provenance",
    "resource_capability",
    "whole_family",
    "completed_history",
    "observer_information_access",
    "relabel_gauge",
)

FAMILY_TO_CONCLUSION = {
    **{family: PHYSICAL_PREDICTIVE_ABSORPTION for family in PHYSICAL_FAMILIES},
    **{family: OPERATIONAL_CONTEXT_ABSORPTION for family in OPERATIONAL_FAMILIES},
    **{
        family: REPRESENTATIONAL_SURPLUS_ABSORPTION
        for family in REPRESENTATIONAL_FAMILIES
    },
    **{family: GLOBAL_ONTOLOGICAL_ABSORPTION for family in GLOBAL_FAMILIES},
}

CONCLUSION_PRECEDENCE = (
    PHYSICAL_PREDICTIVE_ABSORPTION,
    OPERATIONAL_CONTEXT_ABSORPTION,
    REPRESENTATIONAL_SURPLUS_ABSORPTION,
    GLOBAL_ONTOLOGICAL_ABSORPTION,
)


@dataclass(frozen=True)
class CompletionWitness:
    witness_id: str
    family_ids: tuple[str, ...]
    predeclared: bool
    outcome_independent: bool
    physically_admissible: bool
    reproduces_joint_trace: bool
    preserves_comparison_contract: bool
    quotient_respecting: bool
    certificate_verified: bool


@dataclass(frozen=True)
class CompletionCase:
    case_id: str
    represented_family_ids: tuple[str, ...]
    verified_nonfactorization_family_ids: tuple[str, ...]
    witnesses: tuple[CompletionWitness, ...]
    composition_closure_declared: bool = True


def family_ids_valid(family_ids: tuple[str, ...]) -> bool:
    return bool(family_ids) and set(family_ids).issubset(PRIMITIVE_FAMILY_IDS)


def witness_conclusion(witness: CompletionWitness) -> str:
    conclusions = {
        FAMILY_TO_CONCLUSION[family_id] for family_id in witness.family_ids
    }
    for conclusion in CONCLUSION_PRECEDENCE:
        if conclusion in conclusions:
            return conclusion
    raise ValueError("Completion witness has no registered conclusion class")


def witness_is_verified(witness: CompletionWitness) -> bool:
    if not family_ids_valid(witness.family_ids):
        return False
    conclusion = witness_conclusion(witness)
    common = bool(
        witness.reproduces_joint_trace
        and witness.preserves_comparison_contract
        and witness.quotient_respecting
        and witness.certificate_verified
    )
    if conclusion in (
        PHYSICAL_PREDICTIVE_ABSORPTION,
        OPERATIONAL_CONTEXT_ABSORPTION,
    ):
        return bool(
            common
            and witness.predeclared
            and witness.outcome_independent
            and witness.physically_admissible
        )
    return common


def _strongest_conclusion(conclusions: set[str]) -> str:
    for conclusion in CONCLUSION_PRECEDENCE:
        if conclusion in conclusions:
            return conclusion
    raise ValueError("No absorption conclusion available")


def classify_case(case: CompletionCase) -> dict[str, Any]:
    represented = set(case.represented_family_ids)
    verified_nonfactorization = set(case.verified_nonfactorization_family_ids)
    valid_witnesses = tuple(
        witness for witness in case.witnesses if witness_is_verified(witness)
    )
    absorbed_family_ids = {
        family_id
        for witness in valid_witnesses
        for family_id in witness.family_ids
    }
    missing_family_ids = set(PRIMITIVE_FAMILY_IDS) - represented
    unresolved_family_ids = represented - (
        verified_nonfactorization | absorbed_family_ids
    )
    conclusions = {witness_conclusion(witness) for witness in valid_witnesses}

    if conclusions:
        verdict = _strongest_conclusion(conclusions)
    elif (
        missing_family_ids
        or unresolved_family_ids
        or not case.composition_closure_declared
    ):
        verdict = INCOMPLETE_NULL_CLASS
    else:
        verdict = SURVIVES_BOUNDED_COMPLETION_CLASS

    return {
        "case_id": case.case_id,
        "verdict": verdict,
        "absorption_conclusions": sorted(conclusions),
        "valid_witness_ids": sorted(
            witness.witness_id for witness in valid_witnesses
        ),
        "absorbed_family_ids": sorted(absorbed_family_ids),
        "missing_family_ids": sorted(missing_family_ids),
        "unresolved_family_ids": sorted(unresolved_family_ids),
        "composition_closure_declared": case.composition_closure_declared,
        "physical_source_issuance_established": False,
    }


def _witness(
    witness_id: str,
    family_ids: tuple[str, ...],
    *,
    predeclared: bool = True,
    outcome_independent: bool = True,
    physically_admissible: bool = True,
    certificate_verified: bool = True,
) -> CompletionWitness:
    return CompletionWitness(
        witness_id=witness_id,
        family_ids=family_ids,
        predeclared=predeclared,
        outcome_independent=outcome_independent,
        physically_admissible=physically_admissible,
        reproduces_joint_trace=True,
        preserves_comparison_contract=True,
        quotient_respecting=True,
        certificate_verified=certificate_verified,
    )


def _nonfactorization_except(*family_ids: str) -> tuple[str, ...]:
    excluded = set(family_ids)
    return tuple(
        family_id
        for family_id in PRIMITIVE_FAMILY_IDS
        if family_id not in excluded
    )


def fixture_cases() -> tuple[CompletionCase, ...]:
    cases: list[CompletionCase] = []

    for family_id in PRIMITIVE_FAMILY_IDS:
        is_predictive_or_operational = family_id in (
            *PHYSICAL_FAMILIES,
            *OPERATIONAL_FAMILIES,
        )
        cases.append(
            CompletionCase(
                case_id=f"single_{family_id}_absorber",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    family_id
                ),
                witnesses=(
                    _witness(
                        f"{family_id}_witness",
                        (family_id,),
                        predeclared=is_predictive_or_operational,
                        outcome_independent=is_predictive_or_operational,
                        physically_admissible=is_predictive_or_operational,
                    ),
                ),
            )
        )

    for omitted_family_id in PRIMITIVE_FAMILY_IDS:
        represented = tuple(
            family_id
            for family_id in PRIMITIVE_FAMILY_IDS
            if family_id != omitted_family_id
        )
        cases.append(
            CompletionCase(
                case_id=f"omitted_{omitted_family_id}",
                represented_family_ids=represented,
                verified_nonfactorization_family_ids=represented,
                witnesses=(),
            )
        )

    cases.extend(
        (
            CompletionCase(
                case_id="hybrid_stochastic_seed_plus_access",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    "stochastic_seed", "observer_information_access"
                ),
                witnesses=(
                    _witness(
                        "hybrid_seed_access_witness",
                        ("stochastic_seed", "observer_information_access"),
                    ),
                ),
            ),
            CompletionCase(
                case_id="unverified_whole_family_certificate",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    "whole_family"
                ),
                witnesses=(
                    _witness(
                        "unverified_whole_family_witness",
                        ("whole_family",),
                        predeclared=False,
                        outcome_independent=False,
                        physically_admissible=False,
                        certificate_verified=False,
                    ),
                ),
            ),
            CompletionCase(
                case_id="posthoc_fixed_source_model",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    "fixed_source"
                ),
                witnesses=(
                    _witness(
                        "posthoc_fixed_source_witness",
                        ("fixed_source",),
                        predeclared=False,
                        outcome_independent=False,
                    ),
                ),
            ),
            CompletionCase(
                case_id="bounded_survivor_control",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=PRIMITIVE_FAMILY_IDS,
                witnesses=(),
            ),
            CompletionCase(
                case_id="world_a_compatibility",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    "hidden_state", "fixed_source", "observer_information_access"
                ),
                witnesses=(
                    _witness(
                        "world_a_hidden_source_access_witness",
                        (
                            "hidden_state",
                            "fixed_source",
                            "observer_information_access",
                        ),
                    ),
                ),
            ),
            CompletionCase(
                case_id="world_b_compatibility",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=_nonfactorization_except(
                    "fixed_source", "whole_family"
                ),
                witnesses=(
                    _witness(
                        "world_b_fixed_family_witness",
                        ("fixed_source", "whole_family"),
                    ),
                ),
            ),
            CompletionCase(
                case_id="world_c_fail_closed",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=(),
                witnesses=(),
            ),
            CompletionCase(
                case_id="composition_closure_missing",
                represented_family_ids=PRIMITIVE_FAMILY_IDS,
                verified_nonfactorization_family_ids=PRIMITIVE_FAMILY_IDS,
                witnesses=(),
                composition_closure_declared=False,
            ),
        )
    )
    return tuple(cases)


def run_contract() -> dict[str, Any]:
    cases = fixture_cases()
    results = tuple(classify_case(case) for case in cases)
    by_id = {result["case_id"]: result for result in results}
    single_absorber_ids = tuple(
        f"single_{family_id}_absorber" for family_id in PRIMITIVE_FAMILY_IDS
    )
    omission_case_ids = tuple(
        f"omitted_{family_id}" for family_id in PRIMITIVE_FAMILY_IDS
    )
    verdicts = {result["case_id"]: result["verdict"] for result in results}

    return {
        "fixture_id": "completion_class_v1",
        "contract_version": "completion_class_v1",
        "primitive_family_ids": list(PRIMITIVE_FAMILY_IDS),
        "conclusion_classes": list(CONCLUSION_CLASSES),
        "family_to_conclusion": dict(FAMILY_TO_CONCLUSION),
        "composition_closure_required": True,
        "all_primitive_absorbers_exercised": all(
            verdicts[case_id] in CONCLUSION_CLASSES
            for case_id in single_absorber_ids
        ),
        "all_omission_mutants_fail_closed": all(
            verdicts[case_id] == INCOMPLETE_NULL_CLASS
            for case_id in omission_case_ids
        ),
        "hybrid_completion_exercised": (
            verdicts["hybrid_stochastic_seed_plus_access"]
            == PHYSICAL_PREDICTIVE_ABSORPTION
        ),
        "unverified_certificate_fails_closed": (
            verdicts["unverified_whole_family_certificate"]
            == INCOMPLETE_NULL_CLASS
        ),
        "posthoc_predictive_model_fails_closed": (
            verdicts["posthoc_fixed_source_model"] == INCOMPLETE_NULL_CLASS
        ),
        "bounded_survivor_is_not_issuance": (
            verdicts["bounded_survivor_control"]
            == SURVIVES_BOUNDED_COMPLETION_CLASS
        ),
        "world_a": verdicts["world_a_compatibility"],
        "world_b": verdicts["world_b_compatibility"],
        "world_c": verdicts["world_c_fail_closed"],
        "e177_modified": False,
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "claim_status_change": "none",
        "case_verdicts": verdicts,
        "honest_current_result": (
            "CompletionClass v1 covers the eleven declared primitive null "
            "families and their declared compositions in a bounded executable "
            "contract. It does not prove the inventory physically exhaustive, "
            "verify domain-specific nonfactorization theorems, or establish "
            "physical source issuance."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/completion_class_v1_result.json"),
    )
    args = parser.parse_args()
    result = run_contract()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
