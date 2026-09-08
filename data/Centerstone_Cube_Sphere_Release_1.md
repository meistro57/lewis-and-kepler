# Centerstone: spheres generate the golden vertices

**Experiment CUBE-SPHERE-001 · September 8, 2026**

**Research direction and originating Centerstone work: Subject963. New construction, computation, visualization, and exact verification in this experiment: OpenAI Codex.** Earlier geometry and contributor credits are preserved. This is an additive extension, not a replacement of the original 23-sphere construction.

## What we established

A specified nine-sphere construction, based on one already verified cube, generates **two exact regular dodecahedra sharing that cube**. The golden-ratio coordinates follow from the sphere-intersection equations; they are not supplied to the sphere generator.

Its generated points also determine **48 exact regular pentagonal circles**. Their centers form **four exact regular icosahedra**, arranged in two orientations at two sizes. The smaller icosahedra come from internal pentagonal rings, while the larger ones come from dodecahedral face circles.

This gives a concrete route through the geometry:

**Verified cube → cube-derived spheres → actual intersection points → regular pentagonal circles → their centers.**

![Sphere-based construction of the golden solids](Centerstone_Sphere_to_Golden_Solids.png)

## The construction, explicitly

Take a cube with corners (±h, ±h, ±h), where signs are independent.

1. Put one sphere at each of its eight corners. Give each sphere radius **2h**, the cube's edge length. Each therefore passes through that corner's three neighboring cube vertices.
2. Retain a central reference sphere of radius **√3h**, through all eight cube corners.
3. Find every isolated intersection of three of these nine sphere surfaces.
4. Among the generated points on the central reference sphere, identify regular pentagonal circles. Record their centers as a distinct derived point type.

The reference in step 2 is the **circumsphere of the cube vertices**. It does not enclose the complete corner spheres. A concentric envelope enclosing those whole balls would instead have radius **(√3 + 2)h**.

This is a new, declared extension. The previously saved seven-circle nesting rule uses envelopes around complete circles and was specified exactly in 2D; it did not already prescribe these nine 3D spheres or the subsequent circle-center operation.

## How √5 appears without inserting it

Choose adjacent cube corners A = (h, −h, h) and B = (−h, −h, h). Their two radius-2h spheres meet the central radius-√3h sphere where

    x² + y² + z² = 3h²,
    (x − h)² + (y + h)² + (z − h)² = 4h²,
    (x + h)² + (y + h)² + (z − h)² = 4h².

Subtracting these equations gives

    x = 0,
    z − y = h,
    y² + z² = 3h².

Therefore

    2y² + 2hy − 2h² = 0,
    y/h = (−1 ± √5)/2.

Writing φ = (1 + √5)/2, the two resulting points are

    (0, h/φ, hφ),
    (0, −hφ, −h/φ).

Repeating this across the twelve cube edges produces **24 distinct golden vertices**. Together with the eight original cube corners, they form two regular dodecahedra. Each contains 20 points, and their overlap is exactly the original eight-point cube: 20 + 20 − 8 = 32.

One dodecahedron uses the cube corners plus signed cyclic permutations of (0, h/φ, hφ). The other uses the corresponding opposite coordinate ordering. A **90° rotation about a cube coordinate axis** exchanges the two while preserving their shared cube as a point set. This is a static orientation relationship; no motion law was simulated.

## The sphere intersections and the circle centers are different layers

The nine spheres produce **160 raw triple-intersection records**, consolidating to **64 distinct intersection points**. Including the central sphere's center gives a 65-point center-and-junction registry.

The normalized intersection points occupy five radial shells:

| Radius divided by h | Points | Geometry on that shell |
|---|---:|---|
| √2 − 1 | 6 | Regular octahedron |
| 1/√3 | 8 | Smaller cube |
| 1 | 12 | Regular cuboctahedron |
| √3 | 32 | Two regular dodecahedra sharing the original cube |
| √2 + 1 | 6 | Regular octahedron |

The original and smaller cubes each contain two complementary regular tetrahedra. Thus tetrahedra, cubes, octahedra, and dodecahedra have vertices in the sphere-intersection layer. The icosahedra are recovered at the **next circle-center layer**; the finite search found none among the 65 center-and-junction points themselves.

The search for circles used all coplanar candidate triples among the 32 points on the central reference sphere. It checked for five equally spaced points on a circle, rather than supplying dodecahedron faces as input. It found and exactly verified **48 regular pentagonal circles with 48 distinct centers**. Their centers partition into four disjoint 12-vertex regular icosahedra.

| Circle-center level | Radius | Icosahedra |
|---|---|---:|
| Inner | h√(1 − 2/√5) ≈ 0.324919696h | 2 orientations |
| Outer | h√(1 + 2/√5) ≈ 1.376381920h | 2 orientations |

Matching inner and outer copies share directions but differ in depth. Their exact radius ratio is

    R_outer / R_inner = 2 + √5 = φ³ ≈ 4.2360679775.

This is a genuine nested-scale relation in the constructed geometry. It is not a demonstrated growth rate, feedback gain, or physical frequency.

## Applying it at our three verified cube scales

All lengths below use the original sphere-radius units. The eight seed corners in each row were matched back to the existing original registry.

| Existing cube | Corner-sphere radius | Cube reference radius | Inner icosahedron radius | Outer icosahedron radius |
|---|---:|---:|---:|---:|
| Inner | 0.488033872 | 0.422649731 | 0.079285909 | 0.335860499 |
| Middle | 1.333333333 | 1.154700538 | 0.216613131 | 0.917587947 |
| Outer | 1.821367205 | 1.577350269 | 0.295899039 | 1.253448446 |

Each row gives the same construction at a different scale. These new corner spheres are derived from the verified cube; they are not relabeled as original members of the 23-sphere family.

## Controls: which step made the difference?

| Test | Outcome in the tested point sets |
|---|---|
| Eight corner spheres alone | 40 distinct triple-intersection points; no complete regular dodecahedron or icosahedron found |
| Add the envelope around the whole corner balls, radius (√3 + 2)h | Same 40 intersection points; no complete golden solid found |
| Add the sphere through the cube vertices, radius √3h | 64 intersection points; two exact regular dodecahedra |
| Read centers of the regular pentagonal circles | Four exact regular icosahedra |

The 40-point control is a different construction from the earlier object named Candidate A. A matching count does not identify the objects.

We also tested an aligned scale extension of the original 23-sphere family at scales 1, 2, 3, 4, 6, 8 and their reciprocals. Across **253 spheres**, none of the **72 fixed golden target positions** associated with the three cube scales lay on any of those sphere surfaces at tolerance 10⁻⁷. The nearest boundary gap was approximately 0.00142073 in original radius units.

That test concerns fixed cube-anchored targets and aligned scale copies. It does not exclude other relative rotations, translations, continuous-curve constructions, or different recursive growth operations. The reciprocal copies were a shrinking-scale diagnostic; they were not silently added to the earlier outward-only nesting rule.

The positive result therefore depends on a specific new relation: **spheres centered at cube corners, with edge-length radii, intersect a reference sphere through those corners**. Enlarging a whole-ball envelope alone did not supply the same relation in these controls.

## Exact verification and numerical checks

The symbolic certificate verified all 64 normalized intersection coordinates using exact expressions in √2 and √5. Of the 84 possible sphere triples, 80 have two distinct exact solutions each; the remaining four have inconsistent collinear constraints. This establishes the complete isolated triple-intersection census for these nine spheres.

It also verified:

- Both generated dodecahedra match exact standard coordinate sets.
- All 48 detected pentagons are planar, have equal edges and equal circumradii, and have the exact regular-pentagon diagonal-to-edge ratio.
- The 48 exact circle centers form the four reported regular icosahedra.
- The two circle-center radius levels and the ratio 2 + √5 are exact.

Numerical edge-length spreads were approximately 10⁻¹⁵. Regenerating the spheres after a generic rotation, translation, and reduction to the smallest original cube scale preserved the points and circle centers within approximately 3 × 10⁻¹⁶. These residuals describe arithmetic checks, not physical measurements.

The numerical template searches audit the output; they do not supply coordinates to the sphere generator. Counts of detected pentagonal circles apply to the declared reference-sphere point set. The symbolic check certifies those circles and solids; it does not claim a global census of every conceivable solid in all future nested systems.

## What this means for the ongoing search

There is now a verified constructive bridge from existing Centerstone cube nodes to both golden Platonic families using sphere intersections and circle centers. It gives substance to examining interior curved relationships and changing which generated objects are treated as references.

It does not establish that the unchanged 23-sphere source contained the complete solids, or that the earlier whole-circle nesting rule automatically generates this extension. The reference convention and the circle-center readout must remain explicit. Nothing here revises the separate Minimal Core nonembedding result or derives a physical growth mechanism.

The next bounded continuation would identify the cubes actually present in the generated point set and apply this same declared sphere operation to them, preserving shared points and construction histories. That would test recursive continuation without importing the coordinates of desired child solids.

## Files and reproduction

The packet contains this report and figure, the new operator definition, numerical results, exact symbolic coordinates and certificate, unchanged source geometry and nesting notes, and the scripts.

With Python, NumPy, SciPy, Matplotlib, and SymPy installed:

```sh
python run_cube_sphere_release.py
python exact_certificate.py
```

The first script generates and audits the new sphere geometry. The second checks the exact arithmetic. Existing original research files are inputs only. Credit for Subject963's nesting proposal and prior contributors, including Spedis where previously recorded, remains attached to their source material; this nine-sphere extension and its implementation are identified separately above.
