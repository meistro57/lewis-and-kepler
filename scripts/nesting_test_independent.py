#!/usr/bin/env python3
"""Candidate A vs Minimal Core: reconstruct both, then test nesting/containment."""
import itertools
import numpy as np
from sympy import sqrt, Rational

# ---------- exact symbolic constants ----------
r  = 1/sqrt(3)
u  = (3+sqrt(3))/6
v  = (3-sqrt(3))/6
e2 = 2/sqrt(5)   # 2/√5
e1 = 1/sqrt(5)   # 1/√5

def sign_permutations(repr_vals):
    """All distinct coordinate permutations and all independent signs of nonzero entries."""
    # find distinct permutations of the tuple
    seen = set()
    perms = []
    for p in itertools.permutations(repr_vals):
        if p in seen: continue
        seen.add(p); perms.append(p)
    pts = []
    for p in perms:
        nz = [i for i, x in enumerate(p) if x != 0]
        for signbits in itertools.product([1, -1], repeat=len(nz)):
            arr = [0.0, 0.0, 0.0]
            for i, x in enumerate(p):
                arr[i] = float(x)
            for j, si in enumerate(nz):
                arr[si] *= signbits[j]
            pts.append(tuple(arr))
    return pts

# ---------- Minimal Core, 128 vertices (cubic frame) ----------
core_families = {
    'S8':   (r, r, r),
    'A12':  (0, r, r),
    'A6':   (r, 0, 0),
    'VF24': (r, r/2, r/2),
    'EF24': (e2, e1, 0),
    'D6':   (e2, 0, 0),
    'VEF48':(r, u, v),
}
core_pts = []
core_labels = []
for name, rep in core_families.items():
    pts = sign_permutations(rep)
    core_pts.extend(pts)
    core_labels.extend([name]*len(pts))
core = np.array(core_pts)
print("Core vertices:", len(core), "(expect 128)")
from collections import Counter
print("  family counts:", dict(Counter(core_labels)))

# radii distribution
radii = np.round(np.linalg.norm(core, axis=1), 9)
print("  distinct radii:", sorted(set(radii)))
print("  points at radius 1 (unit sphere):", int(np.sum(np.abs(radii-1) < 1e-8)))

# ---------- Candidate A, 40 vertices ----------
a = (12 - 2*sqrt(3))/33
b = (18 + 8*sqrt(3))/33
c = (6 + 10*sqrt(3))/33

A24 = sign_permutations((a, b, b))
# 16-family: signs of ONLY (c,c,b) and (c,b,c) — no (b,c,c)
def signs_only(repr_vals):
    nz = [i for i, x in enumerate(repr_vals) if x != 0]
    out = []
    for signbits in itertools.product([1, -1], repeat=len(nz)):
        arr = [float(x) for x in repr_vals]
        for j, si in enumerate(nz):
            arr[si] *= signbits[j]
        out.append(tuple(arr))
    return out
A16 = signs_only((c, c, b)) + signs_only((c, b, c))

A = np.array(A24 + A16)
print("\nCandidate A vertices:", len(A), "(expect 40)")
RA = float(sqrt(2*b))
print("  R_A =", RA)
print("  all on sphere radius R_A:", np.allclose(np.linalg.norm(A,axis=1), RA))

A_norm = A / RA   # normalized to unit sphere
print("  normalized radius:", np.round(np.linalg.norm(A_norm[0]), 12))

# ---------- distance multiset necessary condition ----------
def pair_dist2(P):
    d = []
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            d.append(float(np.sum((P[i]-P[j])**2)))
    return np.array(d)

# Candidate A normalized pairwise squared distances
dA = pair_dist2(A_norm)
# Core unit-sphere points pairwise squared distances
core_unit = core[np.abs(radii-1) < 1e-8]
dC = pair_dist2(core_unit)
print("\n=== necessary condition (unit-sphere, no translation) ===")
print("  A normalized has", len(dA), "pairwise distances")
print("  Core unit sphere has", len(core_unit), "pts,", len(dC), "pairwise distances")

# does every A distance appear in Core's distance set (within tolerance)?
tol = 1e-7
dC_sorted = np.sort(dC)
def count_matches(dA_val):
    return np.sum(np.abs(dC_sorted - dA_val) < tol)

unmatched = []
for dv in dA:
    if not np.any(np.abs(dC - dv) < tol):
        unmatched.append(dv)
print("  A distances NOT present in Core unit-sphere set:", len(unmatched))
if unmatched:
    print("  sample:", unmatched[:5])

# histogram comparison
print("  A distinct distances:", len(set(np.round(dA, 6))))
print("  Core distinct distances:", len(set(np.round(dC, 6))))
