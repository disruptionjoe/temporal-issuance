---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0012
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run RUN-0013 as a definition repair pass.

## Why

RUN-0012 ran W002 and weakened the launch `IssuanceSystem`. It killed generic `mu` and narrowed the surviving object to local/access-relative patches. The next highest-learning move is definition repair focused on `mu`, `kappa_i`, and `G_ij`.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- RUN-0013 run record
- definition repair notes for `mu`, `kappa_i`, and `G_ij`
- decision whether repaired definitions are worth a second W002 pass or should be queued
- closeout checklist status
- metrics update
- memory and next-trigger updates
- next route for RUN-0014 before W004 assessment

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
