---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-RUN-001
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to create observation-only steward metrics.

## Why

SIM-RUN-001 created the governance-change ledger. The next smallest missing guardrail is an observation-only metrics surface that lets the steward notice drift, churn, stale memory, automation failures, and research/governance imbalance without locking a scoring system too early.

## Proposed Subagents

- Systems Engineer
- AI Alignment / Agent Governance Researcher
- Product Manager

## Expected Outputs

- `agent-governance/STEWARD-METRICS.md`
- a SIM-RUN-002 run record
- memory update
- next-trigger plan moving to contributor intake

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
