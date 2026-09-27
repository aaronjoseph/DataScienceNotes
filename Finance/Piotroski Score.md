---
tags:
  - "finance"
---

The Piotroski F-score is a 0–9 score built from nine yes/no signals in a company's financial statements. Joseph Piotroski designed it to separate likely winners from losers **among high book-to-market (value) stocks**, which are often financially weak.[^piotroski] A higher score means more good signals: 9 is the best, 0 the worst.

## The Nine Signals

Each signal scores 1 if the condition holds, 0 otherwise.[^piotroski]

**Profitability**

1. **ROA > 0.** Net income before extraordinary items, scaled by beginning-of-year total assets, is positive.
2. **CFO > 0.** Cash flow from operations, scaled by beginning total assets, is positive.
3. **ΔROA > 0.** ROA improved on the prior year.
4. **Accrual: CFO > ROA.** Operating cash flow exceeds earnings, a sign of earnings quality.

**Leverage, liquidity and source of funds**

5. **ΔLeverage < 0.** The ratio of long-term debt to average total assets fell.
6. **ΔLiquidity > 0.** The [[Current Ratio|current ratio]] improved.
7. **No equity issued.** The company did not issue common equity in the prior year.

**Operating efficiency**

8. **ΔMargin > 0.** The [[Gross Profit|gross margin]] improved.
9. **ΔTurnover > 0.** Asset turnover (sales over beginning total assets) improved; see [[Total Assets Turnover]].

The earlier version had "positive net income" and "positive ROA" as separate points, which is the same test, and it omitted signal 3, the improvement in ROA.

$$
\text{F-score} = \sum_{i=1}^{9} F_i, \qquad F_i \in \{0, 1\}
$$

## Worked Example

**Inputs:** a value stock whose latest year shows positive ROA and CFO, CFO above net income, a lower long-term debt ratio, a higher current ratio, no share issuance and a higher gross margin, but lower ROA and lower asset turnover than the year before.

**Step 1: add the signals.**

$$
1 + 1 + 0 + 1 + 1 + 1 + 1 + 1 + 0 = 7
$$

A score of 7 falls in the high group (Piotroski treated 8–9 as high and 0–1 as low), so this stock would be a candidate for further analysis rather than a buy signal on its own.

## What the Paper Found

In US data from 1976 to 1996, choosing high-scoring firms within the high book-to-market portfolio raised the mean return by at least 7.5% a year, and a strategy buying expected winners and shorting expected losers earned 23% a year.[^piotroski] These are historical results for that universe and period, before trading costs. The score was not designed for, or tested on, growth stocks in that study.

## References & Useful Links

[^piotroski]: [Piotroski (2000), "Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers", *Journal of Accounting Research* 38 (Supplement)](https://www.ivey.uwo.ca/media/3775523/value_investing_the_use_of_historical_financial_statement_information.pdf) — Section 2 read: definitions of the nine signals and the composite F-score; abstract: the 7.5% and 23% return results for 1976–1996.