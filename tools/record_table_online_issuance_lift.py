"""Record-table to OnlineIssuance lift-or-demote fixture.

The fixture maps RecordTableSystem^TI components into OnlineIssuance^LC and
checks whether the record-table formulation adds any formal surplus over the
existing E091 residue.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import record_table_no_fixed_schema_gauntlet as e106


@dataclass(frozen=True)
class MappingEntry:
    record_table_component: str
    online_issuance_component: str
    mapping: str
    status: str
    formal_surplus_over_e091: bool


@dataclass(frozen=True)
class GateResult:
    gate_id: str
    requirement: str
    passed_by_record_table: bool
    basis: str
    required_for_e091_residue: bool


@dataclass(frozen=True)
class SurplusCheck:
    feature: str
    online_issuance_owner: str
    record_table_contribution: str
    adds_surplus: bool


def _component_mapping() -> list[MappingEntry]:
    return [
        MappingEntry(
            record_table_component="Schema_n",
            online_issuance_component="Gamma_n",
            mapping="available row fields, declarations, compatibility objects, and proof records become the prefix-presented context",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Cand_n",
            online_issuance_component="CandExt(Gamma_n)",
            mapping="candidate row/schema updates become candidate source extensions",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Compat_n",
            online_issuance_component="Adm_n",
            mapping="row compatibility becomes the admissibility predicate for candidate extensions",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Append_n",
            online_issuance_component="Iss_n / e_n",
            mapping="a witnessed append becomes a source-extension step when it passes the properness gate",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Witness_n",
            online_issuance_component="w_n : Adm_n(e_n)",
            mapping="formation and append witnesses become proof terms inhabiting admissibility",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Trace_n",
            online_issuance_component="tau_n",
            mapping="row and formation records become the recordable source trace",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
        MappingEntry(
            record_table_component="Project_i,n / TaF_i,n",
            online_issuance_component="Proj_{o,n} / Glue_n",
            mapping="observer rendering and finality reconstruction become projection and downstream gluing",
            status="maps_cleanly",
            formal_surplus_over_e091=False,
        ),
    ]


def _properness_gates(gauntlet_result: dict[str, object]) -> list[GateResult]:
    fixed_absorbers_succeed = gauntlet_result["comparisons"][
        "all_fixed_precontainment_absorbers_succeed"
    ]
    return [
        GateResult(
            gate_id="P1",
            requirement="formed present domain",
            passed_by_record_table=True,
            basis="the prefix model explicitly distinguishes formed and unformed schema/candidate/compatibility objects",
            required_for_e091_residue=True,
        ),
        GateResult(
            gate_id="P2",
            requirement="witnessed extension",
            passed_by_record_table=True,
            basis="f_witness_join records an admissibility witness for the join append",
            required_for_e091_residue=True,
        ),
        GateResult(
            gate_id="P3",
            requirement="prior-context unavailability",
            passed_by_record_table=True,
            basis="the join schema, candidate, compatibility predicate, and witness are unavailable before prefix 2",
            required_for_e091_residue=True,
        ),
        GateResult(
            gate_id="P4",
            requirement="no internally formed hidden completed oracle",
            passed_by_record_table=not fixed_absorbers_succeed,
            basis=(
                "E106 shows fixed universal schema, fixed proof registry, fixed latent table, "
                "and fixed richer source plus changing access all preserve the record-table trace"
            ),
            required_for_e091_residue=True,
        ),
        GateResult(
            gate_id="P5",
            requirement="recordability for projection/finality audit",
            passed_by_record_table=True,
            basis="row records, formation records, and the TaF trace are explicitly emitted",
            required_for_e091_residue=True,
        ),
    ]


def _surplus_checks() -> list[SurplusCheck]:
    return [
        SurplusCheck(
            feature="dimensions as columns",
            online_issuance_owner="Gamma_n declarations",
            record_table_contribution="helpful interface language for typed record fields",
            adds_surplus=False,
        ),
        SurplusCheck(
            feature="time is append/finality, not a column",
            online_issuance_owner="tau_n plus downstream Proj/Glue/TaF",
            record_table_contribution="useful anti-clock discipline, but no new source discriminator",
            adds_surplus=False,
        ),
        SurplusCheck(
            feature="formation records",
            online_issuance_owner="tau_n and w_n : Adm_n(e_n)",
            record_table_contribution="good concrete trace format for admissibility formation",
            adds_surplus=False,
        ),
        SurplusCheck(
            feature="observer rendering",
            online_issuance_owner="Proj_{o,n} and Glue_n",
            record_table_contribution="clear observer-interface vocabulary",
            adds_surplus=False,
        ),
        SurplusCheck(
            feature="fixed precontainment resistance",
            online_issuance_owner="P4 no-hidden-completed-oracle discipline",
            record_table_contribution="does not supply the discipline; E106 shows fixed absorbers succeed",
            adds_surplus=False,
        ),
        SurplusCheck(
            feature="productive/self-encoding witness",
            online_issuance_owner="E090 diagonal local-constructive witness",
            record_table_contribution="not present in the record-table join fixture",
            adds_surplus=False,
        ),
    ]


def run_lift() -> dict[str, object]:
    gauntlet_result = e106.run_gauntlet()
    mapping = _component_mapping()
    gates = _properness_gates(gauntlet_result)
    surplus_checks = _surplus_checks()

    component_mapping_total = all(entry.status == "maps_cleanly" for entry in mapping)
    required_gates_pass = all(
        gate.passed_by_record_table
        for gate in gates
        if gate.required_for_e091_residue
    )
    productive_or_self_encoding = any(
        check.adds_surplus
        for check in surplus_checks
        if check.feature == "productive/self-encoding witness"
    )
    adds_surplus = any(check.adds_surplus for check in surplus_checks)
    archive_as_vocabulary = component_mapping_total and not adds_surplus

    return {
        "fixture": "record_table_online_issuance_lift_or_demote_v0_1",
        "source_artifacts": [
            "explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md",
            "explorations/E106-record-table-no-fixed-schema-witness-or-demote-2026-06-30.md",
            "tools/record_table_no_fixed_schema_gauntlet.py",
        ],
        "component_mapping": [asdict(entry) for entry in mapping],
        "properness_gates": [asdict(gate) for gate in gates],
        "surplus_checks": [asdict(check) for check in surplus_checks],
        "comparisons": {
            "component_mapping_total": component_mapping_total,
            "record_table_is_online_issuance_interface": component_mapping_total,
            "properness_gates_pass_without_extra_axioms": required_gates_pass,
            "fails_no_hidden_oracle_gate": any(
                gate.gate_id == "P4" and not gate.passed_by_record_table
                for gate in gates
            ),
            "productive_self_encoding_witness_present": productive_or_self_encoding,
            "adds_formal_surplus_over_e091": adds_surplus,
            "inherits_e091_residue_without_extra_axioms": (
                required_gates_pass and productive_or_self_encoding
            ),
            "record_table_archive_as_vocabulary": archive_as_vocabulary,
            "physics_adapter_route_closed_for_record_table": archive_as_vocabulary,
            "source_side_residue_found": False,
        },
        "verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
            "claim_status_change": "none",
            "demote_record_table_ti": archive_as_vocabulary,
            "best_result": (
                "RecordTableSystem^TI maps cleanly into OnlineIssuance^LC as an interface, "
                "but it does not add no-hidden-oracle discipline, self-encoding admissibility, "
                "or a productive witness beyond E091."
            ),
            "next_gate": "machine_check_online_issuance_witness_or_frontier_rerank",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the record-table OnlineIssuance lift-or-demote fixture."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_lift()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
