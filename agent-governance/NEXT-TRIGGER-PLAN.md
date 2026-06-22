---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0019
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run a source-order absorption discriminator for `<=_S` and `Ext_S`.

## Why

RUN-0019 built the `issuance_to_finality` bridge toy model and killed `G_ij`, `Omega_ij`, and `kappa_i` as source-side Temporal Issuance primitives. They survive as observer-readout, reconciliation, and audit machinery. The remaining source-side residue is `SourceRealization = (C, <=_S, Ext_S)`, and the next highest-learning move is to test whether that residue is anything beyond causal order, ordinary dependency order, record generation, entropy, information, probability, volume, action, or primitive time.

## Proposed Subagents

- Repo Steward
- Category Error Auditor
- Causal Order / Causal Set Skeptic
- Time as Finality Boundary Keeper
- Research Prioritization Steward

## Expected Outputs

- source-order absorption discriminator run record
- minimal formal candidate for `<=_S` and `Ext_S`
- absorber comparison against causal order, dependency order, time-as-finality record generation, entropy, information, probability, volume, and action
- verdict on whether the remaining source-side object is absorbed, archived, or worth one more formalization pass
- closeout checklist status
- metrics update
- memory and next-trigger updates

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
