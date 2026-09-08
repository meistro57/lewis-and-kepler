#!/usr/bin/env python3
"""Independent full cross-family triple census (CROSS-FAMILY-003).
Rebuild the 42-sphere registry from the 64-point set, enumerate all C(42,3)=11,480
triples, classify outcomes, and verify the report's counts."""
import numpy as np
from itertools import combinations
from scipy.spatial import cKDTree

# ---- regenerate the 64 junction points (cube + central reference sphere) ----
h = 1.0
corners = np.array([[x,y,z] for x in (-h,h) for y in (-h,h) for z in (-h,h)], dtype=float)
centers9 = np.vstack([corners, [[0.,0.,0.]]])
radii9 = np.array([2*h]*8 + [np.sqrt(3)*h])

def ti(c1,c2,c3,r1,r2,r3):
    p2=c2-c1; p3=c3-c1; d=np.linalg.norm(p2)
    if d<1e-12: return []
    ex=p2/d; i=ex@p3; ey=p3-i*ex; j=np.linalg.norm(ey)
    if j<1e-12: return []
    ey/=j; ez=np.cross(ex,ey)
    x=(r1*r1-r2*r2+d*d)/(2*d); y=(r1*r1-r3*r3+i*i+j*j-2*i*x)/(2*j)
    hh=r1*r1-x*x-y*y
    if hh<-1e-9: return []
    if abs(hh)<1e-12: hh=0
    z=np.sqrt(max(0,hh)); base=c1+x*ex+y*ey
    return [base] if z==0 else [base+z*ez, base-z*ez]

raw=[]
for (i,j,k) in combinations(range(9),3):
    raw.extend(ti(centers9[i],centers9[j],centers9[k],radii9[i],radii9[j],radii9[k]))
P=np.array(raw); tree=cKDTree(P); seen=set(); U=[]
for i,p in enumerate(P):
    if i not in seen:
        U.append(p); seen.update(tree.query_ball_point(p,1e-7))
U=np.array(U)
print(f"64-point set: {len(U)} points")

# ---- build the 42-sphere registry ----
# 32 corner spheres: centers = points on the sqrt(3) shell, radius 2
# 8 corner spheres: centers = points on the 1/sqrt(3) shell, radius 2/3
# 1 reference sphere: center 0 radius sqrt(3)
# 1 reference sphere: center 0 radius 1/sqrt(3)
rt3 = np.array([p for p in U if abs(np.linalg.norm(p)-np.sqrt(3)) < 1e-6])
r1o3 = np.array([p for p in U if abs(np.linalg.norm(p)-1/np.sqrt(3)) < 1e-6])
print(f"sqrt(3) shell: {len(rt3)}, 1/sqrt(3) shell: {len(r1o3)}")

spheres = []  # (center, radius)
for p in rt3: spheres.append((p, 2.0))
for p in r1o3: spheres.append((p, 2.0/3.0))
spheres.append((np.zeros(3), np.sqrt(3)))
spheres.append((np.zeros(3), 1.0/np.sqrt(3)))
print(f"total spheres: {len(spheres)} (claim 42)")

# dedupe by (center, radius) to be safe
skey = set(); dedup = []
for c, r in spheres:
    k = (tuple(np.round(c,6)), round(r,6))
    if k not in skey:
        skey.add(k); dedup.append((c,r))
print(f"distinct spheres after dedupe: {len(dedup)} (claim 42)")

centers = np.array([c for c,r in dedup]); radii = np.array([r for c,r in dedup])
N = len(dedup)

# ---- classify all triples ----
def classify_triple(i, j, k, tol=1e-7):
    c1,c2,c3 = centers[i],centers[j],centers[k]
    r1,r2,r3 = radii[i],radii[j],radii[k]
    # radical planes P12 and P13 relative to sphere 1:
    # P12: 2(c2-c1).x = |c2|^2 - |c1|^2 + r1^2 - r2^2
    n12 = 2*(c2-c1); b12 = c2@c2 - c1@c1 + r1*r1 - r2*r2
    n13 = 2*(c3-c1); b13 = c3@c3 - c1@c1 + r1*r1 - r3*r3
    # check coincident spheres
    if np.linalg.norm(c1-c2) < tol and abs(r1-r2) < tol: return 'coincident'
    if np.linalg.norm(c1-c3) < tol and abs(r1-r3) < tol: return 'coincident'
    if np.linalg.norm(c2-c3) < tol and abs(r2-r3) < tol: return 'coincident'
    cross = np.cross(n12, n13)
    if np.linalg.norm(cross) > tol * (np.linalg.norm(n12)*np.linalg.norm(n13)+1e-12):
        # independent radical planes -> line
        # direction = cross(n12, n13)
        dline = cross / np.linalg.norm(cross)
        # find a point on the line: solve n12.x=b12, n13.x=b13
        A = np.vstack([n12, n13, dline])
        b = np.array([b12, b13, 0.0])
        # solve for a point p0 with n12.p0=b12, n13.p0=b13, dline.p0=0
        p0 = np.linalg.solve(A, b)
        # intersect line p0 + t*dline with sphere 1
        # |p0 + t dline - c1|^2 = r1^2
        v = p0 - c1
        a = dline@dline  # =1
        bb = 2*(v@dline)
        cc = v@v - r1*r1
        disc = bb*bb - 4*a*cc
        if disc < -tol:
            return 'empty_indep'
        if abs(disc) < tol:
            return 'tangent'
        return 'two_points'
    else:
        # parallel radical planes
        # are they the same plane? check consistency
        # if n12 ~ 0 and n13 ~ 0 -> spheres concentric -> either coincident or concentric-disjoint
        if np.linalg.norm(n12) < tol and np.linalg.norm(n13) < tol:
            # all three centers equal (concentric)
            return 'degenerate'
        # check if planes are parallel but distinct (inconsistent)
        # normalize
        nn12 = n12/(np.linalg.norm(n12)+1e-30); nn13 = n13/(np.linalg.norm(n13)+1e-30)
        if abs(nn12@nn13) > 1 - tol:  # parallel (same or opposite)
            # check if same plane: compare normalized offsets
            off12 = b12/(np.linalg.norm(n12)+1e-30); off13 = b13/(np.linalg.norm(n13)+1e-30)
            if abs(off12 - off13*np.sign(nn12@nn13)) < tol:
                # same plane -> shared circle (if it cuts sphere 1)
                # distance from c1 to plane
                dist = abs(nn12@c1 - off12)
                if dist < r1 + tol:
                    return 'shared_circle'
                return 'empty_degenerate'
            else:
                return 'empty_degenerate'
        else:
            return 'degenerate'

outcomes = {'two_points':0,'empty_indep':0,'empty_degenerate':0,'shared_circle':0,'tangent':0,'coincident':0,'degenerate':0}
two_point_triples = 0
all_points = []

from collections import Counter
for (i,j,k) in combinations(range(N),3):
    o = classify_triple(i,j,k)
    outcomes[o] += 1
    if o == 'two_points':
        two_point_triples += 1
        pts = ti(centers[i],centers[j],centers[k],radii[i],radii[j],radii[k])
        all_points.extend(pts)

print(f"\n=== triple census (total {N} spheres, {N*(N-1)*(N-2)//6} triples) ===")
for o in ['two_points','empty_indep','empty_degenerate','shared_circle','tangent','coincident','degenerate']:
    print(f"  {o}: {outcomes[o]}")
print(f"\ntwo-point triples: {two_point_triples} (claim 9792)")
print(f"point occurrences: {len(all_points)} (claim 19584)")
# dedupe points
AP = np.array(all_points)
tree2 = cKDTree(AP); seen2=set(); UP=[]
for i,p in enumerate(AP):
    if i not in seen2:
        UP.append(p); seen2.update(tree2.query_ball_point(p,1e-7))
print(f"distinct points: {len(UP)} (claim 8566)")
