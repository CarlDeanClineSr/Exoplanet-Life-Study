#!/usr/bin/env python3
"""
Build a reproducible census of confirmed transiting planets hosted by
K-type main-sequence stars from the NASA Exoplanet Archive PSCompPars table.

Optional --jwst performs a MAST observation lookup for each unique host.

The script does not assign habitability or life scores. Missing values remain
explicit.

Standard-library dependencies are used for the NASA Exoplanet Archive query.
Optional MAST cross-match:
    pip install astroquery astropy
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TAP_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
TABLE = "pscomppars"

CANDIDATE_COLUMNS = [
    "pl_name",
    "hostname",
    "sy_dist",
    "sy_disterr1",
    "sy_disterr2",
    "st_spectype",
    "st_teff",
    "st_mass",
    "st_rad",
    "st_vj",
    "ra",
    "dec",
    "pl_masse",
    "pl_masseerr1",
    "pl_masseerr2",
    "pl_rade",
    "pl_radeerr1",
    "pl_radeerr2",
    "pl_dens",
    "pl_orbper",
    "pl_orbsmax",
    "pl_orbeccen",
    "pl_insol",
    "pl_eqt",
    "tran_flag",
    "pl_trandep",
    "pl_ntranspec",
    "pl_nespec",
    "pl_nobs_jwst_tran",
    "pl_nobs_jwst_e",
    "pl_nobs_jwst_pc",
]


def fetch_schema() -> set[str]:
    query = "select column_name from TAP_SCHEMA.columns where table_name = 'pscomppars'"
    payload = fetch_csv(query)
    return {row["column_name"] for row in csv.DictReader(io.StringIO(payload))}


def archive_query(columns: list[str]) -> str:
    select_list = ", ".join(columns)
    return (
        f"select {select_list} from {TABLE} "
        "where tran_flag = 1 "
        "and st_spectype is not null "
        "and st_spectype like 'K%'"
    )


def fetch_csv(query: str) -> str:
    params = urlencode({"query": query, "format": "csv"})
    request = Request(
        f"{TAP_URL}?{params}",
        headers={"User-Agent": "Exoplanet-Life-Study/0.1"},
    )
    with urlopen(request, timeout=90) as response:
        payload = response.read()
    return payload.decode("utf-8")


def parse_number(value: str | None) -> float | None:
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def classify_k_dwarf(spectral_type: str | None) -> tuple[bool, str]:
    if not spectral_type:
        return False, "missing"

    s = re.sub(r"\s+", "", spectral_type.upper())

    if not re.match(r"^K[0-9]", s):
        return False, "not_K"

    if re.search(r"(IV|III|II|IB|IA)$", s):
        return False, "non_main_sequence"

    if re.search(r"V(?:E|K|AR|COMP)?$", s):
        return True, "K_main_sequence_explicit"

    return True, "K_type_luminosity_class_unspecified"


def mass_band(mass: float | None) -> str:
    if mass is None:
        return "unknown"
    if 0.8 <= mass <= 1.5:
        return "within"
    if mass < 0.8:
        return "below"
    return "above"


def ly_from_pc(pc: float | None) -> float | None:
    return None if pc is None else pc * 3.26156


def build_base_rows(raw_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []

    for row in raw_rows:
        is_k, classification = classify_k_dwarf(row.get("st_spectype"))
        if not is_k:
            continue

        mass = parse_number(row.get("pl_masse"))
        distance_pc = parse_number(row.get("sy_dist"))

        new = dict(row)
        new["distance_ly"] = (
            f"{ly_from_pc(distance_pc):.3f}"
            if distance_pc is not None
            else ""
        )
        new["k_dwarf_classification"] = classification
        new["preferred_mass_band_0p8_1p5_me"] = mass_band(mass)
        new["jwst_mast_obs_count"] = ""
        new["jwst_mast_status"] = "not_queried"
        output.append(new)

    return output


def mast_lookup(target: str) -> tuple[int | None, str]:
    try:
        from astroquery.mast import Observations
    except ImportError:
        return None, "astroquery_not_installed"

    try:
        table = Observations.query_criteria(
            object_name=target,
            obs_collection="JWST",
        )
        return len(table), "queried"
    except Exception as exc:
        return None, f"query_error:{type(exc).__name__}"


def enrich_with_mast(rows: list[dict[str, Any]], delay_seconds: float) -> None:
    seen: dict[str, tuple[int | None, str]] = {}

    for row in rows:
        host = row.get("hostname", "").strip()
        if not host:
            continue

        if host not in seen:
            seen[host] = mast_lookup(host)
            time.sleep(delay_seconds)

        count, status = seen[host]
        row["jwst_mast_obs_count"] = "" if count is None else str(count)
        row["jwst_mast_status"] = status


def write_csv(rows: list[dict[str, Any]], output_path: Path, retrieval_time: str, source_columns: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    headers = source_columns + [
        "distance_ly",
        "k_dwarf_classification",
        "preferred_mass_band_0p8_1p5_me",
        "jwst_mast_obs_count",
        "jwst_mast_status",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        handle.write(f"# source=NASA Exoplanet Archive {TABLE}\n")
        handle.write(f"# retrieved_utc={retrieval_time}\n")
        handle.write(
            "# selection=confirmed transiting planets; host spectral type K*; "
            "main-sequence check applied locally\n"
        )
        handle.write(
            "# mass_window=0.8-1.5 Earth masses is a preferred research band, "
            "not an exclusion filter\n"
        )
        writer = csv.DictWriter(
            handle,
            fieldnames=headers,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/live/k_dwarf_transiting_targets.csv"),
    )
    parser.add_argument(
        "--jwst",
        action="store_true",
        help="Cross-match unique host names against MAST JWST observations.",
    )
    parser.add_argument(
        "--mast-delay",
        type=float,
        default=0.5,
        help="Delay between MAST host queries in seconds.",
    )
    args = parser.parse_args()

    retrieval_time = datetime.now(timezone.utc).isoformat()

    print("Checking NASA Exoplanet Archive TAP schema...")
    try:
        available = fetch_schema()
    except Exception as exc:
        print(f"ERROR: NASA TAP schema request failed: {exc}", file=sys.stderr)
        return 2

    missing_required = [name for name in ["pl_name", "hostname", "st_spectype", "tran_flag"] if name not in available]
    if missing_required:
        print(
            "ERROR: Required PSCompPars columns are missing: "
            + ", ".join(missing_required),
            file=sys.stderr,
        )
        return 2

    selected_columns = [
        name for name in CANDIDATE_COLUMNS
        if name in available
    ]
    for required in ["pl_name", "hostname", "st_spectype", "tran_flag"]:
        if required not in selected_columns:
            selected_columns.append(required)

    print("Using live-schema columns:")
    print(", ".join(selected_columns))

    query = archive_query(selected_columns)
    print(query)

    try:
        payload = fetch_csv(query)
    except Exception as exc:
        print(
            f"ERROR: NASA Exoplanet Archive request failed: {exc}",
            file=sys.stderr,
        )
        return 2

    raw_rows = list(csv.DictReader(io.StringIO(payload)))
    rows = build_base_rows(raw_rows)

    if args.jwst:
        print("Querying MAST for JWST observations...")
        enrich_with_mast(rows, args.mast_delay)

    write_csv(rows, args.output, retrieval_time, selected_columns)

    unique_hosts = len({r.get("hostname", "") for r in rows if r.get("hostname")})
    within_mass = sum(
        r["preferred_mass_band_0p8_1p5_me"] == "within"
        for r in rows
    )
    unknown_mass = sum(
        r["preferred_mass_band_0p8_1p5_me"] == "unknown"
        for r in rows
    )

    print(f"Rows written: {len(rows)}")
    print(f"Unique K-dwarf hosts: {unique_hosts}")
    print(f"0.8-1.5 M_E preferred band: {within_mass}")
    print(f"Mass unknown: {unknown_mass}")
    print(f"Output: {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
