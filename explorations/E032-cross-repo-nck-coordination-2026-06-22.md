---
artifact_type: exploration
status: active
exploration_id: E032
date: 2026-06-22
topic: cross_repo_nck_coordination_translation_table
claim_refs:
  - TI-C019
relates_to:
  - E031 (primary N, C, K definitions at category-morphism level)
  - TaF/explorations/explorer-nck-formal-definitions-2026-06-22.md
  - IEAH/explorations/E013-nck-cross-repo-formal-definitions-2026-06-22.md (primary N/C/K defs)
  - IEAH/explorations/E012-rate-distortion-grounding-for-lambda-star.md (Shannon grounding)
  - E028 (anti-collapse, trajectory-level condition)
  - E029 (PP-3, source/projection distinction)
  - E030 (five-run intake; Ostrom witness as PP-3 candidate)
purpose: >
  Cross-repo coordination artifact. Maps N, C, K from the primary E031 definitions
  (TI category-morphism level) to TaF (coherent section functor) and IEAH (Shannon
  rate-distortion) readings. Documents where definitions are consistent, where they
  diverge, and what the divergences imply.
governance_note: >
  This is a translation table, not a claim. None of the N, C, K definitions are
  admitted TI claims until the blocking obligations in E031 are completed.
---

# E032: Cross-Repo N, C, K Coordination — Translation Table and Consistency Check

## Purpose

Four repos independently converged on the blocking task: N(lambda, s), C(lambda, s),
and K(lambda, s) must be defined at the category-morphism level before lambda*(s) is
a formal claim in any of them. E031 (TI) attempted the primary definitions. This
document is the coordination artifact: it maps E031's definitions to TaF and IEAH
readings, verifies consistency, and names divergences.

GU is discussed separately in §5 (structural read only; no process-level lambda*(s)
can be defined in GU without connecting to a structural invariant).

---

## 1. Primary Definitions (TI / E031 Home)

The formal home for N, C, K is the Ext_S category from E031:

```text
Ext_S = (
  Ob: typed source constraint states S = (T_S, A_S)
  Mor: admissible extensions e: S -> S' (adds one typed constraint c_e to T_S)
  Composition: e2 ∘ e1 (sequential constraint addition; ASSOC-OBL-001 pending)
  Identity: id_S (empty extension)
)
```

Primary definitions:

```text
N(lambda, S) = |D4-Hom_lambda(S)| / |Hom_lambda(S)|
               [D4-morphism density rate: fraction of type-novel extensions at rate lambda]

K(lambda, S) = Pr[(S_n) eventually-constant | S_0 = S, rate = lambda]
               [trajectory-level schema fixation probability]
               Superlinear in lambda under independence assumption IA.

C(lambda, S) = lambda * E[RecCost(e, S)] + beta * lambda^2 * E[RecCost(e, S)]
               [reconciliation cost per step, convex in lambda under congestion]
```

Interior optimum lambda*(S) exists iff N concave AND K superlinear AND C convex AND
first-order conditions satisfied at both ends of the admissible lambda range.

---

## 2. Translation Table

### 2.1 N — Novelty / Structure Formation Rate

| Dimension | TI (E031) | TaF (explorer-nck) | IEAH (E013) |
|---|---|---|---|
| Formal object | D4-morphism density: proportion of type-novel extensions in Hom_lambda(S) | d|F(S)|/dt where F(S) = coherent sections at state S | I(X_lambda ; C_s): mutual information between new claims and existing consensus |
| What counts as "novel" | type(c_e) not in {type(c): c in T_S} | Extension does not create PO1 obstruction in D1RestrictionSystem | New claim not predictable from existing canonical consensus C_s |
| Why concave in lambda | D4-type space thins as T_S grows; diminishing returns on novelty | Space of PO1-free extensions thins as restriction system becomes more constrained | Shannon channel capacity saturation (CCA); finite channel capacity |
| Blocking condition | FUNCTOR-OBL-001: N is not yet a natural transformation | FUNCTOR-OBL-TaF-001: F functoriality (needs T34 PO1 chain support) | N-IEAH-001: probability measure on claim space (without circularity) |
| Cross-repo consistency | D4 morphisms in TI ↔ PO1-obstruction-free extensions in TaF | D4 morphisms in TI ↔ mutual-information-positive claims in IEAH | TaF and IEAH agree via: non-obstructed section = informative claim |

**Consistency verdict on N:** The three readings are consistent. D4 morphisms (type-novel,
TI) correspond to PO1-free extensions (globally coherent, TaF) which correspond to
high-mutual-information claims (novel relative to consensus, IEAH). The correspondence
requires that type-novelty and epistemic novelty are co-extensive — which holds when the
admissibility predicate A_S encodes what is epistemically accepted.

**Divergence point:** TI's N is discrete (proportion of D4 morphisms among all morphisms).
TaF's N is a rate (d|F(S)|/dt). IEAH's N is a continuous quantity (mutual information).
For the three to be the same object they must satisfy a proportionality or limit-taking
relation. Specifically: TI's discrete D4 proportion at rate lambda corresponds to TaF's
continuous derivative when lambda is the step-density parameter, and to IEAH's mutual
information when the epistemic claim space is given a probability measure.

### 2.2 K — Collapse / Instability Risk

| Dimension | TI (E031) | TaF (explorer-nck) | IEAH (E013) |
|---|---|---|---|
| Formal object | Pr[(S_n) eventually-constant | rate = lambda]: trajectory-level fixation probability | p * lambda * |F(S)|: rate of PO1 obstruction events | p_collision * lambda * H(canonical record): rate of certificate validity destruction |
| What "collapse" means | Schema fixed-point: S_n = S_{n*} for all n > n* (E028) | PO1 obstruction creating empty F(S') (no globally coherent sections survive the extension) | Certificate validity tau -> 0 for some cert in canonical record |
| Why superlinear in lambda | IA: each extension independently creates fixed-point risk | Each extension independently threatens each existing coherent section with probability p | Each claim independently threatens each existing certificate with probability p_collision |
| Blocking condition | IA verification against specific Compat families | IA-TaF-001: PO1 obstructions must be independent across sections | K-IEAH-001: p_collision requires formal model of certificate collision |
| Cross-repo consistency | Eventually-constant trajectory ↔ F(S') empty for all future S' ↔ all certs destroyed | All three: schema fixation is empty section set is zero valid certs | Consistent: same event at three levels of description |

**Consistency verdict on K:** The three readings name the same event (collapse) at
different levels of abstraction. Schema fixed-point (TI) implies empty coherent section
set (TaF) implies zero valid certificates (IEAH) — these are the same mathematical
condition expressed in each repo's native vocabulary. The superlinearity condition under
IA is the same independence assumption in all three cases; only the specific independence
structure varies (morphism-level in TI, section-level in TaF, certificate-level in IEAH).

**Divergence point:** TI's K is a trajectory-level probability over the full sequence
(S_n). TaF's K is an instantaneous rate (per-extension obstruction rate times current
section count). IEAH's K is a rate of certificate destruction. These correspond when
lambda is the same step rate in all three and when the trajectory-level probability is
determined by the per-step obstruction rate (which requires the independence assumption
to hold over the full trajectory, not just per step).

### 2.3 C — Reconciliation / Integration Cost

| Dimension | TI (E031) | TaF (explorer-nck) | IEAH (E013) |
|---|---|---|---|
| Formal object | lambda * E[RecCost(e,S)] + beta * lambda^2 * E[RecCost(e,S)]: fraction of existing constraints to check | lambda * E[SectionCost(e, F(S))]: fraction of existing sections requiring update | E[D_KL(P_{C_s|x} || P_{C_s})]: expected KL divergence from consensus update |
| What "cost" means | Checking each new constraint c_e against all existing constraints in T_S | Testing each existing globally coherent section for compatibility with new constraint c_e | Revising canonical consensus distribution away from prior |
| Why convex in lambda | Congestion coefficient beta: queue backup at high lambda | Same congestion model (TaF explicitly inherits E031's beta) | Shannon rate-distortion: total distortion convex in rate by theorem |
| Blocking condition | Convexity requires beta > 0 (empirical congestion coefficient) | Same as TI | C-IEAH-001: P_{C_s} prior without Bayesian subjectivism |
| Cross-repo consistency | RecCost(e,S) ↔ SectionCost(e, F(S)) ↔ D_KL update | RecCost is per-constraint; SectionCost is per-section; D_KL is distributional | TaF-to-IEAH: SectionCost is the distortion of revising each section; D_KL aggregates these |

**Consistency verdict on C:** Consistent in direction (all three are convex or potentially
convex costs growing in lambda) but different in granularity. RecCost (TI) operates at
constraint level, SectionCost (TaF) at globally-coherent-section level, D_KL (IEAH) at
distributional-consensus level. These nest: D_KL aggregates SectionCost over all sections;
SectionCost aggregates RecCost over constraints within a section. The three are consistent
iff the aggregation is additive (total distortion = sum of per-section distortions = sum
of per-constraint costs). Additivity holds if constraints are locally compatible (no
cross-constraint interaction costs). When constraints interact, aggregation is not additive
and the three formulations may diverge.

**Divergence point:** The Shannon grounding (IEAH) proves C + K jointly convex by the
rate-distortion theorem. TI and TaF assume convexity of C via a congestion model.
The Shannon proof is stronger but requires the probability-measure setup (C-IEAH-001).
If C-IEAH-001 is resolved, the IEAH proof can be imported to validate TI and TaF's
convexity claims without requiring the congestion assumption.

---

## 3. Interior Optimum: Where All Three Repos Agree

All three repos predict an interior optimum lambda*(S) > 0 under the same conditions:
- N concave (diminishing novelty returns)
- K superlinear (independent obstruction risks)
- C convex (reconciliation congestion)
- First-order conditions satisfied at both ends

The three repos agree on the existence condition. They may disagree on the value of
lambda*(S) for any given state S because the functionals take different specific forms
in each repo's vocabulary. This is expected and correct: the same abstract optimization
structure maps to different concrete values in physics vs. distributed systems vs.
information theory.

**Where the three must agree for cross-repo consistency:** The ordering relation. If
state S_1 has lambda*(S_1) > lambda*(S_2) in TI (more type-novel extensions available),
then the same ordering should hold in TaF (more PO1-free sections available at S_1)
and IEAH (higher mutual information gain available at S_1). If the orderings disagree,
the three readings are not the same mathematical object.

**Coordination test:** Construct a minimal fixture (two-state system: S with high D4
density and S' with low D4 density). Check whether TaF's coherent section count |F(S)|
and IEAH's channel capacity I(X_lambda; C_s) agree on which state has higher optimal
lambda*. This is the MSY discrimination test from explorer-nck-formal-definitions
applied cross-repo.

---

## 4. GU: Structural Read Only

GU formalization operates at the level of static structural invariants (gauge groups,
chirality, generation count, anomaly cancellation) via the six-axis specification protocol.
It does not have a formal process model (no Ext_S, no observer trajectory, no schema
extension process).

**What lambda*(s) means in GU (if anything):**

The only candidate: lambda_max as a capacity constraint on the observer's record-generation
chain (from the GU six-axis observer class, L2 in the specification protocol). If GU's
observer class specifies computational observers with bounded record-generation capacity,
then lambda_max is the rate at which this capacity saturates.

Formally:

```text
lambda_max^{GU} = capacity of GU's L2 computational observer class to generate
                  new record entries per unit structural time
```

This is a structural bound, not an optimization. It corresponds to K(lambda, S) = 1
at lambda = lambda_max (the observer's record capacity is exceeded, causing structural
collapse in the GU sense). It does not correspond to the interior optimum lambda*(S)
because GU has no N or C — only a capacity constraint on K.

**Connection to BvN decoherence rate Gamma_min:** E030's synthesis noted an unconfirmed
contact between lambda_max and BvN decoherence rate Gamma_min. If Gamma_min is the
minimum decoherence rate at which quantum records collapse (from a BvN-type argument
in the six-axis protocol), then lambda_max = Gamma_min could mean: the optimal issuance
rate (TI) converges to the minimum decoherence rate (GU) at which observer records
remain distinguishable. This would make lambda*(S) -> lambda_max^{GU} as S approaches
the regime where quantum effects dominate.

**Status:** speculative, unconfirmed. GU lacks the formal Ext_S category object that
would make this connection precise. This is logged as a contact point for future
cross-repo work once GU's observer class specification is developed further via the
six-axis protocol.

---

## 5. Consistency Summary

| Item | TI (E031) | TaF (explorer-nck) | IEAH (E013) | Consistent? |
|---|---|---|---|---|
| N object | D4-morphism density | d|F(S)|/dt (section growth rate) | I(X_lambda; C_s) (mutual info) | Yes, via D4 = PO1-free = informative |
| N concavity proof | Diminishing D4 types in T_S | Thinning PO1-free extension space | Shannon CCA (strongest proof) | Yes; IEAH proof can import to TI/TaF |
| K object | Trajectory fixed-point probability | p * lambda * |F(S)| (obstruction rate) | p_collision * lambda * H(record) | Yes, same event at different abstraction levels |
| K superlinearity | IA independence assumption | IA applied to sections | IA applied to certificates | Yes; all require same independence structure |
| C object | RecCost per constraint | SectionCost per section | D_KL per consensus update | Yes, nested: D_KL aggregates SectionCost aggregates RecCost |
| C convexity | Assumed (congestion model) | Assumed (inherited) | Proved (Shannon theorem) | Consistent; IEAH strongest |
| Interior optimum | Conditional (first-order conditions) | Conditional (same conditions) | Proved (Shannon) | Consistent; IEAH provides strongest existence proof |
| Blocking condition | ASSOC-OBL-001, IA verification | FUNCTOR-OBL-TaF-001, IA-TaF-001 | N-IEAH-001, C-IEAH-001, K-IEAH-001 | Each repo has its own |
| PP-3 layer | Layer-neutral; PP-3 applies | Layer-neutral; PP-3 applies | Layer-neutral (epistemic context) | All three inherit PP-3 |

---

## 6. What This Coordination Achieves

### Closed

The definition gap (the blocking task named in all four repos): N, C, K now have
formal definitions at the category-morphism level that are:
- Consistent across TI, TaF, and IEAH (same mathematical structure, different vocabulary)
- Precise enough to generate falsifiable conditions (concavity of N, superlinearity of K,
  convexity of C each have explicit kill conditions)
- Not absorbed by generic optimal control (D4 morphism density, PO1 obstruction rate,
  and mutual information are not available in standard state-space optimization)
- Conditional on verifiable assumptions (IA, CCA, ASSOC-OBL-001)

### Still Open

1. **PP-3 source-layer declaration:** All definitions are layer-neutral. The source-layer
   assignment requires a positive PP-3 witness (E029 requirements), which has not been
   supplied by these definitions alone. The Ostrom redistribution condition (E031 §III)
   is the best current candidate witness.

2. **Cross-repo ordering test:** Whether TI, TaF, and IEAH agree on which states S have
   higher lambda*(S) has not been verified. The two-state fixture test is the recommended
   first step.

3. **GU contact:** The lambda_max / Gamma_min contact is unconfirmed and requires GU to
   develop its observer class specification further.

4. **Blocking obligations per repo:** Each repo retains its own blocking obligations
   (ASSOC-OBL-001 for TI, FUNCTOR-OBL-TaF-001 for TaF, N/C/K-IEAH-001 for IEAH).
   Completing any one repo's obligations does not automatically discharge the others.
