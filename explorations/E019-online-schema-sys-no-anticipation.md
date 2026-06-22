---
artifact_type: exploration
status: active
exploration_id: E019
run_ref: RUN-0042
claim_refs:
  - TI-C019
  - TI-C020
topic: online_schema_sys_no_anticipation_axiom
phase: 2B
---

# E019: OnlineSchemaSys and the No-Anticipation Axiom

## Purpose

RUN-0039 produced D4. RUN-0040 killed the unqualified categorical no-go. RUN-0041 killed the
infinite-regress rescue. The surviving position is that D4 discriminates issuance only inside
an explicit comparison class — online, prefix-presented systems where hidden future schema is
excluded. This run formalizes that class as `OnlineSchemaSys`, tests the no-anticipation axiom
(NAA) against eight adversarial cases, and settles whether NAA is principled or merely
protective. It does not protect D4; it attacks NAA with the full adversarial suite.

## Formal Definition: `OnlineSchemaSys`

An `OnlineSchemaSys` is a tuple

```text
O = (N, H, S, A, delta, epsilon, R)
```

where:

- `N` — a totally ordered set of prefixes (the run of the process);
- `H_n` — the history at prefix `n`: a finite record of all states and schema-extension events
  up to and including `n`;
- `S_n` — the available schema at prefix `n`: the set of type-descriptors currently admissible
  as state-types, formally a set of type-labels constructible from `H_n` and `S_{n-1}`;
- `A_n ⊆ S_n^*` — the admissibility predicate at `n`: which finite sequences of `S_n`-typed
  states are admissible at prefix `n`;
- `delta_n : A_n → Dist(S_n^*)` — the transition function at `n`: maps admissible state
  sequences to distributions over `S_n`-typed next states (may be deterministic);
- `epsilon_n : (H_n, S_n) → P(TypeLabels)` — the schema-extension function at `n`: determines
  which new type-labels, if any, enter `S_{n+1} \ S_n`; must produce only labels constructible
  from `H_n` and `S_n`;
- `R_n : H_n → OrderRel(H_n)` — the observer reconstruction function: imposes a temporal or
  causal order on `H_n` from record content alone.

**No-Anticipation Axiom (NAA):**

For all `n in N` and for each of `delta_n` and `epsilon_n`:

> The function may reference only `S_n`, `H_n`, and objects constructible from `S_n` and
> `H_n`. It may not quantify over, sample from, encode, select against, or condition on any
> type-label, type-descriptor, schema element, or generator kind belonging to `S_m` for any
> `m > n`.

NAA is a constraint on what information the transition and schema-extension functions may use,
not on what the system's outputs will be. It is a condition on the information boundary of the
process operations, not a claim about what will eventually exist.

### What NAA Does Not Say

NAA does not say there are no future schemas. It says the current prefix's operations cannot
use future schemas. A God's-eye description of the system might know all future `S_m`; NAA
concerns only what `delta_n` and `epsilon_n` may reference.

NAA does not prohibit computability of `epsilon_n`. `epsilon_n` may be a perfectly computable
function of `H_n` and `S_n`. Its outputs are computed over present information, not over future
schemas.

### Morphisms in `OnlineSchemaSys`

A morphism `f : O → O'` is a prefix-order-preserving family of maps

```text
f_n : (H_n, S_n) → (H'_{phi(n)}, S'_{phi(n)})
```

where `phi : N → N'` is order-preserving, such that:

1. `f_n` preserves admissibility: if `alpha in A_n` then `f_n(alpha) in A'_{phi(n)}`;
2. `f_n` preserves transitions up to distribution: `f_n ∘ delta_n = delta'_{phi(n)} ∘ f_n`
   where defined;
3. `f_n` preserves schema availability: `f_n(S_n) ⊆ S'_{phi(n)}`;
4. `f_n` preserves schema-extension events: if `S_{n+1} \ S_n != empty` then
   `S'_{phi(n+1)} \ S'_{phi(n)} != empty` with the image types entering correspondingly;
5. `f_n` preserves observer reconstruction structure: `f_n` respects the ordering `R_n`.

**Key:** morphisms preserve the *availability structure* of schemas at each prefix. There is no
morphism in `OnlineSchemaSys` that flattens availability indexing, because any such map would
fail condition (3) for prefixes where a schema element is available in the target but not the
source at the same index.

## D4 Inside `OnlineSchemaSys`

**D4 restated for `OnlineSchemaSys`:**

An issuance event at prefix `n` is any `epsilon_n` event with `S_{n+1} \ S_n != empty`. Such
an event is a *genuine issuance event* if:

(i) the new type-labels in `S_{n+1} \ S_n` are not instances of any type in `S_n`; and
(ii) the new type-labels are not determined by `delta_n` alone.

**Theorem (D4 co-extension inside OnlineSchemaSys):**

Inside any `OnlineSchemaSys` satisfying NAA, conditions (i) and (ii) are both automatically
satisfied by any `epsilon_n` event.

*Proof sketch:*

Condition (i): `epsilon_n` produces labels in `S_{n+1} \ S_n` by definition of schema
extension. These are not in `S_n` by construction. They are not instances of types in `S_n`
if "instance" means "element of the extension of a type in `S_n`" — this is guaranteed by the
partition `S_{n+1} = S_n ∪ (S_{n+1} \ S_n)` where the new elements are defined as not already
in `S_n`.

Condition (ii): `delta_n : A_n → Dist(S_n^*)` maps into `S_n`-typed outputs. It cannot
output elements of `S_{n+1} \ S_n` because those labels do not exist in its codomain at `n`.
Any element of `S_{n+1} \ S_n` can only enter through `epsilon_n`, a separate operation at a
different level (type-label level, not instance level). NAA ensures `delta_n` has no access to
future schema elements to pre-generate them.

Therefore, inside `OnlineSchemaSys`, every schema extension event is automatically a D4-type
issuance event. D4 and `epsilon_n`-events are co-extensive in this class.

This is the key structural result: NAA does the work that D4(ii) was trying to do at the
instance level. Once we are inside `OnlineSchemaSys`, D4(i) (type-novelty) is the single
meaningful condition; (ii) is structural rather than a separately required check.

## Adversarial Cases: Full Suite

Testing whether NAA actually excludes each adversarial case, or only stipulatively bars it.

### AC-1: Completed Library of All Future Schemas

**Structure:** All future schemas `S_m` for `m > n` are fixed in a global library `L` present
at the start. `epsilon_n` simply "reveals" the next element of `L`.

**NAA assessment:** If `epsilon_n` reads from `L` to determine `S_{n+1}`, it is quantifying
over type-labels not in `S_n` — a direct NAA violation. If `L` is external to `epsilon_n` and
unavailable to it, the system still satisfies NAA (the library exists but is not accessible to
operations). In the latter case, `epsilon_n` must generate `S_{n+1}` from `H_n` and `S_n`
alone, which is the `OnlineSchemaSys` behavior.

**Verdict: absorbed at the description level, not at the process capacity level.** The
completed library is an external description. For a theory whose organizing question is present
source capacity, the library is the wrong level of analysis. The library tells you what will
exist; it does not characterize what the process can do now. This distinction is not
stipulation — it is what TI's organizing question is asking.

### AC-2: Hidden Random Seed

**Structure:** A seed `sigma` is fixed at the start. `S_{n+1} = f(S_n, sigma, n)` for a
computable `f`. The process does not know `sigma`.

**NAA assessment:** `sigma` is not in `H_n` or constructible from `S_n` and `H_n`. So
`epsilon_n` cannot compute `f(S_n, sigma, n)` — it has no access to `sigma`. From inside the
process, schema extensions appear as genuine novelty. From outside, they are fixed by the seed.

**The deep pressure point:** A hidden-seed world and a genuine-issuance world are
operationally indistinguishable from inside the process. Is NAA a principled distinction or
a definitional barrier?

**Verdict: epistemic novelty, not ontological issuance — but this is the right verdict for
TI's comparison class.** If TI is asking about present source capacity, a hidden-seed process
does not have present capacity to produce `S_{n+1}` — it is executed by `sigma` acting through
the physics, not generated by the process's present state. Whether the seed is "real" or TI's
issuance is "real" is a deeper metaphysical question. But for TI's purposes, the operational
distinction is: does the current prefix's operations determine `S_{n+1}`? With a hidden seed,
the answer is no — the seed does it. This is still a genuine operational difference.

The distinction between "determined by seed outside the process" and "determined by nothing
available at the current prefix" is not merely definitional. It tracks the causal structure of
what-does-the-work. A hidden-seed world has a specific causal story. A genuine-issuance world,
under TI, is one where the shared process itself introduces novelty with no prior hidden cause.
That is what TI is trying to characterize. Excluding hidden seeds is not protective — it is
correct given TI's research question.

### AC-3: Universal Grammar with Delayed Reveal

**Structure:** A fixed universal grammar `G` generates all possible schemas. Each step reveals
the next `G`-generated schema.

**NAA assessment:** If `G` is accessible to `epsilon_n`, it can derive `S_{n+1}` by running
`G` forward — a NAA violation (the output types were already specified by `G`). If `G` is
inaccessible, this collapses to AC-2 (hidden seed = grammar `G`).

**Verdict: absorbed if G is accessible; hidden-seed case if inaccessible.** The interesting
sub-case is: what if `G` is accessible but not fast enough to enumerate the next schema in
time? Then at the operational level, the process cannot use `G` to pre-determine `S_{n+1}`,
and NAA applies. This converges on the constructive motivation (M2 below): types must be
constructible in bounded time, not merely exist in an enumerable grammar.

### AC-4: Meta-Rule "New Type Appears at Step n"

**Structure:** An explicit rule `R : N → TypeLabels` assigns a type to each step.

**NAA assessment:** If `R` is accessible to `epsilon_n`, then `epsilon_n` is computing
`R(n+1)` to generate `S_{n+1}`. But `R(n+1)` outputs a type-label that was not in `S_n`.
Question: is this a NAA violation?

NAA says `epsilon_n` may not reference type-labels from `S_m` for `m > n`. `R(n+1)` produces
a new type-label. Is that label "from `S_{n+1}`" — a circular dependency — or is it freshly
generated?

**The level distinction is decisive:** If `R` maps step indices to type-labels and those
labels are newly constructed (not drawn from a pre-existing type-store), then `epsilon_n`
is generating new type-labels from current information (`n`), not importing them from a future
schema. This satisfies NAA: the new label is constructed at prefix `n`, not pre-loaded from
future state.

If instead `R` maps to pre-existing labels in a global library (AC-1 again), NAA is violated.

**Verdict: satisfies NAA if the meta-rule constructs new labels from current information;
violates NAA if it imports pre-existing labels from a global store.** This is a principled
distinction, not a technicality.

### AC-5: Observer Lacks Access, God's-Eye Has All

**Structure:** Externally, all schemas are fixed. The observer inside the process cannot see
them.

**NAA assessment:** This is AC-1 from the inside. The external description is a completed
library; the process operations satisfy NAA because they don't have access.

**Verdict: same as AC-1.** The God's-eye view is an external description; it is not the
right level for TI's research question. This is not a protective move — TI is explicitly a
theory of shared observer participation. An omniscient external description is excluded from
TI's comparison class by the content of the hypothesis, not by protective stipulation. The
research question is about what embedded observers and the shared process can do, not about
what can be described from outside.

### AC-6: Compression Case — Fixed but Incomputable

**Structure:** The sequence `S_0, S_1, S_2, ...` is fixed (no ontological novelty) but
algorithmically incomputable from any finite prefix.

**NAA assessment:** `epsilon_n` is constrained to use `H_n` and `S_n`. If the mapping from
`(H_n, S_n)` to `S_{n+1}` is incomputable, then there is no computable `epsilon_n` that
generates it. Does the sequence still arise?

This is the most subtle case. The sequence is fixed by some mathematical fact (like Chaitin's
Omega). It has a definition. But no algorithm running on `H_n` and `S_n` can compute it in
finite time.

**Verdict: partial absorption, with a real residue.** If no computable `epsilon_n` produces
`S_{n+1}` from `H_n` and `S_n`, then the schema extension is either: (a) produced by a
non-computable process external to `epsilon_n` (placing it outside `OnlineSchemaSys`); or (b)
genuinely not determined by any process available at prefix `n`, which looks like issuance.

The distinction between "incomputable-but-fixed" and "genuinely undetermined" is philosophically
deep and currently unearlied in TI. This case shows where TI must eventually connect to
computability theory, randomness theory, or quantum indeterminacy. For now, the honest answer
is: incomputability does not equate to issuance, but it does show one way the physical world
could exhibit `OnlineSchemaSys`-style behavior without requiring non-physical primitives.

### AC-7: Pseudorandom Schema Extension

**Structure:** `S_{n+1}` is generated by a PRNG seeded at the start.

**Verdict: same as AC-2 (hidden seed).** The PRNG seed is a fixed prior cause outside the
current prefix. From inside the process, schema extensions appear novel; from outside, they
are determined. The analysis is identical to AC-2.

### AC-8: Genuine Interactive Schema Negotiation

**Structure:** Multiple observers jointly construct `S_{n+1}` through interaction at prefix
`n`. No single observer or external God's-eye view pre-specifies the schema. The schema
emerges from the joint process.

**NAA assessment:** Each observer satisfies NAA individually (their operations use only their
local `H_n` and `S_n`). The joint process produces `S_{n+1}` through a protocol that no
single party pre-determined.

**Verdict: this is the genuinely issuance-favorable case, and it survives NAA cleanly.**

Multi-observer interactive schema construction is exactly what TI's "shared participatory
process" describes. No single observer's `epsilon_n` anticipates the joint outcome; the joint
outcome emerges from coordinated prefix-n operations across participants. This is not a
hidden-seed case (no seed fixes the outcome in advance), not a completed-library case (no
library pre-specifies the joint result), and not a meta-rule case (no rule over step indices
determines what emerges).

This is the strongest case for genuine issuance: multiple bounded observers, each operating
only from present information, jointly producing type-novel schema through a shared process that
none of them unilaterally determined.

TI's hypothesis is precisely that this is the structure of physical reality. AC-8 shows that
`OnlineSchemaSys` has room for this interpretation.

## Independence Test: Is NAA Principled?

Four candidate motivations. The question: does each provide *independent* reason for NAA, or
does each require NAA to already be true?

### M1: Observer Embeddedness and Causal Locality

An observer embedded in a physical process can only receive information that has causally
reached them. At prefix `n`, the observer's light cone contains only events in `H_n`. Future
schema elements in `S_{n+1}` have not yet causally propagated to the observer.

**Independence assessment:** This motivation is real but currently circular for TI. It imports
causal locality — itself a physical structure TI has not yet derived. Using causal locality to
justify NAA would make TI's foundation conditional on physics TI is trying to explain.

**Verdict: partially motivated, causal-structure-dependent.** Not available as a
foundation for TI at the current stage. But it points to where TI should eventually land: once
TI connects to physics, causal locality may provide a derived justification for NAA, making the
circle close non-circularly. The order is: TI → physics → causal locality → NAA derived.
For now, M1 is a promissory note, not a current justification.

### M2: Constructive Type Formation

In constructive type theory (Martin-Löf, Calculus of Constructions, HoTT), a type must be
*introduced* by a type-formation rule before any term of that type can be constructed or
referenced. Types are not pre-existing Platonic objects; they are introduced by formation
events.

Under this reading, `S_n` is the set of types that have been formed by prefix `n`. A "future
schema element" that has not yet been introduced by any `epsilon_m` for `m <= n` is
constructively non-existent — not merely unknown, but not yet a type. NAA is then not a
restriction on what `epsilon_n` may use; it is a statement about what exists to be used.

**Independence assessment:** This motivation is principled and independent of TI-specific
assumptions. It draws on a coherent and well-established framework (constructive type theory)
that does not presuppose TI. NAA under M2 says: future type-labels are not yet types, so
`epsilon_n` could not reference them even if it tried.

The key implication: a completed library of all future schemas (AC-1) is constructively
incoherent. Types in the library that have not yet been formed are not types. They are
descriptions of types-to-be-formed, which is a different (and higher-type) thing.

**Verdict: NAA is independently motivated by constructive type formation. Not merely
protective.** This is a genuine philosophical grounding, not a stipulation.

**Limitation:** This commits TI to a constructive reading of types. If physical types are
Platonic objects that exist independently of formation events, M2 fails. TI must eventually
take a position on this — and doing so connects TI to philosophy of mathematics and physics.

### M3: Record Formation Structure

Records can only be made of events that have occurred. H_n is a record of what has happened
up to prefix n. A record at prefix n cannot contain information about S_{n+1} because S_{n+1}
has not yet occurred.

This is not a claim about physics; it is a structural claim about what records are. A record
is a representation of past events. No record of prefix n can contain information about events
at prefix n+1, because those events have not yet been recorded. This is prior to any physical
theory.

**Independence assessment:** This motivation is principled and pre-theoretic. It requires only
that `H_n` is a record of past events, which TI already posits (TI-C001's reconstruction layer
is built on records). Given TI's architecture, M3 is not an additional assumption — it follows
from TI's own definition of what histories and records are.

**Verdict: NAA is independently motivated by the structure of records, and this motivation is
internal to TI's own framework.** M3 does not import external frameworks; it follows from TI's
posit that observer histories are record-based. This is the strongest available motivation
because it is both principled and non-circular with respect to TI.

### M4: The Research Question's Framing

TI's organizing question is: "Why does reality remain capable of producing genuinely new
structure?" This is inherently a question about *present source capacity* — what can the shared
process do right now, from its current state.

An omniscient completed-domain description answers a different question: "What will exist?"
That is a different question from "What can the process produce now?" These are not equivalent
questions, and answering the second is not the same as answering the first.

The comparison class for TI should contain systems characterized by their present capacity,
not systems characterized by external descriptions of their full trajectory. This is a
methodological boundary imposed by the research question, not by a desire to protect D4.

**Independence assessment:** This motivation is principled by the content of the hypothesis
itself. The comparison class is set by what the hypothesis is asking, not by what would be
convenient. Excluding completed-domain descriptions is not protective — it is correct given
what TI is about.

**Verdict: NAA is independently motivated by the research question's framing.** This is a
weaker form of independence than M2-M3 (it depends on accepting TI's framing as legitimate),
but it is not circular — it does not assume NAA is true to derive NAA.

### Independence Test Summary

| Motivation | Independent of TI? | Avoids circularity? | Verdict |
|------------|-------------------|---------------------|---------|
| M1: Causal locality | No — imports physics | Circular until TI earns physics | Promissory |
| M2: Constructive type formation | Yes | Yes — draws on CTT | Principled |
| M3: Record formation structure | Internal to TI | Non-circular — follows from TI's own posits | Principled |
| M4: Research question framing | Depends on TI framing | Non-circular given the question | Principled |

**Result: NAA is independently motivated by M2, M3, and M4. It is not merely protective.**

The protective-axiom reading fails because M2 provides a foundation entirely independent of TI
(constructive type theory) and M3 provides a foundation internal to TI that does not assume
NAA. A protective axiom is one that exists only to prevent falsification of the main claim;
NAA is motivated by the structure of types (M2) and records (M3) regardless of whether one
accepts issuance.

## Embedding Test: `OnlineSchemaSys` → `MetaCloSys`

RUN-0040 showed that a completed-history encoding embeds *objects* of `OnlineSchemaSys` into
`MetaCloSys`. The question is whether the embedding extends to morphisms.

**Forgetful embedding attempt:**

Define `F : OnlineSchemaSys → MetaCloSys` by taking `O = (N, H, S, A, delta, epsilon, R)` to
the `MetaCloSys` object `M = (Mu, ObjSchema, Gen, K)` where `Mu` contains all schemas in
`{S_n : n in N}` and `K` encodes the full transition + schema extension trajectory.

**What the morphism structure requires:**

An `OnlineSchemaSys` morphism `f : O → O'` preserves schema-availability at each prefix.
Specifically: if type-label `alpha in S_n` then `f_n(alpha)` is available at the corresponding
prefix in `O'`.

A `MetaCloSys` morphism `g : M → M'` preserves the fixed meta-schema: `g` maps types to types
in `Mu'` preserving the meta-schema and transition rules.

**The obstruction:**

Schema availability at a prefix is *not* a concept in `MetaCloSys`. In `MetaCloSys`, all types
in `Mu` are always available. There is no prefix-indexed availability structure.

A morphism in `MetaCloSys` that represents "alpha is available at prefix n" would need to
encode the availability indexing as data in the meta-schema. But then the meta-schema contains
the availability indexing, which is `OnlineSchemaSys` structure encoded inside `MetaCloSys`
objects — not an embedding of categories but a representation of `OnlineSchemaSys` inside a
larger `MetaCloSys` object.

**Formal statement:**

There is no fully faithful functor `F : OnlineSchemaSys → MetaCloSys` that preserves
morphism structure, because:

1. `OnlineSchemaSys` morphisms preserve schema availability at prefixes (condition 3 of the
   morphism definition);
2. `MetaCloSys` morphisms have no availability structure to preserve;
3. any `MetaCloSys` morphism corresponding to an `OnlineSchemaSys` morphism must drop the
   availability information, making `F` fail full faithfulness.

**What this means:** `OnlineSchemaSys` is not a subcategory of `MetaCloSys`. It is a
categorically distinct structure. The embedding kills the availability structure, and
availability is precisely what makes D4 track something in `OnlineSchemaSys`.

This is a stronger result than RUN-0040's completed-history finding: object-level encoding
works (you can describe an `OnlineSchemaSys` object inside a large enough `MetaCloSys` object),
but morphism-level embedding fails (the morphism structure of `OnlineSchemaSys` is lost).

The distinction is the difference between:
- "I can describe X in terms of Y" (encoding, always possible with enough Y)
- "X is a subcategory of Y" (categorical embedding, requires morphism preservation)

`OnlineSchemaSys` is encodable inside `MetaCloSys` at the object level. It is not embeddable
at the morphism level without loss.

## Verdict Labels

Applying the suggested verdict labels:

**NAA: `principled_online_constraint`**

NAA is independently motivated by M2 (constructive type formation), M3 (record formation
structure), and M4 (research question framing). It is not merely a protective axiom. The
protective-axiom reading (`protective_axiom_only`) is defeated by M2 and M3.

**D4 inside `OnlineSchemaSys`: `survives_as_observer-relative_issuance`**

D4 is not an absolute metaphysical primitive (defeated by RUN-0040 and RUN-0041). But within
`OnlineSchemaSys`, D4 is co-extensive with schema-extension events and is structurally
motivated (not merely definitionally stipulated). The label `survives_epistemically_not_ontologically` is too weak: M2 gives a constructive ontological motivation, and M3 gives a
record-structural motivation. The right label is `survives_as_observer-relative_issuance`.

**`OnlineSchemaSys` vs. `MetaCloSys`: `formalizing_candidate`**

The morphism-level non-embedding result is a concrete categorical fact. It is not a theorem
about absolute physical reality, but it is a precise result about the category structure. This
supports moving the characterization of TI-C019 toward `formalizing_candidate` status.

## Effect On TI-C019

TI-C019 is updated from "weakened" to a more precisely stated speculative claim:

**Updated strongest version:**

> Issuance under D4 inside `OnlineSchemaSys` is principled by constructive type formation
> (M2) and record formation structure (M3), not merely protective. NAA follows from what kind
> of system TI is describing: one where histories are records and types are formed, not one
> where all possible types pre-exist in a Platonic library. Schema-extension events in
> `OnlineSchemaSys` co-extend with D4 events by the NAA structural theorem. `OnlineSchemaSys`
> is categorically non-embeddable in `MetaCloSys` at the morphism level, giving a concrete
> categorical fact about the distinction. The genuine issuance case (AC-8: multi-observer
> interactive schema negotiation) survives all adversarial pressure cleanly.

**Updated status: speculative, with formalizing-candidate trajectory.**

TI-C019 is not promoted (promotion requires hostile review). But it is no longer merely
weakened without direction. The precision pass is complete: NAA is principled, D4 is
class-relative but not merely protective, and the categorical distinction is real at the
morphism level.

**What remains for promotion to formalizing:**

Hostile review must test whether:
1. M2 (constructive type formation) can be formalized precisely enough to derive NAA rather
   than just motivate it;
2. The morphism-level non-embedding result holds under a precise category-theoretic proof
   (not just a proof sketch);
3. The AC-8 case (multi-observer interactive schema negotiation) can be modeled formally as
   a concrete `OnlineSchemaSys` object.

## New Claim: TI-C020

This run identifies a new speculative claim that separates TI-C019's philosophical architecture
from its physical application.

**TI-C020:** The physical universe, as an observer-participatory process, is an instance of
`OnlineSchemaSys`: its state evolution involves prefix-indexed schema growth satisfying NAA,
where the no-anticipation constraint is grounded in the physical structure of causal propagation,
quantum measurement dynamics, and/or cosmological boundary conditions.

Status: **speculative**.

This claim is the bridge between TI-C019 (issuance is a principled concept in an appropriate
class) and the physics target (the universe actually exhibits issuance). Without TI-C020, TI
describes a possible architecture for reality but has not argued that physical reality falls
within that architecture.

TI-C020 should be pressured against:
- Whether quantum mechanics implies NAA (no-cloning, causality of measurement);
- Whether causal set theory's growth dynamics resemble `OnlineSchemaSys` schema extension;
- Whether cosmological horizon structure provides a physical basis for prefix indexing;
- Whether the holographic principle or other boundary theories provide a version of M1
  (causal locality) that TI can earn non-circularly.

## What Was Killed

- The reading of NAA as "merely protective" is defeated by M2 and M3.
- The strong claim that D4 is an ontological primitive independent of comparison class remains
  killed (from RUN-0040-0041).

## What Survived and Strengthened

- `OnlineSchemaSys` with NAA is a principled comparison class, not a definitional barrier.
- D4 inside that class is co-extensive with schema-extension events (the NAA structural theorem).
- The morphism-level non-embedding of `OnlineSchemaSys` into `MetaCloSys` is a concrete
  categorical result.
- AC-8 (multi-observer interactive schema negotiation) is the cleanest issuance case and
  survives all adversarial pressure.
- TI-C020 is a new tractable speculative claim distinguishing TI-C019's conceptual architecture
  from its physical application.

## Next Targets

**Primary — Formalize M2 and the morphism-level non-embedding:**

Derive NAA formally from constructive type formation (M2). Produce a precise categorical proof
that `OnlineSchemaSys` morphisms do not factor through `MetaCloSys` morphisms. This moves
TI-C019 from speculative with formalizing-candidate trajectory to fully formalizing.

**Secondary — AC-8 formal model:**

Build a concrete `OnlineSchemaSys` object representing two observers engaged in interactive
schema negotiation. Show that the joint output satisfies D4 at the schema level while each
individual observer satisfies NAA. This is the first concrete multi-observer TI model.

**Tertiary — TI-C020 pressure:**

Test TI-C020 against quantum no-cloning / causality and causal set growth dynamics. Ask
whether either provides a physical grounding for NAA without importing ordinary time as a
primitive. This is the first step toward the issuance-physics bridge from the architecture
side rather than the physics-derivation side (the prior runs tried the physics-derivation
direction and hit BDO/ICO; this approach starts from the architectural requirements).
