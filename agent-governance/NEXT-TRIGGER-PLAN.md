---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-VSM-RUN-003
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run SIM-VSM-RUN-004 as a System 3* audit spot check.

## Why

SIM-VSM-RUN-003 created the component pressure matrix needed for W002. Before the final simulation run, W000 should test whether the new metrics, memory, roadmap, closeout, and claim surfaces remain consistent.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- SIM-VSM-RUN-004 run record
- System 3* audit spot check
- inconsistency list, even if empty
- closeout checklist status
- metrics update
- memory and next-trigger updates

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
