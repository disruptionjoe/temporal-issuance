---
artifact_type: run_record
run_id: RUN-0029
status: complete
governance_role: inverted_construction_momentum_selection
trigger: NEXT-TRIGGER-PLAN (set by RUN-0028 BDO pass)
workflow: W000-repo-steward-cycle
constitutional: false
claims_touched:
  - TI-C007
  - TI-C008
  - TI-C009
  - TI-C010
---

# RUN-0029: Inverted Construction — Momentum Selection via Ext_S

## Timestamp

2026-06-21 (chat-executed steward pass; committed via Claude Code automation)

## Trigger

`agent-governance/NEXT-TRIGGER-PLAN.md` current recommendation (set by RUN-0028 BDO pass):

> Construct or refute an `Ext_S` invariant that selects Lorentzian momentum data the boundary
> leaves open. Define `LorHist'` whose objects are momentum-underdetermining (partial or
> asymptotic boundary data only).

The inverted construction is the single remaining open door after BDO closed the
boundary-fixing energy-momentum route.

## Pre-Work Summary (loaded from prior runs)

RUN-0028 (BDO pass) proved: in `LorHist(M, eta, A)` with Poincare-invariant, Noether-regular
action, total `p^mu` of any on-shell morphism `h: B0 -> B1` is determined by boundary objects
`(B0, B1)` alone. For any parallel pair `e1, e2 : S => S'`, `p^mu(F(e1)) = p^mu(F(e2))`.
Nontriviality and energy-momentum-relevance are mutually exclusive in that control case.

The one surviving door: objects that do NOT encode full `p^mu`. If `F(S)` and `F(S')` only
carry partial or asymptotic data, `p^mu` is not fixed by the objects. An `Ext_S` invariant
might then select among the completions with distinct momentum.

---

## Subagent Section 1: Lorentzian Geometer

### Task

Define `LorHist'` with momentum-underdetermining objects; check covariance.

### Definition of LorHist'

Fix Minkowski spacetime `(M, eta)` and Poincare-invariant Noether-regular action `A`.

A **momentum-underdetermining boundary** is a specification of local data at a spacelike
(or null) surface that does not determine the total conserved four-momentum of any morphism
whose source or target it is.

Three candidate object types:

**Candidate O1: Partial Cauchy data.**
Objects are field configurations on a bounded spatial region `U ⊂ Sigma_t` (proper open
subset of a Cauchy surface). Morphisms are on-shell histories in the causal domain of
dependence `D(U)`. The total `p^mu` integrated over `Sigma_t` includes contributions from
the complement `U^c`, which is not encoded in the object. Therefore `p^mu` of a morphism
is NOT determined by the boundary objects alone.

Covariance check O1: A Cauchy surface is a spacelike hypersurface. Choosing a "bounded
spatial region" requires cutting `Sigma_t` with a surface — in flat space this is a
codimension-2 sphere. The choice of `Sigma_t` itself requires picking a time coordinate or
a foliation. This sneaks in a **preferred foliation**. Covariance status: **FAIL**. O1
violates the covariance guardrail.

**Candidate O2: Asymptotic/conformal boundary data.**
Objects are data on conformal infinity `I^-` (past null infinity) or `I^+` (future null
infinity) restricted to a compact angular sector or a retarded-time window. Morphisms are
on-shell histories with prescribed retarded or advanced data in that window. The total
Bondi four-momentum includes superradiance contributions from other angular sectors not
encoded in the object. Hence `p^mu` is underdetermined by the object.

Covariance check O2: Conformal infinity `I^pm` is a well-defined covariant concept in
asymptotically flat spacetimes — it is defined by the conformal compactification
`(tilde{M}, tilde{g})` without any preferred foliation. Restricting to a compact angular
sector is done via an `S^2` decomposition at `I`, which is covariant under BMS transformations
(angle-preserving diffeomorphisms of `I`). A retarded-time window is a retarded-time interval
`[u_0, u_1]` on `I^+`, covariant under supertranslation-free Lorentz transformations.
Covariance status: **CONDITIONAL PASS** with caveats:
- The angular sector decomposition is BMS-covariant, not fully Poincare-covariant at finite
  radius (it is well-defined at null infinity, where the Poincare subgroup of BMS acts).
- Supertranslation freedom can shift `u_0, u_1` globally; a window defined by absolute
  retarded-time values is only invariant up to supertranslation.
Resolution: define objects as data on all of `I^-` or `I^+` (no sector restriction),
but with free asymptotic data in a gauge-trivial sector (e.g., nonradiative early data,
radiative middle data). This is fully covariant. **Total Bondi four-momentum at `I^-` is
determined by early-time data, but total Bondi four-momentum at `I^+` is shifted by the
flux carried by radiation during the collision/interaction.** If the object specifies only
`I^-`-data (in-state) and not the full `I^+`-data (out-state), then the total outgoing
`p^mu` at `I^+` is underdetermined.

**Candidate O3: Near-region data only (compact support).**
Objects are field configurations with compact support in a spacetime ball `B(x, r)`. Morphisms
are histories that interpolate between compact-support configurations. Total `p^mu` is not
computable from compact-support data alone (it requires Noether integrals at infinity or over
Cauchy slices extending to infinity). So `p^mu` is genuinely underdetermined.

Covariance check O3: Compact balls `B(x, r)` in Minkowski space are Lorentz-invariant
(defining them requires the metric, not a foliation). **Covariance status: PASS.** However,
morphisms between compact-support states have a subtlety: in relativistic field theory, the
domain of dependence of a compact region is a double cone — not a full-space slab — so
the morphism category is that of **local on-shell histories in a compact causal diamond**.
This is a legitimate, covariant construction. `p^mu` for such a history is not total
four-momentum (which requires integrating over all of space) but local field momentum in
the diamond, which is boundary-ambiguous (requires a local stress-tensor but no preferred
integral surface).

### Selected object definition for LorHist'

**Use O2 (full `I^-`/`I^+` asymptotic data, incomplete specification) as the primary
candidate, with O3 as a cross-check.**

**Formal definition:**

```
LorHist'(M, eta, A) objects:
  An object B is a pair (psi_in, sigma_in) where:
    psi_in = asymptotic field amplitude on I^- (in-state specification)
    sigma_in = in-state charge/helicity quantum numbers
  Crucially: psi_in does NOT specify psi_out or the outgoing momentum p^mu_out.
  The total outgoing four-momentum at I^+ depends on radiative content during the interaction.

LorHist'(M, eta, A) morphisms:
  A morphism h: B0 -> B1 is an on-shell history that maps
  in-state B0 = (psi_in^0, sigma_in^0) to out-state B1 = (psi_out^1, sigma_out^1).
  But objects only SPECIFY the in-state, not the out-state.
  A morphism h picks a particular out-state compatible with the in-state under the
  equations of motion, including a particular value of p^mu_out.
  Two morphisms h1, h2: B0 -> B1 correspond to two different on-shell scattering processes
  with the same in-state B0 but reaching the same asymptotic charge quantum numbers in B1,
  while differing in p^mu_out (they differ in the angular distribution and polarization of
  outgoing radiation, hence in the total outgoing four-momentum decomposition).
```

**Momentum-underdetermination check:**
Does fixing B0 (in-state) and B1 (out-state charge data) leave `p^mu` open?

- If B1 specifies the full out-state including amplitude `psi_out^1` at `I^+`, then
  total outgoing four-momentum is determined by the Bondi mass-loss formula from the
  outgoing radiation. `p^mu` is NOT left open.
- If B1 specifies only quantum numbers (charge, helicity) but NOT the full amplitude
  `psi_out^1`, then different morphisms h1, h2 reaching B1 can carry different amounts
  of outgoing radiation with different total `p^mu`. `p^mu` IS left open.

**Verdict from Lorentzian geometer:** `LorHist'` with objects specifying only charge/quantum
numbers at `I^pm` (not full field amplitudes) is the correct momentum-underdetermining
category. Objects are covariant (charge quantum numbers and helicities transform covariantly
under the Poincare group). Morphisms are on-shell histories; multiple distinct morphisms
h1, h2 with the same domain and codomain objects can carry different `p^mu_out`.

This is the first live candidate. It passes covariance at the object level.

---

## Subagent Section 2: Category Error Auditor

### Task

Check whether the selection invariant is hidden-variable bookkeeping.

### Setup

Suppose an `Ext_S` morphism invariant `I(e)` for `e: S -> S'` is claimed to select `p^mu`
from the set of compatible completions. The hidden-variable check asks:

> Is `I(e)` genuinely source-side content, or does it merely label which completion is chosen
> after the fact?

### Three failure modes for `I(e)`

**Failure mode A (trivial label):** `I(e)` is defined as "the value of `p^mu` in the realized
completion." Then the invariant is exactly what we want to determine — it is not a
source-side handle, it is a tautological re-encoding of the output. **Kill condition: trivial.**

**Failure mode B (completion-indexed label):** `I(e)` is defined as "a name for which
completion is realized." Then `I(e)` carries no information beyond a pointer to the chosen
history. It is bookkeeping for the external choice of completion; not source-side content.
**Kill condition: absorbed by choice-of-history selector.**

**Failure mode C (external-parameter label):** `I(e)` is defined by a parameter drawn from
outside the source category (e.g., an interaction coupling constant, a background field, a
gauge parameter). Then `I(e)` is not a morphism invariant of `ExtCat` — it is a label
imported from the physics of the target and wrapped in source-side notation. **Kill condition:
absorbed by target-physics import.**

### What would a non-bookkeeping invariant look like?

A genuine source-side `Ext_S` invariant must:

(a) Be defined from the source-category morphism `e: S -> S'` without reference to any
    particular completion or any parameter from the Lorentzian target.
(b) Be preserved under quotient by gauge equivalence and reparametrization.
(c) Distinguish parallel morphisms `e1 != e2: S => S'` in `ExtCat` with the same induced
    order, based on their source-side structure.
(d) Map, via the functor `F: ExtCat -> LorHist'`, to a parameter that selects among the
    `p^mu`-distinct completions.

The critical burden: (d) requires that the source-side invariant `I(e)` is **correlated**
with a completion selector, and that this correlation is part of the **functor definition**
of `F` — not introduced by hand after the fact.

### Verdict from Category Error Auditor

A non-bookkeeping `Ext_S` invariant for `LorHist'` must satisfy conditions (a)-(d). The
question is whether any such invariant can exist without smuggling in a choice-of-completion
parameter through the back door.

**Key tension:** In `LorHist'` with momentum-underdetermining objects, multiple morphisms
h1, h2: B0 -> B1 with the same boundary objects and different `p^mu_out` represent physically
distinct on-shell histories. A functor `F: ExtCat -> LorHist'` maps each source morphism `e`
to exactly one morphism `F(e)`. If `F(e1)` and `F(e2)` differ in `p^mu_out`, then `F` already
picks one history per source morphism — and the `Ext_S` invariant `I(e)` is exactly what
encodes that pick.

**But this is not automatically bookkeeping.** It is bookkeeping only if `I(e)` is *defined
as* the momentum data of the chosen completion, rather than being defined *independently* and
then *determined to fix* the completion. Compare:

- **Bookkeeping:** Define `I(e) := p^mu(F(e))`. Then `I` is a derived quantity, not a source
  primitive. Kill.
- **Genuine:** Define `I(e)` from source-category data (e.g., the combinatorial structure of
  the extension `e`, its type, its constituent constraints) independently; then prove that
  `F` maps `I(e)` to a parameter that selects `p^mu`. This is a legitimate non-trivial result
  if the proof goes through.

The Category Error Auditor verdict: the construction is **not automatically killed** by the
hidden-variable criterion, but it requires demonstrating condition (a) — a source-side
definition of `I(e)` — before condition (d) can be claimed.

**The critical question for the next section:** Can any source-category morphism invariant
be independently defined and then demonstrated to select `p^mu` via `F`?

---

## Subagent Section 3: Constructor / Hidden-Variable Skeptic

### Task

Aggressively try to show any proposed invariant is just a label.

### Aggressive attack on candidate invariants

Let me enumerate the most natural candidates for `I(e)` and attack each.

**Candidate I1: Source extension "mass" or "energy" parameter.**
One might try: "Let `I(e)` be an energy-like parameter intrinsic to the extension `e: S -> S'`,
defined from source constraints." This is the most direct attempt.

Attack: What does "energy-like parameter intrinsic to a source extension" mean in `ExtCat`
without reference to a Lorentzian target? In `ExtCat`, morphisms are admissible source
extensions. Unless `ExtCat` has been given an energy-like function on its morphisms
(independent of any Lorentzian realization), such a parameter does not exist in the source
category. To add it is to add it by hand — which is failure mode C above. **Kill: imported.**

**Candidate I2: Source category weight `Q(e)` (from RUN-0028).**
RUN-0028 (automated) introduced `Q: Mor(ExtCat) -> ([0, infinity), +)` and showed a toy
functor maps `Q(e)` to proper time. Now ask: does `Q(e)` select `p^mu` data left open by
`LorHist'` objects?

Attack: `Q(e)` is a real-valued additive weight on morphisms. Proper time `tau` for a
timelike worldline is also a real-valued quantity. The functor of RUN-0028 mapped `Q` to
`tau`. Now the question is whether `tau` or any other proper-time-derived quantity selects
`p^mu_out` in the LorHist' asymptotic category.

**Does proper time determine outgoing momentum in asymptotically flat scattering?**
In a scattering process, the outgoing Bondi four-momentum `p^mu_out` depends on the
radiation field at `I^+`, which depends on the coupling strength, the angular distribution
of emission, and the interaction details — none of which are encoded in the proper time of
the source worldline alone. Proper time determines the worldline's arc length; it does not
determine what the source radiated.

More formally: two scattering events can have identical source proper times (same `Q(e)`)
but different radiated energy distributions, giving different `p^mu_out`. **Therefore Q(e) =
proper time does NOT select p^mu among completions. Kill as underdetermining.**

**Candidate I3: Combinatorial type of the extension.**
Let `I(e)` be the "type" of the admissible extension `e` in a typed source category (e.g.,
constraint class, constraint complexity, constraint multiplicity). This is genuinely
source-side.

Attack: The type of an extension determines the constraint structure, not the dynamics of
the Lorentzian realization. Two extensions of the same type can map to Lorentzian histories
with different `p^mu_out` depending on coupling constants, initial conditions, and
interaction geometry — all of which are in the Lorentzian target, not the source type.
**Therefore extension type does NOT select p^mu. Kill as underdetermining.**

**Candidate I4: Internal symmetry charge of the extension.**
Suppose extensions carry an internal symmetry charge `q(e)` (U(1) charge, SU(2) isospin,
etc.) that is covariant and source-defined. Map `q(e)` via `F` to a charge quantum number
that fixes outgoing charge quantum numbers.

Attack: Internal charge quantum numbers are part of `LorHist'` objects (the `sigma_out`
data). If fixing internal charge quantum numbers uniquely fixed `p^mu_out`, then `p^mu_out`
would be object-level — but that contradicts the premise that objects are
momentum-underdetermining. Therefore fixing internal charge does NOT fix `p^mu_out`.
**Kill: charge and momentum are independent in asymptotically flat scattering.**

**Candidate I5: Ext_S "interaction amplitude" invariant.**
Suppose `I(e)` encodes the amplitude of the source extension — analogous to a quantum
mechanical transition amplitude or path-integral weight.

Attack: A transition amplitude is not a morphism invariant in the category-theoretic sense —
it depends on the chosen path-integral measure, which requires the action `A` and the
metric. This is imported from the Lorentzian target. Specifically: the path-integral measure
over on-shell histories ending in `LorHist'` boundary data is exactly what determines the
distribution over `p^mu_out` completions. If `I(e)` is defined to equal this amplitude, it
is failure mode C (target-physics import). **Kill: absorbed.**

**Candidate I6: Scattering matrix selection.**
One might argue: "Let `I(e)` encode which element of the S-matrix is being selected."
Attack: The S-matrix maps in-state quantum numbers to out-state quantum numbers (including
`p^mu`) using the full dynamics of the theory. Encoding an S-matrix element in `I(e)` is
equivalent to encoding all the physics of the Lorentzian target in the source invariant.
This is the maximally severe form of failure mode C. **Kill: absorbed by full target physics.**

### Skeptic Verdict

No natural candidate for a source-side `I(e)` survives attack. Every candidate either:
- Has no source-side definition (requires importing energy, amplitude, or S-matrix from target)
- Is independently defined but does not determine `p^mu` among completions
- Reduces to bookkeeping (directly encodes the completion choice)

The skeptic does not claim a proof of impossibility. The argument is:

> Every reasonable candidate for a non-bookkeeping source-side invariant is either not
> independently source-defined, or independently source-defined but insufficient to select
> p^mu. The space of "reasonable candidates" covers the main structural possibilities.
> An exotic candidate would need to be proposed before it can be evaluated.

---

## Subagent Section 4: Relativity Physicist

### Task

Stress-test the covariance of partial/asymptotic boundary data.

### Covariance stress test for LorHist' objects

The candidate LorHist' object definition (from the Lorentzian geometer's section) uses:

```
B = (psi_in, sigma_in) at I^- (in-state asymptotic data, charge quantum numbers)
```

**Stress test 1: Lorentz transformation.**
Under a Lorentz boost `Lambda`, the asymptotic field amplitude `psi_in` transforms as a
representation of the Lorentz group. The transformation is:

```
psi_in -> D(Lambda) psi_in (circ Lambda^{-1})
```

where `D(Lambda)` is the appropriate representation (spin-0, spin-1, spin-1/2, etc.).
This is a standard, well-defined transformation. The charge quantum numbers `sigma_in`
transform under the same representation. The morphisms (on-shell histories) transform as
fields under Lorentz, and the functor `F: ExtCat -> LorHist'` must map source transformations
to Lorentz transformations on the target side.

**Covariance: PASS under Lorentz.** The objects and morphisms are covariant.

**Stress test 2: Translation invariance.**
Translations shift the retarded time coordinate on `I^-`. An in-state specification at
`I^-` is defined via the retarded limit of the field as `r -> infinity` at fixed `u = t - r`.
A spacetime translation shifts `u -> u - n*a` (where `n` is the null direction and `a` is
the translation 4-vector). The asymptotic field transforms accordingly.

**Covariance: PASS under translation.** But note: the total Bondi four-momentum at `I^-`
IS determined by the incoming field configuration. If B encodes the full in-state amplitude
`psi_in` on all of `I^-`, then `p^mu_in` is determined. Only `p^mu_out` at `I^+` is left
open by an in-state specification alone.

**Stress test 3: BMS invariance.**
The asymptotic symmetry group of asymptotically flat spacetimes is the BMS group
(Bondi-Metzner-Sachs), which is larger than the Poincare group: it includes supertranslations.
Supertranslations are angle-dependent translations `u -> u + f(theta, phi)`. They act on
the asymptotic field by:

```
psi_in -> psi_in + f(theta, phi) * (d/du) psi_in  (at leading order in 1/r)
```

**Critical issue:** The splitting of a scattering process into "incoming Bondi four-momentum"
and "outgoing Bondi four-momentum" depends on a supertranslation frame choice. Two
supertranslation-related in-states have the same total Bondi energy-momentum but different
angular Bondi-news decompositions. The Bondi mass formula relates the supertranslation-transformed
data to supertranslation-transformed memory effects.

**Does supertranslation break the covariance of LorHist' objects?**

If LorHist' objects are defined as full `I^-` amplitudes, they transform covariantly under
BMS including supertranslations. The Bondi four-momentum at `I^-` is supertranslation-invariant
(it is the zero-mode). The splitting between `p^mu_in` and `p^mu_out` is also supertranslation-
invariant in the sense that total Bondi four-momentum is conserved: `p^mu_in = p^mu_out` for
any complete scattering history (by conservation). **No supertranslation covariance problem.**

**Stress test 4: The covariance of partial vs. full specification.**
The key premise is that LorHist' objects under-determine `p^mu_out`. Let us check:

- If B = full `psi_in` on `I^-`: Total incoming Bondi four-momentum `p^mu_in` is determined.
  By conservation, `p^mu_out = p^mu_in` for the TOTAL momentum. But individual outgoing
  particle momenta are not determined by the in-state alone (the scattering angle is
  underdetermined by global conservation). So even with full `psi_in`, the **distribution
  of momenta among outgoing particles** is left open.
- If B = charge quantum numbers only (not amplitudes): Less is fixed. Both total and
  differential outgoing momenta are underdetermined.

**Verdict from relativity physicist:**

LorHist' objects defined as full `I^-` asymptotic amplitudes are covariantly defined and
leave individual outgoing-particle momenta underdetermined even though total `p^mu_out` is
fixed by conservation. This is a weaker form of underdetermination than initially hoped.

**The sharper conclusion:** If we require `Ext_S` to select the **total outgoing** `p^mu_out`,
conservation immediately gives `p^mu_out = p^mu_in`, and `p^mu_in` is determined by the
full in-state object. So total `p^mu` is NOT underdetermined by a full in-state LorHist'
object. **Conservation is BDO's cousin: it closes total momentum.** To leave total `p^mu_out`
genuinely open, objects must under-specify the in-state too — but then they also leave
`p^mu_in` open, and we have left the Poincare-invariant control case entirely.

**The partial specification escape:** Objects that specify only partial in-state data (not
full amplitudes) leave total `p^mu_in` open. Then `p^mu_out` is also open. But now the
BDO argument returns in a different form: if `p^mu_in` is not object-level, then the
source-category functor `F` must carry `p^mu_in` in the morphisms. This means `p^mu_in`
is a morphism-level invariant of LorHist' — and the `Ext_S` invariant must determine it.

This is the central stress-test finding:

> **Momentum-underdetermination in LorHist' objects shifts the momentum data from
> object-level to morphism-level, but does not eliminate it. The Ext_S invariant now
> has to carry the morphism-level momentum — which is exactly where BDO originally
> showed Ext_S invariants cannot reach it.**

The covariance analysis reveals a structural closure: relaxing the object definition
pushes the momentum data into the morphism, where BDO's logic applies in modified form.

---

## Subagent Section 5: NULL-SURVIVOR Advocate

### Task

Argue the inverted construction also collapses; require explicit refutation.

### Argument for NULL-SURVIVOR

The NULL-SURVIVOR hypothesis is: the physical interpretation of Temporal Issuance — that
source-side admissible extensions connect to mass-energy — should be archived. The inverted
construction is the last test before that archiving.

Let me construct the strongest argument that the inverted construction also collapses.

**Argument A: The BDO is a covariance theorem, not a coordination artifact.**

BDO stated: in any Poincare-invariant Lorentzian target, `p^mu` is conserved; a morphism's
`p^mu` equals the boundary object's `p^mu`. This used objects with full boundary data.

In LorHist' with momentum-underdetermining objects, objects no longer carry `p^mu`. But the
underlying physical reason for BDO has not changed: **Noether's theorem applies to any
on-shell history in a Poincare-invariant target, regardless of how objects are defined.**
Translation symmetry still yields conserved `p^mu`; the morphism still carries a definite
`p^mu`. The only change is that this `p^mu` is no longer readable from the object.

Consequence: every morphism `h: B0 -> B1` in LorHist' still has a definite `p^mu(h)`.
Different morphisms with the same endpoints can have different `p^mu`. **A functor
`F: ExtCat -> LorHist'` that maps parallel `e1, e2: S => S'` to histories with different
`p^mu` IS the goal — and this is exactly what the inverted construction proposes.**

But can `F` do this? The functor must be consistent: it must assign each source morphism
exactly one target morphism (up to the chosen composition/identity structure). The question
is whether the assignment can be non-constant on `p^mu` across the parallel pair.

**There is no categorical reason why not.** A functor can certainly map different morphisms
to different morphisms. The real question is whether the FUNCTORIALITY constraints kill this.

**Argument B: Functoriality collapse.**

For `F` to be a functor: `F(e2 circ e1) = F(e2) circ F(e1)` and `F(id_S) = id_{F(S)}`.

Now consider the composition constraint. Suppose `e1, e2: S => S'` are parallel with
`p^mu(F(e1)) != p^mu(F(e2))`. Consider morphisms `e3: S' -> S''`. Then:

```
F(e3 circ e1): F(S) -> F(S'')  with p^mu(F(e3 circ e1)) = p^mu(F(e3)) + p^mu(F(e1))
F(e3 circ e2): F(S) -> F(S'')  with p^mu(F(e3 circ e2)) = p^mu(F(e3)) + p^mu(F(e2))
```

(The addition law for four-momentum is valid in the additive/stacking sense for sequential
histories in a globally Poincare-invariant flat spacetime.)

For functoriality, we need `F(e3 circ e1) = F(e3) circ F(e1)` and
`F(e3 circ e2) = F(e3) circ F(e2)`. These are different target morphisms (since they land
with different total `p^mu`). This is fine — the functor maps them differently.

**Functoriality is NOT automatically broken by carrying `p^mu` distinctions.** The composition
law is respected as long as `p^mu` is additive along compositions, which it is. NULL-SURVIVOR's
functoriality attack fails.

**Argument C: The source-side definition problem.**

The strongest NULL-SURVIVOR argument is not about functoriality — it is about the source-side.
Even if a functor from `ExtCat` to `LorHist'` can map parallel pairs to `p^mu`-distinct
histories, the functor must be defined by something. That something is the `Ext_S` invariant
`I(e)`. And as the Constructor/Skeptic showed: every natural candidate for `I(e)` is either
not independently source-defined, or independently source-defined but insufficient to select
`p^mu`.

This is the genuine obstruction. It is not about covariance (LorHist' passes covariance).
It is not about functoriality (addition law allows it). It is about:

> **There is no source-side content that can determine which Lorentzian momentum completion
> is realized, because the set of completions is parametrized by target-side physics
> (coupling constants, angular distributions, interaction geometry), not by source-side
> extension rules.**

NULL-SURVIVOR's argument: the completions of a momentum-underdetermining boundary are
indexed by **dynamical data of the Lorentzian theory** (interaction Hamiltonian, coupling
constants, detailed field configuration at all scales). None of this data is available in the
source category `ExtCat`, which only knows about admissible extension rules. A source-side
invariant that selects among these completions must encode at least some of this dynamical
data — but then it is not source-side, it is target-side physics re-encoded in source notation.

**NULL-SURVIVOR verdict:** The inverted construction does not produce a genuine source-to-
momentum bridge. It either requires importing target-side dynamical data into the source
invariant (absorbed by failure mode C), or it relies on a source-side invariant that is
insufficient to discriminate completions. The physical interpretation should be archived.

**Requirement for refutation:** NULL-SURVIVOR's argument can be refuted only by producing
an explicit `I(e)` that is:
1. Definable from source-category data alone.
2. Demonstrably correlated with a parameter that selects among `p^mu`-distinct completions.
3. Not reducible to a relabeling of the completion choice.

The Constructor/Skeptic showed this is very hard. The next section (Mathematical Minimalist)
will evaluate whether the demand itself is unreasonable.

---

## Subagent Section 6: Mathematical Minimalist

### Task

Demand the minimal structure; reject anything not earning its slot.

### Minimal structural analysis

**What is the minimal claim being made?**

The inverted construction claims: there exists `F: ExtCat -> LorHist'` with objects
that are momentum-underdetermining, and an `Ext_S` invariant `I(e)` such that
`p^mu(F(e1)) != p^mu(F(e2))` for some parallel pair `e1, e2: S => S'` with `I(e1) != I(e2)`.

This is a weaker claim than: `I(e)` uniquely determines `p^mu(F(e))`. The weaker claim
only requires correlation, not determination.

**Is even this weak claim satisfiable?**

Here is the minimalist's observation: any functor `F: ExtCat -> LorHist'` whatsoever maps
parallel pairs to (possibly) different morphisms. If LorHist' has morphisms with different
`p^mu`, then almost any non-constant functor will map some parallel pair to morphisms with
different `p^mu`. **The question is not whether such a functor exists — it trivially does —
but whether the functor encodes genuine source-side information.**

The minimalist strips away everything that is not earning its slot:

**Strip 1:** The source category `ExtCat` with morphisms `e1, e2: S => S'`. These exist
by definition of any parallel pair in any non-trivial category.

**Strip 2:** A functor `F: ExtCat -> LorHist'`. By axiom of choice, for any category and
any target category with morphisms, one can define a function from morphisms to morphisms.
The question is whether `F` is a FUNCTOR (preserves composition and identity) and whether
it encodes source information.

**Strip 3:** The invariant `I(e)`. If `I(e)` is defined as `p^mu(F(e))`, then it is
trivially not source-side. If `I(e)` is defined independently, it must have a source-side
definition.

**The minimalist's constraint:** For the construction to earn its slot, `F` must be defined
by source-side data, not just exist. An arbitrary function from morphisms to Lorentzian
histories is not a bridge — it is a labeling scheme.

**Minimal honest statement:**

The inverted construction, stripped to its logical core, is:

> Given a category `ExtCat` with source morphisms and a category `LorHist'` with
> momentum-varying morphisms, any functor `F: ExtCat -> LorHist'` that is not constant
> on parallel pairs will map some parallel pair to morphisms with different `p^mu`.

This is true. It is also vacuously true: it does not require any specific relationship
between source-side structure and target-side momentum. It is the statement that a
non-constant functor has non-constant image — which is definitionally trivial.

**What would give the construction content?**

Content requires a mechanism: a proof that some specific source-category structure
(the `Ext_S` rule, the constraint type, the extension composition law) is the reason
`F(e1)` and `F(e2)` have different `p^mu`. Without a mechanism, the construction only
demonstrates that one can define a map from source morphisms to Lorentzian morphisms
with varying momentum — which does not make the source category relevant to momentum.

**Mathematical Minimalist Verdict:**

The inverted construction, as stated, does not earn its slot unless accompanied by a
mechanism. The mechanism must show that removing the `Ext_S` distinction between `e1` and
`e2` collapses `p^mu(F(e1)) = p^mu(F(e2))`. Without that, the `Ext_S` distinction is
irrelevant to the momentum difference; the momentum difference comes from the target-side
free parameters, not the source.

**This is the precise form of the obstruction.**

---

## Synthesis: The Inverted Construction Obstruction (ICO)

### Precise statement

**Theorem (Inverted Construction Obstruction, ICO).** Let `ExtCat` be a category of source
extensions and `LorHist'(M, eta, A)` a Lorentzian history category with
momentum-underdetermining objects (objects do not encode total `p^mu` of morphisms).

For a functor `F: ExtCat -> LorHist'` to deliver the mass-energy bridge — i.e., for
`p^mu(F(e))` to be determined by the `Ext_S` invariant `I(e)` of the source morphism `e` —
one of the following must hold:

**(ICO-1) Target-physics import:** `I(e)` is defined using dynamical data of `LorHist'`
(coupling constants, interaction Hamiltonian, scattering amplitudes, or equivalent). Then
`I(e)` is absorbed into the Lorentzian theory's description of itself, and the source
category adds no information. This is failure mode C.

**(ICO-2) Underdetermination:** `I(e)` is independently defined from source-category data
and carries no information about which `p^mu` completion is realized. Then `F(e)` may be
a non-constant functor, but `p^mu(F(e))` varies by target-side free parameter, not by
source-side `I(e)`. The `Ext_S` distinction is irrelevant to the momentum difference.
This is the Mathematical Minimalist's slot-failure condition.

**(ICO-3) Hidden-variable bookkeeping:** `I(e)` is defined as the `p^mu` data of the chosen
completion. Then `I` is trivial (the source distinction IS the output), and `F` is only
a labeling of which completion is chosen — absorbed by failure mode A or B.

**Verdict: no fourth option has been identified. ICO forecloses the inverted construction
in the Poincare-invariant Lorentzian control case under the given guardrails.**

### Why ICO is not just BDO re-stated

BDO showed: with momentum-determining objects, `p^mu` is object-level, so no morphism
distinction can move it. ICO shows: with momentum-underdetermining objects, `p^mu` is
morphism-level, but the morphism-level variation is parametrized by target-side physics,
not by source-side extension rules. The two obstructions seal from different directions:

- BDO seals from the top: objects over-determine `p^mu`, making it blind to morphisms.
- ICO seals from the bottom: objects under-determine `p^mu`, but the morphism-level variation
  is target-physics-indexed, not source-indexed.

Together, BDO and ICO seal the Poincare-invariant Lorentzian energy-momentum route
on both sides.

### Covariance verdict (final)

`LorHist'` with momentum-underdetermining objects is covariantly definable (confirmed by
the Relativity Physicist). The covariance guardrail does not kill the construction. What
kills it is the **content** question (ICO), not covariance.

### Hidden-variable verdict (final)

Any `Ext_S` invariant that succeeds in determining `p^mu` among completions must encode
target-side dynamical data (ICO-1), be insufficient to determine `p^mu` (ICO-2), or be
trivially absorbed (ICO-3). The hidden-variable check is not bypassed — it is confirmed
as the binding constraint.

### Functoriality and order verdict

Functoriality is NOT broken by the inverted construction (the NULL-SURVIVOR advocate
confirmed this). A non-constant functor `F: ExtCat -> LorHist'` mapping parallel pairs to
`p^mu`-distinct morphisms is formally consistent. The order preservation is unchanged from
BDO: `p^mu . F` does NOT factor through `Preord(<=_S)` in LorHist' (since `p^mu` is
morphism-level, not object-level). **This is the one formal advance over BDO:** the
inverted F does NOT trivially factor through order.

But this formal advance does not rescue the physical bridge, because the non-constant
nature of `p^mu . F` is not driven by `Ext_S` content (ICO-2). The functor is formally
non-constant at `p^mu` but source-decoupled at the mechanism level.

### Does inverted F beat NULL-SURVIVOR at the energy-momentum rung?

**No.** ICO shows that a formally non-constant `p^mu . F` does not require or demonstrate
source-side content. Any `F: ExtCat -> LorHist'` mapping to a LorHist' target with
momentum-varying morphisms will be non-constant at `p^mu` — this is vacuously true. The
claim that `Ext_S` invariants are the reason for `p^mu` variation requires ICO-defeating
evidence, which has not been found.

**NULL-SURVIVOR wins at the energy-momentum rung.**

---

## Disposition Ruling

The inverted construction passes the covariance guardrail (LorHist' objects are covariantly
definable). The inverted construction does NOT pass the hidden-variable / mechanism guardrail.
ICO forecloses it precisely and without residue.

**This is a clean obstruction. Per the NEXT-TRIGGER-PLAN disposition rule:**

> Treat a clean obstruction as success. If the inverted construction collapses, archive the
> physical interpretation to NULL-SURVIVOR and keep only the history-class formal residue.

**Ruling: Archive the physical interpretation of Temporal Issuance (TI -> mass-energy
bridge) to NULL-SURVIVOR. Keep the formal history-class residue.**

---

## Formal Residue (what survives)

After both BDO and ICO, the surviving formal structure is:

1. **History-class nontriviality of F (confirmed by BDO, not reversed by ICO):** A functor
   `F: ExtCat -> LorHist(M, eta, A)` can be nontrivial at the admissible-history-class
   level (different `Ext_S` morphisms map to distinct on-shell sectors sharing boundary data).
   This is absorbed by gauge/topological-sector bookkeeping but is a coherent formal structure.

2. **Preorder-from-extension (RUN-0025):** The induced preorder `<=_S` is a coarser shadow
   of the extension category. Morphism-level invariants exist beyond preorder.

3. **Conditional E008 theorem (formally valid, physically vacuous):** The conditional
   Lorentzian realization theorem is sound: IF a nontrivial-at-mass-energy F exists, THEN
   standard `E = mc^2` follows. BDO + ICO show the antecedent is unsatisfiable in the
   Poincare-invariant Lorentzian control case. The theorem is vacuously satisfied.

4. **ExtCat as a formal category with non-order invariants:** The source category can be
   specified with morphism-level invariants `I(e)` that are not recoverable from the induced
   preorder. This is a coherent formal structure regardless of physical interpretation.

These residues are publishable formal results. They do not support the mass-energy bridge.

---

## Claim-Ledger Update Proposals

### TI-C007: `Ext_S` can be the load-bearing admissible source-extension component

**Current status:** formalizing  
**Proposed update:** weakened  
**New strongest version:** `Ext_S` can be load-bearing at the admissible-history-class level
(parallel extensions map to distinct on-shell sectors) and at the formal extension-category
level (morphism-level invariants beyond preorder). Both BDO and ICO close the energy-momentum
route. The source-side content of `Ext_S` does not reach physical energy-momentum in the
Poincare-invariant Lorentzian control case.  
**New strongest objection:** The history-class distinction is absorbed by gauge/topological-sector
bookkeeping. The formal residue does not demonstrate physical relevance of `Ext_S`.  
**New next action:** None for the energy-momentum route. If pursued further, restrict to
formal category theory results without physical mass-energy claims.

### TI-C008: Admissible extension can induce temporal order while carrying invariant structure not recoverable from that order

**Current status:** formalizing  
**Proposed update:** formalizing (no change in status; the formal claim is intact)  
**Clarification:** The formal claim of TI-C008 is confirmed: morphism-level invariants can
exceed order. ICO does not damage this formal claim. What ICO adds: even with this formal
non-order content, the content does not reach energy-momentum.  
**New next action:** Document as a formal result in E008 and the residue catalog. No
physical bridge implication.

### TI-C009: Temporal Issuance may connect to GU and mass-energy through admissible extension, stabilized invariants, conserved quantities, and energy-momentum

**Current status:** weakened (energy-momentum route path-killed by BDO)  
**Proposed update:** archived (physical interpretation to NULL-SURVIVOR)  
**Reason:** BDO killed the boundary-fixing route; ICO kills the inverted construction route.
Both routes are now closed without a third option being identified. Physical interpretation
has no surviving mechanism.  
**New strongest version:** None at the energy-momentum level.  
**New next action:** Archive to NULL-SURVIVOR. The mass-energy bridge is not a viable claim
in the Poincare-invariant Lorentzian control case.

### TI-C010: Conditional Lorentzian realization theorem recovers mass-energy invariant if a nontrivial F exists

**Current status:** formalizing (antecedent-obstructed)  
**Proposed update:** archived (antecedent permanently obstructed in the Poincare-invariant
control case)  
**Reason:** BDO proved the antecedent is unsatisfiable in the full-boundary-data setting;
ICO proves the antecedent is unsatisfiable in the partial-boundary-data setting. No third
setting is available under the fixed (M, eta) guardrail. The conditional theorem is vacuously
satisfied. It remains a formally valid theorem, but its physical use — as a bridge between
Temporal Issuance and mass-energy — is permanently blocked in this control case.  
**New next action:** Archive to NULL-SURVIVOR. The theorem is a correct mathematical result;
record it as such without Temporal Issuance physical interpretation.

---

## Path Kill for memory/path-kills.md

```yaml
path: Inverted construction — Ext_S selection of Lorentzian momentum data left open by
      momentum-underdetermining LorHist' objects
reason_killed: >
  Inverted Construction Obstruction (ICO). With momentum-underdetermining LorHist' objects,
  p^mu is morphism-level (not object-level). But the morphism-level variation of p^mu is
  parametrized by target-side dynamical physics (coupling constants, interaction Hamiltonian,
  scattering amplitudes, angular distributions), not by source-side Ext_S invariants. Any
  Ext_S invariant that succeeds in selecting p^mu must encode target-side physics (absorbed,
  ICO-1), be insufficient to select p^mu (ICO-2), or be trivially a re-encoding of the
  completion choice (ICO-3). BDO and ICO together seal the Poincare-invariant Lorentzian
  energy-momentum route from both directions: BDO from the top (p^mu over-determined by
  objects), ICO from the bottom (p^mu variation under-indexed by source structure). Physical
  interpretation of Temporal Issuance archived to NULL-SURVIVOR.
evidence: >
  ICO argument in agent-runs/RUN-0029-inverted-construction-momentum-selection.md;
  BDO lemma in agent-runs/RUN-0028-construct-or-refute-minimal-nontrivial-realization-functor.md;
  NULL-SURVIVOR advocate section and Mathematical Minimalist verdict in RUN-0029;
  covariance check (pass) in RUN-0029 Relativity Physicist section.
local_minimum_risk: >
  Low. ICO is not a local-case restriction like BDO. It is an argument about the structure
  of any selection mechanism in any momentum-underdetermining Lorentzian target: the
  completions are parametrized by target-side dynamics, and source-side extension rules
  have no privileged access to those dynamics. The only escape would be a Lorentzian theory
  where the completion space is parametrized by source-category invariants — but this would
  require a non-standard physical theory in which observable scattering data is determined
  by source-category structure. No such theory is known or implied by Temporal Issuance.
possible_future_resurrection_trigger: >
  A non-standard physical theory (beyond standard Lorentzian field theory) in which the
  completion space of asymptotic scattering data is parametrized by an admissible-extension
  rule in a source category, AND where this parametrization is independently motivated
  (not by re-encoding standard physics). This would require going beyond the fixed (M, eta)
  control case — e.g., a new theory where the scattering matrix is generated by source-side
  extension rules rather than a Hamiltonian. Currently speculative at a level beyond the
  current program.
run_ref: RUN-0029
claim_refs:
  - TI-C007
  - TI-C009
  - TI-C010
```

---

## Resurrection / Second Path Kill: Which is it?

This is a **second path kill** (the first being BDO from RUN-0028), not a resurrection.

The inverted construction was the last identified door after BDO. ICO closes it.

The program's physical mass-energy bridge interpretation is therefore path-killed with
two independent obstructions (BDO and ICO), covering the full logical space:
- Full-boundary-data objects: BDO applies.
- Partial/asymptotic-boundary-data objects: ICO applies.

No third object-specification regime has been identified that evades both.

**Result: Second path kill, final for the energy-momentum route in the current control case.**

---

## Closeout Checklist

```yaml
run_record_written: true
strongest_version_generated_before_kill: true
  note: |
    Strongest version was LorHist' with covariant asymptotic objects and a non-trivial F
    that is non-constant on p^mu. This was the best possible version of the inverted
    construction. ICO kills it at the mechanism level, not the covariance level.
subagent_sections_run:
  - lorentzian_geometer: true
  - category_error_auditor: true
  - constructor_hidden_variable_skeptic: true
  - relativity_physicist: true
  - null_survivor_advocate: true
  - mathematical_minimalist: true
covariance_check: pass (LorHist' objects covariant; kill is at mechanism level)
hidden_variable_check: fail (ICO shows any selection mechanism imports target physics)
functoriality_verdict: formally feasible; mechanism-decoupled; does not rescue bridge
order_verdict: p^mu . F is NOT forced through preorder in LorHist' (formal advance over BDO);
  but this is mechanism-decoupled and does not constitute physical content
does_inverted_F_beat_null_survivor: no
claim_ledger_updates_proposed: true
  claims_touched: [TI-C007, TI-C008, TI-C009, TI-C010]
path_kill_recorded: true
  kill_name: Inverted Construction Obstruction (ICO)
memory_log_update_proposed: true
memory_summary_update_proposed: true
roadmap_update_proposed: true
next_trigger_plan_update_proposed: true
metrics_update_proposed: true
e008_update_proposed: true
physical_interpretation_disposition: archived_to_null_survivor
formal_residue_disposition: kept (history-class nontriviality, preorder-from-extension,
  formal E008 theorem, ExtCat non-order invariants)
commit_pushed: false_in_chat_applied_via_claude_code
```

---

## Files Changed

- `agent-runs/RUN-0029-inverted-construction-momentum-selection.md` (this file)
- `CLAIM-LEDGER.md` (TI-C007 weakened; TI-C009 archived; TI-C010 archived; TI-C008 clarified)
- `memory/path-kills.md` (append ICO path kill)
- `explorations/E008-conditional-lorentzian-realization-theorem.md` (append ICO + disposition)
- `ROADMAP.md` (log RUN-0029; update Phase 1F task list)
- `agent-governance/NEXT-TRIGGER-PLAN.md` (update with post-ICO state)
- `memory/steward-memory-log.md` (append RUN-0029 entry)
- `memory/steward-memory-summary.md` (update current state, strategy, killed paths)
- `agent-governance/STEWARD-METRICS.md` (append per-run signal record)
