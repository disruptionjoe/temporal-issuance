---
artifact_type: agent_run
status: completed
run_id: RUN-0172
run_type: progress
created: 2026-07-16
trigger: TI-PHYSICAL-WITNESS-GENERATION
workflow: repo-progress-run
mode: execute
target: temporal-issuance
objective: test Bose-Einstein condensation as a physical issuance witness
claim_status_change: none
external_action: none
---

# RUN-0172: Bose-Einstein Condensation Candidate v0

## Target

Temporal Issuance `PHYSICAL-ISSUANCE-WITNESS` campaign.

## Objective

Select a non-overlapping physical candidate after RUN-0171 killed Schwinger
pair production, then test whether Bose-Einstein condensation supplies a
source-owned transition law.

## Context Reads

- `AGENTS.md`
- `steward/README.md`
- `agent-governance/REPO-STEWARD.md`
- `agent-governance/REPO-STEWARD-AUTHORITY.md`
- `agent-governance/STEWARDSHIP-RULES.md`
- `memory/steward-memory-summary.md`
- `steward/research-portfolio.json`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `README.md`
- `HYPOTHESIS.md`
- `KILL-CRITERIA.md`
- `CLAIM-LEDGER.md`
- `ROADMAP.md`
- `tests/README.md`
- `steward/runs/2026-07-16-progress-fanout-1408-schwinger-pair-production.md`
- `steward/runs/2026-07-16-progress-fanout-1303-skipped-recent-active.md`
- `steward/runs/2026-07-16-progress-fanout-1205-autocatalytic-reaction-network.md`

## Expected Writable Surfaces

- `tools/bose_einstein_condensation_candidate_v0.py`
- `tests/test_bose_einstein_condensation_candidate_v0.py`
- `tests/artifacts/bose_einstein_condensation_candidate_v0_result.json`
- `explorations/E190-bose-einstein-condensation-candidate-v0-2026-07-16.md`
- `agent-runs/RUN-0172-bose-einstein-condensation-candidate-v0.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `steward/research-portfolio.json`
- `steward/memory-log.md`
- `ROADMAP.md`
- `tests/README.md`

## Recent Run Collision Check

The sync guard passed cleanly on `main`, even with `origin/main` at `86ae166`.
The latest Schwinger local run note still says active but contains a completed
receipt and the corresponding material work is committed and pushed. This run
selects a disjoint many-body phase-coherence candidate class and avoids the
eight killed physical-campaign classes named in RUN-0171.

## Forbidden Actions And Stops

No claim promotion, no `TI-C020` reopen, no E177 mutation, no public posture
change, no CapacityOS root write, no non-GitHub external action, and no
universal physical no-go overclaim.

## Method

Use a deterministic Python fixture to freeze the fixed many-body Hamiltonian
and Fock-space rival before scoring the candidate through Adapter fields,
W1-W6, and CompletionClass v1. Validate the result with focused unittest
coverage and preserve the stable JSON output as the run artifact.

## Result

The candidate is killed as `CANDIDATE_KILLED_FIXED_MANY_BODY_HAMILTONIAN`.
Bose-Einstein condensation is a real physical signal, but it does not supply a
native source law, new mode algebra, new admissibility predicate, construction-
space growth, or W4 non-factorization under preserved density, interference,
coherence, condensate-fraction, temperature, and cooling records. No claim
status changed.

## Files Changed

- `tools/bose_einstein_condensation_candidate_v0.py`
- `tests/test_bose_einstein_condensation_candidate_v0.py`
- `tests/artifacts/bose_einstein_condensation_candidate_v0_result.json`
- `explorations/E190-bose-einstein-condensation-candidate-v0-2026-07-16.md`
- `agent-runs/RUN-0172-bose-einstein-condensation-candidate-v0.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `steward/research-portfolio.json`
- `steward/memory-log.md`
- `ROADMAP.md`
- `tests/README.md`

## Boundaries

No claim promotion, no `TI-C020` reopen, no E177 mutation, no public posture
change, no cross-repo write, and no non-GitHub external action.

## Validation

- `python tools/bose_einstein_condensation_candidate_v0.py`
- `python -m unittest tests/test_bose_einstein_condensation_candidate_v0.py`
- `python -m unittest tests/test_emergent_gauge_sector_candidate_v0.py tests/test_measurement_induced_phase_transition_candidate_v0.py tests/test_crossed_product_gravitational_algebra_candidate_v0.py tests/test_crispr_spacer_acquisition_candidate_v0.py tests/test_dynamic_floquet_code_candidate_v0.py tests/test_prion_conformation_candidate_v0.py tests/test_autocatalytic_reaction_network_candidate_v0.py tests/test_schwinger_pair_production_candidate_v0.py tests/test_bose_einstein_condensation_candidate_v0.py`
- `python -m unittest tests/test_hourly_research_portfolio.py`
- `python -m json.tool steward/research-portfolio.json`
- `python -m json.tool tests/artifacts/bose_einstein_condensation_candidate_v0_result.json`
- `python -m py_compile tools/bose_einstein_condensation_candidate_v0.py tests/test_bose_einstein_condensation_candidate_v0.py`
- `python tools/run_record_schema_audit.py --json agent-runs/RUN-0172-bose-einstein-condensation-candidate-v0.md`
- `git diff --check`
- changed-file absolute-home-path scan

## Next-Work Handoff

- current work: Bose-Einstein condensation candidate v0
- current disposition: ENDPOINT_NEGATIVE
- durable priority owner: Temporal Issuance steward
- recommendation status: advisory

| rank | eligible lane or work item | why now | dependencies / gates |
|---:|---|---|---|
| 1 | `TI-PHYSICAL-WITNESS-GENERATION` | The active campaign still needs a non-overlapping physical source-law candidate after nine killed classes. | Avoid effective-gauge/topological-sector, monitored-dynamics phase-transition, gravitational observer-algebra, CRISPR/adaptive immune sequence-space, dynamic/Floquet scheduled-code, prion-like conformational-templating, autocatalytic reaction-network, Schwinger/vacuum pair-production, and Bose-Einstein-condensation/macroscopic phase-coherence repeats unless their missing source objects appear. |
| 2 | `TI-WHOLE-FAMILY-COMPLETION-TOURNAMENT` | Becomes stronger if candidate generation stalls into a class-level no-go target. | Must avoid universal overclaim beyond declared candidate classes; the tested class remains heterogeneous. |

- recommended next: continue `TI-PHYSICAL-WITNESS-GENERATION`
- switch signal: repeated non-overlapping physical candidates killed by fixed-family completion
- strongest alternative: bounded no-go theorem target for a sufficiently scoped tested family, lower because the current candidate set is still heterogeneous
- overturning evidence: a source-owned condensate mode-generation law with internal anti-after-naming and W4 perturbation non-factorization under preserved density, interference, coherence, condensate-fraction, temperature, and cooling records
- steward reconciliation needed: yes, steward should keep the portfolio excluding killed candidate classes

## Receipt

Result: completed. RUN-0172 killed the Bose-Einstein condensation candidate as
fixed many-body Hamiltonian completion with fixed bosonic field algebra,
Fock-space completion, particle species, trap geometry, interaction strength,
cooling trajectory, reservoir, boundary conditions, seed fluctuations,
measurement access, whole-family, and completed-history absorption. No claims
moved, `TI-C020` remains unopened, E177 was untouched, and no external action
occurred.
