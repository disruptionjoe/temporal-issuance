---
artifact_type: exploration
status: active
exploration_id: E036
run_ref: RUN-0047
claim_refs:
  - TI-C003
  - TI-C019
topic: sublinear_mu_discriminator
phase: 2B
date: 2026-06-22
---

# E036: What mu_M Adds That TI's Existing mu Candidates Do Not

## Purpose

E035 established that `mu_M(r) = c * |r|^{3/4}` is partially absorbed (the exponent 3/4 is
absorbed by WBE; the constant `c` is not derived), but identified one non-trivial formal
property: **subadditivity under extension concatenation**.

This exploration asks the structural question: what does a sublinear, non-additive measure
add to TI's program that the existing mu candidates do not?

The existing mu candidates, from FORMAL-OBJECT-PRESSURE-RESULTS.md and the ongoing
formal-object pressure record:

| Candidate | Status | Primary Absorber |
|---|---|---|
| Generic monotone issuance amount | killed | entropy, information, action, probability, volume |
| Entropy (Shannon / thermodynamic) | absorber, not candidate | well-defined but absorbed by thermodynamics |
| Information content | absorber candidate | absorbed by Shannon / Kolmogorov |
| Action (physical) | absorber candidate | absorbed by Lagrangian mechanics |
| Probability measure | absorber candidate | absorbed by standard probability theory |
| Volume / cardinality | weakened placeholder | absorbed by geometry or cardinality |

mu_M as a **subadditive power-law measure** is NOT on this list. The question is whether
subadditivity constitutes a genuine formal addition.

---

## What the Existing Candidates Fail To Capture

### Problem with Additive Measures

All of the killed and named absorbers are additive or super-additive in the natural sense:

```text
entropy: H(A union B) = H(A) + H(B) - I(A;B)   (subadditive, but through mutual info)
information: I(A) + I(B) for independent sources (additive)
action: S[A + B path] = S[A path] + S[B path]  (additive over path segments)
probability: P(A union B) = P(A) + P(B) - P(A intersect B) (inclusion-exclusion, not sub-add)
cardinality: |A union B| = |A| + |B| - |A intersect B|
```

These measures are either additive, inclusion-exclusion additive, or subadditive through
information overlap. None of them is **inherently subadditive as a function of system size**.

Shannon entropy is subadditive in the sense `H(X, Y) <= H(X) + H(Y)` but this is through
correlation structure, not through a power-law scaling of individual systems.

### The Subadditivity Property mu_M Provides

mu_M is subadditive in a different sense: for two disjoint constraint sets A, B with
no shared structure:

```text
mu_M(A union B) = c * (|A| + |B|)^{3/4} < c * |A|^{3/4} + c * |B|^{3/4} = mu_M(A) + mu_M(B)
```

The whole is less than the sum of its parts — not because of shared information, but because
of the power-law scaling. This is **size-driven subadditivity**, not correlation-driven
subadditivity. It is a property of the functional form, independent of any statistical
relationship between A and B.

This type of subadditivity characterizes:
- Biological metabolic efficiency (organisms process resources more efficiently at scale)
- Urban scaling (cities have sublinear infrastructure costs per capita)
- Network effects in distributed systems (shared transport reduces per-unit cost)

None of these are currently in TI's formal vocabulary or its named absorber list.

---

## What mu_M Adds: Three Candidates

### Addition 1: Non-Additivity as a Formal Property of the Issuance Measure

The current TI program has no formal claim about the additivity or non-additivity of the
issuance measure. The killed generic reading (`mu as monotone issuance amount`) made no
additivity claim. The surviving placeholder (`unresolved measure candidate`) is agnostic.

Introducing subadditivity as a **requirement** on mu — rather than a consequence of a
specific scaling law — is a formal constraint on what mu can be. Specifically:

```text
A mu field satisfying the subadditivity constraint:
mu(A union B) < mu(A) + mu(B) for all disjoint A, B with |A|, |B| > 0
```

...rules out:
- Cardinality (not subadditive; it is inclusion-exclusion additive)
- Action (not subadditive in general)
- Probability (not subadditive; inclusion-exclusion additive)
- Linear information measures (additive for independent sources)

It does NOT rule out:
- Shannon entropy (can be subadditive through correlation)
- Bekenstein bound (linear bound; must check case by case)

This is a discriminator. A subadditivity constraint on mu narrows the field of absorber
candidates to those that can produce size-driven subadditivity.

**Verdict:** Subadditivity as a required property of mu adds a formal constraint not
currently stated anywhere in TI's formal object specification.

### Addition 2: Diminishing Marginal Issuance

From E035's transformation behavior analysis:

```text
delta_mu(|r|) = c * ((|r| + 1)^{3/4} - |r|^{3/4}) ~ c * (3/4) * |r|^{-1/4}
```

The incremental issuance per new constraint decreases as the realized structure grows. This
means: **larger realized structures issue at a lower marginal rate than smaller ones.**

This property has a specific formal consequence for TI's claim structure:

```text
If issuance is the mechanism that keeps reality open-ended (TI-C019), and if issuance has
diminishing marginal returns, then:
- small realized structures issue at a higher marginal rate (early sources are more fecund)
- large realized structures issue at a lower marginal rate (mature sources are less fecund)
```

This is a trajectory-level prediction about the TI formal object that no existing mu
candidate makes:

| Measure | Marginal increment per new constraint |
|---|---|
| Cardinality | Constant: 1 per constraint |
| Entropy (uniform) | Decreasing: ~ 1/log |r| per constraint |
| Shannon entropy (general) | Depends on distribution |
| mu_M | Decreasing: ~ (3/4) |r|^{-1/4} (specific power law) |

Only entropy and mu_M among the candidates produce diminishing marginal increments from
system size alone. But entropy's diminishing returns depend on the probability distribution
— they are not purely size-driven. mu_M's diminishing returns are purely size-driven.

**Verdict:** Diminishing marginal issuance as a size-only effect is a new formal property
not captured by any existing candidate.

### Addition 3: Non-Linearity as a Test Surface for Source-Side Discriminators

The PP-3 crux from E029 is:

```text
Can a discriminator prove that D4/issuance events are source-side, not merely projection-
layer disclosure from a fixed richer source?
```

A subadditive mu provides a potential discriminator:

```text
If mu_M is the issuance measure, then the rate of new issuance events decreases as
realized structure grows. A projection-layer system that is simply disclosing a fixed
source Mu_infty through widening apertures would exhibit a DIFFERENT mu pattern:
the rate of new disclosures depends on the aperture growth rate, not on system size.
```

Formally:

```text
Source-side issuance (TI Hypothesis A):
  d(mu_M) / d(|r|) ~ (3/4) c |r|^{-1/4} (size-dependent, decreasing)

Projection disclosure (Hypothesis B):
  rate = d(aperture_exposure) / dt (time-dependent or aperture-dependent, not size-dependent)
```

If an empirical or formal system shows size-dependent sublinear issuance rate — rate
decreasing as |r| grows, independent of aperture — this is inconsistent with pure
projection-layer disclosure and supports source-side structure.

This is a discriminator candidate for PP-3. It does not prove source-side issuance, but
it defines a pattern that the projection-layer absorber (Hypothesis B) cannot reproduce
unless the aperture growth rate happens to track |r|^{-1/4} exactly — an unlikely
coincidence without independent explanation.

**Verdict:** A sublinear mu provides a candidate PP-3 discriminator not available from
any existing mu candidate.

---

## What mu_M Does NOT Add

1. **A derivation of the specific exponent.** The exponent 3/4 is absorbed by WBE.
   Any exponent in (0, 1) produces the same formal properties (subadditivity, diminishing
   marginal issuance, size-dependent rate). The specific value 3/4 requires derivation.

2. **A connection to physical energy.** mu_M is a measure on constraint states, not a
   physical energy quantity. It is not absorbed by thermodynamics, but it does not replace
   thermodynamics either.

3. **A source-side witness.** mu_M alone does not satisfy the E029 source-side witness
   requirement. It provides a candidate discriminator pattern (Addition 3), but that
   pattern must be tested against specific candidate systems before it can count as a witness.

4. **Independence from the constant c.** The constant `c` is not derived. Until TI
   specifies `c` from source admissibility, mu_M is a one-parameter family of sublinear
   measures, not a single well-defined field.

---

## Generalized Sublinear mu Candidate

Based on the analysis above, the productive move is to generalize mu_M beyond the Kleiber
exponent to a **sublinear issuance measure class**:

```text
mu_alpha(r) = c * |r|^alpha    where 0 < alpha < 1, c > 0
```

TI's claim, if pursued: the issuance measure mu belongs to the class of sublinear measures
(alpha < 1), not to the class of additive measures (alpha = 1) or superlinear measures
(alpha > 1).

This claim:
- Kills the generic additive reading (mu ~= cardinality)
- Kills the linear information reading
- Is not killed by entropy (entropy can be sublinear in some regimes)
- Requires a discriminator to separate from entropy at the sublinear regime
- Provides the diminishing-marginal-issuance trajectory property
- Provides the PP-3 discriminator candidate (Addition 3 above)

The specific exponent `alpha` remains unspecified by TI until derivable from source admissibility.

---

## Recommended Next Move

Formalize the sublinear mu class as a new claim candidate:

```text
TI-C021 (candidate): The issuance measure mu is subadditive in realized structure size:
mu(A union B) < mu(A) + mu(B) for all disjoint realized structures A, B with positive size.
Equivalently, the marginal issuance per new constraint is strictly decreasing in realized
structure size. This property distinguishes mu from additive and inclusion-exclusion-additive
measures (cardinality, probability, action, linear information content).
```

This claim:
- Survives absorber testing at the property level (not absorbed by any existing candidate)
- Is falsifiable: exhibit a linear or superlinear mu consistent with TI's formal object
- Provides the PP-3 discriminator candidate
- Does not require the specific exponent 3/4

Kill condition for TI-C021: if entropy's subadditivity (correlation-driven) absorbs the
size-driven subadditivity that TI requires, then the claim is absorbed and should be
filed as an entropy variant. The discriminating test: entropy's subadditivity depends on
the joint distribution; mu_M's subadditivity holds for all disjoint sets regardless of
distribution. If this difference is formal and not merely terminological, TI-C021 survives.
