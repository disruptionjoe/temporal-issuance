---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-VSM-RUN-001
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run SIM-VSM-RUN-002 as a System 1 hard-output research operation.

## Why

SIM-VSM-RUN-001 found that System 2 coordination surfaces agree and that the run-ID distinction is the main coordination risk. The sequence should now produce research-facing hard output rather than repeating coordination checks.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- SIM-VSM-RUN-002 run record
- lightweight W003 absorber gap scan
- hard output that updates absorber or roadmap state
- closeout checklist status
- metrics update
- memory and next-trigger updates

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
