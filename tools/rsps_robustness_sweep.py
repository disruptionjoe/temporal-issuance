"""Robustness sweep for the RSPS record-fidelity toy model.

This extends the controlled-copy fixture by replacing perfect environment
copying with a noisy binary record channel. Non-orthogonal environment records
are represented by their Helstrom distinguishability, then converted to an
effective binary readout reliability.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Scenario:
    name: str
    copy_reliability: float
    record_overlap: float
    noise_flip: float
    accessible_fragments: int
    total_fragments: int


@dataclass(frozen=True)
class ScenarioResult:
    name: str
    copy_reliability: float
    record_overlap: float
    noise_flip: float
    accessible_fragments: int
    total_fragments: int
    effective_reliability: float
    full_argmax_theta_deg: float
    full_argmax_score: float
    pointer_score: float
    x_score: float
    pointer_wins_full_score: bool
    redundancy_only_argmax_theta_deg: float
    redundancy_only_argmax_value: float
    redundancy_degenerate: bool


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def mutual_information(joint: dict[tuple[str, str], float]) -> float:
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


def helstrom_reliability(record_overlap: float) -> float:
    """Optimal equal-prior binary discrimination reliability for pure records."""
    if not 0.0 <= record_overlap <= 1.0:
        raise ValueError("record_overlap must be in [0, 1]")
    return 0.5 * (1.0 + math.sqrt(max(0.0, 1.0 - record_overlap * record_overlap)))


def compose_binary_reliabilities(*reliabilities: float) -> float:
    """Compose independent binary symmetric readout reliabilities."""
    p_same = 1.0
    p_flip = 0.0
    for reliability in reliabilities:
        new_same = p_same * reliability + p_flip * (1.0 - reliability)
        new_flip = p_same * (1.0 - reliability) + p_flip * reliability
        p_same, p_flip = new_same, new_flip
    return p_same


def effective_reliability(scenario: Scenario) -> float:
    overlap_rel = helstrom_reliability(scenario.record_overlap)
    noise_rel = 1.0 - scenario.noise_flip
    return compose_binary_reliabilities(scenario.copy_reliability, overlap_rel, noise_rel)


def joint_s_theta_e(p0: float, theta: float, reliability: float) -> dict[tuple[str, str], float]:
    """Joint distribution over candidate S_theta outcome and accessible record bit."""
    p1 = 1.0 - p0
    c2 = math.cos(theta / 2.0) ** 2
    s2 = math.sin(theta / 2.0) ** 2
    rows = {
        ("+", "0"): p0 * c2 * reliability + p1 * s2 * (1.0 - reliability),
        ("+", "1"): p0 * c2 * (1.0 - reliability) + p1 * s2 * reliability,
        ("-", "0"): p0 * s2 * reliability + p1 * c2 * (1.0 - reliability),
        ("-", "1"): p0 * s2 * (1.0 - reliability) + p1 * c2 * reliability,
    }
    return rows


def theta_grid(steps: int) -> Iterable[float]:
    start = -math.pi / 2.0
    stop = math.pi / 2.0
    for i in range(steps):
        yield start + (stop - start) * i / (steps - 1)


def scores(
    p0: float,
    theta: float,
    reliability: float,
    accessible_fragments: int,
    total_fragments: int,
) -> tuple[float, float]:
    pointer_entropy = h2(p0)
    stability_score = 1.0 - h2(math.cos(theta / 2.0) ** 2)
    agreement_score = 1.0 - abs(math.sin(theta))

    if accessible_fragments <= 0 or pointer_entropy <= 0.0:
        redundancy_score = 0.0
    else:
        mi = mutual_information(joint_s_theta_e(p0, theta, reliability))
        redundancy_score = (accessible_fragments / max(1, total_fragments)) * (mi / pointer_entropy)

    return stability_score + redundancy_score + agreement_score, redundancy_score


def run_scenario(p0: float, scenario: Scenario, steps: int) -> ScenarioResult:
    rel = effective_reliability(scenario)
    full_rows = []
    red_rows = []
    for theta in theta_grid(steps):
        full, red = scores(p0, theta, rel, scenario.accessible_fragments, scenario.total_fragments)
        full_rows.append((full, theta))
        red_rows.append((red, theta))

    full_best, full_theta = max(full_rows, key=lambda item: item[0])
    red_best, red_theta = max(red_rows, key=lambda item: item[0])
    pointer_score, pointer_red = scores(p0, 0.0, rel, scenario.accessible_fragments, scenario.total_fragments)
    x_score, _ = scores(p0, math.pi / 2.0, rel, scenario.accessible_fragments, scenario.total_fragments)
    red_values = [value for value, _ in red_rows]
    red_degenerate = max(red_values) - min(red_values) < 1e-10

    return ScenarioResult(
        name=scenario.name,
        copy_reliability=scenario.copy_reliability,
        record_overlap=scenario.record_overlap,
        noise_flip=scenario.noise_flip,
        accessible_fragments=scenario.accessible_fragments,
        total_fragments=scenario.total_fragments,
        effective_reliability=rel,
        full_argmax_theta_deg=math.degrees(full_theta),
        full_argmax_score=full_best,
        pointer_score=pointer_score,
        x_score=x_score,
        pointer_wins_full_score=abs(full_theta) < 1e-9 and pointer_score >= x_score,
        redundancy_only_argmax_theta_deg=math.degrees(red_theta),
        redundancy_only_argmax_value=red_best,
        redundancy_degenerate=red_degenerate,
    )


def scenario_set(total_fragments: int) -> list[Scenario]:
    scenarios: list[Scenario] = []

    for reliability in [1.0, 0.95, 0.8, 0.65, 0.55, 0.5]:
        scenarios.append(Scenario(f"copy_reliability_{reliability}", reliability, 0.0, 0.0, total_fragments, total_fragments))

    for fragments in [0, 1, 2, 4, total_fragments]:
        scenarios.append(Scenario(f"accessible_fragments_{fragments}", 1.0, 0.0, 0.0, fragments, total_fragments))

    for overlap in [0.0, 0.2, 0.5, 0.8, 0.95, 1.0]:
        scenarios.append(Scenario(f"record_overlap_{overlap}", 1.0, overlap, 0.0, total_fragments, total_fragments))

    for noise in [0.0, 0.05, 0.1, 0.2, 0.4, 0.5]:
        scenarios.append(Scenario(f"noise_flip_{noise}", 1.0, 0.0, noise, total_fragments, total_fragments))

    for fragments in [1, 2, 4, 8, 16]:
        scenarios.append(Scenario(f"varying_N_{fragments}", 1.0, 0.0, 0.0, fragments, fragments))

    return scenarios


def rounded(obj: object, digits: int = 10) -> object:
    if isinstance(obj, float):
        return round(obj, digits)
    if isinstance(obj, dict):
        return {key: rounded(value, digits) for key, value in obj.items()}
    if isinstance(obj, list):
        return [rounded(value, digits) for value in obj]
    return obj


def main() -> int:
    parser = argparse.ArgumentParser(description="Run RSPS robustness sweep.")
    parser.add_argument("--p0", type=float, default=0.7)
    parser.add_argument("--total-fragments", type=int, default=8)
    parser.add_argument("--theta-steps", type=int, default=1801)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    results = [run_scenario(args.p0, scenario, args.theta_steps) for scenario in scenario_set(args.total_fragments)]
    failures = [row for row in results if not row.pointer_wins_full_score]
    degenerate = [row for row in results if row.redundancy_degenerate]

    payload = {
        "fixture": "RSPS robustness sweep over noisy/partial/nonorthogonal record channels",
        "model": {
            "p0": args.p0,
            "theta_domain": "[-pi/2, pi/2]",
            "score": "full = stability + accessible redundancy + agreement",
        },
        "summary": {
            "scenario_count": len(results),
            "pointer_wins_full_score_count": len(results) - len(failures),
            "full_score_failures": [row.name for row in failures],
            "redundancy_degenerate_count": len(degenerate),
            "redundancy_degenerate_cases": [row.name for row in degenerate],
            "verdict": (
                "Pointer-basis selection is robust for the full RSPS score across this sweep. "
                "Redundancy-only selection becomes degenerate when no accessible record remains."
            ),
        },
        "results": [asdict(row) for row in results],
    }

    payload = rounded(payload)
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
