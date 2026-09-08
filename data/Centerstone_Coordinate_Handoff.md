# Centerstone coordinate handoff

Research and construction credit: **Subject963**. Coordinate export, symbolic reconstruction, and checks: **OpenAI Codex**, 2026-09-08. Existing source documents and their attributions are preserved in this separate packet.

This supplies the inputs for the proposed Candidate A / Minimal Core nesting test. It does **not** claim that an embedding has been found.

## Start here

**Centerstone_Coordinates.json** contains all three datasets, exact expressions, numeric coordinates, edge lists, scale conventions, and validation results. The ZIP also contains separate CSVs and the archived source material.

| Dataset | Points or circles | Edges | Coordinate convention |
|---|---:|---:|---|
| Minimal Core v1.0 | 128 vertices | 168 construction-incidence edges | Archived frame plus an exact cubic frame with enclosing sphere radius 1 |
| Candidate A | 40 vertices | 60 polygonal hull edges | Original generator-sphere units plus enclosing sphere radius 1 |
| Two scales meet | 37 radius-2 circles + 19 radius-3 circles | Not applicable | Planar, aligned, base radius 1, z = 0 |

The original Core point IDs 0–127 are retained in both frames. Candidate A IDs 0–39 follow the original storyboard audit and are a separate namespace. Every edge refers to IDs from its own dataset.

## The 128-point Minimal Core, exactly

For a compact description in the new cubic frame, define

\[
r=\frac{1}{\sqrt3},\qquad
u=\frac{3+\sqrt3}{6},\qquad
v=\frac{3-\sqrt3}{6}.
\]

In this table, take **all distinct coordinate permutations and all independent signs of nonzero entries**:

| Archived generator family | Representative coordinate | Count | Squared radius |
|---|---|---:|---|
| S8 | (r, r, r) | 8 | 1 |
| A12 | (0, r, r) | 12 | 2/3 |
| A6 | (r, 0, 0) | 6 | 1/3 |
| VF24 | (r, r/2, r/2) | 24 | 1/2 |
| EF24 | (2/√5, 1/√5, 0) | 24 | 1 |
| D6 | (2/√5, 0, 0) | 6 | 4/5 |
| VEF48 | (r, u, v) | 48 | 1 |

These seven disjoint families total **128 vertices**. They describe the coordinates; the included 168-edge table supplies the particular construction relationships. The seven generator-family names are retained from the archive and should not be confused with its eight historical V0–V7 orbit labels.

The archived point table uses tetrahedron side length 1, giving enclosing sphere radius

\[
R_{\rm archive}=\frac{\sqrt6}{4}.
\]

For row-vector coordinates, the exact cubic-frame export uses

\[
p_{\rm unit}=\frac{p_{\rm archive}B}{R_{\rm archive}},\qquad
B=
\begin{pmatrix}
0&\sqrt2/2&\sqrt2/2\\
\sqrt6/3&-\sqrt6/6&\sqrt6/6\\
\sqrt3/3&\sqrt3/3&-\sqrt3/3
\end{pmatrix}.
\]

Here \(B^\mathsf{T}B=I\) and \(\det B=1\). The source points are already centered. This applies one rotation and one uniform scale to the whole object. **Interior vertices retain their distinct radii**; they are not individually projected onto the unit sphere.

Use **minimal_core_vertices_exact.csv** for the exact cubic coordinates and **minimal_core_edges.csv** for the edges. The original decimal CSVs, generator, and manifest remain unmodified in **minimal_core_archive/**.

## Candidate A comparison coordinates

In its original generator-sphere units:

\[
a=\frac{12-2\sqrt3}{33},\quad
b=\frac{18+8\sqrt3}{33},\quad
c=\frac{6+10\sqrt3}{33}.
\]

Its 24-point family comprises all independent signs and distinct permutations of \((a,b,b)\). Its 16-point family comprises all independent signs of **only** \((c,c,b)\) and \((c,b,c)\); do not add the third permutation \((b,c,c)\).

All 40 points lie on the sphere

\[
R_A^2=2b=\frac{36+16\sqrt3}{33},\qquad
R_A\approx1.3894931812.
\]

The normalized copy divides every coordinate by \(R_A\). Both copies preserve the original point order. **candidate_a_vertices_exact.csv** contains both scales; **candidate_a_edges.csv** contains the 60 hull edges. **candidate_a_source.json** preserves the earlier audit output.

## The “two scales meet” circle layout

This is the earlier planar nested-circle test, with both systems centered at the origin and relative rotation initially zero. For integer axial coordinates \((q,s)\),

\[
(x,y)=\left(a(q+s/2),\,\frac{a\sqrt3\,s}{2}\right),\qquad
\max(|q|,|s|,|q+s|)\le k.
\]

- System A: \(a=2,\ k=3\), giving **37 circles of radius 2**.
- System B: \(a=3,\ k=2\), giving **19 circles of radius 3**.

The exact seven shared centers are

\[
(0,0),\quad (\pm6,0),\quad (\pm3,\pm3\sqrt3),
\]

with independent signs in the final pair. All have \(z=0\).

Both sets of centers extend to radius 6. Including the circles themselves, their outer extents are **8 and 9**, respectively. These are overlapping-circle arrangements: nearest-center spacing equals the circle radius, not the diameter. Two circles sharing a center remain distinct because their radii differ.

To test perspective-independent relative orientation, hold A fixed and rotate every B center by the same planar rotation matrix about the origin. Keep both circle radii unchanged. The archived checks give seven shared centers at 0° and 60°, and one at each of the sampled 0.1°, 1°, 15°, 30°, and 45° orientations. Those samples are not an exhaustive classification of all angles.

The two CSVs **two_scales_meet_circles_0deg.csv** and **two_scales_meet_shared_centers.csv** supply the circle IDs, centers, radii, and shared-center pairs. **nesting_archive/** contains the original exploration and generator. This dataset is planar; it does not silently promote circles to a particular 3D sphere construction.

## Define the nesting question before searching

For native-vertex inclusion, seek one similarity

\[
sQp_i+t=P_{f(i)},\qquad s>0,\quad Q^\mathsf{T}Q=I,
\]

where \(f\) is injective, \(p_i\) are Candidate A vertices, and \(P_j\) are Minimal Core vertices. Include both rotations and reflections, or report them separately. The axis choices in these exports are coordinate conventions; they should not restrict the search.

Two points for interpreting the result:

1. **Equal enclosing radii are a convenient starting comparison, not an exhaustive nesting search.** A subset of the Core may have a different center or radius, so translation and global scale must remain available.
2. **Point inclusion and edge preservation are separate questions.** The Core's 168 edges record construction incidence; Candidate A's 60 edges are hull edges. If a proposed embedding also requires each Candidate A edge to be a native Core edge, check that explicitly. Allowing paths along several edges, or introducing new intersection points, defines a different test and should be reported as such.

Perspective can reveal alignments in a drawing, but the 3D test must use coordinates and incidence. A projected crossing alone is not a new native vertex.

## Verification and provenance

The recovered archived tables match the hashes recorded in the included **CENTERSTONE_MINIMAL_CORE_V1_CERTIFICATE.md** and generator manifest:

- Points SHA-256: 8fce875d6a7587834fb72bc5faf50173ec36e6971fbc09f5e8cb303a882e098c
- Edges SHA-256: c65cf7384c9c0ca882426b8a0d3250a850094b12a9776770f385a729a5d88985

The new symbolic construction matched all 128 archived vertices bijectively after the stated frame conversion, with maximum numerical residual **7.9 × 10⁻¹⁶**, and reproduced the same 168 edges. The graph has seven connected components of sizes 98, 5, 5, 5, 5, 5, 5 and cycle rank 47. Candidate A's exact coordinate expressions agree with its saved table within **5.6 × 10⁻¹⁶**. The circle export agrees with the archived nesting generator; the seven aligned shared centers were checked symbolically.

These checks validate the coordinate handoff. The historical certificate's separate comparison against the Experiment-052 ledgers is included as an archived result; that held-out comparison was not rerun here. Nor was the collaborator's hidden-figure census rerun for this export.

The related **CENTERSTONE_056A_R7_REPORT.md** is included for source context. These files document the recovered Minimal Core construction, not experimental proof of a physical theory.

To reproduce the exports and checks, install Python 3 with numpy and sympy, then run from the extracted packet:

~~~sh
python build_coordinate_packet.py
~~~

The script reads the included archived files and rebuilds the derived CSVs and JSON. Detailed results are in **validation.json**.

The specific pending **√5/√7 derivation** mentioned in the collaborator's note could not be identified from that note. The √5 in the Core's EF24 coordinates follows from normalizing a vector with component ratio 2:1:0; this does not establish the unspecified √5/√7 connection. That derivation remains open.
