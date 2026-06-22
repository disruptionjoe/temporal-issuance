---
artifact_type: steward_metrics
status: active
governance_role: observation_only_metrics
constitutional: false
---

# Steward Metrics

These metrics are observation-only at launch. They should inform steward judgment but must not become an automatic scoring system without a recorded governance change.

## Signal Categories

| Signal | Why It Matters | How To Observe | Current Baseline |
| --- | --- | --- | --- |
| verdict_movement | Measures whether work changes claim state, kill state, absorber state, or formal precision. | Count runs that update `CLAIM-LEDGER.md`, `memory/path-kills.md`, tests, or formal objects. | W001 weakened TI-C001 and killed one path. |
| workflow_churn | Detects process expansion replacing research progress. | Count workflows created, retired, or revised per 10 runs. | W004 created after assessment; W005 still planned. |
| memory_staleness | Detects stale or misleading memory summaries. | Compare `last_summarized_run` to latest completed run. | Current summary tracks SIM-RUN-005 after this run. |
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

## Use Rules

- Metrics observe. They do not command.
- Do not optimize for metric appearance.
- Add, remove, or redefine metrics only with an entry in `GOVERNANCE-CHANGE-LEDGER.md`.
- If a metric creates bad behavior, weaken or retire it.
