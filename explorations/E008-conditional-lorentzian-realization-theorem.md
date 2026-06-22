---
artifact_type: exploration
status: active
governance_role: conditional_embedding_theorem
exploration_id: E008
last_updated_by: RUN-0026
claim_refs:
  - TI-C007
  - TI-C008
  - TI-C009
  - TI-C010
constitutional: false
---

# E008: Conditional Lorentzian Realization Theorem

## Purpose

Formalize the legitimate next-level version of the Temporal Issuance to mass-energy bridge.

This artifact does not derive `E = mc^2` from Temporal Issuance alone. It states a conditional embedding theorem:

```text
If admissible source extensions admit a Poincare-invariant Lorentzian realization with an action principle, then issued structures inherit the standard relativistic energy-momentum invariant.
```

The theorem is useful because it identifies the exact missing premise: a functor from `Ext_S` into a Lorentzian history/action category.

## Source Category

Let `ExtCat` be a category or category-like structure:

```text
objects: typed source states S, S', ...
morphisms: admissible extensions e: S -> S'
composition: admissible sequential extension
identity: null extension id_S
```

The induced source preorder is:

```text
S <=_S S' iff Hom_ExtCat(S, S') is nonempty.
```

RUN-0025 already showed that this preorder is only the thin reflection. The theorem below uses the morphisms, not the preorder, as the load-bearing structure.

## Lorentzian History Category

Fix a Lorentzian spacetime `(M, eta)` for the special-relativistic control case, with signature convention:

```text
eta = diag(1, -1, -1, -1)
x^0 = c t
```

Define a category `LorHist(M, eta, A)`:

```text
objects: admissible boundary data on spacelike hypersurfaces, or particle/field boundary states
morphisms: on-shell Lorentzian histories h: B0 -> B1 satisfying the Euler-Lagrange equations of an action A
composition: concatenation or gluing of histories along matching boundary data
identity: stationary or zero-duration identity history where defined
```

For field theory, a morphism can be a field configuration over a spacetime slab. For particle mechanics, a morphism can be a timelike worldline segment with endpoint data. The category may need a quotient by gauge, reparametrization, or boundary-preserving equivalence.

## Realization Functor

The missing bridge is a functor:

```text
F: ExtCat -> LorHist(M, eta, A)
```

Requirements:

```yaml
object_map: typed source states map to Lorentzian boundary or physical states
morphism_map: admissible extensions map to on-shell Lorentzian histories
composition_preservation: F(e2 circ e1) = F(e2) circ F(e1), up to stated equivalence
identity_preservation: F(id_S) = id_F(S)
quotient_respect: gauge or representation equivalent source extensions map to physically equivalent histories
nontriviality: at least one source distinction changes a Lorentzian observable, invariant, or admissible history class
```

Without such an `F`, the mass-energy bridge is only compatibility language.

## Symmetry And Action Assumptions

Assume:

```yaml
A1_lorentzian_target: F lands in Lorentzian histories over Minkowski spacetime or a local/asymptotic Lorentzian control regime.
A2_action: histories are stationary points of an action functional A.
A3_poincare_invariance: A is invariant under the Poincare group acting on histories.
A4_noether_regular: the standard regularity, boundary, and variational hypotheses needed for Noether currents hold.
A5_energy_momentum_defined: translation symmetry yields conserved energy-momentum p^mu for the interpreted history or total isolated issued structure.
A6_timelike_sector: the issued structure being interpreted has timelike total momentum.
```

The theorem does not hold without these assumptions. They are not currently derived by Temporal Issuance.

## Theorem Sketch

### Conditional Lorentzian Realization Theorem

Let `ExtCat` be a category of source states and admissible extensions. Let:

```text
F: ExtCat -> LorHist(M, eta, A)
```

be a realization functor into Lorentzian histories in Minkowski spacetime, preserving extension composition as history concatenation up to physical equivalence.

Assume the action `A` is Poincare-invariant and satisfies the hypotheses of Noether's theorem. Then each physically interpreted admissible extension `e` whose realized history `F(e)` is in the timelike sector carries a conserved energy-momentum vector `p^mu`. Its Lorentzian norm:

```text
p_mu p^mu
```

is invariant under Poincare transformations. Defining rest mass `m` by:

```text
p_mu p^mu = m^2 c^2
```

gives:

```text
E^2 = |p_vec|^2 c^2 + m^2 c^4
```

and in the rest frame `p_vec = 0`:

```text
E = m c^2
```

### Proof Skeleton

1. Since `F(e)` is an on-shell Lorentzian history for the action `A`, ordinary variational machinery applies to the realized history.
2. Poincare invariance of `A` implies, by Noether's theorem, conserved currents for spacetime translations and Lorentz transformations.
3. Translation invariance yields conserved four-momentum `p^mu`.
4. The Poincare group preserves the Minkowski metric `eta`, so the scalar `p_mu p^mu = eta_mu_nu p^mu p^nu` is invariant.
5. In the timelike sector, define rest mass by `p_mu p^mu = m^2 c^2`.
6. With `p^mu = (E/c, p_vec)`, the invariant equation becomes:

```text
E^2 / c^2 - |p_vec|^2 = m^2 c^2
```

Multiplying by `c^2` gives:

```text
E^2 = |p_vec|^2 c^2 + m^2 c^4
```

7. In the rest frame, `p_vec = 0`, so `E^2 = m^2 c^4`. For positive-energy timelike structures, `E = m c^2`.

## What Is Earned

This theorem legitimately completes the formal tail:

```text
Lorentzian realization + Poincare-invariant action
-> Noether energy-momentum
-> invariant mass shell
-> rest-frame E = mc^2
```

It also shows exactly where `c^2` enters:

```text
from the Lorentzian metric and four-momentum convention, not from issuance alone
```

## What Is Not Earned

The theorem does not prove:

- that `ExtCat` exists as a physical source category
- that Temporal Issuance determines `F`
- that GU's observerse is the right Lorentzian target
- that `F` is unique, canonical, or natural
- that all issued structures are timelike
- that mass is generated by issuance rather than defined by the Lorentzian norm after realization
- that `E = mc^2` is evidence for Temporal Issuance

## Sharp Failure Conditions

The conditional bridge fails if any of these cannot be supplied:

```yaml
no_functor_F: no source-to-Lorentzian realization bridge
no_composition_preservation: source extension composition does not correspond to history composition
no_action: no action functional on realized histories
no_poincare_invariance: no translation/Lorentz symmetry
no_noether_currents: no conserved energy-momentum
no_timelike_sector: no rest-frame mass interpretation
only_imported_physics: F merely labels ordinary relativity without source-side discriminator
```

The last condition is the most important for Temporal Issuance. A bridge that only says "if ordinary relativity, then ordinary relativity" is mathematically true but does no Temporal Issuance work.

## Next-Level Research Target

The next legitimate research target is not proving `E = mc^2`. That is already standard once the Lorentzian/Poincare premises are present.

The target is:

```text
construct or refute a nontrivial realization functor
F: ExtCat -> LorHist(M, eta, A)
```

RUN-0027 tightened this target:

```text
Construct or refute a minimal nontrivial realization functor F.
```

The run is optimized for epistemic value, not for producing a bridge. Failure is a successful outcome if it is precise.

### Nontriviality Requirement

`F` must preserve at least one source-side distinction beyond induced order.

Explicit test:

```text
same <=_S
different Ext_S invariant
```

If `F` cannot distinguish those cases, classify the realization as bookkeeping and downgrade the bridge.

### Earned-Structure Ladder

Evaluate the strongest earned result at each level:

```yaml
causal_preorder:
conformal_lorentzian_structure:
metric_up_to_scale:
full_lorentzian_metric:
action_principle:
noether_poincare_machinery:
```

The run may terminate successfully at any level.

### External Metric Assumption

Start with a fixed externally supplied `(M, g)`.

Do not attempt metric reconstruction unless the construction naturally forces it.

### GU Discipline

Keep GU outside the first construction. First attempt ordinary Lorentzian realization. Evaluate GU compatibility only afterward.

If the construction naturally points toward observerse-style geometry, document that separately instead of importing GU as the target by default.

with:

```yaml
C_type: physical boundary/source states
Ext_S_rule: admissible source extension
projection: source-to-Lorentzian-history functor
equivalence: gauge/reparametrization/representation quotient
invariant: morphism-level source invariant preserved by F
action: explicit A
symmetry: Poincare invariance or stated local/asymptotic replacement
Noether_output: p^mu
kill_test: same induced source order but different Ext_S invariant changes, or fails to change, Lorentzian energy-momentum data
```

If this functor cannot be constructed even in a finite or toy control model, the GU/mass-energy bridge should stay speculative and `NULL-SURVIVOR` remains the default for physical interpretation.

## Relation To Existing Claims

This artifact strengthens `TI-C008` and creates the legitimate formal target behind `TI-C009`. It does not promote `TI-C001`, `TI-C003`, or `TI-C007`.

The conditional theorem is formalizing. The physical existence of `F` remains speculative.
