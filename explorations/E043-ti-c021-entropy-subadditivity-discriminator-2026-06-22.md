---
artifact_type: exploration
status: active
exploration_id: E043
date: 2026-06-22
topic: ti_c021_entropy_subadditivity_discriminator
claim_refs:
  - TI-C021
  - TI-C019
  - TI-C003
relates_to:
  - E035 (mu_M specification; subadditivity property first isolated)
  - E036 (sublinear mu discriminator; three additions; PP-3 discriminator candidate)
  - E040 (Ostrom Witness Theorem; PP-3 source-side backing for the rate discriminator)
  - E041 (finite-pool depletion as the structural cause of diminishing marginal issuance)
  - E029 (static-source / aperture model; PP-3 adversary)
blocking_task_addressed: >
  TI-C021 next_action (CLAIM-LEDGER): run the entropy-subadditivity discriminator — test
  whether correlation-driven Shannon entropy subadditivity absorbs size-driven mu
  subadditivity. If not absorbed: formalize TI-C021 and add the PP-3 rate discriminator.
proof_verdict: >
  NOT ABSORBED. Size-driven subadditivity and correlation-driven subadditivity are
  formally distinct (proved via the Disjoint-Independent Discriminator). TI-C021 survives
  the entropy absorber; formalized; PP-3 rate discriminator now backed by E040/E041.
---

# E043: The Entropy-Subadditivity Discriminator for TI-C021

## Purpose

TI-C021 claims the issuance measure mu is **size-driven subadditive**:
mu(A ∪ B) < mu(A) + mu(B) for all disjoint realized structures A, B with positive size.
The standing strongest objection (CLAIM-LEDGER, E036) is the entropy absorber:

> Shannon entropy is subadditive: H(X, Y) ≤ H(X) + H(Y). If entropy's subadditivity is the
> same formal property as TI-C021's, then TI-C021 is absorbed as an entropy variant.

The named discriminating test (CLAIM-LEDGER next_action):

> entropy subadditivity depends on joint distribution; TI-C021 subadditivity holds for all
> disjoint sets regardless of distribution. This test has not been run.

This exploration runs it. It:
1. States both subadditivity properties precisely as predicates over a common domain
   (Section 2).
2. Proves they are formally distinct via the Disjoint-Independent Discriminator: a case
   where entropy subadditivity is an *equality* (no deficit) but mu subadditivity is *strict*
   (Section 3).
3. Proves the converse separation: a case where entropy subadditivity is strict but reflects
   pure correlation with no size effect, which mu subadditivity does not register (Section 4).
4. Establishes the formal-content surplus of size-driven subadditivity over the entropy
   absorber (Section 5).
5. Formalizes TI-C021 with the now-justified subadditivity axiom and ties the diminishing
   marginal issuance to the E041 finite-pool depletion mechanism (Section 6).
6. Runs the PP-3 rate discriminator (size-dependent vs aperture-dependent rate), now backed
   by the E040 ORT and the E041/E042 fork (Section 7).
7. Records the verdict and remaining open items (Sections 8-9).

---

## 1. The Two Candidate Absorbers and Why Only Entropy Is Live

E036's table of mu candidates: cardinality, action, probability, and linear information are
**additive or inclusion-exclusion additive** — none is subadditive, so none can absorb a
subadditivity claim. The only named measure that *is* subadditive is **Shannon entropy**
(joint entropy is subadditive). So the entropy absorber is the sole live threat to TI-C021,
and the whole verdict turns on whether entropy subadditivity = size-driven subadditivity.

Bekenstein bound (E036) is a linear bound, not a subadditive measure; it is checked
case-by-case and does not produce a generic strict subadditivity, so it is not the absorber.

---

## 2. Two Subadditivity Predicates on a Common Domain

To compare formally, both properties must be predicates over the *same* objects. Let the
common domain be pairs (A, B) of disjoint finite realized structures, where each structure
carries (i) a size |·| ∈ ℕ_{>0} and (ii) optionally a probability law making it a random
object. Define two predicates.

**P_size (size-driven subadditivity).** A measure ν satisfies P_size iff
```text
for all disjoint A, B with |A|, |B| > 0:   ν(A ∪ B) < ν(A) + ν(B),
```
where ν depends on the structure *only through its size*: ν(A) = g(|A|) for some g.
For the sublinear class ν = mu_alpha, g(s) = c·s^alpha with 0 < alpha < 1, and P_size holds
because s ↦ s^alpha is strictly concave with g(0) = 0:
(|A|+|B|)^alpha < |A|^alpha + |B|^alpha for all |A|,|B| > 0. (Strict subadditivity of a
strictly-concave-through-origin function.)

**P_corr (correlation-driven subadditivity).** A measure ν (here ν = H, Shannon entropy of
the law of a structure) satisfies P_corr on (A, B) iff
```text
H(A, B) ≤ H(A) + H(B),   with equality iff A ⟂ B (statistically independent),
```
and the deficit is exactly the mutual information: H(A)+H(B) − H(A,B) = I(A; B) ≥ 0.

These are the two predicates the absorption question pits against each other. The CLAIM-LEDGER
intuition is that P_size and P_corr differ in their dependence on the joint law. We make that
exact.

---

## 3. The Disjoint-Independent Discriminator (entropy deficit = 0, mu deficit > 0)

**Discriminator construction.** Take A and B to be **disjoint and statistically independent**
realized structures, each of positive size, with nondegenerate laws. Examples: A = a fresh
constraint block sampled independently of B; or, in the bit picture, A = k_A independent fair
bits, B = k_B independent fair bits, A ⟂ B.

**Entropy on (A, B):** Because A ⟂ B, mutual information I(A; B) = 0, so
```text
H(A, B) = H(A) + H(B)     — entropy subadditivity holds with EQUALITY. Deficit = 0.
```
P_corr's subadditivity is **vacuous** here: there is no strict subadditivity, because there is
no correlation to drive it.

**mu on (A, B):** With ν = mu_alpha, ν(A) = c·k_A^alpha, ν(B) = c·k_B^alpha, and
```text
mu_alpha(A ∪ B) = c·(k_A + k_B)^alpha < c·k_A^alpha + c·k_B^alpha = mu_alpha(A) + mu_alpha(B).
                                                          — STRICT subadditivity. Deficit > 0.
```
P_size's subadditivity is **strict** here, with deficit
c·(k_A^alpha + k_B^alpha − (k_A+k_B)^alpha) > 0.

**Conclusion (Theorem 4 — Separation, direction 1).**
On the class of disjoint *independent* structures, entropy subadditivity is identically an
equality (deficit 0) while mu_alpha subadditivity is strict (deficit > 0). Therefore P_corr
and P_size are **not the same predicate**: they disagree on an entire nonempty class of inputs.
Entropy cannot absorb size-driven subadditivity, because the size-driven deficit persists
exactly where the entropy deficit vanishes. ∎

This is the precise sense in which "entropy subadditivity depends on the joint distribution"
(it needs I(A;B) > 0) while "TI-C021 subadditivity holds regardless of distribution" (it needs
only |A|,|B| > 0). The discriminator is the **independent** case, where distribution-dependence
zeroes out the entropy effect but not the size effect.

---

## 4. The Converse Separation (entropy deficit > 0, mu deficit = 0)

To confirm the predicates are genuinely orthogonal (not merely one implying the other), we
show the reverse failure: a case with strict entropy subadditivity but **zero** size-driven
subadditivity.

**Construction.** Let A and B be **maximally correlated** structures of the *same fixed size*
that we hold constant — e.g. A and B are two copies of the same k-bit source with a strong
dependence, I(A; B) > 0, but consider the size functional held at a fixed total (a "size-blind"
or additive baseline measure ν_add = cardinality, alpha = 1).

**Entropy:** I(A; B) > 0, so H(A, B) = H(A) + H(B) − I(A; B) < H(A) + H(B). Strict entropy
subadditivity, deficit = I(A;B) > 0.

**Size measure with alpha = 1 (additive baseline):** ν_add(A ∪ B) = |A| + |B| =
ν_add(A) + ν_add(B). Deficit = 0 — no subadditivity. (And for any genuinely additive measure,
correlation is invisible: cardinality does not see the dependence between A and B.)

**Conclusion (Theorem 4 — Separation, direction 2).**
Correlation produces a strict *entropy* deficit that an additive size measure does not register
at all. So P_corr can be strict where P_size (at alpha=1) is null. Combined with Section 3
(P_size strict where P_corr is null), the two predicates are **logically independent**: neither
implies the other. ∎

The two subadditivities are therefore measuring different things: P_corr measures *shared
information between A and B*; P_size measures *concavity of the measure in total size*. They
coincide numerically only by coincidence of parameters, never as the same formal property.

---

## 5. The Formal Surplus of Size-Driven Subadditivity

Sections 3–4 establish non-absorption. We now state precisely what TI-C021 contributes that the
entropy absorber does not, to satisfy the absorption discipline (METHOD.md):

| Property | Entropy (P_corr) | mu_alpha (P_size) |
|---|---|---|
| Deficit source | mutual information I(A;B) | concavity gap c(|A|^α+|B|^α−(|A|+|B|)^α) |
| Holds for disjoint **independent** A,B | NO (equality) | YES (strict) |
| Holds **regardless of any distribution** | NO (needs a law + dependence) | YES (size only) |
| Marginal increment per unit | distribution-dependent | (deterministic) ~ α·c·s^{α−1}, strictly decreasing |
| Absorbs the other | NO (Thm 4 dir. 2) | NO (Thm 4 dir. 1) |

- **Surplus 1 (distribution-freeness):** P_size is a property of the *functional form on sizes*,
  invariant under all relabelings and all probability laws. Entropy has no such invariant
  subadditivity. This is genuinely new structure on the issuance measure: TI-C021 says mu is
  concave-in-size as a *measure-theoretic* fact, not a statistical one.
- **Surplus 2 (deterministic diminishing marginal issuance):** the marginal increment
  Δmu(s) = c((s+1)^α − s^α) ~ α c s^{α−1} → 0 is a deterministic, size-only trajectory
  prediction (E036 Addition 2). Entropy's marginal is distribution-bound.
- **Surplus 3 (PP-3 rate discriminator):** developed in Section 7.

**Category-error check (METHOD.md):** TI-C021 is a claim about a *measure on realized
constraint structure*, not about the *information content of a random variable*. Conflating
them is precisely the category error the discriminator exposes: entropy lives on the law of a
random object; mu lives on the realized structure's size. They are different categories, and
the Disjoint-Independent Discriminator is the test that keeps them separate.

---

## 6. Formalizing TI-C021

With non-absorption established, TI-C021's subadditivity is admitted as a formal axiom on the
issuance measure (still **speculative** as a claim about reality; the formalization is of the
*property*, not a promotion).

**TI-C021 Subadditivity Axiom (SAX).** The issuance measure mu: R → ℝ_{≥0} on realized
structures satisfies:
- (SAX-0) mu(∅) = 0;
- (SAX-1, monotone) A ⊆ B ⇒ mu(A) ≤ mu(B);
- (SAX-2, strict size-subadditivity) for disjoint A, B with |A|, |B| > 0:
  mu(A ∪ B) < mu(A) + mu(B);
- (SAX-3, size-determined) mu(A) = g(|A|) for a strictly concave g with g(0) = 0
  (the canonical realization is g(s) = c·s^α, 0 < α < 1; α, c unspecified by TI).

**Proposition 3 (SAX characterizes the sublinear class up to the size functional).**
A size-determined measure mu(A) = g(|A|) satisfies (SAX-2) for all disjoint positive-size A, B
iff g is strictly subadditive on ℕ_{>0}, which (with g(0)=0, monotone) holds iff g is strictly
concave through the origin. Power laws s^α (0<α<1) are the scale-free members of this class.
*Proof.* Strict subadditivity of g through the origin is equivalent to strict concavity for
monotone g with g(0)=0 by the standard concave-subadditive equivalence; scale-invariance
g(λs)=λ^α g(s) singles out power laws. ∎

**Tie to E041 (structural cause of diminishing returns).** E041 Lemma 1 proved that under FTS
the novel-type pool strictly depletes by one per SBP step, so the marginal novelty per step
strictly decreases. SAX-3's diminishing marginal increment α·c·s^{α−1} is the *measure-level
shadow* of that *category-level* depletion: as realized structure grows, fewer novel types
remain, so each new constraint contributes less issuance. **TI-C021 (measure level) and E041
(morphism level) are the same diminishing-returns phenomenon described in two layers.** This
coherence is new evidence that SAX is not an arbitrary functional choice — it is forced by the
finite-pool structure whenever the source is in the FTS regime.

**Regime caveat (from E041/E042).** SAX-2/SAX-3 are the **FTS-regime** signature. In the
Gödelian regime (E042), the novel-type pool replenishes, so marginal issuance need *not*
decline and mu need not be strictly concave-in-size. Therefore:
```text
TI-C021 (strict size-subadditive, diminishing marginal mu)  ⇔  FTS regime.
Gödelian regime  ⇒  mu may be linear-or-non-concave in size (sustained marginal issuance).
```
This is consistent with — and sharpens — the D-FORK discriminator of E042: the same fork that
governs the witness and the interior optimum also governs whether mu is strictly subadditive.

---

## 7. The PP-3 Rate Discriminator (now backed by E040/E041/E042)

E036 Addition 3 proposed a PP-3 discriminator: source-side issuance has a **size-dependent**
declining rate, while projection-layer aperture disclosure has an **aperture-dependent** rate.
Previously this was a bare proposal. We now state it as a test with backing.

**Discriminator D-RATE.**
```text
Source-side issuance (FTS, TI-C021):   d(mu)/d(|r|) ~ α c |r|^{α−1}, a function of SIZE |r|.
Projection disclosure (E029 SSC):      rate = d(aperture P_n)/dt, a function of the APERTURE
                                       schedule, independent of realized size |r|.
```
A system whose issuance rate declines as a function of realized structure size |r|,
*independent of any aperture-growth schedule*, cannot be the SSC of E029: the SSC's disclosure
rate is set by the (externally chosen) aperture schedule D, which is not tied to |r|. Matching
|r|^{α−1} with an aperture schedule requires the adversary to *pre-tune* aperture growth to
track |r|^{α−1} — an unexplained coincidence (E036), and now provably more than a coincidence:

**Backing from E040/E041/E042.**
- E041 shows the size-dependent declining rate has a *mechanism* (finite-pool depletion),
  so it is not an arbitrary fit: in the FTS regime the declining rate is forced.
- BUT E042 shows the FTS regime is exactly where the SSC *succeeds* (SBP-IND fails). So in the
  FTS regime, the adversary *can* reproduce the trajectory — and indeed can reproduce the
  size-dependent rate by choosing the aperture schedule to be the disclosure of the depleting
  pool. **D-RATE does NOT discriminate in the FTS regime.** This is a correction to E036
  Addition 3: in FTS, the aperture adversary can match |r|^{α−1} because the pool depletion IS
  the aperture schedule.
- Conversely, in the **Gödelian regime** (E042), mu need not be subadditive (Section 6 caveat),
  so D-RATE's size-dependent declining-rate signature is *absent* — but there the *witness*
  (D-FORK / WITNESS-OBL-001) does the discriminating work instead, via productivity.

**Net verdict on D-RATE.** The rate discriminator is **weaker than E036 hoped**: in FTS it is
absorbed by an aperture schedule tracking pool depletion; in Gödelian it does not apply.
D-RATE is therefore demoted from "PP-3 discriminator" to "consistency check": a size-dependent
declining rate is *consistent with* FTS source-side structure but does not *distinguish* it
from aperture disclosure, because in FTS the two coincide. The genuine PP-3 discriminator is
D-FORK (E042: productivity / non-enumerability of the SBP space), not the rate. This is an
honest narrowing, recorded as a correction.

---

## 8. Verdict

```text
TI-C021 ENTROPY-SUBADDITIVITY DISCRIMINATOR: RUN. Verdict: NOT ABSORBED.

- Size-driven subadditivity (P_size) and correlation-driven entropy subadditivity (P_corr)
  are formally distinct and logically independent (Theorem 4, both directions):
  * P_size strict where P_corr is null (disjoint independent A,B): Section 3.
  * P_corr strict where P_size is null (additive baseline, correlated A,B): Section 4.
- Entropy does NOT absorb TI-C021. The size-driven deficit is a concavity-of-the-size-functional
  property, invariant under all distributions; the entropy deficit is mutual information,
  requiring a law and dependence. Different categories (measure-on-structure vs information-of-law).
- TI-C021 formalized as the Subadditivity Axiom (SAX); the sublinear power-law class is
  characterized (Proposition 3); diminishing marginal issuance tied to E041 finite-pool
  depletion as its structural cause.
- PP-3 rate discriminator (D-RATE) HONESTLY NARROWED: in FTS the aperture adversary matches
  the size-dependent rate (pool depletion = aperture schedule), so D-RATE does not discriminate;
  in Gödelian it does not apply. The genuine PP-3 discriminator is D-FORK (E042), not the rate.

CLAIM EFFECT (TI-C021): status stays SPECULATIVE (promotion needs hostile review), but the
standing strongest objection (entropy absorber) is DEFEATED. The claim's surviving content is
sharpened to the distribution-free size-concavity property, and its regime is pinned to FTS.
The next_action changes from "run entropy discriminator" (now done) to "determine the operative
regime (FTS vs Gödelian) via D-FORK," merging TI-C021's open question into the program pivot.
```

---

## 9. Assumptions, Failure Risks, Kill Conditions

### Assumptions
1. The entropy absorber means Shannon (or thermodynamic) entropy with the standard joint-entropy
   subadditivity H(A,B) ≤ H(A)+H(B), deficit = I(A;B). This is the only subadditive named
   absorber (Section 1).
2. mu is size-determined (SAX-3) in the regime where TI-C021 is asserted (FTS). Outside FTS the
   claim is explicitly not asserted (Section 6 caveat).

### Failure risks
1. If a non-Shannon subadditive measure exists in TI's absorber set that *is* distribution-free
   and size-concave, it could absorb TI-C021 after all. No such measure is currently named;
   if one appears (e.g. a Rényi or Tsallis variant with size-concavity), re-run the discriminator
   against it specifically.
2. The D-RATE narrowing (Section 7) depends on the FTS aperture-schedule equivalence; if a
   source-side rate signature survives that does NOT reduce to aperture disclosure, D-RATE could
   be partially restored. Flagged but not expected.

### Kill conditions
1. If size-driven subadditivity is shown to be a *special case* of entropy subadditivity under
   some encoding (e.g. mu = entropy of a size-induced distribution with built-in concavity),
   TI-C021 absorbs into the information-theory entry. The discriminator's direction-1 separation
   (Section 3) blocks this: no such encoding can produce a strict deficit on independent inputs
   where entropy's deficit is forced to zero. So this kill is currently closed.
2. If the operative source is Gödelian (E042), SAX-2/SAX-3 are not asserted, and TI-C021's
   subadditivity claim does not apply to it (correctly — that regime has sustained marginal
   issuance). TI-C021 then narrows to "the FTS sublinear measure class," a conditional claim.

### Effect on other claims
- **TI-C003:** the subadditivity requirement on mu (E036) is now a *justified* formal constraint
  (not absorbed by entropy), partially sharpening the mu placeholder as E036 hoped. mu must be
  distribution-free size-concave to satisfy TI-C021 — a genuine narrowing of the candidate space.
- **TI-C019:** TI-C021's regime-pinning to FTS, and its merge into D-FORK, add measure-level
  evidence to the same FTS/Gödelian fork that governs the witness and the optimum. No status
  change.
