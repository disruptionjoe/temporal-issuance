---
artifact_type: exploration
status: complete
exploration_id: E155
governance_role: obligation_discharge
workflow: W000
goal_ref: compat_comm_extension_confluence
date: 2026-07-09
claim_refs:
  - TI-C019
depends_on:
  - explorations/E031-nck-category-morphism-definitions-2026-06-22.md
  - explorations/E038-assoc-obl-001-composition-associativity-proof-2026-06-22.md
  - explorations/E042-sbp-ind-verification-concrete-compat-family-2026-06-22.md
  - tools/compat_comm_extension_confluence.py
  - tests/test_compat_comm_extension_confluence.py
central_run: RUN-0135
constitutional: false
claim_status_change: none
verdict: COMPAT_COMM_HOLDS_OFF_FORK_LOCUS__FORK_LOCUS_EQUALS_SBP_SET
---

# E155: Compat-Comm — Extension Confluence and the Fork Locus

## Purpose

Resolve Compat-Comm, the commutativity property named but left open in E031 I.3. ASSOC-OBL-001
(associativity of composition) was closed unconditionally by E038, but E031 explicitly
preserved the *distinct* property

```text
Compat-Comm:  Compat(c2, X u {c1}, S) == Compat(c1, X u {c2}, S)
```

as an open named condition. It governs whether `Ext_S` has **order-independent admissibility**
— a local diamond / Church-Rosser property: does the reachable admissible state depend on the
order in which two constraints are added?

## Method

`tools/compat_comm_extension_confluence.py` tests the local diamond (adding two constraints in
both orders from a base state) across the three concrete Compat families in the repo:

- **RecCost-derived admissibility** (E031 II.3): a size/cost check, set-based.
- **Compat_G** (E042 4.1): consistency preservation, `Ax(S) u {c1,c2}` consistent.
- **SBP forking guard** (E031 III.1): forking extensions with no common admissible successor.

Two pair types are exercised: a jointly-admissible pair (two distinct novel propositions) and
a forking pair (same proposition site, opposite polarity — phi vs not-phi).

## Result

```yaml
confluent_on_jointly_admissible_pairs: true      # all three families
forking_pairs_have_no_common_successor: true     # godelian and sbp families
reccost_size_family_never_forks: true            # pure size admits no forks
obligation_discharged: true
claim_status_change: none
```

The verdict is sharp: **Compat-Comm holds exactly on jointly-admissible pairs and fails
exactly on forking (SBP) pairs.** Each forking pair has both single steps admissible but no
common successor (the fixture confirms `common_successor is None` for the Godelian/SBP fork).
Pure-size families (RecCost) never fork, consistent with their absorbability into ordinary
resource accounting.

## Interpretation

The non-confluence locus is **coextensive with the SBP fork set** `SBP(S)`. Extension
non-commutativity is therefore not a defect to be repaired; it is the formal content of
"issuance forks the schema." `Ext_S` is a confluent category *off* the fork locus, and the
fork locus is precisely the source-side witness set that carries the D-FORK / WITNESS-OBL-001
machinery (E040, E042). This unifies three previously separate threads:

- ASSOC-OBL-001 (closed, E038): composition is always associative;
- Compat-Comm (this note): composition commutes exactly off the fork locus;
- SBP / D-FORK (E040/E042): the fork locus is where source-side issuance lives.

So the categorical structure of `Ext_S` is: **associative always, commutative off `SBP(S)`,
and the failure of commutativity marks exactly the morphisms that are candidate source-side
issuance events.**

## Assumptions / scope

- "Inconsistency" for Compat_G is modeled as asserting both polarities of the same proposition
  site — the minimal concrete realization of E042's consistency predicate. Richer arithmetic
  inconsistency is a superset of this locus, so the fork-locus containment is conservative.

## Failure risks / what would reopen this

- If a Compat family is exhibited whose non-confluence locus is strictly larger than its SBP
  set (order-dependence *without* a fork), the coextensivity claim would weaken to containment.
  The three repo families do not show this.

## Claim-ledger effect

TI-C019: unchanged (`formalizing`). Compat-Comm marked discharged; the result adds that
`Ext_S` non-commutativity is coextensive with the SBP witness set. No status movement.
