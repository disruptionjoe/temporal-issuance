---
artifact_type: agent_run
status: complete
run_id: RUN-0103
created: 2026-07-01
constitutional: false
---

# RUN-0103: OI LC Assembly W4-W6 Physical Protocol Fixture

## Trigger

Joe requested:

```text
Do a bigger next swing
```

The active route after RUN-0102 was:

```text
W000 -> oi_lc_assembly_w4_w6_physical_protocol_fixture
```

## Workflow

Built a larger physical-protocol fixture for the Assembly branch. It evaluated real empirical
Assembly-looking traces, the E113 formal/local trace, and a schematic positive control against
`Adapter_P`.

## Execution

```text
python tests/test_oi_lc_assembly_w4_w6_physical_protocol_fixture.py
python tools/oi_lc_assembly_w4_w6_physical_protocol_fixture.py --output tests/artifacts/oi_lc_assembly_w4_w6_physical_protocol_fixture_result.json
python -m unittest discover -s tests
```

Focused result:

```text
6/6 tests passing
55/55 full-suite tests passing
```

## Verdict

```yaml
attempt_count: 6
real_physical_attempt_count: 4
all_real_physical_attempts_absorbed: true
w1_real_physical_candidate_found: false
w4_real_physical_protocol_found: false
w5_record_preservation_available_for_real_attempts: true
w6_real_physical_absorber_defeat_found: false
assembly_current_scope: formal_local_w2_w3_only
Issue[S]^assembly_local: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

## What Was Closed

Assembly Theory is closed as a current physical bridge unless new evidence supplies W1 and W4.
The real physical attempts are absorbed by fixed chemistry, fixed observable algebra, fixed
search/stochastic exploration, bounded access, and instrument/modeler schema.

## What Survived

Assembly remains useful as formal/local W2/W3 witness vocabulary for `OnlineIssuance^LC`.

## Files Changed

- `tools/oi_lc_assembly_w4_w6_physical_protocol_fixture.py`
- `tests/test_oi_lc_assembly_w4_w6_physical_protocol_fixture.py`
- `tests/artifacts/oi_lc_assembly_w4_w6_physical_protocol_fixture_result.json`
- `explorations/E114-oi-lc-assembly-w4-w6-physical-protocol-fixture-2026-07-01.md`
- `agent-runs/RUN-0103-oi-lc-assembly-w4-w6-physical-protocol-fixture.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `explorations/README.md`
- `tests/README.md`
- `HYPOTHESIS-STEELMAN.md`
- `FORMAL-OBJECT.md`

## Recommended Next Run

```text
W000 -> proof_assistant_online_issuance_witness
```
