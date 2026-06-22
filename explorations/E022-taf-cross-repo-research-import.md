---
artifact_type: exploration
status: active
exploration_id: E022
source: time-as-finality repo (cross-repo import, 2026-06-22)
relates_to: TI-C017, TI-C019, TI-C020, B1_presheaf_absorber, AC8_formal_model
note: TaF and TI ledgers do NOT merge. This is a research import only.
date: 2026-06-22
---

# E022: Time-as-Finality Cross-Repo Research Import

## Purpose

Three findings from the `time-as-finality` (TaF) repo are directly relevant to the
current temporal-issuance research state. This exploration imports them without merging
ledgers, changing claim statuses, or importing TaF's hypotheses.

The TaF relationship to TI (from the TaF bridge note, `temporal-issuance-bridge-v0.1.md`):

```text
Temporal Issuance supplies candidate source dynamics.
Time as Finality supplies observer-indexed readout and falsification tests.
Capability Projection asks what the readout preserves or loses.
```

TI does not inherit TaF verdicts and TaF does not inherit TI verdicts.

---

## Import 1: N13 Absorber Map for Y_TI Components

Source: `time-as-finality/literature/N13-temporal-issuance-absorber-map.md`

This is the most immediately actionable import. The TaF repo ran a rigorous absorber
comparison of the TI formal object `Y_TI = (R, <, mu, dR, O_i, kappa_i, A_i, G)` against
the closest neighboring theories. Result: every component has a named absorber unless a
non-circular, same-neighbor-data split survives.

### N13 Absorber Table (adapted for TI repo context)

| TI component / move | Standard absorber | What TI must specify before claiming residue |
|---|---|---|
| `<` as realization order | Relativistic causal order or causal-set order. Locally finite partial order with counting geometry is already the causal-set starting point. | Whether `<` is ordinary causal precedence, causal-set order, a dependency order not reducible to causality, or an operational construction. If causal, record as absorbed. |
| Sequential issuance generates novelty | Causal-set sequential growth uses stochastic birth; label/birth order is not automatically physical. Covariance and label-independence are native discipline. | A label-invariant observable, not a hidden birth-label frontier. Any global sequence must be shown not to smuggle in a preferred foliation. |
| `mu` measures issuance | Counting measure / volume in causal sets; entropy production, work, free energy, path probability in stochastic thermodynamics; Shannon entropy or statistical complexity in information theory. | Units, transformation behavior, operational comparison, and a same-neighbor-data split after volume/counting, thermodynamic, and information variables are matched. |
| `dR` is a local frontier | Cauchy surfaces, causal diamonds, domains of dependence, observer horizons, causal-set stems / past sets. A global frontier reintroduces a hidden present. | A local, covariant boundary/access object with no preferred global slice and no hidden observer-independent present. |
| `kappa_i` is observer cadence | Proper time, detector sampling rate, clock synchronization, measurement protocol, record-channel bandwidth. | Whether cadence is a physical clock/sampling variable already owned by instrumentation and relativity, or a new source-side field. |
| Records certify issuance | TaF record reconstruction, provenance, observer access, gluing. If records define issuance, the source/readout relation is circular. | A source-to-record generation map where issuance is defined without using finality, stabilized records, or observer reconstruction as primitives. |
| Gluing recovers global order | TaF colimit/descent and causal-set reconstruction. Unglued local records do not determine global order. | Explicit identity/overlap/gluing data plus a check that recovered global object is not just ordinary causal completion of the neighbor theory. |

### N13 Same-Neighbor-Data Vector

Before claiming any bridge to physics, TI must freeze this vector and show that candidate
systems differ in a way that is NOT explained by the absorber owning one of these fields:

```text
(causal order,
 spacetime or causal-set volume/counting data,
 observer worldlines/access regions,
 detector sampling/cadence,
 thermodynamic path and reservoir ledgers,
 information-state and compression/statistical-complexity ledgers,
 record-generation rule,
 gluing/identity data,
 gauge/label/foliation convention)
```

If two candidate source systems differ in any of these fields, the difference belongs
to the absorber until TI explains why that field is not legitimate same-neighbor data.

### N13 Promotion Gate (imported as TI pressure condition)

TI's issuance-energy-cosmology bridge can become more than translation residue only after:

1. `<` explicitly typed as ordinary causal order OR explicitly shown not reducible to it.
2. `mu` has units, operational meaning, transformation behavior, and comparison rule.
3. `dR` / local frontier is covariant or label-invariant and does not select a preferred present.
4. `kappa_i` is not hiding ordinary clock, detector, or channel-bandwidth data.
5. Source-to-record generation map that does not define issuance through finality or reconstruction.
6. Positive preservation controls and hostile same-neighbor-data splits after causal, thermodynamic, information, and gluing variables are matched.
7. A declared capability object that is not just "recover the hidden issuance variable."

**Relation to current TI state:** D4 (type-novelty) is TI's attempt to satisfy conditions
1 and 2 by replacing `<` and `mu` with schema-extension events and type-schema growth. The
open question is whether schema-extension is just causal order / information state / CSG
growth with new vocabulary — which is exactly what B2 (Assembly Theory operationalization)
is trying to test empirically.

---

## Import 2: T36 Sheaf Cohomology Audit Findings

Source: `time-as-finality/explorations/T36-sheaf-cohomology-audit.md`

**Relevance:** Directly informs B1 (presheaf absorber test) and the AB convergence theorem
hypothesis from E021. TaF ran a serious audit of whether its own local-to-global obstruction
machinery (`D1RestrictionSystem`, `PO1`) is genuinely sheaf-theoretic / cohomological.

### Key Findings

**What is currently true** (in TaF, but the finding is general):
- Finite local-to-global satisfiability obstructions (every patch satisfiable, global join
  empty) are closest to: finite CSP/SAT, Abramsky-Brandenburger sheaf contextuality, Z2
  parity cohomology on signed graphs, relational database consistency.
- They are NOT automatically Čech cohomology unless a base category, contravariant
  restriction functor, and restriction maps for all inclusions are defined.
- The executable T13 test currently reports `h1_is_nontrivial = False` — no nontrivial
  H1 witness exists yet.

**Implication for TI-C017 (Čech witness classes):**
TI-C017 proposes that non-trivial Čech cohomology classes `H^1(S², F_e)` serve as
witnesses for C-typed extension obstructions. The T36 audit gives a precise caution: calling
the obstruction "Čech cohomology" is premature unless:
- A finite context category is defined for the extension system.
- A presheaf `F: C^op -> Set` of local admissible assignments is defined.
- Restriction maps by projection to subcontexts are explicitly constructed.
- A theorem proves that T26-style `global_section` exists iff the presheaf has a global section.
- A Z2 cohomology theorem is proved for the equality/difference fragment.

**What is currently closest:** A CSP/SAT satisfiability obstruction, or an AB-style
contextuality obstruction (locally satisfiable but globally unsatisfiable), depending on
whether the constraints are parity constraints on an underlying equality/difference graph.

**What this means for B1:** The presheaf absorber test must distinguish between:
- (a) `OnlineSchemaSys` inducing a genuine presheaf/sheaf with a proven global-section theorem
- (b) `OnlineSchemaSys` inducing a finite CSP-style satisfiability obstruction (weaker)
- (c) `OnlineSchemaSys` inducing an AB-style contextuality obstruction (the convergence
  theorem hypothesis from E021)

The T36 audit strongly suggests that route (a) requires substantial additional work (defining
the base category, restriction maps, proving the equivalence theorem). Routes (b) and (c) are
the likelier current-state descriptions, with (c) being the most exciting if it survives.

**Z2 parity cohomology candidate:** The T36 audit identifies the binary constraint case
(same/different) as the closest to genuine cohomology. For TI, this corresponds to the
two-type extension case. Binary Parity Obstruction Theorem (candidate from T36):

> Given a finite graph of types with edge labels in Z2 (0 = same schema, 1 = different
> schema), a global typing assignment exists iff the edge-label 1-cochain is a coboundary.
> Equivalently, every cycle has even total parity.

If a TI schema-extension sequence can be encoded as a Z2-labeled graph, this gives a
concrete cohomological obstruction theorem — one that is genuinely earned rather than
notational.

---

## Import 3: T61 MMO Reconciliation for AC-8 Formal Model

Source: `time-as-finality/explorations/T61-mmo-reconciliation-synthesis.md` and
`time-as-finality/technical-reports/TECHNICAL-REPORT-mmo-reconciliation-finality-v0.1.md`

**Relevance:** T61 provides a complete formal model of exactly the authority/legitimacy
gap identified in E021 (Idea 3). When building the AC-8 formal model (multi-observer
interactive schema negotiation), TI should adopt T61's framework.

### T61 Core Distinction (directly applicable to AC-8)

```text
client-predicted state
  != edge-cached state
  != authority-committed state
  != reconciled observer state
```

For AC-8, this translates as:

```text
observer-local schema extension
  != schema extension proposed to shared process
  != schema extension committed to shared process
  != schema extension received and confirmed by all observers
```

### T61 Operational Answers (adapted for AC-8)

| T61 question | T61 answer | AC-8 translation |
|---|---|---|
| What is locally final? | A predicted action usable in a bounded observer view | Observer-local D4 event: schema extended in that observer's `H_n` record |
| What is event-final? | An authority-committed record inside the synchronization boundary | Schema extension `epsilon_n` committed to shared OnlineSchemaSys state |
| What is only predicted? | A local branch before commit confirmation | Observer-local schema proposal not yet adopted by shared process |
| What gets rolled back? | A predicted branch rejected by authority | Observer-local schema extension rejected by multi-observer negotiation |
| What propagates? | Prediction, commit, rollback, compensation records | Schema proposals, commitments, rejections, and revision offers |
| What handles incompatibility? | Explicit conflict data (T55 style) | AC-8 negotiation outcome: either merge, override, or explicit schema conflict |

### Authority / Legitimacy Layer (from T61 and DS-architect intake)

T61's positive witness shows: "A sound observer record chain can reflect visible source
order, while same TaF readout can lose hidden source order." For AC-8, this means:

The legitimacy condition for a D4 issuance event is NOT just that the issuing observer
can construct the new type locally. It is that the shared process commits the type:
- at least one authoritative record of the type-extension event exists
- the record is accessible (not just local to one observer's `H_n`)
- the record survives reconciliation with other observers' schemas

The failure mode (T61 failure witness) is: two observers propose incompatible schema
extensions. The resolution requires explicit conflict handling, not silent merge. This
is exactly what AC-8 "interactive schema negotiation" must formalize.

---

## What This Changes in the TI Program

1. **N13 same-neighbor-data vector becomes the physics-bridge checklist.** Before TI-C019
   can claim any connection to physical energy, expansion, or structure formation, the
   same-neighbor-data vector must be frozen and each field's absorber status declared.
   This is a precondition for TI-C020 pressure work.

2. **T36 audit refines B1.** B1 should now distinguish between: genuine presheaf/sheaf
   (requires additional structure), CSP/SAT obstruction (current likely state), and
   AB-style contextuality (the convergence theorem hypothesis). The Z2 cohomology
   candidate is the clearest path from current CSP state to earned cohomology.

3. **T61 framework provides the AC-8 formal model template.** When building AC-8,
   use T61's distinction (local / proposed / committed / reconciled) and T61's conflict
   treatment (explicit conflict data, not silent merge) as the architectural template.

4. **No claim status changes.** These are research inputs. Claim updates require a
   steward run with hostile review.
