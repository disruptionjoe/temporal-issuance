---
artifact_type: agent_run
status: complete
run_id: RUN-0144
run_family: user_directed_research_steering_wave
created: 2026-07-12
trigger: joe_direct_request
constitutional: false
---

# RUN-0144: Research Steering Wave 0 Starter

## Objective

Orchestrate a starter wave from the research-steering priority list without violating dependencies.

## Method

1. Re-ran `attention/priority_condorcet.py`.
2. Kept H1 local as the blocking lane.
3. Fanned out read-only sidecar lanes for H2, H3/H4, H5, and H7.
4. Merged the sidecar results into one exploration packet.
5. Added a deterministic Wave 0 starter computation and focused test.

## Result

```yaml
wave0_started: true
blocking_lane: H1 whole-family completion barrier theorem
dependent_starter: H2 operative source-action generator
sidecar_starters:
  - H3/H4 physical calibration pair
  - H5 multi-holder reversal-cost separator
  - H7 Adapter_P preservation-map contract
claim_status_change: none
physical_source_issuance_established: false
```

Primary artifact:

```text
explorations/E164-research-steering-wave0-starter-2026-07-12.md
```

Executable artifact:

```text
tools/research_steering_wave0_starter.py
tests/test_research_steering_wave0_starter.py
tests/artifacts/research_steering_wave0_starter_result.json
```

## Validation

- `python tools/research_steering_wave0_starter.py --output tests/artifacts/research_steering_wave0_starter_result.json`
- `python tests/test_research_steering_wave0_starter.py`
- `python -m py_compile tools/research_steering_wave0_starter.py tests/test_research_steering_wave0_starter.py`
- `python attention/priority_condorcet.py`

## Boundaries

- No claim movement.
- No core hypothesis, North Star, formal object, or claim-ledger changes.
- No physical-source claim and no `TI-C020` reopen.
- No external publication or non-GitHub external action.
