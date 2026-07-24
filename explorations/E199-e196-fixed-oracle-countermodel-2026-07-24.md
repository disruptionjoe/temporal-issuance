---
artifact_type: exploration
status: complete
exploration_id: E199
date: 2026-07-24
lane: 1
work_group: PHYSICAL-ISSUANCE-WITNESS
topic: e196_fixed_oracle_countermodel
result: E196_BOUNDARY_NARROWED_BY_FIXED_ORACLE_COUNTERMODEL
claim_status_change: none
claim_refs:
  - TI-C019
relates_to:
  - E042
  - E045
  - E196
  - E197
run_ref: agent-runs/RUN-0211-e196-fixed-oracle-countermodel.md
---

# E199: E196 Fixed-Oracle Countermodel

## Question

E196 correctly proved a conditional degree guard:

> If the realized source information is not Turing-reducible to oracle `O`,
> no `O`-computable disclosure schedule reproduces the trace.

It then gave a stronger corollary: a single oracle fixed at stage 0 cannot
track the realized path, so escape requires an oracle to be re-indexed as
history unfolds. Is that stronger fixed-versus-re-indexed boundary valid?

## Construction fork

This run uses the **static-source construction**, not the program-native
source construction, because it is testing the strongest disclosure rival.
The rival is allowed the same mathematical object E196 §4 already concedes:
one fixed real containing future-correlated information. This choice does not
assert that such a real is physically available.

The program-native construction remains the target to be earned. It cannot win
by excluding the static construction through terminology alone.

## Countermodel

Let the realized history be `H = (S_0, S_1, ...)`. Define:

```text
Ind_H = effective join of the stagewise option-set predicates
Path_H = sequence of realized quorum selections
J_H = Ind_H ⊕ Path_H
O_H = any oracle computing J_H
```

Choose `O_H` once at stage 0. Define the disclosure schedule `D^{O_H}` to use
the oracle to recover the option set and selected successor for stage `n`.
Then:

1. `O_H` is fixed at stage 0;
2. it is never re-selected;
3. `D^{O_H}` reproduces the realized trace; and
4. its degree is at least the degree of the joined source information.

This is a countermodel to the statement that oracle re-indexing is required
for escape. It is not a counterexample to E196's conditional theorem, because
that theorem assumes `J_H` (compressed there as `deg_src` plus path) is not
reducible to the adversary oracle. Here the assumption intentionally fails.

The same correction survives counterfactual strengthening. A single fixed
oracle can encode the response tree over all finite intervention histories,
not merely one realized path. An intervention test can defeat a
**trace-only** pre-correlation, but it does not defeat a completed
branch-family oracle without an independent physical bound on oracle content
and access.

## What failed

Three properties were conflated:

| Property | Meaning | Implies either other property? |
| --- | --- | --- |
| stage-fixed | One oracle object is selected at stage 0 and never changed. | No. |
| degree-bounded | The oracle does not compute the joined option/path information required by the source trace. | No. |
| future-independent | The oracle is not pre-correlated with realized or counterfactual future choices beyond admitted common-past data. | No. |

NAA-Q constrains what observers or the quorum command before resolution. It
does not, by itself, prove that an external static-source adversary lacks a
future-correlated oracle. Applying NAA-Q to that adversary would assume the
physical independence condition the argument needs to establish.

Therefore these E196 statements are withdrawn:

- "a single fixed `d` chosen at stage 0 cannot compute the path";
- "the only escape is an oracle-unbounded/history-re-indexed adversary"; and
- "oracle-bounded" understood merely as stage-fixed is sufficient for defeat.

## Corrected theorem boundary

Let `J_H` be the join of the information the schedule must reproduce:
stagewise option-set information plus realized path selection. For a declared
oracle `O`:

```text
J_H not <=_T O
    => no O-computable disclosure schedule reproduces H.

J_H <=_T O
    => a fixed O-computable read-off schedule exists in the mathematical
       static-source model.
```

The first implication is the surviving core of E196. The second is the fixed
countermodel. Neither implication decides whether `O` is physically
realizable, physically accessible, causally admissible, or independent of
future choices.

The physical burden is consequently not one "oracle-boundedness" posit. It is
an explicit contract:

1. **degree/access bound:** every admitted physical discloser oracle `O` fails
   to compute `J_H`;
2. **causal-source separation:** a schedule that reads the source after stage
   0 is adaptive copying, not static disclosure;
3. **future-independence:** the initial discloser state is not granted a
   completed realized-history or branch-family oracle by stipulation; and
4. **construction disclosure:** the physical reason for 1–3 must be named,
   rather than inferred from "fixed at stage 0."

These are physical/model-admission assumptions, not computability theorems.

## Executable pressure

`tools/e196_fixed_oracle_countermodel.py` represents:

- a fixed realized-history oracle;
- a fixed branch-complete oracle;
- option-only and path-only omission controls; and
- an adaptive source reader.

The first two reproduce their declared traces without oracle reselection. The
omission controls fail the corrected degree guard. The adaptive reader is
classified as source copying, not a static-source rival. The executable is a
finite contract fixture for the logical distinction, not a proof of physical
realizability or an infinite computability theorem.

## Verdict

```yaml
result: E196_BOUNDARY_NARROWED_BY_FIXED_ORACLE_COUNTERMODEL
e196_conditional_degree_guard_survives: true
stage_zero_fixedness_sufficient_for_defeat: false
oracle_reselection_required_for_escape: false
fixed_precorrelated_oracle_countermodel: exists_mathematically
fixed_branch_complete_oracle_countermodel: exists_mathematically
physical_realizability_established: false
physical_oracle_bound_proved: false
source_issuance_established: false
claim_status_change: none
```

This is material negative Progress: it removes an invalid protection around
the D-FORK witness and converts the physical hinge into four auditable
assumptions. `TI-C019` remains formalizing; `TI-C020` remains parked. The next
North-Star swing must justify or falsify the degree/access and
future-independence assumptions in a named physical construction. Another
computability restatement cannot close that burden.
