# Centerstone: cross-family sphere intersections

**Experiment CROSS-FAMILY-003 · Additive continuation of CUBE-RECURSION-002**

Research origin, direction, and attribution: **Subject963**. Computation, exact-arithmetic implementation, verification, and report: **Codex**. The external verifier quoted by Subject963 is not identified in this turn; their reported verification remains a separate contribution. Earlier contributions, including Spedis where previously recorded, retain their source attribution in the preserved earlier reports; no new result here is assigned to Spedis without a source. No external person's endorsement is claimed for this computation.

## Result

Allowing the **42 already generated spheres** to intersect across parent families produces two specific connections:

1. **48 previously derived pentagonal-circle centers are recovered as sphere-intersection points.** They cover all vertices of **four of the 24 previously catalogued regular icosahedra**. Their regularity is rechecked directly on the sphere-generated coordinates. This is a change in geometric role: these positions can now be reached by intersecting spheres, without first computing the pentagonal-circle centers.
2. **Eight triples share an entire circle.** The centers of those circles are the eight corners of the **one-ninth-size cube already present** in the preceding recursive generation. The cube is not a new discovery; its role as the center set of these triple-shared circles is new in this audit.

The result is a geometric incidence connection. It does not establish graph equality, signal propagation, an efficiency advantage, or a physical mechanism.

![Cross-family connections](Centerstone_Cross_Family_Connections.png)

## Frozen inputs and scope

The input is the exact 42-sphere registry from CUBE-RECURSION-002, copied unchanged into `source_recursion_results.json`. Its SHA-256 is recorded in the output. These spheres came from nine full-size cube parents and one one-third-size parent. All ten parents were centered at the origin.

This operation is **one closure under triple intersection of that fixed sphere set**. It adds no spheres and does not launch another recursive generation. No Platonic-solid coordinate templates are used to generate points. Previously catalogued icosahedra are consulted only after the intersections have been generated, to identify recovered vertex sets.

Some spheres belong to multiple parents. A triple is called **strictly cross-family** only when the intersection of the three spheres' parent-membership sets is empty: no single parent contains all three. Relabeling a previously evaluated triple cannot make it new.

The original 23-sphere registry, Candidate A, the Minimal Core, and the declared nine-sphere construction remain distinct. This result concerns the last construction and its first recursive generation. It makes no retroactive containment claim about the original source.

## Complete triple census

All \(\binom{42}{3}=11,480\) distinct sphere triples were evaluated.

| Triple outcome | Within at least one parent | Strictly cross-family | Total |
|---|---:|---:|---:|
| Two real intersection points | 800 | 8,992 | 9,792 |
| Empty intersection, independent radical planes | 0 | 1,560 | 1,560 |
| Empty intersection, degenerate radical-plane system | 20 | 100 | 120 |
| Entire shared circle | 0 | 8 | 8 |
| **All triples** | **820** | **10,660** | **11,480** |

There are no tangent one-point triples and no coincident-sphere triples in this registry. Degenerate triples are explicitly classified rather than silently skipped.

The 9,792 two-point triples produce 19,584 point occurrences, which deduplicate to **8,566 distinct coordinates** by exact algebraic equality.

| Point accounting | Count |
|---|---:|
| Previously recorded junctions retained | 408 |
| Additional junction coordinates | 8,158 |
| Of those, coordinates already known as circle centers | 48 |
| Coordinates new relative to both preceding junction and circle-center records | **8,110** |
| Previously known circle centers still absent from the junction set | 240 |

Thus **“8,158 new junctions” does not mean 8,158 entirely new positions**: 48 positions have acquired a new role. Of the 408 earlier junctions, 64 also have cross-family generating triples. Every additional junction has at least one strictly cross-family generator.

The point count is not a count of the whole triple-intersection union. Eight triples contribute continuous circles with infinitely many points. **80 of the 8,566 finite-solution points lie on those circles**, leaving **8,486 isolated points plus the eight circles** as the complete union. Each circle contains 15 of the explicitly recorded finite-solution points; the circles share some of those points, so 8 × 15 is not a distinct-point count.

## The circle-center → junction → icosahedron connection

The previous run independently verified the 48 pentagonal circles and four icosahedra in the normalized seed's circle-center layer. Across all ten parent families it recorded 288 distinct circle centers and 24 distinct icosahedral vertex sets.

This new operation recovers 48 of those 288 circle centers as junctions. The four fully recovered catalogued icosahedra have prior list indices **0, 2, 7, and 9** (zero-based). These are not simply all four seed-layer objects; the selected sets come from the combined recursive catalogue. The 48 recovered positions are the disjoint union of these four 12-vertex sets.

Two recovered sets lie at each squared circumradius:

\[
R_-^2=1-\frac{2\sqrt5}{5},\qquad
R_+^2=1+\frac{2\sqrt5}{5}.
\]

Consequently their radius ratio remains

\[
\frac{R_+}{R_-}=2+\sqrt5=\varphi^3,
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

For each recovered set, the audit verifies equal circumradii, 30 equal shortest-distance edges, degree five at all 12 vertices, 20 triangular faces, and the exact regular-icosahedron invariant

\[
\frac{R^2}{e^2}=\frac{10+2\sqrt5}{16}.
\]

Those edges describe the regular geometric figures. The operation itself supplies sphere incidences; it does not install those edges as a communication network.

An explicit recovered coordinate is

\[
p=\left(\frac{5-\sqrt5}{10},\;0,\;\frac{3\sqrt5-5}{10}\right).
\]

It is produced by the triple S001, S002, S010, each of radius 2, whose centers are

\[
\begin{aligned}
c_1&=\left(-\frac{1+\sqrt5}{2},\frac{1-\sqrt5}{2},0\right),\\
c_2&=(-1,1,-1),\\
c_3&=\left(\frac{1-\sqrt5}{2},0,-\frac{1+\sqrt5}{2}\right).
\end{aligned}
\]

Exact substitution gives \(\|p-c_i\|^2=4\) for all three. This is output point X00305 and prior circle center R0012. Its sphere provenance is preserved alongside the earlier role.

This is a recovery test against 24 known objects, **not an exhaustive search for every icosahedron, dodecahedron, or cube in the larger 8,566-point set**.

## Why eight entire circles appear

The shared curves have a short exact derivation. Let

\[
s=(\pm1,\pm1,\pm1).
\]

For each of the eight choices, the registry contains these three spheres:

| Center | Radius | Role |
|---|---:|---|
| \(-s\) | \(2\) | Full-size corner sphere |
| \(0\) | \(1/\sqrt3\) | One-third-size parent's reference sphere |
| \(s/3\) | \(2/3\) | One-third-size corner sphere |

On the reference sphere, \(\|x\|^2=1/3\). Substitution into either of the other sphere equations gives the **same plane**:

\[
s\cdot x=\frac13.
\]

Their common set is therefore the circle

\[
\boxed{\|x\|^2=\frac13,\qquad s\cdot x=\frac13.}
\]

Its center and radius are

\[
c_s=\frac{s}{9},\qquad
r^2=\frac13-\frac1{27}=\frac8{27},\qquad
r=\frac{2\sqrt6}{9}.
\]

The eight centers \((\pm1/9,\pm1/9,\pm1/9)\) form the already verified cube of half-edge \(1/9\). Each has an existing junction ID recorded in the verification file.

Each circle already existed as a **pairwise intersection inside the small parent family**. The newly established fact is that a large sphere from outside that family contains the same entire curve. This is an incidence relationship across scales, rather than a newly invented curve or an arbitrary sample of its points.

## Orientation and scale contributions

Of the strictly cross-family triples, 5,940 mix large and small spheres; 4,720 use only the large-scale families. The additional junctions separate as follows:

| Generating triples | Additional junction coordinates |
|---|---:|
| Different orientations, all at the large scale | 3,622 |
| Large and small scales together | 4,536 |
| Additional junctions reached by both categories | 0 |

This category split concerns new junction coordinates only. It does not deny that previously recorded points can be reached in multiple ways. The eight continuous circles belong to the mixed-scale category.

The largest radius among the finite-solution points increases from approximately **2.41421356 to 3.52014702**, while the 42 sphere surfaces themselves remain fixed. These new outer junctions were already within the spheres' geometric extent; their appearance does not represent physical expansion or additional recursive growth.

## Verification and reproducibility

The source sphere centers and squared radii lie in \(\mathbb Q(\sqrt5)\). `exact_field.py` implements that field with rational pairs \(a+b\sqrt5\), using Python `Fraction` values. Sphere subtraction yields radical planes. Their exact intersection with a sphere is classified by rank, consistency, and discriminant sign.

Points are stored in the exact form \(u+v\sqrt d\), where all components of \(u,v\) and \(d\) lie in \(\mathbb Q(\sqrt5)\). Square roots already in that field are collapsed. For the remaining quadratic extensions, equality is tested through equal field parts, proportional radical vectors, exact squared equality, and sign. Numerical proximity only locates possible duplicates; it does not authorize merging.

Every generated finite point passes exact substitution in all three generating sphere equations. Every shared circle passes an exact whole-curve certificate. An independent floating-point SVD/pseudoinverse implementation agrees with **all 11,480 classifications** and all finite-triple solution sets. This is a second algorithm within the same assistant's work, not third-party validation.

Numerical diagnostics:

- Maximum point discrepancy against the SVD implementation: approximately \(3.46\times10^{-14}\).
- Minimum separation between distinct finite-solution points: approximately \(9.3243\times10^{-4}\).
- Maximum sphere-equation residual under independent 70-digit evaluation: approximately \(1.30\times10^{-68}\).
- Degeneracy controls cover an entire shared circle, a tangent point, and an empty intersection.

Run with Python and NumPy, SciPy, SymPy, mpmath, and Matplotlib installed:

```bash
python run_cross_family.py
python verify_and_trace.py
python draw_results.py
```

The packet includes the unchanged previous result file, all new scripts, both result files, this report, the figure, and a file manifest. Exact point expressions, generating triples, sphere IDs, parent memberships, and previous-role IDs remain available for an external audit.

## What this closes—and what remains open

**Closed for this declared input:** the omitted cross-family triple enumeration; recovery of four known icosahedral vertex sets as direct sphere junctions; and the eight exact circles connecting large and small families through the existing inner cube.

**Still open:** a complete mixed-family solid census, the selection of graph edges or curved paths for a dynamical model, and evidence that such a model improves any specified task. A natural next question is to compare the already known straight-edge graphs with the newly documented shared-circle incidences under a declared propagation rule. This report introduces no such rule and records no dynamics result.
