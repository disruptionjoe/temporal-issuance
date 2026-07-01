---
artifact_type: agent_run
status: complete
run_id: RUN-0093
created: 2026-06-30
constitutional: false
---

# RUN-0093: Record-Table Admissibility vs TaF Fixture

## Trigger

Joe instructed:

```text
Let's run the goal.
```

The active goal was:

```text
W000 -> record_table_admissibility_vs_taf_reconstruction_fixture
```

## Workflow

Direct executable fixture pass.

## Strongest Version

Two record-table models can emit the same downstream TaF trace while differing at the
admissibility-provenance layer:

```text
A: fixed schema / fixed table / fixed predicate
B: prefix-formed candidate / compatibility predicate
```

## Strongest Objection

If the fixed model reproduces the same external trace and same TaF reconstruction, then the
prefix-formed model supplies no source-side evidence unless admissibility formation itself is
a record that cannot be fixed-precontained.

## Execution

```text
python tests/test_record_table_admissibility_taf_fixture.py
python tools/record_table_admissibility_taf_fixture.py --output tests/artifacts/record_table_admissibility_taf_fixture_result.json
```

Result:

```text
5/5 tests passing
```

## What Collapsed

The shortcut "record-table temporal reconstruction is a TI-owned result" collapsed into TaF.
TaF reconstructs the temporal order from the emitted trace in both models.

## What Survived

The admissibility-provenance distinction survived:

```text
B has prefix-formed Compat_n / Cand_n;
A precontains them.
```

But this is not yet source-side evidence.

## What Was Absorbed

The fixed completed table absorbs all external behavior in the fixture.

## What Was Promoted

Nothing.

## Files Changed

- `tools/record_table_admissibility_taf_fixture.py`
- `tests/test_record_table_admissibility_taf_fixture.py`
- `tests/artifacts/record_table_admissibility_taf_fixture_result.json`
- `explorations/E104-record-table-admissibility-vs-taf-fixture-2026-06-30.md`
- `agent-runs/RUN-0093-record-table-admissibility-vs-taf-fixture.md`
- `tests/README.md`
- `FORMAL-OBJECT.md`
- `HYPOTHESIS-STEELMAN.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `explorations/README.md`

## Recommended Next Run

```text
W000 -> record_table_no_fixed_schema_witness_or_demote
```
