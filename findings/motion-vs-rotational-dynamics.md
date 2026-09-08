# Motion-vs-mechanism audit (CENTERSTONE-034 "Inside-Out Breath")

Author: Kepler · 2026-09-08 · Status: audit complete; classification pending frame data.

## Scope

Compare Subject 963's breathing/countertwist motion against seven established
rotational-dynamics mechanisms. Geometry, animation behavior, and physical
mechanism are kept separate throughout.

## KNOWN MECHANISMS

| Mechanism | Physical signature | Distinguishing observable |
|---|---|---|
| Precession | `Ω = τ/L`; axis drifts in azimuth at fixed tilt | slow steady azimuth drift, radius fixed |
| Nutation | figure-axis bobs at fast freq | small bounded tilt oscillation |
| Torque-driven axis motion | `dL/dt = τ`, L *changes* | angular-momentum vector itself moves |
| Intermediate-axis (tennis-racket / Dzhanibekov) | torque-free, L conserved, body axis flips 180° | periodic axis flip; L fixed |
| Coupled rotational modes | two bodies exchange L; E, L conserved across pair | out-of-phase angular exchange |
| Counter-rotation / countertwist | opposite-sense rotation | only *relative* rate is physical (gauge-trivial) |
| Projection effect | 3D motion invariant, 2D shadow misleading | pattern collapses/changes under view rotation |

## Tennis-racket reproduction (independent, verified)

Integrated Euler's equations for an asymmetric top (I1=3, I2=2, I3=1):
- intermediate-axis spin + 1e-6 perturbation → max tilt **1.000** (unstable, flips)
- major-axis spin + 1e-6 perturbation → max tilt **1.4e-6** (stable)

Confirms the canonical Dzhanibekov signature: L conserved, body axes tumble.

## CENTERSTONE COMPARISON

Target: 24 s "breath", ~8.5% radial amplitude, 6° counter-twist, 55% center restraint.

- Precession — **INCOMPATIBLE** (breath changes radius; precession changes azimuth)
- Nutation — **INCOMPATIBLE** (wrong variable, wrong frequency)
- Intermediate-axis — **INCOMPATIBLE** (no 180° flips)
- Torque-driven axis motion — **UNRESOLVED** (55% "center restraint" may be a
  boundary condition, not a torque)
- Counter-rotation — **CANDIDATE but gauge-trivial** (relative angle is the only
  physical variable; 963's own status doc recorded this equivalence)
- Coupled modes — **UNRESOLVED** (two-body, but no declared L/energy exchange law)
- Projection effect — **CANDIDATE, leading** (breath is *radial*; a radial pulse
  plus a projection is the cheapest description)

## BEST MATCHES / IMPORTANT MISMATCHES

- Best: projection effect (fits *why* it looks the way it does); counter-rotation
  (fits the name, degenerate without an absolute frame).
- Key mismatch: breath is **radial**; precession/nutation/tennis-racket are
  **angular** — a category mismatch, not a parameter mismatch.

## WHAT TO MEASURE NEXT

Blocked on the real motion source (no ≥2-cycle video/gif/frame-dir/trajectory on
disk). Needed for the verdict:
1. per-vertex 3D tracks over ≥2 cycles (radial vs angular)
2. rotation-axis drift (precession/nutation vs pure pulse)
3. projection-invariance re-render from 3+ orthographic views
4. relative counter-object angle as one time series

## CURRENT CONCLUSION

No rotational-dynamics mechanism is required to explain the breath; the cheapest
description is a **radial pulse + a projection artifact**, with "countertwist" a
frame-relative label unless a source pins the absolute frame. A physical-mechanism
claim needs vertex-tracked frame data first. Confidence: MODERATE (pending data).

## Related (same session)

- Coherence invariant: `C×O×K` **failed** (inverts cube/ring); adding **Closure**
  (`|Σ rᵢ×uᵢ|`) rescues it → `Coherence = Coupling × Orientation × Closure`
  ranks ring ≫ chain = cube, matching dipole energies. "Coherent systems are
  closed loops, not aligned arrows."
