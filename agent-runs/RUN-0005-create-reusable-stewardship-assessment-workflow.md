---
artifact_type: run_record
status: complete
governance_role: workflow_creation
run_id: RUN-0005
trigger: manual_request
workflow: W000 -> create_reusable_stewardship_assessment_workflow
constitutional: false
---

# RUN-0005: Create Reusable Stewardship Assessment Workflow

## Summary

Converted the prior one-time stewardship assessment prompt into a reusable workflow: `workflows/W004-stewardship-assessment-and-drift-audit.md`.

## Decision

W004 should not run on a fixed five-cycle cadence by default. It should run when W000 judges stewardship assessment to be the highest expected learning move.

## What Changed

- Added reusable purpose, trigger conditions, input surfaces, persona set, assessment questions, lookback guidance, output format, synthesis requirements, memory updates, daily review routing, and design-hypothesis language.
- Updated `workflows/README.md` to register W004.

## What Was Clarified

The assessment design itself is a governance hypothesis. The steward may change personas, questions, lookback windows, synthesis format, or split W004 into lighter and deeper variants, but changes must be recorded with rationale.

## Recommended Next Run

Enter W000 for SIM-RUN-001. Current W000 recommendation remains minimal governance instrumentation before W003.

