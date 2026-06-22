---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-VSM-RUN-004
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run SIM-VSM-RUN-005 as a System 4 strategy handoff.

## Why

SIM-VSM-RUN-004 audited memory, claim, roadmap, metrics, path-kill, and daily-review surfaces. It found no serious viability issue, only a low-severity stale daily-review risk that has been routed to a fresh review artifact.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- SIM-VSM-RUN-005 run record
- System 4 strategy handoff
- clear route into W004 assessment
- recommendation for post-assessment default, likely W003 unless assessment finds a serious issue
- closeout checklist status
- metrics update
- memory and next-trigger updates

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
