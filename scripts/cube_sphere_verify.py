#!/usr/bin/env python3
"""Independent verification of CUBE-SPHERE-001: nine spheres -> golden vertices.
Claim: 8 corner spheres (radius 2h) + 1 central reference sphere (radius sqrt(3)h)
       intersect to produce 64 distinct points on 5 radial shells,
       including 24 golden vertices that complete two dodecahedra sharing the cube."""
import numpy as np
from itertools import combinations
from collections import Counter, defaultdict
from scipy.spatial import cKDTree
from sympy import sqrt, Rational, simplify

h = 1.0
# 8 cube corners
corners = np.array([[x,y,z] for x in (-h,h) for y in (-h,h) for z in (-h,h)], dtype=float)
# 9 sphere centers: 8 corners + origin
centers = np.vstack([corners, [[0.,0.,0.]]])
# radii: 2h for corners, sqrt(3)h for central
radii = np.array([2*h]*8 + [np.sqrt(3)*h])

# triple sphere intersection: solve for points at given distance from 3 sphere centers
def triple_intersection(c1, c2, c3, r1, r2, r3):
    # points P with |P-c1|=r1, |P-c2|=r2, |P-c3|=r3
    # translate c1 to origin
    p2 = c2 - c1; p3 = c3 - c1
    d = np.linalg.norm(p2)
    ex = p2 / d
    i = np.dot(ex, p3)
    ey = (p3 - i*ex); j = np.linalg.norm(ey)
    if j < 1e-12: return []  # collinear
    ey = ey / j
    ez = np.cross(ex, ey)
    x = (r1*r1 - r2*r2 + d*d) / (2*d)
    y = (r1*r1 - r3*r3 + i*i + j*j - 2*i*x) / (2*j)
    h2 = r1*r1 - x*x - y*y
    if h2 < -1e-9: return []
    if abs(h2) < 1e-12: h2 = 0
    z = np.sqrt(max(0, h2))
    base = c1 + x*ex + y*ey
    if z == 0:
        return [base]
    return [base + z*ez, base - z*ez]

raw = []
for (i,j,k) in combinations(range(9), 3):
    pts = triple_intersection(centers[i], centers[j], centers[k], radii[i], radii[j], radii[k])
    raw.extend(pts)
print(f"raw triple-intersection records: {len(raw)} (claim 160)")

# dedupe
P = np.array(raw)
tree = cKDTree(P)
seen = set(); unique = []
for i,p in enumerate(P):
    if i not in seen:
        unique.append(p)
        seen.update(tree.query_ball_point(p, 1e-7))
U = np.array(unique)
print(f"distinct points: {len(U)} (claim 64)")

# radial shells
rad = np.round(np.linalg.norm(U, axis=1), 8)
shells = Counter(rad)
print(f"\n=== radial shells (r/h -> count) ===")
for r in sorted(shells):
    print(f"  {r:.8f}: {shells[r]} points")

# map to claimed values
expected = {np.sqrt(2)-1: 6, 1/np.sqrt(3): 8, 1.0: 12, np.sqrt(3): 32, np.sqrt(2)+1: 6}
print(f"\nclaim: sqrt2-1:6, 1/sqrt3:8, 1:12, sqrt3:32, sqrt2+1:6")
for r in sorted(shells):
    near = [k for k in expected if abs(k-r) < 1e-6]
    tag = f"  <- {'/'.join(str(k) for k in near)} (expect {expected[near[0]] if near else '?'})"
    print(f"  {r:.8f}: {shells[r]}{tag}")

# check golden vertices: among the sqrt(3) shell (32 points), are there (0, ±1/φ, ±φ) type?
phi = (1+np.sqrt(5))/2
rt3 = np.array([p for p in U if abs(np.linalg.norm(p)-np.sqrt(3)) < 1e-6])
print(f"\nsqrt(3) shell points: {len(rt3)} (claim 32)")
# check the 8 cube corners are among them
cube_keys = set(map(tuple, np.round(corners, 6)))
rt3_keys = set(map(tuple, np.round(rt3, 6)))
print("8 cube corners present in sqrt3 shell:", cube_keys <= rt3_keys)
# golden vertices present?
golden_test = []
for (a,b,c) in [(0.0, 1/phi, phi), (1/phi, phi, 0.0), (phi, 0.0, 1/phi)]:
    nz = [i for i in range(3) if abs(a)+abs(b)+abs(c)>0 and [a,b,c][i]!=0]
    # simpler: just check exact golden triples via rounding
golden_pts = 0
for p in rt3:
    ap = np.sort(np.abs(p))
    if abs(ap[2]-phi)<1e-5 and abs(ap[1]-1/phi)<1e-5 and abs(ap[0])<1e-5:
        golden_pts += 1
print(f"golden-ratio vertices (0, 1/phi, phi) form in sqrt3 shell: {golden_pts} (claim 24)")

# verify the ratio R_outer/R_inner = 2+sqrt5 = phi^3
print(f"\nphi^3 = {phi**3:.10f}  = 2+sqrt5 = {2+np.sqrt(5):.10f}")
