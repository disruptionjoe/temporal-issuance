---
artifact_type: run_record
run_id: RUN-0035
workflow: W008 Category G (detailed formal pass)
status: complete
escape_route: Category G — BMS soft charges / asymptotic symmetry
trigger: NEXT-TRIGGER-PLAN (set by RUN-0031 W009 pass) — W008 Category G highest priority
date: 2026-06-22
claims_touched:
  - TI-C013
  - TI-C007
bridge_lemmas_tested:
  - BL-001 (BMS-covariant ExtCat)
  - BL-007 (Q_f is source-side)
---

# RUN-0032: W008 Category G — BMS Soft Charges / Asymptotic Symmetry

## Context Note

This is RUN-0034, the detailed four-phase W008 Category G formal pass (Phases 1–4 with anti-local-
minimum gate). RUN-0032 ran a quick BMS absorbed-construction pass; RUN-0033 ran a bridge-tree
verdict closing the absorb-known-physics strategy. RUN-0034 is the rigorous W008 analysis requested
after RUN-0031 (W009). Its Phase 4 gate found Category G is NOT a local minimum: Skeptic 4 opened
the celestial holography route as a genuine conditional live direction. RUN-0033's "no independent
bridge" verdict is about the current absorb-known-physics strategy and is compatible with RUN-0034's
conditional live finding (celestial holography is a different formalization approach, not an
absorption of known physics).

## Timestamp

2026-06-22

---

## Phase 1: Obstruction Inventory

### BDO Assumptions Relevant to Category G

Boundary-Determination Obstruction (RUN-0028):

- **Setting:** `LorHist(M, eta, A)` where `(M, eta)` is fixed Minkowski spacetime, `A` is a
  Poincare-invariant, Noether-regular action.
- **Objects of LorHist:** Full Cauchy boundary data pairs `(B0, B1)` that determine total `p^mu`.
- **Result:** `p^mu(F(e))` is determined by the target object `F(S')`, not by the morphism `e`.
  For any parallel pair `e1, e2: S => S'`, `p^mu(F(e1)) = p^mu(F(e2))`.
- **Scope:** BDO applies **only** to the observable `p^mu` in the Poincare-invariant Minkowski
  control case. BDO says nothing about:
  - Observables other than `p^mu` (charges, memory, holonomy)
  - Symmetry groups beyond Poincare (BMS, diffeomorphisms, extended BMS)
  - Targets other than `(M, eta, A)` with Poincare-invariant action

**BDO relevance to Category G:** BDO does **not** directly obstruct Category G, because Category G
proposes `Q_f` (BMS soft charge) as the invariant, not `p^mu`. BDO explicitly leaves open any
observable that is morphism-level and not determined by Poincare boundary data.

### ICO Assumptions Relevant to Category G

Inverted Construction Obstruction (RUN-0029):

- **Setting:** `LorHist'` with momentum-underdetermining objects (partial/asymptotic data).
- **Result:** With `p^mu` morphism-level, its variation is indexed by target-side dynamical
  physics (coupling constants, Hamiltonian, scattering amplitudes). Any selection mechanism
  falls to ICO-1 (imports target dynamics), ICO-2 (insufficient), or ICO-3 (bookkeeping).
- **Scope:** ICO applies to `p^mu` and any observable whose morphism-level variation is indexed
  by target-side Hamiltonian selection. ICO does **not** a priori apply to observables whose
  variation is indexed by covariant asymptotic data (like BMS charges at null infinity).

**ICO' — Modified ICO for Category G:** RUN-0031 defined ICO' for soft charges:
- ICO'-1: `Q_f` definition imports target-side radiation dynamics (absorbed)
- ICO'-2: source-side definition exists but is insufficient to determine `Q_f` (insufficient)
- ICO'-3: definition trivially re-encodes the radiation field (bookkeeping)
- **Escape:** `Q_f` is a Noether charge of BMS acting on `ExtCat` as an independent structure

**Key distinction from ICO:** The infrared triangle (Weinberg soft theorem / BMS memory / soft
theorem) shows `Q_f` differences are **universal** — independent of the target-side Hamiltonian.
ICO fires because `p^mu` variation is Hamiltonian-specific. `Q_f` variation is covariant (angle-
dependent flux) and does not require specifying a Hamiltonian to define. This is the precise
gap that ICO' is designed to address.

---

## Phase 2: Category G Escape Route Specification

### What Does "BMS Action on ExtCat Morphisms" Mean Formally?

**ExtCat structure (as established):**

```text
Objects: typed source constraint states S = (C, type)
Morphisms: admissible extensions e: S -> S' satisfying the admissibility predicate P(e)
Composition: sequential extension (concatenation of constraint updates)
Identity: trivial self-extension id_S: S -> S
```

**BMS group (relevant subgroup: supertranslations):**

```text
BMS_supertrans = { T_f | f: S^2 -> R smooth }
T_f acts on Minkowski null infinity I^+ by: u -> u + f(theta, phi)
where u is the retarded time coordinate and (theta, phi) are celestial sphere coordinates.
```

**What BL-001 requires:** A group homomorphism

```text
rho: BMS -> Aut(ExtCat)
```

where `Aut(ExtCat)` is the group of auto-equivalences of `ExtCat` (functors `F: ExtCat -> ExtCat`
with natural isomorphisms `F o F^{-1} ~ id` and `F^{-1} o F ~ id`). Concretely:

- For each `g in BMS` and each morphism `e: S -> S'` in `ExtCat`, define `g · e: g · S -> g · S'`
- The action must satisfy: `g · (e2 o e1) = (g · e2) o (g · e1)` (functor condition)
- The action must preserve admissibility: if `P(e)` holds, then `P(g · e)` holds
- The action must be a group action: `(g1 g2) · e = g1 · (g2 · e)`, `id · e = e`

**What must be true for BL-001 to hold:**

1. Objects of `ExtCat` must admit a BMS group action: `g: S -> g · S` preserving object type
2. Morphisms must transform equivariantly: `g · e` must be an admissible extension `g · S -> g · S'`
3. The admissibility predicate `P` must be BMS-invariant: `P(e) <=> P(g · e)`
4. The action on morphisms must be non-trivial: there must exist `g, e` with `g · e != e`

**What the ICO' trichotomy requires for BL-007:**

- If BL-001 holds AND `Q_f` is the Noether charge of the `T_f` action on `ExtCat`:

```text
Q_f(e) = d/ds|_{s=0} [Action(T_{sf} · e)] = lim_{epsilon -> 0} [Action(T_{epsilon f} · e) - Action(e)] / epsilon
```

- Then `Q_f` is source-side: it depends only on how the supertranslation moves the extension,
  not on target-side completion data.
- This escapes ICO'-1 (no target dynamics imported), ICO'-2 (Q_f is fully determined), and
  ICO'-3 (Noether charge is not bookkeeping — it is derived from a genuine symmetry).

---

## Phase 3: Construction Attempt

### Attempt 3.1 — Pull-Back Construction

**Setup:**

Let `F: ExtCat -> LorHist_BMS` be a functor mapping admissible extensions to Lorentzian histories
in BMS-symmetric spacetime. BMS acts on `LorHist_BMS` (the BMS group is exactly the asymptotic
symmetry group of that category). The pull-back proposal:

```text
g · e := F^{-1}(g · F(e))
```

**Analysis:**

**Step 1: Is F invertible?**

No. `F` is generically neither injective nor surjective on morphisms:

- Non-injectivity: Multiple admissible extensions `e1, e2: S -> S'` in `ExtCat` can map to the
  same Lorentzian history `F(e1) = F(e2)` if they encode the same physical transition but differ
  in internal labeling.
- Non-surjectivity: `LorHist_BMS` contains morphisms (scattering processes with specific matter
  field configurations) that may not be in the image of any source-side admissible extension.

**Step 2: Does `g · F(e)` land in `image(F)`?**

Not necessarily. The BMS action on `LorHist_BMS` is well-defined: `g` sends a scattering history
with asymptotic data at `I^+` to another scattering history with BMS-shifted asymptotic data.
But there is no guarantee that the BMS-shifted history `g · F(e)` is in the image of `F`.

Formally: let `h = F(e)` be a Lorentzian history. `g · h` is another Lorentzian history with
asymptotic boundary condition shifted by the supertranslation `f`. For `F^{-1}(g · h)` to be
defined, we need `g · h` to be in `image(F)`. This is a non-trivial constraint.

**Step 3: Even if `g · F(e) in image(F)`, is the result well-defined?**

If `F` is non-injective (as argued in Step 1), then `F^{-1}(g · F(e))` is a set of morphisms,
not a single morphism. The pull-back is ambiguous.

**Step 4: Does the pull-back satisfy ICO'-1?**

YES, the pull-back construction **falls to ICO'-1**. The proposed action `g · e = F^{-1}(g · F(e))`
requires computing `F(e)` (sending `e` to the Lorentzian category), applying `g` in the Lorentzian
category (which involves target-side asymptotic structure), and pulling back. The action is defined
entirely through the target category `LorHist_BMS`. It is not source-intrinsic.

**Structural obstacle:**

The pull-back construction presupposes `F` is an invertible equivalence. If `F` is not invertible,
the pull-back is ill-defined. Even if `F` is an equivalence, the resulting BMS action on `ExtCat`
is derived from the target category and falls immediately to ICO'-1.

```yaml
attempt_id: 3.1
construction_found: no
structural_obstacle: >
  F: ExtCat -> LorHist_BMS is generically non-invertible (non-injective and non-surjective on
  morphisms). Even when well-defined, the pull-back action g · e = F^{-1}(g · F(e)) is
  target-defined — it computes the BMS action in LorHist_BMS and pulls back. This falls to
  ICO'-1 (target physics import). The pull-back construction cannot produce a source-intrinsic
  BMS action.
ico_prime_category: ICO'-1
verdict: killed
```

---

### Attempt 3.2 — Intrinsic Parametrization

**Setup:**

Suppose each `ExtCat` morphism `e: S -> S'` carries additional labeling data:

```text
lambda(e): S^2 -> R  (a smooth function on the celestial sphere)
```

where `lambda(e)` encodes "when/where" the extension is issued at each angle of null infinity.
Intuitively: a constraint extension that propagates outward from the source records a retarded-time
stamp `lambda(e)(theta, phi)` at each angle of the celestial sphere.

**The proposed BMS action (supertranslations):**

```text
T_f · e = e_{shifted}  where lambda(T_f · e) = lambda(e) + f
```

The supertranslation `T_f` shifts the retarded-time label by `f(theta, phi)` at each angle,
without changing the source objects `S, S'` or the constraint content of `e`.

**Analysis:**

**Step 1: What is the source of `lambda(e)`?**

This is the critical question. There are two readings:

**(A) Source-intrinsic reading:** `lambda(e)` is defined from the source data — the typed
constraint `C` and the admissibility rule. For example: the constraint system has a "retarded
time of extension issuance" built into the constraint type, so `lambda(e)` is the angle-resolved
emission time of the extension in the source description.

**(B) Target-derived reading:** `lambda(e)` is pulled from `LorHist_BMS` — it is the actual
retarded time at null infinity, accessible only by mapping `e` to a Lorentzian history through
`F` and reading off the asymptotic field configuration.

If (A): the action is source-intrinsic and potentially escapes ICO'-1.
If (B): the action falls to ICO'-1 (target physics import).

**Step 2: Can `lambda(e)` be defined source-intrisically?**

For `lambda(e)` to be source-intrinsic, it must be determined by the typed constraint data alone —
not by the Lorentzian dynamics of field propagation. This faces a structural obstacle:

The BMS celestial sphere `S^2` is the space of null directions at null infinity in Minkowski
spacetime. It is a **geometric** object tied to the Lorentzian causal structure of the target.
A source-side constraint state `S = (C, type)` carries no canonical reference to null directions
unless those null directions are explicitly embedded in the constraint type.

**Possible escape:** If the constraint type explicitly includes a null-direction-resolved label
(i.e., if `C` is a typed constraint with a `S^2`-indexed component), then `lambda(e)` can be
read off without invoking target dynamics. This would require:

```text
C = (C_internal, c: S^2 -> R)   [constraint with celestial sphere label]
lambda(e: S -> S') = c(S') - c(S)  [difference of celestial labels across extension]
```

This is formally coherent as an additional piece of structure on `ExtCat`.

**Step 3: Does the supertranslation preserve admissibility?**

The shifted extension `T_f · e` has `lambda(T_f · e) = lambda(e) + f`. For this to remain admissible,
the admissibility predicate `P` must be:

- **Independent of `lambda`:** `P(e)` does not depend on the celestial label `lambda(e)`. Then
  `P(T_f · e) = P(e)` trivially.
- **Or covariant in `lambda`:** `P(T_f · e)` holds whenever `P(e)` holds, for any smooth `f`.

The first case (P independent of lambda) is the simplest and covers any admissibility rule that
does not reference the celestial sphere structure. This is achievable.

**Step 4: Does this give a nontrivial `Q_f`?**

If `lambda(e)` is source-intrinsic and `T_f` acts as label-shift, the Noether charge is:

```text
Q_f(e) = integral_{S^2} f(theta, phi) * delta_lambda(e)(theta, phi) d^2 Omega
```

where `delta_lambda(e)` is the "celestial label density" of the extension. For a localized
extension (one that contributes a delta-function in angle), this becomes:

```text
Q_f(e) = f(theta_0, phi_0)  [for extension localized at direction (theta_0, phi_0)]
```

For an angularly spread extension, `Q_f(e) = int f * rho_e dOmega` where `rho_e` is the
angular distribution of the extension's celestial label.

This `Q_f` is source-side (it depends on `lambda(e)`, which is source-intrinsic by assumption),
morphism-level (different parallel extensions can have different `lambda` profiles), and
nontrivial (it is not determined by the induced preorder `<=_S`, since two extensions from
`S` to `S'` can differ in their celestial profile `lambda` while having identical constraint content).

**Step 5: Does `Q_f` satisfy ICO'-1, ICO'-2, or ICO'-3?**

- **ICO'-1:** Does `Q_f` import target-side radiation dynamics? Under the source-intrinsic reading
  of `lambda`, NO. The celestial label `lambda(e)` is a component of the source constraint type.
  No Lorentzian dynamics are invoked. **ICO'-1 does not apply.**

- **ICO'-2:** Is the source-side invariant insufficient to determine `Q_f`? Under reading (A),
  `Q_f` is fully determined by `lambda(e)` and `f`. **ICO'-2 does not apply.**

- **ICO'-3:** Is `Q_f` trivially re-encoding the radiation field? The celestial label `lambda(e)`
  is a source-side structure, not a re-encoding of radiation. **However**, the question is whether
  this is substantive or just bookkeeping.

**The critical ICO'-3 challenge:**

Is adding `lambda: S^2 -> R` to the source constraint type a genuine physical proposal, or is
it trivially importing the BMS structure under a different name? The answer depends on whether
the celestial label has an independent physical motivation from the source side:

- **If `lambda(e)` is just the retarded time of the source extension, read off from a clock in the
  source system:** This is potentially source-intrinsic (the source has an internal clock plus
  angular resolution).
- **If `lambda(e)` is only interpretable as an asymptotic coordinate at null infinity:** This is
  target-derived and falls to ICO'-3.

**Verdict on Attempt 3.2:**

The construction is **partial** and **conditional**.

- What works: If source constraints are given an `S^2`-indexed celestial label component, then
  the supertranslation action `T_f · e = e[lambda + f]` is formally well-defined, preserves
  admissibility, and gives a nontrivial source-side `Q_f`.
- What fails: The motivation for the celestial label `lambda` is not source-intrinsic unless
  the constraint type already contains `S^2`-indexed data. The celestial sphere `S^2` is a
  geometric object of the Lorentzian target (null directions at null infinity). Importing it
  into the source constraint type requires an independent physical argument for why source
  constraints should care about null directions.
- Status: `partial` — the construction goes through formally if the extra structure is assumed,
  but the extra structure (`lambda: S^2 -> R`) is not independently motivated from the source side
  without already presupposing Lorentzian geometry.

**Formal precision on the ICO'-3 failure mode:**

The action `T_f · e = e[lambda + f]` with `lambda: S^2 -> R` source-intrinsic would escape
all three ICO' legs. But asking "why does a source constraint state carry a smooth function
on `S^2`?" requires answering "because `S^2` parametrizes null directions at null infinity."
This answer imports the Lorentzian geometric target. The `lambda` structure is not independently
motivated; it is the BMS structure under a new name. This is a soft version of ICO'-3: not
trivial bookkeeping, but also not independent source content.

```yaml
attempt_id: 3.2
construction_found: partial
structural_obstacle: >
  The celestial sphere S^2 in the supertranslation labeling lambda: S^2 -> R is a geometric
  object of the Lorentzian target (null directions at null infinity). Adding lambda as a
  source constraint component requires importing S^2 from the target geometry. If lambda is
  independently motivated from the source (e.g., the source constraint system has an intrinsic
  S^2-resolved structure for physical reasons unrelated to Lorentzian geometry), the construction
  succeeds. If lambda is added because BMS requires it, the construction is a soft ICO'-3
  (motivated bookkeeping: renaming target structure as source structure). The key missing step:
  an independent physical motivation for S^2-indexed source constraints without presupposing the
  Lorentzian target.
ico_prime_category: escapes_all_three [conditional on S^2-indexed source constraints being independently motivated]
verdict: conditional_live_route [requires independent motivation for celestial-sphere-indexed source data]
```

---

### Attempt 3.3 — Celestial Amplitude Reinterpretation

**Setup:**

The extended BMS group and its w_{1+infinity} algebra act on **celestial amplitudes**: the S-matrix
elements decomposed on the celestial sphere `S^2` via a Mellin transform in the energies. Under
this decomposition, scattering amplitudes become correlation functions of operators on `S^2`, and
the extended BMS acts as a (local) symmetry of these correlators.

The proposal: if `ExtCat` morphisms ARE celestial amplitudes (or their source-side analogues —
data on `S^2` encoding extension transitions), then `w_{1+infinity}` acts naturally on `ExtCat`.

**Analysis:**

**Step 1: Can `ExtCat` morphisms be identified with celestial data?**

Celestial amplitudes are functions of celestial sphere coordinates: for a 2->2 scattering process,
the celestial amplitude is a function on `(S^2)^4` (one `S^2` per external particle direction)
with conformal weights. For this identification to work, `ExtCat` morphisms `e: S -> S'` must
carry data equivalent to:

```text
A(z, z-bar; w, w-bar; ...) [celestial amplitude on (S^2)^n]
```

where `(z, z-bar)` are stereographic coordinates on `S^2`. This requires morphisms to be labeled
by elements of `S^2` — again the celestial sphere structure.

**Step 2: Is this identification source-side or target-side?**

The celestial amplitude is the S-matrix (target-side) rewritten in celestial coordinates. The
original S-matrix is defined by the target dynamics (Hamiltonian, asymptotic states, LSZ reduction).
The celestial rewriting is a coordinate change, not a change in physics. Therefore:

- The celestial amplitude is **target-defined**: it encodes the same physical content as the
  S-matrix element, just expressed in `S^2`-labeled basis.
- Identifying `ExtCat` morphisms with celestial amplitudes would make `ExtCat` a relabeling
  of the target S-matrix, not an independent source-side structure.

**Step 3: Does this reinterpretation avoid ICO'-1?**

No. The w_{1+infinity} action on celestial amplitudes is defined on the S-matrix: it acts on
target-side scattering data. If `ExtCat` morphisms are identified with celestial amplitudes,
then `w_{1+infinity}` acts on them through their S-matrix content. This falls to ICO'-1.

**Step 4: Is this a new category or a relabeling of `LorHist_BMS`?**

It is a relabeling. The category of celestial amplitudes is `LorHist_BMS` in celestial coordinates.
The morphisms are still target-side scattering processes. The objects are still asymptotic in/out
states. The functor `F: ExtCat -> LorHist_BMS` is now identified with the identity on the celestial
side — i.e., `ExtCat = LorHist_BMS` (celestial). This collapses the source/target distinction that
Category G is meant to establish.

**Structural obstacle:**

The celestial amplitude reinterpretation does not provide a source-side BMS action on `ExtCat`.
It provides a way to **rename** the BMS action on the target as if it were acting on the source.
The source/target distinction is the very thing that must be established for BL-001 to hold.
Renaming the target as the source does not establish the distinction.

```yaml
attempt_id: 3.3
construction_found: no
structural_obstacle: >
  Celestial amplitudes are the S-matrix (target-side) in celestial coordinates. Identifying
  ExtCat morphisms with celestial amplitudes makes ExtCat a relabeling of LorHist_BMS in
  celestial coordinates, not an independent source-side structure. The w_{1+infinity} action
  is then the standard action on the target S-matrix, not a source-intrinsic symmetry. This
  collapses the source/target distinction that the BMS escape route requires. The reinterpretation
  falls to ICO'-1 (target physics import) and additionally fails to preserve the source/target
  independence that BL-001 needs.
ico_prime_category: ICO'-1
verdict: killed
```

---

### Attempt 3.4 — Independent BMS Representation

**Setup:**

Assert an independent representation `rho: BMS -> Aut(ExtCat)` without grounding it in
`LorHist_BMS`. Determine what additional structure on `ExtCat` would be required to define `rho`,
and whether that structure can be specified using only source-side data.

**Analysis:**

**Step 1: What is needed to define `rho: BMS -> Aut(ExtCat)`?**

`rho` must assign to each BMS element `g` an auto-equivalence `rho(g): ExtCat -> ExtCat` such that:
- `rho(g)` sends objects to objects: for each `S in Ob(ExtCat)`, `rho(g)(S)` is another
  source constraint state.
- `rho(g)` sends morphisms to morphisms: for each `e: S -> S'`, `rho(g)(e): rho(g)(S) -> rho(g)(S')`.
- `rho(g)` respects composition: `rho(g)(e2 o e1) = rho(g)(e2) o rho(g)(e1)`.
- `rho` is a group homomorphism: `rho(g1 g2) = rho(g1) o rho(g2)`.

**Step 2: What structure is needed on source constraints?**

For `rho(g)(S)` to be defined, source constraint states `S` must have an action of BMS. The BMS
group structure relevant for supertranslations is:

```text
BMS_supertrans = Diff+(S^2) x C^infty(S^2)  (or: Diff+(S^2) semidirect C^infty(S^2) for full BMS)
```

For `rho` to be non-trivial, the objects of `ExtCat` must carry a representation of `C^infty(S^2)`
(at minimum) that is not trivial. This requires objects to have some `S^2`-indexed structure.

**Step 3: What `S^2` structure can exist on source constraints independently?**

There are three candidate answers:

**(A) The source constraint state is a section of a bundle over `S^2`.** If `S` is a smooth
function or distribution on `S^2` (e.g., a charge distribution at each null direction), then
supertranslations act by shifting the `S^2` argument. This gives a non-trivial `rho`.

**(B) The source constraint state carries a co-character of `Diff+(S^2)`.** If the type of `C`
includes a conformal weight (a number representing how the constraint transforms under diffeomorphisms
of `S^2`), then superrotations (the Diff+(S^2) part of extended BMS) act non-trivially.

**(C) The source constraint state has no `S^2` structure.** Then the only BMS representation is
the trivial one (`rho(g)(S) = S` for all `g`), and any action on morphisms must also be trivial
or ill-defined without `S^2` structure on objects.

**Step 4: Can the `S^2` structure on source constraints be independently motivated?**

This is the same question encountered in Attempt 3.2. The `S^2` of BMS is the celestial sphere —
the space of null directions at null infinity in Minkowski spacetime. For a source constraint state
to carry a natural `S^2`-indexed structure without importing Lorentzian geometry, one of the
following must be true:

1. **The source constraints are themselves localized at `S^2` points.** Example: source constraints
   are operators in a 2D CFT on `S^2`. This is the celestial holography setting (Attempt 3.4 reads
   into Attempt 3.3/Skeptic 4 territory).

2. **The source constraints arise from a pre-geometric structure that has `S^2` naturally.** For
   example, if the constraint category is the category of representations of a quantum group whose
   representation ring has an `S^2` character variety, then `S^2` appears naturally without
   presupposing Lorentzian geometry.

3. **No independent motivation exists.** The `S^2` structure is imported from the target by hand.

**Step 5: What is the structural verdict?**

Options 1 and 2 are speculative new physical theories (they require either identifying source
constraints with 2D CFT operators on `S^2`, or finding a quantum group with `S^2` character
variety). Neither is established. Option 3 is the default if no independent motivation is found.

The independent BMS representation `rho: BMS -> Aut(ExtCat)` requires `S^2` structure on
source constraint states. Without an independent motivation for this structure, the representation
either:
- Is trivial (if `S^2` structure is absent), or
- Imports target geometry (if `S^2` structure is added because BMS requires it)

**What survives as a conditional route:**

If source constraints are independently found to carry `S^2`-indexed data (for a reason unrelated
to BMS), then an independent BMS representation is constructible. Specifically:

```text
If C_type includes an S^2-indexed component c: S^2 -> R, then:
  T_f · S = S[c + f]  (supertranslation acts by adding f to the S^2-index)
  T_f · e = e[c + f]  (equivariant extension)
  Q_f(e) = int f * dc/dlambda dOmega  (Noether charge)
```

This is the 3.2 construction in abstract form. The verdict from 3.2 applies here as well.

```yaml
attempt_id: 3.4
construction_found: partial
structural_obstacle: >
  An independent BMS representation rho: BMS -> Aut(ExtCat) requires source constraint states
  to carry S^2-indexed data. The S^2 of BMS is the celestial sphere of Lorentzian null infinity.
  Without an independent motivation for S^2-indexed source constraints (from outside the BMS
  context), the representation is either trivial (if S^2 structure is absent) or a soft import
  of target geometry (ICO'-3 or soft ICO'-1). The construction goes through formally under the
  assumption of S^2-indexed source constraints, but this assumption is not independently motivated.
  A new physical argument linking the source constraint type to S^2-indexed data — without
  presupposing Lorentzian geometry — is required. Candidate: celestial holography (see Skeptic 4).
ico_prime_category: escapes_all_three [conditional on S^2-indexed source constraints being independently motivated without Lorentzian presupposition]
verdict: conditional_live_route [same conditional as 3.2; the obstacle is the motivation for S^2 structure on source objects]
```

---

### Phase 3 Summary

| Attempt | Construction Found | Structural Obstacle | ICO' Category | Verdict |
| --- | --- | --- | --- | --- |
| 3.1 Pull-back | no | F not invertible; action is target-defined | ICO'-1 | killed |
| 3.2 Intrinsic parametrization | partial | S^2 structure on source not independently motivated | escapes all three [conditional] | conditional live route |
| 3.3 Celestial amplitude reinterpretation | no | ExtCat becomes relabeling of LorHist_BMS | ICO'-1 | killed |
| 3.4 Independent BMS representation | partial | Same S^2 motivation gap as 3.2 | escapes all three [conditional] | conditional live route |

**Phase 3 finding:** Attempts 3.1 and 3.3 are killed with precise obstructions. Attempts 3.2 and
3.4 survive conditionally: they construct a valid BMS action on `ExtCat` IF source constraints
carry independently-motivated `S^2`-indexed data. The precise blocking question is:

> Does the source constraint type `C` have an `S^2`-indexed component for reasons independent of
> the BMS group and Lorentzian null infinity?

This is a single, precise, bounded open question. It is not "BL-001 is proved" — it is "what
independent motivation exists for celestial-sphere-indexed source data?"

---

## Phase 4: Anti-Local-Minimum Gate

### Skeptic 1 — BMS Expert: Does w_{1+infinity} Find Footing in ExtCat?

**Argument:**

"You've analyzed the classical BMS group (Lorentz semidirect supertranslations) and noted that
supertranslations require `S^2`-indexed source data. But you haven't considered the **extended BMS**
group, specifically the `w_{1+infinity}` algebra. `w_{1+infinity}` acts on celestial amplitudes as an
infinite-dimensional algebra of soft symmetries. The algebra is generated by `w_{m,n}` operators
for `(m, n) in Z^2` and encodes the full tower of soft theorems. Now: does `w_{1+infinity}` find a
footing in `ExtCat` that the classical supertranslation group doesn't?"

**Analysis:**

The `w_{1+infinity}` algebra is the infinite-dimensional algebra of area-preserving diffeomorphisms
of a 2-sphere (or equivalently, the algebra of soft graviton modes at `I^+`). Its generators in the
celestial amplitude context are the wedge algebra elements that act as differential operators on
celestial amplitudes.

For `w_{1+infinity}` to act on `ExtCat` without requiring `S^2` structure on source states, it would
need to find an **algebraic** (non-geometric) footing. Possibilities:

1. **`w_{1+infinity}` as a deformation of the extension composition algebra.** If the algebra of
   morphisms in `ExtCat` (under composition) admits a deformation by `w_{1+infinity}` generators
   acting as "soft insertions," this would give a non-geometric footing. But this requires the
   morphism space to have a natural `w_{1+infinity}` module structure, which again requires `S^2`
   structure or a 2D field theory structure on the morphisms.

2. **`w_{1+infinity}` as the deformation quantization of the constraint-extension Poisson bracket.**
   If `ExtCat` morphisms carry a Poisson bracket (from a source-side action principle), and if
   `w_{1+infinity}` is the quantization of this Poisson bracket, then `w_{1+infinity}` acts on
   quantum morphisms without geometric `S^2` data. This is a new physical claim requiring an action
   principle on `ExtCat`.

3. **`w_{1+infinity}` acting on the derived category of `ExtCat`.** The derived category `D^b(ExtCat)`
   (if `ExtCat` is enriched over chain complexes) can carry more symmetry than the classical category.
   But `w_{1+infinity}` is specifically tied to 2D CFT and celestial geometry; it does not naturally
   act on abstract derived categories.

**Does `w_{1+infinity}` open a new route?**

Possibility 2 (deformation quantization of the constraint Poisson bracket) is the most interesting.
If source constraints carry a symplectic structure, and if `w_{1+infinity}` is the Lie algebra of
symplectomorphisms of the constraint phase space, then `w_{1+infinity}` acts naturally. But this
requires:
- `ExtCat` to be a symplectic groupoid (objects = constraint phase space, morphisms = symplectomorphisms)
- The celestial `S^2` to emerge as the space of "symplectic directions" in the constraint phase space

This is a genuine mathematical proposal. It is speculative, not established, but it does not
require importing `S^2` from the Lorentzian target. If the constraint phase space has a natural
`S^2` symmetry (e.g., from angular momentum in the source), then `w_{1+infinity}` could act.

```yaml
skeptic_id: S-1
argument: >
  The w_{1+infinity} algebra might act on ExtCat through the symplectic/Poisson structure of
  the source constraint phase space, not through geometric S^2 structure. If the constraint
  phase space is a symplectic manifold and w_{1+infinity} is the quantization of its
  symplectomorphism algebra, then w_{1+infinity} acts on quantum ExtCat without presupposing
  Lorentzian null infinity.
analysis: >
  This is a genuine conditional route: if (a) ExtCat morphisms are symplectomorphisms of a
  source constraint phase space, and (b) the symplectic phase space has an S^2-isomorphic
  structure (e.g., from angular momentum symmetry of the source constraints), then
  w_{1+infinity} acts on ExtCat as the quantized symplectomorphism algebra. The S^2 would
  arise from the source's angular momentum sector, not from Lorentzian geometry. This
  bypasses the S^2-motivation problem from 3.2/3.4. The route is speculative but not
  obviously blocked — it requires defining ExtCat as a symplectic groupoid with S^2 Poisson
  manifold structure.
verdict: conditional route [new direction not addressed in attempts 3.1-3.4]
```

---

### Skeptic 2 — Category Theorist: Profunctor / Cospan Formulation

**Argument:**

"You've required BMS to act directly on `ExtCat` as a group of auto-equivalences. But there's a
more flexible setting: **profunctors** (or distributors) between categories. A profunctor
`P: C -|-> D` is a functor `D^op x C -> Set`. The BMS group could act via a profunctor
`P: BMS-orbits -|-> ExtCat` without requiring an invertible action on `ExtCat` objects. Similarly,
a **cospan** formulation (diagram `ExtCat -> X <- BMS-category`) might give morphism-level
invariants indexed by BMS sectors without requiring BMS to act directly on `ExtCat`."

**Analysis:**

**Profunctor route:** A profunctor `P: BMS-orbits -|-> ExtCat` assigns to each pair
`(orbit, morphism)` a set of "compatibilities." The BMS charge sectors could label these
profunctor cells. This would give:

```text
Q_f-indexed sector: a morphism e: S -> S' lies in sector Q_f(e) if P(T_f-orbit, e) is nonempty.
```

This bypasses the requirement for a direct group action: BMS sectors label morphisms via the
profunctor without BMS acting as auto-equivalences of `ExtCat`.

**Does this escape ICO'?** Partially. The profunctor `P` must still be defined in a way that
assigns BMS charges to source-side morphisms. If `P` is defined by pulling back from `LorHist_BMS`,
it falls to ICO'-1. If `P` is defined source-intrinsically (e.g., by the `lambda` label from 3.2),
it faces the same `S^2` motivation question.

**New content beyond 3.1-3.4:** The profunctor formulation relaxes the requirement from "BMS acts
on `ExtCat`" to "there is a BMS-compatible correspondence between BMS-orbits and ExtCat morphisms."
This is weaker and more achievable. Specifically:

```text
Q_f(e) can be defined via a profunctor:
  - Objects of BMS-orbits: supertranslation-equivalent classes of asymptotic data
  - Profunctor P: each ExtCat morphism e is "in Q_f-sector" if it has S^2-label satisfying
    int f * lambda(e) dOmega = Q_f
```

This gives a Q_f-indexed morphism classification without requiring BMS to be a symmetry group of
`ExtCat`. The classification is still conditioned on `lambda(e)` being source-intrinsic, but the
requirement is weaker (no group action, just a labeling correspondence).

**Does the cospan route add anything new?** The cospan `ExtCat -> X <- BMS-cat` could make `X` the
category of "boundary data compatible with both source extensions and BMS charges." If `X` is
independently definable (e.g., as a category of `S^2`-labeled charge data), then the cospan gives
morphism-level BMS charges without direct group action on `ExtCat`. This is related to the
"boundary/bulk split" in Skeptic 4's holographic argument.

```yaml
skeptic_id: S-2
argument: >
  A profunctor P: BMS-orbits -|-> ExtCat (or a cospan through a charge-labeling category X)
  can assign BMS charge sectors to ExtCat morphisms without requiring BMS to act as a group
  of auto-equivalences of ExtCat. This weakens the BL-001 requirement from a group action to
  a correspondence.
analysis: >
  The profunctor route is a genuine relaxation of BL-001. Instead of proving BMS is a symmetry
  of ExtCat, it suffices to define a BMS-compatible correspondence (profunctor) that assigns
  soft-charge sectors to morphisms. The correspondence is still conditioned on S^2-labeled
  source data (the lambda structure from 3.2), but the mathematical requirement is weaker.
  This opens a new sub-route: BL-001' (BMS-compatible profunctor from BMS-orbits to ExtCat)
  as a weaker sufficient condition for BL-007. The obstacle (S^2 motivation for source data)
  remains but may be easier to satisfy for the profunctor version than for the direct group
  action version.
verdict: conditional route [BL-001' as weaker alternative to BL-001; shares the S^2-motivation obstacle but in a relaxed form]
```

---

### Skeptic 3 — Physicist Skeptic of the Kill: What If ExtCat is a Subcategory of a Unified Structure?

**Argument:**

"The analysis assumes `ExtCat` and `LorHist_BMS` are two separate categories connected by a functor
`F`. But what if the correct formulation is that there is ONE category — call it `UnivCat` — of
which both `ExtCat` and `LorHist_BMS` are subcategories or functorial images? In that case, BMS
acts on `UnivCat`, and the action restricts to both subcategories. The restriction to the `ExtCat`
subcategory would be a source-intrinsic BMS action without needing `F` to be invertible. Does this
reframing escape ICO'?"

**Analysis:**

**Step 1: What is `UnivCat`?**

For `UnivCat` to unify `ExtCat` and `LorHist_BMS`, it must be a category whose objects include
both source constraint states and Lorentzian boundary configurations, and whose morphisms include
both admissible extensions and Lorentzian histories. One candidate:

```text
UnivCat = the category of all pairs (C, boundary-data)
          morphisms: admissible extensions that are simultaneously consistent
                     with the constraint transition AND with Lorentzian dynamics
```

This is the "junction category" where source and target constraints are both imposed. But this
category is generically empty or very restricted: imposing both source constraint transitions and
Lorentzian dynamics simultaneously requires the source and target physics to be consistent.

**Step 2: Does BMS act on `UnivCat`?**

Yes, if `UnivCat` includes Lorentzian boundary data (conformal infinity), then BMS acts on the
Lorentzian half of the morphisms. The restriction to the `ExtCat` subcategory gives a BMS action
on `ExtCat` IF the `ExtCat` objects can be identified with specific boundary configurations.

**Step 3: Does this reframing escape ICO'?**

The unified category approach faces the following obstacle: the "source" subcategory of `UnivCat`
must be independently definable as `ExtCat` without reference to the Lorentzian half. If the
source constraints already include Lorentzian boundary data (which they must, to allow BMS to act
on them), then the "source/target distinction" is lost — `ExtCat` is not an independent source
category; it is a projection of `UnivCat` that already contains target data.

**Formal statement of the obstacle:**

Let `Pi_S: UnivCat -> ExtCat` and `Pi_T: UnivCat -> LorHist_BMS` be the projection functors.
For BMS to act on `ExtCat` via the unified category:

```text
T_f · e = Pi_S(T_f · Pi_S^{-1}(e) union Pi_T^{-1}(f-data))
```

This requires `Pi_S` to be invertible on morphisms — i.e., each `ExtCat` morphism must come from
a unique `UnivCat` morphism. If the source projection is many-to-one (which it typically is, since
many Lorentzian histories can project to the same source extension), then the pull-back is
ambiguous — the same problem as Attempt 3.1.

**Does the reframing open a new route?**

Yes, under a specific condition: if `UnivCat` is defined so that the source projection `Pi_S` is
an equivalence of categories (i.e., source constraints uniquely determine the Lorentzian history),
then BMS acts on `ExtCat = UnivCat`. But this condition says that source constraints determine
the Lorentzian physics, which is a very strong assumption. It is essentially the statement that the
Temporal Issuance program succeeds completely — source constraints fix all the physics.

If this condition is not imposed, the unified-category reframing does not escape ICO'. The BMS
action on `UnivCat` restricts to `ExtCat` ambiguously (same obstacle as Attempt 3.1).

**New content:** The unified-category reframing identifies the precise condition under which BMS
acts on `ExtCat` via an ambient category: the source-projection functor `Pi_S: UnivCat -> ExtCat`
must be an equivalence. This is a new precise condition, not previously stated in the ledger.

```yaml
skeptic_id: S-3
argument: >
  If there is a unified category UnivCat of which both ExtCat and LorHist_BMS are subcategories,
  then BMS (acting on LorHist_BMS) restricts to ExtCat as a BMS action. This bypasses the
  need for an invertible F and provides a BMS action on ExtCat via the ambient unified category.
analysis: >
  The reframing is formally coherent but introduces the same ambiguity as Attempt 3.1 unless
  the source-projection functor Pi_S: UnivCat -> ExtCat is an equivalence. If Pi_S is an
  equivalence, the source constraints uniquely determine the Lorentzian physics — a very strong
  assumption. Without equivalence, the restriction of the BMS action to the ExtCat subcategory
  is ambiguous (multiple Lorentzian histories can project to the same source extension). The
  reframing identifies a precise new condition (Pi_S is an equivalence) under which BMS acts on
  ExtCat. This is a new precise formulation, not a kill.
verdict: conditional route [Pi_S equivalence condition is a precise new sufficient condition for BMS action on ExtCat; not established but not obviously blocked]
```

---

### Skeptic 4 (Bonus) — Holographic Physicist: Does Celestial Holography Provide a Boundary BMS Action?

**Argument:**

"Celestial holography proposes that quantum gravity in flat spacetime is dual to a 2D CFT on the
celestial sphere `S^2`. In this duality, the `S^2` is the **boundary** of the Minkowski spacetime,
and the bulk lives in the interior. The BMS group is the asymptotic symmetry of the bulk, and it
acts on the boundary CFT as the global symmetry group. If `ExtCat` is defined as a category of
**boundary** data (data on `S^2`), and the bulk is the target, then BMS acts on the boundary
(source) without needing to be induced from the bulk (target). Does this escape ICO'?"

**Analysis:**

**Step 1: Celestial holography as a source/target split.**

In celestial holography, the duality is:

```text
Bulk: flat Minkowski spacetime (quantum gravity, BMS-invariant)
Boundary: celestial sphere S^2 with 2D CFT (BMS symmetry acts as CFT global symmetry)
Bulk observable -> Boundary operator via Mellin transform
```

The boundary `S^2` is not at spatial infinity; it is at null infinity `I^+ cup I^-`, coordinatized
by angles. The BMS group acts on the boundary as the conformal group (plus supertranslations).

**Step 2: Does this provide an independent source-side BMS action?**

YES, under the following identification:

```text
ExtCat objects: boundary states (boundary conditions on S^2, i.e., states in the celestial CFT)
ExtCat morphisms: boundary transitions (insertions of boundary operators, i.e., amplitude elements)
BMS action: the standard CFT symmetry action on the S^2 boundary data
```

This gives a BMS action on `ExtCat` that is:
- **Boundary-side** (source = boundary), not bulk-side (target = bulk)
- **Independent of bulk dynamics** at the kinematic level (BMS acts on the boundary CFT regardless
  of what the bulk dynamics are)
- **Not a pull-back from the bulk** in the holographic sense (the boundary theory is self-sufficient
  as a 2D CFT with its own symmetry structure)

**Step 3: Does this escape ICO'?**

- **ICO'-1:** Does the BMS action on boundary `ExtCat` import bulk dynamics? In the holographic
  setting, the boundary CFT is an independent theory. BMS acts on the boundary CFT via the standard
  Witt algebra / Virasoro action on `S^2`. This action does NOT require knowing the bulk Hamiltonian.
  **ICO'-1 does not apply.**

- **ICO'-2:** Is the boundary BMS action insufficient to determine `Q_f`? No: the BMS Noether
  charge `Q_f` in the boundary CFT is determined by the boundary stress tensor and the supertranslation
  parameter `f`. This is fully determined by boundary data. **ICO'-2 does not apply.**

- **ICO'-3:** Is this trivial re-encoding? The boundary CFT interpretation is NOT trivial bookkeeping:
  it is a genuine physical theory (the celestial holographic dual) with its own dynamics. The fact
  that BMS acts on the boundary is a structural fact, not a definition-by-reference to the bulk.
  **ICO'-3 does not apply — but there is a caveat** (see Step 4).

**Step 4: The independence question.**

The celestial holographic dual is **physically equivalent** to the bulk (holographic duality).
This means:

- Every bulk observable corresponds to a boundary observable.
- The boundary Q_f corresponds to the bulk Q_f.
- The boundary `ExtCat` is equivalent (as a physical theory) to the bulk `LorHist_BMS`.

If `ExtCat = LorHist_BMS-dual` and the duality is a physical equivalence (not just a mathematical
correspondence), then having BMS act on `ExtCat = boundary` is the same as having BMS act on
`LorHist_BMS = bulk`. The source/target distinction is preserved in the formalism but collapsed
in the physics.

**However:** the key question for Temporal Issuance is not whether the physics is equivalent, but
whether the **source** (constraint extension) structure determines the physics. If the celestial
boundary theory is a complete, self-contained theory with BMS symmetry, then the source-side
`ExtCat = boundary-CFT` is a legitimate independent characterization of the physics. The BMS
action on `ExtCat` (boundary) does not require specifying the bulk Hamiltonian.

**This is the sharpest surviving route: ExtCat = celestial boundary theory.**

```yaml
skeptic_id: S-4
argument: >
  In celestial holography, the celestial sphere S^2 (boundary) carries a self-contained 2D CFT
  with BMS symmetry, dual to the bulk flat spacetime. If ExtCat is defined as the category of
  boundary states and boundary transitions (celestial amplitudes as boundary-CFT operators),
  then BMS acts on ExtCat as the boundary CFT symmetry group. This action is independent of
  the bulk Hamiltonian at the kinematic level, and Q_f is the boundary Noether charge.
analysis: >
  This is the strongest surviving route. The celestial holographic identification ExtCat =
  celestial-boundary-CFT gives a BMS action on ExtCat that:
  (1) is not pulled back from the bulk (BMS acts on the boundary independently)
  (2) does not require the bulk Hamiltonian to be specified (Q_f is a boundary Noether charge)
  (3) satisfies BL-001 and BL-007 simultaneously, IF the holographic identification is accepted
  The caveat: the boundary CFT is physically equivalent to the bulk (holographic duality). So
  "source = boundary" is not independent of "target = bulk" in the physical sense -- they are
  dual descriptions of the same physics. However, the S^2-indexed source structure (boundary
  states) is formally independent of the choice of bulk completion, which is exactly the ICO
  escape that Category G needs. This route is genuinely live, not conditionally live -- it
  provides a concrete setting (celestial CFT) where BMS acts on S^2-indexed source data without
  importing bulk Hamiltonian dynamics.
verdict: live route [celestial holographic identification provides the S^2-indexed source structure needed by 3.2/3.4, with BMS acting on the boundary without bulk dynamics import]
```

---

### Phase 4 Result

```yaml
local_minimum_confirmed: no
reasoning: >
  Skeptic 4 opens a genuine live route that the construction attempts (3.1-3.4) did not identify:
  the celestial holographic identification ExtCat = celestial-boundary-CFT. Under this identification,
  BMS acts on ExtCat as the boundary CFT symmetry group, without requiring the bulk Hamiltonian
  (ICO'-1 does not apply), fully determining Q_f as a boundary Noether charge (ICO'-2 does not
  apply), and with genuine physical content rather than bookkeeping (ICO'-3 does not apply, with
  caveat). Skeptics 1-3 also identify conditional routes (symplectic quantization / w_{1+inf},
  profunctor BL-001', Pi_S equivalence condition) that are not obviously blocked.

  Category G is therefore NOT killed. The precise status is:

  - Attempts 3.1 and 3.3 are killed (pull-back and celestial relabeling)
  - Attempts 3.2 and 3.4 are conditionally live (require S^2-indexed source motivation)
  - Skeptic 4's celestial holography route PROVIDES the missing S^2 motivation
  - The remaining question is not "is Category G dead?" but "is the holographic identification
    (ExtCat = celestial boundary CFT) the right formulation of ExtCat?"

  This is a local minimum: there exists a route (celestial holography) that has not been analyzed
  in depth and that the anti-local-minimum gate reveals as live. The kill is not confirmed.
  Category G status: CONDITIONAL LIVE ROUTE (requires holographic formulation analysis).
```

---

## Phase 5: Preview of Next Run

### What Remains Live After RUN-0032

**Category G (BMS Soft Charges):** CONDITIONALLY LIVE

The celestial holography route (Skeptic 4) is the live version:

```text
ExtCat = category of celestial boundary CFT states and operator insertions
BMS acts on ExtCat as the boundary conformal symmetry group (Witt + supertranslations)
Q_f = boundary Noether charge (fully determined by boundary data, independent of bulk Hamiltonian)
BL-001 is satisfied: BMS acts on boundary ExtCat independently of bulk
BL-007 is satisfied: Q_f is the boundary Noether charge of this action
```

**Remaining questions for the holographic route:**

1. Is the celestial boundary CFT a valid identification of `ExtCat`? Specifically: does the
   category of boundary states and operator insertions satisfy the admissibility structure of
   `ExtCat` (typed constraints, admissibility rule)?
2. Is the BMS action on the boundary CFT "source-side" in the Temporal Issuance sense? Or does
   the holographic duality make it equivalent to a target-side action?
3. Does the holographic Q_f have a purely source-side definition, or does it require knowing the
   bulk to define the boundary Noether charge?

**Other surviving routes:**

| Category | Status |
| --- | --- |
| Category G (BMS) — holographic route | CONDITIONAL LIVE |
| Category G (BMS) — symplectic/w_{1+inf} (S-1) | CONDITIONAL LIVE |
| Category G (BMS) — profunctor BL-001' (S-2) | CONDITIONAL LIVE |
| Category G (BMS) — unified UnivCat Pi_S equiv (S-3) | CONDITIONAL LIVE |
| Category A (non-Poincare / LQG) | NOT YET TRIED |
| Category B (quantum path-integral, BL-009) | NOT YET TRIED |
| Category E (source-generated metric) | NOT YET TRIED |
| Category F (lax functors / oo-functors) | NOT YET TRIED |
| Category H (2-category / enriched Ext_S) | NOT YET TRIED |
| TI-C012 Holonomy (BL-004, TM-A) | CONDITIONAL LIVE (needs reversible extensions) |

### Recommended Next Run (Superseded By RUN-0033)

The recommendation below was the local recommendation at the end of this detailed Category G
appendix. It is superseded by RUN-0033, which recommends formal residue documentation unless Joe
explicitly requests a new source-generated dynamics program.

**W008 Category G — Holographic Sub-Route:**

Analyze the celestial holographic identification `ExtCat = celestial boundary CFT`. This is a
concrete, bounded question:

1. Define the celestial boundary CFT as a category (objects: boundary states; morphisms: operator
   insertions / amplitude elements).
2. Verify that this category satisfies the `ExtCat` admissibility structure.
3. Show that the BMS action on the boundary CFT is independent of the bulk Hamiltonian at the
   kinematic level.
4. Define `Q_f` as the boundary Noether charge and show it satisfies BL-007.
5. Apply the ICO' trichotomy to the boundary Q_f.

**Fallback (if holographic route is closed in the next run):**

Route to the symplectic/w_{1+inf} route (Skeptic 1) or the profunctor BL-001' route (Skeptic 2).
Both require formalizing the additional structure identified in Phase 4.

---

## Bridge Lemma Status (Updated)

| Bridge Lemma | Previous Status | Status After RUN-0032 | Next Action |
| --- | --- | --- | --- |
| BL-001 (BMS-covariant ExtCat) | UNKNOWN | CONDITIONAL: holographic route gives S^2 motivation | Formalize celestial-CFT identification |
| BL-002 (Q_f is morphism-level) | UNKNOWN | CONDITIONAL: follows if BL-001 holds | Depends on BL-001 |
| BL-003 (Q_f != p^mu) | SURVIVES | SURVIVES | No action |
| BL-004 (holonomy nontrivial) | WEAK | WEAK | Requires reversible extensions |
| BL-005 (pi_1 nontrivial) | WEAK | WEAK | Requires endomorphisms in ExtCat |
| BL-006 (TQFT functor) | SURVIVES (exist.) | SURVIVES (exist.) | Monoidal structure needed |
| BL-007 (soft charge source-side) | UNKNOWN CRITICAL | CONDITIONAL: follows from BL-001 via holography | Formalize holographic BL-001 |
| BL-008 (conformal target evades BDO) | WEAK | WEAK | Operator-state correspondence check |
| BL-009 (quantum path-integral) | UNKNOWN | UNKNOWN | Action and measure on ExtCat needed |
| BL-001' (BMS profunctor) | (new) | CONDITIONAL LIVE | Define profunctor from BMS-orbits to ExtCat |

---

## Files Changed

- `agent-runs/RUN-0035-w008-category-g-bms-formal-pass.md` (this file)
- `CLAIM-LEDGER.md` (TI-C013 updated: speculative -> formalizing, conditioned on holographic route)
- `memory/path-kills.md` (new entry: pull-back construction killed; celestial relabeling killed)
- `agent-governance/NEXT-TRIGGER-PLAN.md` (replaced with updated version)
- `agent-governance/STEWARD-METRICS.md` (RUN-0034 signal appended)
- `memory/steward-memory-log.md` (RUN-0034 entry appended)
- `ROADMAP.md` (RUN-0034 added to Phase 1E log)
