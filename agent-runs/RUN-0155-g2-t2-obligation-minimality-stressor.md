---
artifact_type: agent_run
status: complete
run_id: RUN-0155
run_family: research_steering_wave
created: 2026-07-12
trigger: joe_direct_request
constitutional: false
claim_status_change: none
---

# RUN-0155: G2 T2 Obligation-Minimality Stressor

## Objective

Execute the approved G2 focused swing: stress-test the T2 counterexample
contract by checking whether any E172/E173 obligation is redundant or
over-strong under single-omission testing.

## Method

1. Treated E173/T2 and E174/T3 as fixed inputs.
2. Built `tools/g2_t2_obligation_minimality_stressor.py`.
3. Added focused tests and generated the JSON artifact.
4. Ran the inline council reflection and generative rerank in E175.
5. Updated the steering card, priority engine, trigger plan, roadmap, memory,
   and test index.

## Result

```yaml
g2_result: all_t2_counterexample_obligations_load_bearing_no_redundant_clause_detected
obligation_count: 19
all_obligations_load_bearing: true
redundant_obligation_ids: []
overstrong_obligation_ids: []
real_counterexample_packet_found: false
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
```

Primary artifact:

```text
explorations/E175-g2-t2-obligation-minimality-stressor-2026-07-12.md
```

Executable artifact:

```text
tools/g2_t2_obligation_minimality_stressor.py
tests/test_g2_t2_obligation_minimality_stressor.py
tests/artifacts/g2_t2_obligation_minimality_stressor_result.json
```

## Files Changed

- `tools/g2_t2_obligation_minimality_stressor.py`
- `tests/test_g2_t2_obligation_minimality_stressor.py`
- `tests/artifacts/g2_t2_obligation_minimality_stressor_result.json`
- `explorations/E175-g2-t2-obligation-minimality-stressor-2026-07-12.md`
- `attention/priority_condorcet.py`
- `attention/research-steering-card.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `memory/steward-memory-summary.md`
- `tests/README.md`
- `agent-runs/RUN-0155-g2-t2-obligation-minimality-stressor.md`

## Validation

- `python tools/g2_t2_obligation_minimality_stressor.py --output tests/artifacts/g2_t2_obligation_minimality_stressor_result.json`
- `python tests/test_g2_t2_obligation_minimality_stressor.py`
- `python tests/test_t3_t2_counterexample_gate_validator.py`
- `python attention/priority_condorcet.py`
- `python tools/run_record_schema_audit.py agent-runs/RUN-0155-g2-t2-obligation-minimality-stressor.md`
- `python -m py_compile tools/g2_t2_obligation_minimality_stressor.py tests/test_g2_t2_obligation_minimality_stressor.py`
- `git diff --check`

## Boundaries

- No claim movement.
- No core hypothesis change.
- No universal physics no-go claim.
- No D-FORK decision claim.
- No physical-source claim.
- No `TI-C020` reopen.
- No external publication or non-GitHub external action.
