---
artifact_type: exploration
status: active_result
governance_role: holonomy_transport_fixture
claim_movement: false
created: 2026-07-10
claim_refs:
  - TI-C012
  - TI-C018
  - TI-C019
---

# E160: Holonomy Transport-Functor Derivation Fixture

## Question

E159 names the holonomy route as a clean Form-A risk: a loop word in `ExtCat` is
not yet a `G`-valued holonomy. The missing object is a transport functor:

```text
A: ExtCat -> B G
```

This fixture asks a bounded toy version of the constructive question:

```text
Does C-typed admissibility derive A: ExtCat -> B Z/2,
or is transport extra data?
```

## Fixture

Executable artifact:

```text
tools/holonomy_transport_functor_derivation_fixture.py
```

Focused test:

```text
tests/test_holonomy_transport_functor_derivation_fixture.py
```

Result JSON:

```text
tests/artifacts/holonomy_transport_functor_derivation_fixture_result.json
```

The fixture compares five toy cases:

1. `bare_loop_word`: an admissible loop with no group labels.
2. `identity_forced_consistency`: consistency derives only identity transport.
3. `c_typed_parity_rule`: C-typed admissibility carries an additive `Z/2`
   edge label and derives a nontrivial loop value.
4. `imported_transport_table`: the same style of nontrivial value appears only
   because a transport table is supplied from outside C.
5. `inconsistent_c_typed_labels`: labels exist but fail functorial composition.

## Result

```yaml
bare_loop_derives_transport: false
identity_only_reopens_holonomy_route: false
source_rule_positive_shape_found: true
imported_table_counts_as_derivation: false
claim_status_change: none
active_trigger_change: none
```

Interpretation:

- Bare loop data still does not derive holonomy.
- A consistency rule that forces all loop values to identity is a derived
  transport functor, but it is not a nontrivial holonomy witness.
- A nontrivial toy result is possible only when C-typed admissibility itself
  carries a composition-compatible label rule.
- A supplied transport table is not a derivation from C; it remains extra data.
- Inconsistent labels do not define a functor.

## Boundary

This does not prove that Temporal Issuance derives a real transport functor.
It sharpens the next positive shape: the holonomy route needs an admissibility
rule that is both source-side and functorial under extension composition.

No claim status, formal object, North Star, public posture, or active trigger
state changes in this result.
