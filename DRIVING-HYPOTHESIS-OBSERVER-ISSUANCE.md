---
artifact_type: driving_hypothesis
status: active
governance_role: lead_hypothesis
constitutional: false
last_updated_by: persona-council-synthesis-2026-06-30
---

# Driving Hypothesis: Observer-Level Issuance (the integrating idea)

Opened 2026-06-30 from a 15-persona council review (TaF persona library + an MMO-networks expert) of a Joe
hypothesis, plus the Turok/Wolfram external reading set. This is a **higher-order driving hypothesis** that
sits above three repos (GU formalization, Time as Finality, Temporal Issuance), each of which is a *component*
of it. It is incubated here in Temporal Issuance by decision, with an explicit promotion trigger (below) to
spin out into its own integration repo once its central object exists.

## Why it lives here (the pivot)

Temporal Issuance's original source-side object `SourceRealization = (C, <=_S, Ext_S)` has been under steady
absorption all reading-set long (the `action-principle-boundary-selection`, cosmological-measure, and
`observer-equivalencing-ruliad-slice` absorbers all push a *single* cosmic source residue toward the `action`,
measure, and ruliad-slice kill clauses). The council's verdict: the **one piece that does NOT reduce** to known
physics is the **issuance act and its multiplicity** -- there are *many* issuance points, one per observer.
That is this repo's territory, and it is the first thing in the reading set that *adds* to the source side
rather than absorbing it. So this driving hypothesis is what TI's source residue *becomes* once the absorbers
are granted: not a cosmic single-source issuance, but **per-observer differential issuance**.

## The hypothesis (one paragraph)

Reality is a three-layer pipeline, and the apparent binary "observers create reality vs. the substrate is
fundamental" dissolves because each layer answers a different question:

1. **Substrate / possibility-space (GU layer).** A fixed space of *possible transformations* (task-space /
   richer substrate / ruliad), which observers **access and project from** but do not author. Projection !=
   finality, permanently.
2. **Observer-level issuance (this repo's layer).** Each observer is a distinct local source endowed with a
   **differential counterfactual repertoire** -- the subset of already-possible transformations *it* can
   bring about. "Issuance at the observer level" is this multiplicity of source-points. It is **bind/select,
   never author**: observers add no matter and no new tasks; they differ in *which* possible transformations
   are available to them. The act is real but, by a Godel-type limit, **not self-certifiable from inside**.
3. **Finality -> shared reality (TaF layer).** A private binding becomes a *shared fact* not by the observer's
   say-so but **externally**: when the transformation that would reverse or privately-revise it has become
   (approximately) impossible for the relevant observer-set -- a rising reversal cost across distinct holders.
   A *globally* shared world is **not automatic**: it is the global section glued from observers' local
   finalized bindings, and it exists only when a gluing obstruction (Cech H1 of the finality sheaf) vanishes.
   Local hardening is necessary but not sufficient; co-creation can succeed locally and fail globally.

## H0 -- the falsifiable spine

> There exists a single quantitative **reversal-cost / impossibility measure `mu`** on transformations of a
> shared record, decomposable into two independent sources -- **thermodynamic (Landauer)** and
> **computational-irreducibility** cost -- such that:
> - (a) a binding is *finalized for observer-set O* iff `mu(reverse)` exceeds threshold for all observers in O;
> - (b) *shared reality* is the global section of finalized bindings, existing iff `H1` of the finality sheaf
>   vanishes;
> - (c) observer-level issuance is *differential repertoire over a fixed task-space*, NOT measure-biasing.

`mu` is the **central missing object**. The skeptic (hostile-rigor gatekeeper) and the builder (constructor
theorist) independently named the same thing: build `mu` and the idea stops being a metaphor, gains a
falsifier, and makes `H1` computable.

## Falsifiers / kill criteria for H0 (using this repo's kill classes)

- **K1 / K4 (absorption / no distinguishable claim):** if `mu` has no computational-irreducibility component
  beyond Landauer, the finality layer is pure thermodynamics -- TaF/decoherence relabeled. Kill the
  "two-source" claim.
- **K5 (metaphysical residue):** if observer-level issuance requires a modified Born rule with **no measurable
  coupling constant**, it is unfalsifiable idealism (and a G1/G3 violation -- observer-creates-outcome). Kill
  the generative reading; keep only differential-repertoire.
- **K4 (no distinguishable claim):** if `H1` is always trivial in physical observer ensembles, "shared
  reality" adds nothing over a single global record. Kill the descent layer.
- **K2 (circularity):** if "differential repertoire" cannot be specified without the observer defining the
  task-space it draws from, the loop is circular (Escher's warning). Ground it in distinct-holder record
  transfer or kill it.

A clean kill of any leg is a SUCCESS for this repo, not a loss.

## The central work-item

Construct `mu` on a finite shared-record model: compute reversal cost two ways -- (i) Landauer/graph-erasure
count and (ii) a computational-irreducibility proxy -- and test whether they are independent (two genuine
sources) or collapse (one source). This is the same object as TaF's WC-23 two-way reversal-cost benchmark and
MC-2 (computational reversal cost); coordinate, do not duplicate.

## Promotion trigger (spin-out condition)

**The day `mu` produces a falsifiable prediction** (e.g., a computed `H1` that flips with a tunable coupling,
or a two-source reversal cost that diverges measurably from pure Landauer), this driving hypothesis graduates
into its own **integration repo**, with GU / TaF / TI as its three named instances. Until then, a standalone
"grand idea" repo would be scaffolding around a non-existent object (the GU prose-checking failure mode) and is
explicitly deferred.

## Discipline (carried from the council)

- **Bind, not create.** Ban the verb "create" outside scare-quotes. Observers *select/entrench/glue* within a
  fixed possibility-space. This keeps the idea G1/G3-clean (see the proposed companion principle in
  `time-as-finality/explorations/co-creation-integration-and-g1g3-reframe-2026-06-30.md`, staged for Joe's
  sign-off -- not yet canon).
- **Equivocation guard.** "Issuance / finality / hard-to-undo" must not slide across thermodynamic,
  computational, quantum, and social senses. State which sense is in use at each step.
- **External, not self-certified.** Finality is conferred by redundancy/irreversibility across distinct
  holders, never by an observer's own attestation (Godel).
- **One-way cross-repo.** GU supplies the substrate layer only; never route GU->TaF/TI as mutual support;
  projection != finality permanently.

## Cross-links

- GU substrate layer: `gu-formalization/explorations/misc/substrate-layer-for-observer-issuance-integration-2026-06-30.md`
- TaF finality + H1-as-co-creation-failure + G1/G3 reframe proposal: `time-as-finality/explorations/co-creation-integration-and-g1g3-reframe-2026-06-30.md`
- This repo: `FORMAL-DEFINITION-REPAIR.md` (the `Ext_S` residue this elevates), `KILL-CRITERIA.md`, the three
  absorbers (`action-principle-boundary-selection`, `observer-equivalencing-ruliad-slice`, cosmological-measure note).
