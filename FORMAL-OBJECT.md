---
artifact_type: formal_object
status: speculative
governance_role: mathematical_seed
claim_refs:
  - TI-C003
constitutional: false
---

# Formal Object

Initial object:

```text
IssuanceSystem = (
  R,          realized events / constraints
  <,          realization-dependency order
  mu,         issuance measure on realized structure
  dR,         frontier between unrealized and realized
  O_i,        observer sites
  kappa_i,    local record-keeping cadence for each observer
  A_i,        access relation: what observer i can inspect
  G,          gluing / reconciliation rules across observers
)
```

## Current Pressure Result

RUN-0012 weakened this object. RUN-0019 weakened the RUN-0014 survivor further. The current working target is no longer the launch object as written, and the local gluing survivor should be treated as readout-side until proven otherwise.

See `FORMAL-OBJECT-PRESSURE-RESULTS.md`.

RUN-0012 working sketch:

```text
LocalIssuancePatch_i = (
  R_i,
  <=_i,
  A_i,
  kappa_i,
  G_ij
)
```

`mu` is demoted to an unresolved measure candidate. Global `dR` remains killed.

RUN-0019 bridge sketch:

```text
SourceRealization = (
  C,
  <=_S,
  Ext_S
)

ObserverReadout_i = (
  A_i,
  kappa_i,
  Rec_i
)

ProjectionAndReconciliation = (
  pi_TaF,
  G_ij,
  Omega_ij
)
```

`kappa_i`, `G_ij`, and `Omega_ij` survive as observer-readout, reconciliation, and audit machinery. They should not be treated as source-side primitives unless a future model shows that they constrain source extensions rather than projected records.

RUN-0021 ontology-resolution correction:

Do not treat `SourceRealization` as one survivor. Treat its source-side components independently:

```text
C
<=_S
Ext_S
```

Each component needs its own absorber threats, kill criteria, resurrection criteria, and status. The next research run should use `explorations/E003-source-residue-ontology-competition-brief.md` to compare source-side ontology competitors, including `NULL-SURVIVOR`.

RUN-0022 steelman correction:

The strongest constructive reading treats `Ext_S` as the likely load-bearing component:

```text
source-side constraints become admissibly extended,
and observer histories are lossy projections of that extension.
```

Use `HYPOTHESIS-STEELMAN.md` as the strongest target and `explorations/E005-ontology-competition-fixture-suite.md` as the shared test surface for ontology competition.

RUN-0024 ontology competition result:

The fixture-based competition in `explorations/E006-ontology-survivor-competition-results.md` separates the source-side components:

| Component | RUN-0024 status | Formal consequence |
| --- | --- | --- |
| `C` | weakened, carrier only | Must be typed by the next `Ext_S` model; not an independent survivor. |
| `<=_S` | killed as independent source-side primitive | Preserve only as a derived invariant or shadow of a successful extension rule. |
| `Ext_S` | formalizing next test target | Must be specified with a typed carrier, projection map, quotient, witness or invariant, transformation consequence, absorber comparison, and kill condition. |

The next formal pass after RUN-0024 should not defend source order first. RUN-0028 attempted the minimal realization branch and showed that a nontrivial `F` requires a weight `Q`. The remaining `Ext_S` no-go now turns on whether `Q` can be source-defined rather than absorbed by transition-system, proof, computation, constructor/resource, thermodynamic, information-theoretic, variational, or time-as-finality accounting.

RUN-0025 category-first correction:

`Ext_S` should be modeled first as a category or category-like structure:

```text
objects: typed source states or constraint states C
morphisms: admissible extensions e: S -> S'
```

The relation `<=_S` is then the thin reflection:

```text
S <=_S S' iff Hom_Ext(S, S') is nonempty
```

If identities and composition are present, this relation is a preorder. It becomes a partial order only after quotienting mutual reachability or imposing antisymmetry conditions. RUN-0025 proves that morphism-level extension invariants can differ while the induced order is identical, so future formal work should not replace `Ext_S` with `<=_S`.

RUN-0026 conditional Lorentzian realization target:

If the source-extension object tries to touch mass-energy, the formal object is not `E = mc^2`. RUN-0026 made the next object a realization functor:

```text
F: ExtCat -> LorHist(M, eta, A)
```

where `LorHist(M, eta, A)` is a category of Lorentzian histories with action `A`. The functor must preserve extension composition as history composition. If `A` is Poincare-invariant and Noether currents exist, ordinary relativistic energy-momentum follows for timelike realized extensions. This is a conditional theorem target, not a substrate claim.

RUN-0028 minimal realization result:

A minimal nontrivial realization functor can be constructed only after adding a morphism-level source invariant:

```text
Q: Mor(ExtCat) -> ([0, infinity), +)
```

The toy target is metric-sensitive Lorentzian history:

```text
F: TI_Ext^Q -> LorHist_g(M)
Tau(F(e)) = alpha Q(e)
```

This preserves same-order/different-extension distinctions when `LorHist_g(M)` remembers proper time. It fails if the target is reduced to causal preorder alone. The result is a kinematic control model, not a physical bridge: `Q`, `(M, g)`, action, Poincare symmetry, and Noether machinery are not derived.

RUN-0049 predictive/accessibility fixture interface:

This is an optional `TI-C020` physical-bridge interface. It does not replace `Ext_S`,
`OnlineSchemaSys`, D-FORK, or the MLTT `Compat_G` formalization. It exists to test whether a
predictive-to-accessible transition is fixed-H readout or H-growing issuance.

```text
P_n       predictive state/process space at stage n
A_n       accessible record or observable algebra at stage n
rho_n     readout/projection map P_n -> A_n
H_fixed   null model: one fixed Hilbert/state/observable space with changing access or values
H_grow    success model: non-isomorphic growth of admissible observable algebra, predicate,
          or construction space
```

Formal discriminator:

```text
fixed-H absorbed:
  exists H_infty and access maps alpha_n such that every A_n and rho_n factors through H_infty

H-growing candidate:
  no fixed H_infty / A_infty / Mu_infty can factor all A_n, rho_n, and admissibility updates
  while preserving records, morphisms, and observer reconstruction
```

Orch-OR, microtubule superradiance, anesthetic perturbation, and GU signed-readout comparisons
belong here only as fixture sources. They do not by themselves supply `H_grow`.

RUN-0081 OnlineIssuance verdict:

The current strongest formal source object is the narrowed class-relative residue:

```text
OnlineIssuance^LC =
(
  Gamma_n,     prefix-presented constructive context
  Adm_n,       admissibility predicate formed at prefix n
  Ext_n,       witness-bearing extension category available at n
  Iss_n,       source extension step
  Proj_{o,n},  observer projection/readout
  Glue_n,      downstream reconciliation/finality operation
  tau_n        recordable source trace
)
```

The load-bearing source gate is:

```text
Issue[S](Gamma_n, e_n, w_n) is source-side only if:

1. Gamma_n, CandExt(Gamma_n), and Adm_n are formed at prefix n.
2. e_n : CandExt(Gamma_n) and w_n : Adm_n(e_n).
3. the issued target is unavailable in Gamma_n.
4. no internally formed future-schema oracle, fixed latent graph, fixed stochastic law, or
   completed extension diagram precontains all future admissible witnesses.
5. the step emits a recordable trace tau_n for projection/finality audit.
```

Absorber verdict:

```text
finite/computable/fixed-law/adaptive-search/fixed-latent growth: absorbed
category/context/fibration/sheaf/colimit structure: absorbed as presentation
external Platonist completion: absorbs as navigation, not internal source issuance
local constructive productive witness: survives class-relatively
```

This is not a physical bridge, not a new category-theoretic primitive, and not a proof that
reality issues. It is the current narrow formal target for `TI-C019`.

## Component Pressures

`R`: What is realized? Events, constraints, records, facts, boundary conditions, or equivalence classes?

`<`: Is the dependency order causal, logical, informational, physical, or something else?

`mu`: What does the measure count? Entropy, action, volume, information, probability mass, constraint density, or a new invariant?

`dR`: Is the frontier meaningful in a relativistic setting, or does it reintroduce a preferred foliation?

`O_i`: What makes an observer site? Physical subsystem, measurement channel, record-keeping process, or access boundary?

`kappa_i`: Can local cadence be defined without smuggling in ordinary time?

`A_i`: What can an observer inspect? Records, events, constraints, histories, summaries, or proofs?

`G`: What reconciliation rules glue observer-local records into global structure?

## First Formal Test

The object must survive these questions before being strengthened:

1. Can each component be defined without circular reference to ordinary time?
2. Does the object reduce to a known framework under clear conditions?
3. Does anything remain after known frameworks absorb it?
4. Can the object generate a theorem, no-go result, model, or discriminator?
