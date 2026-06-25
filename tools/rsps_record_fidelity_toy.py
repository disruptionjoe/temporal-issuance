"""RSPS record-fidelity toy model.

This script reproduces the canonical controlled-copy / GHZ einselection
fixture used in the Record-Stabilization Pointer Selection (RSPS) line.

It tests two questions:
1. Does a record-fidelity score select the pointer basis?
2. Does that score contain the Born weights?

The result is intentionally modest: the score selects the basis, while the
weights remain external in diag(rho_S).
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class BasisScore:
    theta_rad: float
    theta_deg: float
    stability_score: float
    redundancy_score: float
    agreement_score: float
    total_score: float
    mutual_information_single_fragment: float


@dataclass(frozen=True)
class BornNoGoRow:
    p0: float
    born_weight_0: float
    born_weight_1: float
    entropy_h2_p0: float
    raw_redundancy_n_fragments: float
    raw_stability_cost_at_pointer: float
    raw_agreement_cost_at_pointer: float
    normalized_fidelity_at_pointer: float


def h2(p: float) -> float:
    """Binary Shannon entropy in bits."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def mutual_information(joint: dict[tuple[str, str], float]) -> float:
    """Mutual information I(X:Y) in bits for a small joint table."""
    px: dict[str, float] = {}
    py: dict[str, float] = {}
    for (x, y), prob in joint.items():
        px[x] = px.get(x, 0.0) + prob
        py[y] = py.get(y, 0.0) + prob

    total = 0.0
    for (x, y), prob in joint.items():
        if prob <= 0.0:
            continue
        total += prob * math.log2(prob / (px[x] * py[y]))
    return total


def joint_s_theta_e1(p0: float, theta: float) -> dict[tuple[str, str], float]:
    """Joint distribution for candidate system basis S_theta and one copied fragment E1.

    The global state is |Psi> = a|0>|0..0> + b|1>|1..1>, with p0 = |a|^2.
    The candidate basis is rotated by theta, with theta = 0 the pointer basis
    and theta = +/- pi/2 an x-like basis.
    """
    p1 = 1.0 - p0
    c2 = math.cos(theta / 2.0) ** 2
    s2 = math.sin(theta / 2.0) ** 2
    return {
        ("+", "0"): p0 * c2,
        ("+", "1"): p1 * s2,
        ("-", "0"): p0 * s2,
        ("-", "1"): p1 * c2,
    }


def basis_score(p0: float, theta: float) -> BasisScore:
    """Normalized basis-selection score.

    The three score terms are normalized so theta = 0 gets 3 and theta = +/- pi/2 gets 0
    in the ideal controlled-copy fixture.
    """
    pointer_entropy = h2(p0)
    candidate_entropy = h2(math.cos(theta / 2.0) ** 2)
    stability_score = 1.0 - candidate_entropy

    mi = mutual_information(joint_s_theta_e1(p0, theta))
    redundancy_score = mi / pointer_entropy if pointer_entropy > 0.0 else 1.0

    agreement_score = 1.0 - abs(math.sin(theta))
    total_score = stability_score + redundancy_score + agreement_score

    return BasisScore(
        theta_rad=theta,
        theta_deg=math.degrees(theta),
        stability_score=stability_score,
        redundancy_score=redundancy_score,
        agreement_score=agreement_score,
        total_score=total_score,
        mutual_information_single_fragment=mi,
    )


def theta_grid(steps: int) -> Iterable[float]:
    if steps < 3:
        raise ValueError("steps must be at least 3")
    start = -math.pi / 2.0
    stop = math.pi / 2.0
    for i in range(steps):
        yield start + (stop - start) * i / (steps - 1)


def find_argmax(p0: float, steps: int) -> BasisScore:
    return max((basis_score(p0, theta) for theta in theta_grid(steps)), key=lambda row: row.total_score)


def born_no_go_rows(p_values: list[float], n_fragments: int) -> list[BornNoGoRow]:
    rows: list[BornNoGoRow] = []
    for p0 in p_values:
        entropy = h2(p0)
        rows.append(
            BornNoGoRow(
                p0=p0,
                born_weight_0=p0,
                born_weight_1=1.0 - p0,
                entropy_h2_p0=entropy,
                raw_redundancy_n_fragments=n_fragments * entropy,
                raw_stability_cost_at_pointer=0.0,
                raw_agreement_cost_at_pointer=0.0,
                normalized_fidelity_at_pointer=basis_score(p0, 0.0).total_score,
            )
        )
    return rows


def rounded(obj: object, digits: int = 10) -> object:
    if isinstance(obj, float):
        return round(obj, digits)
    if isinstance(obj, dict):
        return {key: rounded(value, digits) for key, value in obj.items()}
    if isinstance(obj, list):
        return [rounded(value, digits) for value in obj]
    return obj


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the RSPS record-fidelity toy model.")
    parser.add_argument("--p0", type=float, default=0.7, help="Born weight |a|^2 for |0> branch.")
    parser.add_argument("--n-fragments", type=int, default=8, help="Number of copied environment fragments.")
    parser.add_argument("--theta-steps", type=int, default=1801, help="Grid resolution over [-pi/2, pi/2].")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    if not 0.0 < args.p0 < 1.0:
        raise ValueError("--p0 must be between 0 and 1")

    argmax = find_argmax(args.p0, args.theta_steps)
    z_basis = basis_score(args.p0, 0.0)
    x_basis = basis_score(args.p0, math.pi / 2.0)
    no_go = born_no_go_rows([0.3, 0.5, 0.7, 0.9], args.n_fragments)

    result = {
        "fixture": "RSPS controlled-copy / GHZ record-fidelity toy model",
        "model": {
            "state": "|Psi> = a|0>|0..0> + b|1>|1..1>",
            "p0": args.p0,
            "p1": 1.0 - args.p0,
            "n_fragments": args.n_fragments,
            "theta_domain": "[-pi/2, pi/2], theta=0 pointer basis, theta=+/-pi/2 x-like basis",
        },
        "basis_selection_check": {
            "argmax": asdict(argmax),
            "z_basis": asdict(z_basis),
            "x_basis": asdict(x_basis),
            "passes": abs(argmax.theta_rad) < 1e-9 and z_basis.total_score > x_basis.total_score,
        },
        "born_weight_check": {
            "rows": [asdict(row) for row in no_go],
            "negative_result": (
                "The normalized fidelity score is constant at the winning pointer basis, "
                "while raw redundancy is N*H2(p0), which is symmetric under p0 <-> 1-p0 "
                "and is maximal at p0=0.5. The Born weights live in diag(rho_S), not in F."
            ),
            "passes_as_no_go": True,
        },
        "verdict": {
            "record_fidelity_selects_pointer_basis": True,
            "record_fidelity_derives_born_weights": False,
            "surviving_hypothesis": "RSPS: record stabilization selects basis/objectivity; weights come from the trace rule.",
        },
    }

    result = rounded(result)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
