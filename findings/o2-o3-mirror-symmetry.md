# O2/O3 mirror symmetry — equal average resistance explained

Status: recorded (Lewis, commit keeper). Result authored by 963, tested by 963; interpretation Kepler.

## The claim

O2 and O3 show equal average resistance not because the network treats them
identically, but because they are related by a mirror symmetry that exchanges
them while relabeling which terminal pairs receive which benefits.

## The mapping

Reflect across the XY plane:

    (x, y, z) -> (x, y, -z)

This exchanges O2 <-> O3 and preserves the full modeled network.

## Test results (963)

| Test | Result |
| --- | --- |
| 24 proper cubic rotations | None exchange O2 and O3 |
| 24 reflection-type cubic symmetries | All exchange O2 and O3 |
| Full resistance matrices after terminal relabeling | Agree within 4.44e-16 |
| Contact resistances checked | 0, 0.01, 0.1, 1, 10 |

## Interpretation

- The equal averages are real but conceal a rearrangement: reflecting and
  relabeling terminals makes the full results match, not just the averages.
- O1 remains distinct, so the earlier finding stands — the combined
  72-junction group concealed genuinely different behavior.
- Coordinate and straight-path correspondence checks were exact; circular-arc
  geometry was verified numerically.

## Reproducibility

Full results and script: Kepler's sandbox
`sandbox:/workspace/scratch/69c86fc56022/Centerstone_Kepler_Math_004.zip`
(not committed here — a sandbox artifact held by Kepler; ask Kepler to mirror it
into `data/` if a durable copy is wanted).

## Provenance note

Recorded from 963's channel message (2026-09-11 16:42 CDT). Numbers quoted
verbatim; no independent re-run performed by Lewis at commit time. Treat as a
recorded finding pending Lewis re-verification, not an independently confirmed
measurement.
