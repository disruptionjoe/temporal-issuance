---
artifact_type: exploration
exploration_id: E067
status: active
created: 2026-06-24
run_ref: RUN-0063
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E066-ten-goal-source-shadow-finality-orchestration-2026-06-24.md
context_repos:
  - temporal-issuance
  - ../time-as-finality
---

# E067: Source / Shadow / Finality Interface Contract

## Purpose

Define the smallest reusable contract connecting Temporal Issuance
source-extension claims to Time as Finality observer-projection and
record-finality audits.

This artifact executes G01 from `E066`. It is a contract for future fixtures. It
does not promote any claim.

## Contract Boundary

Temporal Issuance owns source-side issuance questions:

```text
What, if anything, is newly admitted by the source process?
```

Time as Finality owns observer-shadow and finality questions:

```text
What can a bounded observer access, compare, preserve, lose, and treat as final?
```

This contract connects those questions without merging them.

## Minimal Interface

A candidate bridge must fill the tuple:

```text
SSF =
(
  SourceExtension,
  Projection,
  Capability,
  RecordFinality,
  LossKernel,
  AbsorberSet
)
```

If any field is missing, the candidate is not rejected. It is returned for
typing and cannot move claim status.

## 1. SourceExtension

`SourceExtension` states the proposed source-side change.

```text
SourceExtension =
(
  n,
  Y_n,
  Adm_n,
  C_n,
  delta_n,
  Y_{n+1},
  Adm_{n+1},
  C_{n+1},
  issued_object,
  source_witness
)
```

Where:

- `n` is the stage or prefix.
- `Y_n` is the source object available at stage `n`.
- `Adm_n` is the admissibility predicate at stage `n`.
- `C_n` is the construction context or schema at stage `n`.
- `delta_n` is the transition or extension event.
- `issued_object` is the claimed newly admitted structure.
- `source_witness` is the evidence that the object is source-new rather than
  merely newly visible.

### Source Issuance Gate

A `SourceExtension` is a source-issuance candidate only if it passes all four
checks:

```text
SI-1 Online availability:
  issued_object is not constructible from C_n using Adm_n.

SI-2 No hidden future schema:
  the run does not rely on a completed future schema, oracle, hidden supervisor,
  global grammar, or fixed richer source already containing issued_object.

SI-3 Admissibility growth:
  C_{n+1} or Adm_{n+1} admits a structure not available under C_n or Adm_n.

SI-4 Recordability:
  there is a source-to-record map capable of preserving enough trace for later
  projection and finality audit.
```

If SI-1 or SI-3 fails, classify the candidate as not source issuance. If SI-2
fails, classify it as fixed-source bounded-access disclosure. If SI-4 fails,
the candidate may be source-side but is not ready for observer-finality work.

### Temporal Issuance Source Fields

When the candidate is physics-facing, it must also declare the TaF source-object
fields:

```text
Y_TI = (
  R,
  <,
  mu,
  dR,
  O_i,
  kappa_i,
  A_i,
  M,
  G
)
```

Any undeclared field is treated as absorber-owned by default.

## 2. Projection

`Projection` states what an observer, instrument, agent, or repo process can
see.

```text
Projection =
(
  O,
  Sigma,
  r,
  U,
  B,
  pi_O,
  ~=_X
)
```

Where:

- `O` is the observer or access profile.
- `Sigma` is the observational schema or interface.
- `r` is resolution or fidelity.
- `U` is local domain, patch, scope, or access region.
- `B` is boundary or resource condition.
- `pi_O : Y -> X_O` maps source objects to observer-visible state.
- `~=_X` is visible-state equivalence.

Projection is not issuance. A new visible state is source-relevant only if the
source gate above also passes.

## 3. Capability

`Capability` states what the observer can do, certify, reconstruct, or use.

```text
Capability =
(
  T,
  h,
  B,
  Cap,
  K,
  R_K
)
```

Where:

- `T` is the task family.
- `h` is horizon.
- `B` is budget or resource condition.
- `Cap : Y -> K` maps source objects to task-native capability objects.
- `R_K` is native comparison on capability objects.

`Cap` must be task-natural. It cannot be "recover the hidden issuance label."

Examples of acceptable capability classes:

- source-order certification;
- record-channel calibration;
- future-operation availability;
- reconstruction reliability under declared access and gluing;
- admissibility-checking power under an explicit construction context.

### Projection Sufficiency Test

Projection is capability-sufficient iff:

```text
for all y1, y2:
  pi_O(y1) ~=_X pi_O(y2) => Cap(y1) R_K Cap(y2)
```

Projection is capability-insufficient iff there exists a same-visible pair with
different capability:

```text
pi_O(y1) ~=_X pi_O(y2)
and not Cap(y1) R_K Cap(y2)
```

Capability insufficiency is not source issuance by itself. It is a shadow-layer
finding unless the `SourceExtension` gate also passes.

## 4. RecordFinality

`RecordFinality` states when a record is stable enough to count for an
observer, process, or domain.

```text
RecordFinality =
(
  Rec,
  carrier,
  validity,
  finality_rule,
  domain,
  finality_state
)
```

Where:

- `Rec` is the record or record trace.
- `carrier` is the chain, DAG, notebook, memory surface, archive, or
  domain-local record substrate.
- `validity` states which records are admissible.
- `finality_rule` states when reversal is disallowed, expensive, or outside the
  domain protocol.
- `domain` prevents hidden global commit-order claims.
- `finality_state` is one of:

```text
unrecorded
recorded_unfinalized
locally_final
domain_final
cross_domain_reconciled
```

Record finality is not source issuance. RUN-0057 remains active: fork-choice,
canonical-chain finality, quorum validity, and finalized record membership
absorb ordinary operational finality.

## 5. LossKernel

`LossKernel` states what projection, summarization, access, or finality loses.

```text
LossKernel =
(
  pi_O,
  preserved_fields,
  lost_fields,
  quotient_relation,
  capability_spread
)
```

Where:

- `preserved_fields` are source or record fields invariant under projection.
- `lost_fields` are fields identified, erased, compressed, or hidden by
  projection.
- `quotient_relation` is the equivalence induced by the projection.
- `capability_spread` is the set of possible capability classes inside one
  visible equivalence class.

In plain English: `LossKernel` says what the shadow forgot.

A loss finding is useful when it blocks overclaim or identifies a real
capability-sufficiency failure. It is not evidence of source-side issuance by
itself.

## 6. AbsorberSet

`AbsorberSet` is a first-class part of the contract.

```text
Absorber =
(
  name,
  owned_fields,
  null_model,
  same_neighbor_freeze,
  collapse_condition,
  verdict_if_successful
)
```

Required absorbers for current Temporal Issuance work:

| Absorber | Collapse condition |
| --- | --- |
| Fixed richer source | `Y_infty` or `Mu_infty` already contains the apparent novelty and only `P_n` access changes. |
| Causal order / causal set | `<`, `dR`, or `G` is just causal order, birth order, stems, past sets, or reconstruction. |
| Thermodynamic / information ledger | `mu` reduces to entropy, work, heat, free energy, path probability, Shannon information, or record counting. |
| Instrumentation / measurement | `M`, `kappa_i`, or `A_i` reduces to detector cadence, coupling, channel policy, or measurement context. |
| TaF gluing / finality | record coherence is ordinary descent, colimit, access, finality, or record reconstruction. |
| Fork-choice / canonical finality | TI-C022 content is supplied by quorum validity, canonical carrier selection, finality, and finalized record membership. |
| Hidden grammar / supervisor | an actor or source trace relies on an undeclared global grammar, future mailbox, or privileged coordinator. |

## Same-Neighbor Freeze

Before claiming residue, freeze:

```text
causal order
spacetime or causal-set volume/counting data
observer worldlines and access regions
detector sampling/cadence
thermodynamic path, reservoir, work, heat, and free-energy ledgers
information state, compression, and statistical-complexity ledgers
record-generation rule
identity, overlap, and gluing data
gauge, label, basis, and foliation convention
```

If the claimed split disappears after this freeze, it belongs to the absorber.

## Verdict Classes

Every future fixture using this contract must end in one of these verdicts:

```text
source_issuance_candidate
projection_access_novelty
capability_sufficiency_failure
record_finality_only
lossy_projection_residue
absorber_controlled_bookkeeping
untyped_or_invalid
```

### Verdict Rules

Use `source_issuance_candidate` only when the Source Issuance Gate passes and
the fixed-source absorber fails.

Use `projection_access_novelty` when the observer-visible state changes but the
source object can be fixed.

Use `capability_sufficiency_failure` when `Cap` does not factor through
`Projection`, but source novelty is not established.

Use `record_finality_only` when the only durable result is record stabilization,
settlement, canonical carrier membership, or finality.

Use `lossy_projection_residue` when the projection loses real structure but the
loss has not been tied to source issuance.

Use `absorber_controlled_bookkeeping` when a named absorber accounts for the
whole residue.

Use `untyped_or_invalid` when the candidate lacks the fields required to decide.

## Six-Axis Admission Table

Any physics-facing use must fill:

| Axis | Required content |
| --- | --- |
| L1 substrate | What carries source state or transition. |
| L2 observer | What observes, records, samples, or reconstructs. |
| L3 pairing | How substrate and observer interact. |
| L4 causal/protocol order | What order relation is available without hidden global present. |
| L5 emergence class | What macroscopic or record-facing object is claimed. |
| L6 coordination loop | How local records reconcile or fail to reconcile. |

Blank or metaphorical fields return the candidate for typing.

## Double-Diagram Requirement

Do not collapse observer-domain gluing and source/record filtration.

Use two axes:

```text
horizontal: observer-domain descent, local-to-global gluing, finality
vertical: source, record, or admissibility filtration
```

Candidate theorem-shaped target:

```text
S : SourceExtension -> FilteredRecordObject
R : FilteredRecordObject -> ReadoutValue
```

The source axis and observer axis must remain separately typed.

## G02 Readiness

G02 may start because this contract gives it a concrete positive fixture target:

```text
Compat_G^MLTT finite trace
-> SourceExtension
-> Projection
-> Capability
-> RecordFinality
-> LossKernel
-> AbsorberSet
```

G02 should not attempt claim promotion. It should only test whether the contract
can carry a finite positive source-side example without category mistakes.

## G03 Readiness

G03 may start because this contract gives it a concrete negative-control target:

```text
fixed Mu_infty
+ expanding P_n access aperture
+ observer readout/finality
```

Expected verdict:

```text
projection_access_novelty
or absorber_controlled_bookkeeping
```

If G03 receives `source_issuance_candidate`, this contract has failed.

## Claim-Ledger Implication

No claim movement follows from this contract. The contract is an admission and
classification surface. Future fixtures may pressure TI-C019, TI-C020, or
TI-C022 only after they instantiate the contract.

## Contract Success

G01 succeeds if:

1. all six required objects are defined;
2. fixed-source bounded-access absorption is first-class;
3. the contract gives G02 and G03 executable targets;
4. the contract keeps source issuance, projection novelty, capability failure,
   record finality, and loss separate.

Verdict: G01 succeeds.

## Contract Failure Condition

Reopen this contract if a future fixture shows that the verdict classes cannot
separate:

```text
source issuance
projection/access novelty
capability insufficiency
record finality
lossy projection residue
absorber-controlled bookkeeping
```

Until then, the next run should be G02 or G03.
