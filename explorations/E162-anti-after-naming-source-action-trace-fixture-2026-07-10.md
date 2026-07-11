---
artifact_type: exploration
status: complete
governance_role: anti_after_naming_source_action_trace_fixture
workflow: W000
goal_ref: anti_after_naming_source_action_trace_fixture
claim_refs:
  - TI-C012
  - TI-C018
  - TI-C019
depends_on:
  - explorations/E152-adapter-p-no-go-preflight-2026-07-09.md
  - explorations/E160-holonomy-transport-functor-derivation-fixture-2026-07-10.md
  - explorations/E161-capability-transport-source-action-fixture-2026-07-10.md
created: 2026-07-10
central_run: RUN-0141
constitutional: false
claim_status_change: none
---

# E162: Anti-After-Naming Source-Action Trace Fixture

## Purpose

E161 left one positive shape:

```text
nontrivial C-derived transport
+ supported region-indexed task-menu change
+ source-growth witness
+ no TaF readout expression
+ no fixed-completion/access factorization
+ internal anti-after-naming principle
```

This fixture asks whether that shape can be instantiated as a concrete
formal/local trace, or whether it remains only schematic.

## Executable Fixture

Executable artifact:

```text
tools/anti_after_naming_source_action_trace_fixture.py
```

Focused test:

```text
tests/test_anti_after_naming_source_action_trace_fixture.py
```

Result JSON:

```text
tests/artifacts/anti_after_naming_source_action_trace_fixture_result.json
```

## Trace Idea

The positive trace uses a stage-present-name diagonal successor. With stage
names:

```text
alpha, beta
```

the internal rule builds:

```text
diag__alpha__beta
```

The selected continuation is not available in the stage-present name set. The
after-fact singleton adversary can name it after the action, but stage
stratification blocks using that later name as evidence that it was available
at the action stage.

This is the anti-after-naming principle tested here:

```text
availability is evaluated against stage-present names, not after-fact names
```

## Result

```yaml
fixture_complete: true
e161_positive_shape_instantiated: true
concrete_formal_source_action_trace_found: true
physical_source_action_found: false
active_trigger_change: recommend_full_adapter_p_pressure
next_trigger_recommendation: full_adapter_p_pressure_on_stage_stratified_diagonal_trace
claim_status_change: none
```

The stage-stratified diagonal trace receives:

```text
CONCRETE_FORMAL_TRACE_ESCAPES_E161_LOCAL_CONTROLS
```

Controls:

| Case | Verdict |
| --- | --- |
| E161 sector readout | `TAF_EXPRESSIBLE_READOUT` |
| fixed source access | `FIXED_SOURCE_DISCLOSURE` |
| imported oracle novel name | `IMPORTED_STRUCTURE_REJECTION` |
| unguarded diagonal | `SINGLETON_AFTER_NAMING_ABSORBED` |
| verbal guard without trace | `SCHEMATIC_ONLY_NOT_INSTANTIATED` |
| inconsistent transport | `BLOCKED_INCONSISTENT_TRANSPORT` |

## Interpretation

This is a real formal/local trace, not physical evidence.

It improves the frontier because E161's positive shape is no longer merely
verbal. The trace has:

- a nontrivial C-derived transport value;
- a supported task-menu delta;
- source-growth witness shape;
- no TaF readout classification;
- no fixed-source access classification;
- no imported oracle/table;
- a stage-stratified anti-after-naming guard.

But it has not yet passed the full `Adapter_P` gate. It may still fail under
stronger whole-family completion, physical-source, or preservation-map pressure.

## Claim Effect

No claim status moves.

```yaml
TI-C012:
  status: formalizing   # unchanged
  effect: >
    Source-derived transport now has a formal/local source-action trace target,
    but holonomy remains unpromoted and nonphysical until full Adapter_P pressure
    is run.

TI-C018:
  status: weakened      # unchanged
  effect: >
    The prior weakness is narrowed: bare Ext_S still fails, but the C-derived
    transport route now has a concrete local anti-after-naming candidate.

TI-C019:
  status: formalizing   # unchanged
  effect: >
    The source-formal/capability bridge now has a formal/local candidate trace.
    It does not establish physical or operative source issuance; next pressure
    is full Adapter_P.
```

## Next State

Recommended active trigger:

```text
W000 -> full_adapter_p_pressure_on_stage_stratified_diagonal_trace
```

Minimum next-run contract:

1. Treat the E162 trace as formal/local only.
2. Run it through the full `Adapter_P` fields and W1-W6-style source-growth
   pressure.
3. Include TaF readout, fixed-source/access, imported-structure, after-fact
   singleton, and whole-family completion controls.
4. Preserve no claim movement unless the full gate genuinely passes.
