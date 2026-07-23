---
artifact_type: exploration
status: complete
exploration_id: E198
date: 2026-07-22
claim_status_change: none
---

# E198: Cross-repo boundary target premise typing

## Result

The cross-repo boundary target is now a machine-checked conditional theorem
with no admitted proof term. Its missing self-closure bridge is represented by
the exact typed premise:

```lean
H_leg_a : ¬ WeaklyPointSurjective T
```

and the first conjunct is discharged by `H_leg_a`. The codomain conjunct remains
proved by `no_invariant_valuation H_fpf point`.

This removes a misleading formal placeholder; it does not prove the physical
GU instance. The theorem still assumes abstract `Read`, `B`, `alpha`, and `T`.
The claim that these arise from GU's assembled physical reader construction is
the real cross-repo work.

## Corrected blocker

GU's 2026-07-22 operator/domain audit supersedes the earlier idea that a
product-uniform numerical or reduced-operator surrogate closes the physical
self-closure leg. Reopening the physical instantiation requires one
source-owned packet containing:

- the complete first-order operator and lower-order terms;
- exact end geometry and L2 density;
- initial, minimal, maximal, and selected closed domains;
- Green boundary form and trace space;
- deck, real, and Pin actions; and
- an explicit map from that construction into the abstract assembled `T`.

The TaF premise remains `True` and inert. A later integration must type its
idempotent, oriented, non-invertible retraction separately from the
fixpoint-free GU/TI involution.

## Default-target integration

`OnlineIssuance.lean` now imports `BoundaryInvolution` and `BoundaryParent`.
The first default-target build of those modules exposed two old name-resolution
errors in `ParentHypotheses.no_self_closure` and
`ParentHypotheses.no_invariant_valuation`; fully qualified theorem names repair
both without changing their statements.

## Validation

- `lake build`: PASS, 12 jobs on Lean 4.31.0.
- `python3 tools/boundary_externality_conjunct_split_probe.py`: PASS, deterministic,
  4 evidential checks plus 1 falsification control; the physical instance stays
  explicitly open.
- `BoundaryParent.lean` contains no admitted proof term.
- No TI claim, North Star, physical candidate, CompletionClass, or Lane control moved.
