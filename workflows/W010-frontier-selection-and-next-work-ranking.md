---
artifact_type: workflow
workflow_id: W010
status: active
governance_role: frontier_selection_and_next_work_ranking
constitutional: false
created_by_request: joe
design_hypothesis: A reusable frontier-selection pass improves W000 routing by ranking next work from the full repo state instead of following recency, narrative pull, or stale trigger plans.
---

# W010: Frontier Selection And Next-Work Ranking

## Purpose

Look at the whole repository state and identify the next work that most increases the chance
of reaching the correct verdict on Temporal Issuance.

This workflow is not a research fixture, steelman pass, or bridge test. It is a routing
subroutine for W000:

```text
Given the current repo state, what should the steward do next?
```

The output is a ranked frontier list plus one recommended next trigger.

## Workflow Card

```yaml
workflow_id: W010
status: active
purpose: Extract, rank, and route the live research frontier from current repo state.
trigger_conditions:
  - Joe asks what the repo should do next
  - NEXT-TRIGGER-PLAN and ROADMAP may be stale or in tension
  - several possible next actions compete for attention
  - a major run just completed and the next best work is not obvious
  - W000 needs a routing pass before choosing a specific research workflow
input_surfaces:
  - README.md
  - HYPOTHESIS.md
  - NORTH-STAR.md
  - CLAIM-LEDGER.md
  - ROADMAP.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
  - memory/steward-memory-summary.md
  - memory/steward-memory-log.md
  - memory/path-kills.md
  - agent-runs/ latest run records
  - explorations/ latest frontier artifacts
  - workflows/README.md
  - agent-governance/STEWARD-METRICS.md
optional_input_surfaces:
  - absorbers/
  - FORMAL-OBJECT.md
  - HYPOTHESIS-STEELMAN.md
  - adjacent repo context surfaces when a local-minimum risk appears
personas: Repo Steward, with optional inline hostile reviewer and local-minimum auditor
memory_pack: current steward summary plus latest run delta
expected_outputs: frontier inventory, ranked next-work list, recommended next trigger, success/failure conditions, merge recommendations
merge_surfaces: NEXT-TRIGGER-PLAN.md, ROADMAP.md, memory, claim-ledger recommendations, run record if invoked as W000
retirement_condition: retire if W000's native routing becomes consistently better or if this workflow turns into process ceremony without changing next work
```

## Trigger Conditions

Invoke W010 when:

- Joe asks for "next goals," "most important work," "what should we do next," or similar.
- The repo has multiple live targets and the highest-leverage next move is unclear.
- The latest run added a new result but did not clearly update all routing surfaces.
- `NEXT-TRIGGER-PLAN.md`, `ROADMAP.md`, and memory disagree.
- A recent thread feels pulled by recency, aesthetic appeal, or external excitement.
- W000 is about to choose work after a long or dense sequence of runs.

Do not invoke W010 merely because a known next trigger is already fresh, coherent, and
high-leverage. In that case, run the trigger.

## Phase 1: Load And State Sync

Read the required surfaces in this order:

1. `memory/steward-memory-summary.md`
2. `agent-governance/NEXT-TRIGGER-PLAN.md`
3. `ROADMAP.md`
4. `CLAIM-LEDGER.md`
5. latest 3-5 `agent-runs/` records
6. latest relevant `explorations/` artifacts
7. `memory/path-kills.md`
8. `workflows/README.md`
9. `agent-governance/STEWARD-METRICS.md`

Record a state-sync note:

```yaml
latest_run_seen:
memory_current: true_or_false
next_trigger_current: true_or_false
roadmap_current: true_or_false
surface_tensions:
  - tension_id:
    surfaces:
    description:
```

If a surface is stale but the correct current state is clear from later runs, use the later run
as the source of truth and note the stale surface as an update target.

## Phase 2: Extract Frontier Candidates

Create a candidate card for every live next-work item found in:

- claim ledger next actions
- roadmap open tasks
- next-trigger plan
- latest run recommendations
- unresolved obligations named in explorations
- path-kill resurrection triggers that match current work
- absorber threats not yet tested
- contradiction or stale-state signals
- Joe's explicit request

Candidate card format:

```yaml
frontier_id:
title:
source_refs:
claim_refs:
layer: [source / projection / record_readout / physical_bridge / governance / export]
candidate_workflow:
current_status:
why_live:
success_condition:
failure_condition:
main_absorbers_or_kill_risks:
dependencies:
expected_artifact:
```

Keep candidates concrete. "Think more about physics" is not a candidate. "Run fixed-H vs
H-growing fixture against TI-C020" is a candidate.

## Phase 3: Rank By Verdict Movement

Score each candidate qualitatively, not mechanically. Use these lenses:

```yaml
centrality:
  question: Does this decide or sharpen a central fork?
  high_signal: A result would move TI-C019, TI-C020, or a major path kill.
unblocks_multiple_surfaces:
  question: Does this clear several obligations, claims, or stale tensions at once?
absorber_pressure:
  question: Does this test the strongest live absorber rather than a friendly case?
failure_value:
  question: Would a negative result still teach something decisive?
specificity:
  question: Are success and failure conditions crisp enough to run now?
recency_correction:
  question: Is this being selected because it matters, not merely because it is recent?
local_minimum_escape:
  question: Does it check whether the repo is stuck in a narrow formal or narrative basin?
blast_radius:
  question: Could this overclaim or disturb many surfaces if done sloppily?
```

Rank each candidate:

```yaml
rank:
frontier_id:
score_label: [highest / high / medium / low / defer]
reason:
why_not_higher:
recommended_workflow:
```

Prefer candidates that can kill, absorb, narrow, formalize, or promote claims. Deprioritize
work that only adds narrative, repeats a solved pass, or produces process without verdict
movement.

## Phase 4: Select Recommended Next Trigger

Select exactly one primary next trigger, plus at most three secondary triggers.

Recommended next trigger format:

```yaml
primary_next_trigger:
  workflow_or_run:
  reason:
  claim_refs:
  success_condition:
  failure_condition:
  expected_artifact:
secondary_triggers:
  - workflow_or_run:
    reason:
```

If the top two candidates are genuinely tied, say so and state the deciding question Joe would
need to answer. Otherwise choose.

## Phase 5: Merge Recommendations

If W010 is invoked as part of a W000 cycle, update:

- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md` if open tasks changed
- `memory/steward-memory-summary.md` if the frontier changed materially
- `CLAIM-LEDGER.md` only for recommendations or addenda, not claim promotion
- `agent-governance/STEWARD-METRICS.md`
- a run record under `agent-runs/`

If W010 is invoked only for advice, produce the ranked list and do not update repo state unless
Joe asks to persist it.

## Output Format

Every persisted W010 run should include:

```yaml
run_id:
workflow: W010
latest_run_seen:
surface_tensions:
frontier_candidates:
ranked_next_work:
primary_next_trigger:
secondary_triggers:
surfaces_updated:
surfaces_left_unchanged:
```

In prose, lead with:

1. the primary next trigger
2. why it outranks the alternatives
3. the ranked list
4. stale/tension notes
5. exact repo updates made or recommended

## Guardrails

- Do not let recency outrank centrality.
- Do not let ambition outrank testability.
- Do not select work that only flatters the hypothesis.
- Do not demote a hard absorber just because it is uncomfortable.
- Do not create new workflows unless the missing work pattern has repeated value.
- Do not promote claims from W010 output. W010 routes work; it does not adjudicate claims.
- Keep governance subordinate to research. A governance candidate should rank first only if
  repo state is incoherent enough to block research.

## Design Hypothesis

W010 itself is a governance hypothesis:

> A deliberate frontier-selection pass improves the repo by converting diffuse live context
> into a ranked, falsification-oriented next-work queue.

If W010 repeatedly selects the same trigger W000 would already have selected, keep it as an
on-demand workflow only. If it repeatedly catches stale routing, hidden blockers, or higher-
leverage work, preserve it as the default W000 pre-routing pass after major runs.

