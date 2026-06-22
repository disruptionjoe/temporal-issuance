---
artifact_type: exploration
status: active
governance_role: ontology_competition_fixtures
exploration_id: E005
last_updated_by: RUN-0022
claim_refs:
  - TI-C001
  - TI-C002
  - TI-C003
constitutional: false
---

# E005: Ontology Competition Fixture Suite

## Purpose

Give the next ontology competition run shared fixtures.

Every survivor should face the same tests. This prevents the repo from comparing a steelmanned favorite against straw alternatives.

## Competitors

At minimum:

- source realization order
- constraint extension primitive
- typed constraint inventory
- projection kernel
- witness and certification
- constructor or resource transformability
- obstruction class
- proof or computation order
- emergence or lock-in
- `NULL-SURVIVOR`

## Required Output Per Competitor

```yaml
competitor:
components_used:
C_status:
<=_S_status:
Ext_S_status:
what_it_explains:
assumptions_required:
strongest_absorber_threat:
sharpest_discriminator:
fixture_results:
what_would_kill_it:
what_would_resurrect_it:
does_it_beat_NULL_SURVIVOR:
```

## Fixtures

### F1: Same Records, Different Source

Question:

Can the competitor explain RUN-0019's hidden-source case without becoming unfalsifiable?

Required answer:

```yaml
does_hidden_difference_matter:
why:
required_witness_or_invariant:
absorber_risk:
```

Kill pressure:

If a hidden source difference has no witness, invariant, or transformation consequence, `NULL-SURVIVOR` should beat it.

### F2: Same Order, Different Extension

Question:

Can two candidates share `<=_S` while differing in `Ext_S`?

Required answer:

```yaml
same_order_possible:
different_extension_possible:
what_extension_changes:
does_order_explain_the_difference:
```

Kill pressure:

If `Ext_S` does all the work, demote `<=_S`.

### F3: Same Extension, Different Constraint Typing

Question:

Can the same extension rule operate over different typed `C`?

Required answer:

```yaml
C_type:
typing_changes_result:
typing_absorber:
```

Kill pressure:

If `C` is only records, propositions, event labels, or causal-set elements, absorb it.

### F4: Witnessability

Question:

What could certify a source-side distinction under bounded access?

Required answer:

```yaml
witness_type:
who_can_verify:
what_remains_hidden:
failure_mode:
```

Kill pressure:

Hidden structure without witnessability, invariance, or operational consequence is archive material.

### F5: Transformation Impossibility

Question:

What transformation becomes impossible after source extension?

Required answer:

```yaml
transformation:
possible_before:
possible_after:
reason_not_entropy_or_information:
```

Kill pressure:

If impossibility reduces to entropy, information, action, probability, volume, cost, or ordinary causal update, absorb.

### F6: Gauge Or Representation Equivalence

Question:

Are two source distinctions actually the same under an equivalence relation?

Required answer:

```yaml
equivalence_relation:
distinction_survives_quotient:
invariant:
```

Kill pressure:

If the source difference vanishes under the relevant quotient, do not count it as Temporal Issuance residue.

### F7: Access Loss Without Source Loss

Question:

Can observer access degrade while source realization remains fixed?

Required answer:

```yaml
source_persists:
access_changes:
record_changes:
does_competitor_distinguish_source_from_readout:
```

Kill pressure:

If the competitor cannot distinguish source persistence from readout availability, time-as-finality or access theory absorbs it.

### F8: Local Non-Resolution

Question:

Can local histories remain lawfully non-glued without implying source failure?

Required answer:

```yaml
local_histories:
global_resolution_required:
obstruction_or_nonresolution:
source_effect:
```

Kill pressure:

If non-resolution is only readout-side, do not resurrect `G_ij` or `Omega_ij` as source-side.

### F9: Emergent Lock-In

Question:

Can local dynamics generate apparent source order without a primitive source order?

Required answer:

```yaml
local_rules:
lock_in_condition:
source_order_needed:
what_emergence_absorbs:
```

Kill pressure:

If emergence explains the fixture with fewer assumptions, source-order ontology weakens.

### F10: Null Absorption

Question:

Can existing frameworks explain the whole fixture set?

Required answer:

```yaml
absorbing_frameworks:
what_they_explain:
what_they_fail_to_explain:
remaining_residue:
is_residue_research_grade:
```

Kill pressure:

If the residue is not research-grade, `NULL-SURVIVOR` wins.

## Rule

No competitor gets to skip the null fixture.

No competitor gets to claim survival merely because another competitor failed.
