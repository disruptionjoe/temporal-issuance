---
artifact_type: absorber
status: active
governance_role: absorber_map
constitutional: false
created_by_run: RUN-0046
claim_refs:
  - TI-C019
  - TI-C020
---

# Bayesian Nonparametrics Absorber

## Absorber

Bayesian nonparametric processes such as Chinese Restaurant Process and Indian Buffet Process
models allow new clusters, classes, or latent features to appear as observations arrive.

They are a sharp absorber for Temporal Issuance's online schema-growth language because they
produce novelty-looking events from a fixed probabilistic source:

```text
fixed hyperprior / stochastic process
  -> sequence of observations
  -> new latent cluster or feature appears at prefix n
```

The observer sees an expanding effective schema. The source process may remain fixed.

## What It Explains

- Online appearance of new latent kinds.
- Prefix-relative novelty.
- Open-ended-looking feature or cluster growth.
- A formal distinction between observed categories and a richer generative process.

This maps directly onto PP-3 Hypothesis B: projection-relative novelty from a fixed richer
source.

## What It Does Not Explain

It does not explain source-side issuance unless the hyperprior, process class, or admissible
generator family itself changes in a way not specified by any prior source schema.

```yaml
absorbed:
  - new observed type from fixed hyperprior
  - finite online schema expansion as posterior disclosure
not_absorbed:
  - source-side hyperprior issuance
  - generator-kind creation not contained in the prior process class
  - AC-8-style shared source admissibility change, if independently shown
```

## Temporal Issuance Risk

If TI treats new observer-visible types as source-side issuance, Bayesian nonparametrics
absorbs the claim. The correct comparison is not:

```text
fixed finite schema vs. growing observed schema
```

but:

```text
fixed richer source process vs. source-side generator issuance
```

## Escape Condition

To escape this absorber, TI must show one of:

1. The hyperprior or process class changes by a D4 event at the source level.
2. No fixed hyperprior/process class can represent the relevant schema-extension trace while
   preserving the required admissibility, morphism, and record structure.
3. The physical source is directly shown to be an `OnlineSchemaSys`, not merely observed
   through an online posterior process.

## Relation To Prior Runs

- RUN-0041 / E018: changing the hyperprior reopens PP-1 meta-distribution regress.
- RUN-0045 / E027: constructive context formation explains why an observer cannot use unformed
  types, but not why the source lacks them.
- RUN-0046 / E029: fixed-source aperture models can produce D4 projection events without
  source expansion.
