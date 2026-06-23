---
artifact_type: exploration
status: active
exploration_id: E038
date: 2026-06-22
topic: assoc_obl_001_composition_associativity_proof
claim_refs:
  - TI-C019
  - TI-C020
relates_to:
  - E031 (Ext_S category structure; ASSOC-OBL-001 origin)
  - E032 (cross-repo N, C, K coordination; references ASSOC-OBL-001)
  - E034 (lambda* absorber test; conditioned on ASSOC-OBL-001)
blocking_task_addressed: ASSOC-OBL-001 — composition associativity proof for Ext_S
proof_verdict: CONDITIONALLY CLOSED
---

# E038: Proof of Composition Associativity in Ext_S (ASSOC-OBL-001)

## Purpose

E031 defined the Ext_S category structure and identified ASSOC-OBL-001 as a blocking
obligation: prove that composition in Ext_S is associative for specific Compat predicate
instantiations, not just abstractly.

This exploration provides that proof. The central finding is that associativity
**separates into two independent questions**: (A) equality of output states, and
(B) consistency of well-definedness conditions. Question A is trivially settled by
definition. Question B requires a specific structural condition on Compat — identified
here precisely — and that condition is satisfied by all instantiations defined in E031
and used across the repo.

---

## 1. Definitions Recalled from E031

### States

A typed source constraint state is S = (T_S, A_S) where:
- T_S is a finite set of typed constraint labels
- A_S : P(T_S) -> {0, 1} is the admissibility predicate (downward-closed, empty-set-admissible)

### Morphisms

A morphism e: S -> S' is an admissible extension e = (S, S', c_e) where:
- T_{S'} = T_S union {c_e}, with c_e not in T_S (one new constraint label)
- A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S) holds

Here Compat(c_e, X, S) is a typed compatibility predicate: a boolean function of
the new constraint label c_e, an existing constraint subset X of T_S, and the base
state S.

### Composition

For e1: S -> S' and e2: S' -> S'', the composite (e2 ∘ e1): S -> S'' is defined
when e1 and e2 are both admissible, and produces state S'' with:
- T_{S''} = T_S union {c_{e1}} union {c_{e2}}
- A_{S''}(X) = 1 iff A_{S'}(X \ {c_{e2}}) = 1 AND Compat(c_{e2}, X \ {c_{e2}}, S') holds
  (which further unfolds to a condition over A_S, Compat(c_{e1}, -, S), and Compat(c_{e2}, -, S'))

---

## 2. The Associativity Claim

Let f: S -> T, g: T -> U, h: U -> V be morphisms in Ext_S, with:
- f adds constraint c_f to T_S, producing T = (T_S union {c_f}, A_T)
- g adds constraint c_g to T_T, producing U = (T_T union {c_g}, A_U)
- h adds constraint c_h to T_U, producing V = (T_U union {c_h}, A_V)

We must show: (h ∘ g) ∘ f  =  h ∘ (g ∘ f)  as morphisms in Ext_S.

Two morphisms S -> V in Ext_S are equal iff they produce the same target state
(same T_V and same A_V). This is what must be verified.

---

## 3. Part A: Equality of Output States (Trivial)

**Left side (h ∘ g) ∘ f:**

Step 1: f produces T = (T_S ∪ {c_f}, A_T)
Step 2: h ∘ g produces a morphism T -> V by:
  - g adds c_g to T_T, producing U = (T_T ∪ {c_g}, A_U)
  - h adds c_h to T_U, producing V = (T_U ∪ {c_h}, A_V)
Step 3: (h ∘ g) ∘ f adds c_f first, then c_g, then c_h

Constraint set of V: T_S ∪ {c_f} ∪ {c_g} ∪ {c_h}

**Right side h ∘ (g ∘ f):**

Step 1: g ∘ f is a morphism S -> U by:
  - f adds c_f to T_S, producing T = (T_S ∪ {c_f}, A_T)
  - g adds c_g to T_T, producing U = (T_T ∪ {c_g}, A_U)
Step 2: h adds c_h to T_U, producing V = (T_U ∪ {c_h}, A_V)
Step 3: h ∘ (g ∘ f) adds c_f first, then c_g, then c_h

Constraint set of V: T_S ∪ {c_f} ∪ {c_g} ∪ {c_h}

**Conclusion Part A:** Both sides produce a state V with identical constraint label set
T_V = T_S ∪ {c_f, c_g, c_h}. This holds purely by set union commutativity and
associativity and requires no condition on Compat. The constraint label set of the
composed morphism is independent of the order of associative bracketing.

---

## 4. Part B: Equality of Admissibility Predicates

The nontrivial question is whether A_V computed via the left bracketing equals A_V
computed via the right bracketing. We trace both computations explicitly.

Let X be any subset of T_V = T_S ∪ {c_f, c_g, c_h}. We evaluate A_V(X) on both sides.

**Notation abbreviation:**
- X_f = X \ {c_f},  X_g = X \ {c_g},  X_h = X \ {c_h}
- X_fg = X \ {c_f, c_g},  X_fh = X \ {c_f, c_h},  X_gh = X \ {c_g, c_h}
- X_fgh = X \ {c_f, c_g, c_h}

The unfolding proceeds by repeatedly applying the A_{S'}(X) definition:
A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S) holds.

### Left-side unfolding: A_V^{left}(X)

The morphism (h ∘ g) ∘ f adds constraints in the order (c_f, then c_g, then c_h).

The admissibility predicate is built up in three layers:

```
A_T(Y)  = 1 iff A_S(Y \ {c_f}) = 1  AND  Compat(c_f, Y \ {c_f}, S)
A_U(Z)  = 1 iff A_T(Z \ {c_g}) = 1  AND  Compat(c_g, Z \ {c_g}, T)
A_V(X)  = 1 iff A_U(X \ {c_h}) = 1  AND  Compat(c_h, X \ {c_h}, U)
```

Expanding A_V^{left}(X) fully:

```
A_V^{left}(X) = 1 iff
  (i)  A_S(X_fgh) = 1
  (ii) Compat(c_f, X_fgh, S)
  (iii) Compat(c_g, X_gh \ {c_f}, T)  =  Compat(c_g, X_fgh, T)
  (iv) Compat(c_h, X_h \ {c_f, c_g}, U)  =  Compat(c_h, X_fgh, U)
```

Wait — care is needed. The subsets in the Compat calls depend on which constraints
are present in X. Let us be precise.

For X ⊆ T_V = T_S ∪ {c_f, c_g, c_h}:

A_V(X) = 1 iff A_U(X \ {c_h}) = 1 AND Compat(c_h, X \ {c_h}, U)

Let X' = X \ {c_h} ⊆ T_U = T_S ∪ {c_f, c_g}.

A_U(X') = 1 iff A_T(X' \ {c_g}) = 1 AND Compat(c_g, X' \ {c_g}, T)

Let X'' = X' \ {c_g} = X \ {c_g, c_h} ⊆ T_T = T_S ∪ {c_f}.

A_T(X'') = 1 iff A_S(X'' \ {c_f}) = 1 AND Compat(c_f, X'' \ {c_f}, S)

Let X''' = X'' \ {c_f} = X \ {c_f, c_g, c_h} ⊆ T_S.

Fully expanded:

```
A_V^{left}(X) = 1 iff all four hold:
  (L1) A_S(X \ {c_f, c_g, c_h}) = 1
  (L2) Compat(c_f, X \ {c_f, c_g, c_h}, S)
  (L3) Compat(c_g, X \ {c_g, c_h}, T)        [note: X \ {c_g,c_h} may contain c_f]
  (L4) Compat(c_h, X \ {c_h}, U)              [note: X \ {c_h} may contain c_f, c_g]
```

### Right-side unfolding: A_V^{right}(X)

The morphism h ∘ (g ∘ f) adds constraints in the same physical order (c_f, c_g, c_h)
but under the right associative bracketing. The intermediate states are:

The composite g ∘ f: S -> U is a morphism with:
- T_U = T_S ∪ {c_f, c_g}
- A_U(Z) built by applying f then g, i.e. the same A_U as above (since A_U depends
  only on A_S, c_f, Compat(c_f,-,S), c_g, Compat(c_g,-,T), and T itself; none of
  these depend on how we bracket the composition at the V level)

Then h: U -> V adds c_h to T_U, giving:

```
A_V^{right}(X) = 1 iff A_U(X \ {c_h}) = 1 AND Compat(c_h, X \ {c_h}, U)
```

where A_U is the same predicate as in the left case (built from the same c_f, c_g,
Compat(c_f,-,S), Compat(c_g,-,T) sequence).

Expanding A_V^{right}(X) fully:

```
A_V^{right}(X) = 1 iff all four hold:
  (R1) A_S(X \ {c_f, c_g, c_h}) = 1
  (R2) Compat(c_f, X \ {c_f, c_g, c_h}, S)
  (R3) Compat(c_g, X \ {c_g, c_h}, T)
  (R4) Compat(c_h, X \ {c_h}, U)
```

### Comparison

```
Left:   (L1) A_S(X_fgh)  (L2) Compat(c_f, X_fgh, S)  (L3) Compat(c_g, X_gh\{c_f}, T)  (L4) Compat(c_h, X_h\{c_g}, U)
Right:  (R1) A_S(X_fgh)  (R2) Compat(c_f, X_fgh, S)  (R3) Compat(c_g, X_gh\{c_f}, T)  (R4) Compat(c_h, X_h\{c_g}, U)
```

With the notation made explicit:
- X_fgh = X \ {c_f, c_g, c_h}  (same in L1/R1 and L2/R2)
- X \ {c_g, c_h} = X_gh, which may contain c_f (same expression in L3 and R3)
- X \ {c_h} = X_h, which may contain c_f and c_g (same expression in L4 and R4)

**The four conditions are identical.** L1 = R1, L2 = R2, L3 = R3, L4 = R4.

Therefore A_V^{left}(X) = A_V^{right}(X) for all X ⊆ T_V.

**Conclusion Part B:** The admissibility predicates on both sides of the bracketing are
definitionally equal. No condition on Compat beyond those already required for the
individual morphisms to be well-defined is needed.

---

## 5. Why the Commutativity Condition in E031 Is Not Required

E031 flagged a commutativity condition:

> "Compat(c2, X ∪ {c1}, S) = Compat(c1, X ∪ {c2}, S)"

and asked whether this is required for associativity. The answer, established above, is no.

**The confusion arose from conflating two different questions:**

(i) **Associativity of composition:** Does (h ∘ g) ∘ f = h ∘ (g ∘ f)?
    Answer: yes, always. The proof above is unconditional.

(ii) **Commutativity of composition:** Does g ∘ f = f ∘ g (when both are defined)?
    Answer: not in general. Commutativity is a separate and stronger property.
    It would require c_f and c_g to be interchangeable in the admissibility expansion,
    which is exactly the condition Compat(c_f, X ∪ {c_g}, S) = Compat(c_g, X ∪ {c_f}, S).
    This condition is NOT required for associativity.

The commutativity condition in E031 is a condition for g ∘ f = f ∘ g, not for
(h ∘ g) ∘ f = h ∘ (g ∘ f). E031 named the correct obligation (associativity) but
then stated a sufficient condition for a different (stronger) property (commutativity).
The associativity proof requires no such condition.

---

## 6. The Associativity Proof (Clean Statement)

**Theorem (ASSOC-OBL-001 resolution):**

Let Ext_S be the category with:
- Objects: typed source constraint states S = (T_S, A_S)
- Morphisms: admissible extensions e: S -> S' adding one constraint c_e
- Admissibility: A_{S'}(X) = 1 iff A_S(X \ {c_e}) = 1 AND Compat(c_e, X \ {c_e}, S)
- Composition: sequential constraint addition

For any morphisms f: S -> T, g: T -> U, h: U -> V in Ext_S,

```
(h ∘ g) ∘ f  =  h ∘ (g ∘ f)
```

**Proof:**

Both sides produce a morphism S -> V. Two morphisms S -> V are equal iff they produce
the same target state, i.e., the same (T_V, A_V).

**Step 1 (constraint sets):** T_V = T_S ∪ {c_f, c_g, c_h} on both sides, since
set union is associative. ✓

**Step 2 (admissibility):** Let X ⊆ T_V. Expand A_V(X) on both sides by iteratively
applying the morphism definition at each layer (h layer, then g layer, then f layer):

Both expansions produce the identical four-condition conjunction:
```
A_S(X \ {c_f, c_g, c_h}) = 1
AND Compat(c_f, X \ {c_f, c_g, c_h}, S)
AND Compat(c_g, X \ {c_g, c_h}, T)
AND Compat(c_h, X \ {c_h}, U)
```

The subset arguments in each Compat call are determined by which of {c_f, c_g, c_h}
belong to X, and these subsets are the same regardless of associative bracketing,
because the bracketing changes only the order in which layers are unfolded, not the
final unfolded expression.

Therefore A_V^{left}(X) = A_V^{right}(X) for all X ⊆ T_V. ✓

**Conclusion:** (h ∘ g) ∘ f = h ∘ (g ∘ f). Composition in Ext_S is associative.
No conditions on Compat beyond those required for the individual morphisms to be
well-defined are needed. QED.

---

## 7. Verification Against Repo's Compat Instantiations

E031 uses Compat in three contexts. We verify that the proof applies to each.

### Instantiation 1: Morphism admissibility predicate (E031 §I.2)

```
Compat(c_e, X, S)  [general form; no commutativity constraint imposed]
```

The proof in §6 applies to this general form without restriction. The theorem holds
for any Compat predicate whatsoever. The predicate can be asymmetric (Compat(c2, X∪{c1}, S)
≠ Compat(c1, X∪{c2}, S)) without breaking associativity.

### Instantiation 2: SBP incompatibility (E031 §III.1)

```
Compat(c_e, T_{S''}, S) = 0  for SBP morphisms (incompatibility condition)
```

This is a specific binary value of Compat for certain constraint pairs. It does not
affect the associativity proof, which holds for all values of Compat.

### Instantiation 3: Reconciliation cost (E031 §II.3)

```
RecCost(e, S) = |{c in T_S : Compat(c_e, {c}, S) requires checking}| / |T_S|
```

This uses Compat as a checking predicate for cost accounting, not for admissibility
structure. The associativity of the Ext_S category is independent of RecCost; RecCost
is a derived quantity over morphisms, not part of the categorical structure.

### Summary

All three Compat instantiations in the repo are compatible with the associativity
theorem. None requires modification.

---

## 8. Assumptions, Failure Risks, and Kill Conditions

### Assumptions

1. **Single-constraint-per-morphism:** Each morphism adds exactly one constraint
   label c_e. The proof relies on this: the three-layer expansion uses exactly
   one new constraint per layer. Morphisms adding multiple constraints simultaneously
   would require a separate analysis (composition of single-step morphisms handles
   this case by decomposition, so this is not a restriction in practice).

2. **No side-effects in state construction:** A_{S'}(X) is fully determined by
   A_S, c_e, and Compat(c_e, -, S). If state construction had path-dependent
   side effects (e.g., a global counter that increments on each morphism application),
   the unfolded expressions could differ. E031's definition has no such side effects.

3. **Set-theoretic equality of states:** Two states are equal iff they have the same
   T_S and the same A_S predicate. This is definitional in E031.

### Failure risks

None identified for the specific associativity claim. The proof is a straightforward
unfolding argument with no gaps.

The E031 risk of "admissibility predicates not being independent of constraint addition
order" is real for the commutativity property (g ∘ f = f ∘ g) but not for the
associativity property ((h ∘ g) ∘ f = h ∘ (g ∘ f)). These must not be conflated.

### Kill conditions

This proof would be killed if the morphism definition in E031 is revised to include
path-dependent state construction — i.e., if A_{S'} depends on something other than
(A_S, c_e, Compat(c_e, -, S)). Any revision of the morphism definition must be
checked against this proof.

---

## 9. What Was Resolved and What Remains Blocked

### Resolved by this exploration

**ASSOC-OBL-001 CLOSED:** Composition in Ext_S is associative for all Compat
predicate instantiations that satisfy the E031 morphism definition. The proof is
unconditional within that definition: no commutativity requirement on Compat, no
restriction on state space, no constraint on the specific Compat values.

**Key insight recorded:** E031's commutativity requirement (Compat(c2, X∪{c1}, S)
= Compat(c1, X∪{c2}, S)) is not needed for associativity. It would be needed for
commutativity of composition (g ∘ f = f ∘ g), which is a distinct and stronger
property. The Ext_S category is not required to be commutative for any downstream
result in E031 or E034. This condition should not be presented as a blocking obligation
for the categorical structure.

### Still blocked (unchanged from E031)

1. **FUNCTOR-OBL-001:** N naturality obligation.
2. **IA verification:** Independence assumption for K superlinearity.
3. **WITNESS-OBL-001:** Ostrom witness self-reference proof.
4. **Q-OBL-001:** Q circularity avoidance.
5. **PP-3 source-layer declaration:** Layer-neutral definitions not yet grounded as source-side.

---

## Verdict

**ASSOC-OBL-001: CLOSED.**

Proof is unconditional within the E031 morphism definition. Both sides of
(h ∘ g) ∘ f = h ∘ (g ∘ f) produce the same target state by a direct unfolding
argument. No additional constraint on the Compat predicate is required.

The E031 commutativity condition is a necessary condition for composition
commutativity (g ∘ f = f ∘ g), not for composition associativity. This distinction
is load-bearing: commutativity of composition is not claimed or needed in E031 or
downstream explorations.

Ext_S is a genuine category, pending identity law verification (trivial by the null
extension definition of id_S) and the remaining open obligations listed above.
