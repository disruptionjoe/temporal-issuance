---
artifact_type: agent_run
run_id: RUN-0047
status: complete
phase: 2B
date: 2026-06-22
trigger: cross_repo_research_session_five_ideas
explorations_produced:
  - explorations/E034-lambda-star-absorber-test.md
  - explorations/E035-mu-M-metabolic-field-specification.md
  - explorations/E036-sublinear-mu-discriminator.md
  - explorations/E037-kill-criteria-test-cross-repo-ideas.md
claim_rows_added:
  - TI-C021
  - TI-C022
claims_affected:
  - TI-C003 (narrowing candidate reversed for mu demotion)
  - TI-C019 (strengthening candidate from Idea E ontological version)
---

# RUN-0047: Cross-Repo Intake Absorber Test

## Run Summary

This run processes five ideas from a cross-repo research session, each proposed as a formal
contribution to the Temporal Issuance program. Each idea is tested against the absorption
discipline, the kill criteria, and the current claim state.

The five ideas:

- **A:** lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]
- **B:** mu_M(r) = c * |r|^{3/4} (metabolically-scaled, sublinear, non-additive)
- **C:** Ostrom SES legitimacy: legitimacy requires balancing mechanism against increasing-returns capture
- **D:** Declining issuance curves as optimal (Jermann and Xiang tokenomics result)
- **E:** "Trust in the message requires trust in the system holding the message"

---

## Method Used

1. Orientation: read all governance files, current claim state, and the two most recent
   explorations (E028, E029) to understand the current program position.
2. Absorber test for each idea (E034-E037).
3. Kill-criteria test for each idea (E037).
4. Claim registration for survivors (this run record; CLAIM-LEDGER.md appended).

---

## Absorber Results

### Idea A: lambda*(s) = argmax_lambda [N - C - K]

**Result: absorbed.**

E034 establishes that the argmax selection structure is absorbed by MDP/optimal control
at the structural level, by active inference (free energy minimization) at the structural
level, and by economic profit maximization. The absorption is complete: no residual formal
content survives at the selection-structure level.

A surplus would appear only if N, C, K are independently derived from TI's typed source
constraints without importing optimization, economic, or Bayesian machinery. No such
derivation is provided or available.

**K1 triggered** for lambda*(s) as a formal object.
**K4 triggered** for lambda*(s) without TI-specific content.

Vocabulary contribution: the terms N (novelty), C (constraint cost), K (kill proximity)
are useful as design scaffolding for the AC-8 fixture and the source-side witness fixture,
but they are not formal claims.

---

### Idea B: mu_M(r) = c * |r|^{3/4}

**Result: split — specific form absorbed; sublinear class survives.**

E035 establishes:
- The specific exponent 3/4 is absorbed by the West-Brown-Enquist fractal transport network
  derivation (1997). WBE derives 3/4 from optimizing supply through hierarchical branching
  networks in 3D space. TI does not supply the spatial embedding or network topology required
  by WBE.
- The constant `c` is not derived from source admissibility.
- However, the **subadditivity property** — mu(A union B) < mu(A) + mu(B) for disjoint A, B
  — is not absorbed by any existing TI mu candidate.

E036 establishes that the **sublinear mu class** (mu_alpha(r) = c * |r|^alpha, 0 < alpha < 1)
generates three non-trivial formal contributions:
1. Subadditivity as a discriminator against additive measure candidates
2. Diminishing marginal issuance (size-dependent declining rate)
3. PP-3 discriminator candidate (size-dependent vs. aperture-dependent issuance rate)

**K1 triggered** for mu_M with specific exponent 3/4.
**K1 NOT triggered** for the sublinear mu class.
**K3 NOT triggered:** the sublinear class generates discriminators and test surfaces.

**New claim candidate: TI-C021 (registered below).**

---

### Idea C: Ostrom SES Legitimacy

**Result: not absorbed; fills formal gap in AC-8.**

The Ostrom legitimacy condition (an issuance mechanism is legitimate if the first-mover
advantage in schema extension is bounded — no coalition can lock out later extensions through
increasing-returns capture) is NOT in TI's current formal object. It is not absorbed by NAA,
D4, or the existing quorum legitimacy condition identified in E028.

Formal test surface generated: can a coalition in AC-8 who issue first create a lock-in that
prevents later D4-qualifying events by non-members from becoming part of the shared schema?

This is a no-go result candidate: if such lock-in is possible under current OnlineSchemaSys
+ NAA, then the Ostrom condition is a formal requirement, not just an institutional preference.

The Ostrom condition is formalized as:

```text
An issuance mechanism M is Ostrom-legitimate if for all coalitions C_cap, the
advantage of C_cap over non-members in schema extension events does not grow
without bound as the number of prior C_cap issuance events increases.
Equivalently: first-mover advantage in schema extension is bounded.
```

**No kill conditions triggered.**
**Positive contribution: fills AC-8 formal gap identified in E028.**

---

### Idea D: Declining Issuance Curves (Jermann and Xiang)

**Result: category mismatch; absorbed for TI purposes.**

The Jermann-Xiang result is a tokenomics / macroeconomics result. It establishes optimality
of declining supply curves for digital assets in an intertemporal asset-pricing framework.
The absorbers are standard monetary theory and intertemporal asset pricing.

Applying Jermann-Xiang to TI requires mapping:
- economic issuance rate -> TI D4 event rate
- welfare optimality -> openness optimality
- agent utility -> observer schema extension benefit

TI has no utility function, no time-discounting model, and no price mechanism. The mapping
cannot be constructed from current TI primitives.

**K1 triggered** for direct import of Jermann-Xiang as a TI result.
**K4 partial:** if imported without translation, reduces to known economics.

The result can be used as supporting intuition for the sublinear mu class motivation, but
not as a formal TI claim. No TI-internal formal work is generated.

---

### Idea E: "Trust in the Message Requires Trust in the System Holding the Message"

**Result: partially absorbed (security version); ontological version survives.**

The security and distributed systems version is absorbed by Byzantine fault tolerance (BFT)
and the trusted computing base (TCB) literature. These are well-established frameworks.

The **ontological version** is different and NOT absorbed:

```text
In TI's framework: the reality of issuance records (D4 event records) depends on
the continued validity of the shared participatory process (OnlineSchemaSys + AC-8
legitimacy), not merely on record storage or cryptographic verification.
```

This is not a security claim. It is a claim about ontological dependence: records are real
(in the TI-relevant sense of being genuine shared schema extensions) only while the shared
process remains valid and legitimate. A D4 event that is recorded locally but never
achieves quorum propagation to the shared process is not a genuine shared-process issuance
event — it is a local observation.

Formal discriminator generated:

```text
Test: Can an observer construct a finalized record of a D4 event without the shared
OnlineSchemaSys continuing to be valid? If records are independently real: yes. If the
process is ontologically load-bearing: no.
```

This connects to and sharpens:
- E028's quorum legitimacy condition: D4 events must propagate to a threshold of observers
  within a continuing shared process to count as genuine shared schema extension
- AC-8 adversarial model: a D4 event under challenge (incompatible schema proposals) is
  not genuine until the shared process resolves the fork

**K1 partial** (security version absorbed by BFT/TCB).
**Ontological version NOT absorbed.**
**K3, K4, K5 NOT triggered.**

**New claim candidate: TI-C022 (registered below).**
**Strengthening candidate for TI-C019 shared-participation framing.**

---

## Kill-Criteria Test Summary

No kill conditions triggered for the TI program as a whole.

Kills targeted at specific formal objects:
- lambda*(s) as a novel formal object: killed (K1, K4)
- mu_M with specific exponent 3/4: killed (K1 for exponent)
- Jermann-Xiang as a formal TI import: killed (K1 for direct import)

No existing claims (TI-C001 through TI-C020) are killed or weakened by this run.

---

## Claim Effects

### TI-C003 (IssuanceSystem as candidate formal object)

The sublinear mu class (from Idea B / E036) partially reverses the demotion of `mu` to
an unresolved placeholder. The sublinear class gives `mu` a formal property (subadditivity)
that discriminates it from all killed mu candidates. This does not restore mu to a fully
specified field — the exponent and constant remain unspecified — but it identifies a
formal class membership requirement: any surviving mu must be subadditive in the size-
driven sense.

```yaml
TI-C003:
  status: weakened (unchanged)
  effect: mu_placeholder_partially_sharpened
  added: subadditivity_requirement_candidate
  evidence_ref: explorations/E035-mu-M-metabolic-field-specification.md
                explorations/E036-sublinear-mu-discriminator.md
```

### TI-C019 (Shared-process-and-issuance hypothesis)

Idea E's ontological version strengthens the shared-participation framing. The claim that
the shared process is load-bearing for record reality (not just for coordination) is a
strengthening of TI-C019's shared-participation component.

The Ostrom legitimacy condition (Idea C) identifies an adversarial case for AC-8 not
previously formalized — this is a gap-fill, not a weakening.

```yaml
TI-C019:
  status: formalizing (unchanged)
  effect: shared_participation_framing_strengthened
  added:
    - ontological_process_dependence_of_records (from Idea E)
    - ostrom_legitimacy_gap_in_ac8 (from Idea C)
  evidence_ref: explorations/E037-kill-criteria-test-cross-repo-ideas.md
```

---

## New Claim Rows (Registered Below)

### TI-C021

```yaml
claim_id: TI-C021
claim: >
  The issuance measure mu is subadditive in realized structure size: for all disjoint
  realized structures A, B with positive size, mu(A union B) < mu(A) + mu(B).
  Equivalently, the marginal issuance per new constraint is strictly decreasing in
  realized structure size. This property distinguishes mu from additive and
  inclusion-exclusion-additive measures (cardinality, probability, action, linear
  information content).
status: speculative
current_strongest_version: >
  The sublinear mu class mu_alpha(r) = c * |r|^alpha for 0 < alpha < 1 satisfies
  subadditivity and produces diminishing marginal issuance. The class is not absorbed
  by any existing TI mu candidate. The specific alpha and c remain unspecified.
current_strongest_objection: >
  Shannon entropy is subadditive in some regimes via correlation structure. If
  entropy's subadditivity absorbs the size-driven subadditivity TI requires, then
  TI-C021 is absorbed as an entropy variant. The discriminating test: entropy's
  subadditivity depends on joint distribution; TI-C021's subadditivity holds for all
  disjoint sets regardless of distribution.
evidence_refs:
  - explorations/E035-mu-M-metabolic-field-specification.md
  - explorations/E036-sublinear-mu-discriminator.md
next_action: >
  Determine whether entropy's correlation-driven subadditivity absorbs TI-C021's
  size-driven subadditivity. If no: formalize TI-C021 and add the PP-3 discriminator
  candidate (size-dependent rate vs. aperture-dependent rate) as a test condition.
  If yes: absorb TI-C021 into the entropy absorber entry and close.
```

### TI-C022

```yaml
claim_id: TI-C022
claim: >
  The shared participatory process (OnlineSchemaSys + AC-8 legitimacy) is ontologically
  load-bearing for the reality of issuance records: a D4 event is genuine shared-process
  issuance if and only if its record propagates to a quorum of observers within a
  continuing valid shared process. Records that are locally finalized but do not achieve
  quorum propagation in a continuing shared process are not genuine shared-process
  issuance events; they are local observations.
status: speculative
current_strongest_version: >
  Formal version: A D4 event e is genuinely shared-process issuance if and only if
  (a) its record appears in R_n for at least k observers (quorum threshold k from AC-8),
  AND (b) the shared OnlineSchemaSys process has not terminated or been invalidated
  before e achieves quorum. Condition (b) is the ontological process-dependence condition.
current_strongest_objection: >
  This is absorbed by Byzantine fault tolerance (BFT) + trusted computing base (TCB):
  the requirement that records be valid within a continuing system is a standard
  distributed systems integrity requirement. TI's version must show what it adds
  over BFT/TCB that is not captured by standard fault-tolerance formalism.
  The candidate surplus: TI's condition is about ontological grounding of record reality
  (not just fault-tolerance), and the process requirement is about schema-extension
  legitimacy (not just message authentication).
evidence_refs:
  - explorations/E037-kill-criteria-test-cross-repo-ideas.md
next_action: >
  Run a discriminator test between BFT/TCB and TI-C022: construct a case where BFT
  guarantees record integrity but TI-C022's ontological condition is not satisfied
  (e.g., the process has terminally forked without resolution). If such a case exists:
  TI-C022 survives as adding content over BFT. If not: absorb into BFT/TCB.
  Connect to AC-8 adversarial model (incompatible schema proposals + fork-choice analog).
```

---

## Provenance Note

This run was triggered by a cross-repo research session that proposed five ideas for TI
evaluation. The anti-premature-closure rule was applied throughout: the strongest versions
of each idea were generated and tested. Two ideas (A, D) were killed as formal objects.
One (B) was split: the specific form killed, the sublinear class survived. Two (C, E) are
not absorbed and generate formal gap-fills and claim candidates.

The run does not promote TI-C021 or TI-C022. Both are speculative. Promotion requires
hostile review (per CLAIM-LEDGER.md governance: do not promote directly from speculative).
