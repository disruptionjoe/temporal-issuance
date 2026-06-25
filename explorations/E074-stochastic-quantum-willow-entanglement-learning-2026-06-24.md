---
artifact_type: exploration
status: active
governance_role: research_learning
constitutional: false
created_by_run: RUN-0069
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E014-cetext-witness-obligations-lens-survey
  - E067-source-shadow-finality-interface-contract
  - E068-barandes-stochastic-quantum-null-model
  - E072-typed-effect-signature-source-shadow-finality
---

# Stochastic Quantum, Willow, And Entanglement Learning

## Trigger

Joe suggested that the newer learnings around stochastic quantum theory, the mathematics
involved, entanglement studies, and Google's Willow research may have something useful to teach
Temporal Issuance.

This run checks that suggestion against the repo's current source/projection/effect discipline.

## Sources Checked

Primary external sources:

- Jacob Barandes, "The Stochastic-Quantum Correspondence", arXiv:2302.10778.
- Jacob Barandes, "The Stochastic-Quantum Theorem", arXiv:2309.03085.
- Jacob Barandes, "Quantum Systems as Indivisible Stochastic Processes", arXiv:2507.21192.
- Google Quantum AI and collaborators, "Quantum error correction below the surface code threshold", Nature, 2025, with 2026 correction notice.
- Google Research Blog, "Making quantum error correction work".
- Google Blog, "Meet Willow, our state-of-the-art quantum chip".

Local sources:

- E014 already marked entanglement-wedge growth as a conditional witness only if it can be
  expressed in TI terms without importing bulk AdS geometry.
- E067 defines the source-shadow-finality interface contract.
- E068 records the Barandes stochastic-quantum correspondence as a stronger fixed-H quantum
  absorber.
- E072 defines the effect discipline: `Issue[S]`, `Project[O]`, `Finalize[R]`, and `Lose[K]`.

## Plain-English Thesis

The useful lesson is not "quantum weirdness proves issuance."

The useful lesson is stricter:

```text
If a quantum-facing example looks like new structure, first test whether it is already absorbed
by stochastic-to-unitary representation, fixed-H quantum dynamics, quantum error correction,
or entanglement-as-reconstruction/capability.
```

That makes the quantum bridge harder, not easier. It also makes the bridge cleaner.

## What Barandes Adds

Barandes' stochastic-quantum program says, in effect, that very broad stochastic processes can
be represented with the mathematical machinery of quantum theory: Hilbert spaces, unitary
evolution, Born-rule probabilities, and noncommuting observables can arise as secondary tools
for describing indivisible stochastic processes.

For Temporal Issuance, this strengthens the null model.

It means:

```text
stochastic novelty != source issuance
quantum representation != source issuance
noncommuting observable bookkeeping != source issuance
wavefunction/collapse/entanglement vocabulary != source issuance
```

Before a TI-C020 physical-source claim can use stochastic or quantum behavior as evidence, it
must show what remains after this absorber:

```text
indivisible stochastic process
  -> Hilbert-space/unitary representation or dilation
  -> fixed-H/fixed-observable-algebra quantum description
```

If the claimed novelty fits inside that path, it is not yet an H-growing or A-growing source
witness.

## What Willow Adds

Willow matters because it is a clean modern case where "more quantum structure" produces a real
capability improvement.

Google's reported result is below-threshold surface-code quantum error correction:

- scaling the surface code from distance 5 to distance 7 suppressed logical error by a reported
  factor near `Lambda = 2.14`;
- the distance-7 code used 101 qubits and reached a reported logical error rate near
  `0.143%` per cycle;
- the system went beyond breakeven, meaning the protected logical qubit outlasted the best
  physical qubits involved;
- real-time decoding was part of the result;
- rare correlated events or error floors remain an open engineering/physics issue.

For Temporal Issuance, this is important but not claim-promoting.

Willow looks like:

```text
Project[O] + Finalize[R] + Lose[K] + capability improvement
```

not:

```text
Issue[S]
```

Why:

- A surface code intentionally projects physical-qubit states into a protected logical record.
- Syndrome extraction and decoding repeatedly finalize partial error information.
- The logical qubit is a lossy abstraction over the physical substrate.
- The capability improvement is real, but it is produced inside an engineered code family and
  fixed quantum-control architecture unless shown otherwise.

So Willow is a strong model of capability/finality engineering. It is not, by itself, evidence
that the physical source issued a new state space, observable algebra, or admissibility regime.

## What Entanglement Adds

Entanglement should be treated as a capability and reconstruction structure before it is treated
as source-side evidence.

Useful interpretations:

- In quantum error correction, entanglement helps distribute logical information across many
  physical qubits so local damage does not immediately destroy the logical record.
- In holographic or entanglement-wedge settings, entanglement can determine what a boundary
  observer can reconstruct about a bulk region.
- In both cases, the first TI reading is about access, projection, correctability, and record
  stability.

That means entanglement studies are highly relevant to `Capability`, `Projection`, and
`RecordFinality`.

They are not automatically relevant to `Issue[S]`.

The source-side question is narrower:

```text
Does the entanglement change force a non-isomorphic admissibility space, observable algebra,
or construction space that cannot be represented as fixed-source access, fixed-H dynamics,
or fixed-code QEC?
```

If yes, it becomes possible fixture material. If no, it remains an important projection and
capability result.

## Absorber Checklist

Any future TI-C020 quantum-facing artifact should include this explicit check:

```yaml
Barandes_Willow_entanglement_absorber_check:
  stochastic_to_quantum:
    question: Can the behavior be modeled as an indivisible stochastic process with a
      Hilbert-space/unitary representation or dilation?
    if_yes: not source issuance by itself
  fixed_H_quantum:
    question: Does the candidate stay inside a fixed Hilbert space and fixed observable algebra?
    if_yes: not H-growing/A-growing evidence
  QEC_capability:
    question: Is the reported improvement an encoded logical capability inside a fixed code
      family plus decoder?
    if_yes: capability/finality engineering, not Issue[S]
  entanglement_reconstruction:
    question: Does entanglement change only alter what can be reconstructed, protected, or
      accessed?
    if_yes: Projection/Capability/RecordFinality, not Issue[S]
  residue:
    question: After all four absorbers, does a non-isomorphic source/admissibility/construction
      space remain?
    if_yes: fixture candidate
    if_no: keep as absorber-controlled quantum learning
```

## Result For Current Claims

```yaml
TI-C019:
  status_change: none
  note: Formal source-side issuance remains alive only through the existing source gate.
TI-C020:
  status_change: none
  pressure_change: increased
  note: Stochastic-quantum theory and Willow strengthen the fixed-H/QEC absorber stack.
TI-C022:
  status_change: none
  note: Willow-like QEC is useful record-finality material, but finality does not imply source
    issuance.
path_killed: none
path_promoted: none
```

## Recommended Next Fixture

Run:

```text
W000 -> quantum_QEC_entanglement_fixed_H_absorber_fixture
```

Required:

1. Choose one concrete quantum-facing candidate: Willow/QEC, entanglement wedge reconstruction,
   or a stochastic-quantum model.
2. Type its operations with E067/E072.
3. Apply the Barandes stochastic-to-quantum absorber.
4. Apply the fixed-H/fixed-observable-algebra absorber.
5. Apply the QEC/capability/finality absorber.
6. State whether any non-isomorphic source/admissibility/construction residue remains.

Kill condition for the quantum route:

```text
If every current quantum-facing candidate reduces to stochastic-to-unitary representation,
fixed-H/fixed-A dynamics, QEC capability engineering, or entanglement reconstruction, then
quantum work remains valuable for projection/finality/capability but should not be used as
TI-C020 source evidence.
```

Promotion condition:

```text
A candidate must show residue after all four absorbers: not just better protection, better
access, stronger correlation, or more complex stochastic dynamics, but a forced change in the
source-side admissibility or construction space.
```
