---
artifact_type: exploration
status: active
exploration_id: E031
date: 2026-06-22
topic: nck_category_morphism_definitions
claim_refs:
  - TI-C019
  - TI-C020
relates_to:
  - E028 (anti-collapse hypothesis, trajectory-level non-eventually-constant condition)
  - E029 (bounded-accessibility source/projection model, PP-3)
  - E030 (five-run issuance rate intake)
  - E034 (lambda*(s) absorber test)
  - E039 (IA verification for K superlinearity — IA fails for all repo Compat families)
  - E040 (Ostrom Redistribution Theorem — WITNESS-OBL-001 conditionally closed 2026-06-22)
  - RUN-0025 (category-first correction, outstanding formal work)
blocking_task_addressed: Ext_S category structure specification (RUN-0025 outstanding)
cross_repo:
  - time-as-finality (coherent section functor, F: States(Ext_S) -> FinSets)
  - ai-native-epistemic-systems (Shannon rate-distortion reading of N, C, K)
governance_note: >
  This exploration fixes the Ext_S category structure that RUN-0025 required and uses
  it to provide formal definitions of N, C, K. These definitions are candidates, not
  admitted claims. Each carries a blocking condition and a kill condition. The Ostrom
  interaction_witness result from E030 Run 5 is formalized here as the schema-boundary
  proposal right morphism class.
---

# E031: N, C, K at the Category-Morphism Level — Formal Definitions for Ext_S

## Purpose

E030 established that lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]
is absorbed by generic optimal control **unless** N, C, K are defined as TI-native objects
over the category-morphism structure of Ext_S. E034 confirmed this independently.

E028 and E029 showed that the non-eventually-constant trajectory condition and the
source/projection distinction are the crux formal objects. RUN-0025 directed that the
Ext_S category structure must be specified first: objects, morphisms, composition, identity.

This exploration does that specification and then attempts the N, C, K definitions.

---

## Part I: Ext_S Category Structure (Fixing RUN-0025 Outstanding Work)

### I.1 Objects

Let S be a **typed source constraint state**:

```text
S = (T_S, A_S)
```

where:
- T_S is a finite set of typed constraint labels (the schema at this state)
- A_S : P(T_S) -> {0, 1} is an admissibility predicate on subsets of T_S

A_S must satisfy:
- (A1) A_S(empty set) = 1 (the empty subset is always admissible)
- (A2) If A_S(X) = 1 and Y subset X, then A_S(Y) = 1 (downward closure: admissible
  subsets remain admissible after removing constraints)

The objects of Ext_S are all such states S. Notation: Ob(Ext_S).

**Cardinality note:** Ob(Ext_S) is in general infinite, as new typed constraint labels
can always be introduced. A finite restriction to states reachable from a given initial
state S_0 is permitted for local analysis.

### I.2 Morphisms

A morphism e: S -> S' in Ext_S is an **admissible extension** satisfying:

```text
e = (S, S', delta_e)
```

where:
- T_{S'} = T_S union {c_e} for a new constraint label c_e not in T_S
  (each morphism adds exactly one new typed constraint; multi-step additions compose)
- A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND the compatibility condition
  Compat(c_e, X \ {c_e}, S) holds
- Compat(c_e, X, S) is a typed compatibility predicate for the new constraint c_e
  with respect to existing constraint subset X in state S

**D4 connection:** A morphism e: S -> S' is a **D4 morphism** (type-novel extension)
when c_e carries a type not present in T_S. Formally: type(c_e) not in {type(c) : c in T_S}.
Non-D4 morphisms (refinements within existing type schema) are permitted but distinguished.

**PP-3 note:** Whether D4 morphisms at the projection layer correspond to genuine source-layer
morphisms remains the PP-3 open question. These definitions apply at whatever layer is being
modeled; the layer must be declared.

**Compat covariance constraint (E049, 2026-06-22):** Compat instantiations must be
schema-relabeling-covariant: for any bijection r on type names,
Compat(r(c_e), r(X), r(S)) = Compat(c_e, X, S). This ensures the admissibility predicate
is sensitive to type STRUCTURE, not type NAMES (distortion-style, not torsion-style).
The specific instantiations defined in this document — the SBP incompatibility guard (§III.1)
and the RecCost check (§II.3) — are both schema-relabeling-covariant, as verified formally
by E049 (GAUGE-COV-OBL-001).

### I.3 Composition

For morphisms e1: S -> S' and e2: S' -> S'':

```text
e2 ∘ e1 : S -> S''
```

is the composite extension with:
- T_{S''} = T_{S'} union {c_{e2}} = T_S union {c_{e1}} union {c_{e2}}
- Admissibility of S'' determined by applying A_{S''} to subsets of T_{S''}
- The compatibility predicates compose: Compat(c_{e2}, X \ {c_{e2}}, S') uses the
  admissibility structure of S', which was produced by e1

**Associativity:** (e3 ∘ e2) ∘ e1 = e3 ∘ (e2 ∘ e1) holds because both sides produce
the same typed constraint set T_{S'''} and the same admissibility structure over it.
The order in which constraints were added matters for the sequence of compatibility checks
but not for the final admissibility predicate on the resulting state.

**Formal obligation (open):** A rigorous proof that admissibility predicates in the
composed state are independent of the order of constraint addition requires that Compat
be commutative: Compat(c2, X union {c1}, S) = Compat(c1, X union {c2}, S) for
overlapping subsets. This is a constraint on the admissibility predicate family, not
guaranteed by the definition alone. Note: this commutativity condition is required for
commutativity of composition (g ∘ f = f ∘ g), NOT for associativity.
**ASSOC-OBL-001 CLOSED by E038** (2026-06-22): the associativity proof is unconditional
within the E031 morphism definition — no Compat commutativity constraint is needed.
The commutativity condition here is preserved as a named property (Compat-Comm) distinct
from the now-closed associativity obligation.

### I.4 Identity

For each state S, the identity morphism id_S: S -> S is:

```text
id_S = (S, S, null)
```

No new constraint is added. T_S is unchanged. A_S is unchanged.

This is a degenerate extension: formally required for categorical identity laws but
carries no D4 content. An OnlineSchemaSys in the non-eventually-constant regime
must see infinitely many non-identity morphisms; identity morphisms witness schema fixation.

### I.5 Summary of Category Structure

```text
Ext_S = (
  Ob(Ext_S),              -- typed source constraint states (T_S, A_S)
  Hom(S, S'),             -- admissible extensions e: S -> S'
  composition,            -- e2 ∘ e1 as defined above (ASSOC-OBL-001 CLOSED, see E038)
  id_S                    -- empty extension at each S
)
```

Key functor declared here but not fully developed:

```text
Target: Ext_S -> Meas
```

Target assigns to each state S a measurable space over T_S (constraint labels with
sigma-algebra induced by the admissibility predicate). To each morphism e: S -> S',
Target(e) is the measurable map extending the sigma-algebra by the new constraint label.

---

## Part II: Formal Definitions of N, C, K

### II.1 N(lambda, S) — Morphism-Density Rate (Novelty Functor)

**Informal target:** N should measure the rate at which new type-novel morphisms (D4
morphisms) are generated in Ext_S at issuance rate lambda, given current state S.

**Definition:**

```text
N(lambda, S) = |D4-Hom_lambda(S)| / |Hom_lambda(S)|
```

where:
- Hom_lambda(S) = {e in Hom(S, -) : e is reachable from S in one step at rate lambda}
  This is the set of morphisms departing S that are generated with positive probability
  at issuance rate lambda. At lambda = 0, this set is {id_S}. As lambda increases,
  more extensions become reachable per unit time.
- D4-Hom_lambda(S) = {e in Hom_lambda(S) : type(c_e) not in {type(c) : c in T_S}}
  The subset carrying genuinely type-novel new constraints (D4 predicate satisfied).
- |.| denotes cardinality (or, for continuous extension spaces, a density measure
  that must be specified; the discrete case is the primary formal target).

**Functor status:** N is not yet a natural transformation over Ext_S in the strict sense.
It is a function Ob(Ext_S) x R_+ -> [0, 1]. Making it a natural transformation requires
specifying how N transforms under morphisms in Ext_S: for e: S -> S', does N(lambda, S')
relate to N(lambda, S) in a natural way? This is FUNCTOR-OBL-001 (N naturality obligation).

**Concavity in lambda:** N is concave in lambda under the assumption that the space of
type-novel constraints available to extend S is finite and diminishing returns set in as
lambda increases (because each new extension of type t removes t from the available pool
of novel types). Formally:

```text
d^2 N / d(lambda)^2 < 0 whenever D4-Hom_lambda(S) is nonempty
```

This is the key claim needed for an interior optimum to exist. It holds when the D4-Hom
space thins as lambda grows (more extensions generated per step, but the marginal
extension is less likely to carry a genuinely novel type). Concavity fails if novel types
are generated endogenously as S grows — this is the Gödelian mechanism from E028, which
can produce sustained novelty. If it applies, N may remain concave globally but with
a higher asymptote.

**Falsifiability condition:** N fails to be concave in lambda if there exists a state S
and a threshold lambda_0 such that for lambda > lambda_0, the proportion of D4 morphisms
increases rather than decreases. This would happen if new types beget new types (Gödelian
self-reference). Testing this requires specifying a concrete Compat predicate family.

**PP-3 note:** N as defined here is a projection-layer quantity unless the Hom_lambda(S)
space is specified at the source layer. N becomes a source-side quantity only when
lambda is the source-layer extension rate and S is the source-layer state.

### II.2 K(lambda, S) — Trajectory-Level Collapse Probability (Stability Functor)

**Informal target:** K should measure the probability that the trajectory (S_0, S_1, ...)
starting from S at issuance rate lambda becomes eventually-constant (schema fixed-point
collapse), connecting to E028's anti-collapse condition.

**Definition:**

```text
K(lambda, S) = Pr[ (S_n)_{n >= 0} is eventually-constant | S_0 = S, rate = lambda ]
```

where:
- (S_n) is the Markov chain on Ob(Ext_S) induced by the extension process at rate lambda
- "eventually-constant" means: there exists N* such that for all n > N*, S_n = S_{N*}
  (no further extensions are admitted; schema reaches a fixed point)
- The probability is over the stochastic choice of morphisms at each step,
  distributed according to some process distribution P_lambda on Hom(S_n, -)

**E028 connection:** The trajectory-level non-eventually-constant condition from E028 is:

```text
(∀N* ∈ N)(∃n > N*)[S_{n+1} strictly contains S_n]
```

K(lambda, S) < 1 iff this condition holds with positive probability from state S at rate
lambda. The anti-collapse regime is K < 1; schema fixed-point collapse is K = 1.

**Superlinearity in lambda (load-bearing condition):**

K is superlinear in lambda under the following independence assumption:

```text
Independence assumption (IA): Each new extension e: S_n -> S_{n+1} creates an
independent probability p_e > 0 that the extension will block further admissible
extensions from S_{n+1} (i.e., that Hom(S_{n+1}, -) becomes empty).
```

**IA STATUS (E039, 2026-06-22): IA does not hold for any Compat family in the repo.**
The admissibility predicate is path-dependent, making obstruction probabilities at
successive steps correlated through the schema state. K superlinearity requires the
monotone-obstruction property instead. See E039 §6-9 for the complete analysis.

Under IA, the probability that the trajectory collapses within k steps satisfies:

```text
K(lambda, S, horizon k) >= 1 - (1 - p)^{lambda * k}
```

where p = E[p_e] is the average per-extension obstruction probability.

As lambda increases:
- More extensions per unit time: lambda * k increases
- Each extension independently contributes obstruction risk
- K(lambda, S) grows faster than linearly in lambda (geometric / superlinear)

This is the key condition: **K is superlinear in lambda iff the independence assumption
holds and each extension creates independent obstruction risk**.

The condition fails (K becomes linear or sublinear) when extensions are positively
correlated with each other's obstruction properties — i.e., when the schema has a
"coherence zone" where many extensions reinforce each other rather than independently
risking collapse.

**Falsifiability condition:** K fails to be superlinear in lambda if there exists a
state S at which the compatibility predicate Compat produces correlated obstructions.
Specifically: if Compat(c2, X union {c1}, S) < Compat(c1, X union {c2}, S) holds
systematically (adding c1 first makes c2 less obstructing than the reverse), extensions
are positively correlated in obstruction-risk reduction, and K may grow sublinearly.

**Interior optimum existence (from superlinearity of K):**

If N is concave and K is superlinear in lambda, and C is convex in lambda (see below),
then the net functional N - C - K is strictly concave in lambda at S, guaranteeing an
interior maximum at some lambda*(S) > 0.

Proof sketch: N is concave (decreasing marginal returns), so dN/d(lambda) is decreasing.
K is superlinear, so dK/d(lambda) is increasing. C is convex, so dC/d(lambda) is increasing.
The first-order condition d/d(lambda)[N - C - K] = dN/d(lambda) - dC/d(lambda) - dK/d(lambda) = 0
has a solution at some lambda*(S) if dN/d(lambda) > dC/d(lambda) + dK/d(lambda) at lambda = 0
(issuance is worthwhile at low rates) and dN/d(lambda) < dC/d(lambda) + dK/d(lambda) at lambda
= lambda_max (issuance becomes too costly at high rates). Both conditions are plausible but
must be checked against specific instantiations. The interior optimum existence claim is
conditional on these first-order conditions being satisfied.

### II.3 C(lambda, S) — Reconciliation Cost (Coherence Functor)

**Informal target:** C should measure the expected cost of reconciling new extensions
(at rate lambda from state S) against the existing constraint set. This connects to
AC-8 quorum update cost from E028.

**Definition:**

```text
C(lambda, S) = lambda * E_{e ~ P_lambda}[ RecCost(e, S) ]
```

where:
- lambda is the extension rate (number of new extensions attempted per unit time)
- E_{e ~ P_lambda} is expectation over extensions drawn from the rate-lambda process
- RecCost(e, S) = |{c in T_S : Compat(c_e, {c}, S) requires checking}| / |T_S|
  is the fraction of existing constraints that must be checked for compatibility with
  the new constraint c_e introduced by extension e

**Interpretation:** Each new extension must be checked against all existing constraints.
The reconciliation cost grows because:
1. Each new extension adds lambda extensions per unit time (linear in lambda)
2. Each extension must be checked against |T_S| existing constraints (growing with S)

**Convexity in lambda:** C is linear in lambda by definition above (holding S and the
distribution P_lambda fixed). To make C strictly convex in lambda, one needs to model
that higher lambda creates congestion effects in reconciliation — each extension is slower
to reconcile because the queue of pending reconciliations is longer.

Adding a queue-congestion term:

```text
C(lambda, S) = lambda * E[RecCost(e, S)] + beta * lambda^2 * E[RecCost(e, S)]
```

where beta > 0 is the congestion coefficient. This makes C strictly convex in lambda.

**AC-8 quorum cost connection:** In E028's multi-observer setting, RecCost(e, S) must
also include the cost of propagating the extension e through the quorum until a threshold
of observers records it. This adds a communication-cost term:

```text
C_AC8(lambda, S) = C(lambda, S) + lambda * QuorumCost(S, k)
```

where QuorumCost(S, k) is the cost of propagating a schema extension to k-of-n observers
(O(k * log n) in typical quorum protocols). QuorumCost grows with |T_S| because larger
schemas require more quorum rounds to reconcile incompatible proposals.

**Falsifiability condition:** C fails to be convex in lambda if the reconciliation
process has decreasing marginal cost at high lambda — i.e., if batch reconciliation
makes each additional extension cheaper than the last. This would occur if compatible
extensions can be reconciled in bulk without per-constraint checking. The convexity
claim requires that extensions must be individually checked against all existing constraints.

---

## Part III: The Ostrom Interaction Witness and Schema-Boundary Proposal Rights

E030 Run 5 identified the schema-boundary proposal right as the strongest current PP-3
interaction_witness candidate. This section formalizes it in the Ext_S category.

### III.1 Schema-Boundary Proposal Right as Morphism Class

**Definition:** A morphism e: S -> S' is a **schema-boundary proposal** (SBP morphism) iff:
- type(c_e) not in {type(c) : c in T_S}  (D4 condition: genuinely novel type)
- For all morphisms f: S -> S'' in Hom(S, -) with S'' != S', the constraint c_{f}
  and c_e are **type-incompatible**: Compat(c_e, T_{S''}, S) = 0 AND
  Compat(c_f, T_{S'}, S') = 0
  (the two extensions cannot be composed into a common successor state)

Informally: an SBP morphism introduces a constraint whose type is genuinely novel AND
which is incompatible with the types introduced by alternative extensions from S.
This is the formal expression of "incompatible proposal" — not just a new type but a
type that forks the schema space.

**The Ostrom redistribution condition:** A multi-observer AC-8 system satisfies the
Ostrom redistribution condition iff:

```text
For each observer O_i and each state S, O_i retains the capacity to submit SBP morphisms
from S that reach quorum processing (i.e., are evaluated by the shared admissibility
predicate over the quorum, not unilaterally rejected before quorum).
```

### III.2 The AC-8 Redistribution Witness Theorem (Candidate)

**Claim candidate (from E030 Run 5, formalized here):**

```text
In a multi-observer Ext_S system satisfying NAA and the E028 quorum legitimacy condition:
if all observers retain schema-boundary proposal rights (capacity to submit SBP morphisms
to quorum), then the shared schema trajectory (S_0, S_1, ...) cannot be reproduced by
a fixed source Mu_infty plus widening apertures.

Reason: any fixed Mu_infty would have to pre-commit all possible type-incompatible
SBP morphisms. But the incompatibility of SBP morphisms is defined relative to the
current shared schema S_n, which itself evolved via prior SBP proposals. The self-
referential dependency blocks the fixed-Mu_infty construction:
- Mu_infty must contain all SBP morphisms from all future S_n
- But future S_n depends on which SBP morphisms were accepted by quorum
- Which SBP morphisms are accepted depends on Compat over the shared schema
- Which is itself produced by prior SBP acceptances
- Therefore Mu_infty must pre-determine all quorum outcomes — but quorum outcomes
  are multi-observer coordination events that cannot be pre-determined without
  specifying all observer states, which is the full OnlineSchemaSys trajectory
```

**Status:** candidate interaction_witness for PP-3 (from E029's five witness types).
Requires proving that the self-referential dependency above is not a circular argument.
Specifically: the self-referential dependency blocks the fixed-Mu_infty construction
only if incompatibility is genuinely schema-relative (not pre-computable from initial
conditions). This is WITNESS-OBL-001: Ostrom witness self-reference proof obligation.

### III.3 The Q-Grounding via Quorum-Validity

RUN-0028 required a morphism-level invariant Q: Mor(ExtCat) -> ([0, infinity), +).
E030 Run 5 proposed quorum-validity as Q.

**Candidate Q definition:**

```text
Q(e) = quorum-validity weight of morphism e
     = (number of observers that would accept e as a valid schema extension
        given the current shared admissibility predicate) / (total observer count)
```

Q(e) in [0, 1] by definition. For Q to map to ([0, infinity), +), use -log Q(e), the
information-theoretic surprise of acceptance. Then Q is additive under composition
(independent acceptance events multiply: Q(e2 ∘ e1) = Q(e2) * Q(e1), so
-log Q(e2 ∘ e1) = -log Q(e2) + (-log Q(e1))).

**Blocking condition for Q:** Q requires a measure of "observers that would accept"
which presupposes a probability distribution over observer acceptance. This distribution
must be defined without circularity (acceptance depends on the shared admissibility
predicate, which is itself Q-weighted). This is Q-OBL-001: Q grounding circularity
avoidance.

---

## Part IV: Cross-Repo Translation Layer

The definitions in Parts I-III are the primary formal home for N, C, K. The cross-repo
translation (TaF and IEAH readings) is developed in E032. Compact note here:

**TaF reading:** S = a typed source constraint state, S' = extended state, e: S -> S' in
Ext_S. The coherent section functor F: States(Ext_S) -> FinSets (TaF's Run 3 of the
five-run pass) assigns to S the set of globally coherent sections — globally admissible
combinations of local extensions. Then:
- N = d|F(S)|/dt = growth rate of globally coherent sections (which is a special case
  of D4-Hom_lambda(S): a new extension generates a globally coherent section iff it
  does not create a PO1 obstruction in the TaF claim ledger)
- K = p * lambda * |F(S)| when each new extension independently obstructs with
  probability p (TaF five-run pass Run 4's resource theory reading)
- C = cost of extending global sections to include the new constraint

**IEAH reading:** S = epistemic consensus state, e: S -> S' in Ext_S is a new epistemic
evaluation. Then N = mutual information gain, C = integration distortion, K = validity
collapse risk. Shannon rate-distortion theorem applies (E007 Run 5) when N is concave
and C is convex. Full treatment in E032.

---

## Part V: What Was Resolved and What Remains Blocked

### Resolved by This Exploration

1. **Ext_S category structure specified** (objects, morphisms, composition, identity).
   RUN-0025 outstanding work: addressed. ASSOC-OBL-001 CLOSED by E038 (2026-06-22).

2. **N formally defined** as D4-morphism density rate, concave in lambda under
   diminishing-returns assumption, TI-native (not available in standard optimal control
   state spaces because it references morphism type-novelty in Ext_S).

3. **K formally defined** as trajectory-level eventually-constant probability, superlinear
   in lambda under independence assumption IA, TI-native (references the non-eventually-
   constant trajectory condition from E028).

4. **C formally defined** as reconciliation cost per step, convex in lambda under
   congestion assumption, with AC-8 quorum cost extension.

5. **Interior optimum existence condition stated:** lambda*(S) is a well-defined interior
   optimum iff N is concave AND K is superlinear AND C is convex in lambda, and the
   first-order conditions are satisfied at both ends of the admissible lambda range.
   This is a conditional claim, not a theorem until the conditions are verified for
   specific Compat instantiations.

6. **Ostrom interaction_witness formalized** as SBP morphism class and AC-8 redistribution
   condition. Theorem candidate stated. Proof obligation WITNESS-OBL-001 named.
   **E040 UPDATE (2026-06-22):** Ostrom Redistribution Theorem proved under H1-H4;
   WITNESS-OBL-001 conditionally closed. SBP-IND verification is the remaining open item.

7. **Q grounded** in quorum-validity with information-theoretic structure (-log Q additive
   under composition). Circularity avoidance obligation Q-OBL-001 named.

### Still Blocked

1. **ASSOC-OBL-001:** ~~Proof that composition is associative for specific Compat
   instantiations. Required before Ext_S is a genuine category.~~
   **CLOSED by E038** (2026-06-22). Composition is associative unconditionally within
   the E031 morphism definition. The commutativity condition noted in §I.3 is not
   required for associativity; it would be needed for commutativity of composition
   (g ∘ f = f ∘ g), which is a distinct property. See E038 for the full proof.

2. **FUNCTOR-OBL-001:** N naturality obligation. N is not yet a natural transformation;
   it is a pointwise function. Naturality requires showing how N transforms under
   morphisms in Ext_S.

3. **IA verification:** ~~The independence assumption for K superlinearity must be
   checked against specific Compat families. If Compat produces correlated obstructions,
   K may not be superlinear, which would eliminate the interior optimum guarantee.~~
   **PARTIALLY ADDRESSED by E039** (2026-06-22): IA does not hold for any Compat family
   in the repo. The failure is structural: the admissibility predicate is path-dependent,
   making obstruction probabilities at successive steps correlated through the shared schema
   state. K superlinearity is therefore not guaranteed by IA. K remains superlinear iff
   the Compat family is monotone-obstructive (obstruction probability non-decreasing along
   the trajectory). This holds for SBP Compat with a finite type space (type-pool
   depletion) but is NOT established for the general case or for the Gödelian type-
   generation regime. The interior optimum existence proof is conditional on
   monotone-obstruction being demonstrated for the operative Compat instantiation.
   See E039 for the complete analysis and the replacement condition for IA.

4. **WITNESS-OBL-001:** ~~Ostrom witness self-reference proof. The argument that SBP
   incompatibility blocks fixed-Mu_infty requires formal proof of the self-referential
   dependency.~~
   **CONDITIONALLY CLOSED by E040** (2026-06-22): the Ostrom Redistribution Theorem
   is proved under NAA + E028 quorum legitimacy + Ostrom redistribution condition +
   SBP-IND. The structural mechanism is formally identified. Full closure requires
   SBP-IND verification for at least one concrete Compat predicate family, and the
   infinite-trajectory extension. See E040 for proof and open conditions.

5. **Q-OBL-001:** Q circularity avoidance. The quorum-validity weight must be definable
   without circular reference to the shared admissibility predicate it is meant to measure.

6. **PP-3 source-layer declaration:** All of N, C, K are defined in a layer-neutral way.
   For the definitions to constitute a PP-3 positive witness, the source layer must be
   independently specified and the definitions must be shown to apply at that layer.
   Until PP-3 is resolved, these definitions apply to whichever layer (source or
   projection) the Ext_S category is being used to model.

7. **LAYER-OBL-001 (E046, 2026-06-22):** Source-layer declaration for the AC-8 coordination
   process. The Ostrom Redistribution Theorem (E040) proves global-coordination-structure
   irreducibility — the trajectory cannot be factored through any pre-committed computable
   source. However, this does not distinguish between:
   (a) Quorum navigating a fixed non-computable source (Gödelian pre-existing structure)
   (b) Quorum collectively constructing new source constraints (genuine source extension)
   LAYER-OBL-001 requires: specify conditions under which interpretation (b) is correct
   and (a) is excluded.

   **Sub-requirement 1 UPDATE (E049, 2026-06-22): CONDITIONALLY CLOSED.**
   The distortion residue test (E049) established that the admissibility predicate evolution
   A_{S_n} -> A_{S_{n+1}} carries non-zero, gauge-equivariant content not explainable by
   any type-relabeling of A_{S_n}. This is the formal signature of Ehresmannian (source-
   layer) content. Sub-requirement 1 (specify what it means for quorum coordination to
   change the SOURCE admissibility predicate) is conditionally satisfied by the distortion
   residue being non-zero and gauge-equivariant.

   **Sub-requirements 2 and 3 remain OPEN:**
   Sub-req 2: causal attribution of DR to source layer vs. coordination dynamics.
   Sub-req 3: Gödelian SBP space as genuine extension vs. Platonist discovery (= D-FORK).
   Until sub-reqs 2 and 3 are discharged, the ORT's PP-3 interpretation remains
   provisional. See E046 and E049 for the full analysis.

---

## Governance Constraints

1. Do not admit lambda*(s) as a TI claim until IA verification and
   the first-order condition check are completed.

2. Do not import these definitions as source-side primitives without a PP-3 source
   witness. The definitions are layer-neutral; layer assignment is the remaining gap.

3. The Ostrom redistribution condition is a candidate interaction_witness only.
   WITNESS-OBL-001 is CONDITIONALLY CLOSED (E040, 2026-06-22): the Ostrom Redistribution
   Theorem is proved under NAA + E028 quorum legitimacy + Ostrom redistribution condition
   + SBP-IND. Full closure requires SBP-IND verification for a concrete Compat family.

4. N, C, K as defined here escape absorption by generic optimal control because they
   reference morphism type-novelty (N), trajectory-level schema fixation probability (K),
   and quorum-reconciliation cost structure (C) — all of which are specific to the Ext_S
   categorical setting and not available in generic state-space optimization.
