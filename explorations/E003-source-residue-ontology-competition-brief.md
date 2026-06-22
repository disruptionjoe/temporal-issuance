---
artifact_type: exploration
status: active
governance_role: ontology_resolution_brief
exploration_id: E003
last_updated_by: RUN-0021
claim_refs:
  - TI-C001
  - TI-C002
  - TI-C003
constitutional: false
---

# E003: Source Residue Ontology Competition Brief

## Purpose

Record the post-RUN-0019 ontology-resolution correction.

The primary bottleneck is no longer governance architecture. The bottleneck is ontology resolution. The remaining source-side residue is small enough that the next mistakes are likely conceptual: treating the survivor as one object, testing one meaning of `<=_S` while thinking another is under review, or becoming attached to the last un-killed residue.

## Current Residue

The current source-side candidate has been written as:

```text
SourceRealization = (
  C,
  <=_S,
  Ext_S
)
```

Do not treat this as one survivor.

Treat these as separate survivors:

- `C`
- `<=_S`
- `Ext_S`

Each may survive, absorb, remain undecidable, or archive independently.

## Component Split

| Component | Working meaning | Independent absorber threats | Kill condition | Resurrection condition | Current status |
| --- | --- | --- | --- | --- | --- |
| `C` | Candidate source constraints or constraint states. | causal-set elements, record sets, facts, propositions, proof objects, information states, physical boundary data. | Kill or absorb if `C` is only an event set, record collection, proposition set, or hidden-variable inventory with no independent constraint role. | Resurrect or preserve if `C` can be typed as constraints whose extension changes allowed transformations, projections, or invariants. | live but underspecified |
| `<=_S` | Candidate source relation over constraints. | causal order, dependency order, proof order, computational order, construction order, observer-readout order, resource preorder. | Kill or absorb if every definition factors through known causal, logical, computational, construction, or record order. | Preserve if a source relation has formal consequences not recoverable from those orders. | live but highest local-minimum risk |
| `Ext_S` | Candidate rule for admissible source extensions. | transition systems, proof derivations, constructor tasks, resource convertibility, thermodynamic irreversibility, information update, database commits. | Kill or absorb if extension means only "later state" or imports ordinary time, records, entropy, information, action, probability, volume, or causal update. | Preserve if extension rules constrain what can become fixed without being reducible to a known update, proof, or transformation system. | live and probably the most important component |

## Source-Order Taxonomy

Before any narrow source-order absorption pass, the repo must state which meaning of `<=_S` is under test.

| Candidate meaning of `<=_S` | Plain meaning | Leading absorber | First discriminator | Kill condition |
| --- | --- | --- | --- | --- |
| causal order | `a <=_S b` means `a` can causally precede or influence `b`. | relativity, causal set theory. | Compare against causal set or relativistic causal order. | Exact mapping with no leftover formal role. |
| dependency order | `b` depends on `a` being fixed. | ordinary dependency graphs, DAGs, build systems, proof dependencies. | Find dependency with no causal or logical interpretation. | All examples are standard dependency edges. |
| constraint order | `a` narrows the admissible state space before `b`. | constraint satisfaction, optimization, boundary-condition formalisms. | Show narrowing that changes allowed extensions. | Merely restates set inclusion or constraint propagation. |
| realization order | `a` becomes fixed before `b` in a source-side sense. | primitive time, process philosophy, block-universe narration. | Define "becomes fixed" without time or records. | Requires primitive time or metaphysical becoming. |
| proof order | `b` can be derived only after `a`. | proof theory, type theory, formal methods. | Separate physical fixation from derivability. | All order claims are proof artifacts. |
| computational order | `a` must be computed before `b`. | algorithms, cellular automata, rewrite systems. | Show non-computational fixation role. | Reduces to execution trace or rewrite order. |
| construction order | `a` must be constructed before `b` is possible. | constructor theory, resource theory, engineering build order. | Name possible and impossible transformations. | All claims reduce to known construction or resource convertibility. |
| observer-independent order | Order exists independently of observer access. | hidden-variable models, causal order, gauge redundancy. | Show gauge-invariant or witnessable hidden structure. | Hidden distinctions have no invariant or witness. |
| observer-relative order | Order is relative to observer site or access boundary. | time-as-finality, information theory, access-control systems. | Show source-side effect beyond observer readout. | Fully absorbed by readout, access, or records. |
| resource preorder | `a <=_S b` means `a` can be transformed into or enables `b` under allowed operations. | resource theory, thermodynamics, constructor theory. | Define free operations and monotones. | Monotone collapses to entropy, information, action, probability, volume, or cost. |
| projection kernel order | Order is the equivalence or loss structure induced by projection to records. | information theory, category theory, cryptographic witness theory. | Identify nonfaithful projection classes and witnessability. | It is only ordinary information loss. |
| null order | There is no meaningful source-side order. | archive path. | Attempt full absorption by existing frameworks. | Null wins if no candidate beats archive. |

## Competing Ontologies

The next major learning step should force explicit competition among ontologies.

| Ontology | Core idea | What it explains | Main threat | First test |
| --- | --- | --- | --- | --- |
| O1: source realization order | `C`, `<=_S`, and `Ext_S` describe source-side realization. | Nonfaithful projection from RUN-0019. | causal order, dependency order, hidden records. | Specify each component independently. |
| O2: constraint extension primitive | `Ext_S` is primary; order is only a shadow of admissible extension. | Why extension may matter more than relation. | proof systems, transition systems, constructor theory. | Same order, different extension rules. |
| O3: constraint inventory | `C` is primary; the relation and extension are bookkeeping over constraint types. | Need to type what is being realized. | event sets, propositions, records, causal-set elements. | Same order and extension, different typed constraints. |
| O4: projection-kernel ontology | The residue is projection loss between source and observer records. | RUN-0019 F2. | information theory, category theory. | Define equivalence classes under projection. |
| O5: witness-certification ontology | Hidden source structure matters only if certifiable by witnesses under bounded access. | Nonfaithful projection without metaphysical hiddenness. | ZK, proof-carrying records, access control. | Same records, rival sources, one valid witness. |
| O6: constructor/resource ontology | Realization is a change in possible and impossible transformations. | Irreversibility without primitive time. | constructor theory, resource theory, thermodynamics. | Name transformations made impossible by realization. |
| O7: obstruction ontology | The survivor is obstruction to gluing source or record patches. | `Omega_ij` and local-to-global failure. | sheaf theory, time-as-finality. | Same source order, different obstruction class. |
| O8: proof/computation ontology | Realization is derivation, computation, or rewrite order. | Formalizes extension without physics. | proof theory, type theory, computation. | Find physical constraint not represented by derivation. |
| O9: emergence ontology | Apparent source order emerges from local rules, basins, or regime shifts. | Path dependence and lock-in. | complex systems, dynamical systems. | Local-rule model reproduces source/readout fixtures. |
| O10: NULL-SURVIVOR | There is no meaningful source-side residue. Existing frameworks absorb everything. | Prevents survivor attachment. | premature closure. | Absorption proof attempt across all live components. |

## Survivor Competition Requirements

The next research run should not ask only whether `SourceRealization` survives.

It should compare candidates using the same questions:

```yaml
survivor:
components_used:
what_it_explains:
assumptions_required:
strongest_absorber_threat:
sharpest_discriminator:
what_would_kill_it:
what_would_resurrect_it:
does_it_beat_NULL_SURVIVOR:
```

## Null Competitor Rule

Every survivor must compete against:

```text
NULL-SURVIVOR
```

Meaning:

There is no meaningful source-side residue. Every surviving ontology is absorbed by existing frameworks or archived as useful intuition.

If a survivor cannot beat archive, archive wins.

## Survivor Attachment Warning

The repo has made progress against premature absorption. The new failure mode is survivor attachment.

Survivor attachment means the repo becomes structurally or emotionally attached to the remaining residue because so much else has already been killed.

The final survivor deserves at least as much skepticism as the first hypothesis.

## Governance Boundary

No major governance expansion is recommended.

Do not create new governance workflows, metrics, or assessment layers unless a concrete failure appears. Current governance is sufficient. From this point, governance should stay subordinate to ontology resolution and research pressure.

## Daily Review Question

Highest-value question for Joe:

```text
What would have to be true for the current source-order residue to be completely absorbed by an existing framework?
```
