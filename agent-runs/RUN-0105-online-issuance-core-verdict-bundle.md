---
artifact_type: agent_run
status: complete
run_id: RUN-0105
run_family: repo_progress
created: 2026-07-01
fan_out_experiment: true
constitutional: false
---

# RUN-0105: OnlineIssuance Core Verdict Bundle

## Objective

Execute:

```text
W000 -> online_issuance_core_verdict_bundle
```

The run synthesized the E108 machine check, E115 proof-obligation hardening, and E114 Assembly
physical-protocol absorption into a compact current verdict.

## Result

Primary artifact:

```text
explorations/E116-online-issuance-core-verdict-bundle-2026-07-01.md
```

Verdict:

```yaml
core_result: narrowed_formal_local_residue_survives
Issue[S]^LC: true
Issue[S]^physical: false
physical_source_issuance_established: false
external_platonist_absorber_defeated: false
TI_C020_reopened: false
claim_status_change: none
```

## Claim Movement

None.

## Validation

Focused validation:

```text
python -m unittest tests/test_online_issuance_witness_checker.py tests/test_proof_assistant_online_issuance_witness.py
python tools/proof_assistant_online_issuance_witness.py --output tests/artifacts/proof_assistant_online_issuance_witness_result.json
```

## Next Run

```text
W000 -> online_issuance_lc_hostile_review_packet
```

The next run should pressure the formal/local result before any promotion or publishable claim.
