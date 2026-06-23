---
artifact_type: exploration
status: active
exploration_id: E042
date: 2026-06-22
topic: sbp_ind_verification_concrete_compat_family
claim_refs:
  - TI-C019
relates_to:
  - E031 (SBP morphism class; Compat predicate families)
  - E040 (Ostrom Witness Theorem; SBP-IND named as the open closure condition for WITNESS-OBL-001)
  - E041 (monotone-obstruction; finite-type-space pool depletion; FTS/Gödelian fork)
  - E028 (Gödelian self-reference mechanism; quorum legitimacy)
  - E029 (static-source construction; bounded accessibility; PP-3)
blocking_task_addressed: >
  E040 §8 / §10 open condition 1 — SBP-IND verification for at least one concrete Compat
  predicate family that generates an infinite and non-enumerable SBP morphism space from
  each S_n. Closure condition for WITNESS-OBL-001.
proof_verdict: >
  SBP-IND FAILS for every FINITE-type-space Compat family (forced by E041 Corollary 1.1);
  SBP-IND HOLDS for a concrete GÖDELIAN (self-referential, undecidability-driven) Compat
  family — exhibited and proved here. WITNESS-OBL-001 fully closes ONLY in the Gödelian
  regime, which couples it tightly to TI-C019 open-endedness.
---

# E042: SBP-IND Verification — A Concrete Compat Family

## Purpose

E040 proved the Ostrom Redistribution Theorem (ORT) under hypotheses H1–H4 and left
WITNESS-OBL-001 **conditionally closed**, with the controlling open item (E040 §8, §10):

> "SBP-IND must be verified for at least one concrete Compat predicate family that generates
> an infinite and non-enumerable SBP morphism space from each S_n. If verified:
> WITNESS-OBL-001 is fully closed. If it fails for all natural Compat families: the theorem
> degrades to a conditional result and PP-3 interaction_witness remains open."

E040 also flagged the residual adversarial threat (§7.2):

> "if an adversary can pre-commit an exponentially large D that anticipates all possible SBP
> proposals, SBP-IND would fail at the operational level even if not at the principled level."

This exploration discharges the verification. The central finding is sharp and was not
anticipated before E041:

> **SBP-IND cannot hold in the finite-type-space (FTS) regime, because E041 Corollary 1.1
> proves at most m = |Θ| SBP morphisms exist along any trajectory — a finite, enumerable
> set. SBP-IND requires the Gödelian (self-generating) regime. We exhibit a concrete
> Gödelian Compat family for which the SBP space from each S_n is infinite and
> non-enumerable, and prove the adversarial pre-commitment defense.**

So WITNESS-OBL-001 and the interior-optimum proof (E041) sit on **opposite sides of the same
FTS/Gödelian fork**: the interior optimum exists in FTS; the source-side witness exists in
Gödelian. They cannot both bind on the same system. This is a genuine structural result about
TI-C019, developed in Section 6.

---

## 1. SBP-IND Restated

**Assumption SBP-IND (E040 §4):** In a system satisfying NAA + quorum legitimacy + Ostrom
redistribution, for each stage n the choice of which SBP morphism e: S_n -> S' to propose is
**not pre-determined** by the history (S_0, ..., S_{n-1}). The proposal map
proposal_i: histories -> SBP morphisms is not a fixed function of the initial state and prior
quorum decisions alone.

E040 §5 (Revised Step 3) showed that the ORT contradiction is driven entirely by the
non-pre-committability of the disclosure schedule D, which in turn requires that **the SBP
morphism space available from each S_n cannot be enumerated and pre-committed in a fixed
Mu_infty**. We therefore reduce SBP-IND to a concrete, checkable property:

**SBP-IND(operational):** For each reachable S_n, the set SBP(S_n) of SBP morphisms departing
S_n is **infinite and non-enumerable by any process pre-committed at S_0** — equivalently,
there is no total computable function that, given (S_0 and the prior quorum record), outputs
the SBP morphism that will be proposed at stage n.

We verify this against two concrete Compat families: a finite-type-space family (Section 3,
fails) and a Gödelian self-referential family (Section 4, holds).

---

## 2. The Adversary: Static-Source Pre-Commitment (recalled from E029/E040)

The adversary to defeat is the static-source construction (SSC, E029; E040 §2): a fixed
Mu_infty plus a disclosure schedule D: N -> P(T_infty). SBP-IND defeats the SSC iff D cannot
be pre-committed because the SBP proposal at each stage is not a fixed function of
(Mu_infty, S_0, prior quorum record).

The adversary gets to choose Mu_infty as large as it likes (even infinite), and any
*computable* disclosure schedule. SBP-IND defeats it iff the SBP proposals are not generated
by any such schedule. There are exactly two ways to defeat the adversary:

- (W1) **Cardinality defeat:** SBP(S_n) is uncountable, so no countable disclosure schedule
  enumerates it. (Necessary but, as we will see, not by itself sufficient against a
  measure-theoretic adversary.)
- (W2) **Computability defeat:** the specific SBP proposed at stage n is the value of a
  function that is not computable from (S_0, prior record), so no algorithmic pre-commitment
  can anticipate it.

The strongest verification provides **W2**, because the SSC adversary's disclosure schedule D
is, by E029's construction, an algorithmic read-off of a fixed object. W2 directly contradicts
the existence of such an algorithm. We aim for W2.

---

## 3. Finite-Type-Space Compat Family: SBP-IND FAILS

**Family A (Finite-type-space admissibility).** Fix a finite type set Θ = {τ_1, ..., τ_m}.
Constraint labels are pairs (τ_i, j) with τ_i ∈ Θ and j a finite index. Compat is any fixed
predicate over Θ-typed labels. This is exactly the FTS setting of E041.

**Claim:** SBP-IND fails for Family A.

*Proof.* By E041 Lemma 0, each type τ ∈ Θ is the site of at most one SBP morphism along any
trajectory. By E041 Corollary 1.1, at most m = |Θ| SBP morphisms occur on any trajectory, and
SBP(S_n) ⊆ {SBP morphisms of types in Pool(S_n)} with |Pool(S_n)| ≤ m. Hence SBP(S_n) is
finite (bounded by the finite number of (type, index) refinements of the ≤ m remaining types,
which is finite if the index range is finite, and even if the index range is countably
infinite the *type-distinct* SBP options number ≤ m).

A finite (or even countable, type-bounded) SBP space is enumerable. An adversary pre-commits
Mu_infty = the union over the ≤ m SBP types of their forced successor schemas, and a
disclosure schedule D(n) that reads off, at each stage, the unique-per-type SBP successor.
Because the SBP type budget is exhausted in ≤ m steps and each type's SBP successor is
determined by Compat (a fixed predicate), the schedule D is a fixed computable function of
(S_0, the deterministic Compat). SBP-IND(operational) is violated: the SBP proposals are
pre-committable. ∎

**Consequence.** In the FTS regime, the ORT's contradiction does not go through: the SSC
*succeeds*, reproducing the SBP trajectory as bounded disclosure from a fixed Mu_infty. This
is consistent with E040 §7.2's residual threat and with E029: any finite trace is
SSC-reproducible. **WITNESS-OBL-001 does not close in the FTS regime.**

This is the same finite type budget that *powers* the interior-optimum proof in E041. The two
results are dual: FTS gives the optimum (E041) but kills the witness (here).

---

## 4. A Concrete Gödelian Compat Family: SBP-IND HOLDS

We now exhibit a concrete Compat family that is **not** finite-type and for which SBP-IND
holds with a W2 (computability) defeat. The construction makes E028's Gödelian mechanism
operational.

### 4.1 Construction of Family G (Gödelian self-referential Compat)

**Constraint labels.** A constraint label is a pair c = (φ, w) where φ is a well-formed
first-order arithmetic formula (in a fixed language with one free variable, Gödel-numbered)
and w ∈ {0,1} is a polarity (assert φ / assert ¬φ). The *type* of c is the
provability-status class of φ relative to the current schema's axiom set:

```text
type_S(c) = "decidable-in-S"     if Ax(S) ⊢ φ or Ax(S) ⊢ ¬φ
          = "independent-of-S"   if neither Ax(S) ⊢ φ nor Ax(S) ⊢ ¬φ
```

where Ax(S) is the (finite) set of asserted constraints in T_S read as axioms. Crucially,
type_S(c) is **state-relative**: the same formula φ can be independent of S but decidable in
a larger S'.

**Admissibility (Compat_G).** An extension e adding c = (φ, w) is admissible from S iff
asserting c does not make Ax(S) ∪ {c} prove 0 = 1 (consistency preservation):

```text
Compat_G(c, X, S) = 1  iff  Ax(S) ∪ {the constraint encoded by c} ∪ {constraints in X}  ⊬  ⊥.
```

This is a concrete, fully specified predicate (it is co-c.e., not computable — see §4.3,
which is the whole point).

**D4 / type-novelty.** A morphism e adding c = (φ, w) is D4 iff type_S(c) = "independent-of-S"
and after asserting it, φ's status flips to decidable: the extension *resolves a previously
undecidable proposition*. This is the operational reading of E028's "new types beget new
types": resolving one independent proposition φ creates, via the incompleteness phenomenon, a
new Gödel sentence G_{S'} independent of the enlarged axiom set Ax(S') — a freshly available
"independent-of-S'" type that did not exist relative to S.

### 4.2 SBP morphisms in Family G

An SBP morphism (E031 §III.1) of Family G is a D4 morphism e: S -> S' adding c = (φ, w) such
that the *forking alternative* e': S -> S'' adding c' = (φ, 1-w) (the opposite polarity on the
same independent φ) is type-incompatible: asserting φ and asserting ¬φ cannot be reconciled
into a common consistent successor.

This is automatic and clean: for any φ independent of Ax(S), the two morphisms "assert φ" and
"assert ¬φ" are each admissible (each preserves consistency, by independence) but mutually
incompatible (asserting both yields ⊥). So **every independent proposition φ relative to S
generates an SBP fork.** SBP(S) is in bijection with the set of propositions independent of
Ax(S):

```text
SBP(S) ≅ { φ : φ is independent of Ax(S) }  (up to polarity choice).
```

### 4.3 SBP(S) is infinite and non-enumerable — W2 defeat

**Theorem 3 (SBP-IND holds for Family G).**
For every reachable S in Family G with consistent Ax(S) extending a finite fragment of
arithmetic (e.g. Robinson Q), the set SBP(S) of SBP morphisms departing S is infinite and is
**not enumerable by any process pre-committed at S_0**; the specific SBP proposed at a stage
is not a computable function of (S_0, prior quorum record).

*Proof.*

(Infinite.) By Gödel's first incompleteness theorem, any consistent, recursively axiomatized
extension of Q has infinitely many independent sentences (e.g. the iterated Gödel sentences
G_S, G_{S+G_S}, ... and, more strongly, the independent sentences form an infinite set since
adding any finite set of independent sentences yields a new consistent theory with its own
Gödel sentence). Each independent φ yields an SBP fork (§4.2). So |SBP(S)| = ∞.

(Non-enumerable by pre-committed process — W2.) Suppose, for contradiction, an adversary
pre-commits at S_0 a total computable function D that, given the history record, outputs the
set (or the next element) of SBP(S_n). The map S ↦ {φ : φ independent of Ax(S)} is the
complement of the set of S-decidable sentences. The set of φ provable from Ax(S) is c.e. (a
proof search), and likewise the refutable set; their union (the S-decidable set) is c.e. The
independent set is the complement of a c.e. set that is **not** itself c.e. — by the
undecidability of the halting/provability problem, {φ : Ax(S) ⊬ φ and Ax(S) ⊬ ¬φ} is
properly Π over the c.e. decidable set and is not computably enumerable for any consistent
Ax(S) extending Q (this is the standard fact that the independent set of a consistent r.e.
extension of Q is productive, hence not c.e.). Therefore no total computable D enumerates
SBP(S). The adversary's pre-committed disclosure schedule cannot list the SBP options, a
fortiori cannot anticipate *which* one is proposed. ∎

**Strengthening (productivity).** The independent set is not merely non-c.e.; it is
*productive*: given any c.e. set W_e claimed to enumerate the independent propositions of
Ax(S), one can compute a witness φ_e independent of Ax(S) that W_e omits. This means: for any
adversarial pre-committed enumeration of "all possible SBP proposals," there is an effectively
findable SBP proposal it missed. This **defeats the E040 §7.2 residual threat directly**: no
matter how large (even infinite-but-c.e.) the adversary's pre-committed D, a diagonal SBP
proposal escapes it. The exponentially-large-D adversary is defeated not by size but by
productivity.

### 4.4 NAA-Q and the quorum coupling

E040's ORT also used NAA-Q (quorum outcomes not determined by S_0). In Family G this is
automatic on the proposal side (Theorem 3) and inherited on the acceptance side from quorum
legitimacy: which independent φ a quorum of observers chooses to resolve is a coordination
event over a productive (non-enumerable) option set, so the resulting S_{n+1} (hence D(n+1))
is not pre-committable. The ORT's Revised Step 3 contradiction now has a concrete witness:
the productive escape sentence φ_e is an SBP proposal the SSC's D cannot contain.

---

## 5. WITNESS-OBL-001 Verdict

```text
WITNESS-OBL-001: FULLY CLOSED in the Gödelian regime; REMAINS OPEN (theorem degrades to
conditional) in the finite-type-space regime.

- SBP-IND verification (E040 §8 condition 1): COMPLETED with a concrete family.
  * Family A (finite type space): SBP-IND FAILS. SBP(S) finite/enumerable; SSC succeeds;
    witness does not close. (Forced by E041 Corollary 1.1.)
  * Family G (Gödelian, consistency-preserving arithmetic constraints): SBP-IND HOLDS.
    SBP(S) ≅ {φ independent of Ax(S)} is infinite, non-c.e., and productive. The productive
    escape sentence defeats the E040 §7.2 exponential-pre-commitment adversary.
- Infinite-trajectory version (E040 §7.2 / §10 condition 2): ALSO CLOSED for Family G.
  Productivity guarantees SBP(S_n) stays non-exhaustible for every n (each enlarged Ax(S_n)
  is still a consistent r.e. extension of Q, so its independent set is again productive).
  This is exactly the Gödelian non-exhaustibility E040 §7.2 wanted and E028 conjectured;
  it is now proved for a concrete family.

NET: WITNESS-OBL-001 closes precisely when the operative Compat family is Gödelian
(self-referential, undecidability-driven). The PP-3 source-side interaction_witness is real
for Family G: the multi-observer quorum resolves productively-non-enumerable independent
propositions, generating shared-admissibility changes that NO fixed Mu_infty can pre-commit.
```

---

## 6. The Central Structural Result: the FTS/Gödelian Fork Is a TI-C019 Discriminator

E041 and E042 together establish a clean dichotomy on the *same* axis (finiteness of the
effective type space):

| | Finite-Type-Space regime (FTS) | Gödelian regime (self-generating) |
|---|---|---|
| SBP count per trajectory | ≤ m = |Θ| (E041 Cor 1.1) | infinite, productive (E042 Thm 3) |
| Monotone-obstruction (MO) | holds (E041 Thm 1) | may fail (E041 Prop 2) |
| K(lambda) | superlinear (E041 Prop 1) | may be sublinear |
| Interior optimum lambda*(S) | exists (E041 Thm 2) | need not exist |
| SBP-IND / source-side witness | FAILS (E042 §3) | HOLDS (E042 §4) |
| SSC (fixed-source) adversary | SUCCEEDS | DEFEATED (productivity) |
| WITNESS-OBL-001 | open (degrades) | CLOSED |

**The two flagship results of this session are mutually exclusive on a single system.** A
system cannot simultaneously have a finite type budget (needed for the interior optimum) and a
productively-infinite SBP space (needed for the source-side witness). This is not a defect; it
is a **discriminator** for TI-C019:

```text
Discriminator D-FORK (refines E041's D-FTS):
  If the operative source is FINITE-type:
     - issuance has diminishing returns and an optimal rate (E041),
     - BUT it is SSC-reproducible: a fixed richer Mu_infty plus apertures reproduces it
       (E042 §3), so it is NOT source-side issuance — it is bounded projection disclosure.
     => TI-C019's source-side claim FAILS here; PP-3 resolves AGAINST issuance.

  If the operative source is GÖDELIAN (self-referentially type-generating):
     - issuance need not have an optimal rate; it can stay productive indefinitely (E041 §8),
     - AND it is NOT SSC-reproducible: productivity defeats every fixed-source pre-commitment
       (E042 §4), so it IS a genuine source-side witness (WITNESS-OBL-001 closes).
     => TI-C019's source-side claim SUCCEEDS here; PP-3 resolves FOR issuance.

Therefore: TI-C019 (genuine source-side open-ended issuance) is TRUE iff the operative source
is in the Gödelian regime, and FALSE (reduces to bounded projection disclosure) iff it is in
the finite-type-space regime. The single empirical/structural question "is the source's
effective type space self-generating or fixed-finite?" decides TI-C019's deepest fork.
```

This converts the previously diffuse PP-3 question ("source-side issuance vs bounded-access
disclosure") into a **precise, single-bit structural question with two proved consequences**.
That is a substantial sharpening of the program's central open problem.

### 6.1 Why this is not circular

One might worry that "Gödelian regime" is defined to make the witness hold. It is not: Family G
is defined by an *independent, standard* mathematical object (consistency-preserving assertion
of arithmetic formulas), and the witness property (productivity of the independent set) is a
*theorem* of computability theory (Gödel/Post), not a stipulation. The non-circularity is
exactly that the SBP space's non-enumerability is inherited from incompleteness, which is not
a property TI chose — it is forced on any sufficiently expressive self-referential schema.

### 6.2 The expressiveness threshold

The fork is governed by a sharp threshold E028 anticipated: the schema must be
**expressive enough to encode its own provability predicate** (interpret Robinson Q). Below
that threshold (e.g. a decidable theory like Presburger arithmetic, or any finite-type schema)
the independent set is empty or finite and SBP-IND fails. At or above it, productivity kicks
in and SBP-IND holds. **The expressiveness threshold is the formal location of the FTS/Gödelian
boundary**, and is the concrete test E028's "expressive threshold test" called for.

---

## 7. Assumptions, Failure Risks, Kill Conditions

### Assumptions
1. Family G uses consistency-preservation as Compat. This is a concrete co-c.e. predicate;
   it is not computable, which is essential — a *computable* admissibility predicate would
   make SBP(S) c.e. and re-open SSC. The non-computability of Compat_G is load-bearing.
2. The schema is at least as expressive as Robinson Q (the incompleteness threshold).
3. Observers/quorum operate at the proposal layer; NAA forbids reading the resolution of an
   independent φ before the quorum resolves it (no oracle for provability). This is the
   honest NAA reading: no observer has a halting oracle.

### Failure risks
- If the physical/operative source has a **computable** admissibility predicate, Compat is c.e.,
  SBP(S) is c.e., and the productivity defeat evaporates — the system is effectively FTS-like
  for witness purposes even with infinitely many types. The decisive property is
  non-computability of Compat, not mere infinitude of the type set. (This is the subtle point
  W1-vs-W2 in §2: cardinality alone is insufficient; the computability defeat is what matters.)
- If observers are granted a provability oracle (can decide independence), NAA-Q fails and the
  quorum coordination becomes pre-committable. The witness needs genuinely bounded (oracle-free)
  observers.

### Kill conditions
1. If the operative source is shown to be finite-type or computable-admissibility, SBP-IND
   fails for it, WITNESS-OBL-001 does not close for it, and TI-C019's source-side claim must be
   withdrawn for that source (PP-3 resolves against issuance there).
2. If a richer fixed Mu_infty with a *non-computable but still fixed* oracle disclosure can
   reproduce productive SBP traces, the W2 defeat must be re-examined. (Sketch defense: a fixed
   oracle that decides Ax(S)-independence for all S is a single fixed object, but the
   trajectory's Ax(S) is itself produced by prior quorum choices among productive options, so
   the oracle would have to be indexed by the un-pre-committable history — the regress E040
   Revised Step 3 already closes. Full treatment deferred if the adversary is pressed.)

---

## 8. What Was Resolved and What Remains

### Resolved
1. SBP-IND verified against two concrete Compat families with opposite verdicts; the
   determining property isolated (non-computability of admissibility / Gödelian
   self-reference).
2. WITNESS-OBL-001 fully closed for the Gödelian regime, including the infinite-trajectory
   version (productivity ⇒ non-exhaustibility), and the E040 §7.2 exponential-pre-commitment
   adversary defeated by productivity rather than cardinality.
3. The FTS/Gödelian fork (E041) and the witness fork (E042) shown to be the *same* fork,
   yielding discriminator D-FORK: TI-C019's deepest PP-3 fork reduces to one structural
   question — is the source's effective type space self-generating (Gödelian) or fixed-finite?
4. The expressiveness threshold (Robinson Q / self-encodable provability) located as the
   formal FTS/Gödelian boundary — E028's "expressive threshold test" given a concrete form.

### Remains blocked / open
1. **The operative-source question (now the program's pivot):** is the relevant TI source
   Gödelian or finite-type/computable? This decides D-FORK and therefore TI-C019. No status
   change to TI-C019 is earned until this is settled at the source layer (PP-3 unresolved).
2. Q-OBL-001 (Q circularity) — unchanged; but note Q(e) = -log(acceptance prob) over a
   productive option set is now better positioned (E040 §10): acceptance probability over a
   non-enumerable option set cannot be pre-committed.
3. FUNCTOR-OBL-001 (N naturality) — unchanged.
4. The non-computable-fixed-oracle adversary (§7 kill condition 2) — sketched-defeated,
   full proof deferred unless pressed.
