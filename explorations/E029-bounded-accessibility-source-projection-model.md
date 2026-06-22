---
artifact_type: exploration
status: active
exploration_id: E029
run_ref: RUN-0046
claim_refs:
  - TI-C019
  - TI-C020
topic: bounded_accessibility_source_projection_model
phase: 2B
---

# E029: Bounded Accessibility Source/Projection Model

## Purpose

RUN-0045 left PP-3 as the current crux:

```text
Does D4/OnlineSchemaSys detect source-side issuance, or bounded-access disclosure from a
richer source?
```

This pass builds the two-layer fixture required by E026/E027 and processes the pending
three-lens intake actions that directly bear on PP-3.

## Verdict

```yaml
projection_d4_without_source_expansion: constructible
naa_from_projection_limits_alone: true
online_to_metaclosys_nonembedding_status: observer_access_fact_unless_source_layer_is_shown_online
d4_alone_proves_source_side_issuance: false
finite_trace_source_issuance_discriminator: not_found
ti_c019_status_effect: narrowed_not_killed
ti_c020_status_effect: pressured
next_required_test: source_side_witness_or_formal_narrowing
```

A static richer source plus a changing access aperture can produce a projection-layer
`OnlineSchemaSys` with genuine D4 events relative to the observer-accessible schema, while
the source schema does not expand. This means D4 currently measures projection-relative
novelty unless the source layer is independently shown to be online and expanding.

## Two-Layer Fixture

Define a source/projection system:

```text
Source layer:
  M_infty = (Mu_infty, K_infty)
  Mu_infty is a fixed richer source schema or completed MetaCloSys.
  K_infty is a fixed source rule or static availability relation.

Projection layer:
  O = (N, H, S, A, delta, epsilon, R)
  P_n : Mu_infty -> S_n is the access aperture at prefix n.
  S_n = image(P_n), the currently observer-accessible schema.
  epsilon_n updates P_n or exposes new source descriptors through P_{n+1}.
```

The key distinction:

```text
source expansion:      Mu_{n+1} strictly extends Mu_n
projection expansion:  image(P_{n+1}) strictly extends image(P_n)
```

D4 as currently formulated fires on projection expansion. It does not by itself say whether
`Mu_infty` expanded.

## Construction: D4 Without Source Expansion

Let the fixed source schema be:

```text
Mu_infty = {A, B, C}
```

Let access apertures be:

```text
P_0 exposes {A}
P_1 exposes {A, B}
P_2 exposes {A, B, C}
```

At prefix 0, the observer-accessible schema is `S_0 = {A}`. At prefix 1, `S_1 = {A, B}`.
Relative to `S_0`, type `B` is not an instance of any type admissible in `S_0`, and `delta_0`
has codomain over `S_0`, so it cannot produce `B` as an `S_1` type. Therefore the event
`B in S_1 \ S_0` is a D4 event in the projection layer.

But `B` was already in `Mu_infty`. The source did not expand.

This generalizes: for any finite projection trace

```text
S_0 subset S_1 subset ... subset S_k
```

a static source can be chosen as:

```text
Mu_infty = union_{i <= k} S_i
```

with `P_i` exposing exactly `S_i`. Therefore no finite D4 trace, by itself, proves source-side
issuance.

## NAA From Projection Limits

NAA follows in the projection layer if prefix operations have access only to `S_n`, `H_n`, and
the current aperture state, not to the full `Mu_infty`.

```text
delta_n, epsilon_n may use image(P_n)
delta_n, epsilon_n may not inspect Mu_infty \ image(P_n)
```

This derives the same no-reference behavior as RUN-0045's constructive-context result. The
observer/process cannot use unexposed source descriptors. But this is an access fact, not a
source-expansion fact.

## Non-Embedding Reinterpreted

RUN-0042's morphism-level non-embedding result remains correct for the projection category:
`OnlineSchemaSys` morphisms preserve prefix-indexed availability, while a plain `MetaCloSys`
category has no such structure.

E029 narrows its interpretation:

```yaml
if OnlineSchemaSys models the source:
  nonembedding_is_source_fact: possible
if OnlineSchemaSys models the projection:
  nonembedding_is_observer_access_fact: true
```

The non-embedding shows that availability-indexed processes are not plain closed
meta-schemas. It does not prove that the source itself is availability-indexed unless the
source is independently specified as an `OnlineSchemaSys`.

## Strongest Surviving Source-Side Version

The strongest source-side version of TI-C019 after this pass is:

> Reality is not merely a fixed richer source projected through widening observer apertures.
> At the source layer itself, the admissible schema or generator space genuinely extends.
> Projection-layer D4 is evidence only if paired with a source-side witness that cannot be
> represented as aperture disclosure from a fixed `Mu_infty`.

This is still coherent, but it is not established by the current D4/OnlineSchemaSys apparatus.

## Positive Source-Side Witness Requirement

A positive source-side witness must do at least one of the following:

```yaml
source_access:
  show the tested `S_n` is the source schema, not only an observer projection
static_source_obstruction:
  prove no fixed `Mu_infty` plus access apertures can reproduce the relevant trace while
  preserving the required morphisms, admissibility predicates, and records
generator_issuance:
  exhibit a new generator kind or admissibility rule not contained in any prior source
  hyperprior, grammar, or completed source schema
interaction_witness:
  show multi-observer AC-8 negotiation changes the shared source admissibility predicate,
  not merely the community's synchronized access to pre-existing descriptors
physical_witness:
  for TI-C020, identify a physical process where the observable algebra or admissible type
  schema expands in a way not representable as bounded access to a fixed Hilbert/operator
  structure
```

Without one of these, source-side issuance remains an interpretation of projection-layer
novelty.

## Path Kill

The run kills the following narrow path:

```text
D4 projection-level events as sufficient evidence for source-side issuance.
```

This does not kill D4. It kills the inference from projection-relative type novelty to
source-side type creation.

## Intake Actions Processed

### C1: Sheaf/Holonomy Identity Check

The intake's sheaf/holonomy proposal is not independent of B1/TI-C017. It is the same family
of questions in cohomological clothing:

```text
observer patches + restriction/gluing maps + nonzero H^1 / holonomy
```

RUN-0044 already found that generic sheaf/no-global-section witnesses are AB-absorbed unless
`C`-typed admissibility supplies the compatibility predicate. E029 adds the PP-3 caution:
nonzero holonomy can certify projection-access inconsistency without certifying source-side
issuance. A distinct E030-style fixture is useful only if it explicitly compares:

```text
source-side cocycle generation vs. fixed-source aperture disclosure with monodromy
```

### C3: Rivalrousness Fork

Decision:

```yaml
possibility_availability_layer: non_rival
record_finalization_layer: locally_rival_or_context_consuming
shared_legitimacy_layer: quorum_dependent
commons_language_allowed_for: finalization_and_legitimacy_only
commons_language_blocked_for: source_possibility_as_such
```

Using a possibility does not obviously deplete possibility for other observers. Treating
possibility as a common-pool resource imports scarcity that TI has not earned. Commons
language may apply later to finality, record commitment, access bandwidth, and AC-8 legitimacy
conditions, but not to possibility availability itself.

This split is another expression of PP-3: finalization and legitimacy are projection/shared-
record layer phenomena unless a source-side rivalrous resource is independently specified.

### C5: DNN / Grokking Correction

Grokking and emergent neural-network capabilities are absorbers for the soft D4 reading, not
support for source issuance.

```yaml
fixed_training_distribution_or_architecture:
  role: richer_source
learned_representation_available_to_model:
  role: projection_layer
grokking_event:
  role: projection_d4_like_schema_disclosure
source_expansion:
  not_established
```

D4-like representation jumps can occur when a fixed source distribution becomes accessible to
a bounded learner. That is PP-3 Hypothesis B at scale. A better future fixture is
grokking-vs-self-play: compare fixed-dataset disclosure against open-ended endogenous
environment generation.

### C6: Bayesian Nonparametrics Absorber

IBP/CRP-style Bayesian nonparametrics are now logged as a named absorber:

```text
new latent features or clusters appear over time, but are drawn from a fixed hyperprior.
```

This absorbs online type appearance unless the hyperprior or process class itself is issued.
If the hyperprior is allowed to change, the issue reopens PP-1 at the meta-level rather than
solving PP-3.

## Claim Effects

```yaml
TI-C019:
  status: formalizing
  effect: narrowed
  reason: D4/OnlineSchemaSys remains a formal projection/process object; source-side issuance
    now requires an explicit source witness.
TI-C020:
  status: speculative
  effect: pressured
  reason: physical-universe-as-OnlineSchemaSys cannot be inferred from observer-level D4.
TI-C017:
  status: unchanged
  effect: PP-3 caution added
  reason: sheaf/holonomy obstruction may be projection inconsistency unless C-typed
    admissibility supplies source-side compatibility.
```

## Next Work

Primary next work:

```text
source_side_witness_fixture
```

Required: pick one candidate witness class and try to prove it cannot be represented by a
fixed richer source plus access apertures. The best candidates are:

1. AC-8 formal model with quorum legitimacy and incompatible schema proposals.
2. Sheaf/holonomy source-vs-projection fixture, but only if it supplies a source-side
   compatibility predicate.
3. Grokking-vs-self-play fixture as the cheap empirical proxy for projection disclosure vs
   endogenous source change.

Secondary:

```text
assembly_theory_D4_operationalization_with_source_projection_split
```

Assembly Theory should not be used as issuance evidence until schema-relative assembly index
is defined separately at source and projection layers.
