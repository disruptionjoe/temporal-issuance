---
artifact_type: exploration
status: complete
governance_role: frontier_selection
workflow: W010
goal_ref: W010_frontier_selection_after_post_hardening_review
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
  - explorations/E133-frontier-selection-after-external-platonist-boundary-2026-07-02.md
  - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
  - explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md
created: 2026-07-02
central_run: RUN-20260702-080-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E135: Frontier Selection After Post-Hardening Review

## Purpose

Execute W010 after RUN-0119 / E134 completed the post-hardening hostile review.

Routing question:

```text
Given that the Lean-backed OnlineIssuance^LC theorem contract is ready for
bounded repo citation, but FORMAL-OBJECT.md and CLAIM-LEDGER.md integration is
Joe-gated, what is the best automation-safe next work?
```

## State Sync

```yaml
latest_run_seen: RUN-0119
memory_current: true_for_RUN_0119
next_trigger_current_before_this_run: true
roadmap_current: true_for_latest_route
claim_ledger_current: true_for_status_no_new_movement
surface_tensions:
  - tension_id: highest_value_branch_is_joe_gated
    surfaces:
      - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
      - FORMAL-OBJECT.md
      - CLAIM-LEDGER.md
    description: >
      The highest-value formal-source branch is now bounded integration of the
      Lean theorem contract into FORMAL-OBJECT.md and CLAIM-LEDGER.md, but
      E134 explicitly routes that work to Joe and authorizes no status
      promotion or gated-surface edit.
  - tension_id: formal_branch_diminishing_returns
    surfaces:
      - formal/lean/OnlineIssuance/
      - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
      - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
      - explorations/E128-internal-predicate-syntax-for-admissibility-2026-07-02.md
      - explorations/E129-enumerator-present-pa-o2-fidelity-2026-07-02.md
      - explorations/E131-t8-general-name-absorption-2026-07-02.md
      - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
    description: >
      The formal hardening queue is closed enough that another adjacent theorem
      inventory or local caveat pass risks polishing the same bounded result
      instead of moving verdict.
  - tension_id: physical_branch_candidate_starved
    surfaces:
      - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
      - explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md
      - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
      - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
    description: >
      Physical source issuance remains central to the long-range North Star,
      but no current concrete candidate supplies source-side admissibility,
      constructor, or witness formation plus W1 and W4-W6 absorber controls.
      A generic scout now would likely repeat E112/E125.
  - tension_id: record_reality_surplus_is_concrete_and_unrun
    surfaces:
      - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
      - explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md
    description: >
      TI-C022 is not the central source branch, but it has a crisp remaining
      question after fork-choice absorption: can record-reality typing diverge
      from canonical-chain/finality machinery under the same assumptions?
```

## Frontier Candidates

```yaml
- frontier_id: F1
  title: Bounded FORMAL-OBJECT / CLAIM-LEDGER integration
  source_refs:
    - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
    - FORMAL-OBJECT.md
    - CLAIM-LEDGER.md
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: bounded_formal_object_claim_ledger_integration
  current_status: highest_value_but_joe_gated
  why_live: >
    E134 says the theorem contract is ready for bounded repo citation. A
    carefully scoped integration would reduce citation drift and preserve the
    formal result in the two canonical surfaces.
  success_condition: >
    Joe authorizes a no-status-promotion integration and the run records the
    bounded theorem contract without changing public posture or claim status.
  failure_condition: >
    Joe declines or withholds authorization; the repo keeps E134 as the
    citable review packet and selects other automatable work.
  main_absorbers_or_kill_risks:
    - unattended claim movement
    - public posture change
    - treating bounded Lean result as external Platonist or physical defeat
  dependencies:
    - explicit Joe authorization
  expected_artifact: gated_updates_only_if_authorized

- frontier_id: F2
  title: TI-C022 record-reality typing fixture
  source_refs:
    - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
    - explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md
    - memory/steward-memory-summary.md
  claim_refs: [TI-C022, TI-C019]
  layer: record_readout
  candidate_workflow: ti_c022_record_reality_typing_fixture
  current_status: highest_automatable
  why_live: >
    RUN-0057 narrowed TI-C022 to ontological record-reality typing after
    operational fork-choice/canonical-chain absorption. The remaining fixture
    has a concrete discriminator: find a trace where record-reality typing and
    canonical finality diverge under the same protocol assumptions, or record
    that the surplus remains interpretation.
  success_condition: >
    Produce a trace where unique cofinal quorum-legitimate carrier membership
    differs from canonical-chain/finality record membership without changing
    quorum, carrier-selection, or finality assumptions.
  failure_condition: >
    No such trace exists in the tested class; TI-C022 remains operationally
    absorbed, with only an ontological interpretation residue.
  main_absorbers_or_kill_risks:
    - fork-choice / canonical-chain finality
    - quorum validity
    - BFT / TCB integrity
    - record membership as ordinary finality
  dependencies: []
  expected_artifact: explorations/E136-ti-c022-record-reality-typing-fixture-2026-07-02.md

- frontier_id: F3
  title: Physical source-formation candidate scout
  source_refs:
    - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
    - explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md
    - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
  claim_refs: [TI-C020, TI-C019]
  layer: physical_bridge
  candidate_workflow: source_formation_candidate_scout
  current_status: central_but_candidate_starved
  why_live: >
    The physical bridge remains the long-range North Star target, and a real
    candidate would immediately outrank record-readout work. Current repo
    state supplies burden conditions rather than a new candidate.
  success_condition: >
    Identify a concrete candidate with Adapter_P fields, W1-W6 controls,
    intervention/trace evidence, and fixed-source null models.
  failure_condition: >
    No candidate is found; TI-C020 remains parked and the run does not repeat
    the E112/E125 candidate-starvation result.
  main_absorbers_or_kill_risks:
    - fixed-H / fixed-A / fixed-Mu completion
    - fixed block universe
    - CSG-style fixed-law growth
    - TaF capability readout
  dependencies:
    - new candidate material or explicit candidate-selection mandate
  expected_artifact: candidate_table_only_if_nonduplicative

- frontier_id: F4
  title: Theorem-contract inventory or integration proposal
  source_refs:
    - explorations/E134-online-issuance-lc-post-hardening-hostile-review-2026-07-02.md
    - formal/lean/OnlineIssuance/
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: online_issuance_lc_theorem_contract_inventory
  current_status: useful_but_near_duplicate
  why_live: >
    A standalone inventory could help future integration, but E134 already
    records the theorem contract and model limits. Running it now risks
    creating a second integration-adjacent artifact while the canonical edit is
    still Joe-gated.
  success_condition: >
    A compact inventory exposes a concrete missing dependency not already
    stated in E134.
  failure_condition: >
    It repeats E134 and adds coordination weight without verdict movement.
  main_absorbers_or_kill_risks:
    - process churn
    - accidental pressure toward gated edits
  dependencies: []
  expected_artifact: optional_inventory_note

- frontier_id: F5
  title: Filtered-source functor and Q residue revisit
  source_refs:
    - explorations/E060-filtered-source-functor-q-obligation-2026-06-24.md
    - explorations/E061-h3-c1-c3-bridge-from-finite-filtered-functor-2026-06-24.md
  claim_refs: [TI-C017, TI-C012, TI-C019]
  layer: source
  candidate_workflow: filtered_functor_q_residue_revisit
  current_status: older_formal_residue
  why_live: >
    The finite filtered witness remains useful residue, but no current bridge
    candidate makes it more central than the record-reality discriminator.
  success_condition: >
    Reconnect the finite filtered witness to a current source-side obligation.
  failure_condition: >
    The route remains formal residue without verdict movement.
  main_absorbers_or_kill_risks:
    - global normalized Q as hidden completed oracle
    - finite witness overclaiming GU/H3/C3 bridge
  dependencies:
    - renewed bridge candidate
  expected_artifact: bridge_residue_note
```

## Ranked Next Work

```yaml
- rank: blocked_1
  frontier_id: F1
  score_label: highest_but_blocked
  reason: >
    It is the most direct use of the post-hardening result, but E134 and repo
    guardrails make it a Joe-review branch. A scheduled worker must not touch
    FORMAL-OBJECT.md or CLAIM-LEDGER.md.
  why_not_selected: requires_explicit_joe_authorization
  recommended_workflow: bounded_formal_object_claim_ledger_integration_if_authorized

- rank: 1
  frontier_id: F2
  score_label: highest_automatable
  reason: >
    It is concrete, bounded, and falsification-oriented. A negative result
    still teaches something by keeping TI-C022 operationally absorbed rather
    than lingering as vague surplus. It does not require claim movement, public
    posture change, or a new physical candidate.
  why_not_higher: only because F1 is Joe-gated
  recommended_workflow: ti_c022_record_reality_typing_fixture

- rank: 2
  frontier_id: F3
  score_label: medium
  reason: >
    Physical source formation is more central in principle, but the current
    branch is candidate-starved. Without a new candidate, another scout risks
    repeating the existing W1-W6 burden table.
  why_not_higher: no_concrete_candidate_in_hand
  recommended_workflow: source_formation_candidate_scout_only_if_nonduplicative_candidate_exists

- rank: 3
  frontier_id: F4
  score_label: low_medium
  reason: >
    Useful for future integration, but E134 already records the theorem
    contract and the canonical integration remains gated.
  why_not_higher: near_duplicate_of_E134_and_adjacent_to_gated_edits
  recommended_workflow: defer_until_integration_authorized_or_specific_gap_found

- rank: 4
  frontier_id: F5
  score_label: low
  reason: >
    Honest older residue, but bridge-starved and less likely to move verdict
    than the TI-C022 discriminator.
  why_not_higher: no_new_bridge_candidate
  recommended_workflow: filtered_functor_q_residue_revisit_only_if_bridge_reopens
```

## Recommended Next Trigger

```yaml
primary_next_trigger:
  workflow_or_run: W000 -> ti_c022_record_reality_typing_fixture
  reason: >
    The formal-source integration branch is blocked for Joe review and the
    physical branch has no concrete candidate. TI-C022 record-reality typing is
    the best remaining automatable fixture because it has a crisp divergence
    test and a useful failure result.
  claim_refs: [TI-C022, TI-C019]
  success_condition: >
    Find a trace where record-reality typing and canonical-chain/finality
    record membership diverge under the same assumptions.
  failure_condition: >
    Record that the tested TI-C022 surplus remains operationally absorbed by
    canonical-chain/finality machinery and survives only as ontological
    interpretation unless a new trace appears.
  expected_artifact: explorations/E136-ti-c022-record-reality-typing-fixture-2026-07-02.md
secondary_triggers:
  - workflow_or_run: bounded FORMAL-OBJECT / CLAIM-LEDGER integration
    reason: Highest-value branch only if Joe explicitly authorizes it.
  - workflow_or_run: W000 -> source_formation_candidate_scout
    reason: Use only if a concrete nonduplicative physical source-formation candidate is supplied or selected.
  - workflow_or_run: W000 -> online_issuance_lc_theorem_contract_inventory
    reason: Use only if a specific theorem-contract gap is found before integration.
```

## Merge Recommendations

Update now:

- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `memory/steward-memory-summary.md`
- `ROADMAP.md`
- `explorations/README.md`
- `agent-governance/STEWARD-METRICS.md`
- `agent-runs/RUN-0120-frontier-selection-after-post-hardening-review.md`

Leave unchanged:

- `FORMAL-OBJECT.md` and `CLAIM-LEDGER.md`, because integration is Joe-gated.
- `HYPOTHESIS.md`, `NORTH-STAR.md`, and constitutional/governance posture.
- Lean source, because this is a routing pass after formal hardening, not a
  theorem change.
- Public posture and claim statuses.

## Verdict

```yaml
w010_complete: true
selected_frontier: F2
blocked_higher_frontier: F1_bounded_formal_object_claim_ledger_integration
primary_next_trigger: ti_c022_record_reality_typing_fixture
claim_status_change: none
formal_object_or_claim_ledger_edit_authorized: false
physical_source_issuance_established: false
TI_C020_reopened: false
reason_integration_not_selected: joe_review_gate
reason_physical_branch_deferred: no_concrete_source_formation_candidate_after_E125_E134
```
