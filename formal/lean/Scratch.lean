/-
Axiom-audit scratch file (cumulative across the G1/G2/G3 pass-two modules).

NOT part of the `OnlineIssuance` library — `lake build` does not compile it.
Run manually from `formal/lean`:

  lake env lean Scratch.lean

Bar: every `#print axioms` output must be a subset of
{propext, Classical.choice, Quot.sound}. No `sorryAx`, no `ofReduceBool`,
no user axioms.

Baseline bookkeeping (hostile-verification fix, G3 pass, 2026-07-02):
Core.lean byte-identity to the E120 state is git-checkable, not
mtime-circumstantial. Verified at this pass:
  git hash-object formal/lean/OnlineIssuance/Core.lean
    = e56432c3d4aa6b4dce6223b40af7723e248548a5
    = git rev-parse HEAD:formal/lean/OnlineIssuance/Core.lean
      at commit c68c840 "Execute online_issuance_lc_lean_core_encoding
      gate (E120)" (2026-07-02 06:32:50 -0500)
  SHA-256(Core.lean)
    = 3b1fde43d11e058c3268a3f008fabf8fe0da77b356e3f8a31067b32f4735b2e0
Re-run either hash to re-check byte-identity of Core.lean to E120.
-/

import OnlineIssuance

open OnlineIssuance

/-! ## G1 — OnlineIssuance.Diagonal -/

#print axioms flip_ne
#print axioms diagChars_length
#print axioms diagChars_getElem
#print axioms diagChars_ne
#print axioms diagChars_not_mem
#print axioms diagName_toList
#print axioms diagName_not_mem
#print axioms diagName_length
#print axioms diagName_ne_empty
#print axioms diagonalFormed_derived
#print axioms issue_lc_from_derived_diagonal
#print axioms registerDiagonal_stage
#print axioms registerDiagonal_registers
#print axioms diagonalFormedAtPrefix_derived
#print axioms len_le_maxLen
#print axioms freshName_length
#print axioms freshName_not_mem

/-! ## G2 — OnlineIssuance.Admissibility -/

#print axioms adm_of_present
#print axioms enumerated_candidates_admissible
#print axioms adm_not_trivial
#print axioms adm_rejects_future
#print axioms admDef_of_diagonal
#print axioms present_witness_prefix_typed
#print axioms AdmDerived.toAdmWitness
#print axioms adm_witness_derived
#print axioms adm_witness_diagonal_derived
#print axioms issue_lc_derived_witness
#print axioms diagonal_inadmissible_for_disclosure
#print axioms no_universal_self_encoding
#print axioms issuedCtx_stage
#print axioms issuedCtx_registers
#print axioms issue_lc_all_derived
#print axioms issue_lc_all_derived_full

/-! ## G3 — OnlineIssuance.Comparator -/

#print axioms stage_fresh_escape
#print axioms stage_diag_escape
#print axioms freshName_eq_allAName
#print axioms fresh_diagonal_absorbed
#print axioms fresh_diagonal_grammar_disclosed
#print axioms no_whole_family_name_escape
#print axioms fresh_family_disclosure
#print axioms diagSem_ne_at_own_index
#print axioms diagSem_escapes
#print axioms diag_absorbed_by_extension
#print axioms extension_preserves
#print axioms no_fixed_point_of_absorption
