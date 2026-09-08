# Lewis independent verification notes — 2026-09-08

## 1. Bloom orbit-stability (Spike-and-Bloom) — CLOSED

- G24 = 24 proper rotations, det∈{1}, all orthogonal, identity present, closed under multiplication → genuine octahedral group **O**. ✓
- native (362 verts) ⊆ G24_complete (626 verts) exactly (362/362). G24_complete = union of all G24-orbits of native vertices.
- Both graphs collapse to **138 distinct coordinate signatures** and **20 distinct G24-orbits**. Orbit-stable under octahedral action. ✓
- Note: raw vertex-level closure shows ~40% "misses" at 1e-4 — this is Float32 mesh-centerline quantization noise, NOT missing symmetry. The source header confirms "Not symbolic exact input." Signature/orbit counts are the robust readout.

## 2. "10 cubes" census (Recursion_002) — INDEPENDENTLY REPRODUCED

- Wrote my own sphere-triple intersection + exhaustive cube search, importing nothing from the packet.
- Recovered **64 distinct sphere-intersection points** (32 on central r=√3, 32 off) from the h=1 construction. ✓
- Detected **10 cubes**: 9 full-size (edge 2, half-edge h=1) in distinct orientations + 1 at one-third (edge 2/3, half-edge 1/3). All centered at origin. ✓

**Verdict: the census is sound. No number disagreement on the falsifiable joint.**

## 3. Process note (not a data divergence)
My first pass of the sphere-triple solver used wrong SVD nullspace indexing and
returned 8 points / 0 cubes. That was my bug (`Vt[2:]` vs `Vt[2]` on a 2×3
constraint matrix). Fixed; final run is clean. Flagging for reproducibility
only — the packet's math was never wrong, my first translation was.

Scripts: `/home/dev/Subject963/audit/_lewis_cube_census.py` (orbit check inline), cube census run ad-hoc.
