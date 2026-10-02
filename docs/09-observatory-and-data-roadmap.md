# Observatory and Data Roadmap

## Current architecture

The scientific question is kept separate from the instrument.

**Question:**
Can the observed planetary system sustain a strongly disequilibrium atmosphere?

**Current observing sources may include:**

- JWST
- Hubble
- ground-based spectroscopy
- Kepler/K2/TESS discovery and transit data
- Gaia stellar properties
- laboratory measurements and photochemical models

## JWST

JWST's role is primarily infrared atmospheric characterization.

Useful observation types include:

- Transit spectroscopy
- Eclipse spectroscopy
- Phase-curve observations
- Time-series photometry/spectroscopy

NASA's Earth-as-an-exoplanet explanation identifies transmission spectroscopy as a major method for remotely determining atmospheric composition and illustrates expected signals from molecules including H2O, CO2, O2 and CH4.

Reference:
https://science.nasa.gov/mission/webb/science-overview/science-explainers/what-would-earths-atmosphere-look-like-from-the-james-webb-space-telescope/

## MAST

MAST/STScI is the archival layer for many space-telescope observations.

The project should eventually record:

- Program ID
- Target
- Planet
- Instrument
- Mode
- Observation date
- Wavelength range
- Data product
- Publication
- Molecules analyzed
- Detection limits

Reference:
https://archive.stsci.edu/missions-and-data/jwst

## NASA Exoplanet Archive

Use the archive for:

- Host-star parameters
- Planet parameters
- Transit flags
- Discovery methods
- Orbital parameters
- Literature references

Reference:
https://exoplanetarchive.ipac.caltech.edu/

## Roman

The Nancy Grace Roman Space Telescope launched on **August 30, 2026** according to NASA.

Roman is now part of the project's future data ecosystem. Its wide-field survey capabilities can contribute to the broader exoplanet census and target discovery/characterization pipeline, while atmospheric biosignature confirmation remains a different observational problem.

Reference:
https://science.nasa.gov/mission/roman-space-telescope/roman-launch/

## Habitable Worlds Observatory

NASA describes the Habitable Worlds Observatory as a future observatory designed specifically to identify and directly image potentially habitable planets and search their atmospheres for biosignature gases.

Reference:
https://science.nasa.gov/astrophysics/programs/habitable-worlds-observatory/

## Data architecture

The eventual pipeline is:

**catalogs**
→ **target selection**
→ **observations**
→ **spectra**
→ **molecular retrieval**
→ **photochemical model**
→ **abiotic challenge**
→ **repeat observations**
→ **independent confirmation**
→ **evidence report**

The telescope may change.

The examination method should not.
