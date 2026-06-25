---
artifact_type: exploration
status: active
governance_role: formal_object_candidate
run_ref: RUN-0077
claim_refs:
  - TI-C019
  - TI-C003
depends_on:
  - explorations/E086-online-issuance-five-goal-formalization-sequence-2026-06-25.md
  - explorations/E055-expressiveness-threshold-fixture-2026-06-24.md
  - explorations/E067-source-shadow-finality-interface-contract-2026-06-24.md
---

# E087: OnlineIssuance v0.1 Formal Object

## Purpose

This executes Goal 1 from E086: state the smallest precise `OnlineIssuance` object that is
ready for absorber pressure.

The object must not win by vocabulary. It must separate:

```text
Issue[S]      source-side admissible extension
Project[O]    observer-side readout
Finalize[R]   record-finality operation
Lose[K]       information loss under projection
```

## Definition

An `OnlineIssuance v0.1` trace is a sequence:

```text
OI =
(
  Gamma_n,
  Adm_n,
  Ext_n,
  Iss_n,
  Obs_{o,n},
  Proj_{o,n},
  Glue_n
)_{n in P}
```

where `P` is a prefix order. `P` is not metric time; it is the order in which the formal trace is
presented and extended.

### Source Layer

`Gamma_n` is a prefix-presented constructive context, theory, or schema.

```text
Gamma_n = declarations, constructors, admissibility predicates, and proof terms formed at
prefix n.
```

`Adm_n` is an admissibility predicate formed in `Gamma_n`.

```text
Adm_n : CandExt(Gamma_n) -> Type
```

Read: a candidate source extension is admissible at prefix `n` only when there is a witness term
inhabiting `Adm_n(e)`.

`Ext_n` is the extension category available at `n`.

```text
Obj(Ext_n) = contexts reachable from Gamma_n by finite admissible extensions
Mor(Ext_n) = witness-bearing extension traces
```

The induced order is only the thin reflection:

```text
Gamma <= Gamma' iff Hom_Ext(Gamma, Gamma') is inhabited.
```

`Iss_n` is an issuance step:

```text
Iss_n(Gamma_n, e_n, w_n) = Gamma_{n+1}
```

with:

```text
e_n : CandExt(Gamma_n)
w_n : Adm_n(e_n)
Gamma_{n+1} = Gamma_n + e_n + w_n + recordable source trace tau_n
```

The step is source-side only if it satisfies the properness gate below.

### Projection Layer

For each observer/process `o`, `Obs_{o,n}` is a local record/model state.

```text
Obs_{o,n} = local schema, local record trace, accessible interface, and update state.
```

`Proj_{o,n}` is an observer readout:

```text
Proj_{o,n}: Gamma_n -> Obs_{o,n}
```

`Glue_n` is a reconciliation/finality operation over projected records:

```text
Glue_n({Obs_{o,n}}_{o in O_n}) -> compatible record state or obstruction record.
```

`Proj` and `Glue` are not source issuance. They can expose, stabilize, or lose information about
source traces, but they do not make a source extension true.

## Properness Gate

An issuance step is proper only if all of the following hold.

### P1: Formed Present Domain

`Gamma_n`, `CandExt(Gamma_n)`, and `Adm_n` must be well-formed at prefix `n`.

Forbidden: appealing to a completed future context as if it were already formed.

### P2: Witnessed Extension

The accepted extension has a present witness:

```text
e_n : CandExt(Gamma_n)
w_n : Adm_n(e_n)
```

The witness may justify a new declaration, new admissibility predicate, new construction rule,
or new term.

### P3: Unavailability In Prior Context

The issued structure is unavailable in `Gamma_n`:

```text
not Term(Gamma_n, target(e_n))
```

or, more strongly, `target(e_n)` is not a formed type/proposition/rule in `Gamma_n`.

This is stronger than "the observer had not seen it." It is a source-context claim.

### P4: No Hidden Completed Oracle

The model may not contain an internal object at `Gamma_0` or `Gamma_n` that already supplies:

```text
all future contexts
all future admissibility predicates
all future accepted witnesses
the complete future extension graph
a fixed access schedule revealing pre-existing future objects
a fixed stochastic law over all future source extensions
a fixed latent graph whose later "new" edges are only disclosed
```

External Platonist completions can still be stated as an absorber class, but they are not
internal `OnlineIssuance v0.1` models.

### P5: Recordability

The step emits a trace `tau_n` sufficient for later projection and finality audit:

```text
tau_n = (Gamma_n, e_n, w_n, Gamma_{n+1}, effect_tag)
```

If no trace is recordable, the step may be metaphysical residue but is not usable in this repo.

## Effect Typing

```text
Issue[S](Gamma_n, e_n, w_n):
  source context is extended by a witnessed admissible extension.

Project[O](Gamma_n, Proj_{o,n}):
  an observer-accessible state is read from the source context.

Finalize[R]({Obs_{o,n}}, Glue_n):
  records are stabilized, reconciled, or marked obstructed inside a domain.

Lose[K](Proj_{o,n}):
  the projection is nonfaithful, coarse, lossy, delayed, or aperture-limited.
```

Only `Issue[S]` can move the source claim.

## No-Hidden-Oracle Discipline

The discipline is class-relative, not metaphysical.

Allowed:

```text
finite prefixes
local admissibility predicates
proof terms formed at the current prefix
productive successor rules that operate on present encodings
observer projections that lose information
external comparison models used as absorbers
```

Forbidden inside the source object:

```text
completed future schema
global Stone space used as available source state
oracle over future contexts and proof terms
latent graph containing every future admissible move
fixed law assigning all future source extensions
ambient category whose total object/morphism data is available to the source from the start
```

## Examples And Non-Examples

| Candidate | Classification | Reason |
| --- | --- | --- |
| Finite context with finite option pool | Non-example | All options can be pre-enumerated. |
| Infinite computable grammar with c.e. admissibility | Non-example | A fixed generator plus access schedule absorbs the trace. |
| Fixed latent graph with revealed edges | Non-example | Newness is projection/access novelty, not source issuance. |
| Stochastic process with fixed law over future extensions | Non-example | Random sampling from a fixed law is not source-context properness. |
| Classical Platonist total future schema | Absorber / navigation model | It can represent the trace externally, but violates internal no-hidden-oracle discipline. |
| `Compat_G^MLTT` with self-encoding admissibility and diagonal productive successor | Candidate example | E055 says it passes the expressiveness threshold under local constructive discipline. |
| Observer record stabilization / Quantum Darwinism / sheafification | Projection/finality only | These type as `Project[O] + Finalize[R] + Lose[K]` unless the source gate also passes. |

## Immediate Absorber Targets

The definition is intentionally vulnerable to two hard tests.

1. Adaptive computation absorber:
   if every `OI` trace can be represented as fixed richer source plus computation/access, the
   object is absorbed.
2. Category-theory bookkeeping absorber:
   if every `OI` trace is just a context category, fibration, presheaf, colimit, forcing, or
   gluing construction with no class-relative residue, the object is absorbed.

## Goal 1 Verdict

```yaml
goal_1: complete
object_status: precise_enough_for_absorber_pressure
claim_status_change: none
surviving_residue: >
  A source-side proper extension requires current-prefix admissibility, witnessed extension,
  prior-context unavailability, no internal completed future oracle, and recordability.
main_risk: >
  The object may still be absorbed once external computation/category presentations are allowed.
next_goal: adaptive_computation_absorber_gauntlet
```

No claim is promoted. This is a sharpened formal target, not a theorem that reality issues.
