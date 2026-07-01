---
artifact_type: agent_run
status: complete
run_id: RUN-0102
created: 2026-07-01
constitutional: false
---

# RUN-0102: OI LC Assembly Source Adapter Fixture

## Trigger

Joe requested:

```text
Do another big swing
```

The active route after RUN-0101 was:

```text
W000 -> oi_lc_assembly_source_adapter_fixture
```

## Workflow

Built an executable Assembly source-index absorber fixture for:

```text
AI_src,n undefined -> AI_src,n+1 defined
```

The fixture compares against projection access, fixed complete assembly space, modeler-added
schema, and fixed stochastic/search-process controls.

## Execution

```text
python tests/test_oi_lc_assembly_source_adapter_fixture.py
python tools/oi_lc_assembly_source_adapter_fixture.py --output tests/artifacts/oi_lc_assembly_source_adapter_fixture_result.json
python -m unittest discover -s tests
```

Focused result:

```text
5/5 tests passing
49/49 full-suite tests passing
```

## Verdict

```yaml
all_negative_controls_rejected: true
local_source_candidate_source_d4: true
local_source_candidate_targeted_absorbers_defeated: true
local_source_candidate_passes_assembly_source_gate: true
local_source_candidate_adapter_contract_passed: false
Issue[S]^assembly_local: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

## What Survived

Assembly Theory source assembly index survives as a formal/local witness shape:

```text
AI_src,n(ABC) undefined
AI_src,n+1(ABC) = 2
```

where `bind_c(AB, C) -> ABC` is source-generated and recorded.

## What Was Rejected

The fixture rejects four false positives:

```text
projection/access D4
fixed complete assembly space
experimenter/modeler-added schema
fixed search/discovery process
```

## What Was Not Promoted

No physical claim was promoted. The surviving trace lacks W1 and W4 and is not a real physical
candidate.

## Files Changed

- `tools/oi_lc_assembly_source_adapter_fixture.py`
- `tests/test_oi_lc_assembly_source_adapter_fixture.py`
- `tests/artifacts/oi_lc_assembly_source_adapter_fixture_result.json`
- `explorations/E113-oi-lc-assembly-source-adapter-fixture-2026-07-01.md`
- `agent-runs/RUN-0102-oi-lc-assembly-source-adapter-fixture.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `explorations/README.md`
- `tests/README.md`
- `HYPOTHESIS-STEELMAN.md`
- `FORMAL-OBJECT.md`

## Recommended Next Run

```text
W000 -> oi_lc_assembly_w4_w6_physical_protocol_fixture
```
