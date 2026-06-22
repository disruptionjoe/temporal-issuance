---
artifact_type: memory_summarizer_protocol
status: active
governance_role: memory_summarization
constitutional: false
---

# Memory Summarizer Protocol

## Purpose

Keep compact steward memory useful without rewriting history or silently turning memory into policy.

## Source Surfaces

Read:

1. `memory/steward-memory-log.md`
2. `memory/steward-memory-summary.md`
3. recent run records since the last summarized run
4. `CLAIM-LEDGER.md`
5. `ROADMAP.md`
6. `agent-governance/NEXT-TRIGGER-PLAN.md`
7. `memory/path-kills.md`
8. `memory/export-queue.md`

## When To Summarize

Summarize when:

- W000 completes a run that changes strategic state
- the summary is behind the latest run record
- a W004 assessment finds memory drift
- a claim status changes
- a path is killed
- the next-trigger plan changes materially
- a governance-change ledger entry changes operating rules

For very small runs, W000 may update only the `last_summarized_run` and one concise current-state sentence if no deeper summary change is warranted.

## What To Preserve

The summary should preserve:

- current strongest version
- current strongest objection
- current strategy
- killed paths that still affect current reasoning
- open blockers
- governance assumptions under test
- next recommended workflow

## What Not To Do

Do not:

- delete memory-log entries
- rewrite history
- convert memory observations into policy without an authority surface
- hide disagreement or reversals
- summarize away resurrection triggers
- over-compress path kills into vague lessons

## Output Contract

Every summarizer pass should update:

- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md` if the summarizer itself produced a material learning

If the summarizer changes a governance rule or summary format, also update:

- `agent-governance/GOVERNANCE-CHANGE-LEDGER.md`

## Design Hypothesis

The memory summary should be a compact load surface, not a second governance authority.

If future runs show that summary updates are becoming policy or losing important failures, revise this protocol.

