---
artifact_type: exploration
status: active
exploration_id: E035
run_ref: RUN-0047
claim_refs:
  - TI-C003
  - TI-C019
topic: mu_M_metabolic_field_specification
phase: 2B
date: 2026-06-22
---

# E035: Formal mu_M Specification — Metabolically-Scaled Sublinear Issuance Measure

## Purpose

The cross-repo session proposed a mu field candidate:

```text
mu_M(r) = c * |r|^{3/4}
```

where `r` is a realized structure (constraint state, event, or extension instance) and `c`
is a positive constant. The exponent 3/4 is explicitly metabolic: it matches the Kleiber
scaling law of biological metabolism (metabolic rate scales as body mass to the 3/4 power).
The proposal is that issuance cost or issuance rate may scale sublinearly (non-additively)
with realized structure size.

This exploration attempts to draft a formal specification of `mu_M` that meets the
source-object spec's field requirements as derived from FORMAL-OBJECT.md, FORMAL-OBJECT-
PRESSURE-MATRIX.md, and the current claim state of TI-C003.

The five required field properties (from the FORMAL-OBJECT spec pressure):

1. **Units / dimensional consistency:** mu must be defined on a domain with a meaningful
   size measure `|r|` and must produce a real-valued output with consistent units.

2. **Comparison rule:** For two realized structures r, r', the comparison mu_M(r) vs
   mu_M(r') must be well-defined and interpretable.

3. **Monotonicity:** mu_M should be monotonically increasing in |r| (more realized
   structure cannot have less measure than less realized structure, under the same
   comparison basis).

4. **Transformation behavior:** How does mu_M transform under extension? If `e: S -> S'`
   is an admissible extension, what is the relation between `mu_M(S)` and `mu_M(S')`?

5. **Absorber comparison:** Does mu_M differ from named alternatives — entropy, action,
   information, Bekenstein bound, metabolic rate, or assembly complexity?

---

## Formal Specification Attempt

### Domain

Let `r` be an element of the realized set `R`, where `R` is the set of realized source
constraints or extension instances in TI's formal object. For the mu_M field to be
well-defined, `R` must carry a size measure:

```text
| · | : R -> [0, infinity)
```

The most natural candidate for `|r|` in TI's context is the number of typed constraints
realized in `r`, i.e., the cardinality or volume of the constraint state:

```text
|r| = |{c in C : c is active in r}|
```

For a continuous or weighted version: `|r| = sum_{c in C} w(c) * [c active in r]` where
`w(c)` is a weight assigned to constraint `c`.

**Field requirement 1 (units):** If `|r|` is dimensionless (constraint count or weighted
constraint mass), then `mu_M(r) = c * |r|^{3/4}` produces a dimensionless output scaled
by `c`. For `mu_M` to have units interpretable as an issuance measure, `c` must carry the
appropriate dimensional factor:

```text
c in [issuance_units / constraint_units^{3/4}]
```

This is not a problem in itself, but `c` is externally supplied — TI does not currently
derive the constant `c` from source admissibility. This is the first absorption risk point.

### Definition

```text
mu_M : R -> [0, infinity)
mu_M(r) = c * |r|^{3/4}        (c > 0, externally supplied)
```

### Field Requirement 2: Comparison Rule

For r, r' in R:

```text
mu_M(r) <= mu_M(r')  iff  |r| <= |r'|
```

The comparison rule inherits from the size measure `|·|`. mu_M is a strictly increasing
function of |r| (for |r| > 0), so comparison by mu_M is equivalent to comparison by size.

This means mu_M does NOT add a new comparison structure beyond the size ordering — it
is a monotone rescaling of |r|. Two structures with the same size have the same mu_M.

**Implication:** mu_M cannot be a discriminator between same-size extensions. If TI needs
mu to distinguish extensions of equal constraint cardinality, mu_M is insufficient.

### Field Requirement 3: Monotonicity

```text
If |r| < |r'|, then mu_M(r) < mu_M(r')
```

Proved: `x^{3/4}` is strictly increasing on `[0, infinity)`.

Monotonicity is satisfied. However, the monotonicity is inherited from size, not from any
TI-specific structure. This weakens the case for mu_M as a formal advance.

### Field Requirement 4: Transformation Behavior Under Extension

Let `e: S -> S'` be an admissible extension in `Ext_S`. Then:

```text
S' extends S: |S'| >= |S| (source state S' includes all constraints in S plus new ones)
```

Under this growth assumption:

```text
mu_M(S') = c * |S'|^{3/4} >= c * |S|^{3/4} = mu_M(S)
```

So mu_M is non-decreasing under extension. The growth rate is:

```text
delta_mu = mu_M(S') - mu_M(S) = c * (|S'|^{3/4} - |S|^{3/4})
```

For a single constraint addition (`|S'| = |S| + 1`):

```text
delta_mu = c * ((|S| + 1)^{3/4} - |S|^{3/4})
         ≈ c * (3/4) * |S|^{-1/4}   (for large |S|)
```

The incremental issuance decreases as the source grows. This is the sublinearity (non-
additivity) property: each new constraint added contributes less issuance measure than the
previous one. The system does not issue at a constant per-constraint rate; it issues at a
diminishing marginal rate.

**Key formal property:** mu_M is NOT additive under extension concatenation. For two
independent constraint sets A, B:

```text
mu_M(A union B) = c * |A union B|^{3/4}
mu_M(A) + mu_M(B) = c * |A|^{3/4} + c * |B|^{3/4}
```

By the inequality `(a + b)^{3/4} < a^{3/4} + b^{3/4}` for `a, b > 0`, we have:

```text
mu_M(A union B) < mu_M(A) + mu_M(B)
```

This subadditivity is the formal signature of mu_M that distinguishes it from an additive
measure (entropy, information content, cardinality itself).

### Field Requirement 5: Absorber Comparison

The question is whether `mu_M(r) = c * |r|^{3/4}` adds any formal content over named
alternatives.

#### vs. Entropy

Shannon entropy `H(r) = -sum_i p_i log p_i` is defined over probability distributions,
not constraint sets. For a uniform distribution over `|r|` constraints, `H = log |r|`.
mu_M grows faster than entropy for large |r| (|r|^{3/4} >> log |r|), so mu_M is not
equivalent to entropy.

**Absorber status:** Not absorbed by entropy.

#### vs. Cardinality / Volume

`mu_L(r) = c * |r|` is the linear (additive) measure. mu_M differs from mu_L in being
subadditive. This is a formal difference.

**Absorber status:** Not absorbed by cardinality measure.

#### vs. Bekenstein Bound

The Bekenstein bound `S <= 2 pi k R E / (hbar c)` scales linearly in energy and radius —
it is a linear bound on entropy. mu_M is a power-law measure, not a linear bound. They
are incommensurable without a mapping between `|r|` and physical energy/radius.

**Absorber status:** Not directly absorbed by Bekenstein, but no connection to Bekenstein
is established either.

#### vs. Assembly Index (Assembly Theory)

Assembly Theory's assembly index `a(x)` counts the minimum number of steps needed to
assemble object `x` from basic parts. For an object assembled from `n` copies of a
basic unit, `a(x) ~= n`. This is linear in the number of basic units, so `a(x) ~= |r|`
under the simplest mapping.

mu_M with exponent 3/4 is sublinear in |r|. Therefore mu_M is NOT equivalent to assembly
index unless the assembly process itself has a sublinear step-count scaling.

**Absorber status:** Not absorbed by assembly index (different scaling). However, the
distinction requires a formal argument connecting `|r|` to assembly steps.

#### vs. Metabolic Rate (Kleiber Law)

Kleiber's law: metabolic rate ~ body mass^{3/4}. This is an empirical biological law
describing energy throughput in living systems. mu_M is proposed as the analogue of
metabolic rate for TI's issuance measure.

**Absorber status:** mu_M is motivated by Kleiber, but Kleiber applies to biological
organisms in physical space. The absorber question is: does Kleiber supply the exponent
3/4 as a necessary consequence of some structure TI can specify, or is 3/4 an empirical
biological constant imported without justification?

If 3/4 is derived from a fractal transport network (West-Brown-Enquist derivation, 1997):
the exponent comes from optimizing supply through a hierarchically branching network in 3D
space. This derivation requires a spatial embedding and a network topology — neither of
which TI's source constraints supply.

Therefore: the specific exponent 3/4 is absorber-threatened by the WBE derivation. TI
would need its own derivation of the exponent from source admissibility.

**Absorber status:** The exponent 3/4 is absorbed by WBE fractal transport network
optimization unless TI derives the exponent from typed source constraints.

---

## Formal Specification Summary

```yaml
object: mu_M
definition: mu_M(r) = c * |r|^{3/4}
domain: R (realized constraint states)
codomain: [0, infinity)
constant_c: externally_supplied (not derived)
exponent: 3/4 (motivated by Kleiber; WBE-absorbed unless derived from source structure)
units: consistent if c carries appropriate dimensional factor
comparison_rule: inherits from size ordering (not new)
monotonicity: satisfied (strict for |r| > 0)
transformation_under_extension: non-decreasing; subadditive (mu_M(A union B) < mu_M(A) + mu_M(B))
key_formal_property: subadditivity (non-additivity under extension concatenation)
absorption_result:
  - not absorbed by entropy
  - not absorbed by cardinality
  - not absorbed by Bekenstein directly
  - not absorbed by assembly index (different scaling)
  - exponent 3/4 absorbed by WBE network optimization UNLESS derived from source admissibility
  - constant c not derived
primary_open_question: >
    Can TI derive the exponent 3/4 (or any specific sublinear exponent) from typed source
    admissibility predicates without importing spatial embedding, biological metabolism, or
    network topology? If yes: mu_M has a non-trivial TI-specific content. If no: it is
    motivated Kleiber import.
kill_condition: >
    If the exponent 3/4 cannot be derived from source admissibility AND c is freely
    tunable, then mu_M is a parametric family of power-law measures available to any
    theory — it is not TI-specific and should be treated as a measure design choice,
    not a formal claim.
specification_status: partially_complete
blocking_gap: derivation of exponent from source admissibility
```

## Provisional Result

mu_M is partially specified. Its key formal property — subadditivity under extension
concatenation — is non-trivial and distinguishes it from additive measures. However,
the specific exponent 3/4 is not derived from TI's formal object and is absorbed by the
WBE fractal network derivation. The constant `c` is also not derived.

mu_M is a **candidate** issuance measure with one genuine formal property (subadditivity)
and one unearned component (the exponent). The specification is not complete until the
exponent is either derived or generalized to an arbitrary sublinear exponent family
`mu(r) = c * |r|^alpha` for `0 < alpha < 1`, with TI providing no further constraint on
`alpha`. In the generalized form, the claim is: issuance is subadditive in realized
structure size — the specific scaling is not TI's to determine.

The generalized subadditivity claim is not killed by WBE and deserves its own exploration.
See E036.
