"""Absorber gauntlet for the E096 clock-free record-cadence fixture.

The target is the C behavior from E096: reject the hostile p3 proposal, admit
p4, preserve coherence without revision, and use no hidden global tick.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import clock_free_record_cadence_fixture as e096


@dataclass(frozen=True)
class AbsorberResult:
    absorber_id: str
    description: str
    reproduces_c_exactly: bool
    uses_hidden_tick: bool
    revises_final_records: bool
    admitted_records: list[str]
    rejected_records: list[str]
    reason: str
    verdict: str


def c_signature() -> dict[str, object]:
    c = e096.run_fixture()["systems"]["C"]
    return {
        "admitted_records": c["admitted_records"],
        "rejected_records": c["rejected_records"],
        "global_ticks_used": c["global_ticks_used"],
        "hidden_total_order_used": c["hidden_total_order_used"],
        "revised_final_records": c["revised_final_records"],
        "coherence_without_revision": c["coherence_without_revision"],
    }


def result(
    absorber_id: str,
    description: str,
    admitted: list[str],
    rejected: list[str],
    uses_hidden_tick: bool,
    revises_final_records: bool,
    reason: str,
) -> AbsorberResult:
    c = c_signature()
    exact = (
        admitted == c["admitted_records"]
        and rejected == c["rejected_records"]
        and not uses_hidden_tick
        and not revises_final_records
    )
    return AbsorberResult(
        absorber_id=absorber_id,
        description=description,
        reproduces_c_exactly=exact,
        uses_hidden_tick=uses_hidden_tick,
        revises_final_records=revises_final_records,
        admitted_records=admitted,
        rejected_records=rejected,
        reason=reason,
        verdict="absorbs_C" if exact else "does_not_absorb_C",
    )


def run_fixed_site_sheaf() -> AbsorberResult:
    return result(
        absorber_id="fixed_site_sheaf_gluing",
        description="fixed cover with local sections and parity compatibility on overlaps",
        admitted=["p1", "p2", "p4", "p5", "p6", "p7"],
        rejected=["p3"],
        uses_hidden_tick=False,
        revises_final_records=False,
        reason=(
            "The observer patches, handle set, bit projections, and parity compatibility "
            "predicate are all fixed in advance. Prefix extendability rejects p3 exactly."
        ),
    )


def run_causal_order_only() -> AbsorberResult:
    return result(
        absorber_id="ordinary_causal_order_only",
        description="partial order of proposal dependencies without a value compatibility predicate",
        admitted=["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
        rejected=[],
        uses_hidden_tick=False,
        revises_final_records=False,
        reason=(
            "A causal partial order can say p3 occurs after p1 and p2, but order alone does "
            "not know that x_BC=0 violates parity. It needs an added compatibility predicate."
        ),
    )


def run_database_constraint() -> AbsorberResult:
    return result(
        absorber_id="database_constraint_checking",
        description="known relational schema with a parity CHECK constraint per record handle",
        admitted=["p1", "p2", "p4", "p5", "p6", "p7"],
        rejected=["p3"],
        uses_hidden_tick=False,
        revises_final_records=False,
        reason=(
            "The behavior is reproduced by ordinary online insertion into a known schema with "
            "a deferred-but-prefix-checkable parity constraint."
        ),
    )


def run_fixed_h_record_update() -> AbsorberResult:
    return result(
        absorber_id="fixed_H_record_update",
        description="fixed finite state space with allowed subspace parity projector",
        admitted=["p1", "p2", "p4", "p5", "p6", "p7"],
        rejected=["p3"],
        uses_hidden_tick=False,
        revises_final_records=False,
        reason=(
            "A fixed finite state space over the two handles can contain the parity-allowed "
            "record states from the start; update is projection/filtering, not H growth."
        ),
    )


def run_fixed_latent_access() -> AbsorberResult:
    return result(
        absorber_id="fixed_latent_source_changing_access",
        description="completed latent parity table with observers receiving partial apertures",
        admitted=["p1", "p2", "p4", "p5", "p6", "p7"],
        rejected=["p3"],
        uses_hidden_tick=False,
        revises_final_records=False,
        reason=(
            "The full admissible table for h0 and h1 can be fixed from the start; observers "
            "only gain access to local projections as proposals arrive."
        ),
    )


def run_gauntlet() -> dict[str, object]:
    absorbers = [
        run_fixed_site_sheaf(),
        run_causal_order_only(),
        run_database_constraint(),
        run_fixed_h_record_update(),
        run_fixed_latent_access(),
    ]
    absorbing = [absorber.absorber_id for absorber in absorbers if absorber.reproduces_c_exactly]
    failing = [absorber.absorber_id for absorber in absorbers if not absorber.reproduces_c_exactly]

    return {
        "fixture": "clock_free_cadence_absorber_gauntlet_v0_1",
        "source_artifacts": [
            "explorations/E096-clock-free-record-cadence-fixture-2026-06-30.md",
            "tools/clock_free_record_cadence_fixture.py",
        ],
        "target_c_signature": c_signature(),
        "absorbers": {absorber.absorber_id: asdict(absorber) for absorber in absorbers},
        "summary": {
            "absorbing_count": len(absorbing),
            "failing_count": len(failing),
            "absorbing_absorbers": absorbing,
            "failing_absorbers": failing,
            "source_side_residue_found": False,
            "strongest_survivor": (
                "clock-free record coherence is a useful reconstruction-layer discipline, "
                "but E096 C is fully reproduced by fixed compatibility/admissibility machinery"
            ),
        },
        "verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
            "claim_status_change": "none",
            "path_kill": (
                "E096 clock-free coherence by itself => source-side Temporal Issuance evidence"
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the E097 clock-free cadence absorber gauntlet.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    data = run_gauntlet()
    text = json.dumps(data, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
