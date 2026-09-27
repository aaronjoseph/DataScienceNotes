---
tags:
  - "finance"
---

Discounted cash flow (DCF) analysis values a business as the present value of the cash it is expected to generate. It is used to estimate [[Intrinsic Value & Margin of Safety|intrinsic value]] and to judge whether a stock looks overpriced or underpriced.

In the author's [[Stock Selection Methodology]], DCF is stage III, after reading the annual report (stage I) and passing the [[Stock Selection Checklist|selection checklist]] (stage II).

## Time Value of Money

Money available now is worth more than the same amount later, because it can be invested in the meantime. This is the central idea behind DCF.

**Future value** compounds today's amount forward at the opportunity-cost rate $r$ for $n$ years:

$$
\text{FV} = \text{PV} \times (1 + r)^n
$$

**Present value** discounts a future amount back to today:

$$
\text{PV} = \frac{\text{FV}}{(1 + r)^n}
$$

A series of cash flows $\text{CF}_t$ is worth the sum of their present values:

$$
\text{PV} = \sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + r)^t}
$$

## Worked Example

**Inputs:** 100 today and a 10% opportunity cost.

**Step 1: value in three years.**

$$
100 \times 1.1^3 = 133.1
$$

**Step 2: discount it back.**

$$
\frac{133.1}{1.1^3} = 100
$$

Compounding and discounting are inverses: 133.1 received in three years is worth exactly 100 today to someone who can earn 10%.

## Techniques

- [[Discounted Cash Flow - Method 1]] — owner earnings discounted at 15%, with a simple terminal multiple.
- [[Free Cash Flow (FCF) - DCF Method]] — two-stage growth, a Gordon-growth terminal value, and a per-share value.

## Pitfalls

- Small changes in the discount rate or the terminal growth rate change the result a lot, especially when most of the value sits in the terminal value.
- Forecasts far into the future are guesses; this is why a [[Intrinsic Value & Margin of Safety|margin of safety]] is applied.