---
artifact_type: absorber
status: active
absorber: distributed_systems_cs_literature
constitutional: false
added_by: external_persona_intake / ds-architect (three-note synthesis)
---

# Distributed Systems / CS Absorber Set

This absorber file was identified as a critical gap by a distributed-systems architect
persona review (three-note synthesis, 2026-06-22). The CS/distributed-systems literature
is closer to the TI vocabulary than most physics frameworks. Several entries are potential
near-complete absorbers for specific TI components.

## Absorber 1: Lamport Logical Clocks (1978)

**Threat level: HIGH — near-complete absorber for TI-C001 reconstruction layer**

Lamport (1978) shows that temporal order can be derived as a downstream reconstruction
from message-passing records, with no global "now" primitive. `kappa_i` (observer cadence
relation) ≈ logical/vector clocks. The "cadence without primitive time" blocker is *already
solved* in the CS literature.

**Pressures:** TI-C001 (temporal reconstruction layer), `kappa_i`.

**What it does NOT absorb:**
- TI-C019 (shared participation + ongoing issuance). Lamport gives order-from-records; TI-C019
  claims something different — that the source capacity to issue type-novel states is what makes
  the shared process open-ended. Lamport does not address whether the schema of possible message
  types can expand.
- D4 (type-novelty). Logical clocks presuppose a fixed message vocabulary. They do not address
  whether new message types can enter the schema.

**Current verdict:** TI-C001 must be compared against Lamport before claiming "temporal order
as downstream reconstruction" is a TI contribution. This is probably absorbed for TI-C001
specifically. TI-C019 and D4 survive this absorber.

**Action:** When claiming "temporal order is downstream," cite Lamport and state the surplus
over logical clock theory explicitly.

## Absorber 2: Vector Clocks (Fidge 1988, Mattern 1988)

**Threat level: MEDIUM — pressures `<=_S` and multi-observer partial order**

Vector clocks give a partial order from message-passing without a global clock. The induced
order structure is exactly the kind of structure `<=_S` was intended to capture.

**Pressures:** `<=_S` (killed as independent primitive in RUN-0024, but the reason Lamport/Fidge
already did this work should be recorded).

**Current verdict:** `<=_S` is already killed (RUN-0024). This absorber explains *why* it was
right to kill it.

## Absorber 3: CRDTs / Join-Semilattice Merge

**Threat level: MEDIUM — pressures G_ij**

Convergent Replicated Data Types (CRDTs) achieve eventual consistency via commutative,
associative, idempotent merge. The `G_ij` reconciliation maps in the TI formal object need
the same properties. If `G_ij` is a CRDT merge operation, it is absorbed.

**Pressures:** `G_ij` (reconciliation/gluing maps across observers).

**What survives:** If `G_ij` merges *schemas* (type-sets), not just values, and if the merged
schema contains type-novel content not present in either input, that is not standard CRDT merge.
CRDTs merge within a fixed type schema; D4-issuance requires schema-expanding merge.

**Current verdict:** G_ij for value-merge is absorbed. G_ij for schema-expanding merge
(D4-level) may survive, but this distinction must be made explicit.

## Absorber 4: CAP Theorem / PACELC / FLP Impossibility

**Threat level: LOW for TI-C019, HIGH for any global-consistency claim**

CAP formalizes the trade-off between consistency, availability, and partition tolerance.
The TI system being described is plainly **AP (Available + Partition-tolerant)**, not CP.
"No global finality" is just the AP posture restated.

**Pressures:** Any claim that the shared process achieves global consistency.

**What survives:** TI-C019 does not claim global consistency — it claims shared participation
under local coherence. This aligns with AP. FLP impossibility rules out deterministic consensus
in asynchronous networks with failures; TI does not rely on deterministic consensus.

**Current verdict:** No kill for TI-C019. But TI must explicitly adopt the AP posture and
not inadvertently claim CP-style global finality in the reconstruction layer.

## Absorber 5: Event Sourcing / CQRS

**Threat level: LOW — descriptive alignment, not a kill**

Event sourcing uses append-only event logs as the source of truth, with read-models
(projections) reconstructed from events. The TI observer-records layer maps directly: events
= issuance events, records = append-only logs, temporal reconstruction = read-model projection.

**Pressures:** TI-C001 reconstruction layer vocabulary.

**Current verdict:** Descriptive alignment but not an absorber — event sourcing does not address
whether the event *schema* can expand online (that is D4/issuance). It presupposes a fixed
event type vocabulary.

## Absorber 6: Abramsky–Brandenburger Sheaf-Theoretic Contextuality

**Threat level: CRITICAL — potential absorber of TI-C017 AND potential convergence result**

Abramsky and Brandenburger (2011, "The Sheaf-Theoretic Structure of Non-Locality and
Contextuality") show that quantum non-locality and contextuality are characterized by the
*obstruction to a global section* of a sheaf of local measurement outcome distributions.
A non-contextual model = a system admitting a global section. A contextual model = a system
where local sections are compatible but no global section exists.

**Why this is critical:**
The convergence theorem hypothesis (see `explorations/E021-ds-architect-convergence-theorem.md`):

```
G_ij gluing obstruction (TI-C008 residue)
  = AB sheaf contextuality (obstruction to global section)
  = NAA / no pre-existing global assignment (TI-C019)
  = OnlineSchemaSys ⊄ MetaCloSys (morphism non-embedding)
```

If these are the same theorem from different faces:
- (a) **Consolidation**: TI finds its formal home in sheaf-theoretic contextuality. This is
  GOOD — it means TI is not floating; it is a specific instance of a known formal result.
- (b) **Absorber kill**: TI-C017 (Čech witness classes) is just AB contextuality applied to
  issuance. TI contributes naming, not a new result.

**What survives in case (b):** TI's claim that the obstruction arises from *source-side
admissibility* (C-typed extensions, D4 schema-growth) rather than from quantum measurement
statistics. AB contextuality applies to any sheaf; TI would be claiming a specific sheaf
(OnlineSchemaSys extensions) where the obstruction is physically/philosophically significant
in a new way. Whether that contribution is genuine or merely a relabeling must be decided.

**Key difference from B1 (presheaf absorber):** The presheaf/Grothendieck fibration test
(B1 from RUN-0043) asks whether `OnlineSchemaSys` is a standard fibration. The AB absorber
test asks whether the NAA obstruction theorem is a standard contextuality result. These are
adjacent but distinct. Both must be tested.

**Current verdict:** AB sheaf contextuality is the most dangerous unlogged absorber. It is
also the most potentially exciting convergence result. The AB absorber test should be run
*jointly* with B1 (presheaf absorber test) since both concern the sheaf-theoretic structure
of `OnlineSchemaSys`.

**Action:** See `explorations/E021-ds-architect-convergence-theorem.md`. The B1 presheaf
absorber test should be augmented to include the AB question.

## Authority / Legitimacy Gap (not an absorber — a missing component)

The distributed-systems lens surfaces a gap in the current TI formalism: what makes an issued
type *real* rather than a private hallucination, local corruption, or unauthorized modification?

In distributed systems: authoritative server + anti-cheat + rate-limiting + validation.
In TI: no equivalent is currently specified.

This is not an absorber (no existing framework absorbs it). It is a missing piece of the
formal object. The observer-records layer needs an account of what distinguishes shared
issuance from private schema drift.

**Relation to AC-8:** AC-8 (multi-observer interactive schema negotiation) addresses this
partially — negotiated consensus about schema extensions. The authority/legitimacy question
asks what that consensus guarantees and what violation looks like.

**Action:** When building the AC-8 formal model (secondary next trigger), include an explicit
treatment of the legitimacy condition.
