"""de Sitter comoving-horizon mode-issuance Adapter_P fixture (TI-C020 big swing, RUN-0124).

This is a TOY DISCRIMINATOR, not a physics simulation. It asks whether "a comoving mode
crossing the de Sitter horizon and freezing into the cosmological record" is genuine source
issuance or fixed-source disclosure, by mapping the candidate onto the Adapter_P interface and
running the fixed-source null models.

Physical framing (informal):
  In de Sitter expansion a(t) = e^{Ht}, comoving modes exit the Hubble horizon; super-horizon
  modes freeze and, via decoherence, seed classical structure (the CMB / large-scale record).
  TI question: does the algebra of frozen-record observables GROW non-isomorphically (H_grow /
  Issue[S]), or is it a growing accessible SUBalgebra of a fixed global algebra on a fixed
  comoving lattice with a fixed decoherence law (H_fixed / disclosure)?

Two regimes are compared:
  * fixed_background  -- the physically standard case: fixed comoving lattice K_infty, the
                        horizon access threshold sweeps over it, frozen record modes Gamma_n
                        are a growing SUBSET of a fixed lattice.
  * generated_lattice -- a self-generating (Goedelian) background: the admissible mode label
                        formed at stage n+1 diagonalizes the stage-n present enumerator, so it
                        is fresh with respect to any fixed finite prefix completion.

Adapter_P fields (per RUN-0099 / FORMAL-OBJECT.md):
  Gamma_n   frozen cosmological record at e-fold n
  Adm_n     admissibility predicate: a mode is issuable at n iff it crosses the horizon in [n, n+1)
  e_n       the crossing/freezing event
  w_n       witness that the mode was sub-horizon (unrecorded) at n and super-horizon (frozen) at n+1
  Gamma_n+1 record after admission
  tau_n     the frozen amplitude (structure seed) record trace
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


STAGES = 8  # e-folds modeled
LATTICE_SIZE = 32  # fixed comoving lattice size for the fixed-background regime


# --------------------------------------------------------------------------------------
# Regime 1: fixed_background (standard de Sitter QFT on a fixed comoving lattice)
# --------------------------------------------------------------------------------------

def fixed_lattice() -> list[int]:
    return list(range(1, LATTICE_SIZE + 1))


def k_cross(n: int) -> int:
    """Comoving horizon threshold at e-fold n (grows: more modes frozen with expansion)."""
    return 2 * (n + 1)


def fixed_gamma(n: int) -> set[int]:
    """Frozen record modes at stage n: a growing SUBSET of the fixed lattice."""
    return {k for k in fixed_lattice() if k <= k_cross(n)}


def fixed_background_report() -> dict[str, object]:
    lattice = set(fixed_lattice())
    gammas = [fixed_gamma(n) for n in range(STAGES)]

    # Fixed completion exists: every frozen record set is contained in the fixed lattice.
    all_subsets_of_fixed = all(g <= lattice for g in gammas)

    # Perturbation W4: change H -> reschedule k_cross. The record still factors through the
    # same fixed lattice under a different access schedule (no new algebra element appears).
    def k_cross_perturbed(n: int) -> int:
        return 3 * (n + 1)  # different H

    perturbed_gammas = [{k for k in lattice if k <= k_cross_perturbed(n)} for n in range(STAGES)]
    perturbation_factors_through_fixed = all(g <= lattice for g in perturbed_gammas)

    w = {
        "W1_non_isomorphic_algebra_growth": False,   # record algebra embeds in fixed A_infty
        "W2_prefix_formed_admissibility": False,      # k<=k_cross(n): fixed fn of a pre-given lattice
        "W3_construction_provenance": False,          # modes revealed by access, not constructed
        "W4_perturbation_non_factorization": not perturbation_factors_through_fixed,  # False
        "W5_record_preservation": True,               # super-horizon freezing preserves the record
        "W6_gauge_access_language_non_absorption": False,  # comoving/gauge relabeling absorbs it
    }

    nulls = {
        "fixed_H_infty": all_subsets_of_fixed,                 # absorbs
        "fixed_A_infty": all_subsets_of_fixed,                 # absorbs
        "bounded_access_to_Mu_infty": True,                    # fixed lattice = fixed index set
        "fixed_stochastic_or_collapse_law": True,              # freeze/decohere is a fixed law
        "fixed_boundary_or_holographic_completion": True,      # fixed global state pre-contains it
        "experimenter_added_schema": False,                    # n/a here
    }

    absorbed = (not any(v for k, v in w.items() if k != "W5_record_preservation")) and \
        all(nulls[k] for k in (
            "fixed_H_infty", "bounded_access_to_Mu_infty", "fixed_stochastic_or_collapse_law"))

    return {
        "regime": "fixed_background",
        "all_frozen_sets_subset_of_fixed_lattice": all_subsets_of_fixed,
        "perturbation_factors_through_fixed": perturbation_factors_through_fixed,
        "W_gate": w,
        "fixed_source_nulls_absorb": nulls,
        "verdict": "absorbed_as_fixed_source_disclosure" if absorbed else "not_absorbed",
    }


# --------------------------------------------------------------------------------------
# Regime 2: generated_lattice (self-generating / Goedelian background)
# --------------------------------------------------------------------------------------

def menu(n: int, width: int = 6) -> list[str]:
    """Labels 'reachable' from the stage-n context menu (NOT the diagonal)."""
    return [f"m{n}_{j}" for j in range(width)]


def diagonal_label(enumerated: list[str]) -> str:
    """Construct a label guaranteed NOT in `enumerated` (genuine diagonalization)."""
    existing = set(enumerated)
    i = 0
    candidate = f"d|{len(enumerated)}"
    while candidate in existing:
        i += 1
        candidate = f"d|{len(enumerated)}|{i}"
    return candidate


def generated_run() -> dict[str, object]:
    issued: list[str] = []          # diagonal labels issued so far (the record)
    enumerators: list[list[str]] = []
    for n in range(STAGES):
        # present enumerator at n: this stage's menu + all prior menus + all prior issued labels
        present = list(issued)
        for k in range(n + 1):
            present.extend(menu(k))
        enumerators.append(present)
        issued.append(diagonal_label(present))
    return {"issued": issued, "enumerators": enumerators}


def generated_lattice_report() -> dict[str, object]:
    run = generated_run()
    issued = run["issued"]
    enumerators = run["enumerators"]

    # Finite-prefix freshness: a fixed completion equal to the ENTIRE stage-P enumerated menu
    # still misses the stage-P diagonal label. Check every stage.
    finite_prefix_fresh = all(
        issued[n] not in set(enumerators[n]) for n in range(STAGES)
    )

    # Whole-family absorption (the OnlineIssuance^LC / E127 ceiling): a singleton enumerator that
    # simply lists the realized diagonal sequence absorbs the whole family AFTER THE FACT.
    singleton_enumerator = set(issued)
    whole_family_absorbed = all(lbl in singleton_enumerator for lbl in issued)

    # No fixed FINITE lattice chosen at stage 0 pre-contains all issued labels:
    fixed_stage0_completion = set(menu(0))
    no_fixed_finite_precontainment = not set(issued) <= fixed_stage0_completion

    w = {
        "W1_non_isomorphic_algebra_growth": "class_relative",  # finite-prefix yes; absolute no
        "W2_prefix_formed_admissibility": True,                # admissibility formed at prefix (Adm_n)
        "W3_construction_provenance": True,                    # diagonal construction provenance
        "W4_perturbation_non_factorization": "inherits_ceiling",  # not an independent physical W4
        "W5_record_preservation": True,
        "W6_gauge_access_language_non_absorption": "partial",  # freshness not pure gauge, but exposed
    }

    nulls = {
        "fixed_H_infty_finite_prefix": not finite_prefix_fresh,  # False: does NOT absorb finite prefix
        "fixed_H_infty_whole_family_singleton": whole_family_absorbed,  # True: absorbs after the fact
        "bounded_access_to_Mu_infty_fixed_finite": not no_fixed_finite_precontainment,  # False
    }

    return {
        "regime": "generated_lattice",
        "finite_prefix_freshness_survives": finite_prefix_fresh,
        "whole_family_absorbed_by_singleton": whole_family_absorbed,
        "no_fixed_finite_precontainment": no_fixed_finite_precontainment,
        "W_gate": w,
        "fixed_source_nulls": nulls,
        "verdict": "reduces_to_OnlineIssuance_LC_class_relative_residue",
    }


# --------------------------------------------------------------------------------------
# Top-level
# --------------------------------------------------------------------------------------

def run_fixture() -> dict[str, object]:
    fixed = fixed_background_report()
    generated = generated_lattice_report()

    # The candidate reopens TI-C020 only if the physically-standard fixed-background regime
    # yields a genuine (non-class-relative, non-gauge) W1 witness. It does not.
    ti_c020_reopened = (fixed["verdict"] != "absorbed_as_fixed_source_disclosure")

    # New physical surplus over the formal residue: only if the generated regime gives an
    # ABSOLUTE (whole-family) escape that the formal OnlineIssuance^LC leg does not already have.
    generated_gives_absolute_escape = not generated["whole_family_absorbed_by_singleton"]

    return {
        "fixture": "desitter_comoving_horizon_mode_issuance",
        "kind": "toy_adapter_p_discriminator_not_physics_simulation",
        "stages": STAGES,
        "fixed_background": fixed,
        "generated_lattice": generated,
        "summary": {
            "fixed_background_regime": fixed["verdict"],
            "generated_lattice_regime": generated["verdict"],
            "new_physical_surplus_over_formal_residue": generated_gives_absolute_escape,
            "physical_question_separable_from_D_FORK": generated_gives_absolute_escape,
            "Issue[S]^physical": False,
            "TI_C020_reopened": ti_c020_reopened,
            "claim_status_change": "none",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=str(Path(__file__).resolve().parents[1]
                    / "tests" / "artifacts"
                    / "desitter_horizon_mode_issuance_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
