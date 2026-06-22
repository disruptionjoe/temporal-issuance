---
artifact_type: research_improvements
status: active
governance_role: research_improvement_plan
exploration_id: E004
last_updated_by: RUN-0022
claim_refs:
  - TI-C001
  - TI-C002
  - TI-C003
constitutional: false
---

# E004: Research Improvements From Steelman Pass

## Source

Generated from `agent-runs/RUN-0022-taf-persona-steelman-hegelian-pass.md`.

## Main Lesson

The repo has been strong at killing weak formulations. The next improvement is to make sure it kills the strongest formulation.

The 62-persona steelman pass converged on one heterodox recommendation:

```text
Treat Temporal Issuance first as an admissible extension problem,
not first as a source-order problem.
```

This does not promote the hypothesis. It changes what the next test should attack.

## Research Improvements

### RI-001: Add A Steelman Surface

Problem:

The repo has `HYPOTHESIS.md` and `ANTI-HYPOTHESIS.md`, but after many kill passes the current strongest version is scattered across run records.

Improvement:

Create `HYPOTHESIS-STEELMAN.md`.

Purpose:

State the strongest current version in one place before each major kill or absorption pass.

Implemented:

`HYPOTHESIS-STEELMAN.md`

### RI-002: Use Fixture-Based Ontology Competition

Problem:

Ontology competition can become another prose comparison unless every survivor faces the same tests.

Improvement:

Create a fixture suite that each survivor must answer.

Implemented:

`explorations/E005-ontology-competition-fixture-suite.md`

### RI-003: Test `Ext_S` As Potentially Load-Bearing

Problem:

The repo risks treating `<=_S` as the main residue because it looks like order, even though many personas identified `Ext_S` as the likely load-bearing component.

Improvement:

The next W000 route should require each survivor to answer whether extension rules explain more than order.

Implemented:

Updated `agent-governance/NEXT-TRIGGER-PLAN.md`.

### RI-004: Keep `C`, `<=_S`, And `Ext_S` Separately Scored

Problem:

The repo may preserve or kill SourceRealization as a bundle.

Improvement:

The next run must assign independent status to each component.

Implemented:

Updated `CLAIM-LEDGER.md`, `FORMAL-OBJECT.md`, and `NEXT-TRIGGER-PLAN.md`.

### RI-005: Make Witnessability A First-Class Test

Problem:

The RUN-0019 hidden-source fixture can become unfalsifiable if hidden source distinctions require no witness, invariant, or operational consequence.

Improvement:

Every hidden-source distinction must answer:

```text
What would witness it?
What invariant would preserve it?
What transformation would it change?
```

Implemented:

Added witnessability fixtures in `explorations/E005-ontology-competition-fixture-suite.md`.

### RI-006: Preserve The Narrative, But Keep It Out Of Claim Promotion

Problem:

The core intuition is useful, but narrative strength can inflate claim strength.

Improvement:

Place the narrative steelman in `HYPOTHESIS-STEELMAN.md` and keep the claim ledger austere.

Implemented:

`HYPOTHESIS-STEELMAN.md`

## Not Implemented

These ideas are useful but deferred:

- Add new claim IDs for `TI-C`, `TI-ORDER`, and `TI-EXT`.
- Add a full schema validator for survivor competition.
- Add more governance workflows.
- Add a permanent persona hierarchy.

Reason:

The current bottleneck is research ontology, not governance architecture. Claim decomposition may become necessary after the next run if `C`, `<=_S`, and `Ext_S` receive different statuses.

## Success Criteria For Next Run

The next run succeeds if it can say:

```yaml
C_status:
<=_S_status:
Ext_S_status:
best_survivor:
does_best_survivor_beat_NULL_SURVIVOR:
why:
next_kill_test:
```

No claim should be strengthened merely because it was steelmanned.
