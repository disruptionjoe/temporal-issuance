---
artifact_type: workflow
workflow_id: W000
status: active
governance_role: repo_steward_modular_container
constitutional: false
owner_agent: repo-steward
memory_summary: ../memory/steward-memory-summary.md
next_trigger_plan: ../agent-governance/NEXT-TRIGGER-PLAN.md
---

# W000: Repo Steward Cycle

This is the main modular container for Temporal Issuance automation.

Hourly automation should invoke this workflow, not an individual research workflow.

The Repo Steward uses this container to decide what should happen now. It may run existing workflows, revise workflows, create new workflows, create personas, attach memory packs, launch parallel subagents, or update the next-trigger plan.

## Purpose

Maximize the probability of reaching the correct verdict on the Temporal Issuance hypothesis.

## Required Load Order

1. `AGENTS.md`
2. `agent-governance/REPO-STEWARD.md`
3. `memory/steward-memory-summary.md`
4. `memory/steward-memory-log.md`
5. `CLAIM-LEDGER.md`
6. `KILL-CRITERIA.md`
7. `ROADMAP.md`
8. `agent-governance/NEXT-TRIGGER-PLAN.md`
9. `workflows/DYNAMIC-WORKFLOW-PROTOCOL.md`
10. `agent-governance/RUN-CLOSEOUT-CHECKLIST.md`
11. `agent-governance/STEWARD-METRICS.md`
12. `agent-governance/VSM-MAP.md`
13. `agent-governance/RUN-NOMENCLATURE.md`
14. `agent-governance/CROSS-REPO-CONTEXT-PROTOCOL.md`

## Decision Frame

Ask:

> What work pattern now most increases the probability of reaching the correct verdict on the core hypothesis?

The answer may be:

- run W001, W002, W003, or another existing workflow
- run W010 when multiple next actions compete or roadmap, memory, and next-trigger surfaces are stale or in tension
- create a new dynamic workflow
- create a dynamic persona
- attach a memory pack to a repeated workflow or persona
- launch several parallel subagents
- update claim status
- record a path kill
- update the export queue
- produce the daily learning brief or daily review artifact
- pause for uncertainty-driven human review
- consult cross-repo context when stuck or at local-minimum risk

## Hourly Operating Sequence

1. Check git status.
2. Load the required surfaces.
3. Compare `NEXT-TRIGGER-PLAN.md` against current claim, memory, roadmap, and kill surfaces.
4. Choose the highest-learning run or run set.
5. Execute the chosen workflow(s) or create the dynamic workflow needed.
6. Merge outputs into repository state.
7. Update `CLAIM-LEDGER.md`, `ROADMAP.md`, and memory as needed.
8. Update `agent-governance/NEXT-TRIGGER-PLAN.md`.
9. Write a run record under `agent-runs/`.
10. Update steward metrics.
11. Apply the run closeout checklist.
12. Run relevant checks.
13. Commit and push coherent changes.

## Parallelization Rule

Parallelize when workstreams have separable surfaces and parallel pressure improves falsification, absorption mapping, formalization, or governance learning without creating unmergeable noise.

If parallelization is not available in the current environment, simulate it by producing separate persona sections inside one run record and record that limitation.

## Strongest-Version Rule

Before killing a path, generate the strongest version available inside the run. Then attack that version from first principles.

## Path-Kill Rule

Every killed path must update `memory/path-kills.md` with:

```yaml
path:
reason_killed:
evidence:
local_minimum_risk:
possible_future_resurrection_trigger:
run_ref:
claim_refs:
```

## Completion Contract

Every W000 cycle should leave:

- a run record
- an updated next-trigger plan
- memory update
- metrics update
- claim, roadmap, kill, or export updates when touched
- closeout checklist status in the run record
- clean git status, unless a blocker is explicitly recorded
