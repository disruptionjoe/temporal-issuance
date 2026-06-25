---
artifact_type: exploration
exploration_id: E070
status: active
created: 2026-06-24
run_ref: RUN-0065
goal_ref: G02_source_shadow_finality_positive_fixture
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
  - E069-fixed-source-bounded-access-negative-control-2026-06-24.md
---

# E070: Source / Shadow / Finality Positive Fixture

## Purpose

Run G02 from the ten-goal sequence. This fixture tests whether the E067 contract
can carry a bounded positive formal source-side example without promoting a
physics claim or confusing source issuance with projection/finality.

## Fixture Scope

This is a formal-source fixture only:

```text
source candidate: Compat_G^MLTT
physics claim: not tested
TI-C020 status: unchanged
```

It uses the RUN-0050 / E055 result:

```text
Compat_G^MLTT crosses the expressiveness threshold as a formal staged-
construction model because fixed completed future oracles are not well-formed
present objects and productive SBP successors are construction events.
```

## Finite Trace

Let:

```text
Gamma_n      = current MLTT construction context
Adm_n        = current admissibility judgment in Gamma_n
Enum_n       = any admissible pre-committed enumeration of SBP successors
sigma_star   = productive SBP successor escaping Enum_n
Gamma_{n+1}  = Gamma_n + sigma_star + construction record rho_star
Adm_{n+1}    = admissibility judgment after sigma_star is formed
```

The finite trace is:

```text
Gamma_n -> Gamma_{n+1}
```

where `sigma_star` is not a prior formed object in `Gamma_n`.

## E067 Contract Instantiation

### SourceExtension

```text
SourceExtension =
(
  n,
  Y_n = Compat_G^MLTT(Gamma_n),
  Adm_n,
  C_n = Gamma_n,
  delta_n = construct_productive_SBP_successor,
  Y_{n+1} = Compat_G^MLTT(Gamma_{n+1}),
  Adm_{n+1},
  C_{n+1} = Gamma_{n+1},
  issued_object = sigma_star,
  source_witness = rho_star
)
```

### Source Issuance Gate

```yaml
SI-1_online_availability: passes
  reason: sigma_star is not a formed object in Gamma_n and escapes Enum_n.
SI-2_no_hidden_future_schema: passes_for_local_MLTT_model
  reason: fixed A_infty / completed future schema is not a well-formed present object.
SI-3_admissibility_growth: passes
  reason: Gamma_{n+1} admits sigma_star and its downstream constructions.
SI-4_recordability: passes
  reason: rho_star records the construction event.
```

Result:

```text
source_issuance_candidate
```

This verdict is formal and class-relative. It does not establish that physical
reality is a `Compat_G^MLTT` source.

### Projection

Use an observer-facing record projection:

```text
Projection =
(
  O = bounded record observer,
  Sigma = construction-record schema,
  r = records sigma_star and admission event, not full proof search space,
  U = local finite trace,
  B = finite audit budget,
  pi_O = record_projection(Gamma_n -> Gamma_{n+1}),
  ~=_X = same visible construction-record class
)
```

The projection sees the admitted construction record, not the whole source
construction space.

### Capability

Use a task-natural capability:

```text
T = future admissibility checking and successor construction using sigma_star
h = one successor step
B = finite audit budget
Cap(Gamma_n) = cannot use sigma_star
Cap(Gamma_{n+1}) = can use sigma_star in downstream admissibility checks
R_K = same future-operation availability
```

This capability change is source-linked because the source gate passes. It is
not merely first access to a fixed hidden object, by the local MLTT class rule.

### RecordFinality

```text
Rec = rho_star
carrier = source construction log / repo artifact
validity = rho_star checks under Adm_{n+1}
finality_rule = record persists as the construction witness for the finite trace
domain = formal finite trace
finality_state = domain_final
```

Record finality is downstream. The source verdict comes from SourceExtension,
not from finality.

### LossKernel

The observer projection preserves:

```text
preserved_fields:
  - sigma_star admitted
  - rho_star exists
  - Gamma_n -> Gamma_{n+1}
  - downstream capability changed
```

It loses:

```text
lost_fields:
  - full proof-search space
  - all rejected successor candidates
  - all future successors after Gamma_{n+1}
  - any external Platonist completion question
```

Therefore the fixture also has:

```text
lossy_projection_residue
```

but the loss is not doing the source work. The source work is done by the local
MLTT no-hidden-oracle rule plus the productive successor construction.

### AbsorberSet

| Absorber | Result |
| --- | --- |
| Fixed richer source | Fails internally for the local MLTT source class; fixed completed future schema is not well-formed at `Gamma_n`. |
| External Platonist oracle | Survives only as alternate ontology, already classified as navigation rather than local source creation. |
| Projection/access novelty | Fails as total explanation because the source context changes from `Gamma_n` to `Gamma_{n+1}`. |
| Record finality only | Fails as total explanation because record finality is downstream of the construction event. |
| Hidden grammar/supervisor | Not used in this fixture. |

## Same-Neighbor Contrast With G03

G03 had:

```text
fixed Mu_infty
P_n -> P_{n+1}
source unchanged
```

This fixture has:

```text
Gamma_n -> Gamma_{n+1}
sigma_star not formed at Gamma_n
no fixed A_infty as well-formed present object
```

That is the decisive difference.

## Verdict

```text
source_issuance_candidate
lossy_projection_residue
```

Explicitly not:

```text
projection_access_novelty only
record_finality_only
absorber_controlled_bookkeeping
```

## Contract Result

E067 passes the first positive fixture. It can carry a formal source-side
example while preserving the distinction between source issuance, projection,
record finality, and loss.

## Claim-Ledger Implication

No claim status changes. This fixture reuses the already-recorded RUN-0050
formal-source result and verifies that E067 can classify it. It does not move
TI-C020 or the physical-source question.
