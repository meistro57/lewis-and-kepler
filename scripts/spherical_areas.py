#!/usr/bin/env python3
"""Candidate A: spherical (solid-angle) areas of the 22 faces — test the '22 regions, groups 2/4/8/8' claim."""
import json
import numpy as np
from scipy.spatial import ConvexHull
from collections import Counter, defaultdict

d = json.load(open('/home/dev/Subject963/audit/audit_results.json'))
X = np.array(d['candidate_a_points'])

# reconstruct faces (coplanar merge, same as prior audits)
hull = ConvexHull(X)
faces = {}
for simplex, eq in zip(hull.simplices, hull.equations):
    faces.setdefault(tuple(np.round(eq, 8)), set()).update(map(int, simplex))
faces = list(faces.values())
print(f"faces: {len(faces)}")

def solid_angle(a, b, c):
    """Solid angle (spherical triangle area) of unit vectors a,b,c in steradians."""
    # normalize
    a = a / np.linalg.norm(a); b = b / np.linalg.norm(b); c = c / np.linalg.norm(c)
    denom = 1 + np.dot(a, b) + np.dot(b, c) + np.dot(c, a)
    num = abs(np.dot(a, np.cross(b, c)))
    return 2 * np.arctan2(num, denom)

face_areas = []
for face in faces:
    ids = list(face)
    p = X[ids]
    c = p.mean(axis=0)
    # project centroid to unit sphere as the fan center
    cc = c / np.linalg.norm(c)
    # order vertices around face normal
    _, _, basis = np.linalg.svd(p - c)
    coords = (p - c) @ basis[:2].T
    ang = np.arctan2(coords[:, 1], coords[:, 0])
    order = np.argsort(ang)
    seq = [ids[i] for i in order]
    # triangulate fan from centroid: sum spherical triangle areas
    total = 0.0
    n = len(seq)
    for i in range(n):
        v1 = X[seq[i]] / np.linalg.norm(X[seq[i]])
        v2 = X[seq[(i + 1) % n]] / np.linalg.norm(X[seq[(i + 1) % n]])
        total += solid_angle(cc, v1, v2)
    face_areas.append((total, len(face), tuple(sorted(ids))))

# round areas to group
areas = [round(a, 4) for a, _, _ in face_areas]
area_groups = Counter(areas)
print("\n=== spherical (solid-angle) area groups ===")
print(f"distinct area values: {len(area_groups)}")
for area, count in sorted(area_groups.items(), reverse=True):
    print(f"  area ~{area:.4f} sr: {count} faces")

# group sizes
group_sizes = sorted(area_groups.values(), reverse=True)
print(f"\ngroup sizes: {group_sizes}  (sum = {sum(group_sizes)})")
print(f"claim 'groups of 2, 4, 8, 8' -> sorted {sorted([2,4,8,8], reverse=True)}")

# also show face-size histogram for cross-reference
face_sizes = Counter(len(f) for f in faces)
print(f"\nface size histogram: {dict(sorted(face_sizes.items()))}")
