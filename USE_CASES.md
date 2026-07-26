# Where this work is useful

Anscombe (1973) built four datasets with **identical** summary statistics —
same mean, same variance, same correlation (r = 0.816), same regression line
(y = 3.0 + 0.5x) — that look completely different when plotted. This
reproduction confirmed all three shared statistics to the registered tolerance.

Two halves below: what is genuinely established, and what is extrapolation.

---

# Part A — What this reproduction establishes

## A1. The three claims held exactly

| claim | paper | observed | tolerance | verdict |
|---|---|---|---|---|
| Pearson r shared across all four sets | 0.816 | 0.816 | ±0.001 | REPRODUCED |
| least-squares slope | 0.5 | 0.5 | ±0.005 | REPRODUCED |
| least-squares intercept | 3.0 | 3.0 | ±0.05 | REPRODUCED |

**3/3, and that is the point of including it here.** A verification pipeline that
only ever reports failures is not measuring anything — it is broken in a way that
happens to look rigorous. Anscombe is the positive control: a claim that *should*
reproduce exactly, and does.

## A2. The paper's own argument is the use case

Anscombe's thesis is that summary statistics without a plot can conceal anything.
That argument is still the reason every statistics course opens with these four
scatterplots. Nothing here needs updating for 2026 — the result is arithmetic on
eleven data points and will not change.

---

# Part B — Unvalidated suggestions

> ### ⚠️ Not tested by this reproduction.
> Extrapolations from the artifacts. Hypotheses, not results.

### B1. A regression test for any statistics implementation — *procedure*

Anscombe's quartet is a genuinely good fixture: eleven rows, exactly known
answers to four decimal places, and four datasets that must agree on the
statistics while disagreeing on everything else. If a refactor of your
correlation or OLS code changes any of these values, it is wrong.

`code/` runs it in well under a second.

### B2. A dashboard/metric-design smoke test — *procedure*

The failure Anscombe describes — a single summary number hiding four different
realities — is exactly what a KPI tile does. Plotting the quartet through a
metrics pipeline that only reports means and correlations demonstrates the
blind spot to a non-technical audience in about thirty seconds.

### B3. A calibration check for a verification pipeline — *procedure*

Use it the way this repo does: as the positive control. Any claim-checking
system should be run against a claim known to be true before its failures are
believed. If your tooling cannot reproduce Anscombe, its NOT_REPRODUCED verdicts
mean nothing.

### B4. Teaching pre-registration with a case that passes — *procedure*

Most pre-registration teaching examples are cautionary. This one is short,
arithmetic, and passes — which makes it the right first exercise before showing
a case where the answer was "not enough runs to tell" (see
[repro-lottery-ticket](https://github.com/kowshikgunda71/repro-lottery-ticket)).
