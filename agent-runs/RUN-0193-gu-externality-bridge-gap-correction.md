---
artifact_type: agent_run
status: completed
run_id: RUN-0193
run_type: stewardship
lane: A
created: 2026-07-21
trigger: capacityos_cai_repository_work_cycle_child
workflow: repository-work-cycle
mode: execute
target: temporal-issuance
parent_run: RUN-20260721-103650-repository-work-cycle-cai-hourly
objective: correct the over-attributed interpretation of TI commit 2a76c69
claim_status_change: none
external_action: github_push_only
---

# RUN-0193: GU Externality Bridge-Gap Correction

## Evidence

Committed GU correction `a0a140186d856d92990e4b3eaa515e902d7d874f`
hostile-verifies TI's `InvariantValuation` definition. `alpha` acts only on the
codomain, so `no_invariant_valuation` proves that no map has pointwise
alpha-fixed outputs when alpha is fixpoint-free. It does not define a domain
action and does not exclude an alpha-equivariant sigma-reader.

Later committed GU revisions through `bf2b9416c583e27f9f73c454243e101b9ab9c12b`
do not close that bridge. Uncommitted GU working-tree files were not read or
used.

## Disposition

TI commit `2a76c6906ffe56bf5247e71f862a9da94858e41c` remains mathematically valid
for its literal codomain conjunct. Its physical/GU interpretation required a
bounded correction:

- retain theorem bodies and historical API names;
- relabel the result as a codomain fixed-output fact;
- state that the Bool witness is generic, not a typed GU reader instance;
- leave open the domain-side bridge that every internal sigma-supplier belongs
  to the alpha-even observable class; and
- do not treat eigenspace completeness as that bridge.

The substantive "GU cannot internally read sigma" claim remains conditional
on the bridge and the separately verified domain-side Schur/zero-capacity
result. The self-closure, product-uniformity, and typed TaF-retraction
obligations also remain open.

## Result

```yaml
result: progressed
primary_purpose: stewardship_due
lane: A
correction_source: a0a140186d856d92990e4b3eaa515e902d7d874f
ti_commit_corrected: 2a76c6906ffe56bf5247e71f862a9da94858e41c
lean_theorem_body_changed: false
literal_codomain_result_valid: true
gu_internal_reader_result_proved: false
domain_alpha_even_bridge_status: open
claim_status_change: none
physical_candidate_13_admitted: false
heavy_job_run: false
dirty_gu_partial_files_consumed: false
```

## Validation Boundary

No Lean/Lake command ran. Validation is documentation/static consistency,
JSON/YAML parsing, and `git diff --check`. No claim, canon, physical candidate,
CompletionClass, Lane 1 control, or non-GitHub external surface changed.
