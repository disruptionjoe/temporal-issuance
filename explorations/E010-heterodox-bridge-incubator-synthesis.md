---
artifact_type: exploration
exploration_id: E010
status: active
governance_role: w009_final_artifact
source_run: RUN-0031
target_bridge: Temporal Issuance -> Lorentzian physics / mass-energy / spacetime structure
constitutional: false
---

# E010: Heterodox Bridge Incubator Synthesis

## Purpose

This is the W009 Final Artifact for RUN-0031. It is designed to be a standalone reference that
a mathematician or physicist can pick up and evaluate without needing the rest of the repo.

**What this document is:**
- The strongest surviving mechanism for connecting Temporal Issuance to physical theory
- A complete list of bridge lemmas (proved, open, and weakened)
- Toy models with explicit falsification conditions
- Resurrection triggers and kill conditions
- The recommended next research step

**What this document is not:**
- A claim promotion (all claims are speculative or below)
- A defense of Temporal Issuance (it accurately records the strength and weakness of each mechanism)
- A replacement for the formal proof program (it is a bridge-incubation artifact, not a theorem)

---

## Background: What Was Closed

**BDO (RUN-0028):** In `LorHist(M, eta, A)` with Poincare-invariant Noether-regular action,
total four-momentum `p^mu` of any on-shell morphism is determined by boundary objects. For any
parallel pair `e1, e2: S => S'`, `p^mu(F(e1)) = p^mu(F(e2))`. Nontriviality and energy-momentum-
relevance are mutually exclusive in the Poincare-invariant Minkowski control case.

**ICO (RUN-0029):** With momentum-underdetermining `LorHist'` objects, `p^mu` is morphism-level
but indexed by target-side dynamical physics (coupling constants, interaction Hamiltonian, scattering
amplitudes). Any selection mechanism falls to ICO-1 (imports target physics), ICO-2 (insufficient),
or ICO-3 (bookkeeping).

**Scope of BDO/ICO:** Both are theorems about fixed `(M, eta)`, Poincare-invariant dynamics, and
classical completions. They do not address:
- Non-Poincare targets (BMS, conformal group, diffeomorphism group)
- Quantum completions (path-integral, superposition)
- Topological targets (TQFT, knot invariants)
- Morphism invariants other than `p^mu` (holonomy, soft charges, topological charges)

---

## Strongest Mechanism

**Name:** BMS Soft Charge Mechanism with Holonomy Backbone

**Core claim:**
```text
There exists a formulation of ExtCat as a BMS-equivariant category, and a functor
F: ExtCat -> LorHist_BMS, such that:

(a) BMS supertranslation memory Q_f is a morphism-level invariant of F (not object-level)
(b) Q_f is not determined by Poincare four-momentum data
(c) Q_f is a Noether charge for the BMS action on ExtCat morphisms (source-defined)

If (a), (b), (c) hold, then BL-007 is proved, and the BMS escape route evades both
BDO (Q_f is morphism-level, not object-level) and ICO (Q_f is source-side Noether charge,
not target-side completion selector).
```

**Status of the mechanism:**
- (a): Supported by BMS literature (BMS memory is morphism-level in LorHist_BMS). Status: SURVIVES.
- (b): Established physics (Christodoulou-Kibble memory, Strominger infrared triangle). Status: SURVIVES.
- (c): CRITICAL OPEN QUESTION. Requires: definition of BMS action on ExtCat morphisms. No known
  theorem proves or disproves this. Status: UNKNOWN.

**The mechanism is alive.** It has not been killed. It requires a definition attempt (BL-001)
and a proof (BL-007) before it can be promoted.

**Secondary mechanism:** Holonomy invariants (M1). Even if the BMS mechanism fails, the holonomy
of the `Ext_S` connection is a standalone formal invariant that evades both BDO and ICO. It is
weaker (no direct physical interpretation yet) but formally sound.

---

## Bridge Lemmas

### BL-001: BMS-Covariant Extension Category
**Statement:** `ExtCat` can be formulated so that morphisms transform covariantly under BMS supertranslations.
**Status:** UNKNOWN. Requires definition attempt.
**Dependencies:** None.
**Next action:** Attempt to define BMS action on admissible extensions.

---

### BL-002: Soft Charge Is Morphism-Level in ExtCat
**Statement:** There exists Q_f: Mor(ExtCat) -> R with Q_f(e1) != Q_f(e2) for some parallel e1, e2.
**Status:** UNKNOWN. Supported by physical intuition from LorHist_BMS; source-side status unclear.
**Dependencies:** BL-001.
**Next action:** Attempt to define Q_f as a function of source-side extension data.

---

### BL-003: Soft Charges Are Not Determined by Poincare Boundary Data
**Statement:** Q_f is not a function of p^mu alone. Two morphisms with the same p^mu can have
different Q_f (gravitational / electromagnetic memory effect).
**Status:** SURVIVES. Established by Christodoulou-Kibble, Bieri-Garfinkle, Strominger et al.
**Evidence:** Gravitational memory effect; BMS infrared triangle.
**Dependencies:** None.

---

### BL-004: Holonomy of Ext_S Connection Is Nontrivial
**Statement:** For some constraint system, the holonomy group of the `Ext_S` connection is nontrivial.
**Status:** WEAK. Requires reversible extensions (non-DAG ExtCat) and non-flat connection curvature.
**Dependencies:** BL-005.
**Next action:** Construct a concrete constraint system with reversible extensions; compute curvature.

---

### BL-005: ExtCat Fundamental Group Is Nontrivial
**Statement:** For some constraint system, pi_1(BExtCat) is nontrivial.
**Status:** WEAK. Requires constraint systems with endomorphisms or cycles.
**Dependencies:** None.
**Next action:** Define an extension system with admissible self-extensions or reversible paths.

---

### BL-006: TQFT Functor from ExtCat Exists
**Statement:** There exists Z: ExtCat -> Hilb with nontrivial partition functions for extensions.
**Status:** SURVIVES (existence). WEAK (interesting properties require monoidal structure).
**Dependencies:** Monoidal structure on ExtCat (tensor product of constraint states).
**Next action:** Define tensor product of constraint states; compute Z for minimal example.

---

### BL-007: Soft Charge Is Source-Side Ext_S Invariant (Critical Bridge Lemma)
**Statement:** Q_f can be defined as a source-category invariant of ExtCat morphisms, rather than
as a target-side dynamical quantity.
**Status:** UNKNOWN. The critical bridge lemma. Fate of BMS mechanism depends on this.
**Open obstacle:** ICO' — modified ICO applied to Q_f. Trichotomy:
  - ICO'-1: Q_f is defined using target-side radiation dynamics (absorbed)
  - ICO'-2: source-side invariant but doesn't determine Q_f (insufficient)
  - ICO'-3: trivially re-encodes the radiation field (bookkeeping)
Escape from ICO': Q_f is a Noether charge of BMS action on ExtCat (requires BL-001).
**Dependencies:** BL-001, BL-002, BL-003.
**Next action:** W008 Category G — attempt to define BMS action on ExtCat.

---

### BL-008: Conformal Target Evades BDO
**Statement:** In a conformally invariant target, BDO's argument (p^mu is object-level) does not apply.
**Status:** WEAK. Conformal dimension may be object-level via operator-state correspondence.
**Dependencies:** None.
**Next action:** Prove or refute that conformal dimension is morphism-level in LorHist_CFT.

---

### BL-009: Quantum Path-Integral Over ExtCat Gives Non-Classical Invariant
**Statement:** A path-integral Z[ExtCat] over morphisms produces observables not in any classical theory.
**Status:** UNKNOWN. Depends on whether ExtCat is isomorphic to field-configuration space.
**Dependencies:** Action and measure on Mor(ExtCat).
**Next action:** Construct a candidate action on ExtCat morphisms; check whether the resulting QFT
is equivalent to a known quantum field theory.

---

## Existing Analogues

| Domain | Analogy | Relevance |
| --- | --- | --- |
| Gauge theory | Holonomy of gauge connection | M1 directly generalizes; holonomy is morphism-level invariant of gauge groupoid |
| BMS asymptotic symmetry | Supertranslation memory effect | BL-003 is the physical basis of M2; infrared triangle provides formal foundation |
| Hashgraph consensus | Signed event DAG | Concrete implemented example of morphism-level invariants (Persona 55, RUN-0030) |
| Conservative/optimistic sync | Rollback structure in distributed simulation | BL-002 analogue; different sync rules (same order) produce different morphism invariants |
| TQFT / Chern-Simons theory | Partition function of morphisms | M3 formalizes ExtCat as cobordism-like category with TQFT observables |
| Hannay-Berry phase | Geometric phase in adiabatic dynamics | M1 classical analogue; computable and observable |
| Git merge DAG | Commit hash as morphism invariant | Concrete example of parallel morphisms with different invariants in version control |

---

## Toy Models

### TM-A: Minimal Holonomy Model

```text
ExtCat: two objects S0, S1; two parallel morphisms e01a (type alpha), e01b (type beta).
Binary invariant: I(e01a) = 0, I(e01b) = 1.
Physical target: TQFT functor Z(e01a) = identity matrix, Z(e01b) = swap matrix.
Predicted difference: Z(e01a) != Z(e01b) as operators (even though Tr are equal in 2x2 case).
Falsification condition: I(e01a) = I(e01b) forced by admissibility rule => no morphism-level
  invariant exists for this extension rule.
```

### TM-B: Minimal BMS Memory Model

```text
ExtCat: two objects B_in (in-state), B_out (out-state charge data).
Two parallel morphisms h1 (no soft emission), h2 (with soft emission).
p^mu(h1) = p^mu(h2) by conservation (same objects).
Q_f(h1) = 0, Q_f(h2) > 0 (different BMS soft charge).
Predicted difference: Q_f distinguishes h1 from h2 morphism-level.
Falsification condition: ICO' proves Q_f is always target-defined => BMS mechanism closed.
```

### TM-C: TQFT-ExtCat Toy Model

```text
ExtCat: symmetric monoidal category with two objects (S0, S1) and two parallel morphisms (e, e').
Z(e) = identity 2x2, Z(e') = swap 2x2.
Morphism-level invariant: Tr(Z(e)*Z(e')^T) = 0 (orthogonality in operator space).
Physical interpretation: two extension routes produce orthogonal quantum channels.
Falsification condition: all functors Z: ExtCat -> Hilb have Z(e) = Z(e') for all parallel
  morphisms => TQFT functor cannot distinguish parallel extensions.
```

---

## Resurrection Triggers

The following discoveries would revive the bridge:

1. **BMS action on ExtCat is defined and consistent.** If BL-001 can be proved, the entire BMS
   mechanism chain (BL-001 -> BL-002 -> BL-007) opens for systematic investigation.

2. **A physical theory exists where scattering completion data is parametrized by source-category
   extension rules rather than a Hamiltonian.** This would be the new theory hypothesized in ICO's
   path-kill record as the resurrection trigger.

3. **Holonomy of Ext_S connection is computed to be nontrivial for a specific constraint system.**
   This would give a standalone formal result (M1 mechanism) that is the starting point for physical
   interpretation search.

4. **Quantum information evidence for soft charge non-classicality.** If soft charges are shown to
   carry quantum information beyond the classical S-matrix, their source-side status becomes more
   plausible.

5. **Non-flat curvature of Ext_S connection for a natural constraint system.** This would support
   BL-004 and revive M1 with a specific physical example.

---

## Kill Conditions

The following future results would permanently retire the bridge:

1. **BMS action on ExtCat is proved impossible.** If BL-001 can be proved false (no consistent
   BMS action on admissible extensions exists), the BMS soft-charge mechanism is definitively closed.

2. **Holonomy of Ext_S connection is provably trivial for all physically motivated constraint systems.**
   If M1 cannot produce nontrivial holonomy in any physically relevant case, the holonomy mechanism
   is closed.

3. **ICO' is proved: Q_f is always target-defined.** If a theorem shows that for any source-side
   invariant I(e) that determines Q_f, I(e) must encode target-side radiation field data (ICO'-1),
   or I(e) is insufficient to determine Q_f (ICO'-2), the BMS mechanism is definitively closed.

4. **ExtCat is proved isomorphic to field-configuration space.** If `ExtCat` is not a new
   mathematical object (it is isomorphic to the ordinary space of field boundary conditions), then
   Temporal Issuance is entirely absorbed by standard QFT, and all bridge mechanisms reduce to
   standard physics.

5. **TQFT functor invariants are proved to be equal for all parallel extensions.** If the only
   TQFT invariants distinguishing morphisms are the induced order, M3 is closed.

---

## Recommended Next Step

**Primary:** W000 -> W008 Category G — Attempt to define a BMS group action on `ExtCat`.

This is the highest expected-value move because:
- BL-003 is already established (Q_f != p^mu is settled physics)
- BL-007 is the only remaining open question for the BMS mechanism
- A definition attempt is a concrete, bounded task
- The resolution (BL-001 provable or not) directly determines whether Category G survives or is closed

**Secondary:** Formalize TM-A and compute the curvature of the `Ext_S` connection for the minimal
holonomy model. If curvature is nonzero, this is a standalone mathematical result supporting M1.

**Tertiary:** Publish the formal residue (BDO lemma, ICO theorem, preorder-from-extension, E008
conditional theorem) as a standalone mathematics paper. This is independent of all bridge questions
and is a publishable result as it stands.

---

## Formal Residue (What Survives Independently)

The following formal results are correct regardless of the fate of the bridge:

1. **Preorder-from-extension (RUN-0025):** Extension categories carry morphism-level invariants
   not recoverable from the induced preorder. Theorem.

2. **BDO lemma (RUN-0028):** In `LorHist(M, eta, A)` with Poincare-invariant Noether-regular
   action, `p^mu` is boundary-object-determined. Proven lemma.

3. **ICO theorem (RUN-0029):** With momentum-underdetermining objects, any selection mechanism
   for `p^mu` among completions falls to ICO-1, ICO-2, or ICO-3. Proven theorem.

4. **E008 conditional theorem (RUN-0026):** IF a nontrivial-at-mass-energy functor F: ExtCat ->
   LorHist(M, eta, A) exists, THEN standard relativistic energy-momentum follows. The antecedent
   is obstructed by BDO + ICO in the Poincare-invariant Lorentzian control case. Formally valid;
   vacuously satisfied in the control case.

5. **History-class nontriviality (BDO, RUN-0028):** A functor F: ExtCat -> LorHist can be
   nontrivial at the admissible-history-class level (parallel extensions map to distinct on-shell
   sectors). Proven (absorbed by gauge/topological bookkeeping, but coherent formal structure).
