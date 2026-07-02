---
artifact_type: exploration
status: active
governance_role: frontier_selection
workflow: W010
claim_refs:
  - TI-C001
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
  - explorations/E123-everett-fixed-unitary-source-absorber-gauntlet-2026-07-02.md
  - explorations/E124-relativistic-block-universe-absorber-gauntlet-2026-07-02.md
  - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
created: 2026-07-02
central_run: RUN-20260702-070-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E126: Frontier Selection After Capability Gate

## Purpose

Execute W010 after the Everett, block-universe, and capability-typed `Ext_S`
gates.

The prior three gates closed the current physical/capability shortcut: region
task-menu differences are real comparison data, but they are not source
issuance unless a candidate supplies source-side admissibility, constructor, or
witness formation. W010 now asks what work most increases verdict movement
without repeating that negative gate.

## State Sync

```yaml
latest_run_seen: RUN-0110
memory_current: partially
next_trigger_current: true
roadmap_current: partially
claim_ledger_current: true_for_status_no_new_movement
surface_tensions:
  - tension_id: memory_and_roadmap_lag_recent_gate_sequence
    surfaces:
      - memory/steward-memory-summary.md
      - ROADMAP.md
    description: >
      Older sections still foreground W010-after-RUN-0081 and physical adapter
      campaign routes, while E120 through E125 have already hardened
      OnlineIssuance^LC and then absorbed the latest physical/capability exits.
  - tension_id: physical_branch_has_burden_but_no_candidate
    surfaces:
      - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
      - agent-governance/NEXT-TRIGGER-PLAN.md
    description: >
      E125 states the exact source-formation burden, but no concrete physical
      or region-supported candidate currently supplies the needed constructor,
      admissibility predicate, or witness relation.
```

## Frontier Candidates

```yaml
- frontier_id: F1
  title: Strict c.e. comparator for OnlineIssuance^LC
  source_refs:
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
    - formal/lean/OnlineIssuance/Comparator.lean
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: online_issuance_lc_ce_tier_comparator
  current_status: live_open_tier
  why_live: >
    E121 derives the comparator result only for total Nat-indexed families.
    The strict c.e. tier remains open and directly tests the strongest formal
    source residue.
  success_condition: >
    A Lean-backed partial-computability/c.e. model proves a precise
    escape/absorption pair or a bounded no-go.
  failure_condition: >
    The c.e. tier collapses into a classical ceiling or requires assumptions
    that show the current formal residue is weaker than advertised.
  main_absorbers_or_kill_risks:
    - external Platonist completion
    - partial-computability nontermination and enumeration-order effects
    - classical existence without internal computable construction
  dependencies:
    - Lean toolchain
    - likely mathlib computability support
  expected_artifact: explorations/E127-online-issuance-lc-ce-tier-comparator.md

- frontier_id: F2
  title: PA-O2-faithful enumerator presence
  source_refs:
    - explorations/E120-online-issuance-lc-lean-core-encoding-2026-07-02.md
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: enumerator_present_pa_o2_fidelity
  current_status: live_hardening
  why_live: >
    Core's `EnumeratorPresent` is intentionally weaker than the Python PA-O2
    fixture. Strengthening it would remove a documentation caveat.
  success_condition: >
    Symbol registration, kind discipline, and totality flag are added in a
    successor interface module and the diagonal derivation replays.
  failure_condition: >
    The stronger predicate exposes a hidden dependency in the Lean bridge.
  main_absorbers_or_kill_risks:
    - hygiene-only work crowding out the harder c.e. tier
  dependencies:
    - existing Lean modules
  expected_artifact: formal/lean/OnlineIssuance/PAO2.lean

- frontier_id: F3
  title: Internal admissibility predicate syntax
  source_refs:
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: internal_predicate_syntax_for_admissibility
  current_status: live_deeper_formalization
  why_live: >
    E121 derives self-encoding for `AdmDef`, but the predicate is still a
    meta-level Lean predicate. Internal syntax would test the Godel-style
    reading more directly.
  success_condition: >
    Admissibility predicates become internal objects with a checked
    self-application or obstruction theorem.
  failure_condition: >
    Internalization adds only presentation overhead or reintroduces
    assumptions the current fixture avoided.
  main_absorbers_or_kill_risks:
    - category/context presentation absorption
    - meta-level proof mistaken for internal source formation
  dependencies:
    - stable comparator and PA-O2 interface choices
  expected_artifact: formal/lean/OnlineIssuance/PredicateSyntax.lean

- frontier_id: F4
  title: T8 general name-level absorption
  source_refs:
    - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
  claim_refs: [TI-C003, TI-C019]
  layer: source
  candidate_workflow: t8_general_name_absorption
  current_status: live_but_secondary
  why_live: >
    E121 flags T8 as a double-negation restatement for `freshName` only, with
    the `diagName` name-level absorption still prose-only.
  success_condition: >
    The `Nat -> String` surjection statement and name-level diagonal
    absorption are machine checked.
  failure_condition: >
    The result remains only a presentation cleanup with no changed comparator
    verdict.
  main_absorbers_or_kill_risks:
    - technical cleanup without verdict movement
  dependencies:
    - existing Lean comparator module
  expected_artifact: formal/lean/OnlineIssuance/Comparator.lean

- frontier_id: F5
  title: Physical source-formation candidate scout
  source_refs:
    - explorations/E123-everett-fixed-unitary-source-absorber-gauntlet-2026-07-02.md
    - explorations/E124-relativistic-block-universe-absorber-gauntlet-2026-07-02.md
    - explorations/E125-capability-typed-ext-s-surplus-test-2026-07-02.md
  claim_refs: [TI-C020, TI-C019]
  layer: physical_bridge
  candidate_workflow: source_formation_candidate_scout
  current_status: burden_only_no_candidate
  why_live: >
    The physical ambition remains central, but the latest gate supplies only a
    burden: source formation must be shown, not merely capability change.
  success_condition: >
    A concrete candidate states region support, `construct(w)`-type task,
    source-side formation, audit trace, and absorber controls.
  failure_condition: >
    The scout finds no candidate and records TI-C020 as still parked.
  main_absorbers_or_kill_risks:
    - fixed block completion
    - CSG-style fixed-law growth
    - fixed-source aperture disclosure
    - TaF capability readout
  dependencies:
    - new candidate material or a deliberate candidate-scout run
  expected_artifact: exploratory_candidate_table_only
```

## Ranked Next Work

```yaml
- rank: 1
  frontier_id: F1
  score_label: highest
  reason: >
    It tests the exact open tier left by the strongest formal result. A
    positive or negative outcome would materially sharpen TI-C019's formal
    residue, while the physical branch currently has only a burden and no
    candidate.
  why_not_higher: already highest
  recommended_workflow: online_issuance_lc_ce_tier_comparator

- rank: 2
  frontier_id: F3
  score_label: high
  reason: >
    Internal predicate syntax would attack the next deepest formal caveat, but
    it is more design-heavy and less directly tied to the open computability
    tier than F1.
  why_not_higher: c.e. comparator is crisper and more decisive now
  recommended_workflow: internal_predicate_syntax_for_admissibility

- rank: 3
  frontier_id: F2
  score_label: medium_high
  reason: >
    PA-O2 fidelity is clean, bounded, and likely useful, but mostly removes a
    stated interface caveat rather than testing a central absorber.
  why_not_higher: hardening rather than verdict movement
  recommended_workflow: enumerator_present_pa_o2_fidelity

- rank: 4
  frontier_id: F5
  score_label: medium
  reason: >
    The physical bridge is central in the long run, but the latest three gates
    just showed that capability/readout differences are not enough. Running a
    new physical gate without a concrete candidate would duplicate absorber
    work.
  why_not_higher: no source-formation candidate is currently in hand
  recommended_workflow: source_formation_candidate_scout_only_after_candidate

- rank: 5
  frontier_id: F4
  score_label: medium_low
  reason: >
    T8/general name-level absorption is a real caveat but less central than the
    strict c.e. tier and internal predicate syntax.
  why_not_higher: mostly closes a citation/hygiene gap
  recommended_workflow: t8_general_name_absorption
```

## Recommended Next Trigger

```yaml
primary_next_trigger:
  workflow_or_run: W000 -> online_issuance_lc_ce_tier_comparator
  reason: >
    This is the highest-verdict, most specific continuation after E121 and the
    correct pivot after E125's physical/capability branch found no source
    formation candidate.
  claim_refs: [TI-C003, TI-C019]
  success_condition: >
    Prove or precisely bound the escape/absorption pair for a strict c.e. or
    partial-computability model, carrying the model-boundary label in the
    theorem and prose.
  failure_condition: >
    Record the obstruction or classical ceiling that prevents the c.e. tier
    from supporting the OnlineIssuance^LC residue.
  expected_artifact: explorations/E127-online-issuance-lc-ce-tier-comparator.md
secondary_triggers:
  - workflow_or_run: W000 -> internal_predicate_syntax_for_admissibility
    reason: Deepest remaining formalization after the computability tier.
  - workflow_or_run: W000 -> enumerator_present_pa_o2_fidelity
    reason: Bounded interface hardening if the c.e. tier is too dependency-heavy.
  - workflow_or_run: W000 -> source_formation_candidate_scout
    reason: Only if a concrete physical candidate is supplied or selected.
```

## Merge Recommendations

Update now:

- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `memory/steward-memory-summary.md`
- `explorations/README.md`
- `agent-governance/STEWARD-METRICS.md`
- `agent-runs/RUN-0111-frontier-selection-after-capability-gate.md`

Leave unchanged:

- `CLAIM-LEDGER.md` because W010 does not adjudicate claims.
- `ROADMAP.md` because the route change is already captured in the trigger
  plan and memory; roadmap sections can be compressed in a dedicated
  stewardship pass.
- `HYPOTHESIS.md`, `NORTH-STAR.md`, and constitutional/governance posture.

## Verdict

```yaml
w010_complete: true
selected_frontier: F1
primary_next_trigger: online_issuance_lc_ce_tier_comparator
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
reason_physical_branch_deferred: no_concrete_source_formation_candidate_after_E125
reason_formal_branch_selected: strict_ce_tier_is_open_specific_and_central
```
