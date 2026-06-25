---
artifact_type: exploration
status: active
governance_role: research_learning
constitutional: false
created: 2026-06-25
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E067-source-shadow-finality-interface-contract
  - E072-typed-effect-signature-source-shadow-finality
  - E082-sheafification-bridge-projection-absorber
context_repo:
  - ../time-as-finality/explorations/legitimacy-monad-finality-bridge-addendum-2026-06-25.md
  - ../gu-formalization/explorations/time-as-finality-crosswalk/legitimacy-monad-observer-mathematics-v0.1.md
  - ../architecture-of-legitimacy/explorations/legitimacy-monad-s7-crosswalk-2026-06-25.md
---

# E084: Legitimacy Monad As Projection / Finality Status

## Status

This exploration integrates the S7 legitimacy-monad steelman into Temporal
Issuance. It does not move any claim.

The strong reading is useful:

```text
legitimacy is an idempotent operation that turns local records into stable
observer-usable records for a declared capability.
```

The overstrong reading is blocked:

```text
legitimate record
therefore Issue[S]
```

Temporal Issuance must keep those separate.

## Strong Form vs Conservative Effect Gate

Strong-form S7:

```text
legitimacy may be a first-class primitive for turning local data into
buildable observer mathematics.
```

Conservative TI gate:

```text
classify legitimacy operations as Project[O] + Finalize[R] + Lose[K] unless a
separate source-side witness passes the Issue[S] gate.
```

The conservative gate is not a rejection of the strong form. It is the effect
discipline that prevents a successful legitimacy operation from being
misreported as source issuance.

## Typed Reading

Let `(C, J)` be a fixed site and coverage of local observer contexts, and let:

```text
P : C^op -> D
```

be a local-data presheaf in a fixed target category.

The legitimacy operation is:

```text
L : PSh(C, D) -> PSh(C, D)
eta_P : P -> L(P)
L(L(P)) ~= L(P)
```

In the sheafification case:

```text
L(P) = i aP
```

where `a` is the associated-sheaf reflector.

Temporal Issuance interpretation:

```text
Project[O]:
  local data is made observer-visible through P and eta_P.

Finalize[R]:
  L(P) is stable enough for the declared observer capability.

Lose[K]:
  distinctions, coherent rights, contextual residues, or reversal capabilities
  do not survive eta_P.

Issue[S]:
  not implied by legitimacy.
```

## Source Gate

S7 pressures source-side issuance only if the legitimacy operation forces one
of the source-side changes already required by E082:

```text
1. non-isomorphic source category;
2. issued rather than fixed coverage J;
3. target category or observable algebra growth;
4. new admissibility predicate not representable in the prior model;
5. construction-space expansion after ordinary sheafification/descent and
   fixed-source absorbers are granted.
```

Absent one of those, the correct verdict is:

```text
legitimate final record;
Project[O] + Finalize[R] + Lose[K];
not Issue[S].
```

## Relation To Quorum Legitimacy

This note does not replace the older quorum-legitimacy branch.

Quorum legitimacy asks which multi-observer process can update a shared schema
without capture or equivariance failure.

The S7 legitimacy monad asks which local data becomes a stable record object
for a declared observer capability.

They can be composed, but neither one implies source issuance by itself:

```text
quorum legitimacy + record legitimacy
  may support Finalize[R]
  still not automatically Issue[S]
```

## Absorber Checklist

Add this checklist after the E082 sheafification absorber:

```yaml
Legitimacy_monad_absorber:
  idempotent_operator:
    question: Is L declared and idempotent or reflector-like?
    if_no: vocabulary only
  fixed_point_condition:
    question: Are legitimate records fixed points or operational fixed points
      of L?
    if_no: vocabulary only
  capability_relative:
    question: Is legitimacy relative to a declared observer capability?
    if_no: authority language, not TI evidence
  source_gate:
    question: Does L force source-side growth in category, coverage,
      target, admissibility, or construction space?
    if_no: Project[O] + Finalize[R] + Lose[K], not Issue[S]
  loss_profile:
    question: Are non-preserved distinctions across eta_P explicitly recorded?
    if_no: fail the bridge witness
```

## Claim Effects

```yaml
TI-C019:
  status_change: none
  note: Legitimacy of observer records does not relax the source-side gate.

TI-C020:
  status_change: none
  pressure_change: absorber_strengthened
  note: S7 gives a sharper null for quantum/classical bridge claims: stable
    observer records can be legitimate without being source-issued.

TI-C022:
  status_change: none
  note: Legitimate record fixed points may help specify continuity/finality,
    but continuity and finality still do not imply source issuance.

path_promoted: none
path_killed: none
```

## Recommendation

Use S7 as a naming upgrade for the sheafification/finality absorber only when a
candidate supplies:

```text
L, eta_P, fixed-point condition, capability, and loss profile.
```

Otherwise, treat "legitimacy" as rhetoric and demote it.

Architecture of Legitimacy is the natural institutional testbed for this
absorber: its contribution workflow can test whether local contribution
evidence becomes legitimate final record without being mistaken for source
issuance.
