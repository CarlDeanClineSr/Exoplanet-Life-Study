# K-Dwarf Census Method

## Phase 3 objective

Build a reproducible census of confirmed transiting exoplanets hosted by K-type main-sequence stars.

The census is a research-triage and teaching dataset. It is not a claim that K dwarfs are universally the best life-search targets.

## Primary catalog

The NASA Exoplanet Archive Planetary Systems Composite Parameters (PSCompPars) table is the primary population table.

NASA describes PSCompPars as a one-row-per-confirmed-planet compilation intended for population studies and warns that parameters in one row may be drawn from different sources and may not be fully self-consistent.

Source:
https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html

## Initial selection

The first query selects:

- confirmed planets
- transiting planets
- host spectral types beginning with K

A local classification check then separates explicit K main-sequence classifications from ambiguous or non-main-sequence classifications.

## Main-sequence treatment

Preferred:
- K0 V through K9 V

Retained but flagged:
- K-type spectral classification where luminosity class is missing

Excluded:
- explicit K subgiants
- explicit K giants
- ambiguous classifications that cannot safely be interpreted as a K dwarf

## Mass window

The working research band is 0.8 to 1.5 Earth masses.

This is a preferred band, not a hard filter.

The census records:
- within
- below
- above
- unknown

A planet with unknown mass remains in the census.

## Target fields

For each planet record:

- host name
- planet name
- spectral type
- stellar temperature
- stellar mass and radius
- stellar distance
- V magnitude
- planet mass and uncertainty
- planet radius and uncertainty
- density
- orbital period
- semi-major axis
- eccentricity
- insolation
- equilibrium temperature
- transit depth
- transmission-spectrum count
- JWST transit/eclipse/phase counts when available from NExoList
- sky coordinates

NASA documents these fields in the Exoplanet Archive data-column documentation.

Source:
https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html

## JWST cross-match

Two different records are retained.

NExoList count:
An Exoplanet Archive field indicating approved JWST observations associated with a planet.

MAST match:
A separate archival query to MAST for JWST observations associated with the host target.

These are not treated as interchangeable.

## Observability variables

Calculate or record:

- distance
- stellar brightness
- stellar radius
- planet radius
- transit depth
- orbital period
- mass availability
- atmospheric spectroscopy history
- JWST observation count
- stellar activity information availability

Do not call this a biological ranking.

## Reproducibility

The canonical builder is:

scripts/build_k_dwarf_census.py

Each generated snapshot should preserve:

- source service
- query
- retrieval time
- archive update information where available
- script version or commit
- field definitions

The generated dataset is a time-stamped snapshot, not permanent truth.
