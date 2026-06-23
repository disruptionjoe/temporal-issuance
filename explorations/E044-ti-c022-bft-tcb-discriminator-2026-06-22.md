---
artifact_type: exploration
status: active
exploration_id: E044
date: 2026-06-22
topic: ti_c022_bft_tcb_discriminator
claim_refs:
  - TI-C022
  - TI-C019
relates_to:
  - E037 (kill-criteria test; TI-C022 ontological version first isolated)
  - E040 (Ostrom Witness Theorem; quorum legitimacy; SBP fork)
  - E042 (Gödelian SBP space; fork-choice over productive option set)
  - E028 (quorum legitimacy condition; AC-8 adversarial model)
  - absorbers/crypto-economic-security.md (Absorber 2: BFT / accountable safety)
  - absorbers/distributed-systems.md
blocking_task_addressed: >
  TI-C022 next_action (CLAIM-LEDGER): run the BFT/TCB discriminator — construct a case where
  BFT guarantees record integrity but TI-C022's ontological condition is not satisfied
  (e.g., permanent fork without resolution). If the case exists: TI-C022 survives. Connect
  to the AC-8 adversarial model (incompatible schema proposals + fork-choice analog).
proof_verdict: >
  TI-C022 SURVIVES. The Permanent-Fork Discriminator exhibits a case where BFT/TCB integrity
  holds on each branch but TI-C022's ontological condition (genuine shared-process issuance)
  is violated on both. The surplus over BFT/TCB is real and is precisely the
  continuing-valid-shared-process condition (b), which BFT safety does not provide.
---

# E044: The BFT/TCB Discriminator for TI-C022

## Purpose

TI-C022 claims the shared participatory process is **ontologically load-bearing** for the
reality of issuance records:

> A D4 event e is genuine shared-process issuance iff (a) its record appears in R_n for at
> least k observers (quorum), AND (b) the shared OnlineSchemaSys process has not terminated
> or been invalidated before e achieves quorum. Condition (b) is the ontological
> process-dependence condition.

The standing objection (CLAIM-LEDGER, E037) is the BFT/TCB absorber:

> Absorbed by Byzantine fault tolerance + trusted computing base: "records valid within a
> continuing system" is standard distributed-systems integrity. TI's version must show what
> it adds over BFT/TCB.

The named test (CLAIM-LEDGER next_action):

> construct a case where BFT guarantees record integrity but TI-C022's ontological condition
> is not satisfied (e.g., the process has terminally forked without resolution). If such a
> case exists: TI-C022 survives.

This exploration constructs that case. It:
1. States exactly what BFT/TCB guarantees and, crucially, what it does *not* (Section 2).
2. Exhibits the Permanent-Fork Discriminator: a run where BFT integrity holds on each branch
   but TI-C022 condition (b) fails on both (Section 3).
3. Proves the surplus is real: condition (b) is not derivable from BFT safety/liveness
   (Section 4).
4. Connects to the AC-8 fork-choice model and the E042 productive SBP space (Section 5).
5. Records the verdict, the new discriminator, and what it does and does not earn (Sections 6-8).

---

## 1. The Object Under Test

A D4 issuance event e is recorded by observers. Two readings of "the record is real":

- **BFT/TCB reading (the absorber):** the record is real iff it was finalized by a
  fault-tolerant protocol — i.e. it is integrity-protected (authenticated, tamper-evident)
  and safety-finalized (no conflicting record is also finalized) under the protocol's fault
  assumption (≤ f Byzantine out of n, typically f < n/3).
- **TI-C022 reading (the claim):** the record is genuine *shared-process issuance* iff (a) it
  reaches a quorum AND (b) the shared OnlineSchemaSys process remains valid/continuing through
  that quorum — i.e. the schema extension it encodes is legitimately part of the *one*
  ongoing shared process, not a branch that the shared process has abandoned or that never
  rejoins.

The absorption question: does (b) add anything to BFT integrity + safety? We answer by
exhibiting a run where BFT is fully satisfied but (b) fails.

---

## 2. What BFT/TCB Guarantees — and the Gap

Standard BFT (PBFT, HotStuff, Casper FFG) under its fault assumption guarantees:
- **Safety:** no two conflicting records are both finalized (no equivocation survives).
- **Liveness:** under partial synchrony and ≤ f faults, progress continues.
- **Accountable safety (Casper):** if safety *is* violated (i.e. the fault bound is exceeded),
  ≥ 1/3 of validators are identifiable and slashable.
- **TCB integrity:** records are authenticated and tamper-evident relative to the trusted base.

The **gap**, stated precisely:

> BFT safety is a statement about **non-equivocation within one protocol instance under a fault
> bound**. It does NOT guarantee that the protocol instance *remains a single continuing
> process*. When the fault bound is exceeded (> f Byzantine) or the network partitions beyond
> the synchrony assumption, BFT's safety guarantee is **void**, and the system can split into
> two branches *each of which independently satisfies BFT integrity on its own validator subset*.

This is the standard CAP-theoretic fact: under a partition, a consistency-preferring (CP)
protocol like BFT halts on the minority side, but if BOTH sides have ≥ a local quorum (because
the partition splits a system whose two halves each exceed their local threshold, or because
> f validators are Byzantine and deliberately maintain two consistent-looking branches), you
get **two locally-integrity-valid branches with conflicting finalized records**. Accountable
safety then says "≥1/3 are slashable" — but slashing is a *post-hoc* attribution; it does not
make either branch's record the genuine one. BFT has no notion of which branch *is* the
continuing shared process. That notion is exactly TI-C022 condition (b).

---

## 3. The Permanent-Fork Discriminator

**Construction.** Take an AC-8 multi-observer OnlineSchemaSys with n observers running a BFT
finality protocol over schema extensions, quorum threshold k (k-of-n). Consider an SBP fork
(E031 §III.1 / E042 §4.2): two incompatible schema-boundary proposals on the same independent
proposition φ,
- e: assert φ (extension to S'),
- e': assert ¬φ (extension to S''),
with e, e' mutually incompatible (cannot be reconciled into a common successor).

Now drive the system into a **permanent fork** by either mechanism (both are within scope —
the first is a fault-bound violation, the second a never-healing partition):

- (M1, >f Byzantine) Suppose > f validators are Byzantine and split the honest validators into
  two groups G_e and G_f, each of size ≥ k, by feeding them disjoint views. G_e finalizes e;
  G_f finalizes e'. Each group runs a *locally valid* BFT instance: within G_e, record(e) is
  authenticated, non-equivocating, and finalized; within G_f, record(e') likewise. BFT
  integrity holds *on each branch's TCB*.
- (M2, eternal partition) Suppose the network partitions into P_e and P_f, each of size ≥ k,
  and the partition **never heals**. Each partition independently finalizes its branch under
  its local quorum. Again, integrity holds on each branch.

**The two branches never reconcile** (the fork is permanent; φ and ¬φ cannot both be in a
consistent schema, so there is no future S that extends both branches).

**Record-integrity check (BFT):** record(e) on branch e and record(e') on branch e' are each
integrity-valid, authenticated, finalized, and tamper-evident within their own TCB. **BFT/TCB
is satisfied for each record.** A BFT/TCB auditor inspecting branch e sees a perfectly valid
finalized record; same for branch e'.

**TI-C022 condition (b) check:** condition (b) requires that the *shared* OnlineSchemaSys
process has not terminated or been invalidated before e achieves quorum *in the continuing
shared process*. But after a permanent fork, **there is no single continuing shared process** —
the shared process has split into two mutually-inconsistent branches, neither of which is "the"
continuing process (by symmetry, and by the absence of any reconciliation). So:

```text
record(e):  (a) quorum within G_e/P_e: YES.  (b) continuing valid SHARED process: NO
            (the shared process forked; branch e is not the one shared process, it is one of two).
record(e'): (a) quorum within G_f/P_f: YES.  (b) continuing valid SHARED process: NO (symmetric).
```

By TI-C022, **neither e nor e' is a genuine shared-process issuance event** — each is a *local*
(branch-local) observation that achieved branch-local quorum but not shared-process legitimacy.

**Discriminator achieved.**

```text
                       BFT/TCB integrity     TI-C022 genuine shared-process issuance
record(e), branch e:        VALID                         NO
record(e'), branch e':      VALID                         NO
```

**Theorem 5 (BFT/TCB does not absorb TI-C022).**
There is a run (the permanent SBP fork, M1 or M2) in which both branch records satisfy BFT/TCB
integrity but neither satisfies TI-C022's genuine-issuance condition. Therefore TI-C022's
condition (b) is not implied by BFT/TCB integrity; TI-C022 is not absorbed. ∎

---

## 4. The Surplus Is Real, Not Terminological

To meet the absorption discipline (METHOD.md), we show condition (b) carries content BFT
cannot express, and identify the precise surplus.

**Surplus statement.** BFT safety quantifies over *one protocol instance under a fault bound*:
"no two conflicting records finalized **assuming ≤ f faults**." TI-C022 condition (b)
quantifies over *the persistence of a single shared process*: "the shared process did not
fork/terminate." These differ exactly when the fault bound is exceeded or the partition is
permanent — the regime where BFT's antecedent ("≤ f faults / synchrony") fails and its
guarantee is vacuous, while TI-C022 still renders a verdict (neither record is genuine).

- **BFT is silent off-assumption; TI-C022 is not.** When > f faults occur, BFT says nothing
  (its guarantee is conditional and the condition failed). TI-C022 says: neither fork branch is
  genuine shared-process issuance. This is content *beyond* BFT, precisely in the regime BFT
  abandons.
- **Accountable safety is attribution, not ontology.** Casper's "≥1/3 slashable" identifies
  *culprits*; it does not designate a *genuine record*. TI-C022's (b) is an ontological
  predicate on records (genuine vs local), not an attribution of blame. Different category.
- **TCB is about trust in the base, not continuity of the process.** A record can have an
  impeccable TCB (correct hardware, correct signatures) on a branch that the shared process has
  abandoned. TCB integrity ⊬ shared-process continuity.

**The precise surplus:** TI-C022 = BFT integrity **+ a global continuity predicate on the
shared process** (no permanent unreconciled fork through the quorum event). BFT provides the
first conjunct; the second is the genuinely new TI content. It is the *ontological* reading of
E028's quorum legitimacy: a record is real-as-issuance only if the one shared process carries
it, not merely if some fault-tolerant subset finalized it.

**Category-error check.** The risk was that "valid within a continuing system" is just BFT
restated. The discriminator shows it is not: BFT's "continuing system" is "one instance under
its fault bound," whereas TI-C022's "continuing shared process" is "the unique unforked
participatory process." These coincide *on-assumption* (≤ f faults, no permanent partition) and
*diverge off-assumption* (permanent fork) — and the off-assumption regime is non-empty and
physically/operationally reachable (permanent partitions and >f-fault forks both occur). So the
surplus is real.

---

## 5. Connection to the AC-8 Fork-Choice Model and E042

E028 and E037 asked for the AC-8 adversarial case: incompatible schema proposals + a
fork-choice analog. This discriminator instantiates it concretely.

- The incompatible proposals are the SBP fork e (assert φ) vs e' (assert ¬φ) — exactly the
  E042 §4.2 Gödelian SBP fork over an independent proposition.
- **Fork-choice rule = the operationalization of TI-C022 condition (b).** In blockchains, a
  fork-choice rule (longest chain, GHOST, LMD-GHOST) selects *which* branch is canonical. TI-C022
  condition (b) is the *ontological* fork-choice: a record is genuine iff its branch is the
  continuing shared process. When a fork-choice rule eventually selects one branch and the other
  is abandoned, condition (b) is *restored for the canonical branch* and *permanently denied for
  the orphaned branch* — the orphaned record was a local observation, never genuine
  shared-process issuance. This matches blockchain practice (orphaned/uncle blocks are valid
  records that are not part of the canonical history) and gives TI-C022 a concrete operational
  reading: **genuine shared-process issuance = canonical-branch records under the shared
  process's fork-choice.**
- **The permanent fork is the case with NO fork-choice resolution.** When the fork never heals
  (M1/M2), no branch is ever canonicalized, so condition (b) fails for *both* — the Theorem 5
  case. This is the irreducible adversarial case E028 sought: BFT gives each branch integrity,
  but the shared process never resolves which is genuine, so neither is.

**Tie to E042.** E042 proved the SBP space is productive (non-enumerable) in the Gödelian
regime. Each productive SBP fork is a potential permanent-fork site. TI-C022 supplies the
ontological discipline that says: a productively-issued schema extension counts as genuine only
if the shared process carries it through. So E042 (the witness exists) and TI-C022 (records are
genuine only under continuing shared process) are complementary: E042 says source-side issuance
is real; TI-C022 says a *record* of it is real only if the shared process legitimizes it. The
quorum-validity weight Q(e) = −log(acceptance prob) (E031 §III.3, E040 §10) is the natural
quantitative carrier: an orphaned-branch record has acceptance probability that decays to 0 in
the continuing process, so Q → ∞ (infinite surprise = not genuinely accepted).

---

## 6. Verdict

```text
TI-C022 BFT/TCB DISCRIMINATOR: RUN. Verdict: TI-C022 SURVIVES (NOT ABSORBED).

- Permanent-Fork Discriminator (Theorem 5): a run (>f Byzantine fork M1, or eternal partition
  M2) where each branch record satisfies BFT/TCB integrity but neither satisfies TI-C022's
  genuine-shared-process condition (b). The discriminating case the next_action demanded EXISTS.
- The surplus is real and identified precisely (Section 4): TI-C022 = BFT integrity + a GLOBAL
  CONTINUITY predicate on the shared process (no permanent unreconciled fork through the quorum
  event). BFT provides only the first conjunct; it is silent off its fault assumption, exactly
  where TI-C022 still renders a verdict.
- AC-8 fork-choice connection (Section 5): condition (b) IS the ontological fork-choice rule;
  genuine shared-process issuance = canonical-branch records; the permanent (unresolved) fork is
  the irreducible adversarial case where both branches fail (b). Concrete, matches blockchain
  orphan-block practice, and ties to the E042 productive SBP fork.

CLAIM EFFECT (TI-C022): status stays SPECULATIVE (promotion needs hostile review), but the
standing strongest objection (BFT/TCB absorber) is DEFEATED. The claim's surviving content is
sharpened to the global-continuity-predicate surplus and given an operational reading
(ontological fork-choice). next_action changes from "run BFT discriminator" (done) to "specify
the shared-process continuity predicate as a formal liveness-class condition and test whether it
reduces to eventual-synchrony liveness."
```

---

## 7. Residual Pressure (the honest next objection)

The strongest *surviving* objection, which the next run must face: is the
"continuing-shared-process" predicate just **eventual-synchrony liveness** restated? BFT
liveness assumes the partition eventually heals; under that assumption a fork-choice rule
eventually canonicalizes one branch, restoring (b). So one might argue TI-C022's surplus only
appears under permanent partition, which BFT *also* concedes it cannot handle — making TI-C022's
extra content "the negation of a BFT assumption" rather than new positive structure.

**Partial rebuttal (why TI-C022 still adds content):** the difference is the *direction of the
verdict*. BFT under permanent partition says "no guarantee" (silence). TI-C022 says
"neither record is genuine issuance" (a *positive ontological verdict*). A theory that converts
BFT's silence-off-assumption into a definite ontological verdict on record-reality is adding
content: it tells you what is *true about the records* in the regime BFT declines to discuss.
This is the same move TI makes generally (turning an absence-of-guarantee into a structural
claim). Whether this surplus is *useful* (supports a theorem, discriminator, or prediction)
beyond the verdict itself is the open question — which is why TI-C022 stays speculative, not
promoted. The discriminator earns survival, not promotion.

---

## 8. Assumptions, Failure Risks, Kill Conditions

### Assumptions
1. BFT means the standard safety/liveness/accountable-safety guarantees under a ≤ f fault bound
   (Section 2). TCB means standard authentication/tamper-evidence.
2. A permanent fork (M1 >f Byzantine, or M2 never-healing partition) is admissible — both are
   standard off-assumption regimes; their reachability is not in dispute.
3. The shared process's "continuity" is well-defined: there is a fact of the matter about
   whether the one participatory process forked. (TI-C019 supplies this as the shared
   participation layer.)

### Failure risks
1. If every operational fork eventually resolves (no permanent forks ever), the discriminating
   case is unreachable in practice and TI-C022's surplus is only counterfactual. Defense:
   permanent partitions and orphaned histories demonstrably occur (network splits, abandoned
   chains), so the case is reachable.
2. If "continuing shared process" cannot be made precise without invoking ordinary time
   (KILL-CRITERIA K2 circularity risk), TI-C022 weakens. Flagged for the next run: the
   continuity predicate must be stated in OnlineSchemaSys / quorum-legitimacy terms (no
   global clock), e.g. "there exists a single ⊆-directed chain of quorum-legitimate schema
   states containing the event," which is order-theoretic, not time-indexed.

### Kill conditions
1. If the continuity predicate provably reduces to eventual-synchrony liveness *as a formal
   condition* (not just agreeing on-assumption), TI-C022 absorbs into BFT liveness. Section 7
   gives the partial rebuttal (verdict-direction surplus); a full reduction proof would kill it.
2. If the positive ontological verdict ("neither record genuine") supports no theorem,
   discriminator, or prediction beyond restating (b) (KILL-CRITERIA K3/K4), TI-C022 is
   metaphysical residue and should be archived as a useful framing, not a research claim.

### Effect on other claims
- **TI-C019:** TI-C022 survival strengthens the shared-participation component (the shared
  process is load-bearing for record reality, not just coordination) — as RUN-0047 already
  noted, now backed by a concrete discriminator. The ontological fork-choice reading connects
  shared participation to a standard, well-understood operational mechanism (fork-choice rules)
  without absorbing into it. No status change.
- **AC-8 model:** the permanent-fork case is now the canonical adversarial fixture for the AC-8
  formal model (incompatible proposals + fork-choice), discharging the E028/E037 AC-8 gap-fill
  request at the discriminator level.
