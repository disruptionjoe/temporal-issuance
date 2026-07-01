---
artifact_type: agent_run
status: complete
run_id: RUN-0101
created: 2026-07-01
constitutional: false
---

# RUN-0101: OI LC Candidate Scout W1-W6 Table

## Trigger

Joe requested:

```text
All right, let's take the next big swing.
```

The active route after RUN-0100 was:

```text
W000 -> oi_lc_candidate_scout_w1_w6_table
```

## Workflow

Built an executable `Adapter_P` candidate scout and scored seven candidate families against:

```text
adapter mapping
W1-W6 witness obligations
fixed-source nulls
stop-rule verdict
```

## Execution

```text
python tests/test_oi_lc_candidate_scout_w1_w6_table.py
python tools/oi_lc_candidate_scout_w1_w6_table.py --output tests/artifacts/oi_lc_candidate_scout_w1_w6_table_result.json
python -m unittest discover -s tests
```

Result:

```text
5/5 focused tests passing
44/44 full-suite tests passing
```

## Verdict

```yaml
candidate_count: 7
fixture_candidate_count: 1
parked_count: 2
killed_shortcut_count: 4
selected_fixture_candidate: assembly_theory_source_assembly_index
selected_scope: executable absorber fixture target, not evidence
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

## What Was Promoted

Nothing.

## What Was Selected

Assembly Theory source assembly index was selected only as the next fixture target because it can
state a concrete W2/W3 obligation:

```text
AI_src,n undefined -> AI_src,n+1 defined
```

It still has to defeat bounded-access and experimenter-added-schema absorbers.

## What Was Killed As Shortcut

```text
quantum measurement/contextuality alone
holographic/boundary encoding as fixed completion
quantum-biological / Orch-OR substrate alone
current-form dual-record adjacent-possible graph route
```

## Files Changed

- `tools/oi_lc_candidate_scout_w1_w6_table.py`
- `tests/test_oi_lc_candidate_scout_w1_w6_table.py`
- `tests/artifacts/oi_lc_candidate_scout_w1_w6_table_result.json`
- `explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md`
- `agent-runs/RUN-0101-oi-lc-candidate-scout-w1-w6-table.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `explorations/README.md`
- `tests/README.md`
- `HYPOTHESIS-STEELMAN.md`

## Recommended Next Run

```text
W000 -> oi_lc_assembly_source_adapter_fixture
```
