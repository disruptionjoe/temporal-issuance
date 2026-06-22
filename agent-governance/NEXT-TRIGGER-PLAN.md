---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: SIM-RUN-002
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is to create a contributor-intake and evaluation workflow stub.

## Why

SIM-RUN-002 created observation-only steward metrics. The next smallest missing guardrail is a public contribution intake workflow so outside issues, pull requests, and comments can become evidence without becoming operative instructions.

## Proposed Subagents

- Open Source Governance Architect
- Institutional Economist
- AI Alignment / Agent Governance Researcher
- Product Manager

## Expected Outputs

- `workflows/W005-contributor-intake-and-evaluation.md`
- workflow registry update
- a SIM-RUN-003 run record
- memory update
- next-trigger plan moving to memory summarizer protocol

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or parallelized subagent runs.
