#!/usr/bin/env python3
"""CUBE-SPHERE-001: verify sqrt(5) is FORCED out of the sphere algebra, and the
64-point census with two regular dodecahedra sharing the cube."""
import numpy as np, math, itertools, collections
from scipy.spatial import cKDTree, ConvexHull
from sympy import sqrt, symbols, solve, simplify

# symbolic: does sqrt(5) fall out?
x, y, z, h = symbols('x y z h', positive=True)
sol = solve([(x**2+y**2+z**2-3*h**2).subs(x,0),
             ((x-h)**2+(y+h)**2+(z-h)**2-4*h**2).subs(x,0),
             ((x+h)**2+(y+h)**2+(z-h)**2-4*h**2).subs(x,0)], [y,z], dict=True)
print("y/h roots:", [simplify(s[y]/h) for s in sol])

# numerical
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
U=np.array(U)
print("raw=%d unique=%d (expect 160 -> 64)"%(len(raw),len(U)))
rad=np.linalg.norm(U,axis=1)
print("shells (r:n):", dict(sorted(collections.Counter(np.round(rad,6)).items())))
shell32=U[abs(rad-math.sqrt(3))<1e-6]
phi=(1+math.sqrt(5))/2
def cyc(v): return [(v[0],v[1],v[2]),(v[2],v[0],v[1]),(v[1],v[2],v[0])]
goldA=set(); goldB=set()
for a in(-1,1):
    for b in(-1,1):
        for p in cyc((0.0,a*h/phi,b*h*phi)): goldA.add(tuple(np.round(p,6)))
        for p in cyc((0.0,a*h*phi,b*h/phi)): goldB.add(tuple(np.round(p,6)))
def is_dod(pts):
    H=ConvexHull(pts); faces={}
    for s,eq in zip(H.simplices,H.equations):
        faces.setdefault(tuple(np.round(eq,6)),set()).update(map(int,s))
    return len(faces)==12 and set(len(v) for v in faces.values())=={5}
for name,g in [("A",goldA),("B",goldB)]:
    pts=np.array([corners[i] for i in range(8)]+[np.array(q) for q in g],float)
    print(f"dodecahedron {name} regular:", is_dod(pts))
