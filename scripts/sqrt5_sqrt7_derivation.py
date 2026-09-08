#!/usr/bin/env python3
"""√5/√7 radius derivation — where the surds come from, from first principles.

For 3 unit spheres centered at A,B,C (all |A|=|B|=|C|=1), an intersection point p
satisfies |p-A|²=1 → |p|² = 2(p·A), and subtracting pairs gives p·A = p·B = p·C.
So p = 2·d·n where n is the unit normal to the plane through A,B,C and d is the
signed distance from the origin to that plane. Hence r = 2|d|.

For the 12-fold generator (centers at 30° steps), the plane normal has components
built from 1 and √3/2, so |n|² is rational. The surds emerge from Pythagoras:
  √(3 + 3/4) = √(15/4) = √15/2 = √3·√5/2  ->  √5
  √(1 + 3/4) = √(7/4)  = √7/2           ->  √7
"""
from sympy import sqrt, Matrix, cos, sin, pi, simplify

def triple(xy1_deg, xy2_deg, xz_deg):
    A = Matrix([cos(xy1_deg*pi/180), sin(xy1_deg*pi/180), 0])
    B = Matrix([cos(xy2_deg*pi/180), sin(xy2_deg*pi/180), 0])
    C = Matrix([cos(xz_deg*pi/180), 0, sin(xz_deg*pi/180)])
    n = (B-A).cross(C-A)
    d = abs(A.dot(B.cross(C))) / n.norm()
    r = 2*d
    return simplify(r**2), simplify(r), simplify(n), simplify(n.dot(n))

for label, t in [
    ("r = 2/√5",     (-150, -30, -90)),
    ("r = 2/√3",     (-120, -30, -90)),
    ("r = 2√(3/7)",  (-120, -60, -90)),
]:
    r2, r, n, nsq = triple(*t)
    print(f"{label}:  r²={r2}  r={r}  |n|²={nsq}  (normal={n})")
