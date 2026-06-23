---
artifact_type: exploration
status: active
exploration_id: E045
date: 2026-06-22
topic: d_fork_synthesis_interior_optimum_verdict
claim_refs:
  - TI-C019
  - TI-C021
  - TI-C022
relates_to:
  - E041 (monotone-obstruction; interior optimum under FTS; D-FTS)
  - E042 (SBP-IND; WITNESS-OBL-001 closure in Gödelian regime; D-FORK)
  - E043 (TI-C021 entropy discriminator; SAX; D-RATE narrowed)
  - E044 (TI-C022 BFT/TCB discriminator; permanent-fork; ontological fork-choice)
  - E028 (Gödelian mechanism; expressive threshold)
  - E029 (static-source / aperture; PP-3)
governance_note: >
  Synthesis exploration for RUN-0048. Collects the cross-cutting structural result that
  emerged from E041–E044 (the FTS/Gödelian fork as the single axis governing the interior
  optimum, the source-side witness, mu subadditivity, and the PP-3 fork), states the interior
  optimum verdict, and frames the program pivot. No claim promotion.
---

# E045: D-FORK — The Finite/Gödelian Axis as the Program Pivot

## Purpose

E041–E044 each discharged a named blocking obligation. This synthesis records the result that
was not visible from any single one: **four previously separate questions are governed by a
single structural axis** — whether the operative source's effective type space is
finite (FTS) or self-generating (Gödelian). This axis (D-FORK) reorganizes the program's open
problems and is the highest-value finding of RUN-0048.

---

## 1. The Four Results and Their Shared Axis

| # | Obligation (origin) | Result | Regime where it holds |
|---|---|---|---|
| E041 | Monotone-obstruction / interior optimum (E039 §11.1) | MO proved; interior optimum lambda*(S) exists | **FTS** (finite type space) |
| E042 | SBP-IND / WITNESS-OBL-001 closure (E040 §10.1) | SBP-IND holds; witness closes; SSC defeated by productivity | **Gödelian** (self-generating) |
| E043 | TI-C021 entropy discriminator (ledger next_action) | Size-subadditivity ≠ entropy subadditivity; TI-C021 survives | mu strictly subadditive in **FTS**; not asserted in Gödelian |
| E044 | TI-C022 BFT/TCB discriminator (ledger next_action) | Permanent-fork case; TI-C022 survives | discriminator lives at the **fork** (the boundary event) |

The first three are each pinned to one side of the FTS/Gödelian fork; the fourth lives at the
fork itself (the SBP fork is the boundary event whose resolution-or-not decides record
genuineness). **The fork is the organizing object.**

## 2. D-FORK Stated

```text
Discriminator D-FORK (the program pivot):

Let the operative TI source have effective type space Θ_eff (the set of constraint types the
source can ever instantiate). Exactly one of:

(I) FINITE regime:  |Θ_eff| < ∞ (equivalently: the source's admissibility predicate is
    computable / below the incompleteness threshold).
    THEN, proved this session:
      - issuance has diminishing marginal returns (E043 SAX; E041 pool depletion),
      - an optimal issuance rate lambda*(S) exists (E041 Thm 2),
      - mu is strictly size-subadditive (E043),
      - BUT the trajectory is SSC-reproducible: a fixed richer Mu_infty + apertures reproduces
        it (E042 §3), so it is bounded PROJECTION DISCLOSURE, not source-side issuance.
      ⇒ PP-3 resolves AGAINST source-side issuance. TI-C019's deepest claim FAILS here.

(II) GÖDELIAN regime:  Θ_eff self-generates (source admissibility is non-computable;
    at/above the Robinson-Q incompleteness threshold; new types beget new types, E028).
    THEN, proved this session:
      - the SBP space is infinite, non-c.e., productive (E042 Thm 3),
      - the source-side witness closes; SSC defeated by productivity (E042),
      - issuance need NOT have an optimal rate; openness can be sustained (E041 §8),
      - mu need NOT be strictly subadditive (sustained marginal issuance, E043 §6),
      - the interior optimum need NOT exist (E041 Prop 2).
      ⇒ PP-3 resolves FOR source-side issuance. TI-C019's deepest claim SUCCEEDS here.

THEREFORE: TI-C019 (genuine source-side open-ended issuance) is TRUE iff the operative source
is Gödelian, and reduces to bounded projection disclosure iff it is finite. The entire PP-3
fork — the deepest unresolved question in the program (CLAIM-LEDGER TI-C019 objection) — is
equivalent to the single structural question:

      Is the operative source's effective type space self-generating or fixed-finite?
```

This is a strict sharpening. Before RUN-0048, PP-3 was "is D4 source-side or projection?", a
diffuse question with no decision procedure. After RUN-0048, it is a single structural bit with
two fully-proved, mutually exclusive consequence-sets. The program's central problem now has a
crisp form and a clear test target (the expressiveness threshold, E042 §6.2).

## 3. The Interior-Optimum Existence Verdict

```text
INTERIOR OPTIMUM lambda*(S):  status history:
  E031: existence CONDITIONAL on IA.
  E039: IA killed; existence CONDITIONAL on unproven monotone-obstruction.
  E041 (this session): existence PROVED conditional on FTS + type-fairness + C-convexity.
  E045 (this synthesis): existence is now understood as a REGIME PROPERTY:
     - exists in the FINITE regime (E041 Thm 2),
     - does NOT generally exist in the GÖDELIAN regime (E041 Prop 2),
     - and its NON-existence is the formal SIGNATURE of genuine open-endedness (TI-C019).

The interior optimum question is therefore RESOLVED at the structural level: lambda*(S) is not
a universal feature of TI systems; it is the finite-regime feature, and its absence marks the
open-ended (Gödelian) regime. lambda*(S) is NOT admitted as a TI claim (it remains absorbed by
optimal control per E034 in the finite regime; it is absent in the Gödelian regime). What is
admitted is the structural understanding of WHEN it exists and what its (non-)existence means.
```

## 4. Why This Is Coherent, Not a Patchwork

The four results are not independently bolted together; they share one mechanism:
**finite-novel-type-pool depletion vs. productive self-generation.**

- E041's interior optimum is driven by pool depletion (Lemma 1): finite pool ⇒ diminishing N
  and rising K ⇒ optimum.
- E043's mu subadditivity is the *measure-level shadow* of the same depletion (E043 §6): finite
  pool ⇒ diminishing marginal issuance ⇒ strictly concave mu.
- E042's witness is the *negation* of depletion: productive (Gödelian) pool ⇒ non-enumerable SBP
  space ⇒ SSC defeated.
- E044's permanent fork is a depletion-vs-generation event at the boundary: an SBP fork is the
  atomic site where the schema either resolves (one branch becomes canonical, continuing the
  shared process) or permanently splits (neither branch is genuine).

A single concept — does the source spend a finite novelty budget, or regenerate it? — drives
all four. That is why D-FORK is a genuine structural result and not a coincidence of four
separate proofs.

## 5. Program Pivot and Next Targets

The pivot: **the program's central effort should now be to determine whether the operative TI
source is finite or Gödelian** — equivalently, whether the source's effective admissibility is
below or at/above the incompleteness (self-encoded-provability) threshold (E042 §6.2). This is
the concrete form of E028's "expressive threshold test" and the resolution path for PP-3.

Concrete next moves (priority order):
1. **Expressiveness-threshold fixture:** specify what it would take for the *physical/operative*
   source to encode its own admissibility predicate (the Robinson-Q analog). If it can, it is
   Gödelian (TI-C019 succeeds); if it provably cannot, it is finite (TI-C019 reduces to
   projection). This is the single highest-value next run.
2. **Non-computable-fixed-oracle adversary (E042 §7 kill-condition 2):** complete the defense
   that a fixed non-computable oracle cannot reproduce productive SBP traces, since Ax(S) is
   itself produced by un-pre-committable quorum choices.
3. **Continuity predicate formalization (E044 §7):** state TI-C022's shared-process-continuity
   predicate as an order-theoretic (clock-free) liveness-class condition and test reduction to
   eventual-synchrony liveness.
4. **FUNCTOR-OBL-001 and Q-OBL-001:** still open; both are now better positioned (Q over a
   productive option set cannot be pre-committed, E042 §8).

## 6. What RUN-0048 Did and Did Not Earn

**Earned:**
- Four named blocking obligations discharged (monotone-obstruction; SBP-IND/WITNESS-OBL-001 in
  the Gödelian regime; TI-C021 entropy non-absorption; TI-C022 BFT/TCB non-absorption).
- Interior optimum existence resolved as a regime property.
- The PP-3 fork collapsed to a single structural bit (D-FORK) with proved consequence-sets.
- Two standing strongest objections defeated (entropy absorber for TI-C021; BFT/TCB absorber
  for TI-C022).
- One honest narrowing (D-RATE demoted to a consistency check, E043 §7).

**NOT earned (no promotion):**
- No claim promoted. TI-C019 remains formalizing; TI-C021 and TI-C022 remain speculative
  (promotion requires hostile review per CLAIM-LEDGER governance).
- The operative-source question (FTS vs Gödelian) is NOT resolved — it is *sharpened to a single
  bit*. Until it is settled at the source layer, PP-3 is open and TI-C019's deepest claim is
  undecided.
- lambda*(S) is NOT admitted as a TI claim.

The session moved the hypothesis toward being *decidable*: the deepest fork now has a crisp
form and a clear test. That is the methodologically correct kind of progress (METHOD.md:
"traceable learning that moves the hypothesis toward being killed, absorbed, narrowed,
formalized, tested, promoted, or archived") — here, **formalized and narrowed to a single
testable structural question.**
