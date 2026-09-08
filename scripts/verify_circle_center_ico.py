#!/usr/bin/env python3
"""Circle-center -> icosahedron layer: 48 pentagonal circles -> 4 icosahedra.
The circle center is the projection of the origin onto the pentagon's plane."""
import numpy as np, math, itertools, collections
from scipy.spatial import cKDTree, ConvexHull

h=1.0
corners=np.array([(a,b,c) for a in(-1,1) for b in(-1,1) for c in(-1,1)], float)
centers=[(c,2.0) for c in corners]+[(np.zeros(3), math.sqrt(3))]
def trip(A,rA,B,rB,C,rC):
    v=B-A; d=float(np.linalg.norm(v))
    if d<1e-12: return []
    ex=v/d; delta=C-A; i=float(ex@delta); t=delta-i*ex; j=float(np.linalg.norm(t))
    if j<1e-12: return []
    ey=t/j; ez=np.cross(ex,ey)
    xp=(rA*rA-rB*rB+d*d)/(2*d); yp=(rA*rA-rC*rC+i*i+j*j-2*i*xp)/(2*j)
    h2=rA*rA-xp*xp-yp*yp
    if h2<-1e-9: return []
    hh=math.sqrt(max(0.,h2)); base=A+xp*ex+yp*ey
    out=[base+hh*ez]
    if hh>=1e-10: out.append(base-hh*ez)
    return out
raw=[]
for (A,rA),(B,rB),(C,rC) in itertools.combinations(centers,3):
    raw+=trip(A,rA,B,rB,C,rC)
raw=np.array(raw); tree=cKDTree(raw); seen=set(); U=[]
for i,p in enumerate(raw):
    if i not in seen: U.append(p); seen.update(tree.query_ball_point(p,1e-7))
U=np.array(U); rad=np.linalg.norm(U,axis=1)
shell=U[abs(rad-math.sqrt(3))<1e-6]
phi=(1+math.sqrt(5))/2

def is_reg_pent(pts):
    d=[]
    for i in range(5):
        for j in range(i+1,5): d.append(np.dot(pts[i]-pts[j],pts[i]-pts[j]))
    d=np.array(sorted(d))
    if np.max(d[:5])-np.min(d[:5])>1e-7 or np.max(d[5:])-np.min(d[5:])>1e-7: return False
    return abs(math.sqrt(d[5]/d[0])-phi)<1e-4

def circle_center(pts):
    m=pts.mean(0); _,_,vt=np.linalg.svd(pts-m); n=vt[-1]; n=n/np.linalg.norm(n)
    return np.dot(n,m)*n

clist=[]
for idx in itertools.combinations(range(len(shell)),5):
    p=shell[list(idx)]
    if is_reg_pent(p): clist.append(circle_center(p))
pc=np.array(clist); t=cKDTree(pc); keep=[]; seen=set()
for i,p in enumerate(pc):
    if i not in seen: keep.append(p); seen.update(t.query_ball_point(p,1e-6))
pc=np.array(keep)
print("pentagons=%d  distinct centers=%d"%(len(clist),len(pc)))
rl=collections.Counter(np.round(np.linalg.norm(pc,axis=1),6))
print("center radius levels (r:n):", dict(sorted(rl.items())))
rs=sorted(rl)
print("ratio R_outer/R_inner = %.6f (expect 2+sqrt5=%.6f)"%(rs[1]/rs[0],2+math.sqrt(5)))
