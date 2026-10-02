# First K-Dwarf Census Results

## Snapshot

Run #5 of the Refresh K-dwarf census workflow successfully queried the NASA Exoplanet Archive PSCompPars table.

Results:
- 226 confirmed transiting planet rows
- 152 unique K-type host stars
- 4 planets in the preferred 0.8–1.5 Earth-mass band
- 38 planet rows with nonzero NExoList JWST observation counts
- 28 unique hosts represented among those JWST-count rows
- 30 planet rows with at least one JWST transit count

This is a time-stamped catalog snapshot. Future archive updates can change the numbers.

## The four preferred-mass records

| Planet | Host | Spectral type | Distance (ly) | Best mass (M_E) | Mass provenance | Radius (R_E) | Insolation |
|---|---|---|---:|---:|---|---:|---:|
| TOI-500 b | TOI-500 | K6 V | ~154.6 | 1.420 | Mass | 1.166 | 1138 Earth |
| EPIC 201754305 d | K2-16 | K3 V | ~1092.5 | 1.080 | M-R relationship | 1.030 | not reported |
| HD 101581 c | HIP 56998 | K4/5V | ~41.7 | 0.937 | M-R relationship | 0.990 | 52 Earth |
| HD 101581 b | HIP 56998 | K4/5V | ~41.7 | 0.827 | M-R relationship | 0.956 | 80 Earth |

The distances are converted from parsecs using 1 pc = 3.26156 light-years.

## First scientific lesson

The target mass band is only one filter.

None of the three records with reported insolation values is close to the Earth-like irradiation regime. EPIC 201754305 d needs additional investigation because the snapshot does not report an insolation value.

Mass provenance also matters. Three different situations are visible in this first set:

- direct/dynamical mass provenance
- mass estimated from a mass-radius relationship
- missing/uncertain physical parameters

The database therefore records the provenance rather than treating every catalog mass as equally measured.

## JWST lesson

The 38 JWST-count rows are not automatically atmospheric detections.

NExoList observation counts indicate associated approved JWST observations. They do not by themselves establish:
- a usable spectrum,
- molecular detection,
- atmospheric retrieval,
- or a life-related result.

Phase 4 must cross-match these rows with actual MAST observations and record instrument, mode, wavelength range, and published analysis.

## Classification lesson

The raw K-type query intentionally retains boundary and ambiguous stellar classifications.

The builder now reports:
- strict K main-sequence
- K-type luminosity class unspecified
- K/M boundary or mixed
- ambiguous non-main-sequence luminosity class

This prevents a star such as K0 IV/V from being silently treated as an unambiguous K dwarf.

## Sources

NASA Exoplanet Archive PSCompPars:
https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html

PSCompPars column definitions:
https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html

NASA Exoplanet Archive JWST / NExoList:
https://exoplanetarchive.ipac.caltech.edu/docs/JWSTMission.html
