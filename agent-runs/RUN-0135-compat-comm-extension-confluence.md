---
artifact_type: agent_run
status: complete
run_id: RUN-0135
run_family: repo_progress
created: 2026-07-09
trigger: source_formal_obligation_closure
constitutional: false
---

# RUN-0135: Compat-Comm — Extension Confluence

## Objective

Resolve Compat-Comm, the commutativity property named but left open in E031 I.3 (distinct from
the closed ASSOC-OBL-001).

## Method

Tested the local diamond (two constraints added in both orders) across the three concrete
Compat families (RecCost, Compat_G, SBP forking) on jointly-admissible and forking pairs.

Primary artifact: `explorations/E155-compat-comm-extension-confluence-2026-07-09.md`.

Executable artifacts:

- `tools/compat_comm_extension_confluence.py`
- `tests/test_compat_comm_extension_confluence.py`
- `tests/artifacts/compat_comm_extension_confluence_result.json`

## Result

```yaml
confluent_on_jointly_admissible_pairs: true
forking_pairs_have_no_common_successor: true
fork_locus_equals_SBP_set: true
obligation_discharged: true
claim_status_change: none
```

Ext_S is associative always and commutative off the fork locus; the non-commutativity locus is
coextensive with the SBP witness set.

## Files Changed

- `explorations/E155-compat-comm-extension-confluence-2026-07-09.md`
- `tools/compat_comm_extension_confluence.py`
- `tests/test_compat_comm_extension_confluence.py`
- `tests/artifacts/compat_comm_extension_confluence_result.json`

## Boundaries

No claim status moved. No constitutional, public-posture, mailbox, or external change. Physical
branch untouched.
