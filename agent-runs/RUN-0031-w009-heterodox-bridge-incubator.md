---
artifact_type: run_record
run_id: RUN-0031
status: complete
governance_role: w009_heterodox_bridge_incubator_pass
trigger: RUN-0030 synthesis; W009 created and immediately run against Phase 1 output
workflow: W009-heterodox-bridge-incubator
constitutional: false
claims_touched:
  - TI-C007
  - TI-C008
  - TI-C012 (new, speculative)
  - TI-C013 (new, speculative)
target_bridge: Temporal Issuance -> Lorentzian physics / mass-energy / spacetime structure
---

# RUN-0031: W009 Heterodox Bridge Incubator — Temporal Issuance to Physics

## Timestamp

2026-06-22

## Trigger

RUN-0030 W007 pass completed. Phase 2 (Heterodox Panel Synthesis) identified 5 constructive routes
not yet tried. W009 is applied immediately to the strongest routes from RUN-0030.

## Input from RUN-0030

The 62-persona panel synthesis identified the following W009 incubation targets:
1. Fiber bundle holonomy invariant of `Ext_S`
2. BMS soft charges as `Ext_S` morphism invariants
3. Resource theory with novel monotone
4. Conformal / TQFT target instead of Lorentzian
5. Quantum path-integral over `Ext_S` completions

The core rule for this W009 pass: assume there exists a coherent mechanism connecting Temporal
Issuance to Lorentzian physics or spacetime structure. Build the strongest possible version of that
mechanism before any adversarial testing.

---

## Phase 1: Strongest Intuition Extraction

### Input: Heterodox Panel Synthesis from RUN-0030

The core intuition, stripped of all specific physics machinery:

**The base intuition (strongest version):** There is a mathematical structure — the admissible
extension category `ExtCat` — that carries morphism-level invariants beyond the induced preorder.
This structure is not invented: the morphism-level invariants are already proven to exist (RUN-0025).
The question is whether any physical theory has the property that its admissible boundary-value or
completion structure is exactly this extension category, making `Ext_S` invariants the reason
certain physical quantities take particular values.

**Why it feels like it might point at something real:** The strongest analogy is gauge theory.
In gauge theory, the gauge group acts on the fiber of a bundle; different gauge transformations
are parallel morphisms in the gauge groupoid; physical observables are gauge-invariant functions
on the groupoid (not on the base space). The morphism-level invariants of the gauge groupoid (holonomy,
Chern classes, winding number) are the physical observables. Temporal Issuance proposes that
`Ext_S` plays the role of the gauge groupoid for a different physical structure — one where
the "gauge transformations" are admissible extensions.

**The most minimal formal object capturing the intuition:**

```text
ExtCat: a category with
  objects:  typed source constraints C
  morphisms: admissible extensions e: S -> S'
  key property: Hom(S, S') can have |Hom| > 1 for some S, S'
                (parallel extensions, not just a preorder)

The physical claim: there exists a physical theory T such that
  - the space of solutions to T's boundary-value problems is ExtCat
  - the observables of T are gauge-invariant functions on ExtCat
  - the morphism-level invariants of ExtCat are the non-trivial observables of T
```

**Cross-domain examples of the same structure:**
- Gauge theory: parallel gauge transformations (morphisms) produce observable holonomies
- Hashgraph: parallel gossip paths (morphisms) produce signed event histories (invariants)
- Git: parallel merge histories (morphisms) produce distinct commit hashes (invariants)
- Database transactions: parallel execution histories (morphisms) produce distinct anomaly profiles

All four examples have the same structure: parallel morphisms in a category produce observable
invariants not captured by the induced order.

**The strongest version of the intuition:**

```text
Temporal Issuance is the hypothesis that the fundamental arena of physics is ExtCat —
a category of constraint extensions — and that physical observables are invariants
of morphisms in this category. The standard physical quantities (energy-momentum, charge,
spin) are the morphism-level invariants of ExtCat under appropriate functors.

BDO and ICO show that in the Poincare-invariant Lorentzian control case, energy-momentum
is NOT a morphism-level invariant of ExtCat (it is object-level). This means either:
(a) Temporal Issuance is wrong about energy-momentum, or
(b) The Poincare-invariant Lorentzian control case is not the right physical setting.

The W008 escape-route taxonomy lists 7 possible alternative settings.
W009's job: build the strongest mechanism for option (b).
```

---

## Phase 2: Mechanism Construction

### Candidate Mechanism M1: Gauge Holonomy Mechanism

**Formal objects:**
```text
E: a fiber bundle over constraint space, with
   base space B: the space of constraint types (typed C)
   fiber F_C: the set of admissible extensions from constraint C
   structure group G: the group of automorphisms of F_C
   connection omega: a connection on E (the Ext_S rule as a connection)

The Ext_S morphism e: S -> S' corresponds to parallel transport in E
along a path in B from C(S) to C(S').

Physical observable: the holonomy of omega around a loop of admissible extensions
Hol(gamma) in G for a closed loop gamma in ExtCat.
```

**What this predicts differently from absorbers:**
Holonomy is a morphism-level invariant not captured by the induced preorder. Unlike energy-momentum
(which BDO shows is object-level), holonomy is inherently a loop invariant. BDO's argument does not
apply to holonomy: BDO said "p^mu is determined by boundary objects." Holonomy is not determined by
boundary objects — it requires information about the closed loop, which is precisely the morphism-level
data.

**The new invariant:**
```text
Hol: pi_1(BExtCat) -> G
```
The holonomy representation of the fundamental group of the classifying space of `ExtCat`.
This is nontrivial whenever `ExtCat` has nontrivial loop structure (i.e., parallel extensions
that compose to something nontrivial).

**Why BDO/ICO do not apply:**
BDO: proved that energy-momentum is object-level. Holonomy is not energy-momentum.
ICO: proved that source-side invariants cannot select completions indexed by target-side Hamiltonian.
Holonomy is not a completion selector — it is a loop invariant defined purely in ExtCat.

---

### Candidate Mechanism M2: BMS Soft Charge Mechanism

**Formal objects:**
```text
LorHist_BMS: a Lorentzian history category where objects are
   defined as data at conformal infinity I^+ and I^-,
   but include the FULL BMS group action, not just the
   Poincare subgroup.

Soft charges Q_f(e) for supertranslation parameter f:
   - a BMS supertranslation f acts on I^+ as u -> u + f(theta, phi)
   - the soft charge Q_f is the corresponding Noether charge
   - crucially: Q_f is NOT determined by the Poincare subgroup of BMS
     (it is sensitive to supertranslation data that Poincare ignores)
   - Q_f is morphism-level: it measures the supertranslation memory effect
     of a scattering process (gravitational wave memory, electromagnetic memory)

Ext_S invariant identification:
   The supertranslation memory effect of an admissible extension e: S -> S'
   is Q_f(e) = the difference in soft charge between the in-state and out-state.
   Different parallel extensions e1, e2: S => S' with the same Poincare energy-
   momentum p^mu can have different supertranslation memory Q_f.
```

**What this predicts differently from absorbers:**
BDO proved that `p^mu` is object-level in `LorHist(M, eta, A)` with Poincare-invariant action.
The BMS case EVADES BDO: the BMS group is NOT the Poincare group. Supertranslation charges Q_f
are NOT determined by Poincare boundary data. They are sensitive to soft photon/graviton content
that Poincare-invariant actions cannot capture.

**The escape route from BDO:**
BDO's key step: "A is Poincare-invariant and Noether-regular, so p^mu is conserved and determined
by boundary data." This step FAILS if A is BMS-invariant (not Poincare-invariant). BMS includes
supertranslations that are NOT symmetries of the Poincare-invariant action. Hence BMS Noether charges
include contributions beyond p^mu.

**The escape route from ICO:**
ICO's key step: "morphism-level variation of p^mu is parametrized by target-side dynamical physics
(coupling constants, Hamiltonian)." For soft charges Q_f, the variation IS determined by the
asymptotic field configuration at I^+ — which is covariant data, not choice of Hamiltonian.
The infrared triangle (Weinberg soft theorem / BMS supertranslation / gravitational memory) shows
that soft charge differences are universal, not Hamiltonian-specific.

**The new invariant:**
```text
Q_f: Mor(ExtCat) -> R (real numbers, or R^{S^2} for angle-dependent f)
The supertranslation memory carried by each admissible extension.
```

---

### Candidate Mechanism M3: Topological Field Theory Mechanism

**Formal objects:**
```text
TQFT target: instead of LorHist(M, eta, A), use the target
   Z: ExtCat -> Hilb  (a TQFT-type functor from ExtCat to Hilbert spaces)

In TQFT, the physical content is in the cobordism category:
   objects: (d-1)-manifolds (boundaries)
   morphisms: d-manifolds (cobordisms from one boundary to another)

If ExtCat can be identified with (a subcategory of) the cobordism category,
then the TQFT functor Z assigns:
   - to each constraint state S: a Hilbert space Z(S)
   - to each admissible extension e: S -> S': a linear map Z(e): Z(S) -> Z(S')

The morphism-level invariant is the trace of Z(e) (the partition function of the cobordism).
Different parallel extensions e1, e2: S => S' can have Tr(Z(e1)) != Tr(Z(e2)).
```

**What this predicts differently from absorbers:**
TQFTs have no local degrees of freedom (no energy-momentum in the bulk). They are purely topological.
BDO and ICO both apply to theories with local degrees of freedom (Lorentzian field theory with
conserved p^mu). A TQFT target bypasses BDO/ICO entirely: there is no p^mu to be determined by
boundary objects (TQFT has no Poincare charges in the bulk; observables are knot invariants, etc.).

**The new invariant:**
```text
Z(e): morphism-level linear map in the TQFT functor
Tr(Z(e)): partition function of the extension (topological invariant)
```

This invariant is genuinely morphism-level and not captured by the induced order.

---

## Phase 3: Bridge Lemma Discovery

For the strongest mechanism (M2, BMS Soft Charge Mechanism, supplemented by M1 as the formal
backbone), identify all missing intermediate steps.

### Bridge Lemma BL-001: BMS-Covariant Extension Category

**Statement:** `ExtCat` can be formulated so that its morphisms transform covariantly under the
BMS group (not just the Poincare group), with BMS supertranslations acting on morphisms in
a well-defined way.

**Why needed:** For M2 to work, the source-side extension category must have the right symmetry
group. If `ExtCat` only has Poincare symmetry, the soft charges are not source-side quantities.

**Current status:** Unproved. The current formulation of `ExtCat` does not specify which symmetry
group acts on morphisms.

**Possible formalization:** Define morphisms in `ExtCat` as sections of a BMS-equivariant bundle.
The BMS group acts on the bundle fibers; admissible extensions are equivariant sections.

**Dependencies:** Requires: (a) a definition of the BMS group action on source constraints; (b) a
proof that this action is compatible with the extension admissibility rule.

---

### Bridge Lemma BL-002: Soft Charge Is Morphism-Level in ExtCat

**Statement:** The BMS supertranslation memory Q_f can be defined as a morphism invariant of
`ExtCat` — i.e., there exists a function Q_f: Mor(ExtCat) -> R such that Q_f is not determined
by the induced preorder (i.e., parallel morphisms e1, e2: S => S' can have Q_f(e1) != Q_f(e2)).

**Why needed:** This is the core claim of M2. Without it, soft charges are not source-side invariants.

**Current status:** Partially supported by physical intuition. The infrared triangle shows that
supertranslation memory is morphism-level in LorHist: two scattering histories with the same in-
and out-state particle content can differ in the soft photon/graviton content (memory effect).
Whether this translates to ExtCat morphisms is unproved.

**Possible formalization:** Use the Campiglia-Laddha / Strominger reformulation of supertranslation
charges as insertion operators on the in-state. If the in-state is an object of `ExtCat`, then the
supertranslation charge acts on the morphism space Hom(S, S') by shifting the soft content.

**Dependencies:** Requires BL-001 (BMS action on ExtCat); requires the infrared-triangle identification
of supertranslation charge with memory effect.

---

### Bridge Lemma BL-003: Soft Charges Are Not Determined by Poincare Boundary Data

**Statement:** In a Lorentzian scattering setting, the BMS supertranslation charge Q_f of a morphism
is NOT determined by the Poincare four-momentum data of the boundary objects. There exist parallel
morphisms h1, h2: B -> B' in LorHist_BMS with the same p^mu(h1) = p^mu(h2) but Q_f(h1) != Q_f(h2).

**Why needed:** This is what makes soft charges "morphism-level beyond BDO." BDO proved p^mu is
object-level. BL-003 asserts Q_f is strictly more than p^mu data.

**Current status:** Well-supported by known physics. The gravitational memory effect: two spacetimes
with the same total ADM energy can differ in gravitational wave memory (a BMS supertranslation charge).
This is established physics (Bieri-Garfinkle memory effect, Christodoulou memory).

**Possible formalization:** Use the Compere-Nichols / Strominger papers on BMS charges. The key
equation: Delta Q_f = integral over I^+ of f * T_uu dOmega, where T_uu is the radiation flux. This
integral depends on the angular distribution of outgoing radiation, NOT on total p^mu.

**Dependencies:** Standard general relativity and BMS literature. Status: supported by known results.

---

### Bridge Lemma BL-004: Holonomy of Ext_S Connection is Nontrivial

**Statement:** If `Ext_S` is formulated as a connection omega on a fiber bundle E over constraint space,
the holonomy group Hol(omega) is nontrivial — i.e., there exists a closed loop gamma in `ExtCat` such
that parallel transport around gamma does not return to the identity.

**Why needed:** This is the core of M1. Without nontrivial holonomy, the fiber bundle formulation
collapses to the trivial (flat) case, and M1 produces nothing new.

**Current status:** Unproved. Nontrivial holonomy requires: (a) a definition of E and omega;
(b) a proof that some loop in ExtCat produces nontrivial parallel transport. For the minimal
ExtCat (two objects, two parallel morphisms), holonomy trivializes because there is only one
loop structure. A larger ExtCat (with nontrivial fundamental group) is required.

**Possible formalization:** Define E as the Borel construction ExtCat x_G * for some group G
acting on the space of admissible extensions. A loop in ExtCat corresponds to a cycle in the
nerve of the category; parallel transport around the loop is the holonomy.

**Dependencies:** Requires: (a) a group action G on admissible extensions; (b) ExtCat with
nontrivial fundamental group (at least one non-contractible loop).

---

### Bridge Lemma BL-005: ExtCat Fundamental Group Is Nontrivial for Non-Trivial Constraint Systems

**Statement:** For a constraint system with at least two constraint types and a non-trivial
admissibility rule, the classifying space BExtCat has nontrivial fundamental group pi_1(BExtCat).

**Why needed:** BL-004 requires nontrivial fundamental group for nontrivial holonomy.

**Current status:** Plausible but unproved. For any category C, BExtCat has pi_1 corresponding
to automorphisms of objects. If some object S in ExtCat has a nontrivial automorphism (a loop
e: S -> S with e != id_S), then pi_1(BExtCat) is nontrivial.

**Possible formalization:** In any category with morphisms e: S -> S (endomorphisms, not identities),
there exist nontrivial loops in the classifying space. For `ExtCat` with typed constraints, an
endomorphism e: S -> S would be an admissible self-extension of a constraint state.

**Dependencies:** Requires constraint systems where self-extensions are admissible.

---

### Bridge Lemma BL-006: TQFT Functor from ExtCat Exists for Appropriate Constraint Systems

**Statement:** There exists a symmetric monoidal functor Z: ExtCat -> Hilb (or a variant) for
at least one non-trivial constraint system, where Z assigns Hilbert spaces to constraint states
and linear maps to admissible extensions.

**Why needed:** M3 requires this functor. Without it, the TQFT mechanism is a formal placeholder.

**Current status:** Plausible but unproved. Any functor from a category to Hilb (a TQFT-type
functor) can be constructed given: (a) an assignment of Hilbert spaces to objects; (b) a
consistent assignment of linear maps to morphisms (functor axioms). For finite ExtCat, this
is always possible (every finite category has a representation in Hilb). The question is whether
the functor has interesting properties (nontrivial trace, topological invariance).

**Possible formalization:** For the minimal ExtCat (two objects S, S', two morphisms e1, e2),
define Z(S), Z(S') as C^n for some n, and Z(e1), Z(e2) as distinct n x n matrices. The trace
Tr(Z(e1)) != Tr(Z(e2)) would give a computable morphism-level invariant.

**Dependencies:** Requires ExtCat to be monoidal (tensor product of constraint states).

---

### Bridge Lemma BL-007: Soft Charge Can Be Identified as Ext_S Morphism Invariant (Bridging Lemma)

**Statement:** There exists an `Ext_S` rule such that the source-side morphism invariant I(e) is
functorially identified with the BMS soft charge Q_f of the realized scattering history F(e) in
LorHist_BMS.

**Why needed:** This is the bridge lemma connecting M2 (BMS soft charge) to the source category.
Without this, Q_f is a target-side invariant, not a source-side one.

**Current status:** The strongest positive evidence: the infrared triangle shows that supertranslation
memory is equivalent to a soft photon/graviton theorem, which is in turn related to the Ward identity
of a large gauge symmetry. If the large gauge symmetry can be identified as a symmetry of `ExtCat`
(a symmetry acting on admissible extensions), then Q_f is both a target-side charge and a source-side
invariant under the same symmetry.

**Strongest obstacle:** ICO's argument still applies here in a modified form: the supertranslation
charge Q_f depends on the angular distribution of outgoing radiation, which is physics of the
Lorentzian target (scattering angles, coupling strengths). Even if Q_f is morphism-level (beyond p^mu),
its value is still determined by target-side dynamics.

**ICO-modified version (ICO'):** With BMS objects (objects encoding only supertranslation-frame data,
not full angular radiation data), Q_f is morphism-level. But Q_f variation is still parametrized by
angular radiation dynamics, not ExtCat structure. This is ICO applied to Q_f rather than p^mu.

**Current status:** This is the critical bridge lemma. Its fate determines whether the BMS escape
route evades ICO or merely shifts the ICO problem to a higher-order observable.

**Dependencies:** BL-001, BL-002, BL-003; resolution of the ICO' question.

---

### Bridge Lemma BL-008: Conformal Target Evades BDO for Massless Theories

**Statement:** In a conformally invariant target (no Poincare mass, conformal group symmetry),
BDO's key step ("conserved p^mu is boundary-object-determined") does not apply, because massless
theories do not have a rest-frame concept and conformal invariants are not energy-momentum.

**Why needed:** This opens the Category A/B escape route from BDO for the class of conformally
invariant theories (CFT, massless QED, etc.).

**Current status:** Well-supported. In a CFT, the physical observables are conformal weights and
OPE coefficients, not energy-momentum. BDO's argument is specific to Noether charges for Poincare
symmetry. Conformal charges (the dilatation charge, special conformal charges) are morphism-level
in CFT in a way that energy-momentum is not.

**Possible formalization:** Define LorHist_CFT as a category of conformal histories. Prove that
conformal dimension (the CFT analog of mass) is morphism-level and not object-level in LorHist_CFT.
If true, BDO fails for conformal targets.

**Dependencies:** Standard CFT; proof that conformal dimension is morphism-level in LorHist_CFT.

---

### Bridge Lemma BL-009: Quantum Path-Integral Over ExtCat Morphisms Gives Non-Classical Invariant

**Statement:** The path-integral Z[ExtCat] = sum over morphisms of exp(i S[e]) produces a morphism-
level invariant that is not captured by any single classical morphism, because quantum superposition
over completions generates interference between parallel extensions.

**Why needed:** This is the Category B escape route (quantum path-integral). ICO applies to
classical completion selection; quantum superposition might evade ICO by distributing over all
completions simultaneously.

**Current status:** Plausible but formalization-dependent. The quantum path-integral over `ExtCat`
morphisms would need: (a) an action S[e] defined on morphisms; (b) a measure over Mor(ExtCat);
(c) a consistency check that the resulting partition function is not equivalent to a classical theory
absorber.

**Possible formalization:** Define the generating functional Z[J] = integral over Mor(ExtCat) of
exp(i S[e] + J*e) dmu(e), where dmu is the measure on morphisms. Compute the connected correlation
functions. If the resulting theory has observables not present in any classical Lorentzian theory,
Temporal Issuance has quantum content.

**Dependencies:** Requires: a well-defined action and measure on ExtCat morphisms; a prescription
for the path-integral that is not equivalent to ordinary quantum field theory.

---

## Phase 4: Specialist Divergence

### Team A — Physics

**What Team A finds:**

BMS Mechanism (M2, BL-003, BL-007):
The physical support for BL-003 is strong: the Christodoulou-Kibble electromagnetic memory effect
(Bieri-Garfinkle) and the gravitational memory effect both demonstrate that two distinct scattering
histories with the same total energy can differ in soft charge content. The infrared triangle
(Strominger) unifies soft theorem, memory effect, and asymptotic symmetry charge as three faces
of the same phenomenon. This is established physics, not speculation.

The critical gap is BL-007: does the soft charge become a source-side invariant, or is it always
determined by target-side dynamics (outgoing radiation field)? The Team A finding: **there is no
known physics result that makes soft charges source-side invariants.** The soft charge depends on
the angular distribution of radiation, which is a dynamical quantity of the Lorentzian target theory.
This is ICO' — a modified form of ICO applied to soft charges.

Conformal Mechanism (M3, BL-008):
BL-008 is physically well-motivated. In N=4 super-Yang-Mills or other CFTs, the conformal
dimensions are the physical observables, and there is no rest-frame energy-momentum concept.
However, CFT observables are also not "source-side" in the sense required by Temporal Issuance:
they are defined by the target theory, not by an independent source category.

Quantum Path-Integral (BL-009):
The quantum path-integral approach is the most open-ended. QFT already sums over classical
solutions weighted by exp(iS). The question is whether summing over ExtCat morphisms instead
of field configurations produces different observables. Team A assessment: this depends on
whether ExtCat is a genuinely new structure or isomorphic to the space of field configurations.
If `ExtCat` is the space of boundary conditions (distinct from the space of solutions), the
path-integral over ExtCat morphisms is different from the ordinary QFT path-integral.

**Team A summary verdict:** BL-003 is established. BL-007 is open and faces ICO' as an obstacle.
BL-008 is supported but the source-side connection is unclear. BL-009 is open.

---

### Team B — Mathematics

**What Team B finds:**

Holonomy Mechanism (M1, BL-004, BL-005):
The fiber bundle / holonomy approach (M1) is mathematically well-defined. For any connection on
a principal bundle, holonomy is a nontrivial invariant whenever the bundle is non-flat. The
construction is:
1. Define G = Aut(C) (automorphisms of the space of constraint types).
2. Define E = ExtCat x_G * (the associated bundle via the G-action on ExtCat morphisms).
3. Define omega as the natural connection induced by the admissibility rule.
4. Compute Hol(omega) for loops in ExtCat.

BL-005 follows from the structure of categories: any category with endomorphisms has nontrivial
loops in its classifying space. The condition for nontrivial holonomy is that the bundle is
non-flat, which requires the curvature of omega to be nonzero. The curvature of omega measures
the "failure of commutativity" of sequential extensions — whether extending via e1 then e3 gives
the same result as extending via e2 then e3 (for parallel e1, e2 and then a common e3).

Team B assessment: BL-004 requires a specific condition (non-flat curvature). The flatness/non-
flatness of the `Ext_S` connection is a computable property of the extension category. For the
minimal example (two objects, two parallel morphisms), the connection is trivially flat (no loops
long enough). For larger categories with cycles, non-flatness is generically expected.

Sheaf Cohomology (Persona 4 from RUN-0030):
H^1 of the extension sheaf measures obstructions to global section existence. This is independent
of all physical bridge questions. Team B finds: the sheaf cohomology of `Ext_S` is a standalone
mathematical invariant. If it is nontrivial for specific constraint systems, this is a publishable
result independent of any physics claim.

TQFT Functor (BL-006):
For finite `ExtCat`, the TQFT functor Z: ExtCat -> Hilb always exists (by direct construction).
The question is whether Z has interesting properties. Team B notes: for the functor to be
interesting (in the TQFT sense), ExtCat should be symmetric monoidal. This requires a tensor
product of constraint states, which is not currently defined.

**Team B summary verdict:** M1/holonomy is the most mathematically grounded. The sheaf cohomology
invariant is the most publishable standalone result. M3/TQFT requires monoidal structure that is
not yet defined.

---

### Team C — Complex Systems

**What Team C finds:**

The complex-systems perspective is most relevant to the dynamical and multiscale analogues from
RUN-0030 (Personas 16-21). Team C notes:

For M1 (holonomy): holonomy in a dynamical system corresponds to the Hannay-Berry phase — the
classical analog of the geometric phase. If `ExtCat` is a dynamical system where extensions are
quasi-static parameter changes, the holonomy of the `Ext_S` connection is the classical Hannay
phase. This is a well-defined, measurable quantity in classical mechanics.

For M2 (BMS soft charges): Team C draws an analogy with chimney plumes and atmospheric memory.
Large-scale atmospheric systems (jet streams, blocking patterns) can persist in two distinct
states with the same local temperature and pressure fields but different "soft" content
(topological defects, Rossby wave packet structures). These are complex-systems analogs of
soft charges — morphism-level invariants of atmospheric dynamics not captured by thermodynamic
boundary data.

For simulation analogues (Personas 57-62 from RUN-0030): the most concrete complex-systems
example is conservative vs. optimistic synchronization (Persona 59). The rollback structure is
a morphism-level invariant of the synchronization rule. This has been verified empirically in
distributed simulation benchmarks: two simulations with the same logical process graph but
different synchronization rules produce different rollback depth distributions.

**Team C summary verdict:** The Hannay phase analogy (M1 in dynamical systems language) is the
most empirically tractable. The synchronization analogy (M2 in distributed systems language) is
the most concretely verified.

---

### Team D — Information Theory

**What Team D finds:**

The information-theoretic perspective is most directly relevant to M2 (soft charges) and M3 (TQFT).

For M2: The soft charge Q_f measures the amount of "soft" information in a scattering process —
information that is not captured by the Poincare-invariant S-matrix. In the information-theoretic
language: the S-matrix maps in-state quantum numbers to out-state quantum numbers (Poincare-invariant);
the "soft information" (supertranslation memory) is the excess information beyond the S-matrix.
This is precisely the non-faithfulness gap identified by Persona 19 (Causal Inference Expert).

Information-theoretic bound: The soft information is bounded above by the entanglement entropy of
the soft photon/graviton sector with the hard sector. If `Ext_S` invariants can be bounded by this
entropy, Temporal Issuance connects to the black hole information paradox.

For M1 (holonomy): The holonomy of the `Ext_S` connection can be bounded by the mutual information
between source-side extension paths and target-side observables. Nontrivial holonomy corresponds to
nonzero mutual information between extension paths and holonomy observables — a computable bound.

Team D finding for BL-007: The ICO' obstacle for soft charges can be stated information-theoretically:
the soft charge Q_f is conditionally independent of `Ext_S` structure, given the outgoing radiation
field. That is, I(Q_f; Ext_S | radiation_field) = 0. This is a precise information-theoretic
version of ICO' that is potentially testable.

**Team D summary verdict:** ICO' can be stated precisely as a conditional mutual information bound.
The key open question: is I(Q_f; Ext_S | radiation_field) = 0 or > 0? If the `Ext_S` structure
carries information about Q_f beyond what the radiation field determines, BL-007 is supported.

---

### Team E — Heterodox Synthesis

**Strongest surviving mechanism from Teams A-D:**

The teams converge on the following synthesis:

**Primary candidate: BMS Soft Charge Mechanism (M2) + Holonomy Backbone (M1)**

The synthesis: treat `Ext_S` as a BMS-equivariant connection on a bundle over constraint space.
The morphisms in `ExtCat` carry two types of invariants:
1. Holonomy invariants (from M1): defined purely in `ExtCat`, no physics required
2. BMS soft charge projections (from M2): defined by the functor F: ExtCat -> LorHist_BMS

The key bridge lemma chain:
BL-005 (nontrivial pi_1(BExtCat)) -> BL-004 (nontrivial holonomy) -> BL-001 (BMS covariance)
-> BL-002 (Q_f is morphism-level) -> BL-003 (Q_f != p^mu) -> BL-007 (Q_f is source-side invariant?)

The critical gap: BL-007. Is the supertranslation memory source-defined or target-defined?

The ICO' problem: ICO applied to Q_f instead of p^mu. The same trichotomy applies:
- ICO'-1: Q_f is defined using target-side dynamics (absorbed)
- ICO'-2: source-side invariant but doesn't determine Q_f (insufficient)
- ICO'-3: trivially re-encodes the radiation field (bookkeeping)

**Team E's strongest bet:** BL-007 survives if and only if the BMS supertranslation symmetry is
a genuine symmetry of `ExtCat` (not just of LorHist_BMS). If BMS acts on `ExtCat` morphisms,
then Q_f is a Noether charge for this action — a source-side invariant by construction.

The key question: Is BMS a symmetry of the space of admissible constraint extensions?

This is not answered by BDO or ICO. It is a new question that requires either:
(a) A definition of BMS action on typed source constraints, or
(b) A proof that no such action exists (which would close the BMS escape route definitively).

**Team E recommendation:** Attempt to define a BMS action on `ExtCat`. If it can be defined
consistently (compatibility with admissibility, equivariance of composition), BL-007 may be
provable. If no such action exists, record this as a new obstruction closing the BMS route.

---

## Phase 5: Toy Models

### Toy Model TM-A: Minimal Holonomy Model

**State space:**
```text
Objects: S0, S1, S2 (three constraint states)
Morphisms:
  e01a: S0 -> S1 (admissible extension, type alpha)
  e01b: S0 -> S1 (admissible extension, type beta; parallel to e01a)
  e12:  S1 -> S2 (admissible extension, type gamma)
  e02a: S0 -> S2 (= e12 . e01a, defined by composition)
  e02b: S0 -> S2 (= e12 . e01b, defined by composition; distinct from e02a if holonomy nontrivial)
Loop: e02a and e02b both map S0 -> S2; their composition with a hypothetical e20: S2 -> S0
   would define a loop gamma_a = e20 . e02a and gamma_b = e20 . e02b.
```

**Extension rule:**
`Ext_S` = the rule that alpha-type and beta-type extensions are both admissible from S0 to S1,
but they differ in a binary flag I(e) in {0, 1}.

**Invariant:**
I: Mor(ExtCat) -> {0, 1}; I(e01a) = 0, I(e01b) = 1.
Holonomy of a loop gamma: Hol(gamma) = I(e01a) XOR I(e01b) = 1 (nontrivial).

**Target (if a physical target is chosen):**
Map TM-A to a TQFT: Z(e01a) = [[1, 0], [0, 1]], Z(e01b) = [[0, 1], [1, 0]] (distinct matrices).
Tr(Z(e01a)) = 2, Tr(Z(e01b)) = 2 (same trace — holonomy distinction not visible in trace).
Better: Tr(Z(e02a)) = Tr(e12 * e01a) vs Tr(Z(e02b)) = Tr(e12 * e01b) — differs if e12 is non-symmetric.

**Prediction vs. absorbers:**
The induced order is: S0 <= S1 <= S2. Absorbers (causal order, proof order, transition systems)
can reproduce this order. They cannot reproduce the I-flag distinction unless they independently
define the flag.

**Falsification condition:**
TM-A is falsified if I(e01a) = I(e01b) for every consistent assignment of a binary flag to
parallel morphisms — i.e., if the admissibility rule forces all parallel morphisms to have the
same invariant value. This would mean `Ext_S` admits no morphism-level invariants beyond the
induced order.

---

### Toy Model TM-B: Minimal BMS Memory Model

**State space:**
```text
Objects:
  B_in: in-state at I^- (in-coming constraint state)
  B_out: out-state at I^+ (out-going constraint state, charge quantum numbers only)

Morphisms:
  h1: B_in -> B_out (scattering with no soft emission; zero memory Q_f = 0)
  h2: B_in -> B_out (scattering with soft photon emission; nonzero memory Q_f > 0)

Note: h1 and h2 are parallel morphisms (same boundary objects) with the same
  Poincare four-momentum p^mu(h1) = p^mu(h2) (by total energy-momentum conservation)
  but different BMS soft charges Q_f(h1) = 0 != Q_f(h2) > 0.
```

**Extension rule:**
`Ext_S` = the admissibility rule that both zero-memory and nonzero-memory histories are
admissible from B_in to B_out (this is physically true: you can scatter particles with or
without soft photon emission and conserve total four-momentum either way).

**Invariant:**
Q_f: Mor(ExtCat_BMS) -> R; Q_f(h1) = 0, Q_f(h2) > 0.
This is a morphism-level invariant not determined by the boundary objects (p^mu is the same).

**Target:**
Map TM-B to LorHist_BMS: the functor F maps the parallel extensions to the two scattering
histories. The BMS soft charge is the invariant.

**Prediction vs. absorbers:**
BDO cannot absorb TM-B: p^mu is the same for h1 and h2, so p^mu is NOT a discriminator here.
ICO' applies: is Q_f source-defined? This is the open question. If the source-side constraint
encodes "type of emission" (zero-emission constraint vs. nonzero-emission constraint), Q_f is
source-defined. If not, ICO' applies.

**Falsification condition:**
TM-B is falsified if the morphism invariant Q_f is always determined by target-side dynamics
(radiation field) and cannot be encoded in a source-side extension constraint. A precise
obstruction would be a proof that any source-side invariant I(e) with I(h1) != I(h2) must
encode the outgoing radiation field content — i.e., a BMS-level ICO.

---

### Toy Model TM-C: TQFT-ExtCat Toy Model

**State space:**
```text
ExtCat_TQFT: a symmetric monoidal category with
  Objects: S_0, S_1, S_2 (constraint states; S_0 @ S_1 = S_01, tensor product defined)
  Morphisms:
    e: S_0 -> S_1 (admissible extension)
    e': S_0 -> S_1 (parallel admissible extension, distinct from e)
  Tensor product:
    e @ e': S_0 @ S_0 -> S_1 @ S_1 (parallel composition)
```

**Extension rule:**
`Ext_S` = the symmetric monoidal rule that defines tensor products of extensions as
"simultaneous independent extensions of two constraint systems."

**Invariant (TQFT functor):**
```text
Z: ExtCat_TQFT -> Hilb
  Z(S_0) = C^2 (a 2-dimensional Hilbert space)
  Z(S_1) = C^2
  Z(e)  = [[1, 0], [0, 1]]  (identity, corresponding to "trivial" extension)
  Z(e') = [[0, 1], [1, 0]]  (swap, corresponding to "swapping" extension)

Tr(Z(e)) = 2, Tr(Z(e')) = 2 (same trace; first invariant is not trace)
But: Tr(Z(e) * Z(e')^T) = 0 (off-diagonal overlap is zero; orthogonality in operator space)
```

**Prediction vs. absorbers:**
Z(e) and Z(e') are distinct operators. Their distinction is a morphism-level invariant not
captured by the induced order. The TQFT functor assigns different partition functions to loops
containing e vs. e'. This distinction is captured by the Jones polynomial or similar TQFT
invariants applied to extension loops.

**Falsification condition:**
TM-C is falsified if for every symmetric monoidal functor Z: ExtCat_TQFT -> Hilb, the trace
Tr(Z(e)) = Tr(Z(e')) for all parallel extensions. This would mean TQFT invariants cannot
distinguish parallel extensions — i.e., TQFT morphism-level invariants are not richer than
the induced order.

**Additional check:** Is TM-C absorbed by knot theory / TQFT? The partition functions of loops
in TM-C are knot-theory-like invariants. If they are exactly reproducing a known TQFT invariant,
TM-C is absorbed by that TQFT (e.g., Chern-Simons theory). This would not falsify TM-C but
would classify it as an instance of a known theory.

---

## Phase 6: Failure Analysis

### BL-001 (BMS-Covariant Extension Category)
**Strongest support:** BMS is the natural symmetry group of asymptotically flat spacetimes; defining
BMS-equivariant extension categories is a well-defined mathematical task.
**Strongest failure mode:** The BMS action on source constraints might not be compatible with the
admissibility rule (some BMS transformations might take admissible extensions to inadmissible ones).
**Strongest obstruction:** No known theorem obstructs this. The compatibility check is an open question.
**Status: UNKNOWN.** Requires a definition attempt.

---

### BL-002 (Soft Charge Is Morphism-Level in ExtCat)
**Strongest support:** In LorHist_BMS, soft charges are clearly morphism-level (TM-B demonstrates
this physically: h1 and h2 have the same objects but different Q_f). The question is whether this
morphism-level property is source-defined.
**Strongest failure mode:** Q_f might always be a target-side quantity (dynamical physics of the
radiation field) that cannot be encoded in a source-side extension rule.
**Strongest obstruction:** ICO' — the modified ICO applied to soft charges. No known result rules
this out, but no known result rules it in either.
**Status: UNKNOWN.** The ICO' question is the crux.

---

### BL-003 (Soft Charges Are Not Determined by Poincare Boundary Data)
**Strongest support:** Established physics. The Christodoulou-Kibble memory effect and Strominger's
infrared triangle confirm this. Q_f != f(p^mu) for all f.
**Strongest failure mode:** None for the stated claim. This is a theorem of general relativity.
**Strongest obstruction:** None. This is established.
**Status: SURVIVES.**

---

### BL-004 (Holonomy of Ext_S Connection Is Nontrivial)
**Strongest support:** For bundles over constraint space with non-flat connections, holonomy is
generically nontrivial. The Hannay-Berry phase analogy provides physical intuition.
**Strongest failure mode:** The natural `Ext_S` connection might always be flat (zero curvature),
meaning all parallel transport is trivial.
**Strongest obstruction:** If `ExtCat` is a free category (all morphisms are distinct composites
with no relations), the classifying space is contractible and holonomy trivializes. `ExtCat` must
have relations (equivalences between different extension sequences) for nontrivial holonomy.
**Status: WEAK.** Holonomy requires `ExtCat` to have relations, which requires specifying when
two extension sequences are equivalent. This is not currently defined.

---

### BL-005 (ExtCat Fundamental Group Is Nontrivial)
**Strongest support:** Any category with endomorphisms has nontrivial loops in BExtCat.
**Strongest failure mode:** If `ExtCat` has no endomorphisms (no constraint self-extensions), the
classifying space may be simply connected.
**Strongest obstruction:** For a category with only forward extensions (no reversals, no loops),
BExtCat is a directed acyclic graph, which is contractible (trivial fundamental group).
**Status: WEAK.** Requires `ExtCat` to have reversible extensions or cycles, which is not guaranteed
by the admissibility rule alone.

---

### BL-006 (TQFT Functor from ExtCat Exists)
**Strongest support:** For finite `ExtCat`, the functor always exists by direct construction.
**Strongest failure mode:** The functor might not be symmetric monoidal (tensor products might not
be defined in `ExtCat`).
**Strongest obstruction:** No known obstruction to the existence of some functor. The question is
whether the functor has interesting properties.
**Status: SURVIVES (existence). WEAK (interesting properties require monoidal structure).

---

### BL-007 (Soft Charge Is Source-Side Ext_S Invariant)
**Strongest support:** Team E's synthesis: if BMS acts on `ExtCat` morphisms, Q_f is a Noether
charge of this action and is source-defined.
**Strongest failure mode:** ICO' — the same trichotomy as ICO, applied to Q_f.
**Strongest obstruction:** No known theorem rules out BMS acting on `ExtCat`. But no positive
evidence for it either. This is the critical open question.
**Status: UNKNOWN.** The critical bridge lemma. Fate determines whether BMS evades ICO.

---

### BL-008 (Conformal Target Evades BDO for Massless Theories)
**Strongest support:** In CFT, physical observables are conformal dimensions, not energy-momentum.
BDO's argument uses Poincare-invariant Noether charges; conformal theory has a larger symmetry group.
**Strongest failure mode:** Conformal dimensions might also be object-level (determined by boundary
data in CFT via the operator-state correspondence).
**Strongest obstruction:** In CFT, the operator-state correspondence maps states (objects) to operators
(morphisms). The conformal dimension is a property of the state/operator — it is object-level in the
CFT Hilbert space. BDO might apply to conformal dimension via a different argument.
**Status: WEAK.** BDO might apply to conformal dimensions via the operator-state correspondence.
Requires more careful analysis.

---

### BL-009 (Quantum Path-Integral Over ExtCat Gives Non-Classical Invariant)
**Strongest support:** Quantum superposition over classical completions (path-integral) is more
general than any single classical completion.
**Strongest failure mode:** The path-integral over ExtCat morphisms might reduce to an ordinary
QFT path-integral over field configurations, in which case no new invariant is produced.
**Strongest obstruction:** If `ExtCat` is isomorphic (as a measure space) to the space of field
configurations, the path-integral is identical to ordinary QFT. The question is whether `ExtCat`
is genuinely a different space.
**Status: UNKNOWN.** Depends on the relationship between `ExtCat` and the field configuration space.

---

## W009 Final Artifact

See `explorations/E010-heterodox-bridge-incubator-synthesis.md` for the standalone artifact.

---

## BDO/ICO Evasion Assessment

| Bridge Lemma | Evades BDO? | Evades ICO? | Method |
| --- | --- | --- | --- |
| BL-003 (soft charges != p^mu) | YES: Q_f is morphism-level, not object-level | ICO' remains open | BMS group larger than Poincare |
| BL-007 (soft charge is source-side) | YES if provable | ICO' must be ruled out | BMS acts on ExtCat |
| BL-008 (conformal target) | Possibly: conformal dim might be morphism-level | Open | Conformal group > Poincare |
| BL-004 (holonomy nontrivial) | YES: holonomy is inherently morphism-level (loop invariant) | YES: holonomy is defined in ExtCat, not from target physics | Fiber bundle construction |
| BL-009 (quantum path-integral) | YES: quantum superposition over completions | ICO applied classically; quantum case is open | Path-integral over ExtCat |

**Key finding:** BL-004 (holonomy) is the mechanism that most cleanly evades both BDO and ICO.
Holonomy is a loop invariant — it is inherently morphism-level (BDO doesn't apply, since holonomy
is not determined by objects). And holonomy is defined in ExtCat without reference to target-side
dynamics (ICO doesn't apply, since no completion selector is needed).

The weakness: BL-004 requires nontrivial loops in ExtCat (BL-005), which requires constraints
allowing reversible extension paths. This is a structural requirement on ExtCat, not an obstruction
from target physics.

---

## W008 Escape-Route Connections

| W008 Category | Bridge Lemmas | Verdict |
| --- | --- | --- |
| Category G (soft charges / BMS) | BL-001, BL-002, BL-003, BL-007 | Live. BL-007 is the critical open lemma. |
| Category A (non-Poincare / curved / LQG) | BL-008 | Weak. BDO via operator-state correspondence may still apply. |
| Category B (quantum path-integral) | BL-009 | Open. Depends on ExtCat vs. field-configuration identity question. |
| Category D (holographic / AdS-CFT) | BL-008 (via AdS/CFT duality) | Open. CFT side may evade BDO differently. |
| Category E (source-generated metric) | No direct bridge lemma yet | Not addressed in this pass. |
| Category F (lax functors / infinity) | BL-004 (holonomy in higher categories) | Live. Nontrivial holonomy is natural in infinity-categories. |
| Category H (2-category / enriched) | BL-004, BL-005 | Live. 2-categorical ExtCat has richer loop structure. |

**Highest-leverage W008 route after this W009 pass:** Category G (BMS soft charges). BL-003 is
already established; BL-007 is the critical lemma; the resolution of ICO' is the key research question.

---

## New Claims Warranted (Speculative Only)

**TI-C012 (speculative):** The holonomy group of the `Ext_S` fiber bundle connection Hol(omega)
is a nontrivial invariant of Temporal Issuance for any constraint system with reversible extension
paths. This invariant is morphism-level (not determined by the induced preorder) and is defined
independently of Lorentzian physics.

**TI-C013 (speculative):** BMS supertranslation memory effects may serve as `Ext_S` morphism
invariants, if and only if the BMS group acts as a symmetry of `ExtCat` morphisms. This would
evade both BDO (Q_f is morphism-level, not object-level) and ICO (Q_f would be a source-side
Noether charge, not a target-side completion selector).

---

## Immediate Path Kills from Phase 6

No bridge lemma was killed with a precise obstruction in Phase 6. The closest are:
- BL-005 (nontrivial fundamental group): WEAK, not killed; requires reversible extensions
- BL-008 (conformal target evades BDO): WEAK, not killed; BDO via operator-state may apply

These are not precise obstructions. No new entries to `memory/path-kills.md`.

---

## Recommended Next Step

**Highest expected-value move after W009:** Attempt to define a BMS group action on `ExtCat`.
This is a direct test of BL-001 and, if successful, opens BL-007. If the BMS action cannot be
defined consistently, record this as a new BMS-level obstruction (a precise kill of the Category G
escape route).

Concretely: W000 -> W008 Category G — BMS / Soft Charge Attempt.

Secondary recommendation: formalize TM-A (minimal holonomy model) and compute curvature of the
`Ext_S` connection. A nonzero curvature would support BL-004 and give a standalone mathematical
result.

---

## Closeout Checklist

```yaml
run_record_written: true
phase_1_completed: true
phase_2_completed: true
  candidate_mechanisms: 3 (M1_holonomy, M2_BMS_soft_charge, M3_TQFT)
phase_3_completed: true
  bridge_lemmas_identified: 9 (BL-001 through BL-009)
phase_4_completed: true
  teams_run: [Physics, Mathematics, Complex_Systems, Information_Theory, Heterodox_Synthesis]
phase_5_completed: true
  toy_models: 3 (TM-A, TM-B, TM-C)
phase_6_completed: true
bdo_ico_evasion_assessed: true
  cleanest_evasion: BL-004_holonomy (loop invariant; neither BDO nor ICO applies)
  critical_open_question: BL-007 (BMS_action_on_ExtCat; ICO_prime)
w008_escape_routes_implicated:
  - Category_G: live_BL-007_critical
  - Category_F: live_holonomy_in_higher_categories
  - Category_H: live_2-categorical_ExtCat
new_claims_warranted:
  - TI-C012: speculative
  - TI-C013: speculative
path_kills_from_phase_6: none_precise
exploration_file_written: true
claim_ledger_updated: true
memory_log_updated: true
memory_summary_updated: true
roadmap_updated: true
next_trigger_plan_updated: true
metrics_updated: true
files_changed:
  - agent-runs/RUN-0031-w009-heterodox-bridge-incubator.md
  - explorations/E010-heterodox-bridge-incubator-synthesis.md
  - CLAIM-LEDGER.md
  - memory/steward-memory-log.md
  - memory/steward-memory-summary.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
  - agent-governance/STEWARD-METRICS.md
  - ROADMAP.md
```
