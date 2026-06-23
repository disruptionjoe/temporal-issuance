---
artifact_type: exploration
status: active
exploration_id: E047
date: 2026-06-22
topic: gu_constructions_ti_cross_repo_check
claim_refs:
  - TI-C019
  - TI-C007
  - TI-C012
relates_to:
  - E031 (Ext_S category structure; SBP morphism class)
  - E040 (Ostrom Redistribution Theorem; WITNESS-OBL-001)
  - E046 (hostile audit; LAYER-OBL-001 named)
  - E029 (bounded-accessibility source/projection model; PP-3)
  - E042 (SBP-IND verification; FTS/Gödelian fork)
  - E045 (D-FORK synthesis; program pivot)
  - E015 (holonomy fixture)
cross_repo: gu-formalization (positive constructions lane proposal)
governance_note: >
  This exploration assesses whether the GU Formalization repo's new Positive
  Constructions Lane (five specific GU targets) changes or usefully reframes
  TI thinking. Verdicts are analogy-strength ratings: genuine isomorphism,
  useful vocabulary, or superficial/vocabulary match. The exploration does NOT
  import GU physics claims. Method discipline only (per absorbers/gu-formalization.md).
---

# E047: GU Positive Constructions Lane — TI Cross-Repo Assessment

## Context and Purpose

The GU Formalization repo has a new "Positive GU Constructions Lane" targeting
five specific constructions: (1) the 14D Observerse / Y^14 / X^4 observation slice,
(2) Riemannian-Ehresmannian unification, (3) precision torsion replacing the
cosmological constant, (4) full spinor group mechanics in 14D, and (5) Higgs
emergence as geometric illusion.

This exploration assesses each against TI's current formal state. The active TI
pivot is D-FORK (E045): the entire PP-3 question — source-side issuance vs.
bounded-projection disclosure — now turns on whether the operative source's
effective type space is finite or self-generating (Gödelian). LAYER-OBL-001 is
the blocking obligation: the inference from global-coordination-structure
irreducibility (proved in E040/E046) to genuine source-side novelty requires
declaring that the AC-8 quorum coordination process operates AT the source layer
rather than the observer-coordination layer.

The question for each GU construction: does it move any of these levers?

---

## Assessment Criteria

For each analogy, the assessment asks:

1. **Formal strength:** Is there a genuine isomorphism (same mathematical structure,
   functorially related), useful vocabulary (shared formal language with load-bearing
   distinctions), or vocabulary match only (same words, different mathematical content)?
2. **Concrete advance:** Does this change, strengthen, or narrow any TI claim or
   blocking obligation? Specifically LAYER-OBL-001?
3. **New formal machinery:** Is there mathematical structure worth importing into TI
   (carefully bounded per the GU absorber rule: method lessons only, not GU physics)?
4. **Verdict:** Hold, partially hold, or collapse under scrutiny?

---

## A. Ext_S / Schema-Boundary Parallel with Y^14 / X^4

**The proposed analogy:**
GU's 14D Observerse (Y^14) projects to 4D spacetime (X^4) via a pullback map. The
X^4 observation slice is a pullback/restriction from richer higher-dimensional geometry.
The proposed TI parallel: Ext_S "source" projects to observable schema events just as
Y^14 projects to X^4. Specifically: does the Riemannian-Ehresmannian fusion (rigid
Levi-Civita structure vs. content-free Ehresmannian gauge) map onto TI's distinction
between bounded-aperture projection (fixed Mu_infty) and genuine source-side extension?

**Analysis:**

The GU pullback Y^14 -> X^4 is a map from a fixed total space to a fixed base space.
X^4 is a slice of Y^14; it does not "receive" novel content from Y^14 — it is already
there in the total space, and the pullback just restricts. This is structurally a
projection from a richer fixed space. In TI terms, the GU pullback is the static-source
construction (SSC): a fixed Mu_infty with a disclosure map.

The Riemannian-Ehresmannian split is more interesting. Riemannian geometry (Levi-Civita)
is rigid: the connection is uniquely determined by the metric, torsion-free. Ehresmannian
geometry (principal bundles, gauge freedom) is "content-free" in the sense that the
connection is not determined by the base-space metric — it carries independent degrees
of freedom. GU fuses these to get geometry that is both canonically grounded AND
gauge-free for content.

**Does this map onto TI's fixed-Mu_infty / source-extension distinction?**

The Riemannian/Ehresmannian split is a split between:
- A geometry whose connection is derived from pre-existing structure (Levi-Civita,
  uniquely determined from the metric)
- A geometry whose connection is an independent field with gauge freedom (principal bundle,
  not derived from metric)

This maps loosely onto TI's:
- Fixed Mu_infty + admissibility predicate determined by that fixed source (the Riemannian
  side: everything derived from the fixed metric/source)
- Ext_S with an independently specified compatibility predicate Compat(-, -, S_n) that
  carries genuine SBP degrees of freedom (the Ehresmannian side: independent field content)

**Strength assessment:**

This is USEFUL VOCABULARY, not a genuine isomorphism. The mathematical structure is
different in important ways:

1. In GU, the Riemannian/Ehresmannian split is within a fixed total space Y^14. The
   Ehresmannian connection is an independent field ON the same total space — it does not
   expand the space. In TI, the question is whether the source expands (Gödelian) or
   whether a fixed source has an independent access policy (Ehresmannian reading of
   bounded projection). The GU split does not map cleanly onto the source-expansion vs.
   navigation question.

2. The pullback Y^14 -> X^4 is a static geometric operation, not a sequential schema-
   extension process. The TI Ext_S category has a time-like sequential structure (stages
   S_0, S_1, ...) that the GU pullback does not have.

3. HOWEVER: the Ehresmannian framing provides a useful vocabulary for naming what is at
   stake in LAYER-OBL-001. The Ehresmannian connection (independent gauge degrees of
   freedom not derived from metric) is a good analogy for the Compat predicate that the
   AC-8 quorum updates at each stage. The question "is Compat derived from a fixed source
   or does it carry independent gauge content?" is structurally isomorphic to "is the
   connection Riemannian (derived) or Ehresmannian (independent)?"

**Concrete advance to LAYER-OBL-001:**

LAYER-OBL-001 requires declaring whether the AC-8 quorum coordination process operates
at the source layer or the observer-coordination layer. The Riemannian/Ehresmannian split
offers a structural vocabulary for this declaration:

- If the admissibility predicate A_{S_n} is always derivable from a fixed underlying
  Mu_infty (the Riemannian case: connection = function of fixed metric), then quorum
  coordination is an observer-layer event and LAYER-OBL-001 fails for source-side claims.
- If A_{S_n} carries independent gauge content not derived from any fixed source (the
  Ehresmannian case: connection is an independent field), then quorum coordination at
  each stage introduces genuine source-layer content, and LAYER-OBL-001 is satisfiable.

This reframing is not a proof of LAYER-OBL-001, but it gives it a structural shape:
the obligation is to show that A_{S_n} is Ehresmannian with respect to any fixed source,
i.e., that no fixed source Mu_infty determines A_{S_n} derivatively (not even a non-
computable one). This is exactly the creation-vs.-navigation question that E046 identified
as the deepest residual gap.

**Verdict: PARTIALLY HOLDS.** The analogy collapses at the static-vs-sequential level
and at the GU pullback-as-projection level. But the Riemannian/Ehresmannian split provides
useful structural vocabulary for LAYER-OBL-001 that is worth importing as a framing device.
It does not advance LAYER-OBL-001 formally, but it names the obligation more precisely:
show that A_{S_n} is Ehresmannian (not derivatively Riemannian) with respect to all
fixed sources.

---

## B. Torsion and the Schema Boundary (D4 Morphisms)

**The proposed analogy:**
In GU, torsion is what standard Riemannian geometry lacks: it is the extra geometric
structure (antisymmetric part of the connection) that enables richer content not
derivable from the symmetric Levi-Civita connection. In TI, D4 morphisms (schema-
boundary extensions, genuinely novel typed constraints) are what standard aperture-
disclosure lacks: the extra structural capacity that enables genuine source-side novelty
beyond disclosure of pre-existing types.

**Analysis:**

The torsion analogy is structurally appealing. In differential geometry, torsion measures
the failure of the connection to be symmetric: T(X,Y) = nabla_X Y - nabla_Y X - [X,Y].
A Levi-Civita connection is torsion-free by definition. Adding torsion gives the connection
degrees of freedom not determined by the metric — this is the Cartan geometry / EC gravity
move that GU's torsion term captures.

The TI parallel: D4 morphisms introduce types NOT in T_S (genuinely novel type condition)
and SBP morphisms introduce types that are TYPE-INCOMPATIBLE with all concurrent extension
candidates (creating genuine fork structure). These are exactly analogous to torsion: they
are degrees of freedom in the extension process not determined by the pre-existing schema.

**Is the analogy formally load-bearing?**

There is a genuine structural parallel at the level of "extra degrees of freedom not
determined by the base structure":
- Torsion: antisymmetric connection part not determined by metric
- SBP/D4: admissibility outcomes not determined by prior schema history (SBP-IND)

And at the level of "what standard machinery lacks":
- Standard Riemannian geometry: no torsion, connection fully determined by metric
- Static-source construction (SSC): no SBP novelty, trajectory fully determined by
  fixed Mu_infty

The precision is higher than it first appears. In GU, the augmented torsion tensor
replaces the cosmological constant (a fixed scalar) with a varying geometric quantity
(a tensor field that can encode position-dependent "dark energy"). The TI parallel:
the fixed admissibility predicate A_infty of the SSC is replaced by the evolving
A_{S_n} of the AC-8 quorum process, which can encode stage-dependent extension
constraints.

**Critical check: does torsion as GU uses it import physics TI cannot claim?**

Yes. GU's torsion term is a specific physical construction: it produces a tensor
contribution to the Einstein equations. TI cannot import the physics. But the FORMAL
STRUCTURE — extra degrees of freedom in the connection not derivable from the base
metric, giving rise to a "dark" or "hidden" field not captured by the standard formalism —
can be imported as vocabulary.

**Does this collapse to vocabulary-only?**

Partially. The mathematical content of "torsion" in differential geometry (antisymmetric
part of a connection on a tangent bundle) is quite specific, while TI's "SBP morphisms
bring extra degrees of freedom to the quorum" is a statement about a set-theoretic
construction on typed constraint states. The formal structures are not isomorphic. But
the analogy is stronger than purely superficial because BOTH:
1. Measure the failure of a canonical derivation (Levi-Civita fails to capture torsion;
   SSC fails to capture SBP-IND)
2. Require an additional field/structure not present in the base object (connection torsion
   tensor; Compat predicate carrying SBP-independent content)
3. Are gauge-related in the sense that their non-triviality cannot be removed by a
   coordinate transformation / relabeling

Point 3 is the strongest parallel. Torsion is a tensorial quantity (gauge-covariant).
The SBP incompatibility condition (Compat(c_e, T_{S''}, S_n) = 0) is defined relative
to the current schema state S_n and is not relabeling-removable if SBP-IND holds —
there is no "gauge transformation" that converts a genuinely-SBP-incompatible extension
into a compatible one.

**Concrete advance:**

The torsion parallel suggests a productive next check for the Compat predicate: is the
SBP incompatibility between concurrent extensions a TENSORIAL property of the Ext_S
category (covariant under base-category transformations) or a COORDINATE property
(removable by relabeling)? This is a non-trivial question that the absorber analysis
in E046 has not yet asked directly. If SBP incompatibility is tensorial/covariant, the
torsion analogy provides a formal warrant for treating the SBP degrees of freedom as
genuine structure (not gauge artifact). If it is coordinate-dependent, the analogy
collapses and absorber #5 (Gauge Absorber in E046) gains force.

**Verdict: USEFUL VOCABULARY with a concrete test suggestion.** The analogy holds at
the structural level ("extra degrees of freedom not derivable from the base metric/source")
and at the covariance level (torsion is tensorial; SBP incompatibility should be
covariant). It collapses at the level of formal isomorphism (different mathematical
categories). The actionable output: run a covariance check on Compat and SBP-incompatibility
to test whether they are schema-relabeling-invariant. This connects directly to E046's
Gauge Absorber (#5) and could partially discharge it.

---

## C. Higgs Emergence and the Source/Projection Distinction (LAYER-OBL-001)

**The proposed analogy:**
GU's "Higgs as illusion" claim: the Higgs field is not an independent field but emerges
as a norm, projection, or connection component from higher-dimensional geometric structure.
What appears to be an independent scalar field is actually derived from the geometry of
the total space. The proposed TI parallel: apparently novel schema types that appear as
D4 events at the observer layer might not be genuinely new — they could be "derived" from
pre-existing richer source structure Mu_infty via aperture-widening, exactly as the Higgs
is "derived" from Y^14 geometry. LAYER-OBL-001 asks whether the AC-8 quorum coordination
produces source-side creation or navigation of pre-existing structure. Does Higgs-as-illusion
provide formal vocabulary for this distinction?

**Analysis:**

The Higgs-as-illusion construction has a specific mathematical form in GU: the Higgs is
identified with the norm of a connection form, or a component of the gauge field in the
Observerse. It is not an independent field at the level of Y^14; it APPEARS as an
independent field only when you restrict attention to X^4. From the X^4 observer's
perspective, the Higgs looks like a new independent field — but it is actually a derivative
of the already-present Y^14 geometry.

This is structurally identical to the PP-3 Hypothesis B (bounded-accessibility source/
projection model from E029): from the projection layer (observer at X^4 / bounded
observer with aperture P_n), genuinely novel fields appear that are "new" at the observer
level — but at the source level (Y^14 / Mu_infty), they were already there.

**This is a precise formal parallel, not merely vocabulary:**

1. Y^14 = Mu_infty (the complete source)
2. X^4 = the observer's current schema state S_n (the restriction/slice)
3. Higgs appearing as new field in X^4 = D4 morphism appearing as type-novel in S_n
4. Higgs is actually norm/component in Y^14 = D4 type was already in T_infty

The entire GU Higgs-as-illusion construction is a PRECISE FORMAL INSTANCE of what
E029 calls the projection absorber for D4. The Higgs illusion is exactly what bounded-
access-disclosure would look like at the physics level.

**What does this mean for TI?**

This is both a threat and a clarification. It is a threat because GU provides an explicit
physical model where D4-like novelty appears at the observer level as illusion, derived
from Y^14. It is a clarification because GU makes precise what the SSC looks like when
fleshed out with actual geometric content: a fixed higher-dimensional space (Mu_infty =
Y^14) with a projection/slice mechanism (disclosure = taking the X^4 slice).

**Critical question: does GU's Y^14 support a Mu_infty that avoids SSC-defeat?**

The E040 ORT proved that an SSC using a computable disclosure schedule D cannot reproduce
an SBP-governed Gödelian trajectory. The question for the Higgs-as-illusion parallel:
is GU's Y^14 -> X^4 projection a computable disclosure schedule?

In GU, the pullback map is a FIXED geometric operation (pullback by a smooth embedding).
If the pullback map and Y^14 are fixed, then the disclosure is entirely determined by the
geometry — there is no SBP non-determinism. The Higgs appears as a "new" field only
because the observer is restricted to X^4; from Y^14, everything is determined. This is
the computable-fixed-source scenario that E040 defeats in the Gödelian regime.

But the TI question is not about GU physics specifically. The question is: does the
Higgs-as-illusion STRUCTURE provide vocabulary for LAYER-OBL-001?

**Concrete advance to LAYER-OBL-001:**

YES, with a specific precision. The Higgs-as-illusion construction gives TI a vocabulary
for the LAYER-OBL-001 declaration:

- Higgs is illusion = A_{S_n}'s apparent novelty is observer-layer disclosure from a
  fixed Mu_infty (source layer is unchanged)
- Higgs is real = A_{S_n} carries genuinely new structure at the Y^14 / source layer
  (the source changes, not just the observer's access to it)

LAYER-OBL-001 asks: is the observed A_{S_n} evolution a Higgs illusion (derived from
fixed source by projection) or a genuine source-level modification?

The Higgs vocabulary gives a NAME for what LAYER-OBL-001 must rule out: the "Higgs
illusion scenario" where all apparent D4 novelty is actually projection from a pre-existing
fixed source. This is more precise than the SSC framing because it is positively
constructive: it says "here is what the illusion LOOKS LIKE geometrically" (a norm or
component in a higher-dimensional structure).

**Formal machinery worth importing:**

The GU Higgs-as-illusion suggests a specific test structure for LAYER-OBL-001: can every
D4 morphism in the trajectory be expressed as a "projection component" of some fixed
higher-dimensional admissibility predicate A_infty? If yes, the Higgs illusion applies
and the source-side claim collapses. If there exist SBP morphisms whose NEW TYPE cannot
be expressed as any component, norm, or projection from A_infty (for ANY choice of A_infty),
then the Higgs illusion fails and source-side novelty is genuine.

This is a more constructive formulation of the E046 creation-vs-navigation question.
The expressiveness-threshold fixture (E045 §5 item 1, Robinson-Q analog) is the right
formalism for this: it asks whether the operative source can encode its own admissibility
predicate. If the source can self-encode, then no fixed higher-dimensional A_infty can
serve as the "Higgs space" for all future SBP morphisms — because the SBP space grows
in ways that outrun any pre-committed A_infty (Gödelian productivity).

**Verdict: USEFUL FORMAL VOCABULARY with a concrete contribution to LAYER-OBL-001.**
The Higgs-as-illusion construction names the projection absorber scenario constructively
and positively. It does not resolve LAYER-OBL-001, but it gives LAYER-OBL-001 a precise
positive characterization: TI must show that NO "Higgs space" A_infty exists from which
all SBP morphisms project. The expressiveness-threshold fixture (D-FORK, E045) is the
right formal approach to this test. The GU framing does not change the underlying
mathematics but sharpens the obligation's target.

---

## D. Spinor/Chirality Parallel with D4 Witness and AC-8 Quorum

**The proposed analogy:**
GU's hard problem is getting generic chiral content (chiral fermions, matter generations,
anomaly cancellation) from higher-dimensional geometry where chirality is not naturally
present. The proposed TI parallel: TI's hard problem (E029/PP-3) is getting source-side
witness for genuinely new types rather than just disclosure of pre-existing types.
Is there a formal isomorphism between "chiral content from geometry" and "D4 witness from
AC-8 quorum"?

**Analysis:**

GU's chirality problem has a specific structure: starting from 14D with a Spin(7,7) or
related spinor group, GU needs to show that restricting to X^4 produces chiral fermion
content (specifically: the three generations of standard model fermions with the correct
gauge quantum numbers). This is a DIMENSIONAL REDUCTION problem: richer geometry in 14D
must produce specific chiral structure in 4D.

The TI PP-3 problem has a different structure: it is not about dimensional reduction but
about distinguishing source-side creation from projection-layer appearance. The spinor
chirality problem presupposes a fixed higher-dimensional space (Y^14 is fixed) and asks
how the chiral structure emerges. TI's PP-3 problem presupposes an unknown source and
asks whether the source is fixed or growing.

**Where the analogy holds:**

There is one structural parallel worth keeping: the chirality problem is about extracting
a TOPOLOGICAL invariant (chirality, an orientation class) from higher-dimensional geometry
that does not intrinsically carry it as a fixed field. Chirality in 4D emerges from the
interplay of the spinor structure and the dimensional reduction.

The TI analog: the interaction_witness for source-side novelty (E040's ORT) is also
attempting to extract a TOPOLOGICAL/structural invariant (the non-SSC-reproducibility
of the trajectory, which is a property of the global coordination structure) from a
process (AC-8 quorum) that does not intrinsically announce whether it is source-side
or projection-side.

**Where the analogy collapses:**

1. GU's chirality emerges FROM a fixed source (Y^14 is fixed; chirality is derived).
   TI's source-side witness would need to show the source is NOT fixed. The causal
   direction is opposite.

2. The "hard problem" in GU is a technical problem about representing chirality within
   a specific geometric framework. The "hard problem" in TI is a conceptual/ontological
   problem about which layer generates novelty. These are different kinds of hardness.

3. There is no isomorphism between the spinor group mechanics (a specific Lie group
   representation theory problem) and the AC-8 quorum mechanics (a multi-observer
   coordination theory problem). The formal structures are unrelated.

**Is there any import value?**

The only import worth keeping is the reminder that emergent structure (chirality from
geometry; D4 novelty from quorum process) can be a TOPOLOGICAL PROPERTY of the process
rather than a new field added ad hoc. This supports the E040/E046 finding that the ORT
proves "global-coordination-structure irreducibility" — the non-SSC-reproducibility is a
topological property of the quorum process, not a local field addition. But E040 already
captures this. There is no new content from the spinor parallel.

**Verdict: COLLAPSES under scrutiny.** The spinor/chirality parallel is a vocabulary
match between "hard problems" of different types. The causal directions are opposite
(chirality derived FROM fixed geometry; D4 witness would show geometry NOT fixed). The
formal structures (Lie group representations vs. multi-observer coordination) are
unrelated. No formal advance to TI from this analogy. The topological-property reminder
is already captured in E040/E046. Discard.

---

## E. Riemannian-Ehresmannian Framing and LAYER-OBL-001

**The proposed connection:**
LAYER-OBL-001 is the blocking obligation from E046: the PP-3 inference from global-
coordination-structure irreducibility to source-side novelty requires declaring that the
AC-8 quorum coordination process operates AT the source layer, not the observer-
coordination layer. Does the GU Riemannian-Ehresmannian framing (distinguishing geometry
types at different structural levels) provide vocabulary or formal machinery for
LAYER-OBL-001?

**Analysis:**

LAYER-OBL-001 has three sub-requirements (from E046):
1. Specify what it means for quorum coordination to change the SOURCE admissibility
   predicate (vs. the observers' SHARED REPRESENTATION of the source)
2. Show that the "global-coordination-structure irreducibility" of the ORT is a
   source-side fact, not a coordination-dynamics fact
3. Distinguish the Gödelian SBP space from the Gödelian completion of a fixed formal
   system (Platonist reading) vs. the Gödelian extension of an open-ended source
   (creationist reading)

The Riemannian-Ehresmannian framing is specifically relevant to sub-requirement 1.

**Sub-requirement 1 analysis:**

The Riemannian geometry is the "observer representation" layer: the Levi-Civita connection
is uniquely determined by the metric (the observers' shared representation of geometry).
There is no freedom at this layer; everything is derived from the metric.

The Ehresmannian geometry is the "source" layer: the principal bundle connection carries
independent gauge degrees of freedom not determined by the base-space metric. The source
layer has genuine content freedom.

The GU FUSION of these geometries (14D Observerse) is precisely the claim that the full
geometry is BOTH metric-derived (Riemannian: the X^4 slice is metrically well-behaved)
AND independently content-bearing (Ehresmannian: the Y^14 connection carries gauge degrees
of freedom that appear to X^4 observers as new fields).

**Direct application to LAYER-OBL-001 sub-requirement 1:**

For TI, the Riemannian-Ehresmannian framing suggests the following vocabulary:

- The "observer representation layer" (Riemannian) corresponds to the observers' shared
  schema S_n: it is derivable from prior shared records and admits no independent gauge
  content (everything is determined by the quorum record history)
- The "source layer" (Ehresmannian) corresponds to the admissibility predicate A_{S_n}
  carrying independent content not derivable from any fixed source Mu_infty: it has gauge-
  like degrees of freedom that the quorum introduces stage by stage

LAYER-OBL-001 sub-requirement 1 then becomes: show that A_{S_n} is EHRESMANNIAN with
respect to the quorum record history — i.e., that it carries gauge-like degrees of freedom
that are not determined by any fixed prior record, analogous to how the principal bundle
connection carries degrees of freedom not determined by the base-space metric.

**Formal precision gained:**

This reframing gives sub-requirement 1 a mathematical shape. The question becomes:

  Is A_{S_n} a CONNECTION (in the geometric sense) over the schema extension process,
  with independent gauge degrees of freedom? Or is it a LEVI-CIVITA connection — uniquely
  determined (metric-compatible, torsion-free analog) from the prior schema history?

The Ehresmannian connection is characterized by its holonomy group: a non-flat connection
has non-trivial holonomy around closed loops. The TI analog: the holonomy of the A_{S_n}
evolution around a closed schema loop (a sequence of extensions that returns to a schema
state equivalent to the starting state) would be non-trivial if and only if the connection
is genuinely Ehresmannian (source-side) rather than Riemannian (observer-derived).

**Connecting to TI-C012 and the holonomy fixture (E015):**

TI-C012 and E015 (holonomy fixture) already tested whether the Ext_S category structure
can produce a non-trivial holonomy observable. E015 found that bare Ext_S with a closed
loop does not determine a G-element; nontrivial holonomy requires an independently
specified transport functor A: ExtCat -> BG.

The Riemannian-Ehresmannian framing NOW PROVIDES A REASON to prioritize that transport
functor: if A is the "Ehresmannian connection" of the AC-8 quorum process, its holonomy
would be a source-layer invariant (non-trivial if Ehresmannian, trivial if Riemannian).
The holonomy of A would then be EXACTLY the formal test for LAYER-OBL-001:
- Trivial holonomy (Riemannian): quorum coordination is observer-layer; A is uniquely
  determined from the schema record history
- Non-trivial holonomy (Ehresmannian): quorum coordination is source-layer; A carries
  independent gauge content introduced at each stage

**Sub-requirement 3 analysis:**

The Platonist vs. creationist reading of Gödelian SBP space (E046 sub-requirement 3)
does NOT map cleanly onto the Riemannian/Ehresmannian distinction. The Riemannian/
Ehresmannian split is about degrees of freedom in a FIXED total space (Y^14 is fixed;
the question is whether the connection is derived or independent). The Platonist vs.
creationist question asks whether the TOTAL SPACE is fixed or growing. These are different
questions at different levels.

**Verdict: GENUINE ISOMORPHISM at the level of LAYER-OBL-001 sub-requirement 1;
COLLAPSES at sub-requirement 3.** The Riemannian/Ehresmannian framing provides
substantial formal vocabulary for LAYER-OBL-001 sub-requirement 1: the obligation to
show that A_{S_n} carries Ehresmannian (gauge-independent) degrees of freedom rather than
Riemannian (uniquely determined) degrees of freedom. This connects LAYER-OBL-001 directly
to the holonomy fixture work (TI-C012, E015) and suggests that a non-trivial holonomy of
the A_{S_n} connection process would be the formal evidence for source-layer declaration.
This is a concrete advance to LAYER-OBL-001.

---

## Summary Table

| GU Construction | Analogy Type | Advance to TI? | LAYER-OBL-001 Advance? |
|---|---|---|---|
| A: Y^14 / X^4 Observerse pullback | Useful vocabulary | Names LAYER-OBL-001 target more precisely | YES — frames as Ehresmannian vs. Riemannian |
| B: Riemannian-Ehresmannian fusion (torsion) | Useful vocabulary + concrete test | Suggests covariance check for SBP-incompatibility (Gauge Absorber partial discharge) | INDIRECT — Ehresmannian framing applies |
| C: Higgs emergence as illusion | Useful vocabulary + positive characterization | Names "Higgs illusion scenario" as what LAYER-OBL-001 must rule out | YES — gives constructive positive characterization |
| D: Spinor/chirality mechanics | Vocabulary match only | None | No |
| E: Riemannian-Ehresmannian + LAYER-OBL-001 | Genuine isomorphism (sub-req 1) | Connects LAYER-OBL-001 to holonomy fixture | YES — formal machinery for sub-req 1 |

---

## Concrete Advances

### 1. LAYER-OBL-001 formal precision (from B and E)

LAYER-OBL-001 sub-requirement 1 can now be formally stated using the Riemannian/
Ehresmannian vocabulary:

**LAYER-OBL-001 (Ehresmannian formulation):**
Show that the admissibility predicate evolution A_{S_n} is EHRESMANNIAN with respect
to the schema history: it carries independent gauge degrees of freedom not derivable
from any pre-committed fixed source Mu_infty, analogous to how the Ehresmannian
connection on a principal bundle carries degrees of freedom not determined by the
base-space metric.

The formal test: does the A_{S_n} evolution have non-trivial holonomy around closed
schema loops? Non-trivial holonomy would be the formal signature of the Ehresmannian
(source-layer) character of the quorum process. This reconnects LAYER-OBL-001 to the
holonomy fixture (TI-C012, E015) and the independently-specified transport functor.

### 2. "Higgs illusion test" for LAYER-OBL-001 (from C)

The Higgs-as-illusion construction gives LAYER-OBL-001 a positive characterization of
what it must rule out: the existence of a fixed "Higgs space" A_infty from which all
SBP morphisms project. Formally: for the source-side claim to hold, there must be NO
fixed admissibility structure A_infty such that for all n, all SBP morphisms from S_n
can be expressed as components or projections from A_infty.

This is equivalent to the expressiveness-threshold fixture (E045 §5 item 1): if the
operative source can encode its own admissibility predicate (Robinson-Q analog), then
no fixed A_infty can serve as the "Higgs space" for all future SBP types, because the
SBP space outgrows any pre-committed A_infty via Gödelian productivity. The Higgs
illusion fails, and source-side novelty is formal.

### 3. Covariance check for Gauge Absorber (E046 #5) (from B)

The torsion parallel suggests checking whether SBP-incompatibility is tensorial (schema-
relabeling covariant) or coordinate-dependent (removable by type relabeling). This is a
concrete next test that could partially discharge E046's Gauge Absorber (#5):
- If SBP-incompatibility is covariant (tensorial analog): gauge relabeling does not
  convert incompatible extensions into compatible ones; the SBP structure is genuine
- If SBP-incompatibility is coordinate-dependent: the absorber succeeds; the incompatibility
  is an artifact of type naming, and Mu_infty with relabeled types could reduce it

This test is formally tractable: it asks whether there exists a type relabeling bijection
phi: T_infty -> T_infty such that phi maps all SBP-incompatible pairs into compatible
pairs. If no such phi exists, SBP-incompatibility is covariant.

---

## What Analogies Hold, What Collapses

**Hold (with precision bounds):**

- **Riemannian/Ehresmannian as LAYER-OBL-001 vocabulary (A, E):** Genuine formal utility.
  The distinction between uniquely-derived connections (Riemannian, observer-layer) and
  independent gauge connections (Ehresmannian, source-layer) maps precisely onto LAYER-OBL-001
  sub-requirement 1. The holonomy signature is the concrete test. This import is bounded
  correctly: it uses structural vocabulary without importing GU physics.

- **Higgs illusion as projection-absorber characterization (C):** Genuine conceptual
  utility. It gives the Higgs illusion scenario — which is the projection absorber made
  geometrically concrete — a positive constructive form. LAYER-OBL-001 becomes: show the
  Higgs illusion scenario fails for the operative source.

- **Torsion as covariance vocabulary (B):** Useful. The torsion parallel is not a formal
  isomorphism but provides a covariance check that is not currently in the TI program.
  This is the lowest-cost concrete test among the five analogies.

**Collapse:**

- **Spinor/chirality parallel (D):** Collapses. Causal direction is opposite (chirality
  derived from fixed source; D4 witness should show source not fixed). Formal structures
  are unrelated. No import value beyond the topological-property reminder already in E040.

- **Y^14 / X^4 as Ext_S source/projection isomorphism (A, literal reading):** Collapses.
  The pullback is a static geometric operation on a fixed total space; it maps to the SSC
  (bounded-access disclosure from fixed source), the exact thing TI must escape. The
  literal reading of the Observerse as a model of Ext_S would make Ext_S a fixed higher-
  dimensional structure, which is PP-3 Hypothesis B, not Hypothesis A.

---

## File Actions

This exploration is complete. No claim status changes are warranted: the GU constructions
do not advance any TI claim to a new status. They provide vocabulary and test suggestions.

**ROADMAP.md update suggested:** Add LAYER-OBL-001 Ehresmannian formulation to the
holonomy-fixture open tasks (Phase 1F). The connection between LAYER-OBL-001 and
holonomy/TI-C012 was noted in E015 as conditional; the Riemannian/Ehresmannian framing
makes it a specific test priority rather than a conditional note.

**CLAIM-LEDGER.md update suggested for TI-C012 and TI-C019:**
- TI-C012 next_action: add "test whether non-trivial holonomy of the A_{S_n} evolution
  serves as the Ehresmannian signature for LAYER-OBL-001 sub-requirement 1"
- TI-C019 LAYER-OBL-001 note: add Ehresmannian formulation and Higgs-illusion-test
  as the two positive characterizations of what LAYER-OBL-001 requires discharging

These updates are made in-place below for reference; the steward should propagate to the
actual ledger in the next run.

---

## E047 Ledger Notes (for propagation)

```yaml
TI-C012:
  next_action_addendum: >
    Run the Ehresmannian holonomy test: check whether a transport functor A from the
    AC-8 quorum process (not from bare ExtCat alone) produces non-trivial holonomy
    around closed schema loops. Non-trivial holonomy would be the formal signature of
    Ehresmannian (source-layer) character of the quorum, supporting LAYER-OBL-001
    sub-requirement 1. This is a more motivated entry point for the transport functor
    than bare ExtCat holonomy, which E015 showed requires A independently. The motivation
    is now: A is the Ehresmannian connection of the quorum process, and its holonomy is
    the formal test of source-layer declaration.
  cross_ref: E047 (GU cross-repo check; Riemannian/Ehresmannian framing)

TI-C019:
  layer_obl_001_addendum: >
    Two positive characterizations of what LAYER-OBL-001 requires discharging (E047):
    (1) Ehresmannian test: show A_{S_n} carries gauge-independent degrees of freedom not
    derivable from any fixed source — the Ehresmannian formulation. Formal signature:
    non-trivial holonomy of the A_{S_n} connection process (connects to TI-C012, E015).
    (2) Higgs-illusion test: show no fixed A_infty exists such that all SBP morphisms
    from any S_n can be expressed as components or projections from A_infty. This is
    equivalent to the expressiveness-threshold fixture (Robinson-Q analog, E042 §6.2,
    E045): Gödelian productivity ensures no such A_infty can serve as the "Higgs space."
    Neither characterization closes LAYER-OBL-001 — both point at the expressiveness-
    threshold fixture (D-FORK) as the correct resolution mechanism.
  cross_ref: E047 (GU cross-repo check; Higgs-illusion characterization)
```
