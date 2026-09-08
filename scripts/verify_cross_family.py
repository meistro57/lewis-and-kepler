#!/usr/bin/env python3
"""CROSS-FAMILY-003: full 11,480-triple census over the 42 generated spheres."""
import numpy as np, math, itertools, collections
from scipy.spatial import cKDTree

h=1.0
corners=np.array([(a,b,c) for a in(-1,1) for b in(-1,1) for c in(-1,1)], float)
base=[(c,2.0) for c in corners]+[(np.zeros(3), math.sqrt(3))]
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
for (A,rA),(B,rB),(C,rC) in itertools.combinations(base,3):
    raw+=trip(A,rA,B,rB,C,rC)
raw=np.array(raw); tree=cKDTree(raw); seen=set(); U=[]
for i,p in enumerate(raw):
    if i not in seen: U.append(p); seen.update(tree.query_ball_point(p,1e-7))
U=np.array(U); rad=np.linalg.norm(U,axis=1)
shell32=U[abs(rad-math.sqrt(3))<1e-6]; small=U[abs(rad-math.sqrt(3)/3)<1e-6]
pts=[tuple(np.round(p,6)) for p in shell32]; pset=set(pts)
cubes=set()
for a in pts:
    A=np.array(a)
    for b in pts:
        if b==a: continue
        e1=np.array(b)-A
        if abs(np.dot(e1,e1)-4.0)>1e-6: continue
        for c in pts:
            if c in (a,b): continue
            e2=np.array(c)-A
            if abs(np.dot(e2,e2)-4.0)>1e-6 or abs(np.dot(e1,e2))>1e-6: continue
            e3=np.cross(e1,e2); e3=e3*2.0/np.linalg.norm(e3)
            cs=[A,A+e1,A+e2,A+e3,A+e1+e2,A+e1+e3,A+e2+e3,A+e1+e2+e3]
            if all(tuple(np.round(x,6)) in pset for x in cs):
                cubes.add(frozenset(tuple(np.round(x,6)) for x in cs))
spheres=[]
for cu in cubes:
    for v in cu: spheres.append((np.array(v,float),2.0))
    spheres.append((np.zeros(3),math.sqrt(3)))
for v in small: spheres.append((np.array(v,float),2.0/3.0))
spheres.append((np.zeros(3),math.sqrt(3)/3.0))
uniq={}
for c,r in spheres:
    uniq.setdefault((tuple(np.round(c,6)),round(r,6)),(np.array(c,float),r))
spheres=list(uniq.values())

cnt=collections.Counter(); allpts=[]
for (A,rA),(B,rB),(C,rC) in itertools.combinations(spheres,3):
    indep = np.linalg.norm(np.cross(2*(B-A),2*(C-A)))>1e-7
    p = trip(A,rA,B,rB,C,rC) if indep else []
    if indep and len(p)==2: cnt['two']+=1; allpts.extend(p)
    elif indep: cnt['empty_indep']+=1
    else: cnt['degen_or_circle']+=1
print("total:", sum(cnt.values()), "(expect 11480)")
print(dict(cnt))
P=np.array(allpts); t=cKDTree(P); keep=[]; seen=set()
for i,p in enumerate(P):
    if i not in seen: keep.append(p); seen.update(t.query_ball_point(p,1e-6))
print("distinct:", len(keep), "(expect 8566)")
