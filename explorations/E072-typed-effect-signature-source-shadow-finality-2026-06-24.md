---
artifact_type: exploration
exploration_id: E072
status: active
created: 2026-06-24
run_ref: RUN-0067
goal_ref: G09_typed_effect_signature
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
  - E069-fixed-source-bounded-access-negative-control-2026-06-24.md
  - E070-source-shadow-finality-positive-fixture-2026-06-24.md
  - E071-issued-capability-contract-test-2026-06-24.md
---

# E072: Typed Effect Signature For Source / Shadow / Finality

## Purpose

Run G09 from the ten-goal sequence. This artifact defines a minimal effect
signature that prevents source, projection, finality, and loss from being
silently interchanged.

## Minimal Effects

```text
Issue[S]     source-side admissibility or construction-space extension
Project[O]   observer-visible projection or access change
Finalize[R]  record-stability or finality transition
Lose[K]      projection, memory, or summarization loss
```

The effects can co-occur, but none of the shadow/finality effects implies
`Issue[S]`.

## Formation Rules

### Issue[S]

Allowed only when:

```text
SourceExtension gate passes
fixed-source absorber fails
hidden future schema / hidden supervisor absorber fails
```

Not allowed from:

```text
new observer access
new record finality
capability insufficiency alone
projection loss alone
```

### Project[O]

Allowed when:

```text
pi_O changes, observer access changes, visible state changes, or projection
equivalence class changes
```

Does not imply:

```text
source changed
```

### Finalize[R]

Allowed when:

```text
record state changes from unrecorded/unfinalized to locally_final,
domain_final, or cross_domain_reconciled
```

Does not imply:

```text
source changed
```

### Lose[K]

Allowed when:

```text
LossKernel has nonempty lost_fields, quotienting, compression, or capability
spread inside a visible equivalence class
```

Does not imply:

```text
source changed
```

## Non-Implication Table

| From | Invalid inference |
| --- | --- |
| `Project[O]` | therefore `Issue[S]` |
| `Finalize[R]` | therefore `Issue[S]` |
| `Lose[K]` | therefore `Issue[S]` |
| `Capability change` | therefore `Issue[S]` |
| `Project[O] + Finalize[R]` | therefore `Issue[S]` |
| `Project[O] + Lose[K]` | therefore `Issue[S]` |

The only route to `Issue[S]` is the E067 source gate.

## Application To G03

G03:

```text
fixed Mu_infty + expanding P_n aperture
```

Effects:

```text
Project[O]   yes
Finalize[R]  yes, for the first-access record
Lose[K]      yes, because P_n loses a and P_{n+1} loses less
Issue[S]     no
```

Verdict:

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## Application To G02

G02:

```text
Compat_G^MLTT finite trace
Gamma_n -> Gamma_{n+1}
sigma_star admitted
```

Effects:

```text
Issue[S]     yes, formal source class only
Project[O]   yes, construction record projection
Finalize[R]  yes, domain-final construction record
Lose[K]      yes, projection loses full proof-search space
```

Verdict:

```text
Issue[S] + Project[O] + Finalize[R] + Lose[K]
```

Scope:

```text
formal source only
not TI-C020
```

## Application To G06

G03 capability:

```text
access capability change = Project[O]
not Issue[S]
```

G02 capability:

```text
formal issued capability = Issue[S] + Project[O] + Lose[K]
```

The effect signature preserves the G06 distinction.

## Category Mistakes Prevented

### Mistake 1: Projection Assembly Index As Source Evidence

Bad inference:

```text
AI_proj,n undefined and AI_proj,n+1 defined
=> source issuance
```

Effect correction:

```text
Project[O] + Lose[K]
does not imply Issue[S]
```

This preserves the RUN-0059 path kill.

### Mistake 2: First Access As Source Issuance

Bad inference:

```text
observer first sees a
=> source issued a
```

Effect correction:

```text
Project[O] + Finalize[R]
does not imply Issue[S]
```

This preserves G03.

### Mistake 3: Finalized Record Membership As Source Reality

Bad inference:

```text
record is finalized on canonical carrier
=> independent source-side surplus
```

Effect correction:

```text
Finalize[R]
does not imply Issue[S]
```

This preserves the RUN-0057 fork-choice absorber.

## Verdict

G09 succeeds.

The minimal effect signature blocks real category mistakes from recent runs and
gives later fixtures a compact notation:

```text
Issue[S]
Project[O]
Finalize[R]
Lose[K]
```

## Claim-Ledger Implication

No claim movement. This is formal discipline for fixture classification, not a
new source witness.
