#!/usr/bin/env python3
"""Toy fixture for the holonomy transport-functor derivation question.

The fixture is deliberately narrow. It asks whether a finite C-typed
admissibility fragment supplies enough data to derive a transport functor
``A: ExtCat -> B Z/2``. It is not a physics theorem and it does not move claim
status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DERIVED_NONTRIVIAL_TRANSPORT = "DERIVED_NONTRIVIAL_TRANSPORT"
TRIVIAL_TRANSPORT_ONLY = "TRIVIAL_TRANSPORT_ONLY"
NOT_DERIVABLE_BARE_LOOP = "NOT_DERIVABLE_BARE_LOOP"
IMPORTED_TRANSPORT_REJECTION = "IMPORTED_TRANSPORT_REJECTION"
BLOCKED_INCONSISTENT_TRANSPORT = "BLOCKED_INCONSISTENT_TRANSPORT"


@dataclass(frozen=True)
class Edge:
    edge_id: str
    source: str
    target: str
    admissible: bool
    c_delta: int | None = None
    imported_transport: int | None = None


@dataclass(frozen=True)
class Composition:
    first: str
    second: str
    composite: str


@dataclass(frozen=True)
class FixtureCase:
    case_id: str
    description: str
    edges: tuple[Edge, ...]
    compositions: tuple[Composition, ...]
    loop_word: tuple[str, ...]
    derivation_rule: str


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    verdict: str
    derived_transport: bool
    nontrivial_loop_holonomy: bool
    imported_transport_used: bool
    loop_holonomy_z2: int | None
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "verdict": self.verdict,
            "derived_transport": self.derived_transport,
            "nontrivial_loop_holonomy": self.nontrivial_loop_holonomy,
            "imported_transport_used": self.imported_transport_used,
            "loop_holonomy_z2": self.loop_holonomy_z2,
            "reason": self.reason,
        }


def add_z2(*values: int) -> int:
    return sum(values) % 2


def edge_index(case: FixtureCase) -> dict[str, Edge]:
    return {edge.edge_id: edge for edge in case.edges}


def derive_labels(case: FixtureCase) -> tuple[dict[str, int] | None, str | None]:
    edges = edge_index(case)
    if any(not edge.admissible for edge in edges.values()):
        return None, "case contains a non-admissible edge"

    if case.derivation_rule == "none":
        return None, None

    if case.derivation_rule == "identity_only":
        return {edge_id: 0 for edge_id in edges}, None

    if case.derivation_rule == "c_delta_z2":
        if any(edge.c_delta is None for edge in edges.values()):
            return None, "c_delta_z2 rule needs every admissible edge to carry c_delta"
        return {edge_id: edge.c_delta % 2 for edge_id, edge in edges.items()}, None

    if case.derivation_rule == "imported_table":
        if any(edge.imported_transport is None for edge in edges.values()):
            return None, "imported_table needs every edge to carry imported_transport"
        return {
            edge_id: edge.imported_transport % 2
            for edge_id, edge in edges.items()
        }, None

    return None, f"unknown derivation rule: {case.derivation_rule}"


def composition_errors(case: FixtureCase, labels: dict[str, int]) -> list[str]:
    errors: list[str] = []
    for composition in case.compositions:
        expected = add_z2(labels[composition.first], labels[composition.second])
        actual = labels[composition.composite]
        if expected != actual:
            errors.append(
                f"{composition.first}+{composition.second}->{composition.composite} "
                f"expects {expected}, got {actual}"
            )
    return errors


def loop_holonomy(case: FixtureCase, labels: dict[str, int]) -> int:
    return add_z2(*(labels[edge_id] for edge_id in case.loop_word))


def evaluate_case(case: FixtureCase) -> CaseResult:
    labels, label_error = derive_labels(case)

    if case.derivation_rule == "none":
        return CaseResult(
            case_id=case.case_id,
            verdict=NOT_DERIVABLE_BARE_LOOP,
            derived_transport=False,
            nontrivial_loop_holonomy=False,
            imported_transport_used=False,
            loop_holonomy_z2=None,
            reason=(
                "A bare admissible loop supplies a loop word, but no canonical "
                "group value or transport functor."
            ),
        )

    if case.derivation_rule == "imported_table":
        if labels is None:
            return CaseResult(
                case_id=case.case_id,
                verdict=BLOCKED_INCONSISTENT_TRANSPORT,
                derived_transport=False,
                nontrivial_loop_holonomy=False,
                imported_transport_used=True,
                loop_holonomy_z2=None,
                reason=label_error or "imported transport table is incomplete",
            )
        errors = composition_errors(case, labels)
        if errors:
            return CaseResult(
                case_id=case.case_id,
                verdict=BLOCKED_INCONSISTENT_TRANSPORT,
                derived_transport=False,
                nontrivial_loop_holonomy=False,
                imported_transport_used=True,
                loop_holonomy_z2=None,
                reason="; ".join(errors),
            )
        holonomy = loop_holonomy(case, labels)
        return CaseResult(
            case_id=case.case_id,
            verdict=IMPORTED_TRANSPORT_REJECTION,
            derived_transport=False,
            nontrivial_loop_holonomy=holonomy == 1,
            imported_transport_used=True,
            loop_holonomy_z2=holonomy,
            reason=(
                "A functor exists only because a transport table is supplied as "
                "extra data, so this does not derive A from C-typed admissibility."
            ),
        )

    if labels is None:
        return CaseResult(
            case_id=case.case_id,
            verdict=BLOCKED_INCONSISTENT_TRANSPORT,
            derived_transport=False,
            nontrivial_loop_holonomy=False,
            imported_transport_used=False,
            loop_holonomy_z2=None,
            reason=label_error or "no labels could be derived",
        )

    errors = composition_errors(case, labels)
    if errors:
        return CaseResult(
            case_id=case.case_id,
            verdict=BLOCKED_INCONSISTENT_TRANSPORT,
            derived_transport=False,
            nontrivial_loop_holonomy=False,
            imported_transport_used=False,
            loop_holonomy_z2=None,
            reason="; ".join(errors),
        )

    holonomy = loop_holonomy(case, labels)
    if holonomy == 1:
        return CaseResult(
            case_id=case.case_id,
            verdict=DERIVED_NONTRIVIAL_TRANSPORT,
            derived_transport=True,
            nontrivial_loop_holonomy=True,
            imported_transport_used=False,
            loop_holonomy_z2=holonomy,
            reason=(
                "The toy C-typed admissibility labels are additive under "
                "composition and derive a nontrivial Z/2 loop value."
            ),
        )

    return CaseResult(
        case_id=case.case_id,
        verdict=TRIVIAL_TRANSPORT_ONLY,
        derived_transport=True,
        nontrivial_loop_holonomy=False,
        imported_transport_used=False,
        loop_holonomy_z2=holonomy,
        reason=(
            "A transport functor is derived, but the only loop value is the "
            "identity. This does not reopen the holonomy route."
        ),
    )


def fixture_cases() -> list[FixtureCase]:
    return [
        FixtureCase(
            case_id="bare_loop_word",
            description="Two admissible edges form a loop word but carry no group data.",
            edges=(
                Edge("ab", "A", "B", admissible=True),
                Edge("ba", "B", "A", admissible=True),
                Edge("aa", "A", "A", admissible=True),
            ),
            compositions=(Composition("ab", "ba", "aa"),),
            loop_word=("ab", "ba"),
            derivation_rule="none",
        ),
        FixtureCase(
            case_id="identity_forced_consistency",
            description="Consistency forces every edge to the identity element.",
            edges=(
                Edge("ab", "A", "B", admissible=True),
                Edge("ba", "B", "A", admissible=True),
                Edge("aa", "A", "A", admissible=True),
            ),
            compositions=(Composition("ab", "ba", "aa"),),
            loop_word=("ab", "ba"),
            derivation_rule="identity_only",
        ),
        FixtureCase(
            case_id="c_typed_parity_rule",
            description=(
                "C-typed admissibility carries an additive parity delta, giving "
                "a source-side rule for A rather than an imported table."
            ),
            edges=(
                Edge("ab", "A", "B", admissible=True, c_delta=1),
                Edge("ba", "B", "A", admissible=True, c_delta=0),
                Edge("aa", "A", "A", admissible=True, c_delta=1),
            ),
            compositions=(Composition("ab", "ba", "aa"),),
            loop_word=("ab", "ba"),
            derivation_rule="c_delta_z2",
        ),
        FixtureCase(
            case_id="imported_transport_table",
            description="A nontrivial transport table is supplied from outside C.",
            edges=(
                Edge("ab", "A", "B", admissible=True, imported_transport=1),
                Edge("ba", "B", "A", admissible=True, imported_transport=0),
                Edge("aa", "A", "A", admissible=True, imported_transport=1),
            ),
            compositions=(Composition("ab", "ba", "aa"),),
            loop_word=("ab", "ba"),
            derivation_rule="imported_table",
        ),
        FixtureCase(
            case_id="inconsistent_c_typed_labels",
            description="C labels are present but do not respect composition.",
            edges=(
                Edge("ab", "A", "B", admissible=True, c_delta=1),
                Edge("ba", "B", "A", admissible=True, c_delta=1),
                Edge("aa", "A", "A", admissible=True, c_delta=1),
            ),
            compositions=(Composition("ab", "ba", "aa"),),
            loop_word=("ab", "ba"),
            derivation_rule="c_delta_z2",
        ),
    ]


def run_fixture() -> dict[str, Any]:
    results = [evaluate_case(case) for case in fixture_cases()]
    by_id = {result.case_id: result for result in results}
    verdicts = sorted({result.verdict for result in results})
    return {
        "fixture_id": "holonomy_transport_functor_derivation_fixture",
        "kind": "bounded_toy_fixture_not_claim_movement",
        "claim_status_change": "none",
        "active_trigger_change": "none",
        "central_question": (
            "Does C-typed admissibility derive A: ExtCat -> B Z/2, or is "
            "transport extra data?"
        ),
        "verdicts_seen": verdicts,
        "bare_loop_derives_transport": by_id["bare_loop_word"].derived_transport,
        "imported_table_counts_as_derivation": by_id[
            "imported_transport_table"
        ].derived_transport,
        "source_rule_positive_shape_found": by_id[
            "c_typed_parity_rule"
        ].nontrivial_loop_holonomy,
        "honest_current_result": (
            "Bare loop data still does not derive holonomy. The toy positive "
            "shape requires an explicit admissibility-carried additive label rule; "
            "without that rule, transport is either trivial, imported, or inconsistent."
        ),
        "cases": [result.as_dict() for result in results],
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "tests/artifacts/"
            "holonomy_transport_functor_derivation_fixture_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
