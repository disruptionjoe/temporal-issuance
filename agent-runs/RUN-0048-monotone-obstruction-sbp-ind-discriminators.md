---
artifact_type: agent_run
run_id: RUN-0048
status: complete
phase: 2B
date: 2026-06-22
trigger: manual_accelerated_thin_trigger
governance_role: accelerated_thin_trigger
workflow: W000 -> source_side_witness_fixture (AC-8 / SBP route) + open-obligation discharge
explorations_produced:
  - explorations/E041-monotone-obstruction-sbp-finite-type-space-2026-06-22.md
  - explorations/E042-sbp-ind-verification-concrete-compat-family-2026-06-22.md
  - explorations/E043-ti-c021-entropy-subadditivity-discriminator-2026-06-22.md
  - explorations/E044-ti-c022-bft-tcb-discriminator-2026-06-22.md
  - explorations/E045-d-fork-synthesis-interior-optimum-verdict-2026-06-22.md
obligations_discharged:
  - monotone-obstruction (E039 §11.1) — PROVED under FTS
  - WITNESS-OBL-001 SBP-IND condition (E040 §10.1) — closed in Gödelian regime
  - TI-C021 entropy-subadditivity discriminator — NOT absorbed
  - TI-C022 BFT/TCB discriminator — TI-C022 survives
claims_affected:
  - TI-C019 (D-FORK pivot; PP-3 fork sharpened to a single structural bit)
  - TI-C021 (entropy absorber defeated; formalized as SAX; regime-pinned to FTS)
  - TI-C022 (BFT/TCB absorber defeated; permanent-fork discriminator)
  - TI-C003 (subadditivity requirement on mu now justified, not absorbed)
---

# RUN-0048: Monotone-Obstruction, SBP-IND, and the TI-C021/TI-C022 Discriminators

## Run Summary

This run executes five sequential research goals, each discharging a named open obligation
from the 2026-06-22 prior session (E038–E040, RUN-0047), and then synthesizes a cross-cutting
structural result.

The run follows the source-side-witness route (NEXT-TRIGGER-PLAN primary: AC-8 / SBP witness
class) and simultaneously clears the four obligations carried forward from E039/E040 and the
TI-C021/TI-C022 next_actions registered by RUN-0047.

### Goals and verdicts

1. **Monotone-obstruction proof for SBP Compat under finite type space (E041).**
   The IA-replacement condition named by E039 §11.1. PROVED: the Type-Pool Depletion Lemma
   (each SBP step strictly removes one type from a finite novel-type pool), the
   Monotone-Obstruction Theorem (per-step obstruction probability non-decreasing along SBP
   trajectories), K superlinearity without IA, and the interior-optimum existence theorem
   (Theorem 2) conditional on FTS + type-fairness + C-convexity. The Gödelian regime is the
   precise place the proof breaks, and that break is the signature of open-endedness (D-FTS).

2. **SBP-IND verification for a concrete Compat family (E042).**
   The closure condition for WITNESS-OBL-001 (E040 §10.1). Result: SBP-IND FAILS for every
   finite-type Compat family (forced by E041 Cor 1.1 — only ≤ m SBP morphisms exist, an
   enumerable set), and HOLDS for a concrete Gödelian Compat family (consistency-preserving
   arithmetic constraints) where SBP(S) ≅ {φ independent of Ax(S)} is infinite, non-c.e., and
   PRODUCTIVE. Productivity defeats E040 §7.2's exponential-pre-commitment adversary (not by
   cardinality but by the diagonal escape sentence). WITNESS-OBL-001 fully closes in the
   Gödelian regime, including the infinite-trajectory version.

3. **TI-C021 entropy-subadditivity discriminator (E043).**
   Verdict: NOT ABSORBED. Size-driven subadditivity (concavity of the size functional,
   distribution-free) and correlation-driven entropy subadditivity (mutual-information deficit)
   are formally distinct and logically independent (Disjoint-Independent Discriminator, both
   directions). TI-C021 formalized as the Subadditivity Axiom (SAX); diminishing marginal
   issuance tied to E041 pool depletion as its structural cause. The PP-3 rate discriminator
   (D-RATE) is HONESTLY NARROWED to a consistency check (in FTS the aperture adversary matches
   the size-dependent rate; the genuine PP-3 discriminator is D-FORK, not the rate).

4. **TI-C022 BFT/TCB discriminator (E044).**
   Verdict: TI-C022 SURVIVES. The Permanent-Fork Discriminator exhibits a run (>f Byzantine
   fork, or eternal partition) where each branch record satisfies BFT/TCB integrity but neither
   satisfies TI-C022's continuing-shared-process condition (b). The surplus is real: TI-C022 =
   BFT integrity + a global continuity predicate on the shared process, the second conjunct
   being content BFT is silent about off its fault assumption. Operational reading: condition
   (b) is the ontological fork-choice rule (genuine issuance = canonical-branch records).
   Honest residual objection flagged (verdict-direction surplus vs eventual-synchrony liveness).

5. **Synthesis — D-FORK and the interior-optimum verdict (E045).**
   The four results share one axis: whether the operative source's effective type space is
   finite (FTS) or self-generating (Gödelian). This axis (D-FORK) collapses the diffuse PP-3
   fork — the deepest open question in the program — into a single structural bit with two
   fully-proved, mutually exclusive consequence-sets. TI-C019 is true (source-side issuance)
   iff Gödelian; reduces to bounded projection disclosure iff finite. The interior optimum is
   resolved as a regime property: it exists in FTS, is absent in Gödelian, and its
   non-existence is the formal signature of open-endedness.

### Net advancement

- Four named blocking obligations discharged.
- The interior-optimum existence proof is no longer blocked on the (killed) IA; it is proved
  for the finite regime and correctly fails for the open-ended regime.
- WITNESS-OBL-001 fully closes in the Gödelian regime (with the infinite-trajectory version and
  the exponential-adversary defeat).
- Two standing strongest objections defeated (entropy absorber for TI-C021; BFT/TCB absorber
  for TI-C022); both claims survive at speculative.
- The program's central open problem (PP-3) sharpened from a diffuse fork to a single testable
  structural bit (D-FORK), with the expressiveness threshold as the concrete test target.
- One honest narrowing recorded (D-RATE demoted to consistency check).
- No claim promoted; no claim killed. The operative-source question (FTS vs Gödelian) is
  sharpened, not resolved.

---

## Learning Return

```yaml
run_id: RUN-0048
workflow: W000 -> source_side_witness_fixture + open-obligation discharge
trigger: manual_accelerated_thin_trigger
agent_personas: Repo Steward (inline; no sub-agents — single-surface formal work)
guidance_used:
  - AGENTS.md, REPO-STEWARD.md, METHOD.md, KILL-CRITERIA.md (absorption discipline,
    anti-premature-closure, strongest-version-first)
  - E031 (Ext_S category), E038 (associativity), E039 (IA failure + MO replacement),
    E040 (ORT + SBP-IND), E036 (sublinear mu), E037/RUN-0047 (TI-C021/TI-C022 registration)
  - NEXT-TRIGGER-PLAN (source-side witness primary route)
missing_guidance: none material
confusion_or_conflict: >
  Apparent tension between E041 (finite SBP budget, ≤ m morphisms) and E040 (SBP-IND needs an
  infinite SBP space). Resolved, not papered over: they are opposite sides of the FTS/Gödelian
  fork. The tension was the signal that produced D-FORK.
claims_touched: [TI-C019, TI-C021, TI-C022, TI-C003]
strongest_version_generated: >
  TI-C019 source-side issuance holds in the Gödelian regime, where the SBP space is productive
  and no fixed-source aperture model can reproduce the trajectory (E042).
strongest_objection_found: >
  In the finite regime, the same trajectory is SSC-reproducible, so TI-C019 reduces to bounded
  projection disclosure (E042 §3). Whether the operative source is finite or Gödelian is unsettled.
what_collapsed:
  - IA as the basis for K superlinearity (already killed E039; confirmed unrecoverable)
  - D-RATE as a PP-3 discriminator (narrowed to consistency check, E043 §7)
  - the diffuse form of the PP-3 question (replaced by the single-bit D-FORK)
what_survived:
  - monotone-obstruction (proved under FTS) and interior optimum (regime property)
  - SBP-IND and WITNESS-OBL-001 (closed in Gödelian regime)
  - TI-C021 (entropy absorber defeated; formalized as SAX)
  - TI-C022 (BFT/TCB absorber defeated; permanent-fork discriminator)
what_was_absorbed:
  - finite-type SBP trajectories absorbed by the static-source construction (E042 §3)
  - size-driven subadditivity NOT absorbed by entropy (E043) — recorded as non-absorption
what_was_clarified: >
  The interior optimum, the source-side witness, mu subadditivity, and the PP-3 fork are all
  governed by one axis (finite vs Gödelian effective type space). The program pivot is to
  determine which regime the operative source is in (expressiveness-threshold test).
what_was_promoted: none
path_kills:
  - IA-based superlinearity route (records the unrecoverability; resurrection trigger noted)
  - D-RATE as an independent PP-3 discriminator (narrowed; resurrection trigger noted)
local_minimum_risks: >
  Medium. The FTS/Gödelian dichotomy is clean but the program must not assume the operative
  source is Gödelian just because that is where TI-C019 succeeds. The finite regime (TI-C019
  reduces to projection disclosure) is a live and possibly correct outcome.
category_error_risks: >
  E043 explicitly guards the measure-vs-information category error (mu on realized structure
  vs entropy on a law). E044 guards the integrity-vs-ontology category error (BFT TCB vs
  shared-process continuity). Both are recorded.
recommended_next_run: >
  W000 -> expressiveness_threshold_fixture: determine whether the operative TI source can encode
  its own admissibility predicate (Robinson-Q analog). This decides D-FORK and resolves PP-3.
files_changed:
  - explorations/E041..E045 (5 new)
  - agent-runs/RUN-0048-monotone-obstruction-sbp-ind-discriminators.md
  - CLAIM-LEDGER.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
  - memory/steward-memory-log.md
  - memory/steward-memory-summary.md
  - memory/path-kills.md
  - ROADMAP.md
```

## Run Closeout Checklist

```yaml
run_record_written: yes
memory_log_updated: yes
memory_summary_checked: yes (RUN-0048 section appended)
claim_ledger_checked: yes (TI-C019/C021/C022/C003 updated; RUN-0048 update block added)
roadmap_checked: yes (Phase 2B status note appended)
next_trigger_plan_updated: yes (D-FORK pivot; expressiveness-threshold primary)
path_kills_recorded_if_any: yes (IA-superlinearity, D-RATE-as-discriminator)
export_queue_updated_if_any: n/a (no externally exportable governance artifact this run)
daily_review_updated_if_needed: n/a (no external intake processed)
governance_changes_logged_if_any: n/a (no governance-mechanism change)
metrics_updated: yes (STEWARD-METRICS RUN-0048 row)
vsm_map_checked: yes (no change; research-over-governance posture maintained)
checks_run_or_skipped_with_reason: formal proofs self-checked inline; no code tests in repo
commit_pushed: deferred to maintainer (Joe) — no push without approval
```
