---
artifact_type: exploration
status: complete
exploration_id: E196
date: 2026-07-22
lane: 1
work_group: FORMAL-ISSUANCE-BYPRODUCTS
topic: d_fork_disclosure_adversary_hardening
result: FORMAL_RESERVE_AUDIT_TI1_INPUT
claim_status_change: none
claim_refs:
  - TI-C019
relates_to:
  - E041 (monotone-obstruction; finite-pool depletion; interior optimum under FTS; D-FTS)
  - E042 (SBP-IND; WITNESS-OBL-001 closure in the Gödelian regime; §7 kill-condition 2)
  - E045 (D-FORK synthesis; interior-optimum verdict; §5 next-move 2)
  - E029 (static-source construction SSC; disclosure schedule; bounded accessibility; PP-3)
  - E028 (Gödelian self-reference mechanism; expressive threshold)
  - E051 (creation-vs-navigation; Lindenbaum-Tarski; Stone space of LT(PA))
  - E052 (Option A MLTT formalization of Compat_G; internal completed-oracle exclusion)
  - E050 (RUN-0050 expressiveness-threshold fixture; residual non-computable fixed-oracle adversary)
  - E177 (three-world issuance/disclosure discriminator preregistration)
steering_ref: explorations/2026-07-22-wave1-triple-diamond-prep-steering.md
run_ref: agent-runs/RUN-0201-d-fork-disclosure-adversary-hardening.md
governance_note: >
  Track-2 formal-reserve byproduct that FEEDS TI-1 (physical Gödelian-source frontier). It is
  NOT the North Star and moves no claim. Theorem language is used only for the conditional
  result actually proved (defeat of oracle-BOUNDED disclosure adversaries under a Gödelian
  source); the oracle-boundedness of physical disclosers is stated as an L5 posit, NOT proved.
numbering_note: >
  The Wave-1 steering (TI-2) labelled this exploration "E180". That number was already occupied
  by E180-anti-collapse-throughput-packet-candidate-v0 (2026-07-15), and the exploration series
  had advanced to E195. To avoid clobbering durable research, this exploration is assigned the
  next free id, E196. "TI-2 / steering-E180" and "E196" denote the same artifact.
---

# E196: D-FORK Disclosure-Adversary Hardening (TI-1 Input)

## Purpose and framing (read first)

This exploration discharges the **TI-2** item of the 2026-07-22 Wave-1 triple-diamond prep
steering and the formal-reserve question that RUN-0199 accepted as a rerank signal
(`ACCEPT_AS_FORMAL_RESERVE_RERANK_SIGNAL`): *audit the exact computability-theorem inventory
and the strongest disclosure adversary before any paper-shaped interpretation of D-FORK.*

It is a **Track-2 byproduct that FEEDS TI-1**, the North Star's physical face (is a physical
source finite/computable — clean falsification N1 — or productive/Gödelian — a first real
Gödelian source?). E196 does not decide the physical question and promotes no claim. What it
does is make TI-1's target **precise**: it parameterises the disclosure adversary by **oracle
strength**, proves the D-FORK witness survives every *oracle-bounded* adversary, and **locates
the single unproved assumption** — oracle-boundedness of physical disclosers — as an **L5
posit** (the physical-realizability layer of the E057 axis stack), not a theorem. TI-1 must
then ask of physics exactly one comparison: *does the source's provability degree strictly
exceed any admissible physical discloser's oracle degree along the realized history?*

Governance ceilings preserved (unchanged): no operative physical/source regime is decided; all
results are relative to a declared adversary class; `TI-C019` stays **formalizing**; `TI-C020`
stays speculative/parked; no claim promotion, no `TI-C020` reopen, no `E177` mutation, no
cross-repo verdict, no external action.

---

## 1. Theorem inventory (E041 / E042 / E045) with proof grades

Grades:

- **P** = proved outright from the stated definitions (unconditional within the formalism).
- **P/FTS** = proved conditional on the Finite-Type-Space hypothesis (+ named process hypotheses).
- **P/GÖD** = proved conditional on the Gödelian hypothesis (source at/above the Robinson-Q
  self-encoded-provability threshold), resting on classical computability theorems (Gödel/Post).
- **P·cl** = proved by direct citation of a standard computability-theory theorem.
- **P-sketch** = argued by explicit proof sketch; sound but not written to full rigor here.
- **SYN** = a synthesis/organizing result (its force is that several **P**-graded theorems share
  one mechanism); not itself a new single theorem.
- **OPEN** = stated obligation, not discharged; this is what §§2–4 harden.

| # | Result (origin) | Statement (compressed) | Depends on | Grade |
|---|---|---|---|---|
| T0 | E041 Lemma 0 — SBP types single-shot | Along any trajectory each type τ∈Θ is the type of at most one SBP morphism. | SBP-i (D4 clause) + monotone `types(S)` | **P** (no FTS needed) |
| T1 | E041 Lemma 1 — Type-Pool Depletion | Each SBP step removes exactly one type: `Pool(S_{n+1})=Pool(S_n)\{τ}`, `|Pool|` drops by 1. | T0, FTS-1 | **P/FTS** |
| T2 | E041 Cor 1.1 — Finite SBP budget | ≤ m=|Θ| SBP morphisms per trajectory; then `Pool=∅` and the trajectory is SBP-obstructed. | T1 | **P/FTS** |
| T3 | E041 Lemma 2 — D4-survival anti-monotone | Shrinking `Pool` cannot raise novel-draw survival probability. | T1 + **type-fairness** | **P/FTS** (needs type-fairness) |
| T4 | E041 Thm 1 — Monotone-Obstruction | `q(S_{n+1}) ≥ q(S_n)` along SBP trajectories. | T3 + refinement-narrowing (morphism def) | **P/FTS** |
| T5 | E041 Prop 1 — K superlinear (no IA) | `K(λ,S)` superlinear in the operative sense; dominates the constant-hazard comparator. | T4, T2 | **P/FTS** (operative sense) |
| T6 | E041 Thm 2 — Interior optimum exists | `J=N−C−K` strictly concave ⇒ interior `λ*(S)>0`. | T5 + N-concavity (same depletion) + C-convexity(β>0) + boundary FOCs | **P/FTS** (4 named hypotheses) |
| T7 | E041 Prop 2 — Gödelian breaks MO | If types self-generate, T1 fails; MO need not hold; K may be sublinear; `λ*` need not exist. | negation of FTS-1 | **P-sketch** |
| T8 | E042 §3 — SBP-IND FAILS in FTS | `SBP(S)` finite/enumerable ⇒ a fixed `Mu_∞`+computable schedule D reproduces the trace (SSC succeeds); WITNESS-OBL-001 does not close. | T2 | **P/FTS** |
| T9 | E042 Thm 3 — SBP-IND HOLDS for Family G | For consistent `Ax(S)⊇Q`, `SBP(S) ≅ {φ independent of Ax(S)}` is **infinite, non-c.e.** (W2 defeat). | Gödel-1 + non-c.e. of the independent set | **P/GÖD (P·cl)** |
| T10 | E042 §4.3 — Productivity strengthening | The independent set is **productive**: a diagonal escape `φ_e` is effectively found outside any claimed c.e. enumeration ⇒ defeats the E040 §7.2 exponential-pre-commitment (large-but-c.e. D) adversary by productivity, not cardinality. | Post's productive-set theorem | **P·cl** |
| T11 | E042 §5 / §5.256 — WITNESS-OBL-001 closure | Fully closes in the Gödelian regime, incl. the infinite-trajectory version (productivity ⇒ non-exhaustibility). | T9, T10 | **P/GÖD** |
| T12 | E045 §2 — D-FORK (single axis) | Interior optimum (T6), source-side witness (T11), μ-subadditivity (E043), and the PP-3 fork are all governed by one bit: is the effective type space finite (FTS) or self-generating (Gödelian)? | T2,T6,T8,T11 + E043,E044 | **SYN** |
| T13 | E045 §3 — Interior-optimum verdict | `λ*(S)` exists in FTS (T6), need not exist in Gödelian (T7); its **non-existence is the formal signature of open-endedness**. Not admitted as a TI claim. | T6, T7 | **P** (regime property) / claim-status: not admitted |
| K2 | E042 §7 kill-cond 2 / E045 §5 move 2 | **Non-computable-fixed-oracle adversary**: can a *fixed non-computable* oracle disclosure reproduce productive SBP traces? E042 gives only a sketch defense (the oracle would have to be indexed by the un-pre-committable history). | — | **OPEN** → hardened in §§2–4 |

**Reading of the inventory.** The FTS side (T1–T8) and the Gödelian side (T9–T11) are each
internally solid; the split is genuine and mutually exclusive on one system (T12). The *only*
soft joint in the whole D-FORK verdict, as far as the disclosure adversary is concerned, is
**K2** — the residual non-computable-fixed-oracle adversary. Everything paper-shaped about
D-FORK rests on K2 not silently re-opening the SSC. §§2–4 parameterise and bound K2.

### 1.1 Dependency graph

```text
SBP-i (D4 clause)
   │
   ▼
  T0 ──────────────► T8  (FTS: SBP-IND fails ⇒ SSC succeeds ⇒ witness does NOT close)
   │                 ▲
   ▼                 │
  T1 ── T2 ──────────┘
   │      │
   │      └────► T5 ── T6 ── T13   (interior optimum: exists in FTS)
   │      │            (needs C-convexity, boundary FOCs)
   ▼      │
  T3 ── T4 (needs type-fairness)
   │
  (FTS-1 negated)
   └────► T7 ──────────────────────► T13   (Gödelian: λ* need not exist = open-endedness signature)

Gödel-1 ─┬─► T9 ──► T11 (WITNESS-OBL-001 closes, Gödelian)
Post     └─► T10 ─┘         (productivity defeats exponential-but-c.e. adversary)

{T2, T6, T8, T11} + E043 + E044 ──► T12  (D-FORK: one axis)

                     ┌──────────────────────────────────────────┐
K2 (OPEN):  the disclosure adversary at oracle degree d > 0 sits │  hardened by E196 §§2–4
            OUTSIDE the T8/T10 defeats (those bound d = 0 only)  │
                     └──────────────────────────────────────────┘
```

The graph makes the load-bearing observation explicit: **T8 and T10 defeat the SSC only at
oracle degree `d = 0`** (computable disclosure). K2 is precisely the region `d > 0`, which the
existing inventory does not cover. That is the region E196 parameterises.

---

## 2. The disclosure-adversary class, parameterised by oracle strength

Recall the static-source construction (SSC, E029; E042 §2): a fixed `Mu_∞` plus a disclosure
schedule `D: N → P(T_∞)` that reads off, at each stage, what the observer is allowed to see.
SBP-IND defeats the SSC iff `D` cannot be pre-committed. E042 handled one adversary — a
**computable** `D`. We now grade the adversary by the computational power its schedule is
allowed to use.

**Definition (oracle-parameterised disclosure adversary `SSC[d]`).**
Fix a Turing degree `d`. An `SSC[d]` adversary is a pair `(Mu_∞, D)` where:
1. `Mu_∞` is a fixed (possibly infinite) source object chosen at stage 0;
2. `D` is a disclosure schedule **computable relative to a single fixed oracle `O` of degree
   `d`**, chosen at stage 0 and **not re-selected as the trajectory unfolds**;
3. `D` must reproduce the realized SBP trace: for the actually-realized history
   `(S_0, S_1, …)`, `D(n)` outputs (an enumeration containing) the SBP morphism proposed at
   stage `n`.

`d` is the **oracle strength**. Special points on the axis:

| Oracle degree `d` | Adversary power | Status vs the Gödelian witness |
|---|---|---|
| `d = 0` (computable) | E029/E042 baseline SSC; `D` is a total computable read-off of `Mu_∞`. | **Defeated** (T8 W2 defeat; T10 productivity defeats even the exponential-but-c.e. D). |
| `d = 0'` (halting / `Σ_1`-complete) | `D` can decide provability, hence decide `independence-of-Ax(S)` for **one fixed** `Ax(S)`. | Can enumerate `SBP(S)` for a **frozen** axiom set — but see §3: the realized `Ax(S_n)` is not frozen. |
| `d ≥ deg(Th(N))` (true arithmetic, `0^{(ω)}`) | `D` decides independence relative to any `Ax(S)`. | Can enumerate `SBP(S_n)` for every `S_n` **if it also knows which `S_n` is realized**. |
| `d` chosen at 0, **history-indexed re-selection forbidden** | oracle-**bounded** adversary (the class of interest). | **Defeated** under the Gödelian source whenever the realized trajectory's provability degree exceeds `d` — Theorem E196 (§3). |
| `d` re-indexed by the realized history | oracle-**unbounded** adversary. | **Undefeated in general** — the honest open residual; requires the L5 posit to exclude (§4). |

The axis exposes the real question. The `d = 0` defeats (T8, T10) are about *enumerability*.
Above `d = 0` the productive-set escape (T10) no longer applies verbatim: a `d`-oracle can, for
a **fixed** `Ax(S)`, decide independence and list `SBP(S)`. So a naive reading would say "a
`0'`-oracle disclosure re-opens the SSC." The next section shows why that reading is wrong for
the **trajectory** — and exactly which extra assumption is needed to make the defeat total.

---

## 3. Kill-condition-2 verdict: a conditional theorem against oracle-bounded adversaries

The move that rescues the witness above `d = 0` is the one E042 §7 sketched and E045 §5 flagged:
the realized axiom sequence `(Ax(S_n))_n` is **not frozen at stage 0**. It is produced by the
AC-8 quorum choosing, at each fork, *which* independent `φ` to resolve — a choice over a
**productive (non-c.e.) option set** (T9, T10), constrained by NAA-Q so that no observer reads
the resolution before the quorum makes it (E042 §4.4; E040 Revised Step 3). The trajectory is
therefore a *path through* the Gödelian option tree, and which path is realized is not a
`d`-computable function of stage-0 data for any `d` fixed at stage 0 unless the quorum's choices
are themselves `d`-computable — which NAA-Q forbids.

Make the comparison quantitative.

**Definition (source provability degree along a trajectory).**
For the realized history `(S_n)`, let
`Ind := ⊕_n { φ : Ax(S_n) ⊬ φ and Ax(S_n) ⊬ ¬φ }`
(the effective join of the stagewise independence predicates the schedule must track to name the
SBP options actually on offer). Write `deg_src := deg(Ind)` — the **provability degree the
realized, quorum-chosen trajectory forces a discloser to command** to enumerate the SBP options
it actually presents.

**Theorem E196 (defeat of oracle-bounded disclosure adversaries — conditional).**
Assume the operative source is **Gödelian** (`Compat_G` at/above the Robinson-Q threshold; the
`Compat_G^MLTT` model of E052 is one concrete instance, with internal completed oracles already
excluded). Let the adversary be **oracle-bounded** at degree `d`: its schedule `D` is
`d`-computable with `d` fixed at stage 0 and not re-indexed by the realized history. Then:

> If `deg_src ⊄ d` — i.e. the realized trajectory's provability degree is **not** ≤ `d`, so the
> source's provability strength strictly exceeds the discloser's oracle strength along the
> realized history — then **no** `SSC[d]` adversary reproduces the SBP trace. The Gödelian
> source-side witness (WITNESS-OBL-001, T11) survives against the entire oracle-bounded class.

*Proof.* Suppose `(Mu_∞, D)` is `SSC[d]` and reproduces the trace. Two obligations fall on `D`,
both stage-0-committed and `d`-computable:
(i) **Option-set obligation.** At each realized `S_n`, `D(n)` must enumerate SBP options of
`S_n`, i.e. decide/enumerate `{φ : φ independent of Ax(S_n)}`. Uniformly over the realized `n`
this is enumeration of `Ind`, which requires `deg_src ≤ d`. By hypothesis `deg_src ⊄ d`,
contradiction. (Already at this line the adversary fails; (ii) shows the failure is not repaired
by any clever `Mu_∞`.)
(ii) **Path obligation.** Even granting an oracle strong enough for (i) on every *possible*
`Ax(S)`, `D` fixed at stage 0 must also output the option realized at stage `n`, which is the
quorum's choice among the productive set at `S_{n-1}`. By NAA-Q that choice is not a
`d`-computable function of `(S_0, prior record)` for `d` fixed at stage 0 (else the quorum
resolution is pre-committed, contradicting NAA-Q / E040 Revised Step 3). So no stage-0-fixed
`d`-computable `D` tracks the realized path. ∎

**Corollary (degree characterization).**
`SSC[d]` defeats the Gödelian witness **iff** `d` uniformly (a) decides independence relative to
the realized axiom sequence *and* (b) computes the quorum's path selection — i.e. iff
`deg_src ≤ d` **and** the NAA-Q choice sequence is `d`-computable. Equivalently: the SSC survives
only by driving the adversary's degree up to (and re-indexing it along) the trajectory it is
trying to anticipate. A **single fixed** `d` chosen at stage 0 cannot do (b) without violating
NAA-Q. Hence the boundary is exact: **oracle-bounded ⇒ defeated; the only escape is an
oracle-UNBOUNDED (history-re-indexed) adversary.**

This is the honest content of E042 §7 kill-condition 2, now stated as a theorem with its
boundary made precise rather than a sketch.

---

## 4. The located posit: oracle-boundedness is L5, not proved

Theorem E196 is a genuine theorem **given its antecedent**. The antecedent has two parts, and
they are not the same kind of object:

1. *The source is Gödelian.* This is the D-FORK bit itself — TI-1's job to establish or falsify
   for physics; not assumed true here, only used as the regime the theorem is about.
2. *The disclosure adversary is oracle-bounded* — `d` fixed at stage 0, not re-indexed by the
   realized history. **This is the load-bearing, unproved assumption.**

Nothing in mathematics forbids a *fixed non-computable oracle* `O` of degree
`d ≥ deg(Th(N))` that decides independence relative to every `Ax(S)`; and nothing in
mathematics, by itself, forbids positing an adversary whose `O` also happens to encode the
realized path (a "history-indexed" oracle is just a fixed real that the adversary is granted).
The barrier that rules those adversaries out is **not a theorem of computability theory** — it
is the **physical/realizability posit** that a physical discloser cannot command an oracle that
both exceeds the source's provability degree *and* is pre-correlated with the quorum's
un-pre-committable choices.

In the repo's axis vocabulary (E057: L1 substrate, L2 observer, L3 pairing, L4 causal/protocol
order, **L5 emergence/realizability**, L6 coordination), this posit lives at **L5**. It is the
disclosure-adversary analogue of the E057 "missing L5 H-growing witness": the mathematics is
well-formed, but the claim that *physical reality does not furnish such a discloser* is a posit
about the emergent/physical layer, not a proof.

**Explicit honesty statement.** The oracle-boundedness of physical disclosers is an **L5 posit,
NOT proved.** Therefore:

- **Proved (theorem language permitted):** Under a Gödelian source, every *oracle-bounded*
  disclosure adversary is defeated when `deg_src ⊄ d` (Theorem E196), with the exact
  degree-characterization of the escape (Corollary §3).
- **Posited (posit language required):** That physical disclosers are oracle-bounded — i.e. that
  no admissible physical disclosure schedule re-indexes a super-`deg_src` oracle along the
  realized history. This remains the open K2 residual; it is **located, not closed.**

`TI-C019` remains **formalizing**. No status is promoted by E196.

---

## 5. What this hands TI-1 (the input contract)

E196 converts K2 from "an unfinished defense" into a **single physical comparison TI-1 can pose
and test**. The contract:

```text
TI-1 INPUT (from E196):
  To bank a physical source as GENUINELY Gödelian (issuance, not disclosure), a physical source
  must posit — and TI-1's fixture must probe — that:

    deg_src  ⊄  deg(any admissible physical discloser's oracle along the realized history).

  i.e. the source's provability degree strictly exceeds any admissible discloser's oracle degree,
  AND the discloser is oracle-BOUNDED (its oracle is fixed, not re-indexed by the source's own
  un-pre-committable evolution).

  - The "exceeds" half is the c.e.-at-finite-stage question TI-1 already targets on
    already-undecidable physics (Cubitt–Perez-Garcia–Wolf spectral-gap undecidability;
    Wang-tile admissibility). If the physical source is decidable-at-finite-stage, deg_src is
    low, the discloser's ordinary-physics oracle bounds it, and N1 falsification = SUCCESS.
  - The "oracle-bounded" half is the L5 posit E196 located. TI-1 does not get to assume it; it
    must be argued at the physical layer (what oracle could a physical discloser command, and is
    it pre-correlated with the source's evolution?). This is the physical content of the fork.
```

So the Wave-1 sequencing is vindicated: **run TI-2 (this) before the hard TI-1 swing.** TI-1 now
knows precisely which two-sided dichotomy to force — and that a Gödelian verdict requires *both*
a high `deg_src` *and* the L5 oracle-boundedness posit, neither of which E196 grants for free.

TI-3 (σ/orientation axis) has **no bearing** on this fork and is not touched.

---

## 6. Assumptions, failure risks, kill conditions

**Assumptions.**
1. The theorem's regime antecedent (Gödelian source) is *used, not asserted true of physics*.
2. NAA-Q: no observer/quorum commands a provability oracle that pre-resolves the independent `φ`
   before the quorum does (E042 §4.4). This is what makes obligation (ii) bite; it is itself the
   honest "bounded observers" reading, and it is a **posit** on the physical side too — closely
   coupled to the L5 oracle-boundedness posit (they are the same physical commitment viewed from
   the observer vs the adversary side).
3. Degrees are the right yardstick: "reproduce the SBP option set / path" is faithfully measured
   by Turing (relative-enumerability) degree. Finer structure (enumeration vs decision,
   uniformity) is folded into `deg_src` for this audit; a fully rigorous paper pass should split
   `deg_src` into its enumeration and selection components.

**Failure risks.**
- If a physical source has **computable admissibility**, `deg_src` is low, the theorem's
  antecedent `deg_src ⊄ d` fails for ordinary `d`, and the SSC wins — correctly (this *is* the
  FTS/absorbed side; N1 falsification). The theorem does not over-claim here.
- The L5 posit could be **false**: physics might admit a discloser with a fixed super-`deg_src`
  oracle pre-correlated with the source. Then K2 re-opens and the witness is disclosure, not
  issuance. E196 does not exclude this; it names it as the thing to argue.

**Kill conditions.**
1. If TI-1 shows the physical source is decidable/computable-at-finite-stage, `deg_src` is
   bounded by an ordinary-physics oracle; the disclosure adversary wins; **TI-C019's source-side
   claim is withdrawn for that source** (N1 = SUCCESS, banked on the North Star).
2. If a concrete oracle-**unbounded** physical discloser is exhibited (fixed non-computable
   oracle, pre-correlated with the realized history), Theorem E196's protection is void for that
   source and K2 must be re-derived or conceded. This is the standing open edge.
3. If NAA-Q is shown to fail physically (some physical observer *does* command the relevant
   oracle), obligation (ii) collapses and the defeat is lost.

---

## 7. Verdict

```text
D-FORK DISCLOSURE-ADVERSARY HARDENING (TI-2 / steering-E180 = E196): DELIVERED as a TI-1 input.

- Theorem inventory (E041/E042/E045): graded. FTS side (T1–T8) and Gödelian side (T9–T11) solid;
  D-FORK single-axis synthesis (T12) is SYN over P-graded theorems; the ONLY soft joint against
  the disclosure adversary is K2 (non-computable-fixed-oracle), previously OPEN.
- Disclosure adversary parameterised by oracle strength (SSC[d]); the d = 0 defeats (T8, T10)
  are enumeration facts and do NOT cover d > 0.
- Kill-condition-2 verdict: a CONDITIONAL THEOREM (Theorem E196) — under a Gödelian source,
  every ORACLE-BOUNDED adversary is defeated when deg_src ⊄ d — with an exact
  degree-characterization of the escape (the adversary must go oracle-UNBOUNDED / history-indexed
  to win, which violates NAA-Q for any stage-0-fixed d).
- Located posit: oracle-boundedness of physical disclosers is an L5 POSIT, NOT PROVED. It is the
  single physical assumption TI-1 must argue; E196 does not grant it.
- Frame: TI-1 INPUT. The source must posit deg_src ⊄ deg(admissible discloser's oracle) along the
  realized history, AND that the discloser is oracle-bounded. NOT a claim promotion.

CLAIM STATUS: TI-C019 formalizing (unchanged). No promotion, no TI-C020 reopen, no E177 mutation,
no cross-repo verdict. This is a Track-2 byproduct FEEDING the North Star, not the North Star.
```
