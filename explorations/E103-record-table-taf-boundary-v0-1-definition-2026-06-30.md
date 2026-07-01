---
artifact_type: exploration
status: active
governance_role: formal_object_definition
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E102-record-table-five-goal-sequence-2026-06-30.md
  - ../time-as-finality/results/finali-event-structure-v0.1-results.md
  - ../time-as-finality/results/reconstruction-without-background-time-v0.1-results.md
created: 2026-06-30
constitutional: false
---

# E103: RecordTableSystem^TI v0.1 - TaF Boundary Definition

## Purpose

Execute Goal 1 from E102 while removing duplication with Time as Finality.

The correction is:

```text
TaF owns record-finality reconstruction.
TI owns row admissibility / append / schema-change pressure.
```

So `RecordTableSystem^TI` should not try to prove again that temporal order can be reconstructed
from finality records. TaF T48/T49 already supplies that baseline. The TI question is whether
the row-append process has a nonfixed admissibility or schema component that TaF finality
reconstruction treats only as input.

## TaF Baseline / Null

Time as Finality already has the relevant reconstruction claim:

```text
Given finalized records / FinaliEvent structures, reconstruct an observer-relative temporal
partial order without primitive background time.
```

Relevant TaF results:

- `T48 FinaliEvent Structure`: record-dependency partial order from finality-crossing events.
- `T49 Reconstruction Without Background Time`: temporal order reconstructed with no temporal
  variable in the reconstruction definitions.

Therefore this route is duplicative if its only result is:

```text
append/order/finality can answer before/past/future-style queries without a time column
```

That is a TaF result or TaF fixture extension.

## Boundary Table

| Object / question | Owner | Reason |
| --- | --- | --- |
| record stabilization | TaF | This is the lead TaF object. |
| reversal cost / finality depth | TaF | TaF owns D1/finality profiles and finality-induced direction. |
| temporal partial order from records | TaF | T48/T49 already test reconstruction without background time. |
| observer-local apparent finality / colimit | TaF | TaF owns observer-finality descent/colimit machinery. |
| `time notin Col` guard | TI | This is the record-table schema claim. |
| row admissibility `Compat_n` / `Adm_n` | TI | This is where source/process novelty can appear. |
| append as witnessed admissible extension | TI | This aligns with `OnlineIssuance^LC` and `Ext_S`. |
| nonfixed compatibility predicate / site / observable algebra | TI | This is the current source-side resurrection burden. |
| fixed completed table and fixed access absorbers | TI | These decide whether append is source-side or only projection/readout. |
| rendered 4D interface | shared, TI-gated | TaF supplies finality rendering; TI may ask whether schema/admissibility adds surplus. |

## Formal Object

The nonduplicative object is:

```text
RecordTableSystem^TI =
(
  Schema_n,      finite/currently formed column schema at prefix n
  Col_n,         columns available in Schema_n; primitive time excluded
  Row_n,         rows already admitted under Schema_n
  Cand_n,        candidate row/extensions formable from the current prefix
  Compat_n,      compatibility/admissibility predicate formed at prefix n
  Append_n,      witnessed transition Row_n -> Row_{n+1}
  Witness_n,     evidence that candidate row c satisfies Compat_n(c)
  Trace_n,       record emitted for downstream finality/reconstruction
  Project_i,n,   observer i access/render map into record/finality layer
  TaF_i,n,       downstream TaF reconstruction/finality process
  Absorb,        fixed-table/fixed-access/fixed-H/database/TaF null maps
)
```

Guard:

```text
time notin Col_n for all n
```

Handoff:

```text
Trace_n -> TaF_i,n
```

TaF may reconstruct order from `Trace_n`. TI may not count that reconstruction as source-side
surplus. TI surplus can only appear before or at `Append_n`: in `Schema_n`, `Cand_n`,
`Compat_n`, `Witness_n`, or failure of a fixed absorber map.

## Effect Typing

Every row event must be typed:

| Effect | Meaning |
| --- | --- |
| `Issue[S]` | `Compat_n` / admissibility / candidate space is not fixed-precontained and a witnessed append becomes available. |
| `Project[O]` | an observer gains access or a render map changes while the source table is fixed. |
| `Finalize[R]` | TaF-style record hardening / reversal-cost increase / finality reconstruction. |
| `Lose[K]` | projection, compression, forgetting, or loss of reconstructive detail. |

Default:

```text
Record-table temporal reconstruction = Project[O] + Finalize[R]
```

Only a nonfixed admissibility/schema witness can upgrade a row event toward:

```text
Issue[S]
```

## Required Absorber Maps

A future fixture must attempt these maps before claiming TI residue:

### A1 - TaF Reconstruction Absorber

Map `Trace_n` to a TaF FinaliEvent / D1-style structure and ask whether all temporal behavior
is recovered downstream.

Absorbed if:

```text
All before/past/future/observer-order behavior is explained after Trace_n enters TaF.
```

### A2 - Fixed Completed Table Absorber

Let a completed table `Table_*` contain all rows and all future admissibility decisions.

Absorbed if:

```text
Append_n is only revealing a prefix of Table_*.
```

### A3 - Fixed Schema / Database Absorber

Let a database schema and constraint engine be fixed in advance.

Absorbed if:

```text
Compat_n is just a fixed constraint check over known column types.
```

### A4 - Fixed Richer Source Plus Changing Access

Let `Mu_infty` contain the richer row/schema space and let observers gain access through
`Project_i,n`.

Absorbed if:

```text
Every apparent new row or column is bounded-access disclosure.
```

### A5 - Fixed-H / Fixed Observable Algebra

For quantum-facing claims, let one fixed Hilbert space / observable algebra plus changing
record maps reproduce the trace.

Absorbed if:

```text
No non-isomorphic observable algebra, admissibility predicate, or construction space is needed.
```

## Minimal Success Condition

The first nonduplicative success is not:

```text
we recovered temporal order without a time column
```

That belongs to TaF.

The first TI success must be:

```text
No fixed table, fixed schema, fixed access map, fixed-H model, or downstream TaF reconstruction
can reproduce the observed append/admissibility behavior while preserving records and witness
formation.
```

## Next Fixture

Replace the plain no-time-column fixture with:

```text
W000 -> record_table_admissibility_vs_taf_reconstruction_fixture
```

Fixture shape:

1. Build two models with the same downstream TaF-reconstructable trace.
2. Model A: fixed schema/fixed table/fixed access.
3. Model B: prefix-formed `Compat_n` or `Cand_n` with a witnessed append not available in the
   prior prefix.
4. Check whether TaF sees the same finality order in both.
5. If TaF sees the same order but only B has nonfixed admissibility, the distinction is
   properly TI-owned.
6. If A reproduces B entirely, record-table TI collapses to TaF/log/database reconstruction.

## Claim Effects

No claim movement.

```yaml
TI-C001:
  movement: none
  note: >
    The observer-side temporal reconstruction component is explicitly delegated to TaF.

TI-C003:
  movement: none
  note: >
    RecordTableSystem^TI v0.1 is defined as schema/admissibility plus TaF handoff, not as a
    standalone replacement for finality reconstruction.

TI-C019:
  movement: none
  note: >
    Source-side issuance remains possible only at nonfixed admissibility / schema / witness
    formation, not at downstream temporal reconstruction.

TI-C020:
  movement: none
  note: >
    Quantum/GU bridges remain parked until fixed-H and TaF reconstruction absorbers are
    defeated.
```
