---
artifact_type: exploration
status: complete
exploration_id: E153
governance_role: obligation_discharge
workflow: W000
goal_ref: functor_obl_001_n_naturality
date: 2026-07-09
claim_refs:
  - TI-C019
depends_on:
  - explorations/E031-nck-category-morphism-definitions-2026-06-22.md
  - explorations/E042-sbp-ind-verification-concrete-compat-family-2026-06-22.md
  - explorations/E049-gauge-cov-obl-001-distortion-residue-test-2026-06-22.md
  - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
  - tools/functor_obl_001_n_naturality.py
  - tests/test_functor_obl_001_n_naturality.py
central_run: RUN-0133
constitutional: false
claim_status_change: none
verdict: N_IS_NOT_A_STRICT_NATURAL_TRANSFORMATION__IS_GAUGE_NATURAL
---

# E153: FUNCTOR-OBL-001 — N Naturality

## Purpose

Discharge FUNCTOR-OBL-001, the N-naturality obligation named in E031 Part V item 2 and
carried forward (with Q-OBL-001) by E058 as the `FUNCTOR_OBL_001_Q_OBL_001_filtered_source_functor`
trigger. That trigger was never fired because the program then pivoted to the physical
`Adapter_P` branch, which is now parked at `compact_no_worthy_work_until_gate_changes`. The
source-formal obligation is unaffected by that park and is genuinely open.

The obligation: is the novelty rate

```text
N(S) = |D4-Hom(S)| / |Hom(S)|
```

a natural transformation over `Ext_S`, or only a pointwise function `Ob(Ext_S) x R_+ -> [0,1]`?

## Method

A small combinatorial fixture (`tools/functor_obl_001_n_naturality.py`) builds an explicit
`Ext_S` fragment and checks two things:

1. **Strict naturality** requires, at minimum, that the D4 (type-novelty) predicate defining
   N's numerator be preserved along `Ext_S` morphisms. It is not.
2. **Gauge naturality** (the positive residue): invariance of N under type-name relabelings,
   i.e. the schema-relabeling covariance established for the operative predicates by E049
   (GAUGE-COV-OBL-001).

## Result

```yaml
strict_naturality: FALSE
  d4_predicate_preserved_along_morphism: false   # beta novel at S, non-novel at S'
  transport_law_well_defined: false              # two morphisms out of S give different N'
gauge_naturality: TRUE                            # N invariant under type relabeling
obligation_discharged: true
claim_status_change: none
```

The obstruction is exact and structural: **type-novelty is state-relative.** A morphism that
adds a `beta`-typed constraint is D4 at `S` (where `beta` is novel) but is not D4 at
`S' = S + beta` (where `beta` is now present). The predicate that defines N's numerator flips
along the very morphism a naturality square would transport across, so no transport law
`Phi_e` can make N natural. Concretely the fixture exhibits two morphisms departing the same
`S` whose targets carry different novelty rates, so there is no single `Phi_e(N(S))` for the
square to commit to.

## Interpretation (why the negative result is the point)

A strictly natural novelty rate would make novelty a **fixed global invariant** — exactly the
fixed-source / disclosure picture in which "how much is new" is a property of a completed
structure read the same way from every state. The non-naturality of N is therefore the
**categorical fingerprint that separates issuance from disclosure**, and it is the same
non-preservation (types novel relative to `S` becoming non-novel relative to `S'`) that powers
the Godelian mechanism of E042 and the D-FORK discriminator. FUNCTOR-OBL-001 does not weaken
TI-C019; it locates, categorically, the exact place where issuance would differ from a fixed
source.

The positive residue is real: N is **gauge-natural** (invariant under type relabeling), so it
is a well-defined invariant of type *structure*, not type *names* — consistent with E049.

## Assumptions

- The one-step `Hom`-menu is taken over the finite local restriction E031 I.1 permits.
- The D4 predicate is E031's: type novelty relative to the current schema `T_S`.

## Failure risks / what would reopen this

- If a future construction supplies a functor into which N transforms naturally (e.g. N as a
  lax/oplax transformation with explicit coherence cells that recover a transport law), the
  "not natural" verdict would be refined to "not *strictly* natural but laxly natural." The
  current fixture only refutes strict naturality; a lax upgrade is a legitimate future move
  and would not contradict this result.

## Claim-ledger effect

TI-C019: unchanged (`formalizing`). Evidence added that the N component's non-naturality is a
signature of issuance vs disclosure, not a defect. FUNCTOR-OBL-001 marked discharged
(negative for strict naturality, positive for gauge naturality). No status movement.
