#!/usr/bin/env python3
"""Lewis independent cube census — Recursion_002 "10 cubes" recount.

Does NOT import any prior generator. Recomputes the 64 sphere-intersection
points from the declared cube-based construction at h=1, then runs an
exhaustive cube search (every point as a corner; 3 mutually-perpendicular
equal-length edge vectors; construct remaining 4 corners by vector addition;
require all 8 present). Counts distinct cubes by vertex set.

Construction (h=1):
  8 corner spheres, centers (+-1,+-1,+-1), radius 2
  1 central sphere, radius sqrt(3) through the corners
Intersect every triple of spheres; collect distinct real points.
"""
import itertools, collections, numpy as np

h = 1.0
centers = []
for sx in (-1, 1):
    for sy in (-1, 1):
        for sz in (-1, 1):
            centers.append(np.array([sx, sy, sz], float))
r = 2.0  # corner sphere radius 2h
R = np.sqrt(3.0)  # central reference sphere radius sqrt(3)h

spheres = [(c, r) for c in centers] + [(np.zeros(3), R)]

def intersect_triple(s1, s2, s3):
    (c1, r1), (c2, r2), (c3, r3) = s1, s2, s3
    # subtract sphere eq: 2(c2-c1).x = r1^2-r2^2 + |c2|^2-|c1|^2
    A = []
    b = []
    for (ci, ri), (cj, rj) in [((c1, r1), (c2, r2)), ((c1, r1), (c3, r3))]:
        d = cj - ci
        A.append(2 * d)
        b.append(ri**2 - rj**2 + (cj @ cj) - (ci @ ci))
    A = np.array(A); b = np.array(b)
    # general solution to A x = b  (two linear constraints, 3D -> 1D line)
    # solve via least-norm + nullspace
    try:
        x0 = np.linalg.lstsq(A, b, rcond=None)[0]
    except np.linalg.LinAlgError:
        return []
    # nullspace of A
    _, s, vt = np.linalg.svd(A)
    # nullspace basis = vt rows where singular value ~0
    null_basis = vt[2:] if vt.shape[0] == 3 else None
    # actually A is 2x3, vt is 3x3; last row(s) with ~0 singular value
    null = []
    for i, sv in enumerate(s):
        if sv < 1e-9:
            null.append(vt[i])
    if len(null) != 1:
        # degenerate (parallel planes): line is 2D intersection; skip triple
        return []
    dvec = null[0]
    dvec = dvec / np.linalg.norm(dvec)
    # intersect line x0 + t*dvec with sphere s1
    # |x0 + t d - c1|^2 = r1^2
    w = x0 - c1
    a = dvec @ dvec  # =1
    bb = 2 * (dvec @ w)
    cc = w @ w - r1**2
    disc = bb**2 - 4 * a * cc
    if disc < -1e-9:
        return []
    if disc < 0:
        disc = 0.0
    sq = np.sqrt(disc)
    pts = []
    for t in [(-bb + sq) / (2 * a), (-bb - sq) / (2 * a)]:
        p = x0 + t * dvec
        pts.append(np.round(p, 12))
    return pts

rng = range(len(spheres))
seen = set()
points = []
for i, j, k in itertools.combinations(rng, 3):
    # require at least the combination be a true 3-sphere meet; keep all distinct real pts
    for p in intersect_triple(spheres[i], spheres[j], spheres[k]):
        key = tuple(np.round(p, 9))
        if key not in seen:
            seen.add(key)
            points.append(p)

points = np.array(points)
print(f"Distinct sphere-intersection points: {len(points)}")

# build spatial index keyed to 1e-9
from collections import defaultdict
idx = defaultdict(list)
for i, p in enumerate(points):
    idx[tuple(np.round(p, 9))].append(i)

def find_point(p, tol=1e-7):
    k = tuple(np.round(p, 9))
    if k in idx:
        return idx[k][0]
    # nearest
    best = None; bd = tol + 1
    for j in k:
        pass
    # brute nearest within tol
    # (points small enough to brute force)
    d = np.linalg.norm(points - p, axis=1)
    m = np.argmin(d)
    if d[m] < tol:
        return m
    return None

# exhaustive cube search
cubes = set()
n = len(points)
for a in range(n):
    pa = points[a]
    for b in range(n):
        if b == a: continue
        e1 = points[b] - pa
        l1 = np.linalg.norm(e1)
        if l1 < 1e-9: continue
        e1 = e1 / l1
        for c2 in range(n):
            if c2 == a: continue
            e2 = points[c2] - pa
            l2 = np.linalg.norm(e2)
            if l2 < 1e-9: continue
            if abs(l2 - l1) > 1e-7: continue  # equal length
            e2 = e2 / l2
            if abs(e1 @ e2) > 1e-7: continue  # perpendicular
            e3 = np.cross(e1, e2)
            # candidate corner = a + l1*(e1+e2+e3)
            target = pa + l1 * (e1 + e2 + e3)
            t = find_point(target)
            if t is None: continue
            # build all 8 corners
            corners_idx = []
            ok = True
            for s1 in (0, 1):
                for s2 in (0, 1):
                    for s3 in (0, 1):
                        q = pa + l1 * (s1 * e1 + s2 * e2 + s3 * e3)
                        qi = find_point(q)
                        if qi is None:
                            ok = False; break
                        corners_idx.append(qi)
                    if not ok: break
                if not ok: break
            if not ok: continue
            # valid cube; record sorted vertex set
            cubes.add(tuple(sorted(corners_idx)))

print(f"Cubes detected (distinct vertex sets): {len(cubes)}")
# report half-edge lengths
for cs in sorted(cubes, key=lambda s: s[0]):
    c0 = points[cs[0]]
    neighbors = []
    for ci in cs[1:]:
        d = np.linalg.norm(points[ci] - c0)
        neighbors.append(d)
    neighbors.sort()
    hl = neighbors[0]  # smallest neighbor distance = edge length = 2h -> h = hl/2
    # actually edges connect corner to 3 neighbors all at edge length
    edge = neighbors[0]
    print(f"  cube center~ {np.round(np.mean(points[list(cs)],axis=0),4)}  edge={edge:.6f}  half-edge={edge/2:.6f}")
