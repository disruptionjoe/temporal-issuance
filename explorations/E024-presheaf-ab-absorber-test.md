---
artifact_type: exploration
status: active
exploration_id: E024
run_ref: RUN-0044
claim_refs:
  - TI-C017
  - TI-C019
topic: presheaf_grothendieck_fibration_and_ab_absorber_test
phase: 2B
---

# E024: Presheaf / Grothendieck Fibration + AB Absorber Test

## Purpose

RUN-0043 identified the presheaf / Grothendieck fibration absorber as the critical path
threat to `OnlineSchemaSys`. E021 augmented that threat with the Abramsky-Brandenburger
(AB) sheaf contextuality question:

```text
G_ij gluing obstruction
  = AB sheaf contextuality
  = NAA / no pre-existing global assignment
  = OnlineSchemaSys not embedded in MetaCloSys
```

This run asks whether that convergence is full absorption or a useful formal home with a
surviving Temporal Issuance surplus.

## Verdict

```yaml
presheaf_fibration_absorber: partial_success
static_schema_indexing_absorbed: true
online_constructibility_absorbed: false
naa_as_standard_fibration_theorem: false
ab_absorbs_naa_structural_theorem: false
ab_remains_threat_to_generic_cech_witness: true
ti_c019_result: formalizing_candidate_survives
ti_contribution: online_constructible_fibration_boundary
next_required_test: hott_or_constructive_type_derivation_of_online_constructibility
```

The absorber succeeds against any claim that prefix-indexed schema availability is novel
category theory. It fails against the stronger claim that `OnlineSchemaSys` is merely a
standard fibration with no additional online construction boundary.

## Strongest Absorber Version

The strongest fibration absorber says:

> An `OnlineSchemaSys` is a category fibered over the prefix poset `N`. Objects are pairs
> `(n, x)` where `x` is schema data available at prefix `n`. Reindexing along `n <= m`
> gives restriction from later schema to earlier prefix. Schema growth is the corresponding
> opfibration direction. NAA is just the usual condition that morphisms live in the
> appropriate fiber and preserve base projection. D4 is a vertical change or non-cartesian
> fiber transition. Therefore TI is naming standard fibred category / presheaf machinery.

The strongest AB absorber says:

> NAA and the `OnlineSchemaSys` non-embedding result are both obstruction-to-global-section
> facts. AB already gives the theorem: local sections can be compatible while no global
> section exists. TI-C017's Cech witness classes are AB contextuality in different language.

These are strong enough that a weak response would be local-minimum protection. The response
must identify exact absorbed structure and exact residue.

## Formal Skeleton

Let `N` be the prefix poset. A completed `OnlineSchemaSys` determines at least two standard
categorical objects:

1. A retrospective presheaf

```text
S : N^op -> Schema
```

where `S(n) = S_n` and restriction along `n <= m` forgets schema elements unavailable at
prefix `n`.

2. A growth opfibration

```text
p : E -> N
```

where the fiber over `n` contains schema-availability states at prefix `n`, and chosen
growth morphisms over `n -> n+1` encode `epsilon_n` events.

So the absorber is correct about the static and retrospective structure:

```yaml
absorbed_by_fibration:
  - prefix-indexed schema availability
  - restriction from later schemas to earlier prefixes
  - schema growth as opcartesian or non-cartesian transition data
  - availability-sensitive morphisms as base-preserving morphisms
```

This is not a problem; it is a formal home. The question is whether NAA is only this.

## Why NAA Is Not A Standard Fibration Theorem

A Grothendieck fibration supplies reindexing structure. It does not by itself constrain
how the transition or growth operation is defined.

In particular, a fibration can be specified from a completed global object. One may define
all fibers and all reindexing maps with full knowledge of the total trajectory. That is
ordinary mathematics and is often the point of the external description.

NAA is different. It is an operational boundary on the *definition and use* of the maps:

```text
delta_n, epsilon_n may reference only H_n, S_n, and objects constructible from them.
```

The fibration can represent the resulting availability structure after the fact. It does not
enforce that `epsilon_n` was defined without consulting future fibers, a completed library,
a hidden global section, or a universal meta-schema.

Therefore:

```yaml
naa_is_not:
  - mere base preservation
  - mere cartesian lifting
  - mere fibredness
  - mere absence of a global section
naa_is:
  - an online constructibility constraint on operation formation
  - a no-future-fiber-oracle condition
  - an internal/process-capacity boundary rather than an external representation boundary
```

The right formal refinement is:

```text
OnlineSchemaSys = online constructible fibration / opfibration over N
```

where "online constructible" is additional structure:

```yaml
online_constructible_fibration:
  base: prefix poset N
  fibers: schema states S_n and histories H_n
  growth: epsilon_n over n -> n+1
  dynamics: delta_n internal to the current fiber
  records: R_n on H_n
  construction_boundary: epsilon_n and delta_n are definable from current-fiber data only
  forbidden_oracles:
    - future fibers S_m for m > n
    - completed total trajectory
    - hidden global section
    - universal meta-schema used as an operational oracle
```

## What The Fibration Absorber Does Kill

The following stronger novelty claims should not be made:

```yaml
killed_or_absorbed:
  - prefix-indexed schemas are novel category theory
  - availability over N is not already presheaf/fibration structure
  - morphism-level availability preservation is unexplained by standard category theory
  - D4 needs a new categorical base just to express schema growth
```

These are standard. TI should use this machinery rather than pretending to have invented it.

## What Survives

The surviving claim is narrower and cleaner:

> TI's formal surplus is not fibredness. It is the interpretation and formal discipline of
> an online constructibility boundary on schema-growth operations inside a fibered/presheaf
> representation.

This preserves the RUN-0042 result but narrows it:

```yaml
old_wording: OnlineSchemaSys is categorically non-embeddable in MetaCloSys
better_wording: >
  The online constructible structure of OnlineSchemaSys is not preserved by a forgetful
  completed-history encoding into MetaCloSys, because that encoding drops the internal
  operation-formation boundary even if it retains all completed object data.
```

That is enough to block full absorption. It is not enough for promotion. The next proof
burden is to derive the construction boundary from constructive type formation, HoTT, or
another precise formal system.

## AB Contextuality Test

AB contextuality concerns a sheaf of local measurement outcome assignments over a cover of
contexts. Contextuality appears when compatible local sections fail to extend to a global
section.

The NAA theorem in `OnlineSchemaSys` is not the same theorem:

```yaml
ab_contextuality:
  base: measurement contexts / cover
  central obstruction: no global section compatible with local sections
  local data: outcome assignments or distributions
  theorem shape: local compatibility does not imply global assignment

online_schema_sys_naa:
  base: prefix poset N
  central boundary: current operations may not use future schema data
  local data: current schema/history and constructible operations
  theorem_shape: schema-extension events are D4 events because delta_n has codomain S_n
```

Over a simple linear prefix base, a completed run usually has a global trajectory in the
external mathematical description. NAA does not deny that. It denies that the operation at
prefix `n` may use that global trajectory as an oracle.

So:

```yaml
naa_reduces_to_ab: false
reason: AB is about nonexistence of global sections; NAA is about non-use of future/global data by prefix operations.
```

However, the AB absorber remains serious for TI-C017. If TI-C017 only says "there are local
sections with no global section" or "a Cech class detects the obstruction," then it is AB /
standard sheaf cohomology. TI-C017 survives only if C-typed admissibility independently
determines the sheaf or compatibility predicate in a way not supplied by a generic AB model.

## Result For TI-C017

```yaml
ti_c017_status: speculative_but_narrowed
absorbed_part: generic Cech or no-global-section witness
surviving_part: C-typed admissibility may determine the sheaf/compatibility predicate
next_action: do not run Cech witness as novelty until C-typed admissibility supplies the sheaf data
```

## Result For TI-C019

TI-C019 survives the B1 absorber. The claim should move from "speculative with formalizing
trajectory" to "formalizing" only in the following narrowed sense:

```text
The object being formalized is not a novel fibration. It is an online constructible
fibration/presheaf process where NAA is an operation-formation constraint.
```

The strongest objection after this run is no longer "OnlineSchemaSys may just be a standard
Grothendieck fibration." The stronger objection is:

> Online constructibility may itself be derivable from ordinary constructive type theory,
> HoTT universe discipline, or computational sequentiality, leaving TI as an interpretation
> layer over known formal systems.

That is the correct next absorber. It is B3, sharpened by this run.

## Closeout Verdict

```yaml
b1_resolved: yes_partial_absorption_with_surplus_identified
archive_ti_c019: no
promote_ti_c019: no
advance_ti_c019_to_formalizing: yes_narrowly
next_primary: hott_constructive_type_derivation_of_online_constructibility
next_secondary: assembly_theory_d4_operationalization
next_tertiary: ac8_formal_model_with_legitimacy_condition
```
