---
artifact_type: cadence
status: active
governance_role: hourly_trigger_contract
constitutional: false
---

# Hourly Cadence

The hourly trigger invokes `workflows/W000-repo-steward-cycle.md`.

The steward does not run a fixed checklist. It decides what work has highest expected learning value, then chooses or creates the workflow and persona structure needed for that work.

## Hourly Shape

1. Load steward identity and memory.
2. Load claim ledger, kill criteria, roadmap, and next-trigger plan.
3. Evaluate current highest-learning opportunity.
4. Run or create the appropriate workflow set.
5. Launch parallel subagents only when merge surfaces are separable.
6. Merge outputs into repository state.
7. Update next-trigger plan.
8. Append memory.
9. Record run artifact.

## Codex Automation

Local Codex automation target:

- automation id: `hourly-temporal-issuance-repo-steward`
- cwd: `C:\Users\joe\JB\Github Repos\temporal-issuance`
- entry workflow: `workflows/W000-repo-steward-cycle.md`

The automation prompt should stay thin. It should name the repo, read `AGENTS.md`, and invoke W000. The substantive operating instructions belong in the repository, not in the Codex automation record.

## Aggression Default

Unused capacity is initially treated as wasted opportunity. Budget limits should emerge from observed failures such as skipped runs, queue buildup, token exhaustion, or cadence instability.
