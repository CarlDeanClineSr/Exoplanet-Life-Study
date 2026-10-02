# Earth Spectral Baseline

## Purpose

This is the first worked observation lesson in the project.

We start with Earth because its biology is independently established. We can therefore ask what an exoplanet observer would actually measure without pretending that a similar spectrum automatically proves life elsewhere.

NASA provides a model of an Earth-like transmission spectrum from 0.6 to 28 microns specifically for this teaching purpose. The modeled spectrum contains signatures associated with water vapor, carbon dioxide, oxygen, methane, ozone and other atmospheric constituents. [NASA — What would Earth's atmosphere look like from the James Webb Space Telescope?](https://science.nasa.gov/mission/webb/science-overview/science-explainers/what-would-earths-atmosphere-look-like-from-the-james-webb-space-telescope/)

## The observation chain

```
STAR LIGHT
   |
   v
  PLANET
  ATMOSPHERE
   |
   v
MOLECULES ABSORB
SPECIFIC WAVELENGTHS
   |
   v
TRANSMISSION SPECTRUM
   |
   v
MOLECULAR RETRIEVAL
   |
   v
CHEMICAL MODEL
   |
   v
ABIOTIC CHALLENGE
```

A spectral feature is not itself a diagnosis. It is a measurement used to constrain atmospheric composition.

## Teaching spectral map

The project uses representative molecular bands as **teaching landmarks**, not as a substitute for line-by-line spectroscopy.

| Molecule / system | Representative feature(s), microns | JWST coverage | Teaching significance |
|---|---|---|---|
| O2 | 0.63, 0.69, 0.76, 1.27 | NIRSpec covers these wavelengths | Oxygen constraint; 0.76 microns is the O2 A band |
| O4 (O2-O2) | 1.06, 1.27 | NIRSpec | Oxygen-pressure / abiotic-ocean-loss diagnostic |
| H2O | 0.94, 1.4, 1.9, 2.7, 6.3 | NIRSpec + MIRI | Water-vapor and thermal-structure context |
| CO2 | 1.6, 2.0, 2.7, 4.3, 15 | NIRSpec + MIRI | Carbon-cycle / atmospheric-pressure context |
| CH4 | 3.3, 7.7 | NIRSpec + MIRI | Reduced-carbon gas; important with oxidants |
| N2O | 2.3, 4.5, 7.7 | NIRSpec + MIRI | Nitrogen-cycle biosignature candidate |
| CO | 4.6–4.7 | NIRSpec | Important abiotic diagnostic alongside CO2/O2 |
| NO2 | ~6.1 | MIRI | Reactive nitrogen chemistry |
| HNO3 | ~7.5, ~11.3 | MIRI | Oxidized nitrogen chemistry; reservoir for NOx |
| O3 | ~9.6 | MIRI | Oxygen photochemistry |
| SO2 | ~7.3, ~8.6 | MIRI | Volcanic / sulfur chemistry |

Spectral landmarks are drawn from atmospheric/exoplanet spectroscopy literature and molecular databases. They should not be interpreted as saying that every listed molecule is detectable with JWST for every exoplanet.

## JWST wavelength coverage

### NIRSpec

NIRSpec operates from about **0.6 to 5.3 microns**, depending on observing configuration. Its prism can cover the full nominal NIRSpec range in one exposure; grating modes divide the coverage among configurations.

Reference:
[JWST NIRSpec Dispersers and Filters](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-dispersers-and-filters)

### MIRI

MIRI spectroscopy extends from about **4.9 to 27.9 microns**.

MIRI LRS provides approximately 5–14 micron low-resolution spectroscopy.

MIRI MRS provides approximately 4.9–27.9 micron medium-resolution spectroscopy.

Reference:
[JWST MIRI Medium Resolution Spectroscopy](https://jwst-docs.stsci.edu/jwst-mid-infrared-instrument/miri-observing-modes/miri-medium-resolution-spectroscopy)

## What this means for the project

The atmospheric panel should be split into two major observational regions:

**Near infrared: 0.6–5.3 microns**

Important targets include:

- O2 A band
- O2 1.27 micron band
- H2O
- CO2
- CH4 near 3.3 micron
- CO near 4.6–4.7 micron
- N2O near 4.5 micron

**Mid infrared: 4.9–27.9 microns**

Important targets include:

- H2O near 6.3 micron
- NO2 near 6.1 micron
- CH4 near 7.7 micron
- N2O near 7.7 micron
- O3 near 9.6 micron
- HNO3 near 11.3 micron
- CO2 near 15 micron

## The critical limitation

A molecule falling inside an instrument's wavelength range does **not** mean JWST can detect it in a particular exoplanet.

Detectability depends on:

- host-star brightness
- planet/star radius ratio
- atmospheric scale height
- molecular abundance
- temperature
- pressure
- clouds
- hazes
- stellar activity
- spectral resolution
- number of observations
- systematic noise

Therefore the repository must distinguish:

**spectral coverage**

from

**actual detectability**

and from

**actual detection**.

## Earth exercise

Using the Earth reference atmosphere:

1. Identify the O2 and CH4 bands.
2. Identify the strongest CO2 bands.
3. Identify the O3 9.6 micron band.
4. Identify the H2O bands.
5. Identify N2O and HNO3 regions.
6. Identify CO as an abiotic diagnostic.
7. Ask which observations are possible with NIRSpec.
8. Ask which observations require MIRI.
9. Ask which features would be blended.
10. Ask which features require an atmosphere model before they can be interpreted.

## What we are looking for

The project is not looking for one molecule.

The desired scientific object is a **coherent atmospheric state**.

For example:

**H2O + CO2 + N2 + O2/O3 + CH4 + N2O**

must be evaluated together with:

**CO + NO2 + HNO3 + SO2**

and with the star's radiation environment.

The central question becomes:

> Can the observed chemical state be maintained by known non-biological processes?

If the answer is not known, the result remains unresolved.

## Sources

- NASA — Earth transmission spectrum and JWST comparison
- HITRAN — molecular species and spectroscopic data
- NIST Chemistry WebBook — laboratory IR spectra
- Peer-reviewed exoplanet biosignature literature
- JWST/STScI instrument documentation
