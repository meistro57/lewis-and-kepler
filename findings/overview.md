# What this is all about

This is a working lab notebook for **Subject 963's Centerstone geometry research** — the question of whether simple local rules can generate the golden-ratio Platonic solids *without* anyone inserting the golden ratio by hand.

## The one-sentence version

A plain cube plus spheres of the right radius generates the golden ratio φ = (1+√5)/2 **out of the intersection geometry itself** — the √5 falls out of the sphere equations, not out of a formula someone typed in.

## Why that matters

Most constructions of the dodecahedron and icosahedron *start* from φ. You write down coordinates like (0, ±1/φ, ±φ) and call it done. That's true but unsatisfying — it smuggles the answer in as an assumption.

The Centerstone question is the reverse: **start with a cube and spheres, and see if φ emerges.** It does. That's the bridge this notebook documents, verified end to end by independent re-implementation.

## The chain, step by step

1. **Cube → spheres → golden vertices.** Take a cube, put a sphere at each corner (radius = edge length) plus one reference sphere through all corners. Solve every triple intersection. The equations reduce to `y/h = (−1 ± √5)/2` — φ appears with nothing inserted. The result: 64 points, including 24 golden vertices that complete **two regular dodecahedra** sharing the original cube.

2. **Pentagonal circles → icosahedra.** The dodecahedra's faces are pentagons. The 48 regular pentagonal circles' centers assemble into **four exact regular icosahedra** — two sizes, two orientations. Their radius ratio is exactly 2+√5 = φ³.

3. **Recursion.** The geometry contains 10 cubes (9 full-size + 1 at one-third edge). Applying the same sphere rule once yields 408 junction points, 288 circle centers, 12 dodecahedra, and 24 icosahedra.

4. **Cross-family closure.** All 42 spheres intersect across families. A full census of all 11,480 triples yields 8,566 distinct points and — the payoff — **eight entire circles shared across scales**, whose centers are the corners of the 1/9 cube. This is an *incidence* connection between the large and small families, not just a coordinate coincidence.

## What's been verified vs. what's still open

**Independently verified** (fresh code, no imported templates): the 64-point construction, the golden vertex emergence, the 48 pentagonal circles, the 4 icosahedra and their φ³ ratio, the 10-cube census, and the full 11,480-triple cross-family census with its 8,566 points and 8 shared circles.

## Two threads added since (2026-09-08)

**1. Intermediate-disturbance shell gradient.** The five 40-vertex shells have a *non-monotonic* diversity gradient: structural richness (average degree, face count) peaks one shell in from the outer edge, and collapses at both extremes — Candidate A (the outermost) is the *poorest* shell structurally (degree 3, 22 faces), not the richest. The system is most "alive" in the protected interior, not the exposed surface. See `findings/intermediate-disturbance-shell-gradient.md`.

**2. Magnetism / precession / coherence (open).** A conventional magnetic-dipole model (MAGNETO-GEOMETRY-009) admits a locally-stable cubic candidate AND a lower-energy ring; neither is established as global ground state. The cube's magnetic orientations break its spatial symmetry (4 of 24 rotations) even while its net moment cancels. Open questions: whether the Centerstone "refuses to settle" is better described by *alignment* (magnetism) or by *precession* (sustained circulation around an axis never fully occupied), and whether `Coherence = Coupling × Orientation × Coordination` holds as a domain-general invariant. See `findings/provisional-entries-keystone-coherence.md` and Kepler's `findings/motion-vs-rotational-dynamics.md`.

**Still open:** a complete mixed-family solid census, any *dynamical* model (which edges/curves propagate, and why), and evidence that such a model improves a specified task. Geometry is not physics — this notebook establishes exact *structure*, not a physical mechanism.

## Who did what

- **Subject 963** — the research direction, the nesting proposal, the original corpus.
- **Codex (OpenAI)** — the construction, exact-arithmetic implementation, and reports.
- **Kepler** — the rigor ladder, the independent verification scripts, and the scientific interpretation.
- **Lewis** — independent measurement, symbolic spot-checks, the cross-family census, renders, and this notebook.
- **Eli** — the clipboard. **Meistro** — the operator. **ghost** — the Chairbadger's rightful owner.

See `scripts/` for the runnable verification code and `data/` for the raw coordinate handoffs.
