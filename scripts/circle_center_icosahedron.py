#!/usr/bin/env python3
"""Independent audit: circle-center -> icosahedron layer (CUBE-SPHERE-001 / RECURSION-002).
Find all regular pentagonal circles among the 32 central-reference-sphere points,
compute their centers, and verify they form 4 regular icosahedra (2 sizes x 2 orientations),
with radius ratio R_outer/R_inner = 2 + sqrt(5) = phi^3."""
import numpy as np
from itertools import combinations
from collections import Counter, defaultdict
from scipy.spatial import ConvexHull

# ---- regenerate the 64-point set (cube corners + central sphere) ----
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

from scipy.spatial import cKDTree
raw = []
for (i,j,k) in combinations(range(9), 3):
    raw.extend(triple_intersection(centers[i], centers[j], centers[k], radii[i], radii[j], radii[k]))
P = np.array(raw)
tree = cKDTree(P); seen = set(); unique = []
for i,p in enumerate(P):
    if i not in seen:
        unique.append(p); seen.update(tree.query_ball_point(p, 1e-7))
U = np.array(unique)

# 32 points on the central reference sphere (radius sqrt(3))
rt3 = np.array([p for p in U if abs(np.linalg.norm(p)-np.sqrt(3)) < 1e-6])
print(f"central reference sphere (r=sqrt3): {len(rt3)} points (claim 32)")

# ---- find regular pentagons: 5 coplanar, equally-spaced-on-circle points ----
def is_regular_pentagon(idx, tol=1e-6):
    p = rt3[list(idx)]
    c = p.mean(axis=0)
    # coplanarity: singular value 3 ~ 0
    _, s, _ = np.linalg.svd(p - c)
    if s[2] > tol * s[0]:
        return False
    # equal radius from centroid
    r = np.linalg.norm(p - c, axis=1)
    if r.max() - r.min() > tol:
        return False
    # equal angular spacing of 72 deg around centroid
    n = np.cross(p[1]-p[0], p[2]-p[0])
    nn = np.linalg.norm(n)
    if nn < 1e-12: return False
    n = n / nn
    e1 = p[0] - c; e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(n, e1); e2 = e2 / np.linalg.norm(e2)
    ang = np.sort(np.arctan2((p-c)@e2, (p-c)@e1))
    gaps = np.diff(np.concatenate([ang, ang[:1]+2*np.pi]))
    target = 2*np.pi/5
    if np.max(np.abs(gaps - target)) > tol:
        return False
    return True

pentagons = []
for idx in combinations(range(len(rt3)), 5):
    if is_regular_pentagon(idx):
        pentagons.append(idx)
print(f"regular pentagonal circles found: {len(pentagons)} (claim 48)")

# centers
centers48 = []
for idx in pentagons:
    p = rt3[list(idx)]
    centers48.append(p.mean(axis=0))
centers48 = np.array(centers48)
# dedupe centers (distinct)
ckey = set()
unique_centers = []
for c in centers48:
    k = tuple(np.round(c, 6))
    if k not in ckey:
        ckey.add(k); unique_centers.append(c)
unique_centers = np.array(unique_centers)
print(f"distinct circle centers: {len(unique_centers)} (claim 48)")

# radius levels
rc = np.round(np.linalg.norm(unique_centers, axis=1), 6)
levels = Counter(rc)
print("\n=== circle-center radius levels ===")
for r in sorted(levels):
    print(f"  {r:.6f}: {levels[r]} centers")

# claimed: R_inner^2 = 1 - 2/sqrt5, R_outer^2 = 1 + 2/sqrt5
phi = (1+np.sqrt(5))/2
rinner = np.sqrt(1 - 2/np.sqrt(5))
router = np.sqrt(1 + 2/np.sqrt(5))
print(f"\nclaimed R_inner = {rinner:.9f}, R_outer = {router:.9f}")
print(f"claimed ratio R_outer/R_inner = {router/rinner:.10f} = 2+sqrt5 = {2+np.sqrt(5):.10f}")
if len(levels) == 2:
    r_vals = sorted(levels)
    print(f"measured ratio = {r_vals[1]/r_vals[0]:.10f}")

# verify the centers form regular icosahedra: at each level, 24 centers = 2 icosahedra (12 each)
print("\n=== icosahedron verification ===")
for r in sorted(levels):
    pts = np.array([c for c in unique_centers if abs(np.linalg.norm(c)-r) < 1e-5])
    # group into 2 orientation-clusters of 12: use min-distance connectivity
    # a regular icosahedron has 12 vertices, each with 5 nearest neighbors at equal (edge) distance
    # detect via: compute all pairwise distances, find the min (edge length)
    d = np.linalg.norm(pts[:,None,:] - pts[None,:,:], axis=2)
    np.fill_diagonal(d, np.inf)
    edge = d.min()
    # build adjacency at edge distance
    adj = d < edge*1.1
    # connected components of size 12 -> one icosahedron each
    from collections import deque
    visited = set(); comps = []
    for i in range(len(pts)):
        if i in visited: continue
        q = deque([i]); comp = []
        while q:
            u = q.popleft()
            if u in visited: continue
            visited.add(u); comp.append(u)
            for v in range(len(pts)):
                if adj[u,v] and v not in visited:
                    q.append(v)
        comps.append(comp)
    sizes = [len(c) for c in comps if len(c) > 1]
    print(f"  level r={r:.6f}: {len(pts)} centers -> components {sorted(sizes, reverse=True)} (expect [12, 12])")
    # regularity: edges all equal, faces triangular
    for comp in comps:
        if len(comp) == 12:
            sub = pts[comp]
            hull = ConvexHull(sub)
            faces = {}
            for simplex, eq in zip(hull.simplices, hull.equations):
                faces.setdefault(tuple(np.round(eq,8)), set()).update(map(int, simplex))
            sizes_f = Counter(len(f) for f in faces.values())
            # edge length spread
            el = set()
            for f in faces.values():
                ids = list(f)
                for a in range(len(ids)):
                    for b in range(a+1,len(ids)):
                        el.add(round(np.linalg.norm(sub[ids[a]]-sub[ids[b]]), 6))
            print(f"    icosahedron: faces {dict(sorted(sizes_f.items()))} (expect {{3:20}}), distinct edge lengths {len(el)} (expect 1)")
