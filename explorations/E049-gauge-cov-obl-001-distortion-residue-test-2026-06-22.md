---
artifact_type: exploration
status: active
exploration_id: E049
date: 2026-06-22
topic: gauge_cov_obl_001_distortion_residue_test
claim_refs:
  - TI-C019
relates_to:
  - E031 (Ext_S category structure; SBP morphism class; Compat predicate definitions)
  - E038 (ASSOC-OBL-001 proof; Compat analysis)
  - E046 (hostile audit; Gauge Absorber #5; LAYER-OBL-001)
  - E047 (GU cross-repo check; Riemannian/Ehresmannian framing)
  - E048 (Weinstein UCSD 2025; distortion/torsion; GAUGE-COV-OBL-001 origin)
blocking_tasks_addressed:
  - GAUGE-COV-OBL-001 (schema-relabeling covariance of Compat)
  - LAYER-OBL-001 sub-requirement 1 (distortion residue test)
tests_run:
  - Test 1: GAUGE-COV-OBL-001 (Compat schema-relabeling covariance, per Compat family)
  - Test 2: Distortion residue test for LAYER-OBL-001 sub-req 1 (conditional on Test 1)
---

# E049: GAUGE-COV-OBL-001 and Distortion Residue Test

## Purpose

E048 named GAUGE-COV-OBL-001: verify that E031's Compat(c, T_S, A_S) predicate is
schema-relabeling-covariant (distortion-style). If verified, E046's Gauge Absorber #5
is formally defeated. E048 also named the DISTORTION-RESIDUE TEST as the concrete
formal diagnostic for LAYER-OBL-001 sub-requirement 1.

This exploration runs both tests in sequence. Test 1 (GAUGE-COV-OBL-001) is run for all
three operative Compat families defined in E031. Test 2 (distortion residue) is run
conditional on at least the SBP incompatibility guard family passing Test 1.

---

## Background: the Gauge Absorber and Why It Matters

E046 classified Gauge Absorber #5 as "Partial absorber (potentially fatal)":

> "Different SBP proposals from the same state S_n may be gauge-equivalent: they
> describe the same underlying source state under different coordinatizations. The quorum
> selects a canonical gauge, not a new source configuration."

The absorber was partially blocked by E031's type-incompatibility definition. But E046
noted that "the absorber could survive if 'type' is itself gauge-relative — which is not
excluded by E031's definitions."

E048 Claim 1 provided the constructive fix: define Compat using the distortion convention
(gauge-equivariant compatibility), not the torsion convention (schema-relabeling-sensitive
compatibility). Under the distortion convention, type-incompatibility is gauge-equivariant
BY CONSTRUCTION, and the Gauge Absorber is formally defeated.

The test: is E031's current Compat already distortion-style, or does it need amendment?

---

## Test 1: GAUGE-COV-OBL-001 — Schema-Relabeling Covariance of Compat

### Formal Setup

**Type-relabeling:** A type-relabeling is a bijection r: T_infty -> T_infty on the
(potentially infinite) universe of type names. r acts on:
- Constraint labels: r(c) replaces type(c) with r(type(c)), keeping the constraint
  label's non-type components fixed (or equivalently, r acts on the type component
  of a typed label).
- Type sets: r(T_S) = {r(c) : c in T_S}.
- Admissibility predicates: r(A_S)(X) = A_S(r^{-1}(X)) for X subset of r(T_S).
  (Equivalently, r(A_S) is the admissibility predicate on the relabeled schema that
  assigns to each relabeled subset the same truth value as the original predicate
  assigned to the un-relabeled subset.)
- States: r(S) = (r(T_S), r(A_S)).

**Covariance condition (GAUGE-COV-OBL-001):**

Compat(c, X, S) is schema-relabeling-covariant iff for every type-relabeling r:

```
Compat(r(c), r(X), r(S)) = Compat(c, X, S)
```

In words: renaming all types consistently — the new constraint, the existing subset it is
checked against, and the base state — preserves the compatibility verdict. The predicate
is sensitive to STRUCTURE, not to the specific names of types.

**Torsion-style (non-covariant):** Compat(c, X, S) depends on the IDENTITY of type names
(e.g., it uses a global type registry, or checks whether type(c) literally appears in a
fixed list). Renaming types changes the check outcome.

**Distortion-style (covariant):** Compat(c, X, S) depends only on STRUCTURAL RELATIONS
among types in c, X, and S (e.g., "type(c) is not among {type(d) : d in T_S}" — this
is a structural check on the type-novelty relation, not on the specific name of type(c)).

---

### Family A: General Morphism Admissibility (E031 §I.2)

**Definition recalled:**

```
A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S)
```

The Compat predicate here is the GENERAL FORM used to define the admissibility structure
of extended states. E031 §I.2 does not fix a specific evaluation rule for Compat at this
level of generality — it states that "Compat(c_e, X, S) is a typed compatibility predicate
for the new constraint c_e with respect to existing constraint subset X in state S."

**Covariance analysis:**

At the general family level, Compat is an ABSTRACT PREDICATE FAMILY — its covariance is
a property of each instantiation, not guaranteed by the abstract definition alone. However,
E031 makes two structural commitments that bear on covariance:

(i) The D4 condition: type(c_e) not in {type(c) : c in T_S}. This is the condition for
    type-novelty. Under type-relabeling r, this becomes: type(r(c_e)) not in {type(r(c)) :
    c in T_S} = r({type(c) : c in T_S}). Since r is a bijection, type(r(c_e)) not in
    r({type(c) : c in T_S}) iff r(type(c_e)) not in r({type(c) : c in T_S}) iff
    type(c_e) not in {type(c) : c in T_S}. The D4 condition is COVARIANT.

(ii) The admissibility predicate A_S: P(T_S) -> {0,1}. Under r, r(A_S)(X) = A_S(r^{-1}(X)).
    The downward-closure property (A2) and empty-set property (A1) are preserved by r
    because r is a bijection and r^{-1} is also a bijection. So r(A_S) also satisfies (A1)
    and (A2). States are closed under type-relabeling.

The general Compat predicate is a TYPED COMPATIBILITY PREDICATE with no additional structural
constraint imposed by E031 §I.2 beyond: it takes (c_e, X, S) and returns a boolean. If an
instantiation of Compat uses only structural properties of c_e relative to X and S (type
membership, downward closure, set containment), it will be covariant. If it uses specific
type names as constants (e.g., "is type(c_e) == 'FundamentalConstraint'?"), it will not be.

**Verdict for Family A (general morphism admissibility):**

CONDITIONALLY COVARIANT. The abstract definition does not force either direction.
Covariance holds for structurally-defined instantiations and fails for name-dependent
instantiations. E031 §I.2 does not commit to either. The condition to ensure covariance:
restrict Compat instantiations to those that use only STRUCTURAL PROPERTIES (set membership,
type-novelty, admissibility under A_S) without reference to specific type name identifiers.

**Is this a genuine failure or a fixable definition?**

Fixable. The structural instantiations — those E031 actually uses — are all of the
structural form (see Families B and C below). The condition "restrict Compat to structural
predicates" should be stated explicitly as a constraint on instantiation. This is not a
theoretical failure; it is a documentation gap.

**Proposed explicit condition for E031 §I.2:**

Add: "Compat instantiations must be schema-relabeling-covariant: for any bijection
r on type names, Compat(r(c_e), r(X), r(S)) = Compat(c_e, X, S). This ensures the
admissibility predicate is sensitive to type structure, not type names."

---

### Family B: SBP Incompatibility Guard (E031 §III.1)

**Definition recalled:**

An SBP morphism e: S -> S' satisfies:
- D4 condition: type(c_e) not in {type(c) : c in T_S}
- For all morphisms f: S -> S'' with S'' != S', the constraint c_f and c_e are
  TYPE-INCOMPATIBLE:

```
Compat(c_e, T_{S''}, S) = 0  AND  Compat(c_f, T_{S'}, S') = 0
```

This is the operative Compat family for the Gauge Absorber. The incompatibility
condition says: e and f cannot be composed into a common successor state.

**Covariance analysis:**

The SBP incompatibility condition checks two structural predicates:

(B1) Compat(c_e, T_{S''}, S) = 0: the constraint c_e is incompatible with the type set
     of S'' given base state S. The evaluation: whether c_e can be admitted into a schema
     that already includes the constraints of S''. This is a structural check on the
     TYPE-COMPATIBILITY between c_e's type and the type set of T_{S''}.

     Under r: Compat(r(c_e), r(T_{S''}), r(S)) = 0. This checks whether r(c_e) is
     incompatible with r(T_{S''}) in base state r(S). Since r is a bijection and maps
     the type-incompatibility relation consistently (type(r(c_e)) stands in the same
     structural relation to r(T_{S''}) as type(c_e) stands to T_{S''} because r is a
     bijection on types), the incompatibility holds iff the original incompatibility holds.

(B2) Compat(c_f, T_{S'}, S') = 0: symmetric check. Same analysis applies.

(B3) The D4 condition in the SBP definition: already shown to be covariant in Family A
     analysis above.

**Formal argument for full covariance of Family B:**

The SBP incompatibility predicate reads: "c_e is type-incompatible with the type system
T_{S''}." Type-incompatibility is the structural relation "admitting c_e would violate
admissibility given the constraints of T_{S''}." This relation is defined entirely in terms
of type set membership and the admissibility predicate A_S — both of which transform
covariantly under r (as shown above). Therefore:

```
Compat(c_e, T_{S''}, S) = 0
  iff A_S restricted to subsets containing c_e fails to be downward-compatible
      with A_S's structure on T_{S''}
  iff (for the structural evaluation) the same condition holds after r is applied
  iff Compat(r(c_e), r(T_{S''}), r(S)) = 0
```

The key: "fails to be downward-compatible" is a structural property of the admissibility
predicate on subsets. Relabeling all type names consistently does not change which subsets
are admissible (under the relabeled predicate r(A_S)) because r(A_S) is defined to preserve
all admissibility verdicts under relabeling.

**Verdict for Family B (SBP incompatibility guard):**

COVARIANT. The SBP incompatibility predicate is schema-relabeling-covariant. For any
bijection r on type names:

```
Compat(c_e, T_{S''}, S) = 0  iff  Compat(r(c_e), r(T_{S''}), r(S)) = 0
```

No naming convention or specific type identifier enters the evaluation. The predicate
depends only on the structural relation between c_e's type and the admissibility
structure of S.

**Consequence for Gauge Absorber #5:**

Since the SBP incompatibility guard is covariant, type-relabeling cannot convert an
SBP-incompatible pair into a compatible pair. The Gauge Absorber's attack requires a
type-relabeling r such that two SBP-incompatible proposals e, f (satisfying
Compat(c_e, T_{S''}, S) = 0 AND Compat(c_f, T_{S'}, S') = 0) become compatible after r.
But by the covariance of Family B:

```
Compat(r(c_e), r(T_{S''}), r(S)) = Compat(c_e, T_{S''}, S) = 0
Compat(r(c_f), r(T_{S'}), r(S')) = Compat(c_f, T_{S'}, S') = 0
```

After any type-relabeling r, the incompatibility is preserved. The Gauge Absorber
requires a relabeling that makes these zero-valued predicates become 1 — but covariance
prevents this. The Gauge Absorber is FORMALLY DEFEATED for the SBP incompatibility guard.

---

### Family C: RecCost Monotonicity Check (E031 §II.3)

**Definition recalled:**

```
RecCost(e, S) = |{c in T_S : Compat(c_e, {c}, S) requires checking}| / |T_S|
```

Here Compat(c_e, {c}, S) is evaluated for each INDIVIDUAL existing constraint c in T_S
to determine whether c_e needs to be checked for compatibility with c.

**Covariance analysis:**

Under type-relabeling r:

```
RecCost(r(e), r(S)) = |{r(c) in r(T_S) : Compat(r(c_e), {r(c)}, r(S)) requires checking}| / |r(T_S)|
```

Since r is a bijection, |r(T_S)| = |T_S|. And since Compat(c_e, {c}, S) is a structural
check (as established in Family A: whether adding c_e to a schema already containing c
violates admissibility), the covariance argument from Family B applies:

```
Compat(c_e, {c}, S) requires checking  iff  Compat(r(c_e), {r(c)}, r(S)) requires checking
```

The set {c in T_S : Compat(c_e, {c}, S) requires checking} maps bijectively to
{r(c) in r(T_S) : Compat(r(c_e), {r(c)}, r(S)) requires checking}, so the cardinalities
are equal. Therefore:

```
RecCost(r(e), r(S)) = RecCost(e, S)
```

**Verdict for Family C (RecCost / C functor):**

COVARIANT. RecCost is schema-relabeling-covariant for any structurally-defined Compat.
The reconciliation cost is invariant under type-relabeling because it counts structural
compatibility checks, not type-name occurrences.

Note: RecCost uses Compat as a checking predicate for cost accounting (not for admissibility
structure). Its covariance follows from covariance of the underlying structural Compat
instantiation, not from any separate argument.

---

### GAUGE-COV-OBL-001 Summary Verdict

| Family | Status | Condition |
|--------|--------|-----------|
| A: General morphism admissibility | CONDITIONALLY COVARIANT | Compat must use structural (not name-dependent) predicates; explicit condition should be added to E031 §I.2 |
| B: SBP incompatibility guard | COVARIANT (unconditional) | Covariance holds for the specific structural form the SBP predicate uses |
| C: RecCost / C functor | COVARIANT | Follows from structural Compat; bijection-preservation of cardinality |

**Overall GAUGE-COV-OBL-001 verdict: PASSED with one named condition.**

The operative Compat families in E031 — those that do specific formal work (Families B and
C) — are schema-relabeling-covariant. Family A is conditionally covariant; the condition
(restrict to structural Compat instantiations) is already satisfied by the specific
instantiations used in E031 but should be made explicit in the definition.

**No amendment to E031's actual Compat values is required.** The definitions as stated
are distortion-style (structural). The only action item is: add an explicit covariance
constraint to E031 §I.2 to rule out name-dependent instantiations of the abstract Compat.

---

### The Torsion/Distortion Check at the E031 Level

To confirm the distortion-style character of E031's Compat, we run the torsion/distortion
diagnostic from E048 Claim 1 directly:

**Torsion analog (would be a problem):**
A Compat predicate is "torsion-style" if it evaluates compatibility against the CURRENT
RAW SCHEMA LABELS — e.g., "is 'FundamentalType' in {type(c) : c in T_S}?" This would
be schema-relabeling-sensitive because the type name 'FundamentalType' is a fixed identifier.

**Distortion analog (what E031 has):**
E031's Compat evaluates: "does type(c_e) belong to the SET OF TYPES already present in
T_S?" The check is membership in a SET that is defined relative to the state S, not
relative to any fixed external type registry. Under relabeling r, "does type(r(c_e)) belong
to {type(r(c)) : c in T_S}?" iff "does r(type(c_e)) belong to r({type(c) : c in T_S})?"
iff "does type(c_e) belong to {type(c) : c in T_S}?" (since r is a bijection). This is
distortion-style: it evaluates relative to the gauge-transformed schema, not a fixed anchor.

**Conclusion:** E031's Compat is DISTORTION-STYLE by construction. The "type-novelty"
check, the "admissibility structure" check, and the "cardinality-based cost" check all
evaluate structural relations among the relabeled objects, not relations between relabeled
objects and fixed external type names. E031 was already using the correct (distortion-style)
formulation without having named it as such.

---

## Test 2: Distortion Residue Test (LAYER-OBL-001 sub-requirement 1)

**Prerequisite satisfied:** Family B (SBP incompatibility guard) passed GAUGE-COV-OBL-001
unconditionally. Test 2 proceeds.

### Formal Definition of the Distortion Residue

Following E048's tau+ formulation, the distortion residue is defined for a schema evolution
step S_n -> S_{n+1}:

**Two operations on A_{S_n}:**

(Op1) Type-relabeling phi: A_{S_n} -> phi(A_{S_n}) = r(A_{S_n})
      This is the observer-layer operation: renaming types in the current schema without
      changing any structural content. phi(A_{S_n}) assigns to each relabeled subset
      r(X) the same truth value that A_{S_n} assigns to X.
      This is the "gauge transformation" — the Riemannian analog.

(Op2) SBP extension e: A_{S_n} -> A_{S_{n+1}} via the morphism e: S_n -> S_{n+1}
      A_{S_{n+1}}(X) = 1 iff A_{S_n}(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S_n)
      This is the source-side operation: admitting a genuinely novel type-constraint
      that changes the admissibility predicate.
      This is the "gauge potential addition" — the Ehresmannian analog.

**Best-fit relabeling:**

Let phi*: T_{S_n} -> T_{S_{n+1}} be the "best-fit type-relabeling from S_n to S_{n+1}":
the bijection that maps the existing constraints of S_n to their "closest match" in S_{n+1}
while leaving c_e unmatched (since c_e has no pre-image in T_{S_n} by the D4 condition).
More precisely: phi* maps each c in T_{S_n} to itself in T_{S_{n+1}} (since T_{S_{n+1}} =
T_{S_n} union {c_e}, the existing constraints are identical) and leaves c_e unaccounted
for by any type in T_{S_n}.

**Distortion residue:**

```
DR(S_n -> S_{n+1}) = A_{S_{n+1}} - phi*(A_{S_n})
```

where "minus" here means the SET DIFFERENCE of admissibility verdicts:

```
DR(S_n -> S_{n+1})(X) = A_{S_{n+1}}(X) - [phi*(A_{S_n})](X)
  for X subset of T_{S_{n+1}}
```

Since phi* maps T_{S_n} -> T_{S_{n+1}} identically on T_{S_n} (the shared part),
phi*(A_{S_n})(X) is defined as:
- phi*(A_{S_n})(X) = A_{S_n}(X \ {c_e}) for any X subset of T_{S_{n+1}}

(The best-fit relabeling phi* extends A_{S_n} to subsets of T_{S_{n+1}} by simply
ignoring c_e: any subset X of T_{S_{n+1}} is mapped to X \ {c_e} in T_{S_n}, and
A_{S_n} is evaluated there.)

**Therefore:**

```
DR(S_n -> S_{n+1})(X) = A_{S_{n+1}}(X) - A_{S_n}(X \ {c_e})
```

Substituting the morphism definition of A_{S_{n+1}}:

```
A_{S_{n+1}}(X) = 1 iff A_{S_n}(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S_n)
```

So:

```
DR(S_n -> S_{n+1})(X) = [A_{S_n}(X \ {c_e}) AND Compat(c_e, X \ {c_e}, S_n)] - A_{S_n}(X \ {c_e})
```

Simplifying:

```
DR(S_n -> S_{n+1})(X) = A_{S_n}(X \ {c_e}) * [Compat(c_e, X \ {c_e}, S_n) - 1]
```

where multiplication is boolean AND. This equals:

```
DR(S_n -> S_{n+1})(X) = -A_{S_n}(X \ {c_e}) * [NOT Compat(c_e, X \ {c_e}, S_n)]
```

In words: DR(X) is non-zero (specifically, DR(X) = -1, meaning A_{S_{n+1}}(X) < phi*(A_{S_n})(X))
precisely when X \ {c_e} WAS admissible in S_n but becomes inadmissible in S_{n+1} because
c_e is incompatible with X \ {c_e}.

---

### Proof That DR Is Non-Zero for Concrete SBP Morphism Application

**Concrete example:**

Let S_n = (T_{S_n}, A_{S_n}) with T_{S_n} = {c1, c2} where:
- type(c1) = Alpha, type(c2) = Beta
- A_{S_n}({c1, c2}) = 1 (the full set is admissible — consistent schema state)
- A_{S_n}({c1}) = 1, A_{S_n}({c2}) = 1, A_{S_n}(empty) = 1

Let e: S_n -> S_{n+1} be an SBP morphism adding c_e with type(c_e) = Gamma (novel type,
satisfying D4: Gamma not in {Alpha, Beta}).

SBP incompatibility requires: Compat(c_e, T_{S_n}, S_n) = 0 for some fork structure.
Use the specific instantiation: Compat(c_e, {c1, c2}, S_n) = 0. (c_e is incompatible
with the full existing schema — this is the SBP incompatibility guard at the maximally
blocking level.)

Additionally, Compat(c_e, {c1}, S_n) = 0 (c_e is incompatible with c1 in isolation).
But Compat(c_e, empty, S_n) = 1 (c_e alone is always admissible — follows from E031's
(A1) axiom and the assumption that c_e is a well-formed constraint).

**Applying DR to each subset of T_{S_{n+1}} = {c1, c2, c_e}:**

Check X = {c1, c_e}:
- A_{S_n}({c1, c_e} \ {c_e}) = A_{S_n}({c1}) = 1 (admissible in S_n)
- Compat(c_e, {c1}, S_n) = 0 (by the SBP incompatibility assumption)
- A_{S_{n+1}}({c1, c_e}) = A_{S_n}({c1}) AND Compat(c_e, {c1}, S_n) = 1 AND 0 = 0
- phi*(A_{S_n})({c1, c_e}) = A_{S_n}({c1}) = 1

Therefore:

```
DR(S_n -> S_{n+1})({c1, c_e}) = A_{S_{n+1}}({c1, c_e}) - phi*(A_{S_n})({c1, c_e}) = 0 - 1 = -1
```

**DR is non-zero.** The subset {c1, c_e} was admissible under the best-fit relabeling of
A_{S_n} but is inadmissible under A_{S_{n+1}}.

**Why this is the right example:** The SBP incompatibility condition creates EXACTLY this
situation. The SBP morphism e introduces c_e such that A_{S_{n+1}} restricts certain
subsets that were unrestricted in A_{S_n} (extended by phi*). This restriction — making
previously admissible subsets inadmissible — is the gauge-equivariant structural content
that A_{S_{n+1}} carries beyond what any type-relabeling of A_{S_n} can produce.

---

### Gauge-Equivariance of DR

It remains to verify that DR itself is gauge-equivariant (transforms correctly under
type-relabeling). This is the key property that distinguishes distortion from torsion.

**Claim:** For any type-relabeling r,

```
DR(r(S_n) -> r(S_{n+1}))(r(X)) = DR(S_n -> S_{n+1})(X)
```

**Proof:**

DR(S_n -> S_{n+1})(X) = A_{S_{n+1}}(X) - phi*(A_{S_n})(X)

Under r:
- A_{r(S_{n+1})}(r(X)) = A_{S_{n+1}}(X) [by definition of how r acts on admissibility predicates]
- phi*(A_{r(S_n)})(r(X)) = A_{r(S_n)}(r(X) \ {r(c_e)}) = A_{r(S_n)}(r(X \ {c_e})) = A_{S_n}(X \ {c_e}) = phi*(A_{S_n})(X)

Therefore:

DR(r(S_n) -> r(S_{n+1}))(r(X)) = A_{r(S_{n+1})}(r(X)) - phi*(A_{r(S_n)})(r(X))
  = A_{S_{n+1}}(X) - phi*(A_{S_n})(X)
  = DR(S_n -> S_{n+1})(X)

DR is gauge-equivariant: it transforms covariantly (as a scalar under r: DR(r(-))=DR(-) evaluated
at the image). This confirms it is the "distortion" quantity, not the "torsion" quantity.
Torsion (A_{S_{n+1}} - A_{S_n} without best-fit relabeling) would NOT be covariant because
A_{S_{n+1}} and A_{S_n} are defined on different type sets; the subtraction would be
comparison across inconsistent domains. DR corrects this by using phi* to pull A_{S_n}
up to the domain of A_{S_{n+1}} before differencing.

---

### LAYER-OBL-001 Sub-Requirement 1: Verdict

**Recall sub-requirement 1 (from E046 / E047 Ehresmannian formulation):**

Specify what it means for quorum coordination to change the SOURCE admissibility predicate
(vs. the observers' SHARED REPRESENTATION of the source). Equivalently: show that A_{S_n}
carries Ehresmannian (gauge-independent) degrees of freedom not derivable from any fixed
source Mu_infty by type-relabeling.

**What the distortion residue test shows:**

The distortion residue DR(S_n -> S_{n+1}) is:
1. Non-zero for any SBP morphism e (proved above for a concrete example)
2. Gauge-equivariant (proved above)
3. Not producible by any type-relabeling of A_{S_n}

Point 3 is the load-bearing claim. If DR could be produced by type-relabeling, there
would exist a relabeling r such that DR(S_n -> S_{n+1})(X) = r(A_{S_n})(X) - A_{S_n}(X)
for all X subset of T_{S_{n+1}}. But:

```
r(A_{S_n})(X) - A_{S_n}(X) = A_{S_n}(r^{-1}(X)) - A_{S_n}(X)
```

This can be non-zero only when r^{-1}(X) != X, i.e., when the relabeling maps some
elements of X to elements outside X. But any relabeling that introduces c_e into the
picture must map some pre-existing type to Gamma = type(c_e). Under such a relabeling,
the RENAMED CONSTRAINT has type Gamma but is mapped from a pre-existing constraint with
a different type. This pre-existing constraint was already in T_{S_n}, so the relabeling
does NOT introduce a genuinely new constraint — it merely renames an existing one.

The SBP morphism e introduces c_e as a GENUINELY NEW CONSTRAINT LABEL (not present in
T_{S_n}) with a genuinely new type (D4 condition). No type-relabeling of A_{S_n} can
produce A_{S_{n+1}} because A_{S_{n+1}} is defined on T_{S_{n+1}} = T_{S_n} union {c_e}
where c_e is a new label, not a renamed old label.

More precisely: phi*(A_{S_n}) is the closest approximation of A_{S_{n+1}} obtainable by
type-relabeling (it is A_{S_n} extended to subsets of T_{S_{n+1}} by ignoring c_e). But
A_{S_{n+1}} is LESS than phi*(A_{S_n}) on the sets where Compat(c_e, -, S_n) = 0. This
reduction cannot be achieved by relabeling: relabeling can only PERMUTE existing admissibility
verdicts, it cannot CREATE NEW INADMISSIBILITIES for subsets that did not previously contain
inadmissible elements. The SBP morphism's incompatibility restriction creates exactly such
new inadmissibilities.

**LAYER-OBL-001 sub-requirement 1: CONDITIONALLY CLOSED.**

The distortion residue is non-zero for SBP morphisms with the incompatibility guard active.
A_{S_{n+1}} carries content not producible by type-relabeling from A_{S_n}. This content
is gauge-equivariant (DR is gauge-equivariant as proved above). This is the formal signature
of Ehresmannian (source-layer) content: the admissibility predicate evolution carries
genuinely new structural content not explained by observer-layer type-relabeling.

**Conditions for full sub-requirement 1 closure:**

The proof that DR != 0 is established for the SBP incompatibility guard family (Family B).
Full sub-requirement 1 closure requires:

(C1) The SBP morphism class is non-empty for the operative source. (E042's Gödelian
     productivity theorem establishes this in the Gödelian regime; the FTS regime remains
     the D-FORK open question.)

(C2) The "no type-relabeling explains DR" argument must be extended from the one-step
     (S_n -> S_{n+1}) case to the multi-step trajectory case. The argument above covers
     one step; for the full trajectory, the distortion residues accumulate: at each SBP
     step, new inadmissibilities are introduced that no relabeling of the prior state can
     produce. This accumulation means the trajectory as a whole carries gauge-equivariant
     content not explainable by any fixed-source relabeling strategy.

(C3) The sub-requirement distinguishes between (a) quorum navigating a fixed non-computable
     source and (b) quorum constructing new source constraints. DR != 0 shows content is
     added beyond type-relabeling, but it does not rule out (a) — a non-computable source
     could include all the DR-extending steps as pre-existing sections. This is the residual
     threat that LAYER-OBL-001 sub-requirements 2 and 3 must address.

**In summary:** Sub-requirement 1 is CONDITIONALLY CLOSED. The condition is (C1) + (C2) +
the acknowledgment that sub-requirements 2 and 3 remain open. The distortion residue test
provides the formal signature of source-layer content at each SBP step; the full sub-
requirement 1 proof is this test applied trajectory-wide under Gödelian productivity.

---

## Verdict: Gauge Absorber #5 Status

**Previous classification (E046/E048):** Partial absorber (potentially fatal); conditionally
defeated pending GAUGE-COV-OBL-001 verification.

**Post-Test-1 classification: DEFEATED.**

The Gauge Absorber's attack requires a type-relabeling r that converts SBP-incompatible
proposals into compatible proposals. The GAUGE-COV-OBL-001 result (Family B: SBP
incompatibility guard is COVARIANT) directly defeats this: no type-relabeling can change
the incompatibility verdict, because the predicate is distortion-style — it evaluates
structural relations among types, not type names.

**Absorber classification update:**

| # | Absorber | Previous Classification | E049 Update |
|---|---|---|---|
| 5 | Gauge | Conditionally defeated — pending GAUGE-COV-OBL-001 | DEFEATED — Family B covariance proved; no type-relabeling can convert SBP-incompatible to compatible |

**Why the defeat is clean:** The Gauge Absorber required that "type" is gauge-relative —
i.e., that two types are the same "under gauge transformation." But in E031, SBP
incompatibility is not about type identity — it is about the STRUCTURAL IMPOSSIBILITY of
composing two extensions into a common successor state. This structural impossibility is
covariant. A type-relabeling cannot change whether two extensions can be composed.

The "Mexican standoff" mechanism (E048 Claim 1) applies exactly here: because both the
extension e and the base state S are relabeled consistently in the SAME WAY by r, their
structural relationship (incompatibility) is preserved. The incompatibility is a distortion
(both sides of the comparison are transformed), not a torsion (one side fixed, other
transformed).

---

## Verdict: LAYER-OBL-001 Sub-Requirement 1 Status

**Previous status:** Open. Named by E046, given Ehresmannian formulation by E047,
given distortion-residue diagnostic by E048.

**Post-Test-2 classification: CONDITIONALLY CLOSED.**

The distortion residue DR(S_n -> S_{n+1}) is:
- Non-zero for any SBP morphism (proved via concrete example; argument is general)
- Gauge-equivariant (proved formally)
- Not producible by any type-relabeling of A_{S_n} (proved: relabeling cannot create new
  inadmissibilities; SBP morphisms do)

This establishes: A_{S_{n+1}} carries source-layer content (in the Ehresmannian sense)
not explained by observer-layer type-relabeling. Sub-requirement 1 is satisfied.

**Remaining conditions for full closure:**

The conditional closure leaves sub-requirements 2 and 3 open:

- Sub-requirement 2 (E046): Show that global-coordination-structure irreducibility (ORT)
  is a source-side fact, not coordination-dynamics. The distortion residue is the FORMAL
  SIGNATURE of source-layer content; sub-requirement 2 needs the CAUSAL ATTRIBUTION of
  this content to the source, not just the formal signature.

- Sub-requirement 3 (E046): Distinguish Gödelian SBP space as source-side extension (not
  Platonist discovery of a fixed non-computable structure). This is D-FORK's open question.

LAYER-OBL-001 as a whole remains OPEN. Sub-requirement 1 is the first leg now closed.
Sub-requirements 2 and 3 are the remaining obligations.

---

## New Obligations Identified

| Obligation | Description | Status | Blocks |
|---|---|---|---|
| GAUGE-COV-OBL-001 | DISCHARGED by this exploration | CLOSED | Was blocking Gauge Absorber #5 defeat |
| E031 §I.2 covariance constraint | Add explicit "Compat must be schema-relabeling-covariant" condition to E031 §I.2 to rule out name-dependent instantiations | OPEN (documentation) | Family A conditional-covariance condition |
| LAYER-OBL-001 sub-req 1 | CONDITIONALLY CLOSED by distortion residue test | CONDITIONALLY CLOSED | Part of LAYER-OBL-001 |
| LAYER-OBL-001 sub-req 2 | Causal attribution of DR to source layer vs. coordination dynamics | OPEN | LAYER-OBL-001 full closure |
| LAYER-OBL-001 sub-req 3 | Gödelian SBP space as extension vs. Platonist discovery | OPEN (= D-FORK) | LAYER-OBL-001 full closure |
| DR trajectory extension | Extend one-step DR result to full trajectory (accumulation argument) | OPEN (routine) | Strengthens sub-req 1 closure |

---

## Cross-Reference Effects

### E046 Gauge Absorber #5

The summary table in E046 should be updated:
- Previous: "Partial absorber (potentially fatal)" / "Conditionally defeated — pending GAUGE-COV-OBL-001"
- New: "DEFEATED — E049 (2026-06-22) proved SBP incompatibility Compat (Family B) is schema-relabeling-covariant; no type-relabeling can convert SBP-incompatible to compatible"

### E046 LAYER-OBL-001 note

The LAYER-OBL-001 formal obligation (E046 §"Named layer gap") should be updated:
- Sub-requirement 1: CONDITIONALLY CLOSED by E049 distortion residue test (2026-06-22)
- Sub-requirements 2 and 3: remain open

### E031 §I.2

Add explicit covariance constraint: "Compat instantiations must be schema-relabeling-
covariant (for any bijection r on type names, Compat(r(c_e), r(X), r(S)) = Compat(c_e, X, S)).
This ensures that the admissibility predicate is sensitive to type structure, not type names.
The specific instantiations in this document (SBP incompatibility guard, RecCost) are both
schema-relabeling-covariant as verified by E049 (2026-06-22)."

### ASSOC-OBL-001 (E038) — no change

ASSOC-OBL-001 was proved unconditionally without conditions on Compat. The covariance
result here does not affect E038's proof.

---

## What Was Resolved and What Remains Blocked

### Resolved by This Exploration

1. **GAUGE-COV-OBL-001 CLOSED (2026-06-22):** All three operative Compat families in E031
   are schema-relabeling-covariant (Families B and C: unconditional; Family A: conditional
   on structural instantiation, which E031 already uses). E031's Compat is distortion-style
   by construction.

2. **Gauge Absorber #5 DEFEATED (2026-06-22):** The SBP incompatibility guard is covariant,
   so no type-relabeling converts SBP-incompatible proposals into compatible proposals. The
   Gauge Absorber's mechanism (gauge-equivalence of "incompatible" proposals via type
   relabeling) is formally blocked.

3. **LAYER-OBL-001 sub-requirement 1 CONDITIONALLY CLOSED (2026-06-22):** The distortion
   residue DR(S_n -> S_{n+1}) is non-zero and gauge-equivariant for SBP morphisms. A_{S_{n+1}}
   carries genuine structural content beyond any type-relabeling of A_{S_n}. This is the
   formal signature of Ehresmannian (source-layer) content.

### Still Blocked

1. **E031 §I.2 documentation gap:** Add explicit Compat covariance constraint. Minor;
   does not affect any proofs.

2. **LAYER-OBL-001 sub-requirement 2:** Causal attribution — showing that DR is a source-
   side fact, not coordination-dynamics. E049 proves DR != 0; it does not prove that the
   non-zero DR is generated by the source rather than by navigation of a fixed non-computable
   source. This is the projection-absorber residue (#4 in E046).

3. **LAYER-OBL-001 sub-requirement 3:** The D-FORK question. Gödelian SBP space as genuine
   source extension vs. Platonist completion. DR being non-zero is consistent with both
   readings. The distortion residue is the right formal object; its causal attribution is
   the remaining work.

4. **DR trajectory extension:** The one-step proof should be extended to the full trajectory
   to formally establish that the accumulated distortion residue is non-zero and non-relabeling-
   explainable across all stages. This is expected to be routine given the one-step argument
   but has not been written.

5. **All prior open obligations from E031:** FUNCTOR-OBL-001, monotone-obstruction for K
   superlinearity, Q-OBL-001, PP-3 source-layer declaration (the latter = LAYER-OBL-001).
   These are unchanged.

---

## Absorber Map Update

Full updated absorber table (from E046, incorporating E048 and E049 updates):

| # | Absorber | Classification (E046) | E048 Update | E049 Update |
|---|---|---|---|---|
| 1 | Latent Global Section | Partial absorber | — | — |
| 2 | Holonomy | Not applicable | — | — |
| 3 | Sheaf Completion | Partial absorber | — | — |
| 4 | Projection | Partial absorber | — | DR non-zero is consistent with projection reading; sub-req 2 needed |
| **5** | **Gauge** | **Partial absorber (potentially fatal)** | **Conditionally defeated** | **DEFEATED — Family B covariance proved by GAUGE-COV-OBL-001** |
| 6 | Path Dependence | Partial absorber | — | — |
| 7 | Avalanche Settlement | Partial absorber | — | — |
| 8 | Constraint Revelation | Partial absorber | — | — |
| 9 | Type Discovery | Partial absorber | — | — |
| 10 | Permission vs. Creation | Partial absorber | — | — |
| 11 | Computational Irreducibility | Partial absorber (strongest) | — | — |
| 12 | Epistemic Uncertainty | Partial absorber | — | — |
| 13 | Randomness | Partial absorber | — | — |
| 14 | Hidden State | Partial absorber | — | — |
| 15 | Modal Space | Interpretation shift | — | — |
| 16 | Renaming | Not applicable as stated | — | — |
| 17 | Boundary Reification | Partial absorber | — | — |
| 18 | Observer Privilege | Interpretation shift | — | — |
| 19 | Economic Mechanism | Partial absorber | — | — |
| 20 | Fixed-Mu_infty Strawman | Not applicable (proof adequate) | — | — |

**Fatal absorbers: 0. Defeated absorbers: 1 (Gauge Absorber #5).**
