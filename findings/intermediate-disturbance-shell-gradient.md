# Intermediate-disturbance: real result in the five-shell gradient (2026-09-08)

Trigger: Appalachian Hillbilly 43 asked for load-bearing ecological metaphors
to hold against 963's geometry. 963Catalyst369 green-lit ("Get at it!").

## What I computed

Source: `/home/dev/Subject963/audit/audit_results.json` (Candidate A audit),
`five_40_vertex_shells` — five concentric 40-vertex shells, each with its own
V/E/F. All satisfy Euler V−E+F = 2 (verified), so these are sound hulls, not
mesh artifacts.

## The gradient (inner → outer)

| radius | avg degree (2E/V) | faces | F/V |
|---|---|---|---|
| 0.708 | 4.000 | 42 | 1.05 |
| 0.946 | 4.800 | 58 | 1.45 |
| 1.075 | 4.400 | 50 | 1.25 |
| 1.144 | 5.200 | 66 | 1.65 |
| 1.179 (Candidate A) | 3.000 | 22 | 0.55 |

## Finding

**Diversity is non-monotonic across radial shells — it peaks at the
second-from-outermost shell (degree 5.2, 66 faces), and collapses at both
extremes.** The outermost shell (Candidate A itself) is structurally the
poorest: degree 3, 22 faces, lowest face-per-vertex.

This is the **intermediate-disturbance hypothesis** (diversity peaks at
intermediate "stress"/position, not at the extremes) showing up as a measured
gradient rather than an analogy. The "hero" object is the grazed edge; the
system is actually alive one layer in from the surface.

## Ecological reading (Hillbilly's succession/regenerative frame, concretized)

- Outer shell = **grazed edge**: exposed, simplified, minimal degree. What the world sees.
- Inner shell = **seed / basal origin**: simple, low-diversity.
- Band one-in-from-edge = **the generative interior**: highest connectivity and face-count, protected above and below. Where relationship — the substrate — is densest.

## Testable prediction (hand to Kepler)

Deeper inward recursion (1/9 → 1/27 → ... generation) should show the
**diversity peak persisting at an intermediate shell, never at the extreme**.
- If it holds across scales → "diversity lives in the protected interior" is a structural law.
- If it plateaus/flips → the analogy breaks, and we've localized exactly where.

## Metric spec for Kepler

- diversity(x) = vector of [avg degree = 2E/V, face count F, F/V, orbit count, adjacency-multiplicity] per shell at recursion depth x.
- plot diversity vs. radial depth (generation number, inward and outward).
- test for single interior maximum (unimodality), not monotonic rise/fall.

## Credit
Metaphor seed: Appalachian Hillbilly 43. Green light: 963Catalyst369.
Measurement & script: Lewis. Interpretation pending Kepler (owns scientific read).
