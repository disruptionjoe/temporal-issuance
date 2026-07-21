#!/usr/bin/env python3
"""Boundary-parent Lean-extension cross-check probe (TI, 2026-07-20).

Independent finite sanity check of the STRUCTURE formalized in
  formal/lean/OnlineIssuance/BoundaryInvolution.lean   (leg b)
  formal/lean/OnlineIssuance/BoundaryParent.lean        (parent shape + leg a)

It mirrors gu-formalization tests/channel-swings/diagonal_boundary_probe.py's
leg-(b) action arithmetic: the fixpoint-free swap on the Z/2 label object, the
exhaustive "0 invariant valuations" count, and the Lawvere no-closure diagonal
escape -- exhaustively over small finite carriers, so the Python agrees with
the Lean by brute force (not by re-deriving the proof).

Deterministic (double-run byte-identical), pure-Python (no numpy: the arithmetic
is exact integer/enumeration, so no float seed is needed; SEED is recorded for
convention only), tagged [T]/[E]/[F], prints a HEADLINE, exits 0 on ALL PASS.

This is a fixture-grade sanity check, NOT a proof. No claim movement:
TI-C003 / TI-C019 / TI-C020 untouched. claim_status_change: none.
"""

from __future__ import annotations

import itertools
import json
import sys
from typing import Callable

SEED = 20260720  # convention only; the battery is a deterministic enumeration

# ---- The Z/2 label object B = {0, 1} and its two structure maps ----
B = (0, 1)
swap: Callable[[int], int] = lambda b: 1 - b   # fixpoint-free involution (alpha)
idmap: Callable[[int], int] = lambda b: b      # the dissolution control (alpha = id)


def is_involution(alpha, carrier) -> bool:
    return all(alpha(alpha(b)) == b for b in carrier)


def fixed_points(alpha, carrier):
    return [b for b in carrier if alpha(b) == b]


def is_injective(alpha, carrier) -> bool:
    return len({alpha(b) for b in carrier}) == len(list(carrier))


def all_valuations(domain_size, carrier):
    """Every v : A -> B as a tuple of length domain_size."""
    return itertools.product(carrier, repeat=domain_size)


def count_invariant_valuations(alpha, domain_size, carrier) -> int:
    """v is alpha-invariant iff alpha(v(a)) == v(a) for all a."""
    n = 0
    for v in all_valuations(domain_size, carrier):
        if all(alpha(val) == val for val in v):
            n += 1
    return n


def all_binary_ops(a_size, carrier):
    """Every T : A x A -> B, as a nested tuple T[a][x]; a_size rows, a_size cols."""
    row_space = list(itertools.product(carrier, repeat=a_size))  # each row: A -> B
    return itertools.product(row_space, repeat=a_size)           # a_size rows


def is_weakly_point_surjective(T, a_size, carrier) -> bool:
    """Some row a reproduces every g : A -> B (weak point-surjectivity)."""
    rows = set(T)  # the functions A->B that appear as rows of T
    for g in itertools.product(carrier, repeat=a_size):
        if g not in rows:
            return False
    return True


def twisted_diagonal_escapes_every_row(alpha, T, a_size, carrier) -> bool:
    """d(x) = alpha(T[x][x]) is represented by NO row of T (parent's d=alpha.T.Delta)."""
    d = tuple(alpha(T[x][x]) for x in range(a_size))
    return all(row != d for row in T)


def run_battery() -> dict:
    checks: list[dict] = []

    def record(tag, cid, desc, passed):
        checks.append({"tag": tag, "id": cid, "desc": desc, "passed": bool(passed)})

    # ---------- [T] setup ----------
    record("T", "T1", "swap is an involution on B", is_involution(swap, B))
    record("T", "T2", "swap is fixpoint-free on B (0 fixed points)",
           fixed_points(swap, B) == [])
    record("T", "T3", "id is an involution WITH fixed points (control)",
           is_involution(idmap, B) and fixed_points(idmap, B) == [0, 1])

    # ---------- [E] the formalized structure ----------
    # E1: involution_injective (BoundaryInvolution.involution_injective)
    record("E", "E1", "swap involution is injective", is_injective(swap, B))

    # E2a-c: no_invariant_valuation over inhabited domains |A| = 1,2,3
    for k, size in ((2, 1), (3, 2), (4, 3)):
        cnt = count_invariant_valuations(swap, size, B)
        record("E", f"E2_{size}",
               f"no swap-invariant valuation for |A|={size} (count==0)", cnt == 0)

    # E3: no_fixed_in_enumeration over the full label object
    record("E", "E3", "no label in B is swap-fixed (exhaustive count == empty)",
           all(swap(b) != b for b in B))

    # E4a-c: no_self_closure (Lawvere) under fixpoint-free swap, |A| = 1,2,3
    for size in (1, 2, 3):
        any_surj = any(
            is_weakly_point_surjective(T, size, B)
            for T in all_binary_ops(size, B)
        )
        record("E", f"E4_{size}",
               f"no closure candidate T:AxA->B is point-surjective, |A|={size}",
               not any_surj)

    # E5: twistedDiagonal_unrepresented, |A| = 2, exhaustive over all T
    all_escape = all(
        twisted_diagonal_escapes_every_row(swap, T, 2, B)
        for T in all_binary_ops(2, B)
    )
    record("E", "E5", "twisted diagonal d=alpha.T.Delta escapes every row (|A|=2)",
           all_escape)

    # ---------- [F] teeth + plant ----------
    # F1: teeth -- leg (b) DETECTS fixpoint-freeness. swap => 0 invariant
    #     valuations; the dissolution control id => strictly more; counts differ.
    swap_cnt = count_invariant_valuations(swap, 2, B)
    id_cnt = count_invariant_valuations(idmap, 2, B)
    record("F", "F1",
           "dissolution teeth: swap gives 0 but id gives >0 invariant valuations",
           swap_cnt == 0 and id_cnt > 0 and swap_cnt != id_cnt)

    # F2: plant -- a datum whose label object is a SINGLETON {*} has only the
    #     identity involution (a fixed point), so leg (b) does NOT exclude it:
    #     an invariant valuation EXISTS. The law is class-relative, not absolute;
    #     the certificate correctly does not exclude a trivial/fixed-label datum.
    singleton = (0,)
    plant_cnt = count_invariant_valuations(idmap, 2, singleton)
    record("F", "F2",
           "plant: singleton-label datum is NOT excluded (invariant valuation exists)",
           plant_cnt > 0)

    counts = {"T": 0, "E": 0, "F": 0}
    for c in checks:
        counts[c["tag"]] += 1
    all_pass = all(c["passed"] for c in checks)

    return {
        "seed": SEED,
        "checks": checks,
        "counts": counts,
        "all_pass": all_pass,
        "headline": (
            f"{counts['E']} [E] + {counts['F']} [F] = {counts['E'] + counts['F']} "
            f"(setup [T] = {counts['T']} excluded) "
            f"{'ALL PASS' if all_pass else 'FAIL'}"
        ),
    }


def main() -> int:
    first = run_battery()
    second = run_battery()
    a = json.dumps(first, indent=2, sort_keys=True)
    b = json.dumps(second, indent=2, sort_keys=True)
    determinism_ok = a == b

    failed = [c for c in first["checks"] if not c["passed"]]
    for c in first["checks"]:
        print(f"[{c['tag']}] {c['id']}: {'PASS' if c['passed'] else 'FAIL'} -- {c['desc']}")
    print(f"determinism (double-run byte-identical): {'PASS' if determinism_ok else 'FAIL'}")
    print("HEADLINE:", first["headline"])

    if first["all_pass"] and determinism_ok and not failed:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
