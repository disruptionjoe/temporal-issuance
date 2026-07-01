---
artifact_type: agent_run
status: complete
run_id: RUN-0099
created: 2026-07-01
constitutional: false
---

# RUN-0099: OnlineIssuance LC Physical Adapter Contract

## Trigger

Joe instructed:

```text
Do it
```

The active route after RUN-0098 was:

```text
W000 -> online_issuance_lc_physical_adapter_contract
```

## Workflow

Direct contract definition plus executable checker.

## Strongest Version

`OnlineIssuance^LC` might connect to physics only through an adapter:

```text
Adapter_P:
  physical candidate trace ->
    Gamma_n, Adm_n, e_n, w_n, Gamma_{n+1}, tau_n
```

The adapter must import E057's W1-W6 witness gate and defeat fixed-source absorbers.

## Strongest Objection

An adapter contract is a gate, not evidence. A fixed-H or readout candidate can map records
without supplying source growth. TI-C020 cannot reopen until a real candidate passes the gate.

## Execution

```text
python tests/test_online_issuance_physical_adapter_contract.py
python tools/online_issuance_physical_adapter_contract.py --output tests/artifacts/online_issuance_physical_adapter_contract_result.json
```

Result:

```text
5/5 tests passing
```

## What Collapsed

Nothing new collapsed. The contract rejects the negative fixed-H readout control:

```yaml
candidate_id: negative_fixed_h_readout
adapter_contract_passed: false
reason: no W1-W3 source-growth core witness supplied
```

## What Survived

A non-circular adapter contract can be stated:

```yaml
adapter_contract_exists: true
source_growth_core_requires_w1_or_w2_or_w3: true
absorber_control_requires_w4_w5_w6: true
fixed_source_absorber_nulls_defined: true
```

## What Was Promoted

Nothing.

## Files Changed

- `tools/online_issuance_physical_adapter_contract.py`
- `tests/test_online_issuance_physical_adapter_contract.py`
- `tests/artifacts/online_issuance_physical_adapter_contract_result.json`
- `explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md`
- `agent-runs/RUN-0099-online-issuance-lc-physical-adapter-contract.md`
- `tests/README.md`
- `explorations/README.md`
- `FORMAL-OBJECT.md`
- `HYPOTHESIS-STEELMAN.md`
- `ROADMAP.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`

## Recommended Next Run

```text
W000 -> oi_lc_candidate_scout_w1_w6_table
```
