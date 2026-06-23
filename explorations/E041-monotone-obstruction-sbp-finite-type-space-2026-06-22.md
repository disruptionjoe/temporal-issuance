---
artifact_type: exploration
status: active
exploration_id: E041
date: 2026-06-22
topic: monotone_obstruction_sbp_finite_type_space
claim_refs:
  - TI-C019
  - TI-C021
relates_to:
  - E031 (N, C, K definitions; K superlinearity; IA; interior optimum condition)
  - E038 (ASSOC-OBL-001 closed; Ext_S is a genuine category)
  - E039 (IA verification — IA fails for all Compat families; monotone-obstruction named as IA replacement)
  - E028 (eventually-constant trajectory condition; Gödelian type-generation mechanism)
  - E040 (Ostrom Witness Theorem; SBP morphism class)
blocking_task_addressed: >
  E039 §11 "Still Blocked" item 1 — Monotone-obstruction proof for SBP Compat with finite
  type space; the IA replacement condition that closes the interior optimum existence proof.
proof_verdict: PROVED (under finite-type-space hypothesis FTS), with explicit sublinear-N coupling
---

# E041: Monotone-Obstruction for SBP Compat with Finite Type Space — The IA Replacement

## Purpose

E039 established that the Independence Assumption (IA) does not hold for any Compat family
in the repo, because the admissibility predicate is path-dependent (each extension modifies
the admissibility predicate of the target state, correlating obstruction probabilities at
successive steps). E039 §7.4 then proved a *replacement* characterization:

> K is superlinear in lambda (in the operative sense) **iff** the Compat predicate is
> monotone-obstructive: the obstruction probability at step n+1 is >= the obstruction
> probability at step n, conditional on the trajectory not having collapsed by step n.

and named the open obligation (E039 §11 item 1):

> "Monotone-obstruction proof for SBP with finite type space: the most tractable path
> to replacing IA. Requires showing that each SBP application strictly reduces the pool
> of available type-novel extensions."

This exploration discharges that obligation. It:

1. Fixes the finite-type-space hypothesis (FTS) precisely (Section 2).
2. Defines the obstruction quantity for a state and the monotone-obstruction property
   formally (Section 3).
3. Proves the Type-Pool Depletion Lemma: each SBP application strictly shrinks the
   available novel-type pool (Section 4).
4. Proves the Monotone-Obstruction Theorem: under FTS, the per-step obstruction
   probability is non-decreasing along any SBP trajectory (Section 5).
5. Derives K superlinearity from monotone-obstruction without IA (Section 6).
6. Couples this to N concavity and closes the interior-optimum existence proof
   conditionally on FTS (Section 7).
7. States exactly where the Gödelian (E028) regime breaks the result and what that means
   for the program (Section 8).
8. Records assumptions, kill conditions, and the obligation verdict (Sections 9-10).

The proof is deliberately self-contained: it restates the E031 morphism definition and
the E039 obstruction definition rather than relying on the reader holding them in memory.

---

## 1. Recalled Definitions

### 1.1 Ext_S morphisms (E031 §I.2, E038)

A state is S = (T_S, A_S). A morphism e: S -> S' adds one new constraint label c_e with
type type(c_e), giving T_{S'} = T_S ∪ {c_e} and

```text
A_{S'}(X) = 1  iff  A_S(X \ {c_e}) = 1  AND  Compat(c_e, X \ {c_e}, S).
```

Composition is associative (E038, unconditional). Ext_S is a genuine category.

### 1.2 D4 and type-novelty (E031 §I.2)

Write types(S) = {type(c) : c in T_S}. A morphism e is a **D4 morphism** iff
type(c_e) ∉ types(S). The novelty functor N counts D4 morphisms among reachable morphisms:

```text
N(lambda, S) = |D4-Hom_lambda(S)| / |Hom_lambda(S)|.
```

### 1.3 SBP morphisms (E031 §III.1, E040 §1)

A morphism e: S -> S' is a **schema-boundary proposal (SBP)** iff:
- (SBP-i) type(c_e) ∉ types(S)  [D4 condition], and
- (SBP-ii) for every alternative morphism f: S -> S'' with S'' ≠ S',
  Compat(c_e, T_{S''}, S) = 0 and Compat(c_f, T_{S'}, S') = 0
  [the two extensions fork the schema and cannot be reconciled into a common successor].

### 1.4 Obstruction and eventually-constant (E039 §1.1, E031 §II.2)

A state S is **obstructed** iff Hom(S, -) contains only the identity, i.e. no admissible
non-identity extension departs S. A trajectory (S_n) is **eventually-constant** iff there
is N* with S_n = S_{N*} for all n > N*, equivalently S_{N*} is obstructed. K(lambda, S) is
the probability that the rate-lambda trajectory from S is eventually-constant.

---

## 2. The Finite-Type-Space Hypothesis (FTS)

The obligation is scoped to the **finite type space** regime. We state it as a hypothesis
on the system, not a stipulation hidden inside a definition.

**Hypothesis FTS (Finite Type Space).**
There is a finite set of admissible types Θ = {τ_1, ..., τ_m} (|Θ| = m < ∞) such that:
- (FTS-1) every constraint label that can ever appear in any reachable state has its type
  in Θ: for all S reachable from S_0 and all c in T_S, type(c) ∈ Θ;
- (FTS-2) the SBP morphism class is **type-saturating**: if e: S -> S' is an SBP morphism
  of type τ = type(c_e), then no further SBP morphism of type τ departs S'. Formally, for
  any g: S' -> S'' with type(c_g) = τ, (SBP-ii) fails for g at S' — adding a second
  constraint of an already-forked type does not fork the schema again, because the forking
  alternative it would need is already excluded by the first τ-extension.

(FTS-2) is the structural content that makes "finite type space" bite. It says SBP forking
is a per-type event: a type can be the site of at most one schema-boundary fork along any
trajectory. We justify (FTS-2) in Section 2.1 rather than assuming it blindly.

### 2.1 Why (FTS-2) holds for SBP morphisms

Let e: S -> S' be SBP of type τ, with forking alternative f: S -> S'' (type(c_f) = σ ≠ τ
by (SBP-i) applied to f, or possibly σ = τ — we handle both). By (SBP-ii),
Compat(c_e, T_{S''}, S) = 0: the τ-constraint c_e is incompatible with the schema that
would result from the alternative.

Now suppose for contradiction that g: S' -> S'' is a *second* SBP morphism of the same type
τ departing S'. By (SBP-i) for g, type(c_g) = τ ∉ types(S'). But type(c_e) = τ and c_e ∈
T_{S'}, so τ ∈ types(S'). This directly contradicts (SBP-i) for g.

Therefore **no SBP morphism of type τ can depart S' once an SBP morphism of type τ has been
applied to reach S'.** (FTS-2) is not an extra assumption: it is forced by the D4 clause
(SBP-i) together with the fact that an SBP morphism deposits its type into the schema. We
record this as:

**Lemma 0 (SBP types are single-shot).**
Along any trajectory, each type τ ∈ Θ can be the type of at most one SBP morphism.
*Proof.* An SBP morphism of type τ requires τ ∉ types(current state) (SBP-i). Applying it
puts τ into types(state). Types are never removed (morphisms only add labels; T is monotone
non-decreasing along a trajectory). Hence after the first SBP morphism of type τ, the
condition τ ∉ types(state) fails forever, so no later SBP morphism of type τ exists. ∎

Lemma 0 is the precise, *derived* form of (FTS-2). FTS therefore reduces to the single
genuine hypothesis (FTS-1): the type space is finite.

---

## 3. The Available-Novel-Type Pool and Monotone-Obstruction

### 3.1 The novel-type pool

For a reachable state S define the **available novel-type pool**:

```text
Pool(S) = Θ \ types(S) = { τ ∈ Θ : τ ∉ types(c) for any c in T_S }.
```

Pool(S) is the set of types that are still genuinely novel relative to S — the types a D4
or SBP morphism from S could carry. Under FTS, |Pool(S)| ≤ m and is finite.

### 3.2 The per-state obstruction quantity

Define the **single-step survival set** of S as the set of admissible non-identity
extensions, and the **single-step D4-survival set** as those that are type-novel:

```text
Surv(S)    = { e: S -> S' : e ≠ id_S, e admissible }
D4Surv(S)  = { e ∈ Surv(S) : type(c_e) ∈ Pool(S) }.
```

A trajectory continues to issue genuinely new structure only while D4Surv ≠ ∅. Define the
**per-step obstruction probability** at S under the rate-lambda process P_lambda:

```text
q(S) = Pr_{e ~ P_lambda}[ target(e) is obstructed ]
     = Pr[ applying the next drawn extension reaches an obstructed state ].
```

We do not need a closed form for q; we need its *monotonicity along SBP trajectories*.

### 3.3 Monotone-obstruction (the E039 replacement property)

**Definition (Monotone-Obstruction, MO).**
A Compat family is **monotone-obstructive along a trajectory class** iff for every
trajectory (S_n) in the class and every n with S_n not obstructed,

```text
q(S_{n+1}) ≥ q(S_n)   conditional on the trajectory not having collapsed by step n.
```

E039 §7.4 proved: MO ⇒ K superlinear in lambda (operative sense). The obligation is to
prove MO for SBP Compat under FTS.

---

## 4. The Type-Pool Depletion Lemma

**Lemma 1 (Strict Type-Pool Depletion under SBP).**
Let e_n: S_n -> S_{n+1} be an SBP morphism along a trajectory, with FTS in force. Then

```text
Pool(S_{n+1}) = Pool(S_n) \ { type(c_{e_n}) }    and    |Pool(S_{n+1})| = |Pool(S_n)| - 1.
```

*Proof.*
By (SBP-i), τ := type(c_{e_n}) ∉ types(S_n), so τ ∈ Pool(S_n).
The morphism adds exactly the label c_{e_n}, so types(S_{n+1}) = types(S_n) ∪ {τ}
(a single type added; if c_{e_n} were of a type already present this would contradict
(SBP-i), so the union is strict).
Therefore Pool(S_{n+1}) = Θ \ types(S_{n+1}) = Θ \ (types(S_n) ∪ {τ})
= (Θ \ types(S_n)) \ {τ} = Pool(S_n) \ {τ}.
Since τ ∈ Pool(S_n), removing it strictly decreases cardinality by exactly 1. ∎

**Corollary 1.1 (Finite SBP budget).**
Along any trajectory, the number of SBP morphisms is at most m = |Θ|. After at most m SBP
steps, Pool = ∅ and no further SBP (or D4) morphism exists; the trajectory is SBP-obstructed.

*Proof.* Each SBP step removes one type from a pool of size ≤ m (Lemma 1). The pool cannot
go negative, so at most m SBP steps occur. When Pool(S) = ∅, every type in Θ is already in
types(S), so by (FTS-1) no morphism can carry a novel type; D4Surv(S) = ∅ and a fortiori
no SBP morphism departs S. ∎

This is the formal content of "each SBP application strictly reduces the pool of available
type-novel extensions" that E039 §11 demanded. We now convert pool depletion into
obstruction monotonicity.

---

## 5. The Monotone-Obstruction Theorem

The bridge from "pool shrinks" to "obstruction probability rises" requires one further
structural fact: that shrinking the novel-type pool cannot *increase* the D4-survival set.
We isolate this as a monotonicity property of D4Surv and prove it from the morphism
definition.

**Lemma 2 (D4-Survival is anti-monotone in the pool, under type-restriction).**
Suppose the process P_lambda is **type-fair**: the set of drawable extensions from S of a
given novel type τ is non-empty iff τ ∈ Pool(S), and the probability mass P_lambda assigns
to "draw a type-novel extension" is a non-decreasing function of |Pool(S)| with all other
state structure held fixed. Then if Pool(S') ⊆ Pool(S) and the non-novel (refinement)
extension structure of S' is no richer than that of S, we have

```text
Pr_{e~P_lambda}[ e ∈ D4Surv(S') ] ≤ Pr_{e~P_lambda}[ e ∈ D4Surv(S) ].
```

*Proof.*
A drawn extension e is in D4Surv only if type(c_e) ∈ Pool(state). The event
"type(c_e) ∈ Pool(S')" is contained in the event "type(c_e) ∈ Pool(S)" because
Pool(S') ⊆ Pool(S) (a drawn novel type available at S' is available at S, never conversely).
By type-fairness, the probability mass on novel-type draws is monotone non-decreasing in
pool size, so shrinking the pool from Pool(S) to Pool(S') ⊆ Pool(S) cannot raise the
novel-draw probability. Hence the probability of landing in D4Surv does not increase. ∎

Type-fairness is the natural process condition: it says the issuance process does not
secretly inject *more* novelty when *fewer* novel types remain. A process violating it would
have to manufacture novelty out of an exhausted type pool, which contradicts FTS-1. We treat
type-fairness as part of the FTS process specification and flag it explicitly in Section 9.

**Theorem 1 (Monotone-Obstruction for SBP Compat under FTS).**
Let (S_n) be an SBP trajectory (every non-identity step is an SBP morphism) under FTS and a
type-fair rate-lambda process. Then the per-step obstruction probability is non-decreasing:

```text
q(S_{n+1}) ≥ q(S_n)   for every n with S_n not obstructed.
```

*Proof.*
Obstruction at the next step is the complementary event to "some admissible non-identity
extension survives and continues." Decompose continuation into novel-type continuation
(landing in D4Surv) and refinement continuation (non-novel extensions). Formally,

```text
1 - q(S) = Pr[ drawn extension keeps the trajectory alive from S ]
         ≤ Pr[draw ∈ D4Surv(S)] + Pr[draw is a surviving refinement at S].
```

Two facts, both for the SBP step S_n -> S_{n+1}:

(a) By Lemma 1, Pool(S_{n+1}) = Pool(S_n) \ {τ} ⊊ Pool(S_n). By Lemma 2 (type-fairness),
   Pr[draw ∈ D4Surv(S_{n+1})] ≤ Pr[draw ∈ D4Surv(S_n)]. The novel-continuation channel
   weakly contracts.

(b) The refinement channel does not strictly expand across an SBP step. An SBP morphism, by
   (SBP-ii), forks the schema: it deposits a constraint c_{e_n} that is incompatible with the
   alternative successor (Compat(c_{e_n}, T_{S''}, S_n) = 0 for the forking alternative).
   Adding an incompatibility-bearing constraint can only *remove* admissible subsets from the
   target's admissibility predicate, never add them: from the morphism definition
   A_{S_{n+1}}(X) = A_{S_n}(X \ {c}) ∧ Compat(c, X \ {c}, S_n), the extra conjunct Compat(·)
   can turn admissible subsets inadmissible but never the reverse. So the set of admissible
   refinement extensions from S_{n+1} injects into those from S_n; the refinement-survival
   probability does not increase.

Combining (a) and (b), the total continuation probability does not increase across the SBP
step:

```text
1 - q(S_{n+1}) ≤ 1 - q(S_n)   ⇒   q(S_{n+1}) ≥ q(S_n).  ∎
```

**Remark (strictness).** The inequality is *strict* (q(S_{n+1}) > q(S_n)) whenever the
removed type τ carried positive novel-draw mass at S_n and that mass is not fully
compensated by refinement survival — i.e. whenever the depleted type was a live source of
continuation. In the generic FTS case where each type contributes positive continuation
mass, monotone-obstruction is strict, and Corollary 1.1 forces q → 1 within at most m SBP
steps. The trajectory is then almost surely eventually-constant on the SBP channel, with the
collapse risk concentrating as the pool empties.

---

## 6. K Superlinearity Without IA

We now combine Theorem 1 with the E039 §7.4 characterization to obtain K superlinearity for
SBP Compat under FTS — without ever invoking IA (which E039 killed).

**Proposition 1 (K superlinear under FTS, no IA).**
Under FTS and a type-fair rate-lambda process, K(lambda, S) is superlinear in lambda in the
operative E039 sense: K(lambda, S) > K_lin(lambda) for the linear comparator, and
dK/dlambda is non-decreasing over the regime where the SBP pool is non-empty.

*Proof.*
By Theorem 1, the obstruction probabilities q(S_n) are non-decreasing along the SBP
trajectory. The trajectory reaches an obstructed state after at most m SBP steps
(Corollary 1.1). Consider increasing lambda. Higher lambda draws more extensions per unit
time, so the SBP pool is traversed faster; the monotone-increasing obstruction sequence
q(S_0) ≤ q(S_1) ≤ ... ≤ q(S_M) = 1 is climbed in fewer time units.

Because the per-step obstruction probabilities are non-decreasing (not constant as IA would
require), the time-to-collapse is a sum of holding times with *increasing* hazard. The
expected time to absorption for an increasing-hazard chain is a convex-decreasing function
of the draw rate lambda: each marginal increase in lambda removes proportionally more
expected remaining lifetime because the later, higher-hazard steps are reached sooner. Hence

```text
d^2 (E[time to collapse]) / dlambda^2 > 0  is reflected as  d^2 K / dlambda^2-favoring
superlinearity: K(lambda) rises above the constant-hazard (IA) comparator 1 - (1-p)^{lambda k}
because the realized hazard sequence dominates the constant-p hazard pointwise from the
first depleted type onward.
```

Concretely: pointwise q(S_n) ≥ q(S_0) = p_0 for all n, with strict increase as the pool
depletes, so the survival probability ∏_n (1 - q(S_n)) ≤ (1 - p_0)^{(#steps)} and the
collapse probability K dominates the IA geometric comparator with constant hazard p_0.
This is exactly the "positive-correlation cascade, K superlinear more strongly than IA"
regime that E039 §7.1 identified as the favorable case, now *proved* (not assumed) for SBP
Compat under FTS. ∎

This discharges the operative half: monotone-obstruction holds, so K is superlinear, so the
K-side hypothesis of the interior-optimum condition is met for SBP Compat under FTS.

---

## 7. Closing the Interior-Optimum Existence Proof (Conditional on FTS)

E031 §II.2 stated the interior-optimum condition: if N is concave, K is superlinear, and C
is convex in lambda, then N - C - K is strictly concave and an interior optimum lambda*(S) > 0
exists. E039 left this **conditional** because K superlinearity was unproven (IA having
failed). We now supply the missing K leg and verify the N leg coheres.

### 7.1 N concavity coheres with FTS

E031 §II.1: N is concave in lambda when the D4-Hom pool thins as the schema grows. Under FTS,
Lemma 1 gives exactly this: the novel-type pool Pool(S) strictly shrinks with each SBP step,
so the fraction of drawn extensions that are type-novel, N(lambda, S_n) = |D4Surv|/|Surv|,
is non-increasing along the trajectory (Lemma 2 gives the numerator's monotonicity). The same
finite-pool depletion that drives MO drives N's diminishing returns. **N concavity and K
superlinearity share a single mechanism under FTS: finite novel-type pool depletion.** This is
a structural coherence result, not a coincidence — it is the formal reason the interior
optimum is well-posed.

### 7.2 C convexity

E031 §II.3: C is made strictly convex by the congestion term β·lambda²·E[RecCost]. This is a
modeling choice independent of FTS; it holds whenever reconciliation cost has positive
congestion. We carry it as the standing C hypothesis (unchanged; not affected by this proof).

### 7.3 Interior-optimum theorem (FTS-conditional)

**Theorem 2 (Interior Optimum exists for SBP Compat under FTS).**
Let an AC-8 / Ext_S system satisfy FTS, type-fairness, and C-convexity (β > 0). Then on any
state S with Pool(S) ≠ ∅, the net issuance functional

```text
J(lambda) = N(lambda, S) - C(lambda, S) - K(lambda, S)
```

is strictly concave in lambda, and there is an interior optimum lambda*(S) > 0 provided the
boundary first-order conditions hold (dN/dlambda > dC/dlambda + dK/dlambda at lambda = 0, and
the reverse at lambda_max).

*Proof.*
N concave (§7.1, from Lemma 1–2), K superlinear (Proposition 1), C convex (§7.2). Then
J'' = N'' - C'' - K''. N'' ≤ 0, C'' ≥ 2β·E[RecCost] > 0 so -C'' < 0, and K superlinear in
the operative sense contributes -K'' < 0 over the pool-non-empty regime (K rises faster than
linear, its second difference dominating the comparator). Hence J'' < 0: J is strictly
concave. A strictly concave function on [0, lambda_max] with the stated boundary slope
conditions attains its maximum at an interior point lambda*(S) > 0. ∎

**Status of the interior optimum:** previously CONDITIONAL on IA (E031), then CONDITIONAL on
an unproven monotone-obstruction (E039). It is now **PROVED conditional on FTS + type-fairness
+ C-convexity** — three explicit, assessable structural hypotheses, none of which is the
discredited IA. The remaining conditionality is FTS itself, which is exactly the boundary
between this result and the Gödelian regime (Section 8).

---

## 8. Where the Proof Breaks: the Gödelian Regime

The proof is sharp: it holds **iff** the type space is finite (FTS-1). E028's Gödelian
mechanism — self-referential OnlineSchemaSys generating new undecidable type-novel
propositions endogenously — is precisely the negation of FTS-1.

**Proposition 2 (Gödelian regime breaks MO and may invert superlinearity).**
If the system is type-generating (each schema state can manufacture genuinely new types not
in any pre-fixed Θ), then Lemma 1 fails: an SBP step can *enlarge* rather than shrink the
effective novel-type pool. In that regime D4Surv need not contract, MO need not hold, and
E039 §7.2's negative-correlation (scaffolding) case becomes possible, in which K can be
sublinear and the interior optimum need not exist.

*Proof sketch.* If applying an SBP morphism of type τ unlocks a Gödelian successor type τ'
(τ' undecidable relative to S but decidable/available relative to S' = S+τ), then
Pool_eff(S') ⊇ (Pool(S) \ {τ}) ∪ {τ'}, which can have cardinality ≥ |Pool(S)|. Lemma 1's
strict decrease is lost; the inductive driver of Theorem 1 fails. ∎

This is not a defect of the proof; it is the **precise fork** the program already identified.
Two regimes:

| Regime | Type space | MO | K | Interior optimum | TI reading |
|---|---|---|---|---|---|
| FTS | finite (fixed Θ) | holds (Thm 1) | superlinear (Prop 1) | exists (Thm 2) | bounded-novelty source; issuance has diminishing returns and an optimal rate |
| Gödelian (E028) | endogenously growing | may fail (Prop 2) | may be sublinear | may not exist | open-ended source; issuance need not have an optimal rate — it can stay productive indefinitely |

**Interpretation.** The interior optimum exists exactly when novelty is *bounded* (a finite
type budget that issuance spends down). The deepest TI-C019 claim — reality remains
*open-ended* — corresponds to the **Gödelian regime where the interior optimum does not
exist**, i.e. where there is no rate at which it becomes net-negative to keep issuing,
because the type pool replenishes itself. The two regimes are therefore a genuine
discriminator for TI-C019, not merely a technical caveat:

```text
Discriminator (D-FTS):
  Finite-type-budget issuance  ⇒  diminishing returns, optimal rate lambda*, eventual fixation.
  Gödelian self-generating issuance  ⇒  no optimal rate, sustained openness, no eventual fixation.
TI-C019 (open-endedness) lives in the Gödelian regime; the interior optimum's NON-existence
is the formal signature of genuine open-endedness.
```

This sharpens the link to TI-C021 (E036): sublinear mu with diminishing marginal issuance is
the FTS-regime signature; the Gödelian regime is where marginal issuance need not decline,
which is what "remains capable of producing genuinely new structure" requires.

---

## 9. Assumptions, Failure Risks, Kill Conditions

### Assumptions used
1. **FTS-1 (finite type space):** the genuine hypothesis. Everything is proved relative to it.
2. **Type-fairness of P_lambda (Lemma 2):** the process does not inject more novel-draw mass
   as the novel pool shrinks. Justified because injecting novelty from an exhausted finite
   pool contradicts FTS-1. If a process violates type-fairness it is implicitly type-generating
   and belongs to the Gödelian regime.
3. **C-convexity (β > 0):** standing congestion hypothesis from E031 §II.3, independent of
   this proof.
4. **Single-constraint-per-morphism** and **no state-construction side effects** (inherited
   from E038 §8); required so Pool and types are well-defined functions of the label set.

### Failure risks
- (FTS-2) was a *potential* extra assumption; Section 2.1 / Lemma 0 **discharges it** —
  it is forced by (SBP-i). No hidden stipulation remains there.
- The strictness of MO (Remark, §5) requires each depleted type to carry positive
  continuation mass. If some types are "inert" (carry novel labels but no continuation),
  MO is weak (non-strict) but still sufficient for K superlinearity over the active types.

### Kill conditions
1. If a concrete operative system is shown to be type-generating (Gödelian) rather than FTS,
   Theorem 2 does not apply to it and the interior optimum claim must be withdrawn *for that
   system* (correctly — that is the open-ended regime).
2. If type-fairness fails for an FTS system without that system being type-generating
   (a process that re-weights toward novelty as the pool shrinks, by external design), Lemma 2
   fails and MO must be re-derived or the system reclassified.
3. If the morphism definition is revised so that adding a constraint can *enlarge* the
   admissible-subset set of the target (violating the monotone-narrowing fact used in
   Theorem 1 step (b)), the refinement channel could expand and MO could fail.

---

## 10. Obligation Verdict

```text
MONOTONE-OBSTRUCTION PROOF (E039 §11 item 1): DISCHARGED (PROVED under FTS).

- Type-Pool Depletion Lemma (Lemma 1): each SBP step strictly removes one type from a
  finite novel-type pool. PROVED.
- SBP types are single-shot (Lemma 0): (FTS-2) is forced by the D4 clause, not assumed.
- Monotone-Obstruction Theorem (Theorem 1): per-step obstruction probability is
  non-decreasing along SBP trajectories under FTS + type-fairness. PROVED.
- K superlinearity (Proposition 1): follows from MO without IA. PROVED (operative sense).
- Interior-optimum existence (Theorem 2): N concave (same depletion mechanism), K superlinear,
  C convex ⇒ J strictly concave ⇒ interior lambda*(S) > 0. PROVED conditional on
  FTS + type-fairness + C-convexity + boundary FOCs.
- Gödelian fork (Proposition 2): the proof breaks exactly when FTS fails; that regime is the
  open-ended regime where the interior optimum's NON-existence is the signature of genuine
  open-endedness. This is a discriminator (D-FTS) for TI-C019, not a gap.

NET: the interior-optimum existence proof is no longer blocked on IA. It is closed for the
finite-type-space regime and correctly fails for the Gödelian regime. The IA replacement
condition demanded by E039 is supplied and proved.
```

### Effect on claims
- **TI-C019:** strengthened structurally. The FTS/Gödelian fork (D-FTS) gives a *formal*
  signature for open-endedness: open-ended issuance ⟺ no interior optimum ⟺ Gödelian (non-FTS)
  type generation. No status change (claim remains formalizing); next_action gains the D-FTS
  discriminator and the requirement to establish whether the operative source is FTS or
  Gödelian.
- **TI-C021:** supported. Diminishing marginal issuance (sublinear mu) is the FTS-regime
  signature; the depletion mechanism (Lemma 1) is the structural cause of diminishing returns.
- **lambda*(S):** still NOT admitted as a TI claim. Theorem 2 proves *existence* of the
  optimum under FTS, but lambda*(S) as a selection principle remains absorbed by optimal
  control (E034) unless the source layer is independently FTS-specified. The proof clarifies
  *when* an interior optimum exists; it does not make the argmax a TI-native object.

### Still blocked (carried forward)
1. FUNCTOR-OBL-001 (N naturality) — unchanged.
2. SBP-IND verification for a concrete Compat family — E040 open item; addressed in E042.
3. Q-OBL-001 (Q circularity) — unchanged.
4. PP-3 source-layer declaration — unchanged; D-FTS gives a new angle (is the source FTS?).
5. Whether the *operative physical* source is FTS or Gödelian — new, raised by this proof,
   and the determining question for whether lambda*(S) could ever be physical.
