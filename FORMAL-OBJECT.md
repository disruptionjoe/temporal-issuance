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
