---
artifact_type: agent_run
status: complete
run_id: RUN-0096
created: 2026-07-01
constitutional: false
---

# RUN-0096: Record-Table OnlineIssuance Lift Or Demote

## Trigger

Joe instructed:

```text
Keep going
```

The active route after RUN-0095 was:

```text
W000 -> record_table_online_issuance_lift_or_demote
```

## Workflow

Direct lift-or-demote fixture pass.

## Strongest Version

RecordTableSystem^TI might survive as a disciplined interface to `OnlineIssuance^LC`:

```text
Schema_n             -> Gamma_n
Cand_n               -> CandExt(Gamma_n)
Compat_n             -> Adm_n
Append_n             -> Iss_n / e_n
Witness_n            -> w_n : Adm_n(e_n)
Trace_n              -> tau_n
Project_i,n/TaF_i,n  -> Proj_{o,n} / Glue_n
```

## Strongest Objection

A clean component mapping is not enough. E091's source-side residue also requires no internally
formed completed future oracle, self-encoding admissibility, and a productive witness. E106
already showed the record-table fixture does not defeat fixed precontainment on its own.

## Execution

```text
python tests/test_record_table_online_issuance_lift.py
python tools/record_table_online_issuance_lift.py --output tests/artifacts/record_table_online_issuance_lift_result.json
```

Result:

```text
5/5 tests passing
```

## What Collapsed

The claim that record-table vocabulary adds formal surplus over `OnlineIssuance^LC` collapsed.

## What Survived

Record-table remains useful as an interface:

```text
dimensions as columns
time as append/finality rather than a column
formation records as concrete admissibility trace records
observer renderings as projection/finality surfaces
```

## What Was Absorbed

The formal force of record-table TI is absorbed by `OnlineIssuance^LC` plus TaF:

```text
source-side residue -> OnlineIssuance^LC
temporal reconstruction -> TaF
record-table -> explanatory/interface vocabulary
```

## What Was Promoted

Nothing.

## Files Changed

- `tools/record_table_online_issuance_lift.py`
- `tests/test_record_table_online_issuance_lift.py`
- `tests/artifacts/record_table_online_issuance_lift_result.json`
- `explorations/E107-record-table-online-issuance-lift-or-demote-2026-07-01.md`
- `agent-runs/RUN-0096-record-table-online-issuance-lift-or-demote.md`
- `tests/README.md`
- `explorations/README.md`
- `FORMAL-OBJECT.md`
- `HYPOTHESIS-STEELMAN.md`
- `ROADMAP.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`

## Recommended Next Run

```text
W000 -> machine_check_online_issuance_witness_or_frontier_rerank
```
