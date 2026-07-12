"""Temporal Issuance attention priority.

This is the ranking engine for the repo-local research-steering card.

When Joe says he has attention for Temporal Issuance, the assistant should run
this script and hand back the top few ranked items with one-line reasons.

Ranking rule:
- ITEMS is the current open hypothesis or next-move set.
- BALLOTS is the standing inline council vote. Each ballot is a strict order,
  best first, over every item.
- Item X beats item Y when a majority of personas prefer X to Y.
- If the majority graph is acyclic, use that Condorcet order.
- If there is a cycle, fall back to Copeland score, pairwise wins minus losses.
- Ties are broken by average ballot position, then item id.

Re-ranking means editing ITEMS and BALLOTS, then running:

    python attention/priority_condorcet.py
"""
from __future__ import annotations

from collections import defaultdict, deque
from itertools import combinations


ITEMS = {
    "H2": {
        "title": "Pre-action family noncompletion source-action generator",
        "why": "Builds the OSAG rule the H1 classifier identified as the only non-absorbed escape shape.",
    },
    "H5": {
        "title": "Multi-holder completion-channel separator",
        "why": "Tests holder reversal cost against H1 capability-completion and TaF-readout absorbers.",
    },
    "H6": {
        "title": "Internal versus external completion boundary theorem",
        "why": "Clarifies where pre-action family noncompletion is internal rather than external completion language.",
    },
    "H7": {
        "title": "Completion-aware Adapter_P admission contract",
        "why": "Turns H1 completion channels into required preservation maps before any neighbor datum counts.",
    },
    "H8": {
        "title": "D-FORK regime signature bundle",
        "why": "Packages regime signatures after H2/H7 decide the operative source and admission contracts.",
    },
    "H9": {
        "title": "H1 physical calibration batch",
        "why": "Runs CRISPR near-miss and Dynamic/Floquet negative control through H1 plus Adapter_P.",
    },
}


BALLOTS = {
    "orthodox_professor": ["H6", "H2", "H7", "H9", "H5", "H8"],
    "heterodox_rigorous_professor": ["H2", "H7", "H6", "H5", "H9", "H8"],
    "commercial_scientist": ["H9", "H5", "H7", "H2", "H6", "H8"],
    "philosopher_of_science": ["H2", "H6", "H7", "H5", "H9", "H8"],
    "wild_frontier_scientist": ["H2", "H9", "H5", "H7", "H8", "H6"],
    "computability_proof_theory": ["H2", "H6", "H7", "H8", "H5", "H9"],
    "category_sheaf_topos": ["H7", "H2", "H6", "H8", "H9", "H5"],
    "quantum_operator_algebra": ["H9", "H7", "H2", "H5", "H6", "H8"],
    "thermo_information": ["H5", "H9", "H2", "H7", "H6", "H8"],
    "cosmology_boundary_physics": ["H7", "H2", "H9", "H6", "H5", "H8"],
    "distributed_systems_finality": ["H5", "H7", "H2", "H9", "H6", "H8"],
    "evolution_open_endedness": ["H9", "H2", "H5", "H7", "H6", "H8"],
}


def validate() -> None:
    item_set = set(ITEMS)
    for persona, ballot in BALLOTS.items():
        if len(ballot) != len(item_set):
            raise ValueError(f"{persona} ballot length {len(ballot)} != item count {len(item_set)}")
        if set(ballot) != item_set:
            missing = sorted(item_set - set(ballot))
            extra = sorted(set(ballot) - item_set)
            raise ValueError(f"{persona} ballot mismatch; missing={missing}; extra={extra}")


def prefers(ballot: list[str], x: str, y: str) -> bool:
    return ballot.index(x) < ballot.index(y)


def pairwise_margin(items: list[str]) -> dict[tuple[str, str], int]:
    margin: dict[tuple[str, str], int] = {}
    for x, y in combinations(items, 2):
        sx = sum(1 for ballot in BALLOTS.values() if prefers(ballot, x, y))
        sy = len(BALLOTS) - sx
        margin[(x, y)] = sx - sy
        margin[(y, x)] = sy - sx
    return margin


def copeland(items: list[str], margin: dict[tuple[str, str], int]) -> dict[str, int]:
    score = {item: 0 for item in items}
    for x, y in combinations(items, 2):
        result = margin[(x, y)]
        if result > 0:
            score[x] += 1
            score[y] -= 1
        elif result < 0:
            score[y] += 1
            score[x] -= 1
    return score


def average_position(item: str) -> float:
    return sum(ballot.index(item) for ballot in BALLOTS.values()) / len(BALLOTS)


def majority_graph(items: list[str], margin: dict[tuple[str, str], int]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {item: [] for item in items}
    for x, y in combinations(items, 2):
        if margin[(x, y)] > 0:
            graph[x].append(y)
        elif margin[(y, x)] > 0:
            graph[y].append(x)
    for item in graph:
        graph[item].sort(key=lambda x: (average_position(x), x))
    return graph


def condorcet_order_if_acyclic(items: list[str], graph: dict[str, list[str]]) -> list[str] | None:
    indegree = {item: 0 for item in items}
    for winners in graph.values():
        for loser in winners:
            indegree[loser] += 1

    ready = deque(sorted((item for item, degree in indegree.items() if degree == 0), key=lambda x: (average_position(x), x)))
    order: list[str] = []
    while ready:
        item = ready.popleft()
        order.append(item)
        for loser in graph[item]:
            indegree[loser] -= 1
            if indegree[loser] == 0:
                ready.append(loser)
                ready = deque(sorted(ready, key=lambda x: (average_position(x), x)))

    if len(order) != len(items):
        return None
    return order


def rank_items() -> tuple[str, list[str], dict[str, int], dict[tuple[str, str], int]]:
    validate()
    items = list(ITEMS)
    margin = pairwise_margin(items)
    graph = majority_graph(items, margin)
    condorcet_order = condorcet_order_if_acyclic(items, graph)
    score = copeland(items, margin)

    if condorcet_order is not None:
        return "condorcet_acyclic", condorcet_order, score, margin

    order = sorted(items, key=lambda item: (-score[item], average_position(item), item))
    return "copeland_cycle_fallback", order, score, margin


def main() -> int:
    mode, order, score, margin = rank_items()
    print("=" * 78)
    print("TEMPORAL ISSUANCE ATTENTION PRIORITY")
    print("=" * 78)
    print(f"Ranking mode: {mode}")
    print(f"Personas: {len(BALLOTS)}")
    print()
    print("Prioritized list:")
    print()
    for rank, item in enumerate(order, 1):
        data = ITEMS[item]
        print(f"{rank}. [{item}] {data['title']}  Copeland {score[item]:+d}  avg_pos {average_position(item):.2f}")
        print(f"   why: {data['why']}")
    print()
    print("Per-persona first picks:")
    for persona, ballot in BALLOTS.items():
        print(f"- {persona}: {ballot[0]}")
    print()
    print("Top-four pairwise margins, positive means row beats column:")
    top = order[:4]
    header = "       " + "".join(f"{item:>5}" for item in top)
    print(header)
    for row_item in top:
        row = "".join("    ." if row_item == col_item else f"{margin[(row_item, col_item)]:+5d}" for col_item in top)
        print(f"{row_item:>5} {row}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
