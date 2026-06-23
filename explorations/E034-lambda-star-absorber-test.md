---
artifact_type: exploration
status: active
exploration_id: E034
run_ref: RUN-0047
claim_refs:
  - TI-C003
  - TI-C007
  - TI-C019
topic: lambda_star_absorber_test
phase: 2B
date: 2026-06-22
---

# E034: Absorber Test for lambda*(s) = argmax_lambda [N(lambda,s) - C(lambda,s) - K(lambda,s)]

## Purpose

A cross-repo research session proposed the following dynamics equation for the formal
object `Ext_S`:

```text
lambda*(s) = argmax_lambda [ N(lambda, s) - C(lambda, s) - K(lambda, s) ]
```

where:
- `lambda` is an admissible extension action or extension rule
- `s` is the current source state
- `N(lambda, s)` is a novelty term (benefit of extending by lambda from s)
- `C(lambda, s)` is a constraint cost (cost of satisfying typed source constraints)
- `K(lambda, s)` is a kill term (proximity to kill conditions, incompatibility penalties)

The proposal is: `lambda*(s)` selects the optimal admissible extension from source state `s`
under this trade-off structure. This is offered as a candidate dynamics equation for `Ext_S`.

This exploration runs the absorption discipline from METHOD.md:
- absorber framework
- mapping
- what is explained
- what is not explained
- category-error risk
- local-minimum risk
- resurrection trigger

## Absorber Test

### Absorber 1: Variational Principles / Optimization Over Extension Rules

**Framework:** Any system that selects extensions by maximizing a net-value objective
`V(lambda, s) = N - C - K` is an instance of a constrained optimization problem over an
action space. The standard framework is variational optimization, Lagrangian mechanics (when
continuous), or dynamic programming (when sequential and state-indexed).

**Mapping:**
- `s` -> current state
- `lambda` -> action / control variable
- `N(lambda, s)` -> reward or benefit function
- `C(lambda, s)` -> resource cost / constraint penalty
- `K(lambda, s)` -> Lyapunov-style stability penalty or kill-avoidance term
- `lambda*(s)` -> optimal policy (policy-gradient or Bellman-optimal)

This is exactly the structure of a Markov Decision Process (MDP) with reward `N - C - K` and
a deterministic policy. Bellman's equation `V*(s) = max_lambda [R(s, lambda) + gamma V*(s')]`
absorbs this when `K` is included as a negative reward and `N - C` is the net reward.

**What is explained:** The argmax selection structure, the state-conditioned optimal action,
the trade-off between novelty and cost and kill-avoidance. All of this is standard optimal
control and reinforcement learning formalism.

**What is not explained:** Nothing survives as definitively new — the argmax structure is a
well-known variational skeleton. The only TI-specific content would have to come from:
(a) what `N`, `C`, `K` are defined to mean inside TI's formal object, and
(b) whether those definitions cannot be supplied by any external reward/cost formalism.

**Category-error risk:** The MDP absorber assumes a transition function `T(s, lambda, s')`
that produces the next state. If TI's `Ext_S` is modeled as a category with morphisms
`e: S -> S'`, then the next-state structure IS the morphism composition, but the argmax
selection is over morphisms indexed by the extension rule `lambda`. This is the argmax over
`Hom(S, -)` weighted by `N - C - K`. No category-error is evident here — the category
supports the selection.

**Verdict:** Absorbed by MDP / optimal control / variational optimization.

---

### Absorber 2: Economic Production Optimization

**Framework:** `N(lambda, s) - C(lambda, s) - K(lambda, s)` has the structure of a
profit-maximization problem: revenue minus cost minus kill-risk penalty. In economics, the
optimal production quantity or investment strategy is selected by exactly this structure.
The Ostrom framework (see Idea C below) identifies legitimacy as a constraint, but the
selection mechanism itself is standard economics.

**Mapping:**
- `lambda` -> production strategy / allocation choice
- `N` -> output value or marginal benefit
- `C` -> resource cost
- `K` -> risk or kill penalty (analogous to downside risk or regulatory cost)
- `lambda*(s)` -> profit-maximizing strategy

**What is explained:** The selection structure fully absorbs into economic optimization.

**What is not explained:** The formal object `Ext_S` is not an economic agent. The question
is whether TI can use this structure without importing an economic agent who has preferences
and computes the argmax. If the argmax is agent-computed, it is absorbed by economics. If
it is a selection principle without an agent (e.g., a physical extremum principle), a surplus
may remain.

**Category-error risk:** Importing an agent who computes the argmax would violate TI's
governance constraint against rational agents in physical formalism. Any agent-free reading
of the argmax (extremum principle, variational principle) reduces to Absorber 1.

**Verdict:** Absorbed by economic optimization or variational principle. No agent-free
reading of the argmax introduces new formal content beyond Absorber 1.

---

### Absorber 3: Free Energy Minimization (Friston / Active Inference)

**Framework:** The Active Inference framework selects actions to minimize expected free
energy `F`, which has the form `F = -N + C + K` where:
- `N` = expected information gain / novelty value (epistemic value)
- `C` = expected constraint violation cost (cost of departure from prior)
- `K` = expected cost of entering terminal or kill states

`lambda*(s) = argmin_lambda F(lambda, s)` is equivalent to `argmax_lambda [N - C - K]`.

**Mapping:** Exact structural equivalence.

**What is explained:** The argmax/argmin structure, the novelty-cost-kill trade-off, the
state-conditioned selection, and the epistemic role of the novelty term `N`. Active inference
is a substantial framework that would absorb this proposal in full generality.

**What is not explained:** Whether TI's `N, C, K` are `Friston`-style quantities or
something else. Active inference grounds `F` in variational Bayesian inference; TI would
need a Bayesian posterior structure to use the absorption cleanly. If TI's `N, C, K` are
not grounded in Bayesian inference, a category mismatch may remain at the grounding level —
though not at the selection-structure level.

**Verdict:** Absorbed at the structural level. Category mismatch possible if TI's terms
are not Bayesian.

---

### Absorber 4: Source-Side Dynamics vs. Observer-Side Policy

**Framework:** The critical question for TI is whether `lambda*(s)` describes a source-side
dynamics rule (how `Ext_S` selects admissible extensions from source state `s`) or an
observer-side policy (how an observer selects the best available extension to act on). These
are different:

```text
Source-side dynamics: the shared process itself selects extensions by maximizing N - C - K.
Observer-side policy: an observer agent selects which extension to request or instantiate.
```

In the source-side reading, `lambda*` is a physical selection principle — analogous to the
principle of least action. In the observer-side reading, `lambda*` is a decision theory for
agents.

**PP-3 pressure (from E029):** The PP-3 crux is whether TI's formal claims describe source-
side structure or projection-layer structure. `lambda*(s)` as a dynamics equation for `Ext_S`
is a source-side claim. But:

```text
If lambda*(s) is a source-side extremum principle, it faces the same absorption by variational
mechanics that `Ext_S` faces from constructor theory, thermodynamics, and information theory.
If lambda*(s) is observer-side, it imports an agent who computes the argmax, which violates
TI's governance constraint.
```

Neither reading escapes existing absorbers.

**Verdict:** The source/observer ambiguity does not create a survivor — it reveals two
absorber routes.

---

### Absorber 5: Ostrom SES / Legitimacy Constraint (Idea C)

The cross-repo session also proposed: legitimacy requires balancing mechanism against
increasing-returns capture. Under the Ostrom Socio-Ecological System (SES) framework, this
corresponds to an institutional design principle where governance legitimacy is maintained by
preventing monopoly extraction in the presence of increasing-returns dynamics.

**How this relates to lambda*:** If `K(lambda, s)` includes an increasing-returns capture
penalty — i.e., `K` is high when `lambda` creates a mechanism that locks out alternative
extensions — then `lambda*(s)` encodes the Ostrom legitimacy condition as a kill-avoidance
term.

**Mapping:**
- `K` = institutional illegitimacy cost = increasing-returns capture penalty
- `lambda*(s)` = Ostrom-legitimate extension rule = one that balances local optimization
  against systemic capture

**What is explained:** The functional form `N - C - K` can encode the Ostrom legitimacy
condition if `K` is defined appropriately.

**What is not explained:** Whether TI has an independent reason to define `K` in this way
rather than importing the Ostrom institutional design framework directly. The Ostrom SES
framework provides the design principle; TI would be using it, not deriving it.

**Verdict:** The legitimacy condition is encodable in `K` but requires the Ostrom framework
to supply the content of `K`. This is an import, not a derivation.

---

## Overall Verdict

```yaml
absorber_test_result: absorbed
primary_absorbers:
  - MDP / optimal control / variational optimization (structural level)
  - Active inference / free energy minimization (structural level)
  - Economic profit maximization (structural level)
residual_after_absorption: none_at_selection_structure_level
residual_condition: >
  A surplus would appear only if N, C, K are independently derived from TI's
  typed source constraints without importing optimization, economic, Bayesian, or
  agent machinery. No such derivation is currently available.
category_error_risk: >
  Agent-free reading of argmax reduces to variational principle (Absorber 1).
  Agent-based reading violates TI governance constraint against rational agents.
local_minimum_risk: >
  The proposal may look novel because it names N, C, K in TI-adjacent vocabulary
  (novelty, constraint cost, kill penalty) while the structure is standard optimization.
  Do not mistake vocabulary alignment for formal novelty.
resurrection_trigger: >
  If TI independently derives N, C, K from typed source admissibility predicates
  WITHOUT importing optimization, economics, or Bayesian machinery, and if the resulting
  argmax generates a discriminator against all named absorbers, then lambda*(s) is a
  genuine TI formal object and should be registered as a new claim candidate.
  The test is: do N, C, K carry C-typed admissibility content that no optimization
  framework supplies? Currently: no.
ti_claim_effects:
  TI-C003: no_change (Ext_S already formalizing; lambda* does not advance or kill it)
  TI-C007: no_change (lambda* is absorbed, does not help or hurt Ext_S load-bearing status)
  TI-C019: no_change (lambda* is absorbed, does not add source-side witness)
```

## What lambda*(s) Does Contribute (Negative Result With Positive Use)

Although `lambda*(s)` is absorbed as a formal object, the vocabulary it introduces is useful
as a **design scaffold** for the AC-8 formal model:

1. `N(lambda, s)` points toward a novelty-value function for typed schema extensions — this
   is a formalization target for D4 event value that has not been specified.

2. `C(lambda, s)` points toward a typed admissibility cost — the resources or constraints
   consumed by an extension `lambda` from source state `s`.

3. `K(lambda, s)` points toward kill-proximity — encoding the repo's kill criteria as a
   formal penalty function may be useful for testing whether a candidate extension would
   trigger a kill condition.

These are vocabulary-level contributions, not formal novelties. They may be useful as
intuition pumps for the AC-8 fixture or the source-side witness fixture, but they do not
survive absorber testing as independent formal claims.

## Connection to E029 Source-Side Witness Requirement

From E029, the source-side witness requirement is:

```yaml
generator_issuance: exhibit a new generator kind or admissibility rule not contained
  in any prior source hyperprior, grammar, or completed source schema
```

`lambda*(s)` does not provide this. It is a selection principle over existing extension rules,
not a generator of new extension rules not contained in any prior schema. Therefore it does
not satisfy the source-side witness requirement. It is projection-level optimization, not
source-side issuance.
