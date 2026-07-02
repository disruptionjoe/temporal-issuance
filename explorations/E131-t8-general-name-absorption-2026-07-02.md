---
artifact_type: exploration
status: complete
governance_role: formal_hardening
workflow: W000
goal_ref: t8_general_name_absorption
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E121-online-issuance-lc-derivation-swing-2026-07-02.md
  - explorations/E130-frontier-selection-after-pa-o2-fidelity-2026-07-02.md
  - formal/lean/OnlineIssuance/Comparator.lean
  - formal/lean/OnlineIssuance/Diagonal.lean
created: 2026-07-02
central_run: RUN-20260702-076-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E131: T8 General Name Absorption

## Purpose

Execute the direct trigger selected by E130:

```text
W000 -> t8_general_name_absorption
```

The exact caveat was narrow. E121 / `Comparator.lean` machine-checked whole-family
name absorption for `freshName`, while `diagName` name-level absorption remained a
prose countability remark plus semantic `extendFamily` absorption. This run tests
whether the `diagName` name-level absorber can be made explicit without adding a
fully general theorem about arbitrary name constructors.

## Formal Addition

Added:

```text
formal/lean/OnlineIssuance/NameAbsorption.lean
```

and imported it from:

```text
formal/lean/OnlineIssuance.lean
```

The module constructs a fixed finite-stage binary-name grammar:

```text
binaryNameAbsorberFamily n = all {'a','b'} strings of length <= n
```

This is enough because `diagName vs` is always an {'a','b'} string of length
`vs.length + 1`.

## Theorem Inventory

```yaml
binaryCharLists:
  role: enumerates all {'a','b'} character lists of exact length n
BinaryChars:
  role: predicate that every character is 'a' or 'b'
mem_binaryCharLists_of_binary:
  role: every binary character list belongs to the exact-length enumerator
flip_binary:
  role: the diagonal flip always produces 'a' or 'b'
diagChars_binary:
  role: every diagonal character list is binary
diagChars_mem_binaryCharLists:
  role: every diagonal character list belongs to the exact-length binary enumerator
binaryNameAbsorberFamily:
  role: fixed stage grammar emitting all binary names up to stage length
diagName_mem_binaryNamesOfLength:
  role: every diagName belongs to the exact-length binary-name enumerator
diagName_absorbed:
  role: bounded positive form; the fixed absorber discloses diagName at stage vs.length + 1
diagName_family_disclosure:
  role: whole-family form; every diagName output is disclosed somewhere by the same absorber
no_diagName_whole_family_escape:
  role: obstruction form; no input lets diagName escape the fixed binary-name absorber
```

## Result

```yaml
t8_diagname_absorption_closed: true
bounded_name_level_absorber_built: true
broader_nat_to_string_surjection_needed_for_diagname: false
fully_general_arbitrary_name_constructor_theorem_added: false
strict_ce_positive_escape_reopened: false
external_platonist_completion_defeated: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

The broader Nat-to-String surjection theorem is unnecessary for this citation
boundary. The target was not "every conceivable name constructor is absorbed";
the target was "the concrete `diagName` construction is machine-covered at the
name tier." That now has a fixed grammar and theorem names.

## What Is Established

- `freshName` absorption remains covered by `Comparator.lean`.
- `diagName` name-level absorption is now machine-checked by
  `NameAbsorption.lean`.
- The E121 citation contract can be narrowed: T8 for `freshName` is no longer
  the only machine-checked name-tier absorber; `diagName` has its own bounded
  absorber theorem.

## What Is Not Established

- No fully general theorem over arbitrary `List String -> String` constructors
  was added.
- No strict c.e. positive escape was reopened; E127's singleton-enumerator
  ceiling remains.
- No external-Platonist completion absorber was defeated.
- No physical source issuance was established, and `TI-C020` remains parked.
- No claim status changed.

## Next Trigger

```text
W000 -> external_platonist_boundary_packet
```

Reason: after the c.e., internal-predicate, PA-O2, and T8/`diagName` caveats
are closed at the current bounded Lean tier, the next honest pressure point is
not another local interface patch. It is the external-Platonist boundary:
separate exactly what `OnlineIssuance^LC` establishes internally from what it
cannot establish against a completed-structure ontology.

## Validation

Passed:

```text
lake build
python -m unittest discover tests
```

`lake build` completed 10 jobs using the local Lean toolchain. The Python
suite ran 60 tests.

## Verdict

```yaml
status: complete
formal_branch_status: bounded_t8_diagname_absorption_closed
next_required_test: external_platonist_boundary_packet
claim_status_change: none
```
