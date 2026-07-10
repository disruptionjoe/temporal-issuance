#!/usr/bin/env python3
"""FUNCTOR-OBL-001: N naturality obligation.

Discharges the open obligation from E031 Part V item 2: is the novelty rate
N(S) = |D4-Hom(S)| / |Hom(S)| a natural transformation over Ext_S, or only a
pointwise function?

This is a small combinatorial fixture, not a physics claim. It works with a tiny
explicit Ext_S diagram, computes the one-step novelty ratio N at two states linked
by a morphism e: S -> S', and checks:

  (1) STRICT NATURALITY: whether the D4 (type-novelty) predicate is preserved along
      e (a necessary condition for any transport law that makes N natural). It is not,
      because type-novelty is state-relative: a type that is novel relative to S becomes
      non-novel relative to S' once e has introduced it. This is exhibited concretely.

  (2) GAUGE NATURALITY (positive residue): whether N is invariant under type-name
      relabelings (the schema-relabeling covariance of E049 / GAUGE-COV-OBL-001).
      N is gauge-natural even though it is not extension-natural.

The honest verdict: N is NOT a strict natural transformation over Ext_S. The obstruction
is state-relative type-novelty -- the same non-preservation that powers the Godelian
mechanism (E042) and D-FORK. A strictly natural novelty rate would mean novelty is a
fixed global invariant, i.e. the fixed-source / disclosure picture. So the non-naturality
of N is the categorical fingerprint that separates issuance from disclosure.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Constraint:
    """A typed constraint label c = (type, index)."""

    ctype: str
    index: int


@dataclass(frozen=True)
class State:
    """An Ext_S object: a typed source-constraint state S = (T_S, A_S).

    Here A_S is left implicit (downward-closed) because the naturality question is
    about the type schema T_S and the D4 predicate, not about the admissibility lattice.
    """

    name: str
    labels: frozenset[Constraint]

    def types(self) -> frozenset[str]:
        return frozenset(c.ctype for c in self.labels)


@dataclass(frozen=True)
class Extension:
    """A one-step Ext_S morphism e: S -> S' adding exactly one new constraint c_e."""

    source: State
    added: Constraint

    def target(self) -> State:
        return State(
            name=f"{self.source.name}+{self.added.ctype}{self.added.index}",
            labels=self.source.labels | {self.added},
        )

    def is_d4(self) -> bool:
        """Type-novel (D4) iff the added type is not present in the source schema."""
        return self.added.ctype not in self.source.types()


def one_step_menu(state: State, candidate_types: list[str], index_span: int) -> list[Extension]:
    """The one-step Hom-menu departing `state`: all admissible single-constraint adds.

    We enumerate, for each candidate type, a bounded family of fresh indices not already
    present. This is the finite local restriction E031 I.1 explicitly permits.
    """
    present = state.labels
    menu: list[Extension] = []
    for ctype in candidate_types:
        for idx in range(index_span):
            c = Constraint(ctype, idx)
            if c not in present:
                menu.append(Extension(source=state, added=c))
    return menu


def novelty_rate(state: State, candidate_types: list[str], index_span: int) -> dict[str, Any]:
    """N(S) = |D4-Hom(S)| / |Hom(S)| over the one-step menu."""
    menu = one_step_menu(state, candidate_types, index_span)
    d4 = [e for e in menu if e.is_d4()]
    total = len(menu)
    n_value = (len(d4) / total) if total else 0.0
    return {
        "state": state.name,
        "hom_count": total,
        "d4_hom_count": len(d4),
        "N": n_value,
        "present_types": sorted(state.types()),
    }


def relabel(state: State, renaming: dict[str, str]) -> State:
    """Apply a type-name bijection to a state (E049 gauge action)."""
    return State(
        name=state.name + "~relabel",
        labels=frozenset(
            Constraint(renaming.get(c.ctype, c.ctype), c.index) for c in state.labels
        ),
    )


def run_fixture() -> dict[str, Any]:
    candidate_types = ["alpha", "beta", "gamma"]
    index_span = 3

    # Base state S has one constraint of type alpha.
    s = State(name="S", labels=frozenset({Constraint("alpha", 0)}))

    # Two distinct morphisms departing S:
    #   e_beta introduces a genuinely novel type beta (D4 = true at S).
    #   e_alpha refines within the existing alpha type (D4 = false at S).
    e_beta = Extension(source=s, added=Constraint("beta", 0))
    e_alpha = Extension(source=s, added=Constraint("alpha", 1))
    s_prime = e_beta.target()  # S' now contains alpha and beta.

    # --- (1) Strict naturality obstruction: D4 predicate is not preserved along e_beta.
    # The "add a beta-typed constraint" move is D4 at S (beta novel) but NOT D4 at S'
    # (beta already present in S'). So the very predicate defining N's numerator flips
    # along the morphism -> no transport law Phi_e can make the numerator natural.
    beta_move_at_s = Extension(source=s, added=Constraint("beta", 1)).is_d4()
    beta_move_at_s_prime = Extension(source=s_prime, added=Constraint("beta", 1)).is_d4()
    d4_predicate_preserved = beta_move_at_s == beta_move_at_s_prime

    n_at_s = novelty_rate(s, candidate_types, index_span)
    n_at_s_prime = novelty_rate(s_prime, candidate_types, index_span)

    # Two morphisms out of S land in states with different novelty rates, and there is
    # no single number Phi_e(N(S)) that both targets share -> the naturality square is
    # ill-posed (N is state-indexed, not a transformation of a fixed diagram).
    n_after_e_beta = novelty_rate(e_beta.target(), candidate_types, index_span)["N"]
    n_after_e_alpha = novelty_rate(e_alpha.target(), candidate_types, index_span)["N"]
    transport_is_well_defined = n_after_e_beta == n_after_e_alpha  # expected False

    strict_naturality_holds = d4_predicate_preserved and transport_is_well_defined

    # --- (2) Gauge naturality (positive residue): N is invariant under type relabeling.
    renaming = {"alpha": "gamma", "beta": "alpha", "gamma": "beta"}
    s_relabeled = relabel(s, renaming)
    # Relabel the candidate-type universe consistently so the menu is the gauge image.
    relabeled_types = [renaming[t] for t in candidate_types]
    n_relabeled = novelty_rate(s_relabeled, relabeled_types, index_span)["N"]
    gauge_natural = abs(n_relabeled - n_at_s["N"]) < 1e-12

    verdict = {
        "fixture_id": "functor_obl_001_n_naturality",
        "obligation": "FUNCTOR-OBL-001 (N naturality, E031 Part V item 2)",
        "kind": "combinatorial_categorical_fixture_not_physics_theorem",
        "claim_status_change": "none",
        "strict_naturality": {
            "d4_predicate_preserved_along_morphism": d4_predicate_preserved,
            "beta_move_is_d4_at_S": beta_move_at_s,
            "beta_move_is_d4_at_S_prime": beta_move_at_s_prime,
            "transport_law_well_defined": transport_is_well_defined,
            "N_after_e_beta": n_after_e_beta,
            "N_after_e_alpha": n_after_e_alpha,
            "holds": strict_naturality_holds,
        },
        "gauge_naturality": {
            "N_at_S": n_at_s["N"],
            "N_at_relabeled_S": n_relabeled,
            "holds": gauge_natural,
        },
        "N_samples": {"S": n_at_s, "S_prime": n_at_s_prime},
        "verdict": (
            "N is NOT a strict natural transformation over Ext_S. The obstruction is "
            "state-relative type-novelty: the D4 predicate defining N's numerator is not "
            "preserved along extension morphisms (a type novel at S is non-novel at S'). "
            "N IS gauge-natural (invariant under type-name relabeling, E049). The "
            "non-naturality is the categorical signature of issuance vs disclosure: a "
            "strictly natural novelty rate would make novelty a fixed global invariant, "
            "i.e. the fixed-source picture."
        ),
        "obligation_discharged": True,
        "resolution": "negative_for_strict_naturality_positive_for_gauge_naturality",
        "ties_to": ["TI-C019", "D-FORK (E042)", "GAUGE-COV-OBL-001 (E049)"],
    }
    return verdict


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/functor_obl_001_n_naturality_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
