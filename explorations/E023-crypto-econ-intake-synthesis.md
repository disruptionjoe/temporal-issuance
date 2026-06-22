---
artifact_type: exploration
status: active
exploration_id: E023
source: external_persona_intake (three-note synthesis, crypto-economic security researcher)
relates_to: TI-C009, TI-C010, TI-C019, TI-C020, AC-8, B3_hott_naa_derivation
companion_to: explorations/E021-ds-architect-convergence-theorem.md
date: 2026-06-22
---

# E023: Crypto-Economic Security Researcher Intake — Four Decision-Relevant Ideas

## Purpose

Three external agent notes (crypto-economic security researcher) were synthesized. Four
ideas are decision-relevant enough to record formally. This exploration captures them
without running a full steward cycle, so future runs can use them.

Not a run record. Does not update claim statuses. Records proposals for testing.

**Standing risk before any use:** Importing agents, incentives, and attackers into physics
is a stronger anthropomorphic commitment than importing consistency (the DS-architect's
contribution). The highest-risk angle (physical law as incentive-compatible mechanism,
NAA as "dominant strategy") is explicitly NOT integrated here. It remains at the level
of a vivid framing, not a formal proposal.

---

## Idea 1: VDF as NAA Formal Grounding (highest priority)

**Source:** Heterodox Angle 3 — NAA as anti-front-running security property.

**Claim:** A Verifiable Delay Function (VDF) is a concrete cryptographic model of
"the future must be computed, not foreseen." VDFs are formally defined functions
`f: X -> Y` requiring exactly `T` sequential steps regardless of parallelism, with
efficiently verifiable output. This is a sharper formal grounding for NAA than M2
(constructive type formation motivation) currently provides.

**Why this is higher-priority than B3 (HoTT derivation):** B3 tests whether NAA is
derivable from HoTT's type-theoretic structure. VDFs give an orthogonal, operationally
concrete grounding from the computation complexity side. These are complementary:
- VDF grounding: NAA holds because computing future schema requires sequential work
- HoTT grounding: NAA holds because type formation is constructive / path-sequential

Together they could provide NAA with both a computational complexity foundation
and a type-theoretic foundation, which would make M2 a genuine derivation rather
than a motivation.

**The key question to test:**
Does the NAA structural theorem (D4 co-extensive with schema-extension events inside
OnlineSchemaSys) require VDF-style sequential computation, or does it hold for all
prefix-indexed systems including non-sequential ones?

- If NAA requires sequential computation: VDF is the mechanism; NAA is a specific
  instance of VDF-style computation; `absorbers/crypto-economic-security.md` Absorber 3.
- If NAA holds even in non-sequential deterministic systems: VDF is a sufficient
  condition (motivating case) but not necessary; TI's NAA is broader than VDF; VDF
  establishes an operational lower bound.

**Relation to MEV / front-running:** Commit-reveal, encrypted mempools, and threshold
encryption all enforce no-anticipation as an explicit security invariant in adversarial
distributed systems. This re-grounds the repo's claim that NAA is "principled, not
protective" — it is protective in the precise game-theoretic sense: anticipation is an
attack. The repo's claim becomes: NAA is not merely a definitional protection for D4,
but a structural invariant that emerges from the requirement that future schema be computed
(not foreseen) in any online prefix-indexed system.

**Proposed test:**
1. Define a VDF-like sequential computation structure over schema-sequence `(S_n)`.
2. Ask: does NAA follow as a theorem from VDF-style sequential construction of `S_n`?
3. Ask: does NAA hold for systems where schema-construction is not sequential (e.g.,
   a parallel oracle that could generate `S_n` and `S_{n+1}` simultaneously)?
4. If yes on (2) and no on (3): NAA = VDF-style sequentiality; it has a concrete
   computational grounding and is not merely protective.
5. If yes on both: VDF is a sufficient but not necessary condition; find the weaker
   structural property that NAA actually requires.

**Priority:** Run this test as part of B3 (HoTT NAA derivation) or as a companion
test. The VDF question may be easier to resolve than the HoTT question and could
clarify what B3 needs to prove.

---

## Idea 2: Cost-of-Finality Route for `mu` (un-pressured path in TI-C009/C010 archive)

**Source:** Heterodox Angle 1 — `mu` as security budget, and the Landauer "rent" section.

**Claim:** The TI-C009/C010 archives are correctly narrow for the ordering-layer route.
BDO/ICO together closed: *no mechanism connects `Ext_S` (ordering) to `p^mu` (energy)*
under any Lorentzian object specification. However, there is a second route to energy that
was never tested: the cost-of-finality route.

**The un-pressured route:**
```
issuance funds security
  -> security requires making records final
  -> making records final has a thermodynamic cost (Landauer: kT ln 2 per bit)
  -> therefore issuance is coupled to energy via the cost of record commitment
```

This route does NOT go through `Ext_S` ordering. It goes through the thermodynamic cost
of *finality* — of making a record irreversible. BDO/ICO tested the ordering-to-energy
bridge. The finality-cost-to-energy bridge is independent.

**Primary absorber:** Landauer's principle (1961) and Bennett's reversible computing
framework (1982) are standard physics. If the cost-of-finality route reduces entirely to
Landauer, it is a known result. The *adversarial sizing* surplus must survive:

| Layer | Proposal | Primary absorber |
|---|---|---|
| Flow cost | Committing a record costs kT ln 2 per bit | Landauer — standard thermodynamics |
| Stock limit | Total issuable records bounded by Bekenstein | Bekenstein/holographic — standard physics |
| Adversarial sizing | Issuance sized to attack cost, not single-bit cost | Possibly new — proof-of-work economics |

**Why the adversarial surplus might not be absorbed:** In Proof-of-Work, the block reward
(issuance) is calibrated to the cost of a 51% attack, which is much larger than the cost
of committing a single transaction. This is a relational constraint between issuance and
security that is not contained in plain Landauer. If TI can formalize this relational
constraint (issuance/security budget) without importing the specific economic mechanism,
it may have a new result.

**Kill condition:** If the adversarial sizing (issuance ∝ attack cost) reduces to standard
thermodynamic path-integral/free-energy accounting or information-theoretic rate bounds,
close as absorbed and annotate TI-C009/C010 archives accordingly.

**Proposed fixture:**
1. Define a minimal formal system with issuance events and record commitments.
2. Assign a Landauer cost to each record commitment.
3. Ask: does the total issuance budget equal the total finality cost, or is there a
   surplus structure not captured by single-bit Landauer?
4. Test the adversarial sizing: does issuance = attack cost derive from anything beyond
   standard thermodynamics + information theory?
5. If yes: note the formal surplus. If no: archive the cost-of-finality route as
   absorbed by Landauer and annotate TI-C009/C010 accordingly.

**CAUTION:** Do not reopen TI-C009/C010 without a concrete fixture result. The note to
add to the archive annotations is: "The cost-of-finality route via Landauer's principle
was never tested by BDO/ICO. Test before treating the archive as covering all energy-bridge
routes."

---

## Idea 3: Finality = Priced (stronger reading of TI-C019 reconstruction layer)

**Source:** Heterodox Angle 2 — finality is economic, not logical.

**Claim:** The current TI-C019 reconstruction layer says "temporal order and finality are
downstream observer-side reconstructions from records." The economic reading is stronger:
**finality = the point at which rewriting the past costs more than the benefit of doing so.**

This is Nakamoto finality: each observer reconstructs finality as confirmation-depth ×
economic weight. There is no objective finality — only finality-relative-to-attack-cost.

**Why this is stronger:** The current TI formulation treats "finality is observer-reconstructed"
as an epistemic claim (observers build models of what happened). The economic reading adds
a *mechanism*: finality is not just perceived, it is priced. An observer's finality threshold
is the attack cost they can absorb. This is not purely epistemic — it's tied to physical
energy (Landauer) and/or capital at risk.

**Implication for TI-C019:** If the reconstruction layer is the "downstream observer-side"
layer, then the economic reading gives the reconstruction layer a precise operational content:
each observer reconstructs a finality ordering by computing the economic cost of rewriting.
This is more precise than "observers reconstruct order from records."

**Key question:** Does the economic reading of finality add content over the current
observer-reconstruction formulation, or is it just a richer vocabulary for the same thing?

The potential surplus: the economic reading requires that finality be *physical* (tied to
energy, capital, or some conserved resource) rather than merely epistemic. This would
connect the reconstruction layer to physics without going through the `Ext_S` ordering
route that BDO/ICO killed.

**Current verdict:** Note this as a stronger formulation candidate for the TI-C019
reconstruction layer, but do not update the claim without a fixture showing the surplus.

---

## Idea 4: Missing Adversary Model (formalism gap, not an absorber)

**Source:** Heterodox Angle 4 — the repo's adversary is only epistemic.

**Claim:** The repo has epistemic adversaries (hostile review, null hypothesis, local-minimum
adversary) but no physical adversary model. The crypto-econ lens proposes concrete mappings:

```
permanent fork = two local histories that can never be reconciled
               = spacelike separation / unhealed partition
               = G_ij obstruction at the strongest level

fork-choice rule = physical reading of G_ij reconciliation
                 = how an observer selects a canonical history from competing records

lightcone = partition boundary (no coordination possible across it)

"51% attack on reality" = adversarial schema issuance that competes with legitimate issuance
                        = needs a fork-choice rule to resolve
```

**Why this matters for AC-8:** AC-8 (multi-observer interactive schema negotiation) handles
the case where two observers issue *compatible* schema extensions. The adversary model asks
about *incompatible* issuance. If two observers issue incompatible D4-type extensions, what
determines which one becomes part of the shared OnlineSchemaSys state?

The current formalism is silent on this. The adversary model requires:
1. A formal definition of incompatible schema extensions (analogous to T55 conflict pairs
   in the TaF/T61 framework)
2. A fork-choice rule: given incompatible proposals, how does the shared process choose?
3. A statement of what makes that choice legitimate (not just convention)

**Relation to legitimacy gap (E021):** E021 identified the authority/legitimacy gap from
the DS-architect perspective (what makes an issued type real vs. private hallucination).
The crypto-econ adversary model sharpens this: the legitimacy condition is the answer to
"what rule makes one incompatible schema extension canonical over another?"

**Proposed fixture:** When building the AC-8 formal model, include:
- An adversarial case: two observers propose `S_{n+1}` and `S'_{n+1}` that are incompatible
  (both D4-type, but they cannot be simultaneously adopted without contradiction)
- A fork-choice analog: what determines which one wins? (Possible options: priority order,
  majority of observers, causal structure, resource cost)
- A failure case: what happens if no fork-choice rule resolves the conflict? (Permanent fork
  = two divergent OnlineSchemaSys histories from step n+1 onward)

This is not necessarily about adversarial *agents* — incompatible schema extensions can arise
from causal structure or information limits without any adversarial intent.

---

## Ideas Explicitly NOT Integrated

- **Angle 5 (physical law as incentive-compatible mechanism)** — explicitly flagged as
  highest projection risk. Importing Nash equilibria, dominant strategies, and rational agents
  into physics is a category error risk. Hold at vivid framing only.
- **"Blockchain as microcosm of reality"** — framing, not formal content.
- **Slashing conditions as physical analogues** — too engineering-specific.
- **Incentive compatibility of issuance as a physical requirement** — would require importing
  rational agency into the formal object, which TI does not currently do.
- **Toy crypto protocol** — too engineering-specific for the current formal research phase.
- **Long-term ossification / value accrual** — interesting for the research sociology question
  but not for the formal physics/math question.

---

## What This Changes

1. **B3 augmented with VDF question:** The HoTT NAA derivation (B3) should now also test
   the VDF computational grounding. Is NAA derivable from sequential type construction
   (HoTT) and/or from VDF-style sequential computation? These may be the same question.

2. **TI-C009/C010 archive annotations:** Add a note that the cost-of-finality route
   (Landauer) was never tested by BDO/ICO. The archive is narrow: it covers the
   ordering-layer route only.

3. **AC-8 formal model includes adversarial case:** When building the AC-8 formal model,
   include incompatible schema extension proposals and an explicit fork-choice analog.

4. **New absorbers file:** `absorbers/crypto-economic-security.md` created with 5 entries
   (Nakamoto finality, BFT/accountable safety, VDFs, Landauer, Bekenstein).

5. **No claim status changes.** These are proposals for testing, not results.
