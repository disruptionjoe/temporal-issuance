---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0007
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run a VSM-aware five-cycle thin-trigger stress simulation.

## Why

RUN-0007 added the minimum readiness instrumentation requested by the combined stewardship and VSM pass. Because the original `SIM-RUN-001` through `SIM-RUN-005` already exist, preserve them and run the next stress test as `SIM-VSM-RUN-001` through `SIM-VSM-RUN-005`.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- five sequential simulated W000 run records named `SIM-VSM-RUN-001` through `SIM-VSM-RUN-005`
- closeout checklist status in each run record
- metrics update for each run
- governance-change ledger updates when governance changes
- memory and next-trigger updates after each run
- W004 assessment over the five VSM-aware runs
- next route, defaulting to W003 absorber mapping unless the simulation reveals a serious viability issue

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
