---
tags:
  - "finance"
---

The Sharpe ratio measures return per unit of risk: the average return in excess of a benchmark, usually the risk-free rate, divided by the standard deviation of that excess return. William Sharpe introduced it in 1966 as the "reward-to-variability ratio".[^sharpe]

## Formula

With $D_t = R_t - R_{f,t}$ the excess return in period $t$, $\bar{D}$ its average and $\sigma_D$ its standard deviation, the ex post (historical) ratio is:[^sharpe]

$$
\text{Sharpe} = \frac{\bar{D}}{\sigma_D}
$$

## Time Dependence and Annualisation

The ratio depends on the measurement period. If per-period excess returns are uncorrelated, the mean scales with the number of periods $T$ and the standard deviation with $\sqrt{T}$, so:[^sharpe]

$$
\text{Sharpe}_T = \sqrt{T} \times \text{Sharpe}_1
$$

For daily data, the usual convention is $T = 252$ trading days. Serial correlation and compounding make the relationship less exact.

## Worked Example

**Inputs:** Sharpe's illustration of the stock market: a mean annual excess return of 6% and a standard deviation of 15%.[^sharpe]

**Step 1: annual Sharpe ratio.**

$$
\frac{0.06}{0.15} = 0.40
$$

Each unit of volatility earned 0.4 units of excess return. Two funds can be compared this way, as long as their correlations with the rest of the portfolio are similar; the ratio itself ignores correlation.[^sharpe]

## Implementation

The earlier code subtracted an annual 5% risk-free rate from a daily mean return, annualised only the volatility, and called `.shift` on a Python list. This version fixes all three; it was run on a synthetic pandas price series.

```python
import numpy as np
import pandas as pd

def annualised_sharpe(close: pd.Series, annual_rf: float = 0.05, periods: int = 252) -> float:
    returns = np.log(close / close.shift(1)).dropna()      # daily log returns
    excess = returns - np.log(1 + annual_rf) / periods     # daily risk-free rate
    return np.sqrt(periods) * excess.mean() / excess.std()
```

## Pitfalls

- The ratio treats upside and downside volatility alike and assumes mean and standard deviation summarise risk.
- Historical Sharpe ratios are noisy estimates of future ones.
- The ratio is scale-independent, so leverage does not change it; see [[Risk Parity]].

## References & Useful Links

[^sharpe]: [Sharpe (1994), "The Sharpe Ratio", *Journal of Portfolio Management*](https://web.stanford.edu/~wfsharpe/art/sr/sr.htm) — Ex ante and ex post definitions, time dependence and annualisation, the 6% / 15% = 0.40 stock-market example, and the caution about correlations.