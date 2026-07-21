#!/usr/bin/env python3
"""Externality-conjunct split cross-check probe (TI, 2026-07-21).

Sharpens the SPLIT made in
  formal/lean/OnlineIssuance/BoundaryParent.lean :: cross_repo_boundary_law_TARGET
where the `sorry` was factored so that:
  * conjunct (b) EXTERNALITY  -- (no alpha-invariant valuation) -- is PROVED via
    `no_invariant_valuation` (the involution leg), and
  * conjunct (a) SELF-CLOSURE -- (no weakly-point-surjective T) -- KEEPS the sorry
    (the diagonal / product-uniformity leg, GU-side open theorem O-b).

This probe is the GU-instance sanity check: it models the Krein-orientation label
object B = {+K_S, -K_S} as {+1, -1} with alpha = the K_S-sign flip (negation),
GU's Ad(U_h) with `U_h K_S U_h^{-1} = -K_S`. It confirms, by exhaustive finite
enumeration:

  (b) DISCHARGES  -- alpha is a fixpoint-free involution on {+K_S,-K_S}, and over
      every inhabited reading space (|Read| = 1,2,3) there are ZERO
      alpha-invariant valuations -- so the externality conjunct is a genuine,
      NON-VACUOUS theorem (matches Lean `k_s_flip_externality`).

  (b)-teeth       -- the dissolution control alpha = id (no flip) reopens: invariant
      valuations REAPPEAR. So the result detects fixpoint-freeness; it is not
      always-zero.

  (a) STAYS OPEN  -- flagged [T] (declared-open), NOT discharged here. The
      self-closure conjunct is the diagonal leg; its operator-grade obstruction
      (product-uniform norm-resolvent boundary theorem) is out of scope for this
      finite probe and remains the `sorry` in the TARGET.

Deterministic (double-run byte-identical), pure-Python (exact integer
enumeration; SEED recorded for convention only), tagged [T]/[E]/[F], prints a
HEADLINE, exits 0 on ALL PASS.

Fixture-grade sanity check, NOT a proof. No claim movement:
TI-C003 / TI-C019 / TI-C020 untouched. claim_status_change: none.
"""

from __future__ import annotations

import itertools
import json
from typing import Callable

SEED = 20260721  # convention only; the battery is a deterministic enumeration

# ---- GU Krein-orientation label object B = {+K_S, -K_S}, modeled as {+1, -1} ----
B = (1, -1)
k_s_flip: Callable[[int], int] = lambda b: -b   # alpha = Ad(U_h): U_h K_S U_h^-1 = -K_S
id_control: Callable[[int], int] = lambda b: b  # dissolution control (alpha = id)


def is_involution(alpha, carrier) -> bool:
    return all(alpha(alpha(b)) == b for b in carrier)


def fixed_points(alpha, carrier):
    return [b for b in carrier if alpha(b) == b]


def count_invariant_valuations(alpha, domain_size, carrier) -> int:
    """v : Read -> B is alpha-invariant iff alpha(v(a)) == v(a) for all a."""
    n = 0
    for v in itertools.product(carrier, repeat=domain_size):
        if all(alpha(val) == val for val in v):
            n += 1
    return n


def run_battery() -> dict:
    checks: list[dict] = []

    def record(tag, cid, desc, passed):
        checks.append({"tag": tag, "id": cid, "desc": desc, "passed": bool(passed)})

    # ---------- [T] the K_S-flip is a fixpoint-free involution (GU certificate) ----------
    record("T", "T1", "K_S-flip is an involution on {+K_S,-K_S} (Ad(U_h)^2 = id)",
           is_involution(k_s_flip, B))
    record("T", "T2", "K_S-flip is fixpoint-free (U_h K_S U_h^-1 = -K_S; no fixed sign)",
           fixed_points(k_s_flip, B) == [])

    # ---------- [E] conjunct (b) EXTERNALITY discharges, non-vacuously ----------
    # E1a-c: no K_S-flip-invariant valuation over inhabited Read of size 1,2,3.
    #        Matches Lean `k_s_flip_externality` / `no_invariant_valuation`.
    for size in (1, 2, 3):
        cnt = count_invariant_valuations(k_s_flip, size, B)
        record("E", f"E1_{size}",
               f"externality (b): 0 K_S-flip-invariant valuations, |Read|={size}",
               cnt == 0)
    # E2: the hypothesis package is INHABITED (non-vacuous) -- a concrete alpha
    #     satisfying both Involution and FixpointFree exists (it is k_s_flip).
    record("E", "E2",
           "hypotheses inhabited: K_S-flip is a concrete fixpoint-free involution",
           is_involution(k_s_flip, B) and fixed_points(k_s_flip, B) == [])

    # ---------- [F] teeth: (b) DETECTS fixpoint-freeness (not always-zero) ----------
    flip_cnt = count_invariant_valuations(k_s_flip, 2, B)
    id_cnt = count_invariant_valuations(id_control, 2, B)
    record("F", "F1",
           "dissolution teeth: K_S-flip gives 0 but alpha=id gives >0 invariant valuations",
           flip_cnt == 0 and id_cnt > 0 and flip_cnt != id_cnt)

    # ---------- [T] conjunct (a) SELF-CLOSURE is DECLARED-OPEN, not discharged ----------
    # This probe does NOT attempt the diagonal / product-uniformity leg; it stays
    # the `sorry` in the TARGET (GU-side open theorem O-b). Recorded, not asserted.
    record("T", "T3",
           "self-closure (a) left OPEN here (product-uniformity O-b; TARGET keeps sorry)",
           True)

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
            f"(declared-open/setup [T] = {counts['T']}) "
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
