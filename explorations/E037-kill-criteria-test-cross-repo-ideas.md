---
artifact_type: exploration
status: active
exploration_id: E037
run_ref: RUN-0047
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C007
  - TI-C019
topic: kill_criteria_test_cross_repo_ideas
phase: 2B
date: 2026-06-22
---

# E037: Kill-Criteria Test — Cross-Repo Ideas A through E

## Purpose

This exploration runs each of the five cross-repo ideas against TI's KILL-CRITERIA.md to
determine whether any triggers, weakens, or sharpens an existing kill condition.

The kill criteria (from KILL-CRITERIA.md):

- **K1 (Full Absorption):** The hypothesis is fully absorbed by an existing framework, with no
  category mismatch and no residual explanatory work.
- **K2 (Circularity):** The hypothesis requires ordinary time to define its key objects.
- **K3 (No Formal Work):** The proposed object cannot produce a theorem, model, discriminator,
  pressure test, or useful failure condition.
- **K4 (No Distinguishable Claims):** All claims reduce to known physics, mathematics, or
  philosophy-of-time vocabulary without new explanatory leverage.
- **K5 (Metaphysical Residue):** The surviving language cannot be made precise enough to
  support adversarial research.

The five cross-repo ideas under test:

- **A:** lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)] as dynamics for Ext_S
- **B:** mu_M(r) = c * |r|^{3/4} (metabolically-scaled, sublinear, non-additive)
- **C:** Ostrom SES legitimacy framework: legitimacy requires balancing mechanism against increasing-returns capture
- **D:** Declining issuance curves as optimal (Jermann and Xiang tokenomics result)
- **E:** "Trust in the message requires trust in the system holding the message"

---

## Idea A: lambda*(s) = argmax_lambda [N - C - K]

### Kill Criteria Assessment

**K1 (Full Absorption):**

E034 established that `lambda*(s)` is absorbed at the structural level by MDP/optimal
control, active inference, and economic optimization. The absorption is NOT sufficient to
trigger K1 for the TI program as a whole, because `lambda*` was proposed as a candidate
dynamics equation for `Ext_S`, not as the core TI hypothesis.

However, K1 is triggered for `lambda*` as an independent formal contribution:

```text
K1 verdict for lambda* as a formal object: TRIGGERED
lambda*(s) is absorbed by MDP/optimal control with no residual.
```

This does not kill TI-C019 or the core hypothesis — it kills the specific proposal that
lambda*(s) is a novel dynamics equation for Ext_S.

**K3 (No Formal Work):**

lambda*(s) as absorbed by MDP does produce formal work — optimal control theory has a rich
formal apparatus. But the formal work is in optimal control, not in TI. The proposal to
use lambda*(s) in TI does NOT generate new TI theorems or discriminators.

```text
K3 verdict for lambda* within TI: PARTIAL
lambda* does not generate new TI-internal formal results. It imports external formalism.
```

**K4 (No Distinguishable Claims):**

The argmax selection structure does not distinguish TI from optimal control, active
inference, or economics without independent definitions of N, C, K from source admissibility.
No such definitions are provided.

```text
K4 verdict for lambda*: TRIGGERED (for the specific formulation)
All structure reduces to known optimization vocabulary without TI-specific content.
```

**K2, K5:** Not triggered. The proposal is precise and not circular.

**Overall for Idea A:**

```yaml
k1: triggered_for_lambda_star_as_formal_object
k2: not_triggered
k3: partial (no new TI-internal formal results)
k4: triggered (reduces to known optimization)
k5: not_triggered
effect_on_ti_program: weakening (imports optimization vocabulary without earning it)
effect_on_existing_claims: no_change (TI-C003, TI-C007 unaffected; Ext_S still formalizing)
recommendation: do_not_integrate_lambda_star_as_formal_object_without_source_derivation
```

---

## Idea B: mu_M(r) = c * |r|^{3/4}

### Kill Criteria Assessment

**K1 (Full Absorption):**

E035 and E036 established partial absorption: the exponent 3/4 is absorbed by WBE, but
the subadditivity property class (alpha < 1) is not absorbed by any existing TI measure
candidate.

```text
K1 verdict for mu_M with specific exponent 3/4: TRIGGERED (exponent absorbed by WBE)
K1 verdict for sublinear mu class (mu_alpha, 0 < alpha < 1): NOT TRIGGERED
```

**K3 (No Formal Work):**

E036 identified three formal additions from the sublinear mu class:
1. Subadditivity as a formal discriminator (kills additive readings)
2. Diminishing marginal issuance trajectory property
3. PP-3 discriminator candidate (size-dependent rate vs. aperture-dependent rate)

These constitute formal work: a discriminator (item 1), a trajectory prediction (item 2),
and a test surface (item 3).

```text
K3 verdict for sublinear mu class: NOT TRIGGERED
The sublinear mu class generates discriminators and test surfaces.
```

**K4 (No Distinguishable Claims):**

The specific exponent (3/4) produces claims that reduce to WBE/Kleiber without TI-specific
content. But the sublinear mu class (exponent in (0,1)) generates a claim distinguishable
from all killed candidates:

```text
Claim: mu is subadditive in a size-driven sense (not correlation-driven).
This distinguishes mu from cardinality, action, probability, and linear information content.
```

```text
K4 verdict for sublinear mu class: NOT TRIGGERED
Subadditivity class is distinguishable from named absorbers.
```

**K2, K5:** Not triggered. The sublinear mu class is not circular and can be made precise.

**Overall for Idea B:**

```yaml
k1: triggered_for_specific_exponent (3/4 absorbed by WBE)
    not_triggered_for_sublinear_class
k2: not_triggered
k3: not_triggered (generates formal discriminators and test surfaces)
k4: not_triggered_for_sublinear_class
k5: not_triggered
effect_on_ti_program: net_positive (sublinear class provides new formal candidate)
effect_on_existing_claims:
  TI-C003: narrowing_candidate (mu demotion to placeholder may be reversed by sublinear class)
  TI-C019: new_pp3_discriminator_candidate (size-dependent rate vs aperture rate)
recommendation: >
  Do not import mu_M with exponent 3/4 as a derived result.
  Formalize the sublinear mu class as TI-C021 candidate claim.
  The specific exponent must be derived or left as a free parameter.
```

---

## Idea C: Ostrom SES Legitimacy — Legitimacy Requires Balancing Mechanism Against Increasing-Returns Capture

### Kill Criteria Assessment

**K1 (Full Absorption):**

The Ostrom Socio-Ecological System framework is a well-established framework for
institutional design in common-pool resource management. The proposal is that TI's AC-8
(multi-observer interactive schema negotiation) requires a legitimacy condition that prevents
any single observer or coalition from capturing the issuance mechanism through increasing-
returns dynamics (e.g., whoever issues first establishes the standard; later entrants are
locked out).

The K1 question: is the Ostrom legitimacy condition absorbed by TI's existing formalism, or
does it add something?

Current TI apparatus for AC-8 (from E028 and E029):
- NAA (no-anticipation)
- D4 (type-novelty)
- Quorum legitimacy condition (identified in E028 as a gap)
- No formal model of increasing-returns capture

The Ostrom legitimacy condition is NOT in TI's current formal object. It is not absorbed
by NAA (NAA is about anticipation, not capture) or D4 (D4 is about type novelty, not
legitimacy). The quorum legitimacy condition identified in E028 is the closest existing
structure, but it addresses propagation thresholds, not increasing-returns capture.

```text
K1 verdict for Ostrom legitimacy: NOT TRIGGERED
Ostrom adds a formal gap identification (increasing-returns capture) not already in TI.
```

**K3 (No Formal Work):**

The Ostrom framework generates formal work for TI:

```text
Test surface: can a coalition of observers who issue first establish a lock-in that
prevents later observers from registering D4-qualifying schema extensions?

This is a formal adversarial case for AC-8 that does not appear in the current model.
```

If such a lock-in is possible in AC-8, the Ostrom legitimacy condition is a formal
requirement on the issuance mechanism — not just an institutional preference. This
generates a no-go result: if AC-8 permits lock-in, then D4 events by non-capturing
observers are not genuine shared-process extensions. They are contested.

```text
K3 verdict for Ostrom legitimacy: NOT TRIGGERED
Generates formal test surface and no-go result candidate.
```

**K4 (No Distinguishable Claims):**

The Ostrom legitimacy condition distinguishes TI's AC-8 from standard consensus protocols:
in consensus, the goal is agreement; in Ostrom-constrained AC-8, the goal is agreement
that prevents increasing-returns capture. The two are not equivalent.

```text
K4 verdict: NOT TRIGGERED
The lock-in prevention condition is distinguishable from standard consensus.
```

**K5 (Metaphysical Residue):**

The phrase "legitimacy requires balancing mechanism against increasing-returns capture" is
precise enough to be formalized:

```text
Formal version: An issuance mechanism M in AC-8 is Ostrom-legitimate if for all coalitions
C_cap, the issuance advantage of C_cap over non-members does not grow without bound as the
number of prior issuance events by C_cap increases. Equivalently: the first-mover advantage
in schema extension is bounded.
```

```text
K5 verdict: NOT TRIGGERED
The condition can be made formally precise.
```

**Does Idea C weaken any existing kill condition?**

Idea C sharpens the AC-8 model by identifying an adversarial case (increasing-returns
capture) not currently modeled. It does NOT weaken any existing kill condition. It adds
a positive formal requirement (Ostrom legitimacy) to the AC-8 model.

**Overall for Idea C:**

```yaml
k1: not_triggered
k2: not_triggered
k3: not_triggered (generates formal test surface)
k4: not_triggered
k5: not_triggered
effect_on_ti_program: positive (fills AC-8 formal gap; identifies new adversarial case)
effect_on_existing_claims:
  TI-C019: neutral_to_positive (AC-8 formalization path strengthened)
recommendation: >
  Incorporate Ostrom legitimacy condition into the AC-8 formal model as an adversarial
  test case. Define bounded first-mover advantage formally and check whether current
  OnlineSchemaSys + NAA implies it.
```

---

## Idea D: Declining Issuance Curves as Optimal (Jermann and Xiang Tokenomics Result)

### Background

Jermann and Xiang (2022) establish that declining issuance curves (where the per-period
quantity of new token issuance decreases over time) are optimal under certain economic
conditions. The proposal is that this provides formal support for declining issuance as a
design principle in TI's formal object.

### Kill Criteria Assessment

**K1 (Full Absorption):**

The Jermann-Xiang result is a tokenomics / macroeconomics result about optimal monetary
policy for cryptocurrency-like systems. It operates in an economic framework where:
- Issuance = supply of a digital asset over time
- Optimality = welfare-maximizing for agents holding the asset
- Declining curve = the result follows from monetary theory and intertemporal asset pricing

The absorbers are:
- Standard monetary theory (quantity theory of money, Fischer effect)
- Intertemporal asset pricing (discount rates, time-consistent optimal policy)
- Token economics (Bitcoin's halvening schedule as an instance)

TI's issuance is not economic issuance of digital assets. TI's issuance is the introduction
of new possibility/type-novel structure into the shared participatory process. These are
different objects:

```text
Economic issuance: d(supply) / dt
TI issuance: D4 events (type-novel schema extension events)
```

If TI were to import the Jermann-Xiang result, it would be applying an economic optimality
result to a non-economic object. This is a category mismatch risk.

```text
K1 verdict for Jermann-Xiang applied to TI: TRIGGERED
The declining-curve result is absorbed by monetary theory for economic systems. Applying
it to TI's issuance would be a category mismatch without an explicit translation.
```

**Category Mismatch Analysis:**

The proposed import maps:
- Economic issuance rate -> TI D4 event rate
- Welfare optimality -> something-like-openness optimality for TI
- Agent utility -> observer schema extension benefit

None of these mappings are earned by TI's current formalism. Specifically:
- TI has no utility function over schema extensions
- TI has no time-discounting model
- TI has no price or exchange mechanism

Without these, the declining-curve result cannot transfer.

**K3 and K4:** Not independently triggered, but the category mismatch prevents formal work
from being generated within TI.

**Positive residual:**

The Jermann-Xiang result does have a weaker contribution: it establishes that declining
issuance rates can be optimal. If TI's sublinear mu class (from Ideas B and E036) produces
a declining marginal issuance rate, and if TI can independently motivate this as a formal
requirement (not from economics, but from source admissibility), then Jermann-Xiang is
supporting evidence from an adjacent field, not a formal derivation. This is the methodology-
appropriate use: as external supporting intuition, not as a formal import.

**Overall for Idea D:**

```yaml
k1: triggered (for direct import of Jermann-Xiang as a TI result)
k2: not_triggered
k3: not_triggered_independently (but category mismatch prevents TI-internal formal work)
k4: partially_triggered (if imported without translation, reduces to known economics)
k5: not_triggered
effect_on_ti_program: neutral_to_negative (category mismatch risk if imported uncritically)
effect_on_existing_claims: no_direct_change
recommendation: >
  Do not import the Jermann-Xiang declining-curve result as a formal TI claim without
  an explicit translation from economic issuance to TI D4 events.
  Use as supporting intuition for sublinear mu motivation only.
  Record the category mismatch risk in the absorbers file.
```

---

## Idea E: "Trust in the Message Requires Trust in the System Holding the Message"

### Kill Criteria Assessment

**K1 (Full Absorption):**

This principle comes from information security and distributed systems: the integrity of
a message cannot be guaranteed without guarantees about the integrity of the system that
stores, transmits, and verifies the message. In TI's context, the claim is: trust in
issuance records (observer records of D4 events) requires trust in the shared process
(the AC-8 + OnlineSchemaSys substrate).

Potential absorbers:
- **Distributed systems security:** The principle is a restatement of Byzantine fault
  tolerance (BFT) requirements. If the system holding the message can be corrupted
  (Byzantine), the message's integrity is not guaranteed regardless of cryptographic
  protection.
- **Trusted computing base (TCB):** The trusted computing literature establishes that
  all verification reduces to an irreducible trusted base. This is the formal version
  of the same principle.
- **Information-theoretic security:** An encrypted message is only as secure as the
  key management infrastructure. The infrastructure trust requirement is standard.

These absorbers are complete for the proposition as a security or distributed systems
principle. The question is whether TI's version adds something they don't.

**TI-Specific Version:**

In TI's framework, the principle maps to:

```text
Trust in issuance records (observer records of D4 events)
  requires
Trust in the shared participatory process (OnlineSchemaSys + AC-8 legitimacy condition)
```

This is not just a security claim. It is a claim about the **ontological dependence** of
record integrity on process integrity. This goes beyond BFT, which is about fault
tolerance, and beyond TCB, which is about trusted hardware. TI's version says: the process
is load-bearing for the reality of the records, not just for their transmission.

This is closer to:
- **Social ontology** (Searle, Tuomela): institutional facts require the continuing
  validity of the institutional framework that grounds them
- **Performative record formation:** a finalized record is final only within a continuing
  process that enforces finality

These absorbers partially cover the principle, but with a notable gap: TI's claim is
about the source-side process, not merely the observer-side institutional framework.

```text
K1 verdict for Idea E: PARTIAL ABSORPTION
The security and distributed systems version is absorbed by BFT/TCB.
The ontological version (process grounds record reality) is NOT absorbed by known frameworks.
```

**K3 (No Formal Work):**

The ontological version generates formal work:

```text
Test: Can an observer construct a finalized record of a D4 event without the
shared OnlineSchemaSys continuing to be valid? If yes: records are independent of the
process. If no: the process is ontologically load-bearing for record reality.
```

This is a formal discriminator between:
- Record-independence view: finalized records are real regardless of the continuing process
- Process-dependence view: records are real only while the process is valid

The AC-8 + quorum model (E028) already points toward this: a D4 event counts as genuine
shared schema extension only if it propagates to a quorum of observers within a continuing
shared process. If the process terminates, pending events may lose their status.

```text
K3 verdict: NOT TRIGGERED
Generates formal discriminator and test surface.
```

**K4 (No Distinguishable Claims):**

The TI-specific version (process grounds record reality) is distinguishable from BFT
(which is about availability under failures, not ontological grounding) and from TCB
(which is about trusted hardware, not shared participatory processes).

```text
K4 verdict: NOT TRIGGERED for the ontological version
```

**K5 (Metaphysical Residue):**

The phrase "trust in the system" risks becoming metaphysical if left informal. But the
formal version is precise:

```text
Formal version: A D4 event e is genuinely shared-process issuance if and only if it
is recorded in R_n for at least k observers (quorum), where k is the legitimacy threshold
of the AC-8 model, AND the shared process has not terminated before e is so recorded.
The process-termination condition is the formal expression of "trust in the system."
```

```text
K5 verdict: NOT TRIGGERED if the formal version above is used
```

**Does Idea E trigger or weaken any existing kill condition?**

Idea E does NOT trigger any kill condition for TI. Instead, it:

1. Partially absorbs into BFT/TCB for the security reading (K1 partial)
2. Generates a new formal discriminator for the ontological reading (anti-K3)
3. Provides a formalization path for the quorum legitimacy condition from E028

**Effect on Existing Claims:**

The ontological version of Idea E connects to:
- TI-C019: the shared process is not just a coordination mechanism; it is ontologically
  load-bearing for the reality of issuance records. This is a strengthening of TI-C019's
  shared-participation claim, not a weakening.
- TI-C017 (Cech witness): if records are process-dependent, then the witness obligation
  W(e) for an admissible extension is not just about the extension's formal properties —
  it requires the process to remain valid at the moment of witness formation.

**Overall for Idea E:**

```yaml
k1: partially_triggered (security version absorbed by BFT/TCB)
    not_triggered (ontological version not absorbed)
k2: not_triggered
k3: not_triggered (generates formal discriminator)
k4: not_triggered (ontological version distinguishable)
k5: not_triggered (if formal version is used)
effect_on_ti_program: positive (strengthens shared-participation claim; fills AC-8 gap)
effect_on_existing_claims:
  TI-C019: strengthening_candidate (process is ontologically load-bearing for records)
  TI-C017: refinement (witness obligation must include process-validity condition)
recommendation: >
  Incorporate the ontological version of Idea E into TI-C019's shared-participation
  framing. Formalize as: D4 event records require a continuing valid shared process,
  not merely record storage. Connect to AC-8 quorum legitimacy model.
  Do not import the security version without distinguishing it from BFT/TCB.
```

---

## Kill-Criteria Test Summary

| Idea | K1 | K2 | K3 | K4 | K5 | Effect on Program |
|---|---|---|---|---|---|---|
| A (lambda*) | TRIGGERED | no | partial | TRIGGERED | no | Negative — kills lambda* as novel formal object |
| B (mu_M) | partial (exponent) | no | no | no | no | Positive — sublinear class survives; TI-C021 candidate |
| C (Ostrom) | no | no | no | no | no | Positive — fills AC-8 formal gap |
| D (Jermann-Xiang) | TRIGGERED | no | no | partial | no | Neutral/negative — category mismatch; import as intuition only |
| E (Trust=System) | partial (security) | no | no | no | no | Positive — ontological version strengthens TI-C019; fills AC-8 quorum gap |

**Kill conditions triggered for the TI program overall:** NONE

None of ideas A-E triggers a kill condition for TI as a program. The kills are targeted:
lambda*(s) as a novel formal object is killed. Jermann-Xiang as a formal import is killed.
The sublinear mu class, Ostrom legitimacy, and the ontological trust principle all survive
absorber testing with positive contributions.

**Existing kill conditions that are NOT sharpened by any of A-E:**

- K2 (circularity): No new circularity risks introduced.
- K3 (no formal work): B, C, and E all generate formal work. A generates no new TI
  formal work. D generates no TI-internal formal work due to category mismatch.

**Existing kill conditions that ARE sharpened by ideas A-E:**

- K1 is sharpened by A and D: they add to the kill discipline the recognition that
  optimization vocabulary (A) and economic results (D) face full K1 absorption when
  imported without TI-internal derivations of the key terms.
