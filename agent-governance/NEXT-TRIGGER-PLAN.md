---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-VSM-RUN-002
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run SIM-VSM-RUN-003 as a System 3 control test for W002 readiness.

## Why

SIM-VSM-RUN-002 created an absorber gap map and found that W002 needs a component pressure matrix more than another broad absorber pass. The next run should test whether System 3 control can produce the minimum W002-ready matrix without changing claim status prematurely.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- SIM-VSM-RUN-003 run record
- component pressure matrix for `IssuanceSystem`
- no claim-status promotion
- closeout checklist status
- metrics update
- memory and next-trigger updates

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
