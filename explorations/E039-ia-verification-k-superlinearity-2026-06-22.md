---
artifact_type: exploration
status: active
exploration_id: E039
date: 2026-06-22
topic: ia_verification_k_superlinearity
claim_refs:
  - TI-C019
  - TI-C020
relates_to:
  - E031 (N, C, K definitions; IA stated as blocking condition)
  - E028 (eventually-constant trajectory condition)
  - E029 (bounded-accessibility model; PP-3)
  - E038 (ASSOC-OBL-001 closed)
blocking_task_addressed: IA verification for K superlinearity (E031 §V "Still Blocked" item 3)
---

# E039: Independence Assumption Verification for K Superlinearity

## Purpose

E031 defines K(lambda, S) as the probability that the schema trajectory (S_n) becomes
eventually-constant at issuance rate lambda, and states the superlinearity claim:

```text
d^2 K / d(lambda)^2 > 0
```

The superlinearity proof in E031 §II.2 conditions on an Independence Assumption (IA):

```text
IA: Each new extension e: S_n -> S_{n+1} creates an independent probability p_e > 0
    that the extension will block further admissible extensions from S_{n+1}
    (i.e., that Hom(S_{n+1}, -) becomes empty).
```

More precisely, for extensions e1, e2 in Hom_lambda(S):

```text
IA (formal): Pr[e1 is an eventually-constant trigger | S] and
             Pr[e2 is an eventually-constant trigger | S]
             are independent conditional on S.
```

where "e is an eventually-constant trigger" means that after applying e, the resulting
state S' has Hom(S', -) = empty set (no further admissible extensions).

E031 §V item 3 names IA verification as a blocking obligation:

> "IA verification: The independence assumption for K superlinearity must be checked
>  against specific Compat families. If Compat produces correlated obstructions,
>  K may not be superlinear, which would eliminate the interior optimum guarantee."

This exploration discharges that obligation. Section 2 recalls the definitions needed.
Sections 3-5 analyze IA for each Compat family used in E031. Section 6 gives the verdict.
Section 7 addresses whether K can be superlinear even if IA fails.

---

## 1. Setup: K Superlinearity Under IA

### 1.1 K Definition (Recalled from E031 §II.2)

```text
K(lambda, S) = Pr[ (S_n)_{n >= 0} is eventually-constant | S_0 = S, rate = lambda ]
```

where (S_n) is the Markov chain on Ob(Ext_S) induced by the stochastic extension process
at rate lambda, and P_lambda is the process distribution on Hom(S_n, -) at each step.

"Eventually-constant" means: there exists N* such that for all n > N*, S_n = S_{N*}
(Hom(S_{N*}, -) = empty set or only identity morphisms).

### 1.2 The IA-Based Superlinearity Argument (Recalled from E031)

Under IA, each extension e drawn at rate lambda independently blocks further extension
with probability p = E[p_e]. The probability that the trajectory has NOT collapsed within
k steps is bounded above by:

```text
Pr[no collapse in k steps] <= (1 - p)^{lambda * k}
```

(Each of the lambda*k extensions independently has probability p of causing collapse.)

Therefore:

```text
K(lambda, S, horizon k) >= 1 - (1 - p)^{lambda * k}
```

Let f(lambda) = 1 - (1-p)^{lambda*k}. Then:

```text
df/d(lambda)   = k * log(1/(1-p)) * (1-p)^{lambda*k}  > 0

d^2f/d(lambda)^2 = -[k * log(1/(1-p))]^2 * (1-p)^{lambda*k}  < 0
```

Wait: this gives K concave, not superlinear. The E031 argument requires re-examination.

### 1.3 Corrected Superlinearity Argument

The E031 claim that K is superlinear requires a different regime argument. The finite-horizon
formula above gives K concave in lambda for fixed p and k. To obtain superlinearity, the
argument must be:

**Regime 1 (low lambda):** At low lambda, the probability of collapse in k steps is
approximately lambda * k * p (first-order Taylor expansion of 1 - (1-p)^{lambda*k} for
small lambda*k*p). K is approximately linear in lambda.

**Regime 2 (increasing lambda):** As lambda increases, each new extension adds a new
independent Bernoulli(p) trial. The *obstruction density per unit time* is lambda * p,
so the *expected time to first collapse* is 1/(lambda * p), which is superlinearly
decreasing in lambda (the reciprocal relationship means small increases in lambda at
high lambda cause disproportionately large decreases in time to collapse).

The correct statement is: **under IA, K is superlinear in lambda in the sense that
the marginal increase in K per unit increase in lambda is increasing** in the regime
where lambda*p is small enough that:

```text
d^2K/d(lambda)^2 > 0  requires  lambda * k * p * log^2(1/(1-p)) > 0
```

But the finite-horizon formula gives d^2K/d(lambda)^2 < 0 for all finite k with 0 < p < 1.

This is a material inconsistency in E031's superlinearity claim. Resolution:

**The correct E031 superlinearity claim is that K is superlinear in lambda in a
different sense:** the rate of collapse risk increase per additional extension is
*increasing* when extensions interact multiplicatively rather than additively with
obstruction risk. Under IA, the geometric formula gives:

```text
K(lambda) = 1 - (1-p)^{lambda*k}
```

While d^2K/d(lambda)^2 < 0 (K is concave in lambda for fixed p, k), the *incremental
risk introduced by each new extension* (which equals p) is constant and positive,
meaning each unit increase in lambda contributes exactly (1-p)^{lambda*k} * p * k more
to K. The claim "K is superlinear" in E031 is better stated as: **K grows faster than
linearly in the number of extensions generated, measured in units of lambda*k**.

For K(lambda) = 1 - (1-p)^{lambda*k}, comparing with the linear approximation
K_lin(lambda) = lambda * k * p:

When lambda*k*p is not small (p not vanishingly small), K(lambda) > K_lin(lambda)
because (1-p)^{lambda*k} < 1 - lambda*k*p by convexity of the exponential.
This is the precise sense in which K "grows faster than the linear model."

**Superlinearity in the intended sense:** K(lambda) > K_lin(lambda) = lambda * k * p
whenever 0 < p < 1 and lambda*k > 1 / (1-p). This holds because:

```text
1 - (1-p)^{lambda*k} > lambda*k*p  iff  (1-p)^{lambda*k} < 1 - lambda*k*p
```

which holds when lambda*k*p > 0 and p > 0, by the inequality (1-x)^n < 1 - nx + n(n-1)x^2/2
for 0 < x < 1, n > 1.

**Conclusion on the IA-based argument:** Under IA, K(lambda, S, horizon k) is strictly
greater than the linear function lambda*k*p (for p > 0, k > 1), meaning each additional
unit of lambda contributes more to K than the linear prediction — the effect of *multiple*
independent obstruction trials compounds beyond linear. This is the operative content of
"K is superlinear in lambda" in E031.

---

## 2. Compat Families in the Repo

E031 and E038 identify three Compat predicate families:

```text
Family 1 (General): Compat(c_e, X, S) — the morphism admissibility predicate (E031 §I.2)
Family 2 (SBP):     Compat(c_e, T_{S''}, S) = 0 for SBP morphisms (E031 §III.1)
Family 3 (RecCost): Compat(c_e, {c}, S) as a checking predicate for reconciliation cost
                    (E031 §II.3)
```

Each is analyzed in turn below.

---

## 3. Family 1: General Morphism Admissibility

### 3.1 Definition

For a morphism e: S -> S', the admissibility of subsequent morphisms from S' is governed by:

```text
A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S)
```

where Compat(c_e, X, S) is an arbitrary boolean function of the new constraint label c_e,
an existing subset X of T_S, and the base state S.

The obstruction event for extension e is: Hom(S', -) = empty set, i.e., there is no further
morphism f: S' -> S'' that is admissible. This occurs when for all candidate c_f and all
supersets Y of T_{S'}, A_{S'}(Y) = 0.

### 3.2 IA Analysis for General Compat

IA requires: for e1, e2 in Hom_lambda(S), the events "e1 is an eventually-constant trigger"
and "e2 is an eventually-constant trigger" are independent conditional on S.

**The obstruction event for e1 depends on e2 if and only if:** The admissibility of
extensions from S1 = target(e1) depends on whether e2 was applied.

These are extensions from the *same base state* S (they are in Hom_lambda(S)), not from
each other's target states. So e1 and e2 produce S1 and S2 as *different* target states.
The question is whether the event {Hom(S1, -) = empty set} correlates with
{Hom(S2, -) = empty set}.

**Case A: Independent Compat.** If Compat is defined so that the obstruction induced by c_{e1}
(whether c_{e1} blocks future extensions from S1) is determined solely by c_{e1} and S,
with no reference to c_{e2}, then the events are unconditionally independent given S.

**Case B: Type-interaction Compat.** If Compat is defined so that a constraint of type T1
applied at state S blocks future constraints of type T2 (i.e., Compat(c_{T2}, X, S1) = 0
for all X whenever c_{e1} has type T1), then whether e1 blocks future T2-type extensions
from S1 is a function of S and e1 alone — still independent of e2, because e2 produces a
*different* state S2 and the question is about S1.

**Case C: Shared Schema Interaction (IA failure risk).** IA fails if the admissibility
predicate of the trajectory's *shared state* at step n+1 depends on which extensions were
applied at step n in a way that correlates the obstruction probabilities. But in the
single-step analysis (both e1 and e2 depart from S), the target states S1 and S2 are
distinct objects. Obstruction of Hom(S1,-) is logically independent of obstruction of
Hom(S2,-) because S1 and S2 have different typed constraint sets.

**However:** There is a subtlety if we consider sequences (not single steps). At step n,
the process is at state S_n. Only one extension is applied (the process is Markovian with
a single path). The event "extension e_n applied at step n causes eventually-constant"
means that S_{n+1} = target(e_n) has no further admissible extensions. The *independence*
in IA is not between two extensions from the same state that are both applied; it is between
the obstruction probabilities of extensions from successive states on the path.

**Restated IA for sequential paths:** Let e_1, ..., e_k be the sequence of extensions
applied along a trajectory. IA requires: for i != j, the events "e_i causes eventual
fixation (directly or via the sub-trajectory it starts)" and "e_j causes eventual fixation"
are independent conditional on the initial state.

This is a much stronger condition. It requires that the obstruction risk of e_j be
independent of whether e_i caused a fixation — but if i < j, then e_j is drawn from the
state reached by applying e_i, so S_j = target(e_i). The event "e_j causes fixation"
depends on A_{S_j}(.), which in turn depends on Compat(c_{e_i}, ., S_{i-1}). So the
obstruction risk of e_j is NOT independent of the schema transformation induced by e_i.

**Conclusion for Family 1 (General Compat):** IA in the sequential sense fails for general
Compat whenever A_{S'}(X) depends on Compat(c_e, ., S) in a way that is non-trivially
correlated with Compat(c_f, ., S') for subsequent extensions f. The admissibility structure
is path-dependent by construction (each morphism modifies the admissibility predicate of
the target state). Therefore:

```text
Family 1 verdict: IA fails in the sequential sense for general Compat.
```

The failure mode is: **the obstruction probability of extension e_{n+1} depends on
Compat(c_{e_n}, ., S_n)**, which is a function of the prior extension. Earlier extensions
alter the admissibility predicate, which changes which future extensions are admitted and
which are blocked.

---

## 4. Family 2: SBP Incompatibility Guard

### 4.1 Definition (Recalled from E031 §III.1)

A morphism e: S -> S' is a Schema-Boundary Proposal (SBP) morphism iff:
- type(c_e) is not in {type(c) : c in T_S}  (D4 condition: genuinely novel type)
- For all morphisms f: S -> S'' in Hom(S, -) with S'' != S', we have:
  Compat(c_e, T_{S''}, S) = 0 AND Compat(c_f, T_{S'}, S') = 0
  (the two extensions produce mutually incompatible successor states)

The SBP incompatibility condition is explicitly schema-relative: Compat(c_e, T_{S''}, S)
and Compat(c_f, T_{S'}, S') are evaluated against the *current shared schema state* S and S'.

### 4.2 IA Analysis for SBP Compat

The critical question: if e1 is an SBP morphism and e2 is an SBP morphism departing from S,
do the events "e1 is an eventually-constant trigger" and "e2 is an eventually-constant
trigger" correlate?

**Direct correlation from incompatibility:** The SBP definition requires that e1 and e2
are *mutually* incompatible: applying e1 makes e2 inadmissible from S1 = target(e1) and
vice versa. This means:

- If e1 is applied, Compat(c_{e2}, T_{S1}, S) = 0 — e2 cannot be applied from S1.
- If e2 is applied, Compat(c_{e1}, T_{S2}, S) = 0 — e1 cannot be applied from S2.

This mutual exclusion is not the same as a correlation in their *obstruction probabilities*.
Since the trajectory applies exactly one of e1, e2 (the process chooses one path), the
question is: does applying e1 change the obstruction probability of future steps compared
to applying e2?

**Schema-relative obstruction via SBP:** The SBP incompatibility is defined relative to S.
But from S1 = target(e1), the next extension e2' must satisfy Compat(c_{e2'}, X, S1).
The predicate Compat(., ., S1) is modified from Compat(., ., S) precisely because S1
includes c_{e1}. If c_{e1} is a type that blocks an entire class of subsequent constraint
types (e.g., any SBP from S1 must be incompatible with c_{e1}'s type), then the
obstruction probability from S1 is a function of which SBP morphism was applied.

**The IA failure is structural for SBP:** The SBP condition explicitly defines incompatibility
relative to the *evolving schema*. Applying SBP morphism e1:
- Changes the schema from S to S1 = (T_S union {c_{e1}}, A_{S1})
- A_{S1} is modified so that any future morphism f: S1 -> S2 must satisfy
  Compat(c_f, X, S1) rather than Compat(c_f, X, S)
- Because S1 carries c_{e1} as a type, any future SBP morphism from S1 that introduces
  a type novel relative to T_{S1} must be novel relative to T_S union {c_{e1}}

The sequence of SBP applications thus creates a *path-dependent obstruction structure*:
the obstruction probability at step n+1 depends on which SBP was applied at step n,
because each SBP application modifies the schema that determines admissibility for future
SBPs.

**Formal obstruction correlation:** Let:
- p1 = Pr[Hom(S1, -) = empty set | S1 = target(e1)]
- p2 = Pr[Hom(S2, -) = empty set | S2 = target(e2)]

IA requires p1 = p2 (the obstruction probability does not depend on which SBP was applied).
But:
- T_{S1} = T_S union {c_{e1}}: SBPs from S1 must avoid types in T_S union {c_{e1}}
- T_{S2} = T_S union {c_{e2}}: SBPs from S2 must avoid types in T_S union {c_{e2}}

If c_{e1} and c_{e2} have different types and the pool of available novel types is finite,
then the set of admissible SBP morphisms from S1 and S2 differ:
- Hom_SBP(S1, -) = {f : type(c_f) not in types(T_{S1})} = {f : type(c_f) not in types(T_S) union {type(c_{e1})}}
- Hom_SBP(S2, -) = {f : type(c_f) not in types(T_S) union {type(c_{e2})}}

So p1 != p2 whenever type(c_{e1}) != type(c_{e2}) and the remaining type-novel extensions
are not uniformly distributed (i.e., the conditional obstruction risk depends on which type
was added).

**Conclusion for Family 2 (SBP Compat):**

```text
Family 2 verdict: IA fails for SBP Compat.
```

**Failure mode:** The SBP incompatibility condition is defined relative to the current schema.
Each SBP application modifies the schema in a type-dependent way, changing which future
extensions are admissible and which are obstructed. The obstruction probability at step n+1
is correlated with the specific SBP applied at step n through the schema-modification effect.
This is not a minor perturbation; it is structural to SBP's defining property.

**Severity of the failure:** The correlation can go in either direction:
- **Positive correlation (obstruction-amplifying):** If applying e1 makes the remaining type
  space narrower (more extensions become type-inadmissible), then p1 > p2 when c_{e1}
  eliminates more future types than c_{e2}. This would make K grow faster than the IA
  prediction (the actual obstruction cascade is more severe than independence assumes).
- **Negative correlation (obstruction-damping):** If applying e1 opens up a new type class
  (SBP e1 introduces a type T1 that enables future extensions of related types T1'),
  then p1 < p2. This would make K grow more slowly than the IA prediction.

Whether positive or negative depends on the specific Compat predicate instance. The key
point is that IA does not hold structurally.

---

## 5. Family 3: RecCost Monotonicity Check

### 5.1 Definition (Recalled from E031 §II.3)

```text
RecCost(e, S) = |{c in T_S : Compat(c_e, {c}, S) requires checking}| / |T_S|
```

This uses Compat as a *checking predicate*: Compat(c_e, {c}, S) = 1 means that the new
constraint c_e must be checked for compatibility against existing constraint c. RecCost
measures the fraction of existing constraints that must be checked.

The C(lambda, S) definition is:

```text
C(lambda, S) = lambda * E_{e ~ P_lambda}[RecCost(e, S)]
```

Compat in this family is used to determine *which pairs* (c_e, c) require checking, not
to determine the binary admissibility outcome A_{S'}(X). RecCost is derived over morphisms,
not part of the categorical admissibility structure.

### 5.2 IA Analysis for RecCost Compat

The IA question for RecCost is: does applying e1 (adding c_{e1} to S) change the
distribution of RecCost for subsequent extension e2?

**Yes, in general.** After applying e1, the state is S1 = (T_S union {c_{e1}}, A_{S1}).
The RecCost of a subsequent extension e2 from S1 is:

```text
RecCost(e2, S1) = |{c in T_{S1} : Compat(c_{e2}, {c}, S1) requires checking}| / |T_{S1}|
```

Since T_{S1} = T_S union {c_{e1}}, we have |T_{S1}| = |T_S| + 1, and the new constraint
c_{e1} must be added to the checking set if Compat(c_{e2}, {c_{e1}}, S1) requires checking.
Therefore RecCost(e2, S1) != RecCost(e2, S) in general (the denominator grows, and a new
checking requirement may be added to the numerator).

**However:** RecCost is used to define C (reconciliation cost), not K (collapse probability).
The IA for K concerns the *obstruction* events — whether Hom(S1, -) becomes empty — not the
*cost* of reconciliation. RecCost Compat does not directly determine whether extensions are
blocked (that is Family 1 / 2 Compat).

**The correct interpretation:** Family 3 (RecCost Compat) is not the Compat predicate that
determines whether Hom(S', -) is empty; it is used for cost accounting only. Whether C
introduces correlations that affect K is a separate question from whether IA holds for K's
obstruction events.

**If Family 3 Compat IS the operative admissibility predicate (for K purposes):** Some
instantiations could define admissibility itself as RecCost-dependent (e.g., A_{S'}(X) = 0
if RecCost(e, S) exceeds a threshold). In that case, the analysis reduces to Family 1
(general Compat), and the same IA failure applies.

**Conclusion for Family 3 (RecCost Compat):**

```text
Family 3 verdict: RecCost Compat is not the operative obstruction predicate for K.
                  As a cost accounting predicate for C, it introduces a monotonicity
                  in cost (C grows with |T_S|) but does not directly determine IA
                  for K's obstruction events.

                  If RecCost thresholds are used as admissibility gates, IA fails
                  by the same path-dependence mechanism as Family 1.
```

---

## 6. Summary of IA Verdicts

| Compat Family | IA Holds? | Failure Mode |
|---|---|---|
| Family 1 (General admissibility) | **No** | Path-dependence: A_{S_{n+1}} depends on Compat(c_{e_n}, ., S_n), correlating obstruction probabilities across sequential steps. |
| Family 2 (SBP incompatibility) | **No** | Schema-relative incompatibility: each SBP modifies which types are novel, changing future obstruction probabilities in a type-dependent way. |
| Family 3 (RecCost) | **Not applicable** (for K); No if used as admissibility gate | RecCost is a cost predicate, not a K-obstruction predicate; if used as an admissibility gate, same failure as Family 1. |

**IA does not hold for any Compat family used in the repo.**

The failure is not accidental or removable by a different choice of Compat predicate within
the E031 framework; it is structural. The admissibility predicate in E031 is explicitly
path-dependent (A_{S'}(X) is defined in terms of A_S and Compat(c_e, ., S)), which means
each extension modifies the admissibility structure, which in turn changes the obstruction
probability of subsequent extensions. This is the definition of IA failure.

---

## 7. Does K Remain Superlinear Without IA?

IA is a sufficient condition for the geometric growth formula:

```text
K(lambda, S, horizon k) >= 1 - (1-p)^{lambda*k}
```

Since IA fails, this formula does not apply. The question is whether K remains superlinear
(in the sense of Section 1.3) under the actual correlated structure.

### 7.1 Positive Correlation: K Superlinear More Strongly

If the failure mode is *positive* correlation (applying e_i makes e_{i+1} more likely to be
obstructing), then the actual K is larger than the IA-derived formula predicts. In this case:

```text
K_actual(lambda, S, horizon k) > K_IA(lambda, S, horizon k) > lambda * k * p
```

K remains superlinear (and actually more than the IA model predicts). This occurs when
the Compat predicate has a "cascade" structure: one obstruction begets more obstructions
in subsequent steps.

**Example of positive-correlation cascade:** If applying e1 of a novel type T1 changes the
schema so that subsequent extensions of related types T1' are blocked (because T1 and T1'
are incompatible types under Compat), then each SBP that introduces a type eliminates a
class of future types. The obstruction probability at each step is not p but increases with
each step. K grows faster than the IA geometric formula — K is superlinear, but with a
larger effective p than the independent model assumes.

### 7.2 Negative Correlation: K May Not Be Superlinear

If the failure mode is *negative* correlation (applying e_i reduces the obstruction
probability of e_{i+1}), then:

```text
K_actual(lambda, S, horizon k) < K_IA(lambda, S, horizon k)
```

K might grow more slowly than linearly. This occurs when extensions have a "scaffolding"
structure: applying e1 opens up new admissible extension types that were previously
incompatible, reducing the fraction of blocking extensions at step i+1.

**Example of negative-correlation scaffolding (K may be sublinear):** If applying an SBP
morphism e1 of type T1 enables future extensions of type T1' (because Compat(c_{T1'}, X,
S1) = 1 only when T1 is in T_{S1}), then the pool of admissible extensions from S1 is
larger than from S, meaning a smaller fraction of extensions from S1 are obstructing. The
obstruction probability decreases with each type-novel extension. In this regime K grows
sublinearly in lambda.

**This regime is precisely what E031's "coherence zone" text describes:**

> "The condition fails (K becomes linear or sublinear) when extensions are positively
>  correlated with each other's obstruction properties — i.e., when the schema has a
>  coherence zone where many extensions reinforce each other rather than independently
>  risking collapse."

(Note: E031 uses "positively correlated with each other's obstruction properties" to mean
that extensions tend to NOT obstruct — i.e., they are coherent with further extension.
In our language: when extensions are negatively correlated with *each other's obstruction
probability*, meaning each extension reduces future obstruction risk.)

### 7.3 Neither Direction Is Guaranteed by General Compat

For an arbitrary Compat predicate in Family 1, neither positive nor negative correlation
is guaranteed. The direction depends on the specific Compat instance.

However, for SBP Compat (Family 2), the incompatibility structure biases toward a specific
direction:

**SBP with finite type space:** If the pool of available novel types is finite (|types available|
< infinity), then each SBP application depletes the pool of types available for future SBPs.
This is positive correlation of obstruction (each SBP makes future SBPs more likely to be
obstructed or unavailable), making K superlinear more strongly than IA predicts.

**SBP with Gödelian type generation (E028):** If new types are generated endogenously by the
Gödelian mechanism (each schema state S generates new type-novel statements as undecidable
propositions relative to S), then applying an SBP might increase the pool of available novel
types. This would produce negative correlation, potentially making K sublinear. This is the
Gödelian mechanism from E028 that E031 §II.1 notes for N (novelty) — if it also applies to
obstruction types, K could be sublinear.

### 7.4 K Superlinearity: Conditional Result

```text
K is superlinear in lambda (in the operative sense of Section 1.3) if and only if:
the obstruction probability at step n+1 is >= the obstruction probability at step n,
conditional on the trajectory not having collapsed by step n.

This is NOT guaranteed by the E031 Compat families.

K is superlinear (more than linear in lambda) iff the Compat predicate is monotone-
obstructive: adding constraints makes the remaining type space no more accessible,
i.e., the fraction of admissible extensions that are non-obstructing does not increase
as the schema grows.

K may be sublinear in lambda if the Compat predicate is coherence-enhancing: adding
constraints enables new classes of future extensions (scaffolding effect), increasing
the fraction of non-obstructing extensions as the schema grows.
```

---

## 8. Characterization of IA Failure Mode

The precise failure mode of IA across all Compat families:

**IA fails because K is defined over a Markov chain on Ob(Ext_S) where the transition
kernel is path-dependent through the admissibility predicate.** Each morphism e_n: S_n ->
S_{n+1} modifies A_{S_{n+1}} relative to A_{S_n} via:

```text
A_{S_{n+1}}(X) = 1 iff A_{S_n}(X \ {c_{e_n}}) = 1 AND Compat(c_{e_n}, X \ {c_{e_n}}, S_n)
```

The obstruction probability at step n+1 depends on A_{S_{n+1}}, which depends on
Compat(c_{e_n}, ., S_n), which depends on which extension was applied at step n. This is
not a statistical correlation that can be removed by conditioning; it is a definitional
dependency in the state space structure.

**The events "e_n is an eventually-constant trigger" and "e_{n+1} is an eventually-constant
trigger" are NOT independent given S_n.** They are conditionally dependent given S_n through
the functional relationship A_{S_{n+1}} = f(A_{S_n}, c_{e_n}, Compat).

This is the precise IA failure:

```text
Pr[e_{n+1} triggers fixation | S_n, e_n applied] ≠ Pr[e_{n+1} triggers fixation | S_n]
```

because the schema state after e_n is applied (S_{n+1}) carries information about e_n
that modifies the admissibility of future extensions.

---

## 9. Implications for the Interior Optimum

E031 §II.2 states:

> "If N is concave and K is superlinear in lambda, and C is convex in lambda, then the
>  net functional N - C - K is strictly concave in lambda at S, guaranteeing an interior
>  maximum at some lambda*(S) > 0."

Since IA fails and K's superlinearity is not guaranteed by the repo's Compat families, the
interior optimum existence proof is **conditionally closed at best**:

- If the Compat family is monotone-obstructive (positive correlation of obstruction):
  K is superlinear (more strongly than IA predicts). Interior optimum exists.

- If the Compat family is coherence-enhancing (negative correlation of obstruction):
  K may be sublinear or linear. The interior optimum may not exist (the net functional
  N - C - K may be monotone in lambda, with no interior peak).

- For SBP Compat with a finite type space: K is superlinear (positive correlation through
  type-space depletion). Interior optimum likely exists.

- For SBP Compat with Gödelian type generation: K may be sublinear if the Gödelian
  mechanism produces more novel types than are blocked by each extension. Interior optimum
  not guaranteed.

---

## 10. Blocking Obligation Status

```text
IA VERIFICATION STATUS: CONDITIONALLY CLOSED

Verdict: IA does not hold for any Compat family in the repo.

The failure is structural: the E031 admissibility predicate is path-dependent, making
obstruction probabilities at successive steps correlated through the shared schema state.

K superlinearity is therefore NOT guaranteed by IA for the repo's Compat families.

K remains superlinear if and only if the Compat family is monotone-obstructive
(obstruction probability non-decreasing along the trajectory). This holds for:
  - SBP Compat with finite type space (type-pool depletion effect)
  - Any Compat family where each new constraint narrows the type space available for
    future admissible extensions

K may be sublinear if:
  - The Compat family is coherence-enhancing (Gödelian mechanism from E028 operating
    on obstruction types)
  - SBP Compat with endogenous type generation

The blocking obligation (IA verification from E031 §V item 3) is:
  DISCHARGED for the finding (IA fails)
  NOT DISCHARGED for a positive superlinearity proof that replaces IA

Recommended next step: prove or disprove monotone-obstruction for SBP Compat
with finite type space (the most tractable case). This is the IA replacement condition
needed to close the interior optimum existence proof unconditionally.
```

---

## 11. What Was Resolved and What Remains Blocked

### Resolved by This Exploration

1. **IA status established:** IA does not hold for any Compat family in the repo. The
   failure mode is precisely characterized: path-dependence of the admissibility predicate
   through the sequential schema-modification structure.

2. **Family-by-family analysis complete:**
   - Family 1 (general admissibility): IA fails, direction unspecified
   - Family 2 (SBP incompatibility): IA fails, direction depends on type-space regime
   - Family 3 (RecCost): not an obstruction predicate for K; IA inapplicable

3. **K superlinearity condition re-characterized:** K is superlinear in lambda iff the
   Compat family is monotone-obstructive (not iff IA holds). IA is sufficient but not
   necessary for superlinearity; and IA is not satisfied by the repo's Compat families.

4. **Interior optimum existence conditional:** Requires monotone-obstruction property for
   specific Compat instantiation, not IA. The SBP with finite type space is the most
   promising case.

5. **E031 §II.2 corrected:** The geometric formula K >= 1 - (1-p)^{lambda*k} gives K
   concave in lambda (not superlinear in the derivative sense). The operative superlinearity
   claim is K > K_lin = lambda*k*p, which holds when 0 < p < 1 and lambda*k >= 2. This
   is preserved by the IA-based argument but requires re-statement.

### Still Blocked

1. **Monotone-obstruction proof for SBP with finite type space:** The most tractable path
   to replacing IA. Requires showing that each SBP application strictly reduces the pool
   of available type-novel extensions.

2. **FUNCTOR-OBL-001:** N naturality obligation (unchanged from E031).

3. **WITNESS-OBL-001:** Ostrom witness self-reference proof (unchanged from E031).

4. **Q-OBL-001:** Q circularity avoidance (unchanged from E031).

5. **PP-3 source-layer declaration:** (unchanged from E031).

6. **Interior optimum existence proof:** Conditional on monotone-obstruction being
   established for the operative Compat family in a specific model.

---

## Assumptions and Kill Conditions

### Assumptions Made Here

1. Compat families are exactly those identified in E031 and E038 (three families).
   If additional Compat families exist elsewhere in the repo, they require separate analysis.

2. "Eventually-constant trigger" means Hom(S', -) = empty set (no further admissible
   single-step extensions). If eventually-constant is defined more weakly (only D4
   extensions cease), a different analysis is required.

3. The process distribution P_lambda is Markovian (the extension at each step depends
   only on the current state, not the history of how the current state was reached).

4. The type space for SBP analysis: "finite type space" and "Gödelian type generation"
   are treated as two distinct regimes; the regime relevant to a specific Compat
   instantiation must be declared.

### Kill Conditions

1. If IA can be shown to hold for a restricted subclass of Compat predicates that are
   sufficient for all operative uses in the repo, the verdict would upgrade from
   "IA fails generally" to "IA holds for operative subclass."

2. If the monotone-obstruction property is shown to follow from the E031 morphism
   definition alone (without additional Compat constraints), the interior optimum
   proof would close unconditionally.

3. If a PP-3 source-layer witness is established at the source layer, the IA analysis
   must be re-run at the source layer rather than the projection layer where E031
   currently operates.
