---
artifact_type: exploration
status: complete
governance_role: capability_transport_source_action_fixture
workflow: W000
goal_ref: capability_transport_source_action_fixture
claim_refs:
  - TI-C012
  - TI-C018
  - TI-C019
depends_on:
  - explorations/E119-tri-repo-capability-burden-retyping-2026-07-02.md
  - explorations/E152-adapter-p-no-go-preflight-2026-07-09.md
  - explorations/E160-holonomy-transport-functor-derivation-fixture-2026-07-10.md
created: 2026-07-10
central_run: RUN-0140
constitutional: false
claim_status_change: none
---

# E161: Capability-Transport Source-Action Fixture

## Purpose

E160 sharpened the holonomy Form-A issue: a bare loop is not holonomy, but a
toy C-typed admissibility rule can derive a nontrivial `Z/2` transport value.

E119 says the live `Ext_S` burden is stronger than "find an invariant":

```text
Find an Ext_S rule that changes a region-indexed observer task menu in a way
TaF's capability-typed readout cannot express.
```

This fixture joins those two threads. The question is:

```text
Does E160-style C-derived transport become an E119-style capability-changing
source action?
```

## Executable Fixture

Executable artifact:

```text
tools/capability_transport_source_action_fixture.py
```

Focused test:

```text
tests/test_capability_transport_source_action_fixture.py
```

Result JSON:

```text
tests/artifacts/capability_transport_source_action_fixture_result.json
```

The fixture compares eight cases:

1. bare loop, no transport;
2. identity-only derived transport;
3. E160-style C-derived parity sector readout;
4. fixed-access sector disclosure;
5. imported transport table;
6. C-derived finite-prefix transport absorbed by singleton after-naming;
7. schematic anti-after-naming source-action shape;
8. inconsistent C labels.

## Result

```yaml
fixture_complete: true
e160_transport_has_capability_delta: true
e160_transport_becomes_source_action: false
e160_transport_verdict: TAF_EXPRESSIBLE_READOUT
positive_source_action_shape_stateable: true
real_source_action_found: false
claim_status_change: none
active_trigger_change: none
```

The E160 C-derived parity transport does create a task-menu handle:

```text
distinguish_loop_sector
```

But this concrete handle is still expressible as a capability/readout fact. It
does not yet show a TI source-crossing action.

## Verdict

The current holonomy/capability connection is valuable, but it does not promote
the holonomy route.

What the fixture establishes:

- bare loops still do not matter operationally;
- identity-only transport is trivial;
- imported transport remains rejected;
- fixed-access sector revelation is disclosure;
- finite-prefix C-derived transport can remain only class-relative formal residue
  if singleton after-naming absorbs the realized family;
- the positive source-action shape is stateable.

The positive shape requires all of the following:

```text
nontrivial C-derived transport
+ supported region-indexed task-menu change
+ source-growth witness
+ no TaF readout expression of the task delta
+ no fixed-completion/access factorization
+ internal anti-after-naming principle
```

That shape is an admission test for future work, not a current witness.

## Claim Effect

No claim status moves.

```yaml
TI-C012:
  status: formalizing   # unchanged
  effect: >
    E160's source-derived toy transport has now been pushed through a capability
    action gate. The first concrete task delta is TaF-expressible readout, so
    holonomy remains formal residue unless a stronger task delta survives.

TI-C018:
  status: weakened      # unchanged
  effect: >
    Bare Ext_S remains insufficient; C-derived transport is a necessary but
    insufficient condition. A future transport witness must also change a
    capability menu beyond readout/disclosure.

TI-C019:
  status: formalizing   # unchanged
  effect: >
    The source-formal/capability bridge is sharpened, not advanced. The
    remaining useful target is a concrete anti-after-naming source-action trace.
```

## Next State

Do not promote holonomy or TI-C019 from this result.

Future material work should proceed only if a concrete trace fills the positive
anti-after-naming source-action shape, or if this schematic shape is turned into
a full `Adapter_P` fixture. Otherwise the active next state remains compact
no-worthy-work until a gate-changing trace or sharper theorem target appears.
