#!/usr/bin/env python3
"""Reproduce the central result of Anscombe, F.J. (1973), "Graphs in Statistical
Analysis", The American Statistician 27(1):17-21 (DOI 10.1080/00031305.1973.10478966):
four datasets with (nearly) IDENTICAL summary statistics despite different shapes —
Pearson r = 0.816 and the linear fit y = 3.00 + 0.50 x for each.

Stdlib only (statistics.correlation / linear_regression, Python >= 3.10).
Deterministic; no network. The quartet's data values are the standard public
figures reproduced in the paper. We report the mean across the four sets."""
import json, os, statistics

X_common = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
X4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
sets = {
    "I":   (X_common, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  (X_common, [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": (X_common, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  (X4,        [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
rs, slopes, intercepts = [], [], []
for name, (x, y) in sets.items():
    rs.append(statistics.correlation(x, y))
    sl, ic = statistics.linear_regression(x, y)
    slopes.append(sl); intercepts.append(ic)

metrics = {
    "pearson_r": round(statistics.fmean(rs), 3),
    "slope": round(statistics.fmean(slopes), 3),
    "intercept": round(statistics.fmean(intercepts), 2),
}
os.makedirs("/output", exist_ok=True)
json.dump(metrics, open("/output/metrics.json", "w"))
print(metrics)
