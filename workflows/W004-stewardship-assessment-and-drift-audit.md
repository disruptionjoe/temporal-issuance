---
artifact_type: workflow
workflow_id: W004
status: active
governance_role: stewardship_assessment
constitutional: false
design_hypothesis: Stewardship assessment improves mission alignment when invoked by need rather than fixed cadence.
---

# W004: Stewardship Assessment And Drift Audit

## Purpose

Assess whether the repository architecture, stewardship model, memory structures, workflow design, prioritization mechanisms, and governance philosophy are helping or hindering the mission.

This workflow is reusable. It is not tied to a fixed cadence. The Repo Steward invokes it when the current state suggests that governance, memory, workflow behavior, or steward alignment may be affecting verdict quality.

W004 supports:

- deep assessment
- light assessment
- drift audit
- multi-run lookback
- VSM-style viability check when relevant
- changeable persona set
- changeable questions
- reusable synthesis format

## Trigger Conditions

Possible triggers include:

- several runs produce conflicting priorities
- repeated path kills
- memory drift or stale summaries
- large governance changes
- before changing workflow structure
- after high token usage or run failures
- after a human review note
- after a major claim status change
- steward uncertainty
- contributor confusion
- signs of workflow churn
- signs of excessive caution
- signs of research/governance imbalance
- periodic cadence, if later justified by evidence

This list is not exhaustive. The steward may invoke W004 whenever a stewardship assessment is the highest expected learning move.

## Input Surfaces

Required:

1. `AGENTS.md`
2. `workflows/W000-repo-steward-cycle.md`
3. `agent-governance/REPO-STEWARD.md`
4. `agent-governance/NEXT-TRIGGER-PLAN.md`
5. `memory/steward-memory-summary.md`
6. `memory/steward-memory-log.md`
7. `CLAIM-LEDGER.md`
8. `ROADMAP.md`
9. all run records in the chosen lookback window
10. workflow files touched during the lookback window

Optional when relevant:

- `memory/path-kills.md`
- `memory/export-queue.md`
- `memory/daily-review/`
- `memory/daily-briefs/`
- `agent-governance/GOVERNANCE-CHANGE-LEDGER.md`
- `agent-governance/STEWARD-METRICS.md`
- `agent-governance/VSM-MAP.md`
- `agent-governance/RUN-CLOSEOUT-CHECKLIST.md`
- `personas/`
- `governance-package/`
- open issues, pull requests, or contributor inputs, when available

## Default Persona Set

Use these personas unless the steward records a reason to change the mix:

1. Philosophy of Science Researcher
2. Open Source Governance Architect
3. Complexity Scientist
4. Systems Engineer
5. Product Manager
6. Founder / Startup Operator
7. Institutional Economist
8. Mathematician
9. AI Alignment / Agent Governance Researcher
10. Church of AI Steward

The persona set may evolve. Additions, removals, replacements, or split versions must be recorded in `agent-governance/GOVERNANCE-CHANGE-LEDGER.md` once that ledger exists. Until then, record the rationale in the run record.

## Assessment Questions

Default questions for every persona:

1. What is the strongest aspect of the current repo design?
2. What is the weakest aspect of the current repo design?
3. What assumption is currently hidden but likely important?
4. What local minimum is most likely?
5. What governance failure mode is most likely?
6. What research failure mode is most likely?
7. What memory failure mode is most likely?
8. What contributor-management failure mode is most likely?
9. What should the steward learn as quickly as possible?
10. What should the steward delay deciding?
11. What should become constitutional later?
12. What should definitely not become constitutional?
13. What workflows are missing?
14. What workflows should probably be deleted?
15. What metrics or signals should the steward track?
16. What is one thing the steward is currently overestimating?
17. What is one thing the steward is currently underestimating?
18. What would cause you to redesign the architecture entirely?
19. What would success look like after 3 months?
20. What would success look like after 1 year?

Question set changes are allowed. The steward may add, remove, replace, split, or specialize questions when the assessment design itself appears to be limiting learning. Record the rationale.

## Lookback Window

Default lookback:

- since the last W004 run, or
- the last 5 steward cycles, whichever is more informative.

For launch or after major changes, the steward may widen the window to include all relevant prior runs. For lighter checks, the steward may narrow the window to the current failure or drift signal.

The chosen lookback window must be named in the assessment output.

## VSM Readiness Questions

When W004 is invoked after a multi-run sequence or viability concern, answer:

1. Did W000 behave like a steward or a checklist?
2. Did System 5 identity remain stable?
3. Did System 1 operations produce hard outputs?
4. Did System 2 coordination prevent conflicting state?
5. Did System 3 control catch inconsistency?
6. Did System 3* audit reveal anything the steward missed?
7. Did System 4 intelligence improve future options?
8. Did memory preserve learning without becoming policy?
9. Did governance instrumentation help or become ceremony?
10. Did the steward move research forward?
11. Did the steward get too cautious?
12. Did the steward over-focus on governance?
13. Did the steward under-focus on governance?
14. What should change immediately?
15. What should explicitly not change yet?
16. What should go to Joe for human review?
17. What should the next real hourly trigger do?
18. What should the steward watch over the next 24 hours?

## Output Format

Every W004 run produces two artifacts:

1. Output A: normal Markdown report.
2. Output B: the exact same report inside one Markdown code block.

The report must include:

- scope and lookback window
- per-persona findings or a clearly justified lighter variant
- synthesis
- major agreements
- major disagreements
- hidden assumptions
- local-minimum risks
- governance risks
- governance strengths
- research risks
- memory risks
- recommended immediate changes
- recommended delayed changes
- things to explicitly leave alone
- highest-leverage next actions
- governance lessons worth exporting
- open questions for Joe

## Synthesis Requirements

The synthesis must separate:

- what the steward should do now
- what the steward should delay
- what the steward should explicitly not change
- what should be routed to daily human review
- what should become reusable governance

It must identify whether W000 is behaving like an adaptive steward or a static checklist.

## Governance Memory Updates

After W004, update as applicable:

- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `ROADMAP.md`
- `CLAIM-LEDGER.md` if governance claims change
- `memory/export-queue.md` if reusable lessons appear
- `memory/daily-review/` if uncertainty or Joe guidance is needed
- `agent-governance/GOVERNANCE-CHANGE-LEDGER.md` if assessment design changes
- `agent-governance/STEWARD-METRICS.md` if metrics are added or revised
- `agent-governance/VSM-MAP.md` if viability surfaces change

## Daily Review Routing

Add items to the daily review list when:

- the steward is uncertain about a major governance choice
- a constitutional object may need to be added
- contributor legitimacy is unclear
- a workflow or persona should maybe be retired
- W000 appears to be drifting
- the steward may be too cautious or too autonomous
- a governance change might slow research substantially

## Design Hypothesis

W004 itself is a governance hypothesis:

> Stewardship assessment improves mission alignment when invoked by need, using diverse personas and explicit synthesis, without becoming a recurring ceremony.

Future W004 runs should test this hypothesis. If W004 becomes too heavy, split it into lighter and deeper versions. If it becomes too vague, add sharper questions. If it becomes too ceremonial, retire or narrow it.
