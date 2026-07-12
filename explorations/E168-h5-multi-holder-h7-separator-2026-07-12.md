---
artifact_type: exploration
status: active
governance_role: research_result
---

# E168 H5 Multi-Holder H7 Separator

## Purpose

Execute H5 after H7 by testing whether multi-holder reversal cost is TI-side
source crossing or only TaF finality/readout over fixed-source holder maps.

## Artifact

```text
tools/h5_multi_holder_h7_separator.py
tests/test_h5_multi_holder_h7_separator.py
tests/artifacts/h5_multi_holder_h7_separator_result.json
```

## Result

```yaml
h5_result: multi_holder_cost_separated_from_source_crossing
h7_floor_satisfied: true
h7_admitted_packet_ids:
  - boundary_osag_support
matched_physical_and_thermodynamic_controls: true
multi_holder_cost_absorbed_as_taf_readout: true
formal_local_osag_support_admitted: true
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
```

With physical copy count and overwrite count matched, the split-holder case
raises reversal/fork cost only through holder-boundary finality and access
permissions already present in the fixed source. H5 therefore classifies pure
multi-holder cost as `TAF_EXPRESSIBLE_READOUT`, not source crossing.

The only admitted packet is the H7 `boundary_osag_support` case. It remains
formal/local OSAG support and does not establish a physical source claim, reopen
`TI-C020`, or move claim status.

## Next

H9 physical calibration or H6 completion-boundary work should proceed only with
concrete packets that satisfy H7. H5 alone supplies no source-crossing claim.
