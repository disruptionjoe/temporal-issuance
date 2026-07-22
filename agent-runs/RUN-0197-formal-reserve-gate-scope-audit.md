---
artifact_type: steward_run
status: complete
run_id: RUN-0197
lane: A
supports_lane: 1
result: GATE_SCOPE_CORRECTED
---

# Formal Reserve Gate-Scope Audit

## Question

Did the post-tournament six-criteria gate for physical candidate 13 suppress
other work that the authoritative portfolio still marks hourly-eligible?

## Evidence

`agent-governance/NEXT-TRIGGER-PLAN.md` said to return `no_worthy_work` whenever
no six-criteria physical candidate was available. `LANE-STATE.yaml` repeated
that as a Lane-wide default. But `steward/research-portfolio.json` separately
marks `FORMAL-ISSUANCE-BYPRODUCTS` as `hourly_eligible: true`, with activation
only when it closes a named active-lane blocker or no active physical candidate
work is executable. The portfolio also forbids allowing a clean formal result
to replace the physical source question.

## Verdict

`GATE_SCOPE_CORRECTED`. The six survivor criteria remain mandatory for physical
candidate admission. They are not a repo-wide work gate. When no qualifying
physical candidate exists, the steward must rerank the subordinate formal
reserve against its own activation test before returning `no_worthy_work`.

This does not make formal work automatically worthy. A selected action must
name the physical-lane blocker it closes and directly support the campaign;
generic scouts, wrappers, and unrelated clean theorems remain ineligible.

## Changes and nonclaims

The active trigger and Lane state now encode that selection order. No physical
candidate was admitted, no survivor criterion weakened, no claim status moved,
no `TI-C020` reopen occurred, and no external or cross-repo action occurred.

## Handoff

At the next rerank: physical candidate first; if none, identify a concrete
active-lane blocker and test whether one bounded formal-reserve action closes
it. Return `no_worthy_work` only if neither path is executable.
