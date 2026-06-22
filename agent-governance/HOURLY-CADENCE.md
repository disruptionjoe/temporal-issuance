---
artifact_type: cadence
status: active
governance_role: hourly_trigger_contract
constitutional: false
---

# Hourly Cadence

The hourly trigger invokes the Repo Steward first.

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

## Aggression Default

Unused capacity is initially treated as wasted opportunity. Budget limits should emerge from observed failures such as skipped runs, queue buildup, token exhaustion, or cadence instability.

