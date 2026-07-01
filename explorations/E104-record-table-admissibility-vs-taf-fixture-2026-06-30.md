---
artifact_type: exploration
status: active
governance_role: fixture_result
goal_ref: record_table_admissibility_vs_taf_reconstruction_fixture
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E103-record-table-taf-boundary-v0-1-definition-2026-06-30.md
  - tools/record_table_admissibility_taf_fixture.py
  - tests/test_record_table_admissibility_taf_fixture.py
created: 2026-06-30
constitutional: false
---

# E104: Record-Table Admissibility vs TaF Reconstruction Fixture

## Purpose

Execute the immediate E103 route:

```text
W000 -> record_table_admissibility_vs_taf_reconstruction_fixture
```

Question:

```text
If two record-table models emit the same downstream TaF-reconstructable trace, can Temporal
Issuance still identify a nonduplicative difference at the row-admissibility / append layer?
```

## Fixture

The executable fixture compares two models.

### Model A - Fixed Schema / Fixed Completed Table

```text
All columns are present from prefix 0.
All row candidates are present from prefix 0.
The join compatibility predicate is fixed from prefix 0.
```

### Model B - Prefix-Formed Admissibility

```text
Initial schema has only seed-row columns.
The join columns appear at prefix 2.
The join candidate is not available before prefix 2.
The join compatibility predicate is formed at prefix 2.
```

Both models emit the same TaF-style trace:

```text
e_alpha_lock <= e_join_lock
e_beta_lock  <= e_join_lock
e_alpha_lock || e_beta_lock
```

No row contains a `time`, `timestamp`, `clock`, `tick`, or `t` column.

## Execution

Executed locally:

```text
python tests/test_record_table_admissibility_taf_fixture.py
python tools/record_table_admissibility_taf_fixture.py --output tests/artifacts/record_table_admissibility_taf_fixture_result.json
```

Focused tests:

```text
5/5 passing
```

## Results

```yaml
external_trace_equal: true
taf_reconstruction_equal: true
no_time_column: true
taF_absorbs_temporal_order: true
ti_owned_admissibility_provenance_difference: true
fixed_completed_table_absorbs_external_behavior: true
source_side_residue_found: false
```

TaF reconstruction result:

```text
direct dependencies:
  e_alpha_lock -> e_join_lock
  e_beta_lock  -> e_join_lock

incomparable:
  e_alpha_lock || e_beta_lock
```

## Interpretation

This result cleanly separates the layers:

```text
TaF absorbs downstream temporal reconstruction.
TI can still talk about admissibility provenance before the trace enters TaF.
```

But the fixture does not defeat the fixed completed table absorber. Model A reproduces the
same external trace and the same TaF order while precontaining the join candidate and predicate.

So the surviving distinction is:

```text
admissibility provenance only
```

not:

```text
source-side issuance evidence
```

## Verdict

```yaml
Issue[S]: false
Project[O]: true
Finalize[R]: true
Lose[K]: true
claim_status_change: none
```

## What Advanced

The route is no longer duplicating TaF. The exact nonduplicative target is now visible:

```text
Show that prefix-formed Compat_n / Cand_n / Schema_n / Witness_n cannot be represented by a
fixed completed table, fixed schema, fixed access map, or fixed oracle without losing the
formation record.
```

## Next Gate

```text
W000 -> record_table_no_fixed_schema_witness_or_demote
```

Required:

1. Promote admissibility-formation events into explicit trace data.
2. Compare against fixed universal schema, fixed proof registry, fixed latent table, and
   fixed-access disclosure.
3. Decide whether formation records are genuine source/process evidence or just metadata
   that a larger fixed table can precontain.
4. If absorbed, demote record-table TI to TaF/log/database vocabulary.

## Claim Effects

No claim movement.

```yaml
TI-C001:
  movement: none
  note: >
    TaF reconstruction is confirmed as the correct downstream owner for temporal order.

TI-C003:
  movement: none
  note: >
    RecordTableSystem^TI remains a candidate object, narrowed to admissibility provenance.

TI-C019:
  movement: none
  note: >
    No source-side residue is found because fixed completed table absorption succeeds.

TI-C020:
  movement: none
  note: >
    No physical bridge; quantum/GU routes remain parked.
```
