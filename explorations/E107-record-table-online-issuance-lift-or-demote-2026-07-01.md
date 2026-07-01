---
artifact_type: exploration
status: active
governance_role: lift_or_demote_result
goal_ref: record_table_online_issuance_lift_or_demote
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md
  - explorations/E106-record-table-no-fixed-schema-witness-or-demote-2026-06-30.md
  - tools/record_table_online_issuance_lift.py
  - tests/test_record_table_online_issuance_lift.py
created: 2026-07-01
constitutional: false
---

# E107: Record-Table OnlineIssuance Lift Or Demote

## Purpose

Execute the route created by E106:

```text
W000 -> record_table_online_issuance_lift_or_demote
```

Question:

```text
Does RecordTableSystem^TI become a useful instance/interface of OnlineIssuance^LC, and does it
add any formal surplus over E091?
```

## Component Mapping

The record-table components map cleanly:

```text
Schema_n             -> Gamma_n
Cand_n               -> CandExt(Gamma_n)
Compat_n             -> Adm_n
Append_n             -> Iss_n / e_n
Witness_n            -> w_n : Adm_n(e_n)
Trace_n              -> tau_n
Project_i,n/TaF_i,n  -> Proj_{o,n} / Glue_n
```

This is a good interface mapping. It gives OnlineIssuance a concrete record-table presentation:
columns, candidate rows, compatibility predicates, append witnesses, formation records, and
downstream finality traces.

## Properness Gate Check

The record-table fixture passes the interface-friendly gates:

```yaml
P1_formed_present_domain: true
P2_witnessed_extension: true
P3_prior_context_unavailability: true
P5_recordability: true
```

It fails the load-bearing source-side gate:

```yaml
P4_no_hidden_completed_oracle: false
```

Reason:

```text
E106 shows fixed universal schema, fixed proof registry, fixed latent completed table, and fixed
richer source plus changing access all preserve the record-table formation trace.
```

So record-table language does not itself supply the no-hidden-oracle discipline. That discipline
belongs to `OnlineIssuance^LC`.

## Surplus Check

```yaml
component_mapping_total: true
record_table_is_online_issuance_interface: true
properness_gates_pass_without_extra_axioms: false
fails_no_hidden_oracle_gate: true
productive_self_encoding_witness_present: false
adds_formal_surplus_over_e091: false
inherits_e091_residue_without_extra_axioms: false
record_table_archive_as_vocabulary: true
source_side_residue_found: false
```

The missing pieces are exactly the E091/E090 pieces:

```text
no internally formed future oracle
self-encoding admissibility
productive/diagonal witness
```

The record-table fixture does not add those. It provides a clearer interface for them.

## Verdict

```yaml
Issue[S]: false
Project[O]: true
Finalize[R]: true
Lose[K]: true
claim_status_change: none
demote_record_table_ti: true
```

## Interpretation

The record-table idea now has a precise status:

```text
Record-table TI is not a standalone source-side route.
It is useful vocabulary and an interface layer for OnlineIssuance^LC, TaF, and observer records.
```

Plainly:

```text
"Dimensions are columns; time is row append, not a column" is a strong explanatory frame.
It is not, by itself, the thing that beats fixed precontainment.
```

The thing that still matters formally is `OnlineIssuance^LC`.

## Next Gate

Record-table-specific physics adapter work should stop unless a future OnlineIssuance result
supplies stronger residue.

Recommended next route:

```text
W000 -> machine_check_online_issuance_witness_or_frontier_rerank
```

Options:

1. Machine-check the E090 local-constructive witness schema.
2. Run W010 frontier re-ranking now that the record-table route is archived as vocabulary.

## Claim Effects

No claim movement.

```yaml
TI-C001:
  movement: none
  note: >
    TaF remains the downstream owner of temporal reconstruction.

TI-C003:
  movement: none
  note: >
    RecordTableSystem^TI is demoted as an independent formal object and retained as interface
    vocabulary for OnlineIssuance^LC and TaF.

TI-C019:
  movement: none
  note: >
    The only surviving source-side residue remains the E091 OnlineIssuance^LC discipline.

TI-C020:
  movement: none
  note: >
    Record-table-specific physics adapter work is closed until OnlineIssuance supplies stronger
    formal residue.
```
