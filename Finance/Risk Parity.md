---
tags:
  - "finance"
---

Risk parity is a portfolio allocation approach that sizes positions so that each asset class contributes a similar share of the portfolio's **risk**, instead of a similar share of its capital. In a traditional 60/40 portfolio, most of the risk comes from equities because they are far more volatile than bonds; risk parity gives low-volatility assets a bigger weight to balance this.

It is used by hedge funds and institutional investors. Because the resulting portfolio has low overall volatility, managers often apply leverage to reach a target risk level, and some implementations also allow short positions.

## Simplest Version: Inverse-Volatility Weights

If assets are uncorrelated, equal risk contributions are achieved by weighting each asset in inverse proportion to its volatility $\sigma_i$:

$$
w_i = \frac{1 / \sigma_i}{\sum_j 1 / \sigma_j}
$$

With correlations, the weights are found numerically so that each asset's contribution to portfolio variance is equal.

## Worked Example

**Inputs:** stocks with 15% volatility and bonds with 5% volatility, assumed uncorrelated; a target portfolio volatility of 10%.

**Step 1: inverse volatilities.**

$$
\frac{1}{0.15} \approx 6.67, \qquad \frac{1}{0.05} = 20
$$

**Step 2: weights.**

$$
w_{\text{stocks}} = \frac{6.67}{26.67} = 25\%, \qquad w_{\text{bonds}} = \frac{20}{26.67} = 75\%
$$

**Step 3: risk contributions.**

$$
0.25 \times 15\% = 3.75\%, \qquad 0.75 \times 5\% = 3.75\%
$$

**Step 4: portfolio volatility** (uncorrelated assets).

$$
\sqrt{0.0375^2 + 0.0375^2} \approx 5.3\%
$$

**Step 5: leverage to reach the 10% target.**

$$
\frac{10\%}{5.3\%} \approx 1.89
$$

Each asset now contributes the same risk, but the unlevered portfolio is much less volatile than stocks alone, so reaching 10% needs about 1.9 times leverage. That leverage, and its borrowing cost, is the main practical risk of the approach.

## Pitfalls

- Volatilities and correlations change, especially in crises when correlations can rise together.
- Heavy bond weights are vulnerable when interest rates rise sharply.
- Leverage adds financing costs and the risk of forced selling.

## Related Notes

- [[Sharpe Ratio]] — risk-adjusted return.
- [[Investing Strategies]] — the author's own allocation framework.