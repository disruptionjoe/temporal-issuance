---
artifact_type: workflow
workflow_id: W006
status: active
governance_role: divergent_persona_convergence_check
constitutional: false
origin_run: agent-runs/RUN-0020-taf-persona-divergent-assessment.md
design_hypothesis: A full divergent persona pass improves verdict quality when the repo may be converging on a survivor too quickly.
---

# W006: Divergent Persona Convergence Check

## Purpose

Use the full Time as Finality persona set as generators of alternative framings before the repo accepts a narrowed survivor.

This workflow exists to test whether Temporal Issuance has converged too quickly. It should expand the search space first, then evaluate convergence. It is not a generic criticism pass and it is not an absorber map by another name.

## Workflow Card

```yaml
workflow_id: W006
status: active
purpose: Test premature convergence by generating alternative survivor framings through the full Time as Finality persona set.
trigger_conditions: survivor lock-in risk, narrow remaining residue, repeated absorption, source-object convergence, steward uncertainty about local minima
input_surfaces: current Temporal Issuance state, memory, claim ledger, formal objects, relevant run records, absorber files, next trigger plan, Time as Finality personas
personas: all clearly defined Time as Finality personas, defaulting to the 62 numbered expert personas when available
memory_pack: project memory plus persona inventory notes from the source repo
expected_outputs: run record, persona inventory, divergent persona answers, alternative survivor list, convergence recommendation, next W000 route
merge_surfaces: memory, claim-ledger recommendations, next-trigger recommendations, daily review questions, metrics
retirement_condition: retire or narrow if the workflow repeatedly produces no alternatives beyond already-known survivor lanes
```

## Trigger Conditions

Invoke W006 when any of these conditions appears:

- the repo has narrowed to one survivor or one dominant formulation
- a component survived because other components were killed, not because it produced hard output
- the next trigger would run a narrow absorption discriminator without first generating alternatives
- the steward suspects survivor attachment
- several personas or absorbers warn about local-minimum risk
- the current survivor may be a shadow of richer structure
- Joe asks whether the repo has converged too quickly

This workflow should not run on a fixed cadence. It should run when divergent generation is the highest-learning move.

## Input Surfaces

Required:

1. `memory/steward-memory-summary.md`
2. `memory/steward-memory-log.md`
3. `CLAIM-LEDGER.md`
4. `FORMAL-OBJECT.md`
5. relevant formal pressure or definition-repair artifacts
6. relevant recent run records
7. `agent-governance/NEXT-TRIGGER-PLAN.md`
8. relevant absorber files
9. Time as Finality persona definitions

Optional when relevant:

- `HYPOTHESIS-STEELMAN.md`
- `FORMAL-OBJECT-PRESSURE-MATRIX.md`
- `FORMAL-OBJECT-PRESSURE-RESULTS.md`
- `FORMAL-DEFINITION-REPAIR.md`
- recent daily review artifacts
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

Lens registries may be used as coverage checks, but do not silently count a lens as an independent persona unless the source repo defines it that way.

## Phase 1: Divergent Persona Pass

Each persona answers independently:

1. What alternative framing of Temporal Issuance would this persona generate?
2. What has the repo prematurely converged on?
3. What would this persona try before accepting the current survivor?
4. What source object, if any, would this persona propose instead?
5. What absorber might this persona think is being overtrusted?
6. What absorber might this persona think is being underused?
7. What category error might the current repo be making?
8. What local minimum might the current repo be entering?
9. What would this persona preserve from the current narrowing?
10. What would this persona kill immediately?
11. What would this persona test next?
12. What would count as evidence that this persona's alternative is better than the current survivor?

The persona pass must generate alternatives before judging whether the current survivor remains best.

## Phase 2: Alternative Survivor Generation

Synthesize at least 10 distinct alternative survivor framings.

Include these fields for each alternative:

```yaml
name:
core_idea:
what_it_explains:
what_it_fails_to_explain:
main_absorber_threat:
category_error_risk:
first_test:
kill_condition:
```

Potential lanes include, but are not limited to:

- source realization order
- constraint extension system
- nonfaithful observer projection kernel
- causal-order residue
- dependency-order or proof-order residue
- constructor or transformability residue
- resource monotone residue
- thermodynamic boundary-condition residue
- information bottleneck or access residue
- sheaf or obstruction residue
- process algebra or event-commit residue
- complexity or emergence residue
- cryptographic witness or certification residue
- distributed provenance residue
- scale or panarchy residue
- null result or archive path

Do not include an alternative merely to fill the count. If fewer than 10 are genuinely live, say why and route the shortage to daily review.

## Phase 3: Convergent Selection

Only after Phases 1 and 2, answer:

1. Is the current survivor still the best survivor?
2. If yes, why?
3. If no, what replaces it?
4. Should the next trigger run the current planned discriminator?
5. Should the next trigger instead run a divergent-survivor test?
6. What claim-ledger changes are needed?
7. What path-kill or resurrection notes are needed?
8. What memory updates are needed?
9. What daily review questions should go to Joe?

The selection should name the leading survivor, the strongest neglected possibility, and the exact next W000 route.

## Output Format

Every W006 run should produce:

- a normal run record under `agent-runs/`
- persona inventory used
- missing or ambiguous personas, if any
- Phase 1 persona answers
- Phase 2 alternative survivor list
- Phase 3 convergence recommendation
- strongest disagreements
- strongest neglected possibility
- local-minimum warning
- recommended next W000 route
- claim-ledger update recommendations
- memory update recommendations
- daily review questions for Joe

When Joe asks for a copy-paste artifact or the result is meant for external review, also produce the exact same report inside a single Markdown code block.

## Memory And Merge Surfaces

After W006, update as applicable:

- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `CLAIM-LEDGER.md`
- `ROADMAP.md`
- `memory/path-kills.md`
- `memory/future-run-queue.md`
- `memory/daily-review/`
- `agent-governance/STEWARD-METRICS.md`

Do not promote a claim merely because it survived W006. Survival means it earned comparison, not endorsement.

## Guardrails

- Use personas as generators, not merely critics.
- Separate divergent thinking from convergent evaluation.
- Do not collapse immediately into absorber mapping.
- Do not treat existing convergence as automatically wrong.
- Do not treat existing convergence as automatically right.
- Preserve serious disagreement.
- Keep the next trigger focused on the highest-learning research move.
- Avoid governance expansion unless the run reveals a concrete governance failure.

## Design Hypothesis

W006 itself is a research-governance hypothesis:

> A large divergent persona pass can prevent survivor lock-in by forcing alternative framings into the repo before convergence is accepted.

If W006 becomes too expensive or repetitive, split it into lighter and deeper versions. If it produces weak alternatives, narrow its trigger conditions. If it repeatedly changes the best next research move, preserve it as a high-value convergence gate.
