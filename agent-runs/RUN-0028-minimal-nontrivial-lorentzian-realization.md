---
artifact_type: run_record
run_id: RUN-0028
status: complete
governance_role: minimal_lorentzian_realization_attempt
trigger: manual_request
workflow: W000 -> minimal_nontrivial_realization_functor
constitutional: false
claims_touched:
  - TI-C007
  - TI-C009
  - TI-C010
  - TI-C011
---

# RUN-0028: Minimal Nontrivial Lorentzian Realization

## Timestamp

2026-06-21 23:24:04 -05:00

## Trigger

Joe asked to run the target installed by RUN-0027.

## Purpose

Construct or refute a minimal nontrivial realization functor:

```text
F: ExtCat -> LorHist
```

The central question was whether `F` can preserve genuinely load-bearing `Ext_S` structure rather than merely relabeling ordinary Lorentzian histories.

## Work Performed

- Added `explorations/E009-minimal-nontrivial-lorentzian-realization.md`.
- Defined a minimal weighted source-extension category `TI_Ext^Q`.
- Defined a metric-sensitive Lorentzian Moore-curve target `LorHist_g(M)`.
- Constructed a strict functor preserving a same-order/different-extension invariant as proper time.
- Proved that causal-preorder-only realization fails the nontriviality test.
- Evaluated the earned-structure ladder.
- Ran the five-reviewer synthesis requested by RUN-0027.
- Added a claim row for the bounded constructive result.
- Recorded a path kill for treating `F` existence alone as a physical GU/mass-energy bridge.

## Core Result

A minimal nontrivial `F` exists only after strengthening `Ext_S` to a weighted extension category:

```text
Q: Mor(ExtCat) -> ([0, infinity), +)
```

The toy functor maps the morphism weight `Q(e)` to the proper time of a Lorentzian curve:

```text
Tau(F(e)) = alpha Q(e)
```

This preserves a source-side distinction beyond induced order:

```text
same <=_S
different Q
different proper time in LorHist_g
```

## What Collapsed

The following route collapsed:

```text
nontrivial F exists
therefore Temporal Issuance has a physical GU/mass-energy bridge
```

The construction is representational unless the source invariant `Q` is independently earned.

## What Survived

- `Ext_S` as a category-first formal target.
- The RUN-0025 theorem that morphism invariants can exceed induced order.
- A bounded control model showing how a nontrivial Lorentzian realization can be made.
- The RUN-0026 conditional theorem tail, but still only conditional.

## What Was Clarified

The minimal `F` reaches:

```yaml
causal_preorder: yes_for_order_only
metric_sensitive_lorentzian_history: yes_with_external_g_and_Q
action_principle: not_earned
noether_poincare_machinery: not_earned
```

The next hard problem is not constructing another `F`. It is defining `Q` without importing proper time, action, cost, entropy, information, proof length, or resource accounting.

## What Was Promoted

No substrate claim was promoted.

Claim `TI-C011` was added with status `formalizing` for the bounded representational construction.

## New Blockers

`Q` has no independent Temporal Issuance origin. Without one, the minimal functor is absorbed by weighted transition systems, path categories, action accounting, and resource/cost formalisms.

## Recommended Next Run

W000 -> source-invariant audit for `Q`:

```text
Can the extension invariant needed by F be defined source-side before choosing LorHist?
```

If not, archive the GU/mass-energy bridge as a speculative Lorentzian control case.

## Closeout Checklist

```yaml
run_record_written: true
memory_log_updated: true
memory_summary_checked: true
claim_ledger_checked: true
roadmap_checked: true
next_trigger_plan_updated: true
path_kills_recorded_if_any: true
export_queue_updated_if_any: not_applicable
daily_review_updated_if_needed: not_applicable
governance_changes_logged_if_any: not_applicable
metrics_updated: true
vsm_map_checked: true
checks_run_or_skipped_with_reason: git_diff_check_and_ascii_scan_passed
commit_pushed: true
```

## Files Changed

- `explorations/E009-minimal-nontrivial-lorentzian-realization.md`
- `agent-runs/RUN-0028-minimal-nontrivial-lorentzian-realization.md`
- `CLAIM-LEDGER.md`
- `FORMAL-OBJECT.md`
- `ROADMAP.md`
- `agent-governance/NEXT-TRIGGER-PLAN.md`
- `explorations/E008-conditional-lorentzian-realization-theorem.md`
- `memory/path-kills.md`
- `memory/steward-memory-summary.md`
- `memory/steward-memory-log.md`
- `agent-governance/STEWARD-METRICS.md`
