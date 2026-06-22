---
artifact_type: run_nomenclature
status: active
governance_role: run_identity
constitutional: false
---

# Run Nomenclature

## Purpose

Prevent confusion about whether steward runs are real.

All committed run records are real repository runs. They changed files, updated memory, and were committed and pushed.

## Historical Prefixes

The historical prefixes `SIM-RUN-*` and `SIM-VSM-RUN-*` meant:

> manually accelerated thin-trigger sequence, without waiting for the hourly scheduler.

They did not mean fake runs.

Keep those historical IDs for provenance. Do not rename already-pushed files or commits just to improve terminology.

## Future Naming Rule

Future manual accelerated thin-trigger runs should use ordinary sequential run IDs:

```yaml
run_id: RUN-####
trigger: manual_accelerated_thin_trigger
governance_role: accelerated_thin_trigger
```

Use `scheduled_hourly_trigger` only when the actual hourly automation fires.

Use `manual_request` when Joe asks for a one-off run that is not pretending to be an hourly cycle.

## Assessment Language

Prefer:

- accelerated run sequence
- manual thin-trigger run
- real W000 cycle

Avoid using `simulated` unless the run did not actually update repo state or the output is explicitly hypothetical.
