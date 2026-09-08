#!/usr/bin/env python3
"""Independent verification of CUBE-RECURSION-002 key claims:
(1) 10 cubes in the 64-point set (9 at h=1, 1 at h=1/3)
(2) reconvergence: 9 inner cubes (h=1/3) share 32 vertices with the 1/3-parent's dodecahedral layer."""
import numpy as np
from itertools import combinations
from scipy.spatial import cKDTree
from collections import Counter, defaultdict

h = 1.0
corners = np.array([[x,y,z] for x in (-h,h) for y in (-h,h) for z in (-h,h)], dtype=float)
centers = np.vstack([corners, [[0.,0.,0.]]])
radii = np.array([2*h]*8 + [np.sqrt(3)*h])

def triple_intersection(c1, c2, c3, r1, r2, r3):
    p2 = c2 - c1; p3 = c3 - c1
    d = np.linalg.norm(p2)
    if d < 1e-12: return []
    ex = p2 / d
    i = np.dot(ex, p3)
    ey = p3 - i*ex; j = np.linalg.norm(ey)
    if j < 1e-12: return []
    ey = ey / j
    ez = np.cross(ex, ey)
    x = (r1*r1 - r2*r2 + d*d) / (2*d)
    y = (r1*r1 - r3*r3 + i*i + j*j - 2*i*x) / (2*j)
    h2 = r1*r1 - x*x - y*y
    if h2 < -1e-9: return []
    if abs(h2) < 1e-12: h2 = 0
    z = np.sqrt(max(0, h2))
    base = c1 + x*ex + y*ey
    if z == 0: return [base]
    return [base + z*ez, base - z*ez]

raw = []
for (i,j,k) in combinations(range(9), 3):
    raw.extend(triple_intersection(centers[i], centers[j], centers[k], radii[i], radii[j], radii[k]))
P = np.array(raw)
tree = cKDTree(P); seen = set(); unique = []
for i,p in enumerate(P):
    if i not in seen:
        unique.append(p); seen.update(tree.query_ball_point(p, 1e-7))
U = np.array(unique)
print(f"64-point set: {len(U)} points")

# --- cube detection: find 8-point sets forming a cube (3 mutually-perp equal edges) ---
def is_cube(pts, tol=1e-6):
    pts = np.array(pts)
    if len(pts) != 8: return False
    # centroid
    c = pts.mean(axis=0)
    # all vertices should be at radius r from centroid, and r = h*sqrt(3)
    rr = np.linalg.norm(pts - c, axis=1)
    if rr.max() - rr.min() > tol: return False
    # pick vertex 0, its 3 nearest neighbors = edges
    d = np.linalg.norm(pts[0] - pts, axis=1)
    order = np.argsort(d)
    e1, e2, e3 = pts[order[1]]-pts[0], pts[order[2]]-pts[0], pts[order[3]]-pts[0]
    # edges equal + mutually orthogonal
    l = [np.linalg.norm(e) for e in (e1,e2,e3)]
    if max(l)-min(l) > tol: return False
    if abs(np.dot(e1,e2))>tol or abs(np.dot(e1,e3))>tol or abs(np.dot(e2,e3))>tol: return False
    return l[0]  # half-edge length = l/2

# group U by rounding, search cubes via distance structure
# exhaustive: for each point, look for its 3 nearest equal neighbors forming orthonormal edges
cubes = set()
key_to_idx = {}
for idx, p in enumerate(U):
    key_to_idx.setdefault(tuple(np.round(p, 6)), idx)
keys = [tuple(np.round(p, 6)) for p in U]
keyset = set(keys)

found = 0
for idx0, p0 in enumerate(U):
    # candidate edge vectors: all vectors from p0 to others
    for i in range(len(U)):
        if i == idx0: continue
        e1 = U[i] - p0
        l1 = np.linalg.norm(e1)
        if l1 < 1e-6: continue
        for j in range(len(U)):
            if j == idx0 or j == i: continue
            e2 = U[j] - p0
            l2 = np.linalg.norm(e2)
            if abs(l1-l2) > 1e-6: continue
            if abs(np.dot(e1, e2)) > 1e-6: continue
            # third edge = cross(e1, e2) normalized to l1 (two signs)
            e3 = np.cross(e1, e2)
            e3 = e3 / np.linalg.norm(e3) * l1
            for s in (1, -1):
                e3s = s * e3
                # 8 vertices of cube
                verts = [p0, p0+e1, p0+e2, p0+e1+e2, p0+e3s, p0+e1+e3s, p0+e2+e3s, p0+e1+e2+e3s]
                ok = all(tuple(np.round(v,6)) in keyset for v in verts)
                if ok:
                    cubes.add(tuple(sorted(tuple(np.round(v,6)) for v in verts)))
                    found += 1

print(f"\ncubes detected: {len(cubes)} (claim 10)")
half_edges = Counter()
for c in cubes:
    c = np.array([list(v) for v in c])
    cc = c.mean(axis=0)
    d = np.linalg.norm(c[0]-c, axis=1)
    order = np.argsort(d)
    he = np.linalg.norm(c[order[1]]-c[0])/2
    half_edges[round(he,6)] += 1
print("cube half-edge lengths (h) -> count:")
for he, cnt in sorted(half_edges.items()):
    print(f"  h={he:.6f}: {cnt} cubes (claim 9 at h=1, 1 at h=1/3)")
