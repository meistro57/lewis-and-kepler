#!/usr/bin/env python3
"""Independent verification: cube (8) + 12 golden-ratio vertices = regular dodecahedron;
its 12 face centers = regular icosahedron. Standard classical construction, verified from scratch."""
import numpy as np
from itertools import combinations, product
from collections import Counter
from sympy import sqrt, Rational

phi = (1 + sqrt(5)) / 2
invphi = 1 / phi

# Cube: (±1, ±1, ±1)
cube = np.array([[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], dtype=float)
print(f"cube vertices: {len(cube)}")

# The 12 golden-ratio vertices: cyclic permutations of (0, ±1/φ, ±φ)
golden = []
for (u, v, w) in [(0, invphi, phi), (invphi, phi, 0), (phi, 0, invphi)]:
    for su in (-1, 1):
        for sv in (-1, 1):
            golden.append([su*u, sv*v, w])
golden = np.array(golden)
print(f"golden additions: {len(golden)} (expect 12)")

dode = np.vstack([cube, golden])
print(f"dodecahedron vertices: {len(dode)} (expect 20)")

# all on a sphere?
r = np.linalg.norm(dode, axis=1)
print(f"all on sphere radius sqrt(3)={float(sqrt(3)):.10f}: {np.allclose(r, r[0])}")

# regularity: unique edge length via convex hull
from scipy.spatial import ConvexHull
hull = ConvexHull(dode)
faces = {}
for simplex, eq in zip(hull.simplices, hull.equations):
    faces.setdefault(tuple(np.round(eq, 8)), set()).update(map(int, simplex))
print(f"faces: {len(faces)} (expect 12 pentagons)")
print(f"face sizes: {dict(sorted(Counter(len(f) for f in faces.values()).items()))} (expect {{5: 12}})")

# edge lengths (from the 12 pentagonal faces)
edge_lens = set()
for f in faces.values():
    ids = list(f)
    p = dode[ids]
    # order around face and collect consecutive distances
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            edge_lens.add(round(np.linalg.norm(dode[ids[i]]-dode[ids[j]]), 8))
print(f"distinct pairwise distances within faces: {len(edge_lens)} (expect 1 = regular)")

# exact edge length: distance from (1,1,1) to (0, 1/phi, phi)
e2 = (1-0)**2 + (1-float(invphi))**2 + (1-float(phi))**2
print(f"edge length^2 = {e2:.10f}  exact = {simplify((1)**2 + (1-1/phi)**2 + (1-phi)**2)}")

# face centers -> icosahedron
centers = np.array([dode[list(f)].mean(axis=0) for f in faces.values()])
print(f"\nface centers: {len(centers)} (expect 12 = icosahedron vertices)")
rc = np.linalg.norm(centers, axis=1)
print(f"centers on one sphere: {np.allclose(rc, rc[0])}  radius {rc[0]:.10f}")
# regularity of icosahedron: convex hull of centers, count triangular faces
ch = ConvexHull(centers)
cfaces = {}
for simplex, eq in zip(ch.simplices, ch.equations):
    cfaces.setdefault(tuple(np.round(eq, 8)), set()).update(map(int, simplex))
print(f"icosahedron faces: {len(cfaces)} (expect 20 triangles)")
print(f"icosahedron face sizes: {dict(sorted(Counter(len(f) for f in cfaces.values()).items()))} (expect {{3: 20}})")
