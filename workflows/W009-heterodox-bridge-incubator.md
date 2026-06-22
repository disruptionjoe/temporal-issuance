---
artifact_type: workflow
workflow_id: W009
status: active
governance_role: heterodox_bridge_incubator
category: explore
constitutional: false
created_by_run: RUN-0030
related_workflows:
  - W008-bridge-or-definitive-kill.md
relationship_to_w008: |
  W009 is the construction-first companion to W008.
  W008 enumerates escape routes and tests them adversarially.
  W009 runs BEFORE adversarial testing: it builds the strongest
  possible mechanism for a bridge idea before W008 stress-tests it.
  W009 output feeds directly into W008 Phase 3 (Construction Attempt).
  Invoke W009 when a bridge is intuitively attractive but formally weak.
  Invoke W008 when obstructions need escape-route audit.
---

# W009: Heterodox Bridge Incubator

## Purpose

Many research programs fail because they protect weak ideas.

Many formal research programs fail because they kill unusual ideas before those ideas become precise
enough to evaluate.

This workflow exists to solve the second problem.

Its purpose is not:
- validation
- falsification
- contradiction hunting
- claim downgrading

Its purpose is:

> Build the strongest possible mechanism by which an unusual idea could be true.

Only after a coherent mechanism exists should normal contradiction-hunting and theorem-proving
workflows engage.

## Workflow Classification

```
Category: explore
Relationship to existing workflows:

  Heterodox Bridge Incubator (W009)
          ↓
  Theory Compression
          ↓
  Theory Tournament
          ↓
  Contradiction Hunter / W008 Bridge-or-Definitive-Kill
```

Incubation happens before adversarial review.

W009 complements W008:
- W009 builds the strongest possible bridge mechanism for an idea
- W008 audits escape routes and applies the anti-local-minimum gate

## Workflow Card

```yaml
workflow_id: W009
status: active
purpose: Build the strongest possible mechanism for a bridge idea before adversarial testing
trigger_conditions:
  - a hypothesis repeatedly survives informal discussion
  - a bridge is intuitively attractive but formally weak
  - contradiction workflows are killing ideas faster than mechanisms are being built
  - a proposal appears potentially important but lacks intermediate lemmas
  - RUN-0030 synthesis identifies a constructive route not yet tried
input_surfaces:
  - current repo state
  - 62-persona steelman synthesis (from W007 pass)
  - escape-route taxonomy (from W008)
  - HYPOTHESIS-STEELMAN.md
  - memory/steward-memory-summary.md
  - CLAIM-LEDGER.md
expected_outputs: run record, bridge lemma list, toy models, strongest mechanism, failure analysis
retirement_condition: retire if it consistently produces weak bridges that fail Phase 6 without generating
  new bridge lemma candidates
```

## Entry Conditions

Use this workflow when:

- a hypothesis repeatedly survives informal discussion
- a bridge is intuitively attractive but formally weak
- contradiction workflows are killing ideas faster than mechanisms are being built
- a proposal appears potentially important but lacks intermediate lemmas

Examples:

- Temporal Issuance -> spacetime
- Temporal Issuance -> GU
- Temporal Issuance -> mass-energy
- Time as Finality -> physics
- observer structure -> cosmology
- legitimacy -> physical settlement analogies

## Core Rule

Assume for the duration of the workflow: **There exists a coherent mechanism.**

Do not assume the mechanism is true.

Do not assume the mechanism is physical.

Assume only that one exists.

The task is to discover what it would look like.

## Phase 1: Strongest Intuition Extraction

Construct the strongest possible version of the motivating intuition.

**Prohibited:** criticism, debunking, contradiction hunting

**Required output:** What is the strongest version of the idea?

Source material for this phase:
- The W007 heterodox panel synthesis (Persona panel consensus on strongest routes)
- Prior steelman passes
- Prior run records that identified the best surviving formal structure

Questions to answer in Phase 1:
1. What is the core intuition, stripped of all specific physics machinery?
2. What makes this intuition feel like it might be pointing at something real?
3. What is the most minimal formal object that captures the intuition?
4. Which domains outside physics give examples of the same structure?

## Phase 2: Mechanism Construction

Replace metaphors with candidate structures.

**Examples:**
```
Instead of: observers render reality
Produce: observer-accessible record stabilization process

Instead of: issuance creates energy
Produce: extension stabilization carries conserved cost functional
```

**Required output:** Candidate mechanism(s)

For each candidate mechanism:
- Name the formal objects precisely
- State the admissibility rule
- Identify what the mechanism would predict differently from current absorbers
- Identify what mathematical structure carries the new invariant

Produce at least 3 candidate mechanisms.

## Phase 3: Bridge Lemma Discovery

Identify all missing intermediate steps.

**Required format:** Bridge Lemma 1, Bridge Lemma 2, ...

For each lemma:
- Statement: what the lemma claims
- Why needed: what bridge step it provides
- Current status: proved / unproved / unknown
- Possible formalization: candidate mathematical form
- Dependencies: what other lemmas it requires

This phase is deliberately constructive. Do not kill lemmas in this phase.
Record even obviously weak lemmas — they may become constraints later.

## Phase 4: Specialist Divergence

Spawn specialist teams:

**Team A — Physics:** relativity, quantum theory, scattering, field theory
- Check whether any known physics result proves or disproves each bridge lemma
- Identify analogues in known physical theories
- Suggest the weakest physical assumptions sufficient for each lemma

**Team B — Mathematics:** category theory, topology, geometry, dynamical systems
- Identify the formal structure required for each bridge lemma
- Check for existing theorems that prove or imply the lemma
- Suggest the weakest mathematical conditions for each lemma

**Team C — Complex Systems:** emergence, self-organization, constraint propagation
- Identify whether the bridge mechanism appears in known complex systems
- Suggest discrete or simulation-level analogues for each bridge lemma

**Team D — Information Theory:** compression, reconstruction, observer dependence, entropy
- Identify information-theoretic analogues for each bridge lemma
- Check whether the mechanism can be stated as an information-theoretic result
- Identify which bridge lemmas have information-theoretic kill conditions

**Team E — Heterodox Synthesis:** build strongest surviving mechanism from A-D outputs
- Identify the highest-leverage combination of A-D results
- Propose modifications to the bridge lemma list based on A-D divergences
- Synthesize the strongest single mechanism from the A-D outputs

## Phase 5: Toy Models

Construct candidate toy models.

**Requirements:**
- finite: defined over a finite state space or finite constraint set
- executable if possible: can be computed by hand or by code
- falsifiable: has at least one explicit falsification condition

**Required output:** Toy Model A, Toy Model B, Toy Model C

For each toy model:
- State space: what are the objects?
- Extension rule: what are the admissible morphisms?
- Invariant: what is the proposed bridge invariant?
- Target: what physics quantity does the invariant map to?
- Prediction: what would the toy model predict differently from absorbers?
- Falsification condition: what result would kill the toy model?

## Phase 6: Failure Analysis

Only now perform criticism.

For each bridge lemma from Phase 3:
- Strongest support: what evidence supports the lemma?
- Strongest failure mode: what would kill the lemma?
- Strongest obstruction: does any known theorem obstruct the lemma?
- Status verdict: **Survives / Weak / Blocked / Unknown**

Do not perform Phase 6 analysis before Phase 5 is complete.
Criticism before construction produces premature closure.

## Final Artifact

Produce the following as a standalone artifact (also referenced from the run record):

```yaml
Strongest Mechanism: |
  [most coherent surviving bridge — full formal statement]

Bridge Lemmas:
  - BL-001: statement | status | dependencies
  - BL-002: ...
  - (full list)

Existing Analogues:
  - [relevant mathematical or physical precedent: name, reference, relevance]
  - ...

Toy Models:
  - TM-A: [state space | extension rule | invariant | falsification condition]
  - TM-B: ...
  - TM-C: ...

Resurrection Triggers:
  - [what future discovery would revive the bridge]
  - ...

Kill Conditions:
  - [what future result would permanently retire the bridge]
  - ...

Recommended Next Step: |
  [highest expected-value move after this W009 pass]

BDO_ICO_Evasion: |
  [does any bridge lemma or mechanism evade BDO or ICO by relaxing their assumptions?]

W008_Escape_Routes_Implicated: |
  [which W008 Categories A-H does this W009 pass suggest pursuing?]

New_Claims_Warranted:
  - claim: |
      [claim statement]
    status: speculative
    depends_on: [bridge lemma list]
```

## Output Format

Every W009 run should produce:

- a normal run record under `agent-runs/`
- Phase 1-6 outputs in the run record
- a standalone exploration file under `explorations/` containing the Final Artifact
- candidate claim-ledger entries at status `speculative` only
- updates to `memory/path-kills.md` if Phase 6 produces immediate precise obstructions
- update to `NEXT-TRIGGER-PLAN.md` with the recommended next step
- standard memory and metrics updates

## Memory And Merge Surfaces

After W009, update as applicable:

- `explorations/` (Final Artifact)
- `CLAIM-LEDGER.md` (new speculative claims only)
- `memory/path-kills.md` (Phase 6 immediate kills only)
- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `agent-governance/STEWARD-METRICS.md`

## Guardrails

- Phases 1-5 are construction-only. No criticism, no killing, no absorber comparison.
- Phase 6 is the only adversarial phase.
- Bridge lemmas that are immediately killed in Phase 6 with a precise obstruction go to
  `memory/path-kills.md`. Bridge lemmas that survive or are Unknown remain in the Final Artifact.
- New claims warranted by the bridge lemma list are added to `CLAIM-LEDGER.md` at status
  `speculative` only. Do not promote.
- W009 termination does not mean the bridge is dead. It means the incubation pass is complete.
  The bridge proceeds to W008 for escape-route audit.
- A W009 run that produces 0 surviving bridge lemmas is a valid outcome. Record it honestly.

## Design Hypothesis

W009 itself is a research-governance hypothesis:

> Unusual ideas that repeatedly survive informal discussion but lack precise mechanism can be
> made formally evaluable by first building the strongest possible mechanism, then applying
> contradiction-hunting. Killing before building produces premature closure.

If W009 consistently produces bridge lemmas that are immediately killed in Phase 6, it may be
eliminating ideas too slowly. Narrow the Phase 1-5 construction scope.

If W009 consistently produces bridge lemmas that survive Phase 6 and feed into W008, preserve
and expand it.
