# Target Selection Profile

## Purpose

The project needs a practical way to decide which exoplanets deserve detailed study first.

The following is a **working target profile**, not an established law of nature.

It is designed to favor worlds where:

1. terrestrial conditions are physically plausible,
2. atmospheric chemistry can be meaningfully modeled, and
3. present or future telescopes have a realistic chance of measuring the atmosphere.

## Working target profile

### Host star

**K-type main-sequence star (K0–K9 V)**

Preferred characteristics:

- Nearby enough for useful signal-to-noise
- Bright enough for precision spectroscopy
- Relatively well characterized
- Low or moderate activity
- Measured UV/X-ray environment
- Long-lived main-sequence star

NASA identifies K dwarfs as an especially interesting "Goldilocks" stellar class between hotter G stars and more active M dwarfs. NASA gives typical K-dwarf lifetimes of roughly 15–45 billion years and notes that K stars are about three times as common as Sun-like G stars. These are population-level motivations, not guarantees for an individual system.

Reference:
https://science.nasa.gov/exoplanets/stars/
https://science.nasa.gov/missions/hubble/goldilocks-stars-are-best-places-to-look-for-life/

### Planet

Preferred initial research window:

**0.8–1.5 Earth masses**

This is a **selection window**, not a proven biological boundary.

Also collect radius and density because mass alone does not establish composition.

Prefer:

- Terrestrial or likely-terrestrial bulk composition
- Radius consistent with a rocky world
- No evidence for a massive H/He envelope
- Stable orbit
- Habitable-zone insolation

### Orbit

Prefer:

- Long-term residence in a temperate region
- Measurable transit geometry when atmospheric transmission spectroscopy is the objective
- Eccentricity low enough that a simple equilibrium interpretation is not misleading, or else explicitly model the eccentricity

### Rotation

**Do not make rapid rotation a hard filter.**

Rotation affects climate circulation and atmospheric dynamics, but tidal locking does not automatically make a planet uninhabitable. The repository should record rotation state as a physical variable and model its consequences rather than excluding worlds by assumption.

### Magnetosphere

**Do not make a global magnetic field a hard filter.**

A planetary dynamo is scientifically important, but it is not currently measurable for most candidate exoplanets and is not established as a necessary condition for surface habitability.

Instead record:

- Stellar wind environment
- Expected atmospheric loss
- Evidence for or against magnetic protection
- Uncertainty

### Plate tectonics and carbon cycling

Plate tectonics may be important to long-term climate regulation, but it should not be treated as a required property unless evidence supports it for the individual planet.

Record:

- Possible geochemical cycling
- Volcanism indicators
- Surface/ocean reservoir hypotheses
- Climate feedback assumptions

## Why K dwarfs are worth studying

NASA has specifically discussed K dwarfs as attractive habitability targets because they are cooler and longer-lived than G stars while generally being less extreme than M dwarfs. NASA also notes that their habitable zones are farther from the star than those of M dwarfs.

However, the repository should **not** state that K dwarfs automatically maximize atmospheric signal-to-noise.

Observability depends on:

- Stellar brightness
- Stellar radius
- Planet radius
- Atmospheric scale height
- Transit probability
- Orbital period
- Number of accessible transits
- Stellar variability
- Clouds/hazes
- Instrument sensitivity

The best target is therefore a **joint optimization of science and observability**, not simply a spectral class.

## M dwarfs

M dwarfs remain important targets and should not be deleted from the census.

They have major advantages for detecting small planets, but their close-in habitable zones, stellar activity, UV/X-ray environment, atmospheric-loss history, and possible photochemical false positives require explicit modeling.

Therefore:

**M dwarf = more complicated model**

not:

**M dwarf = automatically unsuitable**

## G dwarfs

G dwarfs remain scientifically essential because the Solar System provides the known Earth example.

They should remain in the comparison population.

## Proposed database filter

The first-generation search should support:

**K0–K9 V**
+
**terrestrial candidate**
+
**temperate/HZ candidate**
+
**transiting when atmosphere measurement is required**
+
**nearby/bright host**
+
**known or measurable stellar activity**

Then the same examination procedure can be applied to G and M stars as controls.

## Important correction to the "1.6 Earth-radius rule"

The project should not use "1.6 Earth radii = H/He envelope" as an absolute boundary.

Planet populations show a transition between rocky planets and larger volatile-rich worlds, but individual composition depends on mass, radius, irradiation, age, and formation history.

Use:

**mass + radius + density + atmosphere evidence**

rather than one radius cutoff.

## Important correction to the tidal-locking argument

A planet in a habitable zone around a low-mass star can become synchronously rotating, but synchronous rotation does not by itself prove atmospheric collapse or loss of habitability.

Climate models must be used.

## The target profile in one line

**Nearby, quiet K dwarf + likely rocky planet + temperate orbit + measurable atmosphere + enough signal for repeated spectroscopy.**

That is the working search target for this project.
