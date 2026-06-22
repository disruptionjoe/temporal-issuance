---
artifact_type: steward_metrics
status: active
governance_role: observation_only_metrics
constitutional: false
---

# Steward Metrics

These metrics are observation-only at launch. They should inform steward judgment but must not become an automatic scoring system without a recorded governance change.

Warning: do not optimize for these metrics directly. Use them to detect drift, not to define success.

## Per-Run Signal Schema

Each W000 cycle should add or update a compact signal record.

```yaml
run_id:
workflow_used:
research_vs_governance:
claim_status_changed:
path_killed:
path_resurrected:
workflow_created:
workflow_retired:
memory_updated:
next_trigger_updated:
governance_change_made:
hard_output_created:
daily_review_items_added:
estimated_token_intensity:
```

## Signal Categories

| Signal | Why It Matters | How To Observe | Current Baseline |
| --- | --- | --- | --- |
| verdict_movement | Measures whether work changes claim state, kill state, absorber state, or formal precision. | Count runs that update `CLAIM-LEDGER.md`, `memory/path-kills.md`, tests, or formal objects. | W001 weakened TI-C001 and killed one path. |
| workflow_churn | Detects process expansion replacing research progress. | Count workflows created, retired, or revised per 10 runs. | W004 created after assessment; W005 still planned. |
| memory_staleness | Detects stale or misleading memory summaries. | Compare `last_summarized_run` to latest completed run. | Current summary tracks RUN-0009 after this run. |
| governance_research_balance | Detects governance drift or research neglect. | Classify each run as research, governance, mixed, or maintenance. | Recent runs are governance-heavy by design. |
| next_trigger_volatility | Detects unstable priorities. | Track how often `NEXT-TRIGGER-PLAN.md` changes route. | Volatile during launch instrumentation. |
| path_kill_quality | Detects false closure and weak kill records. | Check killed paths for evidence, local-minimum risk, and resurrection trigger. | One path kill recorded cleanly. |
| automation_health | Detects thin-trigger failure. | Track failed commits, dirty exits, missing run records, or push failures. | No failures observed. |
| contributor_signal | Detects unmanaged outside participation. | Track issues, PRs, comments, or external reviews routed into repo state. | No public contribution handling yet. |

## Current Snapshot

```yaml
snapshot_id: MET-0001
run_ref: SIM-RUN-002
verdict_movement: low_but_real
workflow_churn: expected_launch_churn
memory_staleness: current
governance_research_balance: governance_heavy_launch_phase
next_trigger_volatility: expected_launch_volatility
path_kill_quality: acceptable_one_sample
automation_health: healthy
contributor_signal: untested
```

```yaml
snapshot_id: MET-0002
run_ref: SIM-RUN-005
verdict_movement: moderate_absorber_pressure
workflow_churn: high_but_expected_launch_churn
memory_staleness: current
governance_research_balance: recovered_to_research_after_minimal_instrumentation
next_trigger_volatility: adaptive_not_static
path_kill_quality: unchanged_one_sample
automation_health: simulated_clean
contributor_signal: workflow_ready_untested
```

```yaml
snapshot_id: MET-0003
run_ref: RUN-0006
verdict_movement: moderate_governance_assessment_no_new_research_verdict
workflow_churn: high_but_now_should_pause
memory_staleness: current
governance_research_balance: acceptable_if_next_run_is_w002
next_trigger_volatility: adaptive_route_to_w002
path_kill_quality: unchanged_one_sample
automation_health: simulated_clean_actual_hourly_untested_after_changes
contributor_signal: workflow_ready_untested
```

## Per-Run Signal Records

```yaml
run_id: RUN-0007
workflow_used: readiness_pass
research_vs_governance: governance_readiness
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: true
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
```

```yaml
run_id: SIM-VSM-RUN-001
workflow_used: W000 -> system_2_coordination_check
research_vs_governance: governance_audit
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
```

```yaml
run_id: SIM-VSM-RUN-002
workflow_used: W000 -> W003_absorber_gap_scan
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
```

```yaml
run_id: SIM-VSM-RUN-003
workflow_used: W000 -> component_pressure_matrix
research_vs_governance: mixed
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
```

```yaml
run_id: SIM-VSM-RUN-004
workflow_used: W000 -> system_3_star_audit
research_vs_governance: audit
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: medium
```

```yaml
run_id: SIM-VSM-RUN-005
workflow_used: W000 -> system_4_strategy_handoff
research_vs_governance: mixed
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
```

```yaml
run_id: RUN-0008
workflow_used: W004
research_vs_governance: assessment
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
```

```yaml
run_id: RUN-0009
workflow_used: terminology_and_routing_fix
research_vs_governance: governance_maintenance
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: true
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
```

```yaml
run_id: RUN-0010
workflow_used: W000 -> W003_parallel_absorber_gap_pass
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: true
```

```yaml
run_id: RUN-0011
workflow_used: W000 -> primary_source_readiness
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0012
workflow_used: W000 -> W002_component_pressure_pass
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: false
```

```yaml
run_id: RUN-0013
workflow_used: W000 -> definition_repair
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0014
workflow_used: W000 -> toy_patch_test
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0015
workflow_used: cross_repo_context_protocol
research_vs_governance: mixed
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: true
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
parallel_lanes_used: false
```

```yaml
run_id: RUN-0016
workflow_used: W004
research_vs_governance: assessment
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0017
workflow_used: repo_working_assessment
research_vs_governance: assessment
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0018
workflow_used: stale_pointer_closeout
research_vs_governance: maintenance
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
parallel_lanes_used: false
```

```yaml
run_id: RUN-0019
workflow_used: W000 -> issuance_to_finality_bridge_toy_model
research_vs_governance: research
claim_status_changed: false
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0020
workflow_used: taf_persona_divergent_assessment
research_vs_governance: research_assessment
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: high
parallel_lanes_used: false
```

```yaml
run_id: RUN-0021
workflow_used: post_0019_ontology_resolution_recommendations
research_vs_governance: research_routing
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: low
parallel_lanes_used: false
```

```yaml
run_id: RUN-0022
workflow_used: taf_persona_steelman_hegelian_pass
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: high
parallel_lanes_used: false
```

```yaml
run_id: RUN-0023
workflow_used: workflow_packaging
research_vs_governance: research_workflow_packaging
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: true
workflow_retired: false
memory_updated: true
next_trigger_updated: false
governance_change_made: true
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
parallel_lanes_used: false
```

```yaml
run_id: RUN-0024
workflow_used: W000 -> fixture_based_ontology_survivor_competition
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_competitor_lanes
```

```yaml
run_id: RUN-0025
workflow_used: temporal_issuance_gu_mass_energy_steelman
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_specialist_review
```

```yaml
run_id: RUN-0026
workflow_used: conditional_lorentzian_realization_formalization
research_vs_governance: research
claim_status_changed: true
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: medium
parallel_lanes_used: false
```

```yaml
run_id: RUN-0027
workflow_used: tighten_realization_functor_goal
research_vs_governance: research_planning
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: low
parallel_lanes_used: false
```

```yaml
run_id: RUN-0028 (automated)
workflow_used: W000 -> minimal_nontrivial_realization_functor
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_specialist_review
```

```yaml
run_id: RUN-0028 (BDO pass)
workflow_used: W000 -> construct_or_refute_realization_functor (BDO proof)
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_specialist_review
notes: BDO proved in chat environment; applied via Claude Code automation. TI-C009 weakened (energy-momentum route killed). Next trigger replaced with inverted-construction target.
```

```yaml
run_id: RUN-0029
workflow_used: W000 -> inverted_construction_momentum_selection (ICO proof)
research_vs_governance: research
claim_status_changed: true
path_killed: true
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_six_subagent_sections
notes: >
  ICO proved in chat environment; applied via Claude Code automation. The inverted construction
  (last remaining door after BDO) is sealed. LorHist' with momentum-underdetermining objects
  passes covariance (PASS) but fails the mechanism/hidden-variable check (ICO). BDO + ICO
  together seal the Poincare-invariant Lorentzian energy-momentum route. Physical mass-energy
  bridge interpretation archived to NULL-SURVIVOR. TI-C007 weakened, TI-C009 archived,
  TI-C010 archived. TI-C008 formal claim intact (non-order morphism invariants survive as
  formal residue). Next trigger: formal residue documentation or program scope revision.
```

```yaml
run_id: RUN-0030
workflow_used: W007-steelman-and-hegelian-persona-pass
research_vs_governance: research
claim_status_changed: false
path_killed: false
path_resurrected: false
workflow_created: true
  workflow_created_name: W009-heterodox-bridge-incubator
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
daily_review_items_added: true
estimated_token_intensity: very_high
parallel_lanes_used: all_62_personas
notes: >
  Full 62-persona steelman and Hegelian pass against post-BDO/ICO state. Heterodox panel
  synthesis identified 5 constructive routes not yet tried. Holonomy (M1) and BMS soft
  charges (M2) identified as strongest surviving bridge candidates. HYPOTHESIS-STEELMAN.md
  updated with formal-residue-first posture. W009 created. RUN-0031 dispatched immediately.
```

```yaml
run_id: RUN-0031
workflow_used: W009-heterodox-bridge-incubator
research_vs_governance: research
claim_status_changed: true
  new_claims: [TI-C012_speculative, TI-C013_speculative]
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
  artifacts: [RUN-0031, E010-heterodox-bridge-incubator-synthesis]
daily_review_items_added: false
estimated_token_intensity: very_high
parallel_lanes_used: teams_A_B_C_D_E_specialist_divergence
notes: >
  W009 heterodox bridge incubator pass. 9 bridge lemmas (BL-001 through BL-009). BL-003
  SURVIVES (Q_f != p^mu: established physics). BL-007 is the critical open bridge lemma
  (BMS action on ExtCat). BL-004 (holonomy) cleanly evades both BDO and ICO (loop invariant,
  source-defined). 3 toy models (TM-A/B/C) with explicit falsification conditions. No path
  kills from Phase 6. Next: W008 Category G (BMS soft charges).
```

```yaml
run_id: RUN-0032
workflow_used: W000 -> W008_Category_G_BMS_action_attempt
research_vs_governance: research
claim_status_changed: true
  changed_claims: [TI-C013_weakened, TI-C014_added_formalizing]
path_killed: true
  path: BMS_soft_charges_as_independent_source_side_TI_physics_bridge
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
  artifacts: [RUN-0032, E011-bms-action-physics-bridge-attempt]
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: simulated_five_reviewer_synthesis
notes: >
  Constructed ExtCat_BMS as an absorbed BMS/asymptotic-radiative history category. BL-001
  and BL-002 pass only in the absorbed setting; BL-007 fails as an independent Temporal
  Issuance bridge. Next route moved to holonomy.
```

```yaml
run_id: RUN-0033
workflow_used: W000 -> W008_W009_physics_bridge_tree_verdict
research_vs_governance: research
claim_status_changed: true
  changed_claims: [TI-C012_formalizing, TI-C015_added_archived]
path_killed: true
  paths:
    - holonomy_as_independent_physics_bridge
    - deriving_physics_from_current_TI_under_explored_tree
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
  artifacts: [RUN-0033, E012-physics-bridge-tree-verdict]
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: divergent_persona_local_minimum_check
notes: >
  Followed the current W008/W009 bridge tree through BMS, holonomy, TQFT/conformal/quantum
  variants, and divergent-persona checks. Verdict: current Temporal Issuance does not derive
  physics; successful physics-facing realizations import or identify with known physical
  structure. RUN-0034 later qualified this with a conditional CelExt bridge.
```

```yaml
run_id: RUN-0032_appendix
  signal: >
    W008 Category G (BMS soft charges): Detailed four-phase analysis with anti-local-minimum
    gate. Attempts 3.1 (pull-back) and 3.3 (celestial relabeling) killed with precise
    obstructions (ICO'-1). Attempts 3.2 (intrinsic parametrization) and 3.4 (independent BMS
    representation) survive conditionally, requiring S^2-indexed source constraint data
    independently motivated. Anti-local-minimum gate (4 skeptics) confirms local minimum is
    NOT confirmed: Skeptic 4 (celestial holography) opens a genuine live route — ExtCat as
    celestial boundary CFT with BMS acting as boundary symmetry, Q_f as boundary Noether charge,
    independent of bulk Hamiltonian. Category G is NOT killed; status is CONDITIONAL LIVE ROUTE.
    BL-001' (profunctor formulation) identified as weaker alternative to BL-001.
  date: 2026-06-22
  superseded_by: RUN-0034
  current_status: retained_as_appendix_that_opened_the_CelExt_route
```

```yaml
run_id: RUN-0034
workflow_used: W000 -> W008_Category_G_celestial_boundary_bridge
research_vs_governance: research
claim_status_changed: true
  changed_claims: [TI-C013_updated, TI-C015_qualified, TI-C016_added_formalizing]
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
  artifacts: [RUN-0034, E013-celestial-boundary-physics-bridge]
daily_review_items_added: false
estimated_token_intensity: high
parallel_lanes_used: five_reviewer_synthesis
notes: >
  Tested the celestial-boundary route surfaced by the Category G anti-local-minimum pass.
  Verdict: conditional physics bridge possible through independently specified CelExt, but
  current TI primitives do not derive physics. Next trigger: CelExt fixture suite unless
  formal residue documentation is chosen.
```

```yaml
run_id: RUN-0036
workflow_used: research_note_cetext_witness_obligations
research_vs_governance: research
claim_status_changed: true
  new_claims: [TI-C017_speculative, TI-C018_speculative]
path_killed: false
path_resurrected: false
workflow_created: false
workflow_retired: false
memory_updated: true
next_trigger_updated: true
governance_change_made: false
hard_output_created: true
  artifacts: [E014-cetext-witness-obligations-lens-survey, RUN-0036-cetext-witness-obligations]
daily_review_items_added: false
estimated_token_intensity: very_high
parallel_lanes_used: twelve_lens_survey
notes: >
  12-lens witness-obligation survey of candidate CelExt structures. Verdicts: 5 conditional-live
  (B1/B5/B8/B9/B12), 6 bookkeeping (B2/B3/B4/B7/B10/B11), 1 absorbed (B6), 0 live, 0 blocked.
  Strongest near-nontrivial result: B9 (Holonomy/Gauge). Holonomy parallel pair concretely
  executable and cleanly evades BDO and ICO. Two speculative claims added. Next trigger: holonomy
  fixture — specify (C_min, <=_S^min, Ext_S^min) with closed loop and derive induced connection.
```

## Use Rules

- Metrics observe. They do not command.
- Do not optimize for metric appearance.
- Add, remove, or redefine metrics only with an entry in `GOVERNANCE-CHANGE-LEDGER.md`.
- If a metric creates bad behavior, weaken or retire it.
