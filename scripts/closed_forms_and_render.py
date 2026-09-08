#!/usr/bin/env python3
"""Candidate A — exact algebra hunt + a real 3D render."""
import json
import numpy as np
from sympy import nsimplify, sqrt, Rational, simplify, nsimplify

d = json.load(open('/home/dev/Subject963/audit/audit_results.json'))
X = np.array(d['candidate_a_points'])
hull = set(tuple(e) for e in d['candidate_a_hull_edges'])
native = set(tuple(e) for e in d['native_family_hull_edges'])
retained = native & hull
released = native - hull
added = hull - native

# --- exact forms of the three coordinate magnitudes ---
a = 0.258663587420068
b = 0.7066820628996597
c = 0.965345650319728
print("=== exact coordinate forms (sympy nsimplify) ===")
for name, v in [('a', a), ('b', b), ('c', c)]:
    for dom in ([sqrt(3), sqrt(2), sqrt(5)], [sqrt(3), sqrt(2), sqrt(5), sqrt(6)]):
        try:
            e = nsimplify(v, dom)
            if not e.is_number or e.free_symbols:
                continue
            err = abs(float(e) - v)
            if err < 1e-9:
                print(f"  {name} = {e}   (err {err:.1e})")
                break
        except Exception:
            pass
    else:
        print(f"  {name} = {v}  (no clean form found)")

print("\n=== relations ===")
print(f"  c/a = {c/a:.10f}   (2+√3 = {2+sqrt(3).evalf():.10f})")
print(f"  b/a = {b/a:.10f}   (1+√3 = {1+sqrt(3).evalf():.10f})")
print(f"  c-b = {c-b:.10f}   (a = {a:.10f})")
print(f"  a+b = {a+b:.10f}   (c = {c:.10f})")
print(f"  c^2-b^2 = {c*c-b*b:.10f}  b^2-a^2 = {b*b-a*a:.10f}")
r5 = np.sqrt(2*b*b + c*c)
print(f"  radius (16-family) = {r5:.10f}")

# --- render ---
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# family assignment
fam = {}
for i, x in enumerate(X):
    s = tuple(np.round(np.sort(np.abs(x)), 9))
    fam[i] = 0 if s[0] < 0.3 else 1   # 24-family has small coord 0.2587, 16-family all >=0.7067

fig = plt.figure(figsize=(11, 11), facecolor="#070A12")
ax = fig.add_subplot(111, projection="3d")
for p in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
    p.set_facecolor("#070A12"); p.set_edgecolor("#151a28")
ax.set_axis_off()

c24 = "#6FD3F2"   # teal  -> 24-family (deformed truncated cube)
c16 = "#F0D48A"   # gold  -> 16-family (deformed octagonal prism)
c_ret = "#E6E6E6"
c_rel = "#8A5A5A"
c_add = "#63E6A0"

# draw edges
def line(e, color, lw, alpha):
    for i, j in e:
        ax.plot(*zip(X[i], X[j]), color=color, lw=lw, alpha=alpha)

line(released, c_rel, 0.7, 0.35)   # released (ghost)
line(retained, c_ret, 1.3, 0.9)    # retained
line(added, c_add, 2.2, 1.0)       # new cross-family

# vertices colored by family
for fam_id, col in [(0, c24), (1, c16)]:
    idx = [i for i in range(len(X)) if fam[i] == fam_id]
    ax.scatter(X[idx,0], X[idx,1], X[idx,2], c=col, s=70, edgecolor="white",
               linewidth=0.6, depthshade=False, zorder=5)

ax.set_box_aspect((1,1,1))
ax.view_init(elev=18, azim=-42)
plt.title("Candidate A — 40 vertices, 60 edges\n28 retained · 32 released · 32 new\nD₄h, families 24 (teal) + 16 (gold)",
          color="#CBA766", fontsize=14, pad=14, family="serif")
plt.tight_layout()
out = "/home/dev/Subject963/candidate_a_render.png"
plt.savefig(out, dpi=140, facecolor=fig.get_facecolor())
print("\nsaved", out)
