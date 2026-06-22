---
artifact_type: exploration
exploration_id: E011
status: active
governance_role: w008_category_g_bms_attempt
source_run: RUN-0032
target_bridge: Temporal Issuance -> BMS soft charges / asymptotic physics
constitutional: false
claim_refs:
  - TI-C007
  - TI-C012
  - TI-C013
  - TI-C014
---

# E011: BMS Action Physics Bridge Attempt

## Purpose

Draft and run the strongest bounded goal for getting Temporal Issuance to a physics bridge after
RUN-0031:

```text
Attempt to define a BMS group action on ExtCat morphisms.
If successful, test whether the associated soft charge Q_f is a source-side Ext_S invariant.
If the construction only works by making ExtCat into standard BMS radiative phase space,
classify the bridge as absorbed by known asymptotic-symmetry physics.
```

This executes W008 Category G against the W009 bridge lemmas:

```yaml
BL-001: BMS-covariant ExtCat
BL-002: Q_f is morphism-level in ExtCat
BL-003: Q_f is not determined by Poincare p^mu
BL-007: Q_f is source-side rather than target-side
```

## References Checked

- Bondi, van der Burg, Metzner, "Gravitational waves in general relativity. VII", DOI page: https://inspirehep.net/literature/9161
- Sachs, "Asymptotic Symmetries in Gravitational Theory", DOI page: https://link.aps.org/doi/10.1103/PhysRev.128.2851
- Wald and Zoupas, "A General Definition of Conserved Quantities in General Relativity and Other Theories of Gravity", arXiv: https://arxiv.org/abs/gr-qc/9911095
- Strominger, "Lectures on the Infrared Structure of Gravity and Gauge Theory", arXiv: https://arxiv.org/abs/1703.05448

These sources support the background use of asymptotic symmetries, null infinity, radiation/news,
memory, and charge flux. They do not prove any Temporal Issuance claim.

## Goal Draft

```yaml
goal_name: BMS Soft-Charge Physics Bridge Attempt
objective: >
  Determine whether Temporal Issuance can get a legitimate physics bridge by treating
  admissible source extensions as BMS-covariant radiative histories whose morphism-level
  invariant is the supertranslation soft charge Q_f.
success_A: >
  Define ExtCat_BMS independently of LorHist_BMS, prove BMS acts on its morphisms, and prove
  Q_f is a Noether charge of that source-side action.
success_B: >
  Construct a coherent BMS-covariant realization, but classify it as absorbed because ExtCat_BMS
  is just the standard asymptotic radiative phase-space category.
failure_success: >
  Prove no BMS-compatible admissibility rule can be defined without importing target physics.
claim_discipline: >
  Do not claim Temporal Issuance derives BMS, soft charges, spacetime, mass, or E = mc^2.
```

## Construction Attempt

### Definition: ExtCat_BMS

Let the target physical setting be asymptotically flat general relativity at future null infinity
`I+`.

Define `ExtCat_BMS` as follows.

Objects:

```text
B = (cut, hard_sector, frame_class)
```

where:

- `cut` is a cut of null infinity.
- `hard_sector` records the non-soft particle or hard-radiation sector retained at the boundary.
- `frame_class` records the BMS frame or supertranslation orbit, not the full News tensor over an interval.

Morphisms:

```text
e: B0 -> B1
```

are equivalence classes of finite-flux radiative intervals between cuts. Concretely, a representative
is radiative data such as Bondi News `N_AB(u, z)` over an interval, satisfying the usual asymptotic
falloff and constraint equations, modulo gauge equivalences that preserve the retained object data.

Identity:

```text
id_B = zero-duration / zero-News interval
```

Composition:

```text
e2 o e1 = concatenation of radiative intervals
```

when the codomain cut and retained sector of `e1` match the domain cut and retained sector of `e2`.

Admissibility:

```text
Adm(e) iff e is finite-flux, satisfies the asymptotic field equations/constraints,
and respects the chosen boundary-sector policy.
```

This is a category after quotienting by boundary-preserving gauge/reparametrization equivalence.

### BMS Action

Let `G_BMS` be the BMS group. A BMS element acts on a cut and radiative data by the standard
asymptotic symmetry action at null infinity: it shifts/pulls back the retarded coordinate and angular
data and transforms the shear/News fields accordingly.

Define:

```text
g . B = transformed boundary object
g . e = transformed radiative interval
```

Then:

```text
g . id_B = id_(g.B)
g . (e2 o e1) = (g.e2) o (g.e1)
```

because the BMS action maps solutions satisfying the asymptotic equations and falloff conditions to
solutions satisfying the same class of equations and falloff conditions.

Verdict for BL-001:

```yaml
BL-001: passes_for_ExtCat_BMS
scope: BMS-realized/asymptotic-phase-space ExtCat
not_proved: BMS action on a pre-physical or source-independent ExtCat
```

### Soft Charge Functional

For each supertranslation parameter `f`, define a morphism functional:

```text
Q_f(e) = BMS supertranslation charge/flux associated with the radiative interval e
```

Abstractly, this is the Wald-Zoupas/BMS charge flux across the interval at null infinity. It depends
on the angular distribution of radiative data, not only on total Poincare four-momentum.

It is additive under composition up to the usual boundary conventions:

```text
Q_f(e2 o e1) = Q_f(e2) + Q_f(e1)
```

for compatible intervals and fixed charge convention.

It is morphism-level under the selected object policy:

```text
same B0, B1 retained object data
different radiative interval e1, e2
Q_f(e1) != Q_f(e2)
```

Verdict for BL-002:

```yaml
BL-002: passes_in_BMS-realized_ExtCat
condition: objects must not include the full interval News/radiative field as object data
failure_mode: if objects include full soft charge boundary data, Q_f becomes object-level
```

### Relation To Poincare Momentum

`Q_f` is not the same as total Poincare `p^mu`. BMS supertranslations extend beyond the finite
Poincare translation subgroup. The memory/soft-charge sector retains angular and soft information
that total four-momentum forgets.

Verdict for BL-003:

```yaml
BL-003: accepted_as_established_physics_for_this_run
role: explains why BDO for p^mu does not directly kill Q_f
```

### Critical Test: Is Q_f Source-Side?

The source-side test is stricter than the BMS construction.

Question:

```text
Is Q_f defined from ExtCat before ExtCat is identified with BMS radiative phase space?
```

Result:

```yaml
pre_BMS_source_definition_of_Q_f: not_found
Q_f_defined_after_identifying_ExtCat_with_BMS_phase_space: yes
source_side_independence: fails
absorber: standard asymptotic-symmetry / covariant-phase-space physics
```

This is the key distinction.

If `ExtCat_BMS` is defined as the category of asymptotic radiative intervals, then `Q_f` is a genuine
morphism-level charge and the BMS action is real. But the physics is doing all the work. Temporal
Issuance contributes a categorical wrapper around standard BMS memory/charge theory.

Verdict for BL-007:

```yaml
BL-007: fails_as_independent_Temporal_Issuance_bridge
BL-007_absorbed_version: passes_if_ExtCat_is_BMS_radiative_phase_space
reason: Q_f is source-side only because the source category has been defined as target physics
```

## W008 Verdict

```yaml
escape_route: Category_G_BMS_soft_charges
construction_found: yes
bridge_type: absorbed_physics_bridge
nontriviality_gate: pass_for_Q_f_as_morphism_level_charge
mechanism_check: fail_for_independent_Temporal_Issuance
BDO_applicability: avoided_because_Q_f_not_poincare_p_mu
ICO_prime_applicability: resolves_as_ICO_prime_1_target_physics_import
claim_upgrade: none
claim_downgrade: TI-C013 weakened_or_absorbed
new_claim: TI-C014_absorbed_BMS_realization
```

## What This Earns

1. A coherent BMS-covariant category of admissible radiative extensions can be defined.
2. The BMS group acts functorially on this category.
3. Soft charges can be treated as morphism-level invariants in that category.
4. This gives a real physics-facing bridge object:

```text
ExtCat_BMS -> LorHist_BMS
```

where the functor may be close to identity or inclusion.

## What It Does Not Earn

1. Temporal Issuance does not derive BMS symmetry.
2. Temporal Issuance does not derive soft charges.
3. `Q_f` is not source-side before importing asymptotic radiative phase-space structure.
4. The construction does not recover `E = mc^2`, mass, or Poincare energy-momentum.
5. The construction is not independent evidence for Temporal Issuance as a physical substrate.

## Absorber Comparison

| Absorber | Verdict |
| --- | --- |
| Asymptotic symmetry / BMS physics | Absorbs the construction. |
| Covariant phase space / Wald-Zoupas charges | Absorbs the charge definition. |
| Standard GR memory effect | Absorbs the morphism-level physical content. |
| Category theory | Absorbs the ExtCat presentation as a category of histories. |
| Temporal Issuance | Contributes terminology and a non-order test, not independent physics. |

## Five-Reviewer Synthesis

### Category Theorist

The BMS action on `ExtCat_BMS` is a genuine action by category automorphisms. The functoriality check
passes. The issue is not category theory; it is the choice of source category.

Verdict:

```text
Functorial, but source category is already physical target data.
```

### Relativity / BMS Specialist

The construction is compatible with standard asymptotic symmetry machinery. Soft charges are a valid
target observable and are not just Poincare momentum. However, once radiative null-infinity data is
included, this is standard BMS physics.

Verdict:

```text
Physics-correct control model, not new physics.
```

### Mathematical Physicist

The construction should be called an absorbed realization theorem: if `ExtCat` is the BMS radiative
history category, then BMS charges are morphism invariants. This is true but tautological as a bridge.

Verdict:

```text
Bridge by identification, not by derivation.
```

### Philosophy Of Science Reviewer

This is epistemically useful because it finds the nearest real physics bridge and identifies why it
does not promote the hypothesis. It changes the program from "maybe impossible" to "possible only
when absorbed by a known physical framework."

Verdict:

```text
Useful narrowing, no promotion.
```

### Adversarial Skeptic

The phrase "source-side" is doing illicit work if the source category is defined as BMS radiative
phase space. The bridge is: "if Temporal Issuance is standard BMS physics, then Temporal Issuance has
BMS charges." This is absorption.

Verdict:

```text
No independent bridge found.
```

## Final Classification

### Proven / Constructed

- A BMS-covariant extension category can be constructed when `ExtCat` is taken to be the category of
  asymptotic radiative intervals at null infinity.
- The BMS action is functorial on this category.
- `Q_f` can be treated as an additive morphism-level invariant under the chosen object policy.

### Formalized

- The exact absorption boundary:

```text
Q_f is source-side only if the source category is already BMS radiative phase space.
```

### Speculative

- A pre-BMS, source-independent `ExtCat` carrying a BMS action.
- A source-side admissibility rule that predicts soft charge sectors without importing News/radiative data.

### Refuted / Killed

The independent BMS soft-charge bridge:

```text
generic Temporal Issuance Ext_S
-> BMS action
-> source-side Q_f
-> physical bridge
```

is not earned. The only construction found is absorbed by BMS/covariant-phase-space physics.

## Most Promising Next Step

The next bridge attempt should move to the holonomy route:

```text
W008 Category F/H or W009 TM-A:
define an Ext_S connection,
construct a minimal loop/cycle,
compute curvature/holonomy,
then ask whether any known physical target sees that holonomy.
```

Reason:

`BL-004` was the cleanest BDO/ICO evasion in RUN-0031 because holonomy is defined inside ExtCat
and does not require importing BMS radiative dynamics.

## Most Dangerous Failure Mode

Calling an absorbed realization a bridge. The construction is real physics, but it is BMS physics
presented in Temporal Issuance language.
