---
artifact_type: test_index
status: active
governance_role: test_registry
constitutional: false
---

# Tests

Tests may be mathematical, conceptual, computational, adversarial, or governance-oriented.

Launch tests:

1. Full absorption test.
2. Circularity test.
3. Formal-work test.
4. Category-error test.
5. Local-minimum risk test.

Executable fixtures:

- H3 Cech/sheaf fixture: `python tests/test_cech_sheaf_fixture.py`
- Clock-free record-cadence fixture: `python tests/test_clock_free_record_cadence_fixture.py`
- Clock-free cadence absorber gauntlet: `python tests/test_clock_free_cadence_absorber_gauntlet.py`
- RSPS record-fidelity toy baseline: `python tools/rsps_record_fidelity_toy.py --output tests/artifacts/rsps_record_fidelity_toy_result.json`
- RSPS robustness sweep: `python tools/rsps_robustness_sweep.py --output tests/artifacts/rsps_robustness_sweep_result.json`
