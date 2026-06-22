---
artifact_type: formal_definition_repair
status: active
governance_role: definition_repair
constitutional: false
last_updated_by: RUN-0013
---

# Formal Definition Repair

## Purpose

Repair the highest-risk components from RUN-0012 without strengthening the hypothesis prematurely.

Focus components:

- `mu`
- `kappa_i`
- `G_ij`

## Repair Candidate 1: Measure

Replace generic `mu` with a stricter placeholder:

```text
lambda_i: local constraint-extension measure over R_i
```

Minimum requirements:

- invariant under relabeling of local constraint states
- monotone under extension of fixed constraints
- defined without cosmological scale, volume, entropy, action, probability, or Shannon information as primitive
- able to compare compatible local patches only when `G_ij` supplies a reconciliation map

Status:

`lambda_i` is only a candidate. It does not resurrect killed generic `mu`.

Kill condition:

If `lambda_i` cannot be defined without importing entropy, information, action, probability, volume, or expansion, archive the measure component.

## Repair Candidate 2: Cadence

Replace cadence as clock-rate language with:

```text
kappa_i: ordered record-update relation over A_i-accessible changes in R_i
```

Minimum requirements:

- ordinal, not metric
- defined over record-update order, not external time
- compatible with local partial order
- able to express missed, delayed, or coalesced updates

Status:

`kappa_i` remains circular unless a concrete update relation can be specified without temporal metric assumptions.

Kill condition:

If `kappa_i` requires primitive time to define cadence, kill it or move it to an observer-model layer.

## Repair Candidate 3: Reconciliation

Replace generic `G` with pairwise reconciliation maps and obstruction records:

```text
G_ij: partial reconciliation maps between LocalIssuancePatch_i and LocalIssuancePatch_j
Omega_ij: obstruction or lag record when reconciliation fails or is delayed
```

Minimum requirements:

- state when two local patches are compatible
- state when access limits prevent reconciliation
- expose lag or obstruction rather than silently forcing global agreement
- be compared against existing sheaf, restriction, and time-as-finality machinery

Status:

`G_ij` is promising but likely absorbed unless obstruction or lag structure does real work.

Kill condition:

If `G_ij` is only ordinary gluing or restriction with new names, absorb it.

## Revised Working Object

```text
LocalIssuancePatch_i = (
  R_i,
  <=_i,
  A_i,
  kappa_i,
  lambda_i
)

ReconciliationSystem = (
  {LocalIssuancePatch_i},
  G_ij,
  Omega_ij
)
```

## RUN-0019 Bridge Verdict

The issuance-to-finality bridge toy model moved the repaired components into layers:

| Component | RUN-0019 result | Reason |
| --- | --- | --- |
| `kappa_i` | readout-side | Different cadences changed apparent finality without changing source realization. |
| `G_ij` | readout-side | It reconciles projected observer records after source constraints have already been read out. |
| `Omega_ij` | readout-side audit | It records projection or reconciliation failure, but does not generate source realization. |
| `lambda_i` / `mu` | outside core | Different measures did not change the bridge projection or any invariant. |

Current source-side candidate after RUN-0019:

```text
SourceRealization = (
  C,
  <=_S,
  Ext_S
)
```

Kill condition:

If `<=_S` and `Ext_S` factor through causal order, ordinary dependency order, record generation, entropy, information, probability, volume, action, or primitive time, absorb or archive the remaining formal object.

## Next Test Candidates

1. Specify `<=_S` and `Ext_S` without causal order, ordinary dependency order, record generation, entropy, information, probability, volume, action, or primitive time.
2. Test whether any source extension rule changes observer capabilities in a way time-as-finality readout cannot already express.
3. If not, absorb the remaining object into existing causal/dependency and record-reconstruction machinery.
