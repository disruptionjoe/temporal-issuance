---
artifact_type: exploration
status: complete
lane: 1
work_group: FORMAL-ISSUANCE-BYPRODUCTS
result: FAIL_CLOSED_SURVIVOR_INTAKE
claim_status_change: none
---

# E195: Physical Candidate Survivor Intake

## Named blocker

After RUN-0197 corrected the gate scope, the physical campaign still had a
machine-enforcement gap: E194 and the tournament fixture list the survivor
criteria, but candidate intake did not require evidence and falsifiers for
each criterion. A label-only packet could therefore look complete before
substantive adjudication.

## Result

`tools/physical_candidate_survivor_intake.py` implements a fail-closed shape
gate. Every E194 criterion, including physical record preservation, requires a
supplied flag, nonempty evidence reference, and explicit falsifier. The packet
must also name its construction and strongest fixed rival.

A complete synthetic control returns `ADMIT_FOR_ADJUDICATION_ONLY`; it never
establishes physical source issuance. Missing W4 and label-only controls return
`REJECT_INCOMPLETE`.

## Boundary and handoff

This closes only the prose-to-intake enforcement blocker. It does not validate
the truth of evidence, weaken the six criteria, admit candidate 13, reopen
`TI-C020`, move a claim, or replace CompletionClass adjudication. A future
physical candidate must first pass this shape gate, then undergo source,
completion, and observable-separation review.
