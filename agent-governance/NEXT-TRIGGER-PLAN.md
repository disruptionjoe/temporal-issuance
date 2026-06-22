---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-VSM-RUN-005
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to run W004: Stewardship Assessment And Drift Audit over SIM-VSM-RUN-001 through SIM-VSM-RUN-005.

## Why

SIM-VSM-RUN-005 completed the VSM-aware five-run stress sequence and routed the repo into W004. The assessment should determine whether W000 behaved like a steward, whether VSM viability improved or degraded, and whether the next default should return to W003 absorber mapping.

## Proposed Subagents

- Repo Steward
- VSM Auditor
- Category Error Auditor
- Research Prioritization Steward

## Expected Outputs

- W004 assessment report over `SIM-VSM-RUN-001` through `SIM-VSM-RUN-005`
- answers to the VSM readiness assessment questions
- evaluation of W000 as steward versus checklist
- review of memory, metrics, governance changes, claim ledger, roadmap, next-trigger plan, created artifacts, path kills, and daily-review artifacts
- closeout checklist status
- metrics update
- memory and next-trigger updates
- post-assessment default route, likely W003 unless W004 finds a serious viability issue

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
