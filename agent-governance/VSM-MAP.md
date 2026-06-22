---
artifact_type: vsm_map
status: active
governance_role: viability_map
constitutional: false
---

# VSM Map

## Purpose

Make repository viability visible with minimal bureaucracy.

This map is not a full Viable System Model operating manual. It is a readiness lens for checking whether the steward system can preserve identity, operate, coordinate, control, audit, and adapt while pursuing the research mission.

## Systems

```yaml
vsm_system: System 5 / Identity
repo_responsibility: Preserve the repo identity, core hypothesis, and Repo Steward job description.
current_files:
  - HYPOTHESIS.md
  - agent-governance/REPO-STEWARD.md
  - AGENTS.md
failure_mode: Identity drift, constitution expansion, or accidental merger with time-as-finality.
minimum_viable_signal: Constitutional objects remain unchanged unless Joe explicitly approves a change.
owner: Repo Steward under Joe review for constitutional changes.
```

```yaml
vsm_system: System 1 / Operations
repo_responsibility: Do the research and stewardship work.
current_files:
  - workflows/W000-repo-steward-cycle.md
  - workflows/W001-kill-core-hypothesis.md
  - workflows/W002-formal-object-pressure-test.md
  - workflows/W003-absorber-map.md
  - agent-runs/
  - CLAIM-LEDGER.md
failure_mode: Operations produce prose without hard outputs or verdict movement.
minimum_viable_signal: Each run creates a run record and changes claim state, absorber state, roadmap, memory, or a justified workflow surface.
owner: Repo Steward.
```

```yaml
vsm_system: System 2 / Coordination
repo_responsibility: Prevent conflicting state across memory, roadmap, workflows, and next-trigger planning.
current_files:
  - agent-governance/NEXT-TRIGGER-PLAN.md
  - ROADMAP.md
  - memory/steward-memory-summary.md
  - workflows/README.md
failure_mode: Surfaces disagree about what should happen next or what state the repo is in.
minimum_viable_signal: Next-trigger plan, roadmap, and memory summary name compatible next work.
owner: Repo Steward.
```

```yaml
vsm_system: System 3 / Control
repo_responsibility: Maintain internal accountability for claims, kills, governance changes, metrics, and closeout.
current_files:
  - CLAIM-LEDGER.md
  - KILL-CRITERIA.md
  - agent-governance/RUN-CLOSEOUT-CHECKLIST.md
  - agent-governance/GOVERNANCE-CHANGE-LEDGER.md
  - agent-governance/STEWARD-METRICS.md
failure_mode: The steward changes its own operating system or claim state without inspectable control records.
minimum_viable_signal: Material governance changes are logged, metrics are updated, and closeout items are recorded.
owner: Repo Steward.
```

```yaml
vsm_system: System 3* / Audit
repo_responsibility: Detect drift, inconsistency, stale memory, weak path kills, and coordination failures.
current_files:
  - workflows/W004-stewardship-assessment-and-drift-audit.md
  - agent-governance/RUN-CLOSEOUT-CHECKLIST.md
  - memory/path-kills.md
  - agent-governance/STEWARD-METRICS.md
failure_mode: The steward misses its own drift or treats summaries as truth when logs disagree.
minimum_viable_signal: W004 or a lighter audit can inspect recent runs and identify inconsistencies.
owner: Repo Steward, with Joe review when uncertainty is high.
```

```yaml
vsm_system: System 4 / Intelligence
repo_responsibility: Sense future threats, absorbers, options, category errors, and reusable governance value.
current_files:
  - workflows/W003-absorber-map.md
  - absorbers/
  - personas/
  - memory/export-queue.md
  - explorations/
failure_mode: The repo overfits to current framing, local minima, or internal process and misses outside absorbers.
minimum_viable_signal: Absorber mapping, divergent personas, export candidates, and category-error checks change future options.
owner: Repo Steward.
```

## Readiness Interpretation

The repo is ready for a five-run stress simulation if:

- System 5 identity is stable.
- System 1 can produce hard outputs.
- System 2 surfaces agree on next work.
- System 3 records material changes.
- System 3* can audit runs after the fact.
- System 4 can update strategy from absorber and future-risk signals.

If any of these fail during a simulation, record the failure in the run record and route it through W004 or daily review.
