---
artifact_type: exploration
status: active
governance_role: toy_model_test
constitutional: false
exploration_id: E001
last_updated_by: RUN-0014
---

# E001: Two-Observer Patch Test

## Purpose

Pressure the repaired definitions from RUN-0013 with a minimal toy model.

This is not a physics model. It is a formal sanity check.

## Setup

Two local patches:

```text
LocalIssuancePatch_A = (R_A, <=_A, A_A, kappa_A, lambda_A)
LocalIssuancePatch_B = (R_B, <=_B, A_B, kappa_B, lambda_B)
```

Local fixed states:

```text
R_A = {a0, a1, a2}
R_B = {b0, b1}
```

Local dependency:

```text
a0 <=_A a1
a0 <=_A a2
b0 <=_B b1
```

Access:

```text
A_A = {a0, a1, a2}
A_B = {b0, b1}
```

Reconciliation map:

```text
G_AB(a0) = b0
G_AB(a1) = b1
G_AB(a2) = undefined
```

Obstruction:

```text
Omega_AB = {a2: no accessible counterpart in B}
```

Ordinal update relations:

```text
kappa_A: a0 -> a1 -> a2
kappa_B: b0 -> b1
```

Candidate measures:

```text
lambda_A(R_A) = 3
lambda_B(R_B) = 2
lambda_reconciled = 2 compatible states + 1 obstruction
```

## Test Results

| Candidate | Result | Reason |
| --- | --- | --- |
| `G_ij` | survives toy test | It can represent partial reconciliation rather than forced global agreement. |
| `Omega_ij` | survives toy test | It records obstruction explicitly and may do work that plain gluing hides. |
| `kappa_i` | weakly survives toy test | It can be ordinal rather than metric, but the toy does not prove independence from ordinary time. |
| `lambda_i` | fails as defined | Simple counting collapses into cardinality and does not distinguish constraint-extension measure. |

## Lessons

- Reconciliation obstruction is the strongest part of the repaired object.
- Cadence can be represented ordinally in a toy model, but needs a non-circular definition.
- The measure candidate remains the weakest component.
- The next formal work should focus on obstruction and cadence before trying to resurrect a measure.

## Next Test

Create a second toy where two observers have the same cardinality but different obstruction structure. If `lambda_i` cannot distinguish them without becoming information, entropy, or cardinality, keep measure out of the core object.
