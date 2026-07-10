---
artifact_type: agent_run
status: complete
run_id: RUN-0133
run_family: repo_progress
created: 2026-07-09
trigger: source_formal_obligation_closure
constitutional: false
---

# RUN-0133: FUNCTOR-OBL-001 — N Naturality

## Objective

Discharge FUNCTOR-OBL-001 (N naturality, E031 Part V item 2), an open source-formal obligation
carried forward by E058 and left unexecuted when the program pivoted to the now-parked physical
branch.

## Method

Built a small combinatorial `Ext_S` fixture; checked strict naturality (D4-predicate
preservation along a morphism) and gauge naturality (invariance under type relabeling).

Primary artifact: `explorations/E153-functor-obl-001-n-naturality-2026-07-09.md`.

Executable artifacts:

- `tools/functor_obl_001_n_naturality.py`
- `tests/test_functor_obl_001_n_naturality.py`
- `tests/artifacts/functor_obl_001_n_naturality_result.json`

## Result

```yaml
strict_naturality: false
gauge_naturality: true
obligation_discharged: true
claim_status_change: none
```

N is not a strict natural transformation because type-novelty is state-relative; the
non-naturality is the categorical signature of issuance vs disclosure. N is gauge-natural.

## Files Changed

- `explorations/E153-functor-obl-001-n-naturality-2026-07-09.md`
- `tools/functor_obl_001_n_naturality.py`
- `tests/test_functor_obl_001_n_naturality.py`
- `tests/artifacts/functor_obl_001_n_naturality_result.json`

## Boundaries

No claim status moved. No `FORMAL-OBJECT.md`, hypothesis, public posture, mailbox, or external
system changed. Physical branch untouched.
