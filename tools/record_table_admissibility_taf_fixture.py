"""Record-table admissibility vs TaF reconstruction fixture.

The fixture compares two record-table models with the same downstream
Time-as-Finality-style trace:

A. fixed schema / fixed completed table / fixed access
B. prefix-formed candidate and compatibility predicate

The question is whether the TI-owned append/admissibility provenance survives
after TaF absorbs temporal reconstruction from the emitted trace.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


FORBIDDEN_TIME_COLUMNS = {"time", "timestamp", "clock", "tick", "t"}


@dataclass(frozen=True)
class AppendEvent:
    event_id: str
    prefix: int
    row_id: str
    fields: dict[str, str]
    schema_id: str
    candidate_available_from: int
    compat_predicate: str
    witness_id: str


@dataclass(frozen=True)
class TafTraceEvent:
    event_id: str
    source_records: list[str]
    target_records: list[str]
    finality_profile: dict[str, int]


@dataclass(frozen=True)
class ModelResult:
    model_id: str
    description: str
    columns_by_prefix: dict[str, list[str]]
    candidates_by_prefix: dict[str, list[str]]
    compat_formed_at: dict[str, int]
    append_events: list[AppendEvent]
    taf_trace: list[TafTraceEvent]
    time_columns_present: list[str]
    join_candidate_available_before_inputs: bool
    join_compat_fixed_at_start: bool
    nonfixed_admissibility_provenance: bool


def _trace() -> list[TafTraceEvent]:
    """TaF-style trace intentionally modeled after the T48 shape."""
    return [
        TafTraceEvent(
            event_id="e_alpha_lock",
            source_records=["r_alpha_raw"],
            target_records=["r_alpha_locked"],
            finality_profile={"causal": 2, "info": 2},
        ),
        TafTraceEvent(
            event_id="e_beta_lock",
            source_records=["r_beta_raw"],
            target_records=["r_beta_locked"],
            finality_profile={"causal": 1, "info": 3},
        ),
        TafTraceEvent(
            event_id="e_join_lock",
            source_records=["r_alpha_locked", "r_beta_locked", "r_join_raw"],
            target_records=["r_alpha_locked", "r_beta_locked", "r_join_locked"],
            finality_profile={"causal": 3, "info": 4},
        ),
    ]


def _append_events(candidate_from_join: int, join_schema: str, join_predicate: str) -> list[AppendEvent]:
    return [
        AppendEvent(
            event_id="e_alpha_lock",
            prefix=0,
            row_id="alpha",
            fields={"entity": "alpha", "state": "locked", "value": "A"},
            schema_id="S_seed",
            candidate_available_from=0,
            compat_predicate="seed_row",
            witness_id="w_alpha_seed",
        ),
        AppendEvent(
            event_id="e_beta_lock",
            prefix=1,
            row_id="beta",
            fields={"entity": "beta", "state": "locked", "value": "B"},
            schema_id="S_seed",
            candidate_available_from=0,
            compat_predicate="seed_row",
            witness_id="w_beta_seed",
        ),
        AppendEvent(
            event_id="e_join_lock",
            prefix=2,
            row_id="join",
            fields={
                "entity": "join",
                "state": "locked",
                "left": "alpha",
                "right": "beta",
                "certificate": "alpha_beta_locked",
            },
            schema_id=join_schema,
            candidate_available_from=candidate_from_join,
            compat_predicate=join_predicate,
            witness_id="w_join_from_two_locked_inputs",
        ),
    ]


def _time_columns(columns_by_prefix: dict[str, list[str]], append_events: list[AppendEvent]) -> list[str]:
    found: set[str] = set()
    for columns in columns_by_prefix.values():
        found.update(column for column in columns if column.lower() in FORBIDDEN_TIME_COLUMNS)
    for event in append_events:
        found.update(field for field in event.fields if field.lower() in FORBIDDEN_TIME_COLUMNS)
    return sorted(found)


def run_fixed_schema_model() -> ModelResult:
    columns = ["entity", "state", "value", "left", "right", "certificate"]
    columns_by_prefix = {"0": columns, "1": columns, "2": columns}
    candidates_by_prefix = {
        "0": ["alpha", "beta", "join"],
        "1": ["alpha", "beta", "join"],
        "2": ["alpha", "beta", "join"],
    }
    compat_formed_at = {
        "seed_row": 0,
        "join_requires_two_locked_inputs": 0,
    }
    append_events = _append_events(
        candidate_from_join=0,
        join_schema="S_fixed_all_columns",
        join_predicate="join_requires_two_locked_inputs",
    )
    return ModelResult(
        model_id="A_fixed_schema",
        description="fixed schema, fixed completed candidate table, fixed compatibility predicate",
        columns_by_prefix=columns_by_prefix,
        candidates_by_prefix=candidates_by_prefix,
        compat_formed_at=compat_formed_at,
        append_events=append_events,
        taf_trace=_trace(),
        time_columns_present=_time_columns(columns_by_prefix, append_events),
        join_candidate_available_before_inputs=True,
        join_compat_fixed_at_start=True,
        nonfixed_admissibility_provenance=False,
    )


def run_prefix_formed_model() -> ModelResult:
    columns_by_prefix = {
        "0": ["entity", "state", "value"],
        "1": ["entity", "state", "value"],
        "2": ["entity", "state", "value", "left", "right", "certificate"],
    }
    candidates_by_prefix = {
        "0": ["alpha", "beta"],
        "1": ["alpha", "beta"],
        "2": ["alpha", "beta", "join"],
    }
    compat_formed_at = {
        "seed_row": 0,
        "join_requires_two_locked_inputs": 2,
    }
    append_events = _append_events(
        candidate_from_join=2,
        join_schema="S_prefix_join_columns",
        join_predicate="join_requires_two_locked_inputs",
    )
    return ModelResult(
        model_id="B_prefix_formed",
        description="join candidate and join compatibility predicate are formed only after prefix records",
        columns_by_prefix=columns_by_prefix,
        candidates_by_prefix=candidates_by_prefix,
        compat_formed_at=compat_formed_at,
        append_events=append_events,
        taf_trace=_trace(),
        time_columns_present=_time_columns(columns_by_prefix, append_events),
        join_candidate_available_before_inputs=False,
        join_compat_fixed_at_start=False,
        nonfixed_admissibility_provenance=True,
    )


def taf_reconstruct_order(trace: list[TafTraceEvent]) -> dict[str, object]:
    event_ids = [event.event_id for event in trace]
    target_by_event = {event.event_id: set(event.target_records) for event in trace}
    source_by_event = {event.event_id: set(event.source_records) for event in trace}

    direct: set[tuple[str, str]] = set()
    for left in trace:
        for right in trace:
            if left.event_id == right.event_id:
                continue
            if target_by_event[left.event_id] & source_by_event[right.event_id]:
                direct.add((left.event_id, right.event_id))

    closure = {(event_id, event_id) for event_id in event_ids} | set(direct)
    changed = True
    while changed:
        changed = False
        additions = {
            (a, d)
            for (a, b) in closure
            for (c, d) in closure
            if b == c and (a, d) not in closure
        }
        if additions:
            closure |= additions
            changed = True

    incomparable: list[list[str]] = []
    for i, left in enumerate(event_ids):
        for right in event_ids[i + 1 :]:
            if (left, right) not in closure and (right, left) not in closure:
                incomparable.append([left, right])

    return {
        "events": event_ids,
        "direct_dependencies": [list(pair) for pair in sorted(direct)],
        "order_pairs": [list(pair) for pair in sorted(closure)],
        "incomparable_pairs": incomparable,
        "uses_time_column": False,
    }


def _trace_signature(trace: list[TafTraceEvent]) -> list[dict[str, object]]:
    return [asdict(event) for event in trace]


def run_fixture() -> dict[str, object]:
    fixed = run_fixed_schema_model()
    prefix = run_prefix_formed_model()
    fixed_order = taf_reconstruct_order(fixed.taf_trace)
    prefix_order = taf_reconstruct_order(prefix.taf_trace)

    external_trace_equal = _trace_signature(fixed.taf_trace) == _trace_signature(prefix.taf_trace)
    taf_order_equal = fixed_order == prefix_order
    no_time_column = not fixed.time_columns_present and not prefix.time_columns_present

    fixed_absorbs_external_behavior = (
        external_trace_equal
        and taf_order_equal
        and no_time_column
        and fixed.join_candidate_available_before_inputs
        and fixed.join_compat_fixed_at_start
    )
    ti_owned_provenance_difference = (
        prefix.nonfixed_admissibility_provenance
        and not prefix.join_candidate_available_before_inputs
        and not prefix.join_compat_fixed_at_start
    )

    return {
        "fixture": "record_table_admissibility_vs_taf_reconstruction_v0_1",
        "source_artifacts": [
            "explorations/E103-record-table-taf-boundary-v0-1-definition-2026-06-30.md",
            "../time-as-finality/results/finali-event-structure-v0.1-results.md",
            "../time-as-finality/results/reconstruction-without-background-time-v0.1-results.md",
        ],
        "models": {
            fixed.model_id: asdict(fixed),
            prefix.model_id: asdict(prefix),
        },
        "taf_reconstruction": {
            fixed.model_id: fixed_order,
            prefix.model_id: prefix_order,
        },
        "comparisons": {
            "external_trace_equal": external_trace_equal,
            "taf_reconstruction_equal": taf_order_equal,
            "no_time_column": no_time_column,
            "taF_absorbs_temporal_order": external_trace_equal and taf_order_equal,
            "ti_owned_admissibility_provenance_difference": ti_owned_provenance_difference,
            "fixed_completed_table_absorbs_external_behavior": fixed_absorbs_external_behavior,
            "source_side_residue_found": False,
        },
        "verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
            "claim_status_change": "none",
            "best_result": (
                "TaF absorbs downstream temporal reconstruction; TI-owned difference is "
                "admissibility provenance only, and this fixture does not defeat fixed-table absorption."
            ),
            "next_gate": "record_table_no_fixed_schema_witness_or_demote",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the record-table admissibility vs TaF reconstruction fixture."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_fixture()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
