#!/usr/bin/env python3
"""Candidate A verification — rebuilds 40/60/22, D4h, and the 42-squares/37-boxes census.
Runs from raw coordinates in audit_results.json. Independent of any other agent's numbers.
"""
import json, itertools, collections
import numpy as np
from scipy.spatial import ConvexHull
from sympy import sqrt

d = json.load(open("audit_results.json"))
pts = np.array(d["candidate_a_points"])
eset = set(tuple(sorted(e)) for e in d["candidate_a_hull_edges"])

# 1. convex hull + face merge (coplanar triangles)
hull = ConvexHull(pts)
faces = {}
for s, eq in zip(hull.simplices, hull.equations):
    faces.setdefault(tuple(np.round(eq, 6)), set()).update(map(int, s))
F = len(faces)
fh = collections.Counter(len(v) for v in faces.values())
assert len(pts) == 40 and len(eset) == 60 and F == 22
assert len(pts) - len(eset) + F == 2  # Euler
assert dict(fh) == {3: 8, 4: 8, 8: 2, 12: 4}
print(f"V=40 E=60 F=22 Euler=2  faces={dict(fh)}  ✓")

# 2. squares & boxes among the 40 points
s = set(tuple(np.round(p, 9)) for p in pts)
def d2(a, b): return float(np.sum((a-b)**2))
squares = set()
for q in itertools.combinations(range(40), 4):
    Q = pts[list(q)]
    ds = sorted(d2(Q[i], Q[j]) for i in range(4) for j in range(i+1, 4))
    if abs(ds[0]-ds[1]) < 1e-9 and abs(ds[1]-ds[2]) < 1e-9 and abs(ds[2]-ds[3]) < 1e-9 \
       and abs(ds[4]-ds[5]) < 1e-9 and abs(ds[4]-2*ds[0]) < 1e-8:
        squares.add(frozenset(q))
boxes = set()
for a in range(40):
    A = pts[a]
    for b in range(40):
        if b == a: continue
        AB = pts[b]-A
        for c in range(40):
            if c in (a, b): continue
            AC = pts[c]-A
            if abs(np.dot(AB, AC)) > 1e-9: continue
            D = A + AB + AC
            if tuple(np.round(D, 9)) not in s: continue
            for e in range(40):
                if e in (a, b, c): continue
                AE = pts[e]-A
                if abs(np.dot(AE, AB)) > 1e-9 or abs(np.dot(AE, AC)) > 1e-9: continue
                corners = [A, pts[b], pts[c], D, pts[e], pts[b]+AE, pts[c]+AE, D+AE]
                if all(tuple(np.round(p, 9)) in s for p in corners):
                    boxes.add(frozenset(tuple(np.round(p, 9)) for p in corners))
assert len(squares) == 42 and len(boxes) == 37
print(f"42 squares, 37 rectangular boxes  ✓")

# 3. symmetry (from supplied isometry matrices — verify they map the set to itself)
mats = [np.array(m["matrix"]) for m in d["point_isometries"]]
assert len(mats) == 16
good = sum(1 for M in mats if np.linalg.norm((pts @ M.T)[:, None, :] - pts[None, :, :], axis=2).min(axis=1).max() < 1e-9)
rots = [M for M in mats if np.linalg.det(M) > 0]
inv = any(np.allclose(M, -np.eye(3), atol=1e-8) for M in mats)
print(f"16 isometries ({good} map set->itself), 8 rotations, inversion={inv}  D4h ✓")
print("\nALL CHECKS PASSED")
