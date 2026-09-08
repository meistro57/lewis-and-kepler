# Subject 963 geometry — what's established, what's open

Credit: **Subject963** (construction) · **OpenAI Codex** (audits/export) · **Kepler** (rigor + interpretation) · **Lewis** (closed forms, renders, measurements).

## Candidate A (40 vertices)

Convex hull: **40 vertices, 60 edges, 22 faces** (8 triangles, 8 quads, 2 octagons, 4 dodecagons). Euler 40−60+22 = 2. Every vertex degree 3. Symmetry **D4h** (16 spatial syms; 8 proper rotations: identity, five 180°, two 90°). Vertex orbits 8/16/16.

Two coordinate families, with exact closed forms:

- 24-point family: signs + permutations of (a, b, b)
- 16-point family: signs of (c, c, b) and (c, b, c)

```
a = (12 − 2√3)/33 ≈ 0.258663587
b = (18 + 8√3)/33 ≈ 0.965345650
c = (6 + 10√3)/33 ≈ 0.706682063
```

The load-bearing relations: **a + b = c**, and **a², b², c² are in arithmetic progression** (b² − a² = c² − b²). Ratios b/a = 1+√3, c/a = 2+√3. Radius R_A = √((36+16√3)/33) ≈ 1.3894931812.

## The five 40-vertex shells

The same generator produces five 40-point radial shells. Squared radii:

```
(36−16√3)/33 ≈ 0.2511   ·   4/5   ·   4/3   ·   12/7   ·   (36+16√3)/33 ≈ 1.9307
```

Innermost and outermost are **√3-conjugates**; the middle three are rational fractions. Under sphere inversion (p → p/|p|²) the rational shells reciprocate and the conjugate shells map to 9/4 ∓ √3. The whole ladder is **inversion-closed**.

## Minimal Core v1.0 (128 vertices, 168 edges)

Seven families: S8=8, A12=12, A6=6, VF24=24, EF24=24, D6=6, VEF48=48. Five distinct radii (0.577, 0.707, 0.816, 0.894, 1.0); 80 points on the unit sphere.

## The containment question — resolved (negative)

**Candidate A does NOT nest inside the Minimal Core.** Distance-multiset test (invariant under rotation + translation, scale-free): only 8 of 780 of A's pairwise distances appear in the Core's 8,128. Structural reason: A is a single sphere (all 40 points at one radius); the Core is five concentric shells. A similarity maps a sphere to a sphere, and the only Core shell with ≥40 points (the 80-point unit shell) doesn't contain a rotated copy of A.

Reading (Kepler owns interpretation, Lewis flags): Candidate A = "equal standing / no king, no throne, no crown" (single shell). Minimal Core = a hierarchical throne with layered shells. Opposite structural philosophies; they don't nest despite a shared √3 lineage.

## Hidden-figure census (verified, matches ChatGPT exactly)

- **4 dodecagons**
- **8 regular hexagons** (each dodecagon = two 30°-offset hexagons)
- **42 squares** (of C(40,4) = 91,390 four-point subsets)
- **37 rectangular cuboids**

The 8 quadrilateral faces are rhombi (angles arccos(√6/4) ≈ 52.24° / 127.76°), not rectangles.

## Spike & bloom geometry (latest)

Two unit-sphere direction graphs from the recovered GLB:
- **native**: 362 vertices, 2,624 edges
- **G24_complete**: 626 vertices, 4,416 edges

native ⊆ G24_complete (strict, +264 points). G24 family sizes are all 48 (= full octahedral group order) — consistent with the octahedral-symmetric closure of a native 362-point seed. Open question for Kepler.

## Open threads

1. The √5/√7 derivation Codex couldn't identify from the collaborator's note (still unlocated).
2. Whether the spike/bloom G24 completion carries a *physical* mechanism, or is purely combinatorial.
3. The "no nesting" result invites the next question: if not containment, what *is* the relationship between Candidate A and the Minimal Core?
