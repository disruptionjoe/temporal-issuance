---
artifact_type: workflow
workflow_id: W007
status: active
governance_role: steelman_hegelian_persona_pass
constitutional: false
origin_run: agent-runs/RUN-0022-taf-persona-steelman-hegelian-pass.md
design_hypothesis: A full steelman and Hegelian persona pass improves falsification by making the target stronger before it is attacked.
---

# W007: Steelman And Hegelian Persona Pass

## Purpose

Use the full Time as Finality persona set to build the strongest possible version of the core hypothesis or current survivor before the repo attempts another kill, absorption, or ontology-competition pass.

This workflow exists because the steward should not kill a weak version of the idea. It should assume the hypothesis is true long enough to generate the strongest version, then return that stronger target to hostile testing.

## Workflow Card

```yaml
workflow_id: W007
status: active
purpose: Steelman the core hypothesis or current survivor through all available Time as Finality personas, then synthesize research improvements.
trigger_conditions: before major kill pass, after repeated absorption, before ontology competition, when the target seems underdeveloped, when Joe asks for strongest possible version
input_surfaces: current Temporal Issuance state, hypothesis, steelman file if present, memory, claim ledger, formal object, recent run records, fixture suites, Time as Finality personas
personas: all clearly defined Time as Finality personas, defaulting to the 62 numbered expert personas when available
memory_pack: project memory plus current strongest version and strongest objection
expected_outputs: run record, full persona steelman pass, heterodox panel synthesis, research improvements, bounded implementation of improvements
merge_surfaces: hypothesis steelman, research improvement files, fixture suites, memory, claim-ledger recommendations, next-trigger recommendations, metrics
retirement_condition: retire or narrow if it starts protecting the hypothesis instead of strengthening the target for falsification
```

## Trigger Conditions

Invoke W007 when any of these conditions appears:

- the next major run would kill or absorb a survivor whose strongest form has not been stated
- repeated absorber pressure may have made the repo too deflationary
- the current survivor is being attacked as a thin formal object, but may have a stronger narrative or constructive formulation
- the repo needs a shared target before ontology competition
- Joe asks for a steelman, Hegelian pass, or constructive persona assessment
- the steward suspects the repo is killing straw versions

This workflow should not run on a fixed cadence. It should run when a stronger target would make the next falsification more honest.

## Input Surfaces

Required:

1. `HYPOTHESIS.md`
2. `HYPOTHESIS-STEELMAN.md`, if present
3. `memory/steward-memory-summary.md`
4. `memory/steward-memory-log.md`
5. `CLAIM-LEDGER.md`
6. `FORMAL-OBJECT.md`
7. relevant recent run records
8. `agent-governance/NEXT-TRIGGER-PLAN.md`
9. Time as Finality persona definitions

Optional when relevant:

- `FORMAL-OBJECT-PRESSURE-MATRIX.md`
- `FORMAL-OBJECT-PRESSURE-RESULTS.md`
- `FORMAL-DEFINITION-REPAIR.md`
- `explorations/` fixture suites
- `absorbers/`
- adjacent-repo context surfaces for time-as-finality and gu-formalization

## Persona Inventory

Default persona source:

- every numbered expert persona from `../time-as-finality/personas/EXPERT-PANEL.md`, if available

If the Time as Finality persona definitions are not centralized, search that repo for:

- persona registries
- persona goal runs
- persona future-run goals
- prior persona references
- lens registries

Use every clearly defined persona found. Record the inventory used and any missing or ambiguous personas.

## Phase 1: Persona Steelman Pass

Each persona answers independently:

1. Steelman of the core hypothesis or current survivor.
2. Steelman narrative explanation in plain English.
3. How this could be possible without collapsing into obvious absorbers.
4. Hegelian analysis, including thesis, antithesis, and synthesis.
5. Heterodox next-step opinion that could improve the research path.

The persona should not use the steelman to protect the hypothesis. The point is to create the strongest test target, not to promote the claim.

## Phase 2: Heterodox Panel Synthesis

After all persona answers, synthesize a heterodox panel opinion.

The synthesis should identify:

- strongest constructive version
- strongest narrative version
- strongest "how this is possible" route
- most important Hegelian syntheses
- heterodox next steps that cut across personas
- constructive ideas that should become test fixtures
- ideas that belong in the steelman surface but not in claim promotion
- ideas that should be killed, archived, or challenged by the next run

## Phase 3: Research Improvements Synthesis

Draft a research improvements artifact when the pass produces actionable improvements.

The improvements file should separate:

- immediate improvements
- next-run improvements
- delayed improvements
- things to explicitly avoid
- claim-ledger implications
- formal-object implications
- fixture-suite implications
- daily review questions for Joe

The improvements should keep governance subordinate to research unless the run reveals a concrete governance failure.

## Phase 4: Bounded Implementation

When improvements are obvious and low-risk, implement them in the same run.

Suitable bounded implementations include:

- updating `HYPOTHESIS-STEELMAN.md`
- creating or revising a fixture suite
- clarifying `FORMAL-OBJECT.md`
- adding next-run requirements to `agent-governance/NEXT-TRIGGER-PLAN.md`
- updating memory and metrics
- adding daily review questions

Avoid major governance expansion, new constitutional protections, or broad refactors unless the run discovers an urgent failure.

## Output Format

Every W007 run should produce:

- a normal run record under `agent-runs/`
- persona inventory used
- missing or ambiguous personas, if any
- full Phase 1 persona answers
- Phase 2 heterodox panel synthesis
- Phase 3 research improvements synthesis
- list of improvements implemented
- list of improvements queued
- next W000 route recommendation
- claim-ledger update recommendations
- memory update recommendations
- daily review questions for Joe

When Joe asks for a copy-paste artifact or the result is meant for external review, also produce the exact same report inside a single Markdown code block.

## Memory And Merge Surfaces

After W007, update as applicable:

- `HYPOTHESIS-STEELMAN.md`
- `explorations/`
- `FORMAL-OBJECT.md`
- `CLAIM-LEDGER.md`
- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `memory/daily-review/`
- `agent-governance/STEWARD-METRICS.md`

Do not promote a claim merely because the steelman is stronger. A stronger formulation is a better target, not a verdict.

## Guardrails

- Steelman first, then attack later.
- Do not treat persuasive narrative as evidence.
- Keep poetic or metaphorical language out of claim promotion.
- Preserve absorber threats in the same artifact as the steelman.
- Keep `NULL-SURVIVOR` live when testing the output.
- Use the steelman to sharpen fixtures, not to protect the survivor.
- Keep governance changes out of scope unless there is a concrete process failure.

## Design Hypothesis

W007 itself is a research-governance hypothesis:

> Falsification becomes stronger when the repo first builds the best version of the target from many expert perspectives, then submits that target to fixture-based and absorber-based pressure.

If W007 makes the repo too protective, narrow it or require an immediate kill pass afterward. If it repeatedly improves test quality, preserve it as a pre-kill and pre-competition workflow.
