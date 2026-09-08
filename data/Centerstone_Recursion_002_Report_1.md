# Centerstone: independent verification and one recursive generation

**CUBE-RECURSION-002 · September 8, 2026**

**Research direction: Subject963. Independent implementation, computation, and this report: OpenAI Codex.** Here, “independent” means a separate implementation using different algorithms, written by the same assistant. It is not an external researcher's endorsement or a claim that the collaborator who requested verification has completed their own run.

## Results

The separate implementation reproduced the **48 regular pentagonal circles**, their **four exact regular icosahedra**, and the exact larger-to-smaller radius ratio **2 + √5 = φ³**.

We then found **10 cubes** in the generated geometry and applied the same nine-sphere operation once to each. Nine cubes have the original size, in different orientations; one has one-third the edge length. Every detected cube was verified with exact arithmetic. Adding the sphere centers or the 48 derived circle centers to the input did not introduce further parent cubes.

One complete generation produced **408 distinct sphere-intersection points**, **288 distinct circle centers**, **12 distinct dodecahedra**, and **24 distinct icosahedra** within the parent-generated families. The original points were retained, and duplicate construction histories were recorded rather than counted as separate geometry.

![Two recursive routes reaching the same points](Centerstone_Recursive_Paths.png)

The most useful new relationship is exact reconvergence: the inner cubes produced by the nine full-size parents collectively have the **same 32 vertices** as the dodecahedral reference layer produced by the one-third-size parent. Eight positions already existed; **24 are new**. The two routes have different connections and parent histories despite reaching the same point set.

## 1. How the circle-center layer was independently checked

The new code does not import the previous generator, previous circle-finding routine, or any Platonic-solid coordinate templates.

It starts with the declared cube-based construction at h = 1:

- Eight corner spheres, centers (±1, ±1, ±1), each radius 2.
- One central sphere, radius √3, through those corners.

For each triple of spheres, subtracting their equations gives linear constraints. The new implementation intersects that line with a sphere using exact arithmetic. It independently recovered all **64 distinct intersection points**: 80 sphere triples have two exact solutions each; four collinear triples are inconsistent.

Of these points, 32 lie on the central reference sphere. Instead of the preceding plane-first search, the new implementation examined **all 201,376 five-point subsets**. Candidates passed separate tests for:

1. Five equal short distances and five equal long distances.
2. Planarity and a connected five-edge cycle.
3. A circumcenter obtained from perpendicular-bisector equations.
4. Equal circumradii and equal angular spacing.

It recovered 48 circles. Their centers were then re-derived exactly from the circle vertices. Exact checks confirmed planarity, equal edges, equal circumradii, and the regular-pentagon diagonal-to-edge ratio.

For the icosahedra, the method grouped opposite center directions and checked all **1,848 six-axis subsets** across the two radius levels. Six opposite vertex pairs with the required equiangular relationships supplied each 12-vertex icosahedron. No icosahedron coordinates were inserted.

The exact squared radius levels are

    R_inner² = 1 − 2/√5,
    R_outer² = 1 + 2/√5.

Their positive radius ratio satisfies

    R_outer / R_inner = 2 + √5 = φ³.

The four recovered icosahedra comprise two orientations at each size. The outer ones come from dodecahedron face circles; the inner ones come from internal pentagonal circles. Ordinary face-center duality alone does not describe that entire four-object census.

Comparison with the preceding files occurred after generation. Maximum point and circle-center differences were below 9 × 10⁻¹⁶ in normalized units. The exact checks establish the identities; these floating-point residuals provide a separate consistency check.

## 2. Finding the parent cubes without importing their coordinates

The cube search treats every input point as a possible corner. It looks for three mutually perpendicular, equally long edge vectors to other input points, constructs the remaining four required corners by vector addition, and requires all eight corners to exist. Duplicate vertex sets are merged.

This procedure permits arbitrary centers, orientations, reflections, and sizes. It does not assume that a cube is centered at the origin.

| Input set | Points | Cubes detected |
|---|---:|---:|
| Sphere-intersection points | 64 | 10 |
| Intersections plus sphere centers | 65 | 10 |
| Both preceding types plus circle centers | 113 | 10 |

All ten detected cubes are centered at the origin in this input. Their half-edge lengths are **h = 1** for nine cubes and **h = 1/3** for one cube. The original seed cube is among the nine full-size parents; it is explicitly labeled as a replay.

Each candidate's edge lengths, orthogonality, center, and complete eight-point set were verified exactly. As a detection control, the algorithm recovered an added cube with h = 0.017 at a displaced center and generic orientation. Moving one of its corners caused that eight-point fixture to fail the cube test. Control points were not added to the research geometry.

The search is an exhaustive numerical candidate census with exact verification of every detected cube. It is not a separate interval-arithmetic proof that no floating-point prefilter could miss a candidate.

## 3. The recursive operation

Every parent present at the start of the generation was processed once. Children do not start another generation during this run.

For a detected cube with center o and half-edge h:

- Place radius-2h spheres at its eight actual vertices.
- Place a radius-√3h reference sphere at o.
- Solve that family's sphere intersections afresh.
- Detect regular pentagonal circles in its reference-sphere junctions and record their centers separately.

Each child's actual numerical intersections were then compared with an exact similarity image of the independently regenerated base geometry. The similarity image is a **post-generation verification and coordinate-identity check**, not an imported child target supplied to the generator. Every child's 64 junctions and 48 circle centers passed this check.

Exact coordinate expressions, including parent identities, were used to consolidate the results. Sphere identity also retains radius; coincident centers with different sphere radii are not merged.

| Output type | Construction occurrences across ten parents | Distinct geometry | New relative to the preceding generation |
|---|---:|---:|---:|
| Spheres | 90 | 42 | 33 |
| Sphere-intersection points | 640 | 408 | 344 |
| Circle centers | 480 | 288 | 240 |
| Dodecahedra produced by the families | 20 | 12 | 10 |
| Icosahedra produced by their circle centers | 40 | 24 | 20 |

The solid counts consolidate the objects recovered within each generated family. They are not a new exhaustive census of every solid that could use mixed points from different families.

All original 64 junctions and 48 circle centers remain present. The junction and circle-center coordinate sets are disjoint in this generation. There are therefore 696 distinct positions across those two readout types, plus the common sphere-center origin.

Among the 408 junctions, 64 belong to more than one parent: 40 initial positions and 24 new positions. Among the circle centers, 48 are shared by five parents each. A repeated coordinate is drawn once but retains all of its generating histories.

## 4. Two recursive routes meet exactly

The nine full-size parent cubes each generate an inner cube with half-edge 1/3. These nine inner cubes have **32 distinct corners** in their combined point set.

The one-third-size parent independently generates a 32-point dodecahedral compound on its reference sphere. Exact coordinate comparison gives:

**Union of inner-cube corners from nine full-size parents = reference-sphere junctions of the one-third-size parent = the original 32-point compound scaled by 1/3.**

| Shared positions | Already in the initial 64-point set? | Generating parents |
|---|---|---|
| 8 cube corners | Yes | Three full-size parents plus the smaller parent |
| 24 golden vertices | No | Two full-size parents plus the smaller parent |

The 24 newly shared golden vertices are reached through three parent histories each. Every individual correspondence is listed in `reconvergence_results.json`.

This is a relation between construction routes, not equality of their edge graphs. The left side of the figure reads the points as nine cubes; the right side reads them as two dodecahedra. No information-transfer rule or physical feedback process is inferred from the coordinate coincidence alone.

The smaller parent also generates a further cube with half-edge **1/9**, whose eight vertices were checked exactly. The declared operation therefore supports continued inward scaling. This run does not enumerate or generate the next complete generation.

## 5. Limits and the next useful test

This remains a **new declared cube-based construction**, not a discovery of golden solids in the unchanged 23-sphere registry. Its central reference passes through cube vertices; it is not the envelope around the complete corner balls. The earlier aligned-scale control used six forward scales and their reciprocals, giving eleven distinct scales.

All detected parents in this generation share the original center. Their largest generated junction radius remains 1 + √2 in the normalized units. The measured branching is in orientation and inward scale; displaced child centers and outward spatial expansion were not observed here.

The 42 distinct spheres form a larger combined arrangement, but this run applies the nine-sphere rule **within each parent family**. It does not enumerate new triple intersections involving spheres drawn from different families. That is a separate, well-defined next overlap test. Cross-family junctions should retain all contributing sphere and parent identities before any further cube search or recursive generation.

## Reproduce and inspect

The packet contains the independent implementation, complete numerical and exact-coordinate results, parent and sphere provenance, the shared-point trace, the figure, and preserved preceding material.

With Python, NumPy, SciPy, SymPy, and Matplotlib installed:

```sh
python run_recursion.py
python trace_reconvergence.py
python draw_reconvergence.py
```

`run_recursion.py` imports only the new `independent_geometry.py`. The preceding result file is used for an after-generation comparison, not to provide target shapes. The trace checks the 32-point identity exactly. The drawing uses the resulting coordinates and parent memberships.

Credit remains with Subject963 for the originating research direction and nesting proposal; earlier contributor credits remain attached to the preserved source report. This new implementation and its claims are attributed separately above.
