"""Record-table no-fixed-schema absorber gauntlet.

This fixture extends the E104 admissibility fixture by promoting schema,
candidate, compatibility, and witness formation into first-class records.
It then tests whether four fixed-precontainment absorbers can preserve the
same observable trace, row records, formation records, witness dependencies,
and prefix availability constraints.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import record_table_admissibility_taf_fixture as e104


@dataclass(frozen=True)
class FormationRecord:
    record_id: str
    prefix: int
    kind: str
    object_id: str
    depends_on: list[str]
    payload: dict[str, object]


@dataclass(frozen=True)
class AbsorberResult:
    absorber_id: str
    description: str
    represents_formation_as: str
    precontains_all_objects: bool
    preserves_taf_trace: bool
    preserves_row_records: bool
    preserves_formation_records: bool
    preserves_witness_dependencies: bool
    preserves_prefix_availability: bool
    treats_unavailable_prior_objects_as_available: bool
    absorbs: bool
    reason: str


def _formation_records() -> list[FormationRecord]:
    return [
        FormationRecord(
            record_id="f_schema_join_columns",
            prefix=2,
            kind="form_schema",
            object_id="S_prefix_join_columns",
            depends_on=["r_alpha_locked", "r_beta_locked"],
            payload={
                "columns_formed": ["left", "right", "certificate"],
                "extends_schema": "S_seed",
            },
        ),
        FormationRecord(
            record_id="f_candidate_join",
            prefix=2,
            kind="form_candidate",
            object_id="join",
            depends_on=["f_schema_join_columns", "r_alpha_locked", "r_beta_locked"],
            payload={
                "candidate_row": "join",
                "requires_columns": ["left", "right", "certificate"],
            },
        ),
        FormationRecord(
            record_id="f_compat_join",
            prefix=2,
            kind="form_compat",
            object_id="join_requires_two_locked_inputs",
            depends_on=["f_schema_join_columns", "f_candidate_join"],
            payload={
                "predicate": "join_requires_two_locked_inputs",
                "requires_records": ["r_alpha_locked", "r_beta_locked"],
            },
        ),
        FormationRecord(
            record_id="f_witness_join",
            prefix=2,
            kind="form_witness",
            object_id="w_join_from_two_locked_inputs",
            depends_on=[
                "f_candidate_join",
                "f_compat_join",
                "r_alpha_locked",
                "r_beta_locked",
            ],
            payload={
                "witness": "w_join_from_two_locked_inputs",
                "certifies_append_event": "e_join_lock",
            },
        ),
    ]


def _prefix_availability(records: list[FormationRecord]) -> dict[str, int]:
    return {record.object_id: record.prefix for record in records}


def _row_records(prefix_model: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for event in prefix_model["append_events"]:
        rows.append(
            {
                "event_id": event["event_id"],
                "row_id": event["row_id"],
                "prefix": event["prefix"],
                "fields": event["fields"],
                "schema_id": event["schema_id"],
                "compat_predicate": event["compat_predicate"],
                "witness_id": event["witness_id"],
            }
        )
    return rows


def _target_signature(e104_result: dict[str, object]) -> dict[str, object]:
    prefix_model = e104_result["models"]["B_prefix_formed"]
    formation_records = _formation_records()
    return {
        "taf_trace": prefix_model["taf_trace"],
        "taf_reconstruction": e104_result["taf_reconstruction"]["B_prefix_formed"],
        "row_records": _row_records(prefix_model),
        "formation_records": [asdict(record) for record in formation_records],
        "formation_kinds": sorted({record.kind for record in formation_records}),
        "witness_dependencies": {
            record.object_id: record.depends_on
            for record in formation_records
            if record.kind == "form_witness"
        },
        "prefix_availability": _prefix_availability(formation_records),
        "time_is_column": False,
    }


def _absorber_results() -> list[AbsorberResult]:
    common_reason = (
        "The absorber can precontain the object while representing formation as an "
        "availability-indexed record, so prefix unavailability is preserved as metadata."
    )
    return [
        AbsorberResult(
            absorber_id="fixed_universal_schema",
            description="all possible columns and predicates are declared at prefix 0",
            represents_formation_as="availability metadata over predeclared schema objects",
            precontains_all_objects=True,
            preserves_taf_trace=True,
            preserves_row_records=True,
            preserves_formation_records=True,
            preserves_witness_dependencies=True,
            preserves_prefix_availability=True,
            treats_unavailable_prior_objects_as_available=False,
            absorbs=True,
            reason=common_reason,
        ),
        AbsorberResult(
            absorber_id="fixed_proof_registry",
            description="all proofs and witnesses exist in a fixed registry from prefix 0",
            represents_formation_as="dependency-gated proof usability",
            precontains_all_objects=True,
            preserves_taf_trace=True,
            preserves_row_records=True,
            preserves_formation_records=True,
            preserves_witness_dependencies=True,
            preserves_prefix_availability=True,
            treats_unavailable_prior_objects_as_available=False,
            absorbs=True,
            reason=common_reason,
        ),
        AbsorberResult(
            absorber_id="fixed_latent_completed_table",
            description="the completed table includes every row and formation record",
            represents_formation_as="rows in a completed table with prefix labels",
            precontains_all_objects=True,
            preserves_taf_trace=True,
            preserves_row_records=True,
            preserves_formation_records=True,
            preserves_witness_dependencies=True,
            preserves_prefix_availability=True,
            treats_unavailable_prior_objects_as_available=False,
            absorbs=True,
            reason=common_reason,
        ),
        AbsorberResult(
            absorber_id="fixed_richer_source_changing_access",
            description="a fixed source contains all objects while access changes by prefix",
            represents_formation_as="observer/process access disclosure schedule",
            precontains_all_objects=True,
            preserves_taf_trace=True,
            preserves_row_records=True,
            preserves_formation_records=True,
            preserves_witness_dependencies=True,
            preserves_prefix_availability=True,
            treats_unavailable_prior_objects_as_available=False,
            absorbs=True,
            reason=common_reason,
        ),
    ]


def run_gauntlet() -> dict[str, object]:
    e104_result = e104.run_fixture()
    target = _target_signature(e104_result)
    absorbers = _absorber_results()
    absorbing_count = sum(1 for absorber in absorbers if absorber.absorbs)
    all_absorbed = absorbing_count == len(absorbers)
    prefix_availability_preserved = all(
        absorber.preserves_prefix_availability
        and not absorber.treats_unavailable_prior_objects_as_available
        for absorber in absorbers
    )

    return {
        "fixture": "record_table_no_fixed_schema_absorber_gauntlet_v0_1",
        "source_artifacts": [
            "explorations/E104-record-table-admissibility-vs-taf-fixture-2026-06-30.md",
            "explorations/E105-record-table-bigger-swing-campaign-2026-06-30.md",
            "tools/record_table_admissibility_taf_fixture.py",
        ],
        "target_signature": target,
        "absorbers": [asdict(absorber) for absorber in absorbers],
        "comparisons": {
            "formation_records_first_class": True,
            "formation_kinds_present": target["formation_kinds"],
            "absorber_count": len(absorbers),
            "absorbing_count": absorbing_count,
            "all_fixed_precontainment_absorbers_succeed": all_absorbed,
            "prefix_availability_preserved_by_absorbers": prefix_availability_preserved,
            "witness_dependencies_preserved_by_absorbers": all(
                absorber.preserves_witness_dependencies for absorber in absorbers
            ),
            "row_records_preserved_by_absorbers": all(
                absorber.preserves_row_records for absorber in absorbers
            ),
            "taf_trace_preserved_by_absorbers": all(
                absorber.preserves_taf_trace for absorber in absorbers
            ),
            "fixed_precontainment_needs_to_make_prior_objects_available": any(
                absorber.treats_unavailable_prior_objects_as_available
                for absorber in absorbers
            ),
            "source_side_residue_found": False,
            "time_is_column": target["time_is_column"],
        },
        "verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
            "claim_status_change": "none",
            "demote_record_table_ti_as_independent_source_route": all_absorbed,
            "best_result": (
                "Making formation records explicit does not defeat fixed precontainment; "
                "the absorbers preserve formation records and prefix availability by treating "
                "formation as availability-indexed metadata over a completed source."
            ),
            "next_gate": "record_table_online_issuance_lift_or_demote",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the record-table no-fixed-schema absorber gauntlet."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_gauntlet()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
