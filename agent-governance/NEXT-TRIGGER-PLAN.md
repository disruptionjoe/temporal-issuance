---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0013
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run RUN-0014 as a toy-patch test candidate pass.

## Why

RUN-0013 generated repair candidates for `lambda_i`, `kappa_i`, `G_ij`, and `Omega_ij`. The next highest-learning move is not more definition prose; it is a minimal toy-patch test that can pressure those candidates.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- RUN-0014 run record
- minimal two-observer toy-patch test candidates
- decision whether repaired definitions survive enough to justify another W002 pass
- closeout checklist status
- metrics update
- memory and next-trigger updates
- route to W004 assessment over RUN-0010 through RUN-0014

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
