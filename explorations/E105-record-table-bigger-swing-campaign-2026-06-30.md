---
artifact_type: exploration
status: active
governance_role: goal_campaign
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E104-record-table-admissibility-vs-taf-fixture-2026-06-30.md
  - explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md
created: 2026-06-30
constitutional: false
---

# E105: Record-Table Bigger-Swing Campaign

## Purpose

Orchestrate a few goals that give the record-table idea a bigger but still governed swing.

E104 produced the correct narrow result:

```text
TaF absorbs downstream temporal reconstruction.
The remaining TI-owned surface is admissibility provenance.
Fixed completed table still absorbs the first fixture.
```

So the next campaign must attack the fixed-schema / fixed-table / fixed-oracle absorber
directly. If it cannot, record-table TI should be demoted to TaF/log/database vocabulary.

## Campaign Spine

```text
Goal A: no-fixed-schema witness or demotion
Goal B: productive admissibility / OnlineIssuance lift
Goal C: physics-facing adapter preflight
```

The campaign is serial. Goal C cannot be used as evidence unless Goal A or Goal B leaves a
formal residue.

## Goal A - No-Fixed-Schema Witness Or Demotion

Trigger:

```text
W000 -> record_table_no_fixed_schema_witness_or_demote
```

Question:

```text
Can admissibility-formation records defeat fixed universal schema, fixed proof registry, fixed
latent table, and fixed-access disclosure?
```

Method:

1. Extend the E104 fixture so formation events are first-class records:
   `form_schema`, `form_candidate`, `form_compat`, `form_witness`.
2. Compare four nulls:
   - fixed universal schema;
   - fixed proof registry;
   - fixed latent completed table;
   - fixed richer source plus changing access.
3. Require the absorber maps to preserve:
   - emitted TaF trace;
   - row records;
   - formation records;
   - admissibility witness dependencies;
   - prefix availability constraints.
4. Decide whether the fixed absorber can represent the formation trace without treating
   unavailable prior objects as available.

Success:

```text
At least one formation record cannot be represented by a fixed schema/table/access/oracle
without violating prefix availability or witness dependency preservation.
```

Failure:

```text
All formation records are representable as metadata over a fixed completed object.
```

Failure action:

```text
Demote record-table TI to TaF/log/database vocabulary and stop treating it as a source-side
route unless Joe supplies a stronger candidate.
```

## Goal B - Productive Admissibility / OnlineIssuance Lift

Run only if Goal A is not cleanly absorbed, or if Goal A identifies the exact missing property.

Trigger:

```text
W000 -> record_table_online_issuance_lift
```

Question:

```text
Can RecordTableSystem^TI inherit the strongest OnlineIssuance^LC residue:
local constructive source extension + self-encoding admissibility + productive successor +
no internally formed future oracle?
```

Method:

1. Map E104/E105 objects into `OnlineIssuance^LC`:
   - `Schema_n` -> `Gamma_n`;
   - `Cand_n` -> `CandExt(Gamma_n)`;
   - `Compat_n` -> `Adm_n`;
   - `Append_n` + `Witness_n` -> `e_n : CandExt(Gamma_n), w_n : Adm_n(e_n)`;
   - `Trace_n` -> `tau_n`.
2. Compare against finite/computable/fixed-law/fixed-oracle absorbers already used in the
   OnlineIssuance sequence.
3. Ask whether record-table vocabulary adds any new discriminator or simply re-expresses
   `OnlineIssuance^LC`.

Success:

```text
RecordTableSystem^TI becomes an instance or useful interface for OnlineIssuance^LC, with an
explicit no-hidden-oracle condition and a concrete formation-record fixture.
```

Failure:

```text
RecordTableSystem^TI adds no formal surplus over OnlineIssuance^LC and should be archived as
explanatory vocabulary only.
```

## Goal C - Physics-Facing Adapter Preflight

Run only after Goal A or B leaves a formal residue. This goal does not promote TI-C020.

Trigger:

```text
W000 -> record_table_physical_adapter_preflight
```

Question:

```text
If the formal route survives, what exact physical-facing witness would be required before
relativity, quantum, or GU adapter language becomes meaningful?
```

Method:

1. State the minimal `Adapter_B` contract:
   - nonfixed observable algebra, or
   - nonfixed compatibility predicate, or
   - nonfixed site/cover, or
   - nonfixed admissibility witness formation.
2. Require preservation of:
   - record trace;
   - TaF reconstruction;
   - gauge/covariance discipline;
   - fixed-H and Minkowski/GR-first nulls.
3. Route candidate sources:
   - GU missing-piece adapter;
   - quantum measurement / fixed-H boundary;
   - relativistic render-consistency.
4. Produce only a preflight spec, not a physics claim.

Success:

```text
The campaign names a concrete physical-facing fixture whose success condition is not merely
"looks like quantum/relativity/GU."
```

Failure:

```text
Physics-facing language remains evocative and should stay parked.
```

## Promotion / Demotion Rules

Promote nothing directly.

Demote the route if:

```text
Goal A is fully absorbed and Goal B adds no formal surplus over OnlineIssuance^LC.
```

Keep the route alive if:

```text
Goal A produces a prefix-availability obstruction, or Goal B turns RecordTableSystem^TI into a
clear instance/interface for OnlineIssuance^LC with a runnable formation-record fixture.
```

Only then consider Goal C.

## Recommended Immediate Goal

```text
W000 -> record_table_no_fixed_schema_witness_or_demote
```

This is the honest bigger swing because it attacks the exact absorber that won in E104.

## Claim Effects

No claim movement.

```yaml
TI-C001:
  movement: none
  note: >
    TaF remains the owner of temporal reconstruction.

TI-C003:
  movement: none
  note: >
    RecordTableSystem^TI is now routed through a no-fixed-schema witness gate.

TI-C019:
  movement: none
  note: >
    The campaign tries to connect record-table admissibility to the existing OnlineIssuance^LC
    residue, but no source-side movement is earned yet.

TI-C020:
  movement: none
  note: >
    Physics-facing adapter work is explicitly gated behind formal residue.
```
