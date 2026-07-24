# Reproduction: Graphs in Statistical Analysis

**Verdict: REPRODUCED**  (3/3 claims reproduced within their pre-registered tolerance)

An independent *reproduction* (ACM "Results Reproduced") — re-running the authors' own artifacts and checking the reported numbers against tolerances registered **before** the run.

## Paper reproduced

> Anscombe, F. J. (1973) *Graphs in Statistical Analysis*. The American Statistician, 27(1), 17-21. https://doi.org/10.1080/00031305.1973.10478966

Original work by the authors above; all credit for the research is theirs. This repository is an independent reproduction, not the original work, and does not redistribute the paper's code, data, or models — see [ACQUISITION.md](ACQUISITION.md). See [CITATION.cff](CITATION.cff) to cite both this reproduction and the original paper.

Produced with [paper-repro-gym](https://github.com/kowshikgunda71/paper-repro-gym), a gated, containerized reproduction workbench.

## Results (reported honestly)

Every registered claim is shown with its verdict — reproduced, **not reproduced**, partial, or inconclusive alike. A failure to reproduce is a real, reportable result and is never hidden.

| Claim | Metric | Claimed | Observed | Tolerance | Verdict |
|---|---|---|---|---|---|
| Pearson correlation r shared across the  | pearson_r | 0.816 | 0.816 | 0.001 (abs) | REPRODUCED |
| Least-squares slope shared across the qu | slope | 0.5 | 0.5 | 0.005 (abs) | REPRODUCED |
| Least-squares intercept shared across th | intercept | 3.0 | 3.0 | 0.05 (abs) | REPRODUCED |

## How it was reproduced

- `experiment.json` — the exact image and command that was run.
- `claims.json` — the claims and tolerances, registered before the run.
- `code/` — the reproduction harness (the scripts that were run). This is the reproducer's own code; the paper's artifacts are **not** redistributed (see [ACQUISITION.md](ACQUISITION.md)).

## Evidence in this repo

- `claim_result_matrix.json` — claimed vs observed vs pre-registered tolerance
- `experiment_manifest.json` — image (by digest), command, hashes, resource use, boundary
- `provenance.json` — SLSA-subset build provenance
- `REPRODUCIBILITY.md` — how to reproduce this reproduction
- `logs/` — raw run record, stdout, stderr

## Reproduce it yourself

Clone [paper-repro-gym](https://github.com/kowshikgunda71/paper-repro-gym), acquire the artifacts per ACQUISITION.md,
and run the command in `experiment_manifest.json` on a hardened boundary.

A failure to reproduce is a real, reportable result — this record states the
verdict honestly, whatever it was.
