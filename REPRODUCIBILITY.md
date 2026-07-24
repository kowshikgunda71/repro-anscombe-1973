# Reproducibility — doi:10.1080/00031305.1973.10478966

**Overall verdict: REPRODUCED**

This is *reproduction* (re-running the authors' own artifacts), not
replication. Tolerances were registered before the run.

## Claim / result matrix

| Claim | Metric | Claimed | Observed | Tolerance | Verdict |
|---|---|---|---|---|---|
| Pearson correlation r shared across the  | pearson_r | 0.816 | 0.816 | 0.001 (abs) | REPRODUCED |
| Least-squares slope shared across the qu | slope | 0.5 | 0.5 | 0.005 (abs) | REPRODUCED |
| Least-squares intercept shared across th | intercept | 3.0 | 3.0 | 0.05 (abs) | REPRODUCED |

## Environment & command

- Image: `python:3.12-alpine`
- Command: `python /inputs/reproduce.py`
- Artifact manifest hash: `23f079c0b5779aeffd4dfc6f9ef48452c6fa03bf0bc085e918a39106e1750a92`
- Sandbox policy hash: `c32ebb9dcd7dcc21a399cbc6cfe45458e1a14c065b6cc0262701e9e679c922df`
- Wall seconds: 4.85
- Outcome: COMPLETED

## Containment & limitations

- Runs are **containerized, not sandboxed**: no network, all Linux
  capabilities dropped, non-root user, read-only root filesystem, and
  CPU/memory/pid caps. On a host whose user is in the `docker` group the
  orchestrator is root-equivalent; a kernel escape reaches the host.
- Provenance is SLSA build level L1 (self-attested, unhosted).
- A `FAILED_SAFELY` outcome means a resource/time cap was hit, not that
  the result is wrong.
