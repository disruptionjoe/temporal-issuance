---
artifact_type: exploration
status: active
governance_role: minimal_witness
run_ref: RUN-0080
claim_refs:
  - TI-C019
  - TI-C003
depends_on:
  - explorations/E055-expressiveness-threshold-fixture-2026-06-24.md
  - explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md
  - explorations/E088-online-issuance-adaptive-computation-absorber-2026-06-25.md
  - explorations/E089-online-issuance-category-absorber-2026-06-25.md
---

# E090: OnlineIssuance Minimal Constructive Witness

## Purpose

This executes Goal 4 from E086: build the smallest worked model or cleanly refute the line.

After Goals 2 and 3, the only live residue is:

```text
constructive prefix-formation discipline plus productive admissible witness
```

This artifact tests whether that residue has a minimal witness.

## Four Comparators

### A. Finite-Type Context

```text
Gamma_0 contains a finite set CandExt(Gamma_0).
Adm_0 is decidable over that finite set.
```

Verdict:

```text
FAIL as source issuance.
```

Reason: every candidate extension can be enumerated at the prefix. Later selection is search,
choice, optimization, or projection.

### B. Infinite Computable Context

```text
Gamma_0 contains a computable grammar for candidates.
Adm_0 is computable or c.e. enough to enumerate accepted successors.
```

Verdict:

```text
FAIL as source issuance.
```

Reason: the extension trace factors through a fixed generator plus access or search schedule.
This is the RUN-0078 absorber.

### C. Fixed Platonist Oracle Context

```text
Omega_future contains all future contexts, all future admissibility predicates, all accepted
witnesses, and the whole future extension trace.
```

Verdict:

```text
EXTERNAL ABSORBER, NOT INTERNAL WITNESS.
```

Reason: from outside the source discipline, `Omega_future` represents the whole trace. Inside
`OnlineIssuance v0.1`, it violates the no-hidden-completed-oracle gate. It is navigation through
a completed object, not an internal online source witness.

### D. Local MLTT Source Context

```text
Gamma_n is a local constructive context.
Adm_n : CandExt(Gamma_n) -> Type is formed at Gamma_n.
Future contexts and future proof terms are not a formed type at Gamma_n.
Gamma_n can encode its own present syntax, admissibility judgments, and proof records.
```

Verdict:

```text
CONDITIONAL MINIMAL WITNESS.
```

Reason: this is the E055 regime. The source can form a present self-encoding admissibility
problem and a productive successor against any present admissible enumeration, while no completed
future oracle is well-formed at the prefix.

## Witness Schema

Let:

```text
Code_n:
  codes available in Gamma_n

Cand_n:
  candidate extensions formed in Gamma_n

Adm_n:
  Cand_n -> Type

Enum_n:
  Nat -> Cand_n
```

For any formed `Enum_n` claiming to cover the admissible successor class available at prefix
`n`, define a diagonal candidate:

```text
Diag(Enum_n) : CandExt(Gamma_n)
```

with witness obligation:

```text
w_diag : Adm_n(Diag(Enum_n))
```

and separation:

```text
for every k, Diag(Enum_n) is not equivalent to Enum_n(k)
```

The issued step is:

```text
Iss_n(Gamma_n, Diag(Enum_n), w_diag) = Gamma_{n+1}
```

The source trace records:

```text
tau_n = (Gamma_n, Enum_n, Diag(Enum_n), w_diag, Gamma_{n+1})
```

## Why This Is Not Just A Bigger Search Space

A fixed finite or computable search space fails because `Diag(Enum_n)` is constructed against the
present attempted enumeration.

A fixed stochastic law or hyperprior fails because random draw does not form the diagonal witness.

A fixed latent graph fails because the graph would need the diagonal successor already present.

An external oracle succeeds only by leaving the internal source class.

## What This Witness Actually Establishes

It establishes:

```text
There is a minimal class-relative witness pattern for online issuance under local constructive
discipline.
```

It does not establish:

```text
physical issuance
a new category primitive
a new law of nature
probability weights
observer finality
```

## Creation vs Navigation

The result is class-relative.

```text
External Platonist reading:
  navigation through a completed total object.

Local constructive reading:
  issuance of a source-admissible witness because the future oracle is not a formed object at
  the prefix.
```

The repo should not pretend this defeats every metaphysics. It defeats only the absorbers that
are forbidden by the declared online constructive class.

## Goal 4 Verdict

```yaml
goal_4: complete
minimal_witness: conditional_survives
survival_class: local_constructive_no_hidden_oracle
absorbed_by_external_platonist_completion: true
not_machine_checked: true
claim_status_change: none
next_goal: verdict_and_formal_object_rewrite
```
