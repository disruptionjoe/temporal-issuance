---
artifact_type: absorber
status: active
absorber: crypto_economic_security_literature
constitutional: false
added_by: external_persona_intake / crypto-econ-security (three-note synthesis)
companion_to: absorbers/distributed-systems.md
date: 2026-06-22
---

# Crypto-Economic Security Absorber Set

This absorber file was identified as a critical gap by a crypto-economic security researcher
persona review (three-note synthesis, 2026-06-22). The persona is distinct from the
distributed-systems architect: that persona priced consistency; this one prices finality and
adversarial issuance. The central contribution is a mechanism for the missing `mu` budget
and an economic reading of finality.

## Absorber 1: Nakamoto / Probabilistic Finality

**Threat level: MEDIUM — absorbs the "finality is observer-reconstructed" claim as a known result**

Nakamoto consensus defines finality probabilistically and per-observer: a record is "final"
for observer O when reversing it would require economic work exceeding O's threshold. This is:
- per-observer (different confirmation depths = different finalities)
- probabilistic (not absolute)
- priced (reversal cost is the measure)
- reconstructed from records (local chain view)

**What it absorbs:** TI-C019's claim that "temporal order and finality are downstream
observer-side reconstructions from records" — this is already precisely Nakamoto finality.

**What survives:** TI's claim is more specific than Nakamoto's. TI asks whether issuance
(schema expansion) is possible at all in such a system, not just whether finality is
observer-relative. Nakamoto presupposes a fixed transaction schema; the issuance question
is whether that schema can expand online.

**Key distinction:** Nakamoto finality = per-observer economic reconstruction. D4 issuance =
schema-expanding events not predefined in the transaction type system. These are orthogonal.

**Current verdict:** The observer-reconstruction claim in TI-C019 should cite Nakamoto and
specify the surplus: TI asserts schema-expansion capability, not just observer-relative
ordering. Without that surplus, "finality is observer-side reconstruction" is already known
CS/economics.

## Absorber 2: Byzantine Fault Tolerant (BFT) Finality / Accountable Safety

**Threat level: LOW for TI-C019, MEDIUM for AC-8**

BFT protocols (PBFT, HotStuff, Casper FFG) give deterministic finality under a 2/3
honest-participant assumption. Accountable safety: if finality is violated, at least 1/3
of validators can be identified and penalized. This gives:
- deterministic finality (not probabilistic)
- explicit adversary model (Byzantine faults)
- accountable failure modes

**What it absorbs:** AC-8 (multi-observer interactive schema negotiation) is close to BFT
consensus with schema changes as the proposed updates. If AC-8 is just BFT applied to
type-schema updates, it's absorbed.

**What survives:** AC-8 concerns schema *expansion* (D4-style type-novel events), not just
value consensus. BFT consensus assumes a fixed state machine; AC-8's interesting case is
when the state machine type-schema itself is the subject of consensus.

**Current verdict:** When building the AC-8 formal model, explicitly test whether the
multi-observer schema negotiation reduces to BFT applied to a fixed-schema state machine.
If yes, absorbed. If the type-novelty of schema extensions is what makes it irreducible,
that is TI's contribution to the BFT setting.

## Absorber 3: Verifiable Delay Functions (VDFs)

**Threat level: HIGH for NAA — most concrete absorber/grounding candidate for no-anticipation**

A VDF (Boneh et al., 2018) is a function `f: X -> Y` such that:
1. Sequential computation: `f(x)` requires exactly `T` sequential steps (cannot be parallelized)
2. Efficient verification: the output `y = f(x)` can be verified in polylog time
3. Uniqueness: the output is unique and deterministic

The key property: **the output cannot be computed before the sequential computation is done**.
No amount of parallel hardware can predict `f(x)` faster than `T` steps. This is a
concrete, cryptographically grounded model of "the future must be computed, not foreseen."

**Relevance to NAA:** The No-Anticipation Axiom states that operations `delta_n` and
`epsilon_n` may only reference `S_n`, `H_n`, and constructible objects — they cannot
reference future schema elements. VDFs provide a cryptographic mechanism for *why* this
must be the case: if future schema elements require sequential computation, they are
genuinely unavailable before that computation completes.

**Two possible verdicts:**

| Verdict | What it means |
|---|---|
| NAA reduces to VDF | NAA is a specific instance of VDF-style sequential computation; TI's NAA is absorbed by the VDF literature (Boneh et al. 2018, Wesolowski 2019) |
| NAA requires more than VDF | VDFs are a lower bound on NAA — they show sequential computation is one mechanism for no-anticipation, but NAA applies even to deterministic systems without sequential work; TI contributes the generalization |

**The key question:** Does OnlineSchemaSys NAA require sequential computation (VDF), or
is it a structural constraint that holds even in deterministic, non-sequential systems?
If the latter, NAA is broader than VDF and VDF is a specific mechanism, not the full concept.

**Relation to B3 (HoTT NAA derivation):** VDFs give an operational/cryptographic grounding
for NAA; HoTT gives a type-theoretic grounding. These are complementary and could converge:
type-theoretic sequential computation (HoTT's path types are sequentially constructed) may
be the mathematical analogue of VDF sequential computation.

**Action:** Include VDF as the primary cryptographic candidate for NAA grounding. Test: does
the NAA structural theorem hold for *all* prefix-indexed systems (including non-sequential
ones), or only for systems with a VDF-like computation structure? If only the latter, VDF
is the mechanism; if the former, VDF is a sufficient condition that motivates NAA but does
not exhaust it.

**Current verdict:** VDF is the most concrete and formally grounded mechanism for no-anticipation
that has been identified. It does not absorb NAA but could provide the formal anchor that
M2 (constructive type formation) currently only motivates.

## Absorber 4: Landauer's Principle and Cost of Finality

**Threat level: HIGH for `mu` — absorbs the cost-of-finality route if it adds nothing over thermodynamics**

Landauer's principle (1961): erasing/committing a bit in a computational system has a
minimum thermodynamic cost of `kT ln 2` joules. This establishes a physical connection
between information operations (writes, commits, erasures) and energy.

**Proposed `mu` route (crypto-econ intake):** If issuance funds security and security has
a thermodynamic cost (Landauer), then issuance is coupled to a cost budget. This is an
order-independent energy route: it does not go through `Ext_S` ordering (BDO/ICO closed
that path) but instead goes through the thermodynamic cost of making records final.

**Why BDO/ICO do not block this:** BDO and ICO closed the path from `Ext_S` (ordering
layer) to `p^mu` (energy-momentum). The Landauer route goes from issuance to energy via the
cost of *committing* records, not via ordering. The two paths are distinct. The TI-C009/C010
archive correctly notes "no mechanism connects `Ext_S` to energy-momentum" — but that is
the ordering route. The cost-of-finality route was never tested.

**The absorber threat:** Landauer's principle is standard thermodynamics-of-computation
(Bennett 1982, Landauer 1961). If the cost-of-finality route reduces entirely to Landauer,
it is a known result. The question is whether the *adversarial sizing* (issuance sized to
attack cost, not just to single-bit commitment) survives as something new.

**Adversarial surplus (candidate):** In Proof-of-Work, issuance (block reward) is calibrated
to the thermodynamic cost of securing the ledger against a 51% attack, not just to the cost
of committing a single bit. This sizing relation (issuance ∝ attack cost, not ∝ single-bit
cost) may be what survives where plain Landauer doesn't. But this could also just be energy
economics of hash functions.

**Current verdict:** Candidate but unearned. The Landauer cost-of-finality route for `mu`
must be tested against:
1. Standard Landauer (does TI add anything beyond single-bit commitment cost?)
2. Bekenstein-Hawking bound (does the stock limit add anything beyond holographic entropy?)
3. The adversarial sizing surplus (is issuance-sized-to-attack-cost a new relation?)

See `explorations/E023-crypto-econ-intake-synthesis.md` for the proposed fixture.

## Absorber 5: Bekenstein-Hawking / Holographic Entropy Bound

**Threat level: MEDIUM — potential stock limit for issuance budget; may be absorbed by holographic physics**

The Bekenstein bound (1973) sets an upper limit on the information content of a region of
space: `S_max = 2πkRE / (hbar c)`. This gives an order-of-magnitude entropy/information
budget for any bounded region.

**Proposed role:** If Landauer gives the flow cost (price per bit committed/finalized), the
Bekenstein bound gives the stock limit (total bits a region can hold). Together: a full
resource-accounting model for issuance with both flow and stock.

**Absorber threat:** Both Landauer and Bekenstein are existing physics. Importing them as
`mu` is adding vocabulary, not novel content. The question is whether TI's issuance concept
gives a new interpretation or application.

**Current verdict:** Note as a candidate but do not integrate without a same-neighbor-data
split showing TI's reading differs from standard holographic physics.

## Missing Component: Adversary Model

**Threat level: NOT an absorber — a missing piece in TI**

The crypto-econ persona identified that the repo has epistemic adversaries (hostile review,
null hypothesis) but no physical/causal adversary model. It proposed:

- Permanent fork = two local histories that can never be reconciled = spacelike separation /
  unhealed partition (`G_ij` obstruction = fork condition)
- Fork-choice rule = physical reading of `G_ij` reconciliation
- Lightcone = partition boundary (no coordination is possible across it)
- "51% attack on reality" = a scenario where two incompatible schema histories compete and
  cannot be resolved

This is not an absorber (no existing framework absorbs it). It is a missing formal component.

**Action:** When building the AC-8 formal model, include an explicit adversarial case:
what happens when two observers issue incompatible D4-type extensions? What determines which
one becomes part of the shared OnlineSchemaSys state? The answer should mirror T61's conflict
treatment (explicit conflict data, not silent merge) but should also state what makes
resolution possible at all — the analogue of a fork-choice rule.
