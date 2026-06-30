---
artifact_type: absorber
status: active
absorber: action_principle_boundary_selection
constitutional: false
last_updated_by: external-paper-council-pass-2026-06-30
---

# Action-Principle Boundary Selection

External source: a Joe-fed reading set assessed via an inline LLM-council pass, 2026-06-30. External papers are
calibration anchors, never evidence for Temporal Issuance. This repo succeeds by killing, so a clean
absorption here is a success.

## Threat

Temporal Issuance's surviving source object is `SourceRealization = (C, <=_S, Ext_S)` -- finite constraints, a
source fixation order `<=_S`, and allowed source extensions `Ext_S`. The standing kill condition
(FORMAL-DEFINITION-REPAIR, RUN-0019) absorbs/archives the object if `<=_S` / `Ext_S` factor through causal
order, dependency order, record generation, entropy, information, probability, volume, **action**, or
primitive time.

Tzanavaris-Boyle-Turok (*The free boundary problem in general relativity*, arXiv:2606.18128, 2026) derive --
from the gravitational **action** via free-boundary stationarity -- exactly which initial-boundary
configurations are admissible (condition `K_ij mu_t -> 0` excludes Kasner/BKL, admits conformally-regular
FLRW; stiff fluid killed by non-finite on-shell action). That is an action principle selecting allowed
extensions from the initial boundary. It lands directly on the `action` clause of the `Ext_S` kill condition.

## Mapping

| Temporal Issuance object | Free-boundary paper object |
| --- | --- |
| `Ext_S` (allowed source extensions) | the admissible saddles permitted by the free-boundary condition (6) |
| `<=_S` (source fixation order) | the conformal-regularity ordering selecting FLRW over Kasner/BKL |
| admissibility of a realization | stationarity of the action under unconstrained boundary variation |

## Key test

Does `Ext_S` do work **upstream** of an action principle, or only **downstream** of one? The action *filters*
a pre-given configuration space and a pre-given boundary; it does not *issue* them. Temporal Issuance survives
this absorber only if `Ext_S` generates or constrains the candidate space *before* an action functional
exists (a pre-geometric layer), and only if that does observer-capability work that time-as-finality readout
cannot already express.

## Corroborating papers (same absorber, reinforced)

- **Stelle**, Phys. Rev. D 16, 953 (1977): higher-derivative gravity's extra boundary data and its
  unitarity/probability structure are action-derived. Reinforces both the `action` and `probability` clauses.
- **Avramidi & Barvinsky**, Phys. Lett. B 159, 269 (1985): asymptotic freedom is a scale/action statement;
  reinforces the `action` clause. Neither paper opens a source-side lane; both tighten the absorber.

## Current verdict

This is the most on-target external result Temporal Issuance's current crux has met. It most likely
**tightens the noose** on the source-side residue (pushes toward K1 absorption under the `action` clause)
rather than helping it. The single survival path is `Ext_S` operating upstream of the action at a
pre-geometric layer -- which is precisely the repo's own already-stated next test, now with a concrete
adversary. Escaping the entropy absorber via boundary-asymmetry (no monotone) only relocates the burden onto
this action absorber.

Category risk: the free-boundary condition is a 4D geometric / physical-model feature; Temporal Issuance is
framed as a pre-physical substrate claim. Comparing them directly can be a layer error (cf. the
cosmological-expansion absorber's warning). Absorption is clean only if issuance commits to the geometric
layer -- which costs it its "deeper than physics" ambition.

## Next test (discriminator)

Build an upstream-vs-downstream-of-action discriminator (candidate `explorations/E007`):

```text
Can <=_S and Ext_S be specified so they fix the candidate configuration space BEFORE any action functional
exists, doing observer-capability work TaF readout cannot already express?
```

- No -> absorb the source residue under action + relativity (write the kill-record).
- Cannot even be posed precisely -> K5 metaphysical residue.
- Yes (with a worked finite model) -> the absorber is survived, with a narrowed burden.

## Corroboration (2026-06-30): the cosmological-measure view

In *A Route to Quantum Gravity (Without Strings)* (Theories of Everything podcast, 2026), Turok states a
"no one started the universe" view: rather than positing an initial event that *issues* the universe in a
special state, you **count space-time histories with a measure** (Hawking's gravitational entropy, generalized
to cosmologies), and the smooth, flat, small-Lambda universe is simply the *typical* (maximum-microstate)
state -- no dynamics, no smoothing, no initial-condition-setter required.

This is fresh pressure on the source side. Where Temporal Issuance posits a `SourceRealization` whose `Ext_S`
*issues* allowed extensions, the measure view replaces the issuance *event/order* with a **measure over
histories** plus "pick the typical one." If the observed structure is fully accounted for by counting +
typicality (no issuance act), the source residue is at risk of absorption by a measure/counting framework, not
only by the `action` clause.

Bounded next step: this may deserve its own absorber, candidate `absorbers/gravitational-entropy-measure.md`,
with key test -- *does `Ext_S` do work that a measure-over-histories + typicality argument does not already
do?* Carry the caveat: Turok's program is by his own statement "halfway there," an external provocation, not a
result.
