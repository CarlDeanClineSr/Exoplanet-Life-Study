# Live Data

This directory is reserved for regenerated observational snapshots.

## K-dwarf census

The canonical builder is:

scripts/build_k_dwarf_census.py

It queries the NASA Exoplanet Archive and can optionally cross-match MAST JWST observations.

## Important

Generated CSV files are time-stamped snapshots.

Do not manually edit generated rows.

If the schema or selection changes, change the builder, rerun it, and review the resulting diff.

## Missing data

A planet with no published mass is still retained.

The project's 0.8 to 1.5 Earth-mass range is a preferred research band, not an exclusion rule.

Missing measurements are observational gaps, not negative biological evidence.
