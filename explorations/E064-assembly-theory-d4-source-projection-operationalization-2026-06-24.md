---
artifact_type: exploration
status: active
exploration_id: E064
run_ref: RUN-0059
created: 2026-06-24
claim_refs:
  - TI-C019
---

# E064 - Assembly Theory D4 Source / Projection Operationalization

## Purpose

Operationalize the Assembly Theory connection without collapsing the RUN-0046 distinction
between source-side issuance and projection-side bounded-access novelty.

## Definitions

Source-layer assembly index:

```text
AI_src,n(x) = minimum assembly/construction length for x using only source-layer schema,
              constructors, admissibility predicates, and proof terms formed at source
              prefix n.
```

Projection-layer assembly index:

```text
AI_proj,n(x) = minimum assembly/construction length for x using only observer-accessible
               projection schema image(P_n), exposed constructors, records, and admissibility
               predicates at prefix n.
```

## D4 Classification

```text
projection D4:
  AI_proj,n(x) undefined and AI_proj,n+1(x) defined

source D4:
  AI_src,n(x) undefined and AI_src,n+1(x) defined
  plus fixed-source aperture absorption defeated
```

## Verdict

```yaml
assembly_operationalization: useful
projection_D4_operationalized: true
source_side_issuance_proved_by_projection_AI: false
source_AI_positive_condition: AI_src,n_undefined_and_AI_src,n+1_defined_plus_fixed_source_absorber_defeated
claim_status_change: none
path_kill_added: undefined_projection_assembly_index_as_source_issuance_evidence
```

## Result

Assembly Theory is useful as a measurement vocabulary for D4-like novelty, but only after the
layer split is explicit.

A projection-layer undefined assembly index can mean:

```text
the observer did not yet have the schema, constructor, or record access needed to assemble x
```

That is compatible with the RUN-0046 fixed-source absorber:

```text
fixed Mu_infty + widening apertures P_n
```

So projection D4 is not source-side issuance evidence by itself.

## Positive Source Condition

Assembly Theory helps the source-side claim only if a candidate shows:

1. `AI_src,n(x)` is undefined,
2. `AI_src,n+1(x)` becomes defined through a source-generated extension,
3. no fixed `Mu_infty` plus projection/access schedule can precontain the source constructors
   while preserving admissibility, morphisms, proof terms, and records.

## Path Killed

```yaml
path: undefined_projection_assembly_index_as_source_issuance_evidence
reason_killed: >
  Undefined assembly index at the projection layer can be produced by bounded access to a
  fixed richer source. It operationalizes observer novelty, not source-side issuance, unless
  the source-layer assembly index also changes and fixed-source aperture absorption is defeated.
local_minimum_risk: >
  Medium. Assembly Theory remains useful as an empirical vocabulary and projection-side
  operationalization; the kill applies only to treating projection undefinedness as source
  evidence.
possible_future_resurrection_trigger: >
  A source-layer construction trace where AI_src,n is undefined, AI_src,n+1 is defined, and no
  fixed richer source can precontain the constructors, admissibility predicates, proof terms,
  and record maps.
```

## Next Work

The next run should close the burst by recording the parallelization governance pattern:

```text
W000 -> parallel_burst_mode_governance_assessment
```
