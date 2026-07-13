---
artifact_type: exploration
status: complete
governance_role: research_steering_wave_result
workflow: research_steering_wave10
claim_movement: false
created: 2026-07-12
central_run: RUN-0155
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E173-t2-bounded-completion-barrier-theorem-contract-2026-07-12.md
  - explorations/E174-t3-t2-counterexample-gate-validator-2026-07-12.md
  - tools/g2_t2_obligation_minimality_stressor.py
  - tests/test_g2_t2_obligation_minimality_stressor.py
---

# E175: G2 T2 Obligation-Minimality Stressor

## Purpose

This focused swing executed G2 from the post-T3 steering state:

```text
Distinct T2 contract stressor gate
```

The specific stressor was obligation minimality. It asked whether any
E172/E173 counterexample obligation is redundant or over-strong under the
current T3 gate.

## Wave Type

This was a focused swing, not a full wave. E173 fixed the contract and E174
validated the gate, so the next dependency-bounded question was whether the
gate contains unnecessary obligations.

## Executable Artifact

Executable:

```text
tools/g2_t2_obligation_minimality_stressor.py
```

Focused test:

```text
tests/test_g2_t2_obligation_minimality_stressor.py
```

Result JSON:

```text
tests/artifacts/g2_t2_obligation_minimality_stressor_result.json
```

## Computed Result

```yaml
fixture_id: g2_t2_obligation_minimality_stressor
kind: t2_counterexample_obligation_minimality_stressor
obligation_count: 19
all_obligations_load_bearing: true
redundant_obligation_ids: []
overstrong_obligation_ids: []
real_counterexample_packet_found: false
g2_result: all_t2_counterexample_obligations_load_bearing_no_redundant_clause_detected
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
```

## Interpretation

Every current counterexample obligation is load-bearing under single-omission
stress. Removing any one obligation prevents contract revision. Four omissions
activate terminal safety stops:

- `no_hidden_completion_oracle`;
- `no_imported_law_or_schema`;
- `not_readout_or_finality_only`;
- `does_not_treat_h8_as_d_fork_decision`.

The remaining omissions are nonterminal but still block revision because the
candidate no longer satisfies the full counterexample contract.

This does not prove that the obligation set is globally minimal under every
future formalization. It only says that, under the current E172/E173/T3 gate,
no single obligation is redundant or over-strong.

## Inline Council Reflection

Personas were run inline as one council pass, not one-agent-per-persona.

- Orthodox professor: the result is a bounded minimality check, not a general
  theorem about all admissibility contracts.
- Heterodox-rigorous professor: the danger was overfitting the gate. The
  single-omission stressor finds no redundant clause, but fixed-input changes
  could still alter the obligation set.
- Commercial scientist: this was the cheap decisive contract check. Repeating
  it without changed inputs would be busywork.
- Philosopher of science: the result exposes the contract to falsification
  because every omitted obligation changes the verdict.
- Wild frontier scientist: the highest-upside object remains a real source
  packet, not another synthetic closure test.
- Computability and proof-theory specialist: the completion and no-hidden-oracle
  clauses remain load-bearing.
- Category, sheaf, and topos theorist: H7 preservation clauses remain structural
  rather than decorative.
- Quantum and operator-algebra foundations specialist: W1/W4/W5 are still the
  physical bridge burden.
- Thermodynamics and information theorist: readout/finality remains a terminal
  stop.
- Cosmology and boundary-physics specialist: H8 and boundary language cannot
  substitute for the packet obligations.
- Distributed systems and finality theorist: quorum/finality language does not
  revise the contract without the full obligations.
- Evolution and open-endedness theorist: biological novelty examples still need
  the same source-side packet obligations.

## Generated Re-Rank

Resolved:

- G2 T2 obligation-minimality stressor.

Live set:

| Item | Status |
| --- | --- |
| P1 Real H7-admitted packet intake | Conditional Track 1. Only a real packet through the obligations can revise the bounded contract. |
| W000 Gate-change wait after G2 | Fallback state when there is no real packet or fixed-input change. |

After updating `attention/priority_condorcet.py`, the ranking is:

```text
1. P1 Real H7-admitted packet intake
2. W000 Gate-change wait after G2 minimality stressor
```

## Computed vs Argued Claims

COMPUTED, high confidence:

- The G2 executable artifact exits 0.
- All 19 E172/E173 counterexample obligations are load-bearing under
  single-omission stress.
- No redundant obligations are detected.
- No over-strong obligations are detected.
- No real counterexample packet is found.
- No claim status changes, no physical source issuance is established, and
  `TI-C020` remains parked.

ARGUED, medium confidence:

- The next unattended state should be gate-change wait.
- Further synthetic contract testing has diminishing value unless fixed inputs
  or the obligation set change.

## Next Route

```text
W000 -> gate_change_wait_after_g2_until_real_h7_packet_or_fixed_input_change
```

Minimum contract:

1. Do not repeat T2, T3, or G2 unless fixed inputs change.
2. A real packet must pass E172/E173 obligations before claim movement.
3. Treat this as single-omission minimality, not global logical minimality.
4. Preserve no claim movement unless a later durable artifact actually earns it.
