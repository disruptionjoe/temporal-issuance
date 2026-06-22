---
artifact_type: cross_repo_context_protocol
status: active
governance_role: local_minimum_escape
constitutional: false
last_updated_by: RUN-0015
---

# Cross-Repo Context Protocol

## Purpose

Let Temporal Issuance use prior thinking from adjacent repos without merging projects or importing claims as true.

Relevant context repos:

- `time-as-finality`
- `gu-formalization`

## Boundary

These repos are context and local-minimum escape surfaces. They are not authority for Temporal Issuance claims.

Do not:

- merge claim ledgers
- promote Temporal Issuance claims because another repo has adjacent work
- copy governance or formalism wholesale
- treat prior work as proof

Do:

- inspect adjacent threads when stuck
- use them to find category errors, missing tests, or escape routes
- cite exact source files when a run relies on them
- record whether the context weakens, redirects, or sharpens the current path

## When To Consult

Consult adjacent repos when:

- W002 or W003 hits a local minimum
- `G_ij`, `Omega_ij`, access, cadence, records, or gluing look like time-as-finality machinery
- no-go theorem language appears too broad
- the steward is treating an absorber as dispositive without checking class assumptions
- a toy model looks like a known prior pattern

## Initial Context Handles

### Time As Finality

Use for:

- observer-indexed records
- local-to-global D1 restriction systems
- local persistence
- reconciliation lag
- gluing constraints
- issuance-to-finality projection tests

Initial source handle:

- `../time-as-finality/explorations/temporal-issuance-bridge-v0.1.md`

Current lesson:

Temporal Issuance may be source-side realization order while Time as Finality is observer-facing readout and falsification language.

### GU Formalization

Use for:

- class-relative no-go handling
- specification obligations before defending a substrate claim
- persona dialectic and heterodox escape routes
- source/control-case discipline

Initial source handles:

- `../gu-formalization/README.md`
- `../gu-formalization/OVERVIEW.md`
- `../gu-formalization/canon/six-axis-specification-protocol.md`
- `../gu-formalization/canon/no-go-class-relative-map.md`

Current lesson:

No-go results should be handled by their exact assumptions and known class exits. Candidate substrate programs should be specified before they are defended.

## Output Requirement

Any run that uses cross-repo context should record:

```yaml
context_repo:
source_file:
why_consulted:
what_helped:
what_did_not_transfer:
effect_on_temporal_issuance:
```

## Current Local-Minimum Escape Targets

- If `G_ij` and `Omega_ij` collapse into record gluing, consult time-as-finality bridge and D1 restriction work.
- If `lambda_i` remains decorative, consult GU-style specification discipline before defending a new substrate measure.
- If relativity or causal-set no-go pressure is treated too broadly, consult GU's class-relative no-go handling.
