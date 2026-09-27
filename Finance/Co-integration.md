---
tags:
  - "finance"
  - "ds-foundations"
---

Two time series are **cointegrated** when each wanders like a random walk (is non-stationary), but some linear combination of them is stationary: they may drift, but they drift together and the gap between them keeps reverting. Many financial series, such as prices, are non-stationary, so this matters for pairs trading and for modelling long-run relationships.

## Why Not Just Correlation?

[[Correlation and Covariance|Correlation]] measures co-movement and lies between -1 and 1. For trending, non-stationary series it is misleading: two unrelated random walks often show a large correlation by chance (a *spurious* relationship). Cointegration asks a different question: does a stable long-run link exist between the levels?

## Definition

Let $x_t$ and $y_t$ be integrated of order 1, written I(1): each becomes stationary after one difference. They are cointegrated if, for some $\beta$, the spread below is stationary, I(0):

$$
u_t = y_t - \beta x_t
$$

The earlier wording said the combined series has constant mean and standard deviation; that is the practical meaning of stationarity here.

## Engle–Granger Test

statsmodels' `coint` runs the augmented Engle–Granger two-step test:[^coint]

1. Regress $y_t$ on $x_t$ (with a constant by default) to estimate $\beta$.
2. Test the residuals for a unit root. Rejecting the unit root means the spread is stationary.

The null hypothesis is **no cointegration**; a small p-value rejects it. Both inputs are assumed to be I(1), and gaps or missing values are not handled.[^coint]

## Worked Example

Executed with statsmodels 0.15.0 and NumPy 2.4.6. `y` is built from `x` plus stationary noise; `z` is an independent random walk.

```python
import numpy as np
from statsmodels.tsa.stattools import coint

rng = np.random.default_rng(0)
n = 500
x = np.cumsum(rng.normal(size=n))           # random walk, I(1)
y = 2.0 * x + rng.normal(scale=1.0, size=n)  # tied to x by a stationary error
z = np.cumsum(rng.normal(size=n))           # independent random walk

t_stat, p_value, crit = coint(y, x)
print(f"y vs x: t={t_stat:.2f}, p={p_value:.4f}")  # y vs x: t=-21.62, p=0.0000
t_stat, p_value, crit = coint(z, x)
print(f"z vs x: t={t_stat:.2f}, p={p_value:.4f}")  # z vs x: t=-1.55, p=0.7407
print(f"corr(z, x) = {np.corrcoef(z, x)[0, 1]:.2f}")  # corr(z, x) = -0.58
```

The test rejects no-cointegration for `y` and `x`, as constructed. For `z` and `x` it does not reject, even though their correlation is -0.58: a sizeable correlation between two unrelated random walks, which is exactly the trap cointegration avoids.

## Pitfalls

- Check that each series is I(1) first, for example with an augmented Dickey–Fuller test.
- A relationship found in one period can break down later; re-test on fresh data before trading on it.
- The test depends on which series is the dependent variable when there are more than two, and on the trend specification.

## References & Useful Links

[^coint]: [statsmodels: `statsmodels.tsa.stattools.coint`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html) — Augmented Engle–Granger two-step test, null of no cointegration, I(1) assumption, trend options, and MacKinnon p-values.