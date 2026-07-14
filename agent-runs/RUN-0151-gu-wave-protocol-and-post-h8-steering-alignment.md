---
artifact_type: agent_run
status: complete
run_id: RUN-0151
run_family: research_steering_method_alignment
created: 2026-07-12
trigger: joe_direct_request
constitutional: false
---

# RUN-0151: GU Wave Protocol and Post-H8 Steering Alignment

## Objective

Inspect `gu-formalization`, where the wave method is actively used, and align
Temporal Issuance steering language with that protocol. Then reconcile the
steering card with the already-executed H6 and H8 runs.

## Method

1. Checked the active GU wave-design and synthesis artifacts.
2. Compared GU's full blind-branch wave pattern to Temporal Issuance focused
   swings.
3. Updated Temporal Issuance steering language and post-H8 attention routing.

## Source Checked

```text
repos/public/gu-formalization/explorations/H59-path2-loop-positivity-blockbuster-wave-design-2026-07-11.md
repos/public/gu-formalization/explorations/path2-wave1-synthesis-and-wave2-design-2026-07-11.md
repos/public/gu-formalization/attention/gu_priority_condorcet.py
```

## Result

The GU protocol distinguishes:

```yaml
full_blind_branch_wave: rival constructions swing once in parallel, blind
orchestrator_synthesis: cross-test adversarial/no-go branch against constructive branches
focused_swing: next pass after a wave converges to one decisive target
```

Temporal Issuance changes:

- Added the GU-style full wave protocol to the research-steering card.
- Clarified that E169/H9 was a focused swing, not a full blind-branch wave.
- Added a decision rule to the H6 trigger: choose full blind-branch wave only if
  H6 has rival constructions; otherwise run a focused discriminator swing.
- Marked H6 and H8 as resolved dependencies in the steering card after the
  concurrent progress fan-out completed them.
- Replaced stale H6/H8 priority-engine items with post-H8 restart routes:
  sharper theorem target, new H7-admitted packet intake, intentional follow-on
  gate selection, and W000 gate-change wait.
- Corrected this governance run record to avoid colliding with the H6
  `RUN-0149` record.

## Files Changed

- `attention/research-steering-card.md`
- `attention/priority_condorcet.py`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `agent-runs/RUN-0151-gu-wave-protocol-and-post-h8-steering-alignment.md`

## Validation

- `python attention/priority_condorcet.py`
- `python tests/test_run_record_schema_audit.py`
- `python tools/run_record_schema_audit.py agent-runs` exits 0 with legacy warnings only.
- `git diff --check`

## Boundaries

- No claim movement.
- No core hypothesis change.
- No physical-source claim.
- No `TI-C020` reopen.
- No external publication or non-GitHub external action.
