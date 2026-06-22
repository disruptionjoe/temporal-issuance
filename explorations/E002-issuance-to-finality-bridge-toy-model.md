---
artifact_type: exploration
status: active
governance_role: bridge_toy_model
exploration_id: E002
last_updated_by: RUN-0019
claim_refs:
  - TI-C001
  - TI-C003
constitutional: false
---

# E002: Issuance To Finality Bridge Toy Model

## Purpose

Test whether the current survivor from RUN-0014, especially `G_ij`, `Omega_ij`, and weak ordinal `kappa_i`, belongs on the Temporal Issuance source side or on the Time as Finality observer-readout side.

This is a finite toy model. It is not a physics model and does not promote any claim.

## Context Used

```yaml
context_repo: time-as-finality
source_file: ../time-as-finality/explorations/temporal-issuance-bridge-v0.1.md
why_consulted: RUN-0018 routed the next W000 cycle to an issuance-to-finality bridge test.
what_helped: The source/readout split and the projection-sufficiency fixture list.
what_did_not_transfer: Time-as-finality claim statuses, TaF theorem claims, and any authority over Temporal Issuance claims.
effect_on_temporal_issuance: Forced the survivor to choose between source-side structure and observer-side readout machinery.
```

## Bridge Object

Separate source structure from observer projection:

```text
SourceRealization S = (
  C,          finite constraints
  <=_S,       source dependency / fixation order
  Ext_S       allowed source extensions
)

ObserverReadout_i = (
  A_i,        accessible constraints
  kappa_i,    ordinal record-update relation
  Rec_i       generated observer records
)

pi_TaF(S, i) = ObserverReadout_i

G_ij: partial reconciliation map between Rec_i and Rec_j
Omega_ij: obstruction record when reconciliation is partial, delayed, or conflicting
```

The bridge asks whether `pi_TaF` preserves source-side structure or whether it only produces observer-side finality records.

## Fixtures

### F1: Same Issuance, Different Cadence

Source:

```text
C = {c0, c1, c2}
c0 <=_S c1
c0 <=_S c2
```

Readouts:

```text
kappa_A: c0 -> c1 -> c2
kappa_B: c0 -> {c1, c2}
```

Result:

The source order is unchanged, but observer finality granularity differs. `kappa_i` changes the readout, not the source realization order.

### F2: Same Records, Different Hidden Issuance

Source S1:

```text
c0 <=_S c1
c0 <=_S c2
```

Source S2:

```text
c0 <=_S c1
c1 <=_S h
h <=_S c2
h not in A_i
```

Readout:

```text
Rec_i = {record(c0), record(c1), record(c2)}
```

Result:

If hidden constraint `h` is inaccessible and no record certifies the hidden dependency, the same observer records can come from different source structures. The projection is not faithful. Time-as-finality readout does not by itself kill a source-side realization order, but the source order still needs an independent type.

### F3: Same Source And Records, Different Measure

Source:

```text
C = {c0, c1, c2}
c0 <=_S c1
c0 <=_S c2
```

Candidate measures:

```text
mu_count(C) = 3
mu_weighted(C) = 5
```

Result:

The projection and gluing outputs do not change. In this bridge, `mu` remains decorative unless it changes allowed source extensions, observer capabilities, or a falsifiable invariant.

### F4: Nonmonotone Access Loss

Source:

```text
C grows monotonically from {c0, c1} to {c0, c1, c2}
```

Observer access:

```text
A_i before boundary change = {c0, c1, c2}
A_i after boundary change = {c0, c1}
```

Result:

The source is not undone, but the observer readout loses certification of `c2`. Finality data is observer-boundary dependent. Monotone source realization and monotone record availability are different claims.

### F5: Gluing Failure

Readouts:

```text
Rec_A = {record(c0), record(c1), record(x)}
Rec_B = {record(c0), record(c1), record(y)}
```

Reconciliation:

```text
G_AB(record(c0)) = record(c0)
G_AB(record(c1)) = record(c1)
G_AB(record(x)) = undefined
G_AB(record(y)) = undefined

Omega_AB = {record(x), record(y): no certified common source constraint}
```

Result:

`G_ij` and `Omega_ij` are necessary to state readout failure. They expose lost or conflicting source information, but they do not generate the source realization order.

## Strongest Version Before Attack

Temporal Issuance can say that there is a source-side realization structure whose observer projections become finality records. Time as Finality then audits what observers can reconstruct, while `G_ij` and `Omega_ij` expose projection loss or gluing obstruction.

This strongest version avoids the backwards claim that records create the source arrow.

## Attack

The pieces that survived RUN-0014 are mostly projection-side:

- `kappa_i` changes record-update presentation without changing source realization.
- `G_ij` reconciles observer-local records after projection.
- `Omega_ij` records projection or reconciliation failure.
- `mu` does no work in the bridge unless it changes extension rules or an invariant.

The only source-side residue is `<=_S`, the realization dependency order. That residue is still under severe absorber pressure from causal order, dependency order, causal-set growth, hidden-variable bookkeeping, and ordinary record-generation machinery.

## Verdict

`G_ij`, `Omega_ij`, and `kappa_i` should not be treated as source-side Temporal Issuance primitives after this bridge. They survive as observer-readout, reconciliation, and audit machinery.

Temporal Issuance is not fully absorbed by this toy model because F2 shows that observer finality projection can be non-faithful: same records can hide different source structures. But that only preserves a burden, not a victory. The next object must independently type `<=_S` and `Ext_S` without causal order, ordinary time, entropy, information, or record finality doing the real work.

## Claim Effects

- No claim is promoted.
- TI-C003 remains weakened.
- The source-side reading of `G_ij`, `Omega_ij`, and `kappa_i` is killed unless a future model shows these components constraining source extensions rather than observer readouts.
- Generic `mu` remains outside the core.

## Next Test

Build a source-order absorption discriminator:

```text
Can <=_S and Ext_S be specified so that they do not factor through causal order, ordinary dependency order, record generation, entropy, information, probability, volume, or action?
```

If not, the remaining Temporal Issuance formal object should be absorbed or archived.
