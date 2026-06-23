---
artifact_type: exploration
status: active
exploration_id: E030
run_ref: RUN-0047
date: 2026-06-22
topic: issuance_rate_dynamics_metabolic_scaling_legitimacy_stability
source: five_sequential_persona_passes
claim_refs:
  - TI-C019
  - TI-C020
intake_items_evaluated:
  - A: optimal_issuance_rate_curve_lambda_star
  - B: metabolic_scaled_source_measure_mu_M
  - C: legitimacy_stability_connection_epistemic_inflation
  - D: declining_issuance_curve_tokenomics
  - E: investigation_routes_lambda_star_native_vs_absorbed
personas:
  - Hostile Absorber (Optimal Control + Variational)
  - Non-Equilibrium Thermodynamicist
  - Monetary Economist / Tokenomics Expert
  - Category Theorist / Sheaf Theorist
  - Source-Side Witness Auditor
---

# E030: Five-Run Issuance Rate, Metabolic Scaling, and Legitimacy-Stability Intake

## Purpose

Evaluate five new cross-repo proposals (A-E) against Temporal Issuance's formal apparatus and
kill criteria. All five were generated in a parallel session on 2026-06-22 and need absorber
testing before any of them can influence TI claims or the formal object.

The five intake items are:

```text
A. Optimal issuance rate: lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]
   proposed as the dynamics equation for Ext_S

B. Metabolic-scaled measure: mu_M(r) = c * |r|^{3/4}
   proposed as a candidate for mu in the formal object

C. Legitimacy-stability connection (from IEAH E006):
   epistemic inflation + Ostrom SES framework;
   "trust in the message requires trust in the system holding the message"

D. Declining issuance curve from tokenomics (Jermann & Xiang 2024):
   high early / tapered late / hard-coded schedules = credibility

E. Investigation routes: is lambda*(s) TaF/TI-native or absorbed by generic optimal control?
```

---

## Run 1: Hostile Absorber (Optimal Control + Variational Methods)

**Persona:** A variational methods expert trained in optimal control, calculus of variations,
and dynamic programming. Hostile posture: every new dynamics equation gets tested against
whether it is just a relabeling of Pontryagin, Bellman, or classical free-energy minimization.

### Assessment of Item A

The proposed lambda*(s) equation is:

```text
lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]
```

**Absorber test 1: Bellman / dynamic programming.** This is a static optimization at each
state s. If s is interpreted as a state variable and lambda as a control, this is the
instantaneous reward maximization step of a Bellman equation. The right-hand side is a net
benefit functional: N is the value of novelty (like a reward), C is a reconciliation cost
(like a transition cost), K is a collapse/instability risk (like a constraint penalty).
In standard optimal control, one would write H(s, lambda, p) = N - C - K and maximize over
lambda at each point. This is Pontryagin's maximum principle applied to a net-benefit
Hamiltonian.

Verdict on A: **absorbed by generic optimal control unless at least one of N, C, K is a
TI-native object that cannot be expressed in standard state-dependent cost/reward terms.**

Specifically:

- If N(lambda,s) = rate of D4 events or new morphisms in Ext_S, this is TI-native and not
  directly available in standard optimal control state spaces.
- If C(lambda,s) = reconciliation cost across observer G_ij maps, this could be TI-native.
- If K(lambda,s) = schema fixed-point risk (PP-3 style collapse), this is TI-native.

But as written, N, C, K are undefined. The equation is a schema, not a claim. It is absorbed
until the functionals are given TI-native definitions.

**Absorber test 2: Free-energy minimization (FEP).** If N is interpreted as prediction
accuracy and C as model complexity, the functional reduces to a form of variational free
energy. Friston's active inference would say: minimize free energy (= C + K) subject to
maximizing model evidence (= N). This is the most dangerous absorber because it comes with
a full mathematical apparatus including gradient descent, belief updating, and approximate
Bayesian inference. The equation only escapes this absorber if N is schema-type novelty at
the OnlineSchemaSys level, not model-fit novelty.

**What survives absorber pressure on A:**

- The three-term decomposition (N - C - K) is a useful organizing frame for TI's tension
  between issuance rate and coherence cost. But this is a *framing*, not a theorem.
- The concept that there is an optimal issuance rate (not too high = chaos, not too low =
  schema fixed-point) is consistent with TI's North Star and not blocked by kill criteria.
- PP-3 pressure applies: lambda*(s) as a projection-layer quantity could be maximized without
  the source expanding. A source-layer optimal rate requires s to be specified at the source
  layer, which inherits all of PP-3's unresolved status.

**Strongest insight from Run 1:** If N(lambda,s) is given a TI-native definition as the
*density of D4-morphisms in Ext_S at rate lambda*, and K(lambda,s) is defined as the
*probability that Ext_S enters a schema fixed-point trajectory within a bounded horizon*,
then the equation is not absorbed by generic optimal control because those objects are not
available in standard state spaces. The cost function would need to be defined over morphism
categories, not over scalar state variables.

**Strongest critique from Run 1:** The equation has three undefined functionals (N, C, K)
and one undefined state space (s). In this form it is not a TI claim — it is a placeholder.
Importing it as a "dynamics equation for Ext_S" before N, C, K are defined at the
category-morphism level would be a K3 kill: no formal work is being done, only the appearance
of formalism.

**Heterodox next step (Run 1):** Define N as a morphism-density functor on Ext_S: the
cardinality of new morphism types produced per prefix step. Define K as the probability that
the Ext_S trajectory (S_0, S_1, ...) becomes eventually-constant given rate lambda. Then
lambda*(s) becomes a rate-optimization problem over the trajectory-level non-eventually-constant
condition from E028. This is the minimal TI-native reading that avoids K3.

**Theorem or claim candidate (Run 1):**

```text
Claim candidate: At source-layer Ext_S, there exists a critical issuance rate lambda_c(s)
below which the expected trajectory of (S_n) eventually-constant probability exceeds a
threshold epsilon. The function lambda_c(s) is a source-side property distinct from any
projection-layer analog and constitutes a positive source-side witness for PP-3 purposes if
it can be exhibited without reference to a fixed Mu_infty.

Note: this candidate is speculative. It inherits PP-3 ambiguity and requires N, K to be
defined at the source layer, not the projection layer.
```

**What previous runs missed:** E028 and E029 focused on whether individual D4 events are
source-side. They did not consider whether a *rate* of D4 events at the source layer would
be a qualitatively different witness than individual events. A rate-level argument might
escape the E029 finite-trace critique: no finite trace distinguishes source expansion from
aperture disclosure at event-by-event level, but a *rate profile* over unbounded sequences
might be more constraining (since a fixed Mu_infty with widening apertures has a terminating
rate, while a genuinely online source has a non-terminating rate).

---

## Run 2: Non-Equilibrium Thermodynamicist

**Persona:** A physicist working in non-equilibrium statistical mechanics, Prigogine/England
tradition, with strong awareness of metabolic scaling theory (West-Brown-Enquist). Hostile
to any claim that invents new physics without earning it, but constructive about grounding
formal objects in known non-equilibrium phenomena.

**What previous runs missed:** Run 1 found a potential escape from optimal-control absorption
via morphism-density functors. Run 2 must test whether Item B's metabolic scaling gives mu
a grounded non-equilibrium definition that survives thermodynamic absorption.

### Assessment of Item B

The proposed mu_M(r) = c * |r|^{3/4} is drawn from West-Brown-Enquist (WBE) metabolic
scaling theory. In WBE, metabolic rate B scales as M^{3/4} because hierarchical vascular
networks minimize total impedance subject to space-filling constraints. The 3/4 exponent
emerges from optimizing energy delivery over a fractal-like branching network.

**Absorber test 1: Is this just metabolic rate?** Yes, in its origin. mu_M as proposed is
a rescaling of biological metabolic rate. For TI, the question is whether the WBE mechanism
-- joint optimization of energy delivery and transport geometry -- has a structural analog in
the Ext_S formal object that would give mu a non-biological grounding.

**Absorber test 2: Does sublinearity / non-additivity add TI-specific content?** The claimed
key property is that mu_M is sublinear: larger systems are more efficient per unit than the
sum of their parts. In thermodynamic terms this is a superextensive capacity or an economy
of scale in dissipation. This is well-documented in complex systems (cities, organisms,
networks) and is not TI-native. Non-additivity of a measure is standard in statistical
mechanics (e.g., Tsallis entropy is non-additive) and is absorbed by known physics.

**Absorber test 3: Does |r|^{3/4} have meaning for formal objects?** The variable r is
undefined in the TI context. If r is a realized constraint complex (an element of C or an
object in Ext_S), then |r| would need a cardinality or complexity measure on that object.
WBE's M is mass. Without specifying what |r| means for formal source-side objects, the
functional form has no TI-native content.

**What survives absorber pressure on B:**

The WBE mechanism provides a *template* for how a measure could be non-additive while still
being derivable from network optimization. If Ext_S has a hierarchical structure (extensions
build on extensions, forming tree-like or fractal-like dependency chains), then a mu that
scales sublinearly with the size of the constraint complex could be derived from an
analog of the WBE argument applied to morphism composition chains. This would give mu
a non-circular, non-additive definition grounded in the structure of Ext_S itself.

**However:** mu's current status in FORMAL-OBJECT.md is "demoted to an unresolved measure
candidate." The open questions for mu are: units, transformation behavior, and an operational
split from volume, entropy, and information. WBE metabolic scaling answers none of these
questions directly. It gives a functional form without answering the conceptual question of
what mu measures.

**Critical PP-3 application:** Even if mu_M were well-defined for source-side objects, it
would measure the issuance *capacity* of a realized constraint complex. This is a
source-side quantity only if r refers to source-layer objects. If r refers to
observer-accessible objects, mu_M is a projection-layer measure and inherits PP-3 ambiguity.
A WBE-structured mu is compatible with both: a fixed richer source could have a WBE-structured
accessibility aperture that discloses schema with a 3/4-power rate.

**Strongest insight from Run 2:** The WBE template's true value for TI is not the exponent
3/4 but the *derivation mechanism*: the exponent emerges from optimizing over network
geometry. If Ext_S admits a network geometry (where morphisms form branching chains with
bounded fan-out), then a mu could potentially be derived from minimizing something analogous
to total morphism-composition impedance. This would make mu a *derived* quantity from Ext_S
structure, not an imported biological constant.

**Strongest critique from Run 2:** mu_M = c * |r|^{3/4} is thermodynamically absorbed.
WBE is a well-established theory. Sublinear scaling is known in complex systems. The only
way B escapes absorption is by deriving the analog of the WBE argument from category-level
Ext_S structure, which requires specifying (a) what |r| means in Ext_S, (b) what the
minimized quantity (analogous to total transport impedance) is in the formal object, and (c)
why the resulting exponent is 3/4 rather than some other value. None of these are specified.
As imported from WBE, this is a costume change on known physics, not a TI-native measure.

**Heterodox next step (Run 2):** Attempt the WBE derivation in the Ext_S setting. Define
a *morphism composition chain* of length k as a sequence of admissible extensions
e_1, e_2, ..., e_k where each extends the previous. Define |r| as the minimum chain length
required to reach state r from the initial schema C_0. Then ask: is there a natural
minimization principle on Ext_S such that the optimal mu (measuring issuance capacity) scales
as a power of |r|? If the minimization is over total extension cost in a hierarchical
dependency network, a sub-extensive exponent could emerge. The 3/4 is not guaranteed but
the sub-extensive regime is a testable outcome.

**Theorem or claim candidate (Run 2):**

```text
Claim candidate: If Ext_S admits a hierarchical morphism-composition network with bounded
fan-out, there exists a derived measure mu_{Ext}(r) that is sub-extensive in the minimum
chain-length depth of r. The exponent and derivation depend on the specific minimization
principle over morphism chains; the WBE 3/4 is one instance when the minimization is
over a transport-impedance analog.

Status: speculative. Requires defining chain-length, fan-out, and minimization principle
for the Ext_S category before this can be pressed as a TI claim.
```

**What previous runs missed:** The entire E028/E029 thread treated mu as unresolved but
never asked whether mu's resolution requires understanding the *internal structure of Ext_S*
(its morphism composition network). WBE's value is not the formula but the demonstration
that sub-extensive scaling can be derived from network structure. The formal question of
what network structure Ext_S has is separate from PP-3 and would make progress independent
of the source/projection problem.

---

## Run 3: Monetary Economist / Tokenomics Expert

**Persona:** An economist with expertise in monetary theory, mechanism design, and
crypto-economic protocol design. Familiar with the Jermann-Xiang (2024) framework and the
broader literature on commitment devices and credibility in monetary policy. Skeptical of
importing financial metaphors into physical ontology. Constructive about formal commitment
structures.

**What previous runs missed:** Runs 1 and 2 found that A and B are absorbed unless TI-native
functionals are defined. Run 3 must evaluate whether Item D (declining issuance curve) and
Item C (legitimacy-stability connection) add formal content that the category-theory layer
cannot supply, or whether they are just economic analogs of existing TI ideas.

### Assessment of Item D

The Jermann-Xiang finding: gradually declining issuance rates are optimal, with high early
issuance bootstrapping the system and tapering to low stable rate at maturity.
Hard-coded schedules are credibility-enhancing because they are commitment devices.

**Absorber test: is this Bitcoin's halving schedule restated as economic theory?**
Jermann-Xiang formalize a known empirical feature of tokenomic design. The formal mechanism
is a time-inconsistency problem: an issuer who can expand supply at will has incentive to
inflate, reducing trust. A hard-coded declining schedule removes this incentive
ex ante, anchoring expectations. This is Kydland-Prescott rules-vs-discretion applied
to token issuance.

For TI, the parallel would be: a source that can issue schema extensions at any rate has
an incentive analog to "issuance at the cheapest cost" without regard to coherence. A
hard-coded declining rate would be a commitment device for schema stability at maturity.

**Critical problem:** TI's source layer is not an agent with incentives. TI-C019 explicitly
blocks importing rational agents, Nash equilibria, and goal-seeking from the governance
constraints (see E028's governance constraint 3 and E028's "kills_the_framing" finding on
agency and Nash equilibria). The declining issuance curve requires an issuer with
preferences and a time-inconsistency problem. Neither is available in TI's formal object.

**What survives absorber pressure on D:**

The *structural* content of the declining curve, stripped of incentive language: a process
with high initial schema-extension rate that tapers as the process matures could be a
natural feature of an Ext_S trajectory. In combinatorial terms: early in a process, each
new schema element is type-novel relative to a small S_0; later, most additions are
refinements within an established schema. This produces a naturally declining D4 event rate
over time without any agent or incentive structure.

This is significant: the declining rate could be a *theorem* about OnlineSchemaSys
trajectories rather than a mechanism design choice. If D4 event frequency is bounded by
the number of undecidable propositions relative to S_n (via the Gödelian mechanism in E028),
and if that number per step decreases as S_n becomes more expressive, then a declining rate
follows from the logic of self-referential schema systems, not from monetary policy.

**Assessment of Item C (legitimacy-stability connection):**

The phrase: "trust in the message requires trust in the system holding the message" is the
AC-8 quorum legitimacy problem stated in natural language. The Ostrom SES framework
contribution is the self-governing commons model: participants must have ongoing redistribution
of capacity to participate or the system develops a capture attractor.

For TI, the AC-8 connection is direct and was already partially identified in E028 (quorum
legitimacy condition) and E029 (interaction witness). The epistemic inflation risk is a
formal model for what E028 called "synchronization collapse" in multi-observer settings: if
early participants establish the schema and all later participants can only ratify pre-issued
types, the D4 event rate falls to zero at the projection layer even if the source is still
online.

**The Ostrom capture attractor is the multi-observer analog of PP-3:** At the social/protocol
layer, it is a fixed Mu_infty (the founding participants' schema) with widening apertures
for new participants who can only access pre-existing types. This means Item C operationalizes
PP-3 at the shared-legitimacy layer: a quorum without redistribution of schema-extension
rights drifts toward bounded-aperture disclosure, not source-side issuance.

**What survives absorber pressure on C:**

The redistribution requirement maps directly to the AC-8 fork-choice rule: for D4 events
to count as genuine shared issuance (not just dominant-coalition aperture disclosure), new
participants must retain the ability to propose incompatible schema extensions and have those
extensions processed by the quorum rule. Without this, AC-8 is a bounded-aperture disclosure
system, not a source-expansion system.

**Strongest insight from Run 3:** Item C (Ostrom capture attractor) is not absorbed by
existing TI claims. The quorum legitimacy condition in E028 identified the requirement but
did not supply the redistribution mechanism. Ostrom's SES framework provides a *formal model*
for the redistribution condition: participants retain ongoing rights to propose changes to
admissibility rules, not just to access existing types. This is a structural requirement for
AC-8 that was previously unnamed.

**Strongest critique from Run 3:** Item D (declining curve) is absorbed at the mechanism
level because it requires an issuer with preferences. The structural content (declining D4
rate at maturity) is compatible with TI but was already implicit in the trajectory-level
non-eventually-constant condition from E028: a non-eventually-constant trajectory need not
have a constant D4 rate -- it only requires non-termination. A declining rate with a
non-zero long-run floor is consistent with non-eventually-constant, but the declining
feature is not a new formal claim.

**Heterodox next step (Run 3):** Formalize the Ostrom redistribution condition in AC-8 as
a *source-expansion right*: each participant (observer site O_i) retains the right to submit
incompatible schema proposals that reach quorum processing, distinct from the right to submit
extensions within the current schema. This would split the quorum rule into two layers:
(a) intra-schema extension ratification (existing proposal mechanism) and (b) schema-boundary
proposal processing (new right). Without (b), AC-8 degenerates to bounded aperture by
structural drift, not by formal necessity. This is a testable formal addition.

**Theorem or claim candidate (Run 3):**

```text
Claim candidate (AC-8 Redistribution Theorem):
In a multi-observer system satisfying NAA and the E028 quorum legitimacy condition, if
schema-boundary proposal rights are not structurally protected (i.e., if only intra-schema
extensions can reach quorum), then the system is formally equivalent to a projection-layer
OnlineSchemaSys over a fixed source schema Mu_infty, regardless of the number of observers
or the diversity of their local states. This is the formal capture-attractor at the
shared-legitimacy layer.

Corollary: A positive source-side witness for AC-8 must include protection of
schema-boundary proposal rights, making them formally distinct from intra-schema ratification.
This provides one of the five PP-3 witness types (interaction_witness).
```

**What previous runs missed:** Runs 1 and 2 focused on the formal object's internal
structure (rate dynamics, mu's network derivation). Run 3 finds that Item C provides the
clearest current candidate for a PP-3 interaction witness -- the Ostrom redistribution
condition operationalizes what it would mean for multi-observer interaction to be a
source-side constraint change rather than shared aperture disclosure.

---

## Run 4: Category Theorist / Sheaf Theorist

**Persona:** A category theorist specializing in sheaf theory, topos theory, and categorical
semantics for dependent type theory. Knows the TI formal apparatus in detail from E017
(categorical formalization of D4) and E024 (presheaf AB absorber test). Hostile to
hand-waving about "categories" without specifying functors, natural transformations, and
universal properties. Constructive about finding the right categorical level for new claims.

**What previous runs missed:** Run 1 identified morphism-density functors as a TI-native
reading of N(lambda,s). Run 2 asked whether Ext_S has a network structure. Run 3 found an
AC-8 redistribution theorem candidate. Run 4 must determine whether lambda*(s) (Item A) and
mu_M (Item B) can be placed in the Ext_S categorical setting without losing what makes
them interesting, and whether Item E's investigation routes are categorically tractable.

### Assessment of Item A in categorical terms

The proposed optimization:

```text
lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]
```

For this to be a categorical object, the following must be specified:

- s: an object in Ext_S (a typed source constraint state or morphism class)
- lambda: a parameter indexing a family of functors from Ext_S to some target category
- N, C, K: natural transformations or functors measuring novelty, cost, and stability

The most natural categorical reading: lambda parameterizes the *functor class* from Ext_S
to the target category of issuance processes (e.g., LorHist_g(M) from RUN-0026 or a simpler
abstract target). N(lambda,s) would be a measure of how many new morphism types are generated
by F_lambda at object s. C(lambda,s) would measure the cost of the reconciliation functor
G_ij at that rate. K(lambda,s) would measure how close the trajectory F_lambda(S_0),
F_lambda(S_1), ... is to eventually-constant.

**Sheaf-theoretic layer:** If s is a point in a sheaf over observer patches, then
lambda*(s) defined pointwise would need to satisfy the sheaf gluing condition: the optimal
rates at each patch must glue to a consistent global rate. This is not guaranteed. In the
presence of AC-8 incompatible proposals, the gluing condition fails, and lambda*(s) is only
a local section, not a global one.

This is a genuine formal observation: **lambda*(s) may not be a globally-defined quantity**.
Instead, it could be a section of a presheaf over observer configurations, defined locally
at each observer's accessible schema but not necessarily glueable to a single global optimal
rate. This is a TI-native obstruction that does not appear in generic optimal control.

**Assessment of Item E: is lambda*(s) TaF/TI-native or absorbed?**

From the categorical perspective:

- If s is a scalar state variable and N, C, K are real-valued functions, then lambda*(s) is
  a standard optimal control problem (Pontryagin) and is fully absorbed.
- If s is an object in Ext_S (a typed constraint state in the category) and N, C, K are
  functors, then lambda*(s) is a *functor optimization* problem. This is not standard optimal
  control because the target space (Ext_S objects) has morphism-level structure that is not
  captured by scalar state variables.
- The TaF question is whether time-as-finality's ordering structure (realization order) gives
  lambda*(s) additional constraints not in TI. Since TaF's ordering is TI's <=_S (killed as
  an independent primitive in RUN-0024 but surviving as a derived invariant), TaF provides
  an instance of s-indexing but not an independent formal object.

**Verdict on E:** lambda*(s) is TI-native if and only if s is an object in Ext_S and the
functionals N, C, K are defined over Ext_S morphisms. It is absorbed by generic optimal
control if the categorical structure of Ext_S is ignored.

**Assessment of mu_M in sheaf terms:**

mu_M as a measure on realized structure must satisfy measurability conditions on the Ext_S
category. In categorical terms, a measure is a functor from a measurable category to the
reals. For mu to be non-additive in the sublinear WBE sense, it must fail to be a direct
sum over sub-objects. This is the categorical analog of a non-additive measure (like a
capacity or a Choquet integral over a lattice of subsets).

The sheaf-theoretic version: mu is a measure on sections of a sheaf over source-constraint
patches. Non-additivity means the measure of the union of patches is less than the sum of
measures of individual patches. In sheaf theory, this can arise from sheaf cohomology:
H^1 non-triviality signals that local sections do not add up globally, producing a
non-additive obstruction.

This is a clean categorical mechanism for sub-extensive mu: **mu is sub-extensive because
Ext_S has non-trivial H^1**, meaning that source-side extensions do not combine additively.
If this cohomology is non-zero, it is a TI-native explanation for sub-extensive scaling
that does not require importing WBE's biological network story.

**Strongest insight from Run 4:** The sheaf-cohomological explanation of mu's sub-extensivity
-- H^1 non-triviality on Ext_S -- is cleaner and more TI-native than WBE metabolic scaling.
It would also supply the first formal connection between the T36 sheaf audit (from E022,
which found TI-C017's Cech cohomology claim is premature) and the formal object: if mu's
sub-extensivity is grounded in H^1 of Ext_S, then sheaf cohomology is no longer just a
physics-bridge speculation but a structural feature of the source-side formal object.

**Strongest critique from Run 4:** None of the categorical structures above (functor
optimization, section presheaf, sheaf cohomology) are specified for Ext_S. Before claiming
that lambda*(s) is a functor optimization or that mu is H^1-derived, the category structure
of Ext_S must be given explicitly: objects, morphisms, composition, and the functor from
Ext_S to whatever target represents issuance output. This was identified as the next required
formal pass after RUN-0025 (category-first correction) but has not been completed. Items A
and B cannot be incorporated until that category specification is done.

**Heterodox next step (Run 4):** Fix the category structure of Ext_S minimally: objects are
typed schema states, morphisms are admissible extensions, composition is extension
composition, and there is a functor Target: Ext_S -> Meas (measurable spaces). Then define
N, C, K as natural transformations over this functor. The optimization lambda*(s) becomes a
natural transformation optimization problem: find the functor parameterization lambda that
maximizes the net-benefit natural transformation pointwise. Prove whether such an optimizing
lambda exists (existence theorem) and whether it is unique (uniqueness, requiring the target
category to be well-ordered or convex). This is a well-posed categorical question.

**Theorem or claim candidate (Run 4):**

```text
Claim candidate (Sheaf-Cohomological mu Theorem):
If Ext_S admits a sheaf structure over observer patches with non-trivial H^1, then any
measure mu on realized source-constraint complexes that respects the sheaf's gluing
conditions is necessarily sub-extensive: mu(A union B) < mu(A) + mu(B) for overlapping
patches A, B when the H^1 obstruction is non-zero. This provides a TI-native explanation
for sub-extensive issuance measure without importing WBE's biological network derivation.

Status: speculative. Requires specifying the sheaf structure on Ext_S and computing its
Cech cohomology in the simplest non-trivial case (two observer patches with non-compatible
admissibility predicates per E029's C1 intake action).
```

**What previous runs missed:** Runs 1-3 treated the absorber question about A and B at the
level of content (are the ideas novel?) rather than at the level of formalization (is the
categorical structure in place for the ideas to even be stated as TI claims?). Run 4's
contribution is the meta-absorber point: **items A and B cannot be assessed until Ext_S is
given a complete category specification**, which is the outstanding formal work since
RUN-0025's category-first correction.

---

## Run 5: Source-Side Witness Auditor

**Persona:** A hostile auditor whose only job is to apply E029's positive source-side witness
requirement. Every new proposal is tested against the five witness types from E029
(source_access, static_source_obstruction, generator_issuance, interaction_witness,
physical_witness). Nothing passes unless it satisfies at least one of these. The auditor also
applies the RUN-0028 Q residue: does the new proposal help ground Q (the morphism-level
source invariant) in a way that is not absorbed by existing frameworks?

**What previous runs missed:** Runs 1-4 found conditional survival paths for each item.
Run 5 asks the harder question: do any of these items, even with their strongest readings,
satisfy the E029 witness requirement well enough to narrow the PP-3 gap?

### Applying the Five Witness Types to All Items

**Item A (lambda*(s)) against witness types:**

- source_access: lambda*(s) is an optimization over the source schema rate. If s is source-layer,
  this is a source-access witness attempt. But the optimization requires a source-layer
  objective function, which requires knowing that N, C, K are source-layer quantities.
  Conditional pass: only if N is defined as source-layer D4 event density.
- static_source_obstruction: a source-rate optimization does not by itself obstruct a fixed
  Mu_infty interpretation. A fixed large source with varying aperture would also have an
  optimal disclosure rate. Does NOT satisfy this witness type as currently stated.
- generator_issuance: lambda*(s) is a rate parameter, not a new generator kind. Does not
  satisfy.
- interaction_witness: if lambda*(s) is determined jointly by AC-8 negotiation across
  observers (as Run 3's Ostrom analysis implies), then it could become an interaction
  witness. Conditional pass: only if the AC-8 redistribution theorem holds.
- physical_witness: lambda*(s) has no physical layer specification. Does not satisfy TI-C020.

**Verdict on A as a PP-3 witness:** Not a standalone PP-3 witness. Could become one
if paired with the AC-8 interaction_witness route (Run 3) and if N is defined at the source
layer (Run 1). As a standalone item, absorbed by E029's bounded-aperture construction.

**Item B (mu_M = c * |r|^{3/4}) against witness types:**

- source_access: mu_M would need to measure a property of source-layer objects r. If r is
  a source-constraint complex and |r| is its chain-length depth in Ext_S, this could be a
  source-layer quantity. Conditional pass: requires chain-length to be a source-layer
  invariant, not a projection artifact.
- static_source_obstruction: sublinear scaling does not obstruct a static source. A fixed
  Mu_infty with a hierarchical structure would also have sublinear mu_M over its sub-objects.
  Does NOT satisfy.
- generator_issuance: does not exhibit a new generator kind. Does not satisfy.
- interaction_witness: does not involve multi-observer interaction. Does not satisfy.
- physical_witness: WBE is a biological/physical theory, but it is not a TI physical
  witness because it does not show that the observable algebra or admissible type schema
  expands in a way not representable by bounded access to a fixed Hilbert structure.

**Verdict on B as a PP-3 witness:** Does not satisfy any witness type as currently stated.
The sheaf-cohomological reading (Run 4) could make it a static_source_obstruction candidate
if H^1 non-triviality is shown to be incompatible with a fixed Mu_infty, but this requires
proving that H^1 = 0 for all fixed-source-plus-aperture constructions (a non-trivial theorem).

**Item C (Ostrom redistribution / legitimacy-stability) against witness types:**

- source_access: the redistribution condition is about who can propose schema changes, not
  directly about the source layer. Projection-layer social process.
- static_source_obstruction: if schema-boundary proposal rights are formally protected
  and enforced through quorum, then the AC-8 process cannot be reduced to a fixed Mu_infty
  plus aperture, because incompatible proposals require the shared admissibility predicate
  to change -- which requires the source schema to change. This is a **genuine
  interaction_witness candidate**.
- generator_issuance: indirectly -- if schema-boundary proposals are incompatible generators,
  then their quorum acceptance is generator issuance. Weak but non-zero satisfaction.
- interaction_witness: **YES, strongest candidate.** Multi-observer schema negotiation with
  incompatible proposals that change shared admissibility predicate is the interaction_witness
  type from E029. The Ostrom redistribution mechanism specifies *what structural condition*
  is required for that interaction to qualify as source-side rather than bounded aperture.

**Verdict on C as a PP-3 witness:** Item C (with the Ostrom redistribution formalization)
is the **strongest current PP-3 witness candidate** among the five intake items. It satisfies
the interaction_witness type from E029 and provides the structural condition (schema-boundary
proposal rights) that was previously unnamed. This is a genuine addition to the TI apparatus.

**Item D (declining issuance curve) against witness types:**

- Does not satisfy any witness type. The declining curve is a mechanism design choice for
  agents with time-inconsistency problems. As a structural property of OnlineSchemaSys
  trajectories (declining D4 rate at maturity), it is interesting but not a PP-3 witness.

**Verdict on D:** Not a PP-3 witness. Potentially useful as a descriptive property of
Ext_S trajectories under the Gödelian mechanism (Run 3), but no formal witness work done.

**Q-residue test (RUN-0028):** Does any item help ground Q: Mor(ExtCat) -> ([0,inf), +)?

- Item A: lambda*(s) is a rate, not a morphism-level invariant. But if N is defined as
  D4-event density at rate lambda, the optimization implicitly uses a measure over morphisms.
  The optimal rate lambda*(s) might be related to Q(e) for morphisms e in Ext_S: if
  Q(e) measures the "weight" of a morphism, then the rate optimization is over Q-weighted
  morphism densities. Conditional: A might help ground Q if N is formalized as a Q-density.
- Item B: mu_M over realized structure r is not a morphism-level invariant. Does not
  directly help Q.
- Item C: the quorum legitimacy condition assigns a formal "validity" to schema-boundary
  proposals. If validity is a morphism-level property (a D4 event is valid iff it satisfies
  the quorum-legitimacy + redistribution conditions), then quorum-validity could be a
  component of Q. This is the most direct Q-grounding candidate.
- Items D, E: do not help ground Q.

**Strongest insight from Run 5:** Item C (Ostrom redistribution as AC-8 structural condition)
is the most valuable of the five items for TI's current primary need. It provides: (a) an
interaction_witness candidate for PP-3, (b) a structural condition for AC-8 that was
previously missing, (c) a possible component of Q (quorum-validity as morphism-level
property). These are exactly what PP-3's "next required test" (source_side_witness_fixture)
needs.

**Strongest critique from Run 5:** Items A, B, and D are absorbed, ungrounded, or not PP-3
witnesses as currently stated. Importing all five as TI-native ideas without the witness
auditor would inflate the formal object with unearned content, violating the absorber
discipline the repo has maintained through RUN-0046.

**Heterodox next step (Run 5):** Construct the AC-8 source-expansion fixture using the
Ostrom redistribution condition as the core structural requirement. Specify formally:
(a) the schema-boundary proposal right as a morphism class in Ext_S, (b) the quorum
legitimacy condition as a predicate on D4 event sequences, (c) the redistribution rule as
a structural constraint on the AC-8 update functor, (d) prove that without (c), AC-8 is
equivalent to bounded aperture disclosure. This is a completable formal exercise that
directly advances PP-3.

**Theorem or claim candidate (Run 5):**

```text
Claim candidate (Ostrom Witness Theorem):
In a multi-observer TI system satisfying NAA and the E028 quorum legitimacy condition,
define a schema-boundary proposal right as the formal capacity of an observer O_i to submit
an extension e: S_n -> S_n' where S_n' is incompatible with any extension producible by
delta_n over S_n. If all observer sites O_i retain schema-boundary proposal rights, then
the shared schema sequence (S_n) cannot be reproduced by any fixed Mu_infty plus widening
apertures, because any fixed Mu_infty would have to contain all possible incompatible
extensions pre-committed -- but incompatibility is defined relative to the current shared
schema S_n, which itself evolved via prior incompatible proposals.

Informally: a commons with ongoing redistribution of schema-extension rights is formally
not a bounded disclosure from a fixed source.

Status: candidate for the interaction_witness PP-3 route. Requires proving the self-reference
in the definition of incompatibility blocks the fixed-Mu_infty construction.
```

**What previous runs missed:** Runs 1-4 each found a partial finding. Run 5's contribution
is cross-referencing all five items against the specific E029 witness requirement and finding
that only Item C survives. Items A, B, D are absorber casualties at the PP-3 level. Item E
(investigation routes) is not an item itself but a meta-question, which Run 4 answered: it
depends entirely on whether Ext_S has a complete category specification.

---

## Cross-Run Synthesis

### What Survives Absorber Testing

**Genuinely new to TI and not absorbed:**

1. **AC-8 Redistribution Condition (Item C, primary):** The Ostrom SES redistribution
   requirement -- that ongoing schema-extension rights must be protected at the
   schema-boundary level, not just intra-schema ratification -- is new to TI and satisfies
   the E029 interaction_witness type. This is the strongest intake finding.

2. **The global-section obstruction for lambda*(s) (Run 4):** The finding that lambda*(s)
   may not be a globally-defined section (sheaf gluing fails under incompatible proposals)
   is TI-native and not present in generic optimal control. This is a structural property
   of the issuance rate that follows from AC-8 incompatibility.

3. **The declining D4 rate as a Gödelian structural consequence (Run 3):** The observation
   that D4 event frequency may naturally decline as S_n becomes more expressive (because
   per-step undecidability requires longer proofs) is TI-native and not imported from
   tokenomics. It is a structural feature of self-referential OnlineSchemaSys.

4. **The Q-grounding via quorum-validity (Run 5):** If quorum-valid schema-boundary
   proposals are the primary class of morphisms in Ext_S that carry the Q weight, then
   Item C provides a concrete proposal for what Q measures: the legitimacy weight of a
   morphism, determined by quorum propagation.

### What Is Absorbed

**Absorbed by existing frameworks (not TI-native as stated):**

1. **lambda*(s) as a scalar optimal control problem (Item A, generic reading):** Absorbed
   by Pontryagin / Bellman / FEP unless N, C, K are defined as TI-native category-level
   functionals.

2. **mu_M = c * |r|^{3/4} as imported from WBE (Item B, as stated):** Absorbed by WBE
   metabolic scaling theory and non-equilibrium thermodynamics. The sub-extensive functional
   form is not TI-native.

3. **Declining issuance curve as tokenomics mechanism design (Item D):** Absorbed by
   Kydland-Prescott rules-vs-discretion and Bitcoin halving mechanism design. The
   agent-with-preferences structure required for the mechanism blocks import into TI.

4. **Epistemic inflation as a social process description (Item C, surface reading):**
   The IEAH framing (increasing returns of collaboration + capture attractor) is absorbed
   by social choice theory and commons literature unless it is formalized as the AC-8
   redistribution condition above.

### What Is in Tension with Kill Criteria

**K2 (Circularity) risk:**

- lambda*(s) if s is indexed by ordinary time violates K2. The state s must be indexed
  by prefix number n (OnlineSchemaSys prefix) without reference to clock time.
- The declining curve (Item D) as stated uses maturity as a time-indexed quantity. Must
  be re-expressed as a function of S_n complexity or Gödelian expressivity, not clock time.

**K4 (No Distinguishable Claims) risk:**

- mu_M = c * |r|^{3/4} as imported from WBE is a K4 candidate: it reduces to known
  biology/physics without new explanatory leverage. The sheaf-cohomological reading (Run 4)
  would escape K4 but requires the H^1 calculation first.
- Item D's declining curve as stated reduces to known monetary economics.

**K3 (No Formal Work) risk:**

- All five items carry K3 risk in their current form because none of the functionals
  (N, C, K, mu_M) are formally specified at the category level. Importing them as TI
  claims before Ext_S's category structure is specified would be K3 violations.

### Recommended Claim Candidates

Listed by readiness and PPP-3 relevance:

**Claim candidate 1 (highest readiness, directly advances PP-3):**

```text
AC-8 Redistribution Witness Theorem:
In a multi-observer OnlineSchemaSys satisfying NAA, if each observer retains schema-boundary
proposal rights (formally: the right to submit D4-candidate morphisms that are incompatible
with any intra-schema extension of delta_n), then the shared schema trajectory cannot be
reproduced as aperture disclosure from any fixed richer source Mu_infty.

This satisfies the interaction_witness type from E029 and is the first concrete PP-3
positive witness candidate that the repo has in hand.

Blocking task: formalize schema-boundary proposal rights as a morphism class in Ext_S,
prove the incompatibility-self-reference blocks the fixed-Mu_infty construction.
```

**Claim candidate 2 (medium readiness, mu resolution path):**

```text
Sheaf-Cohomological mu Derivation:
If Ext_S admits a sheaf structure with non-trivial H^1 over observer patches, the canonical
measure mu on realized constraint complexes is necessarily sub-extensive (non-additive in the
WBE sense) because of the H^1 gluing obstruction.

This would make mu a derived quantity of Ext_S structure rather than an imported constant.
It provides the TI-native derivation of sublinear scaling without importing biology.

Blocking task: specify the sheaf structure on Ext_S; compute H^1 for the minimal case
(two observer patches, incompatible admissibility predicates, as in E029 C1).
```

**Claim candidate 3 (conditional, rate dynamics):**

```text
Lambda*(s) as a Functor-Optimization:
If Ext_S has the category structure from RUN-0025 (objects = typed schema states, morphisms
= admissible extensions), then the issuance rate optimization is a functor-optimization
problem: find the parameterization lambda that maximizes the net-benefit natural
transformation (N - C - K) pointwise over Ext_S objects.

The globally-defined lambda*(s) exists as a section iff the net-benefit natural
transformation admits a global section over the sheaf of observer configurations.
When AC-8 incompatible proposals are present, this section fails to exist globally.

Blocking task: complete the Ext_S category specification; define N, C, K as natural
transformations; prove the global-section obstruction.
```

**Claim candidate 4 (descriptive, not formal):**

```text
Gödelian Declining Rate Observation:
In a self-referential OnlineSchemaSys where R_n operates over S_n and H_n (Gödelian
mechanism from E028), the rate of D4 events per prefix step is expected to decline as
S_n grows, because:
(a) The density of Gödel-sentences relative to the current schema decreases as the schema
    becomes more expressive.
(b) The minimum proof length required to identify a D4 candidate increases.

This produces a naturally declining D4 rate at maturity without importing tokenomic
mechanism design or biological metabolic scaling.

Status: informal observation awaiting the Gödelian mechanism formalization from E028.
```

### Outstanding Blocking Tasks (Priority Order)

1. **Ext_S category specification (unblocks A, B, E, Claim 3):** The outstanding formal
   work since RUN-0025. No items from this intake can be formally incorporated until objects,
   morphisms, composition, and key functors are specified.

2. **AC-8 schema-boundary proposal rights formalization (unblocks Item C / Claim 1):**
   Specify the morphism class of schema-boundary proposals in Ext_S; prove the
   fixed-Mu_infty obstruction. This is the most direct path to a PP-3 positive witness.

3. **H^1 calculation on the minimal Ext_S sheaf (unblocks Item B / Claim 2):** Two-patch
   case from E029 C1. This would either give mu a TI-native derivation or confirm that
   H^1 is trivial in the minimal case (narrowing mu's prospects).

4. **Q grounding via quorum-validity (unblocks RUN-0028 residue):** If quorum-validity
   is the Q measure on morphisms, formalize Q: Mor(Ext_S) -> ([0,inf), +) as the
   legitimacy weight function and test whether Q so defined satisfies the RUN-0028
   kinematic conditions.

---

## Governance Constraints for E030 Findings

1. Do NOT import lambda*(s) into the formal object until N, C, K are defined at the
   category level and Ext_S has a complete category specification.

2. Do NOT import mu_M = c * |r|^{3/4} from WBE. If mu's sub-extensivity is to be claimed,
   it must be derived from H^1 of Ext_S, not from biological metabolic scaling.

3. Do NOT import the declining issuance curve from tokenomics. The Gödelian structural
   version (Claim 4) may be documented as an informal observation.

4. Item C (Ostrom redistribution) is the only item from this intake that directly advances
   PP-3 and should be prioritized for the next formal pass. It should be formalized as
   the AC-8 schema-boundary proposal rights condition, not imported in natural-language
   commons framing.

5. All four claim candidates above are speculative. None are TI claims until the blocking
   tasks are completed.

6. The Q-grounding via quorum-validity is the most promising residue from RUN-0028. It
   should be investigated in parallel with the AC-8 formalization (same formal object).
