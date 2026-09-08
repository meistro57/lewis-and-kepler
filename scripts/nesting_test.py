#!/usr/bin/env python3
"""Nesting test: does Candidate A embed into the Minimal Core under any similarity sQ+t?
Scale-invariant distance-multiset test. Expect NEGATIVE.
"""
import itertools, collections
import numpy as np
from sympy import sqrt

# ---- Minimal Core 128 vertices (exact cubic frame, from handoff) ----
r = 1/sqrt(3); u = (3+sqrt(3))/6; v = (3-sqrt(3))/6
def gen(family):
    out = set()
    for perm in set(itertools.permutations(family)):
        perm = list(perm)
        nz = [i for i, x in enumerate(perm) if abs(float(x)) > 1e-12]
        for signs in itertools.product([1, -1], repeat=len(nz)):
            pp = perm[:]
            for idx, s in zip(nz, signs): pp[idx] = pp[idx]*s
            out.add(tuple(round(float(x), 12) for x in pp))
    return out
core = np.array(sorted(gen([r,r,r]) | gen([0,r,r]) | gen([r,0,0]) | gen([r,r/2,r/2])
                       | gen([2/sqrt(5),1/sqrt(5),0]) | gen([2/sqrt(5),0,0]) | gen([r,u,v])))
assert len(core) == 128

# ---- Candidate A 40 vertices ----
a = (12-2*sqrt(3))/33; b = (18+8*sqrt(3))/33; c = (6+10*sqrt(3))/33
fam24 = gen([a,b,b]); fam16 = set()
for signs in itertools.product([1,-1], repeat=3):
    fam16.add(tuple(round(float(s*x),12) for x,s in zip([c,c,b],signs)))
    fam16.add(tuple(round(float(s*x),12) for x,s in zip([c,b,c],signs)))
ca = np.array(sorted(fam24 | fam16))
assert len(ca) == 40

def dist2_multiset(P):
    m = []
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            m.append(round(float(np.sum((P[i]-P[j])**2)), 8))
    return collections.Counter(m)

ca_m = dist2_multiset(ca); core_m = dist2_multiset(core)
ca_distinct = set(ca_m); core_distinct = set(core_m)

# every candidate scale from matching CA's max distance to each core distance
ca_max = max(ca_distinct)
for cd in core_distinct:
    s2 = round(cd / ca_max, 6)
    if all(core_m.get(round(d*s2, 6), 0) >= cnt for d, cnt in ca_m.items()):
        print(f"EMBEDS at scale s^2={s2} — similarity found")
        raise SystemExit(0)
print("NO similarity embeds Candidate A into the Minimal Core.")
print(f"(CA distinct distances={len(ca_distinct)}, Core distinct={len(core_distinct)})")
print("NESTING NEGATIVE CONFIRMED")
