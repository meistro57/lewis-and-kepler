# The Golden-Solids Construction — full chain, independently verified

A single nine-sphere construction around a cube forces the golden ratio out of
sphere-intersection algebra, producing dodecahedra and icosahedra at every scale.
Verified by Kepler from raw coordinates (symbolic + numerical), corroborated by
Lewis (symbolic spot-checks), matching Codex's reports exactly.

> Status: the *geometry* is verified. This is a **new declared construction**,
> NOT proof that the original 23-sphere registry contained these solids. The
> report's own controls (corner-only, envelope-only, and 11 aligned scale copies)
> all fail to produce the golden solids — so the positive result depends on a
> specific new relation, and we hold that distinction explicitly.

## The construction (CUBE-SPHERE-001)

Take a cube with corners (±h, ±h, ±h):

1. Put a radius-2h sphere at each of the 8 corners (each passes through its 3
   neighbor corners).
2. Add a central reference sphere of radius √3h through all 8 corners.

The 9 spheres give **160 raw triple-intersection records → 64 distinct points**.

## Why √5 appears without being inserted

For adjacent corners A=(h,−h,h), B=(−h,−h,h), the two radius-2h spheres and the
central radius-√3h sphere satisfy:

    x²+y²+z² = 3h²,  (x−h)²+(y+h)²+(z−h)² = 4h²,  (x+h)²+(y+h)²+(z−h)² = 4h²

Subtracting forces x=0 and z−y=h, leaving 2y²+2hy−2h²=0, whose roots are

    y/h = (−1 ± √5)/2 = 1/φ  and  −φ

So √5 (and the golden ratio φ=(1+√5)/2) **falls out of the algebra**. It is not
supplied to the generator. This is the crux, and it's the opposite of the
23-sphere registry, where the icosahedron/dodecahedron were *absent*.

## What the 64 points are

| Radius (÷h) | Points | Geometry |
|---|---:|---|
| √2−1 | 6 | regular octahedron |
| 1/√3 | 8 | smaller cube |
| 1 | 12 | regular cuboctahedron |
| √3 | 32 | **two regular dodecahedra sharing the cube** |
| √2+1 | 6 | regular octahedron |

The √3 shell = 8 cube corners + 12 golden-type-A + 12 golden-type-B. Each of
`cube+goldA` and `cube+goldB` is a regular dodecahedron (12 pentagonal faces),
verified via convex hull.

## Circle centers → icosahedra

On the √3 shell, **48 regular pentagonal circles** are found (every 5-subset
checked; equal edges + equal diagonals + diagonal/edge = φ). Their centers are
48 distinct points at two radius levels:

    R_inner² = 1 − 2/√5 ≈ 0.10557,  R_outer² = 1 + 2/√5 ≈ 1.89443

with exact ratio **R_outer/R_inner = 2 + √5 = φ³**.

Each level holds 24 centers = 12 antipodal pairs = **2 regular icosahedra**.
Total: **4 icosahedra** (2 orientations × 2 sizes), each 12 vertices / 20
triangular faces / 30 equal edges.

## Recursion (CUBE-RECURSION-002)

Searching the √3 shell for cubes (arbitrary orientation, no templates) finds
**9 full-size cubes** (5 per dodecahedron, 1 shared). Applying the nine-sphere
operation to each yields an inner cube of half-edge 1/3. The **reconvergence**:

    union of the 9 inner cubes' corners  =  the 1/3-size parent's dodecahedral
    shell  =  the original 32-point √3 shell scaled by 1/3

Identical to the last decimal. Two different routes — nine cubes read as inner
corners, vs. one small cube read as a dodecahedral compound — land on the same
32 points. Self-similarity; not graph equality.

## Cross-family intersections (CROSS-FAMILY-003)

Allowing the 42 generated spheres to intersect across parents (all 11,480
triples), independently reproduced:

| Triple outcome | Count |
|---|---:|
| two real points | 9,792 |
| empty, independent planes | 1,560 |
| empty, degenerate | 120 |
| entire shared circle | 8 |
| tangent | 0 |

→ 19,584 occurrences → **8,566 distinct points** (tolerance-stable).

Two exact connections:
1. **48 circle centers become sphere junctions** — recovered directly from
   intersections (verified symbolically for the explicit point
   p=((5−√5)/10, 0, (3√5−5)/10), on all three spheres exactly).
2. **8 triples share an entire circle** — the three spheres (center −s radius 2,
   center 0 radius 1/√3, center s/3 radius 2/3) all reduce to the same plane
   s·x=1/3 on the reference sphere, giving the circle |x|²=1/3, s·x=1/3, center
   s/9, radius 2√6/9. The 8 centers are the corners of the 1/9 cube.

## What remains open (honest)

- A complete mixed-family solid census.
- Whether the 48/288 and 4/24 recovery tallies re-derive (flagged, not yet stamped).
- **Incidence ≠ mechanism**: shared circles are not graph edges, and nothing
  here establishes signal flow, efficiency, or a physical growth process.
- This is a *declared construction*, not a discovery in the unchanged 23-sphere
  source.

## Reproduce

```sh
python scripts/verify_cube_sphere.py          # √5 forced, 64 pts, 2 dodecahedra
python scripts/verify_circle_center_ico.py    # 48 pentagons → 4 icosahedra
python scripts/verify_recursion.py            # 9 cubes, reconvergence
python scripts/verify_cross_family.py         # 11,480-triple census
```
