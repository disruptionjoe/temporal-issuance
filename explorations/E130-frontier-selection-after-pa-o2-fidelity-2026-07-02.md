---
artifact_type: exploration
status: complete
governance_role: frontier_selection
workflow: W010
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E126-frontier-selection-after-capability-gate-2026-07-02.md
  - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
  - explorations/E128-internal-predicate-syntax-for-admissibility-2026-07-02.md
  - explorations/E129-enumerator-present-pa-o2-fidelity-2026-07-02.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
created: 2026-07-02
central_run: RUN-20260702-075-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E130: Frontier Selection After PA-O2 Fidelity

## Purpose

Execute W010 after the formal hardening queue selected by E126 has closed:

- E127 bounded the strict c.e. tier as finite-prefix freshness plus
  singleton-enumerator whole-family absorption.
- E128 modeled bounded internal admissibility-predicate syntax and refuted
  universal internal-code acceptance.
- E129 made `EnumeratorPresent` PA-O2-faithful while preserving the existing
  `IssueLC` stack.

The routing question is now:

```text
Given the current repo state, what is the next work that most increases the
chance of reaching the correct verdict on Temporal Issuance?
```

## State Sync

```yaml
latest_run_seen: RUN-0114
memory_current: true_for_latest_delta
next_trigger_current: true
roadmap_current: partially
claim_ledger_current: true_for_status_no_new_movement
surface_tensions:
  - tension_id: hardening_queue_now_closed
    surfaces:
      - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
      - explorations/E128-internal-predicate-syntax-for-admissibility-2026-07-02.md
      - explorations/E129-enumerator-present-pa-o2-fidelity-2026-07-02.md
    description: >
      The three highest-priority formal hardening gates from E126 are now
      closed at the current finite-prefix Lean tier. Continuing to invent
      adjacent interface patches would risk local optimization unless it
      targets a named caveat.
  - tension_id: t8_and_diagname_absorption_still_citation_bound
    surfaces:
      - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
      - formal/lean/OnlineIssuance/Comparator.lean
    description: >
      E121 explicitly says T8 has no independent content for `freshName`, and
      that `diagName`'s name-level absorption remains prose-only. This is now
      the crispest remaining Lean-facing caveat in the formal source route.
  - tension_id: physical_branch_still_candidate_starved
    surfaces:
      - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
      - explorations/E129-enumerator-present-pa-o2-fidelity-2026-07-02.md
    description: >
      The physical/source-formation branch remains central but has no concrete
      candidate supplying source-side admissibility, constructor, or witness
      formation. Another broad physical scout would repeat earlier absorber
      work unless new candidate material appears.
```

## Frontier Candidates

```yaml
- frontier_id: F1
  title: T8 general name-level absorption
  source_refs:
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
    - formal/lean/OnlineIssuance/Comparator.lean
    - formal/lean/OnlineIssuance/Diagonal.lean
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: t8_general_name_absorption
  current_status: live_remaining_formal_caveat
  why_live: >
    The c.e. ceiling, internal predicate syntax, and PA-O2 fidelity gates are
    closed. E121's remaining explicit Lean caveat is that T8 is proved only as
    a double-negation restatement for `freshName`, while `diagName`'s
    name-level absorption is still prose-only.
  success_condition: >
    Machine-check a bounded name-level absorber for `diagName`, ideally via a
    fixed binary-string grammar/family that discloses every finite `diagName`
    output at a known stage, and state whether the broader Nat-to-String
    surjection theorem is needed or unnecessary.
  failure_condition: >
    The run records why the general name-level absorption cannot be made
    precise at the current Lean tier without adding nonlocal libraries or
    changing the model.
  main_absorbers_or_kill_risks:
    - technical cleanup without verdict movement
    - accidentally overclaiming from `freshName` to arbitrary constructions
    - treating countable name disclosure as source issuance
  dependencies:
    - existing Lean modules
  expected_artifact: explorations/E131-t8-general-name-absorption.md

- frontier_id: F2
  title: External Platonist boundary packet
  source_refs:
    - explorations/E090-online-issuance-minimal-constructive-witness-2026-06-25.md
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
    - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
  claim_refs: [TI-C019]
  layer: source
  candidate_workflow: external_platonist_boundary_packet
  current_status: live_but_not_a_lean_proof_target
  why_live: >
    External Platonist completion remains the largest unresolved absorber
    boundary for the formal residue. But prior runs already classified it as
    external navigation rather than an internally formed source object.
  success_condition: >
    Produce a hostile boundary brief separating what `OnlineIssuance^LC`
    establishes internally from what it cannot establish against Platonist
    ontology, without moving claim status.
  failure_condition: >
    The packet becomes philosophy-summary work and adds no sharper run gate.
  main_absorbers_or_kill_risks:
    - attempting to settle an ontological choice by local Lean proof
    - overclaiming a class-relative formal result as a metaphysical defeat
  dependencies:
    - best after the last named Lean caveat is closed
  expected_artifact: hostile_boundary_brief

- frontier_id: F3
  title: Physical source-formation candidate scout
  source_refs:
    - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
    - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
    - explorations/E063-ti-c020-physical-bridge-w1-w6-recheck-2026-06-24.md
  claim_refs: [TI-C020, TI-C019]
  layer: physical_bridge
  candidate_workflow: source_formation_candidate_scout
  current_status: central_but_candidate_starved
  why_live: >
    The long-range North Star is physical, but recent gates leave only a burden:
    a candidate must supply source-side formation rather than capability,
    projection, finality, fixed-H, or access/readout novelty.
  success_condition: >
    Identify a concrete candidate with source-generated admissibility,
    constructor or witness formation, audit trace, and W1-W6 absorber controls.
  failure_condition: >
    No candidate is found and TI-C020 remains parked.
  main_absorbers_or_kill_risks:
    - fixed-H/fixed-A/fixed-Mu completion
    - fixed block universe
    - CSG-style fixed-law growth
    - TaF capability readout
  dependencies:
    - new candidate material or explicit candidate-selection mandate
  expected_artifact: candidate_table_only

- frontier_id: F4
  title: TI-C022 record-reality typing fixture
  source_refs:
    - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
    - explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md
  claim_refs: [TI-C022, TI-C019]
  layer: record_readout
  candidate_workflow: ti_c022_record_reality_typing_fixture
  current_status: parked_secondary
  why_live: >
    TI-C022 still has ontological record-reality surplus after operational
    fork-choice absorption, but it is no longer the central formal source
    bottleneck.
  success_condition: >
    Find a trace where record-reality typing does work not absorbed by
    canonical-chain finality under the same assumptions.
  failure_condition: >
    The surplus is only interpretation, not independent operational content.
  main_absorbers_or_kill_risks:
    - fork-choice / canonical-chain finality
    - BFT / TCB integrity
  dependencies: []
  expected_artifact: ontology_fixture

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
    FUNCTOR/Q obligations remain real, but recent `OnlineIssuance^LC` hardening
    is the active formal route and has a sharper remaining caveat.
  success_condition: >
    Reconnect the finite filtered witness to a current source-side obligation.
  failure_condition: >
    The route remains formal residue without a bridge to verdict movement.
  main_absorbers_or_kill_risks:
    - global normalized Q as hidden completed oracle
    - finite witness overclaiming GU/H3/C3 bridge
  dependencies:
    - renewed bridge candidate
  expected_artifact: bridge_residue_note
```

## Ranked Next Work

```yaml
- rank: 1
  frontier_id: F1
  score_label: highest
  reason: >
    It is the named, bounded, machine-checkable caveat left after the higher
    formal gates were closed. A positive result would prevent citation drift;
    a negative result would precisely bound the remaining name-tier absorption
    claim.
  why_not_higher: already highest
  recommended_workflow: t8_general_name_absorption

- rank: 2
  frontier_id: F2
  score_label: high
  reason: >
    The external Platonist boundary is central to the formal residue's honest
    scope, but it is a boundary/adjudication packet rather than a direct Lean
    proof target. It should follow the last named Lean caveat, not precede it.
  why_not_higher: less executable and easier to overclaim than F1
  recommended_workflow: external_platonist_boundary_packet_after_t8

- rank: 3
  frontier_id: F3
  score_label: medium
  reason: >
    Physical source issuance is central in the long run, but current surfaces
    provide only a burden and no new concrete candidate. Running a scout now
    risks duplicating E112/E125-style candidate work.
  why_not_higher: no source-formation candidate is in hand
  recommended_workflow: source_formation_candidate_scout_only_with_candidate

- rank: 4
  frontier_id: F4
  score_label: medium_low
  reason: >
    TI-C022 remains interesting but is downstream record-reality typing after
    operational absorption, not the current source-side bottleneck.
  why_not_higher: less central to the current formal source route
  recommended_workflow: ti_c022_record_reality_typing_fixture

- rank: 5
  frontier_id: F5
  score_label: low
  reason: >
    The filtered-source/Q obligations remain archived live residue, but without
    a new bridge candidate they are less likely to move verdict than F1.
  why_not_higher: older route, bridge-starved
  recommended_workflow: filtered_functor_q_residue_revisit_only_if_bridge_reopens
```

## Recommended Next Trigger

```yaml
primary_next_trigger:
  workflow_or_run: W000 -> t8_general_name_absorption
  reason: >
    This is the highest-specificity remaining formal caveat after PA-O2,
    internal predicate syntax, and the c.e. comparator are closed. It tests a
    real citation boundary in E121/Comparator.lean without changing claim
    status or reopening TI-C020.
  claim_refs: [TI-C003, TI-C019]
  success_condition: >
    Machine-check a bounded name-level absorber for `diagName` and state the
    exact scope of any broader T8/general-name theorem.
  failure_condition: >
    Record the obstruction and preserve the current citation contract: T8 is a
    `freshName`-construction statement only, while diagonal absorption remains
    semantic/prose-bound.
  expected_artifact: explorations/E131-t8-general-name-absorption-2026-07-02.md
secondary_triggers:
  - workflow_or_run: W000 -> external_platonist_boundary_packet
    reason: Best next boundary packet after the remaining Lean caveat is closed.
  - workflow_or_run: W000 -> source_formation_candidate_scout
    reason: Only if a concrete source-formation candidate is supplied or selected.
  - workflow_or_run: W000 -> ti_c022_record_reality_typing_fixture
    reason: Secondary ontology surplus after source route cleanup.
```

## Merge Recommendations

Update now:

- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `memory/steward-memory-summary.md`
- `ROADMAP.md`
- `explorations/README.md`
- `agent-governance/STEWARD-METRICS.md`
- `agent-runs/RUN-0115-frontier-selection-after-pa-o2-fidelity.md`

Leave unchanged:

- `CLAIM-LEDGER.md`, because W010 routes work and does not adjudicate claims.
- `HYPOTHESIS.md`, `NORTH-STAR.md`, and constitutional/governance posture.
- Lean source, because this run selects the next formal patch rather than
  executing it.

## Verdict

```yaml
w010_complete: true
selected_frontier: F1
primary_next_trigger: t8_general_name_absorption
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
reason_physical_branch_deferred: no_concrete_source_formation_candidate_after_E125_E129
reason_formal_branch_selected: t8_diagname_name_level_absorption_is_the_crisp_remaining_caveat
```
