---
artifact_type: exploration
exploration_id: E069
status: active
created: 2026-06-24
run_ref: RUN-0064
goal_ref: G03_fixed_source_bounded_access_negative_control
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
---

# E069: Fixed-Source Bounded-Access Negative Control

## Purpose

Run G03 from the ten-goal sequence. This fixture tests whether the E067
source-shadow-finality contract correctly rejects a false source-issuance
candidate when novelty is only expanding access to a fixed richer source.

## Null Model

Assume a fixed source:

```text
Mu_infty = completed richer source
C_infty  = completed construction context
Adm_infty = completed admissibility predicate
```

At each observer stage `n`, the observer sees only an aperture:

```text
P_n : Mu_infty -> X_n
P_n <= P_{n+1}
```

An object `a` is invisible at stage `n` but visible at stage `n+1`:

```text
a in Mu_infty
a notin im(P_n)
a in im(P_{n+1})
```

This looks like novelty to the observer, but by construction it is already in
the fixed source.

## E067 Contract Instantiation

### SourceExtension

```text
SourceExtension =
(
  n,
  Y_n = Mu_infty,
  Adm_n = Adm_infty,
  C_n = C_infty,
  delta_n = P_n -> P_{n+1},
  Y_{n+1} = Mu_infty,
  Adm_{n+1} = Adm_infty,
  C_{n+1} = C_infty,
  issued_object = a,
  source_witness = observer first-access at n+1
)
```

### Source Issuance Gate

```yaml
SI-1_online_availability: fails
  reason: a is already available in C_infty / Adm_infty.
SI-2_no_hidden_future_schema: fails
  reason: Mu_infty is a fixed richer source already containing a.
SI-3_admissibility_growth: fails
  reason: Adm_n = Adm_{n+1} = Adm_infty.
SI-4_recordability: passes
  reason: first-access can be recorded after P_{n+1}.
```

Result:

```text
not source_issuance_candidate
```

### Projection

```text
Projection =
(
  O = bounded observer,
  Sigma = visible aperture schema,
  r = exact within aperture,
  U = observer-local domain,
  B = access boundary P_n,
  pi_O = P_n,
  ~=_X = equality of visible aperture payload
)
```

The projection changes from `P_n` to `P_{n+1}`. The visible state changes, but
the source does not.

### Capability

Use a task-natural capability:

```text
T = certify or use object a
Cap_n(Mu_infty) = cannot certify/use a through P_n
Cap_{n+1}(Mu_infty) = can certify/use a through P_{n+1}
R_K = same certification/use status
```

This is capability change under access expansion. It is not source issuance.

### RecordFinality

```text
Rec = first-access record for a
carrier = observer-local record log
validity = a appears in im(P_{n+1})
finality_rule = record is stable inside observer-local log
domain = observer aperture history
finality_state = locally_final
```

The record can become locally final, but that finality is downstream of access.

### LossKernel

At stage `n`, the projection loses `a`:

```text
lost_fields(P_n) includes a
preserved_fields(P_n) excludes a
```

At stage `n+1`, the projection preserves `a`:

```text
lost_fields(P_{n+1}) removes a
preserved_fields(P_{n+1}) includes a
```

The LossKernel changes because access changes. Source does not change.

### AbsorberSet

The fixed richer source absorber succeeds:

```yaml
absorber: fixed_richer_source
owned_fields:
  - issued_object
  - admissibility
  - construction_context
null_model: fixed Mu_infty + expanding P_n aperture
collapse_condition: object is already in Mu_infty and only aperture changes
verdict_if_successful: projection_access_novelty
```

## Same-Neighbor Freeze

All non-access fields are fixed:

```yaml
causal_order: fixed_or_irrelevant
volume_counting_data: fixed_or_irrelevant
observer_worldline: fixed
detector_sampling_cadence: fixed
thermodynamic_ledger: fixed_or_irrelevant
information_ledger: fixed_except_visible_payload
record_generation_rule: fixed
identity_overlap_gluing: fixed
gauge_label_basis_foliation: fixed
```

Only access aperture changes:

```text
P_n -> P_{n+1}
```

Therefore the split belongs to access/projection, not source issuance.

## Verdict

```text
projection_access_novelty
absorber_controlled_bookkeeping
```

Explicitly not:

```text
source_issuance_candidate
```

## Contract Result

E067 passes this negative control. The contract does not misclassify fixed
source disclosure as source-side issuance.

## Implication For The Ten-Goal Sequence

G03 succeeds. G02 can now run the positive fixture with a functioning negative
control already in place.

## Claim-Ledger Implication

No claim movement. This run protects the classification boundary; it does not
support or weaken TI-C019 beyond preserving the fixed-source absorber as a live
null.
