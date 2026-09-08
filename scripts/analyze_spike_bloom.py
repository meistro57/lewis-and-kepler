#!/usr/bin/env python3
"""Spike & Bloom geometry analysis — ingest, counts, symmetry, family census.
Point the JSON path via env SPIKE_JSON (default: the staged inbound file).
"""
import json, os, collections
import numpy as np

f = os.environ.get("SPIKE_JSON",
    "/home/dev/.openclaw/workspace-kepler/media/inbound/openclaw-staged-b2952ef4-0d71-4e74-a6b3-c4bf9607afb9/input-Centerstone_Spike_and_Bloom_Geometry_1---2733fbbe-a4cc-44cf-8780-f81a650f6879.json")
d = json.load(open(f))
g = d["normalized_direction_graphs"]

for name, gr in g.items():
    V = np.array(gr["vertices"]); E = gr["edges"]
    r = np.linalg.norm(V, axis=1)
    deg = collections.Counter()
    for u, v in E:
        deg[u] += 1; deg[v] += 1
    print(f"{name}: V={len(V)} E={len(E)}  radius {r.min():.4f}..{r.max():.4f}  "
          f"deg range {min(deg.values())}..{max(deg.values())}")

# G24 symmetry: verify it is a rotation group
rots = [np.array(M) for M in d["G24_rotations"]]
orth = all(np.allclose(M.T@M, np.eye(3), atol=1e-6) for M in rots)
closed = all(any(np.allclose(Mi@Mj, M, atol=1e-6) for M in rots) for Mi in rots for Mj in rots)
print(f"\nG24: {len(rots)} rotations, orthogonal={orth}, closed={closed}, "
      f"identity={any(np.allclose(M,np.eye(3),atol=1e-8) for M in rots)}  -> octahedral group O")

print("\nfamily census:")
for fam in d["native_named_families"]:
    print(f"  {fam['name']}: {fam['instances']}")
print("\nspike apex radii:")
for s in d["spike_instances"]:
    print(f"  {s['family']}: V={len(s['vertices'])}  apex_radius={s['apex_radius']}")
