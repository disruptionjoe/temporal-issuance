---
artifact_type: protocol
status: active
governance_role: run_protocol
constitutional: false
---

# Agent Run Protocol

Every steward run follows this protocol unless a workflow explicitly narrows it.

## Preflight

Read:

1. `AGENTS.md`
2. `agent-governance/REPO-STEWARD.md`
3. `memory/steward-memory-summary.md`
4. `CLAIM-LEDGER.md`
5. `KILL-CRITERIA.md`
6. `ROADMAP.md`
7. `agent-governance/NEXT-TRIGGER-PLAN.md`

## Decide

Choose the work pattern with highest expected learning value.

Options include:

- run existing workflow
- revise existing workflow
- create dynamic workflow
- create dynamic persona
- launch parallel subagents
- update next-trigger plan
- pause for uncertainty-driven human review

## Execute

Run the selected workflow or workflow set. Preserve provenance. Keep outputs tied to claim IDs, absorber IDs, workflow IDs, or run IDs.

## Merge

Update relevant surfaces:

- `CLAIM-LEDGER.md`
- `ROADMAP.md`
- `memory/steward-memory-log.md`
- `memory/steward-memory-summary.md` when summarization is due
- `memory/path-kills.md`
- `memory/export-queue.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `agent-runs/`

## Learning Return

Every workflow returns the schema in `memory/learning-return-schema.md`.

