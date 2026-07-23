---
artifact_type: run_plan_and_receipt
status: complete
run_id: RUN-20260723-023657-temporal-issuance-direct
local_run_ref: RUN-0205
owner_id: temporal-issuance
mode: execute
lane_id: A
starting_revision: 17d766382df4d607b161b75a5c81eca18f0a5e3f
---

# Boundary target premise typing and default build

## Objective

Remove the misleading formal admission from the cross-repo boundary target,
align its live blocker with GU's corrected operator/domain result, and verify
the complete boundary package through the default Lean target.

## Execution

The target's `H_leg_a : True` placeholder is replaced by
`H_leg_a : ¬ WeaklyPointSurjective T`, and its proof uses that typed premise.
The existing codomain proof is unchanged. Comments and the companion finite
probe now distinguish the proved conditional composition from the unbuilt
physical GU instance and the still-untyped TaF retraction.

The boundary modules were absent from `OnlineIssuance.lean`. Adding them to the
default target revealed two pre-existing namespace-resolution errors in
`ParentHypotheses` helper methods. Qualifying their calls repaired the defects.

## Validation

- Confirmed no active repository writer lock.
- Confirmed no active Lean or Lake process before taking the serialized slot.
- `lake build`: PASS, 12 jobs, Lean 4.31.0.
- `python3 tools/boundary_externality_conjunct_split_probe.py`: PASS and
  byte-identical across its internal double run.
- `git diff --check`: required at close.

## Boundary and handoff

No claim, North Star, physical-candidate, CompletionClass, or Lane-control
movement. The physical reopener is the source-owned GU
operator/domain/end/symmetry packet plus an explicit assembly map. The TaF
retraction must remain a distinct later typed premise.
