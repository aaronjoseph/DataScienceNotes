---
tags:
  - "finance"
---

Financial accounting produces and communicates financial information for **external users** (investors, lenders, regulators) so that they can make decisions about the organisation. Management accounting, by contrast, serves internal decision-makers.

Course notes from MGT 8803; the lecture slides are linked in each section.

## Standards and Oversight

Lecture slides: [[Week 1- Introduction to Financial Accounting.pdf]]

- **GAAP (Generally Accepted Accounting Principles):** the US rules for preparing financial statements.
- **FASB (Financial Accounting Standards Board):** an independent, private-sector, not-for-profit body, established in 1973, that sets GAAP for public and private companies and not-for-profit organisations. The **SEC (Securities and Exchange Commission)** recognises it as the designated accounting standard setter for public companies.[^fasb]
- **CPAs (Certified Public Accountants):** as independent auditors, they audit a company's financial statements and issue an audit report with their opinion on whether the statements are fairly presented under GAAP. The earlier wording said CPAs review and verify audit reports; they write them.

## The Financial Statements

1. [[Balance Sheet]] — assets, liabilities and equity at a point in time.
2. [[P&L Statement|Income statement]] — revenue, expenses and profit over a period.
3. **Statement of shareholders' equity** — reconciles the beginning and ending balances of each equity account (share capital, retained earnings and others). See [[Shareholder Equity]].
4. [[Cash Flow Statement]] — cash from operating, investing and financing activities over a period.

How the statements connect (see also [[Connecting P&L and Balance Sheet & Cash Flow]]):

![[Relation Between Cash Flow, Income Statement & Balance Sheet]]

## Classification and Measurement

Lecture slides: [[Week 2- Classification and Measurement.pdf]]

TODO: summarise the week 2 slides; the PDF has not been read into this note.

## Comparing Capital Budgeting Methods

These rules decide whether to accept an investment project. Notation: $C_0$ is the initial investment, $CF_t$ the cash flow in year $t$, $n$ the project life and $k$ the cost of capital.

| Method | Inputs | Accept if | Adjusts for time? | Adjusts for risk? |
|---|---|---|---|---|
| Net present value (NPV) | Cash flows, $k$ | NPV > 0 | Yes | Yes |
| Profitability index (PI) | Cash flows, $k$ | PI > 1 | Yes | Yes |
| Internal rate of return (IRR) | Cash flows, $k$ | IRR > k | Yes | Yes |
| Payback period (PP) | Cash flows, cutoff period | PP < cutoff | No | No |

Is each rule consistent with maximising the firm's equity value?

- **NPV:** yes; NPV measures the value the project creates or destroys.
- **PI:** yes, but it may fail to pick the highest-NPV project when projects are mutually exclusive.
- **IRR:** yes, but it may fail when projects are mutually exclusive or when cash flows change sign more than once.
- **Payback:** no.

The discounted payback period adjusts for time and risk, but still ignores cash flows after the investment is paid back.

### Formulas

**Net present value.**

$$
\text{NPV} = \sum_{t=1}^{n} \frac{CF_t}{(1 + k)^t} - C_0
$$

**Profitability index.**

$$
\text{PI} = \frac{\text{PV of future cash flows}}{C_0}
$$

**Internal rate of return:** the rate $r$ that makes NPV zero.

$$
\sum_{t=1}^{n} \frac{CF_t}{(1 + r)^t} - C_0 = 0
$$

**Payback period:** the time until cumulative undiscounted cash flows equal $C_0$.

### Worked Example

**Inputs:** $C_0 = 1{,}000$, cash flows of 600 in each of years 1 and 2, $k = 10\%$, and a payback cutoff of 2 years.

**Step 1: present value of the cash flows.**

$$
\frac{600}{1.1} + \frac{600}{1.1^2} = 545.45 + 495.87 = 1{,}041.32
$$

**Step 2: NPV.**

$$
1{,}041.32 - 1{,}000 = 41.32
$$

**Step 3: PI.**

$$
\frac{1{,}041.32}{1{,}000} \approx 1.04
$$

**Step 4: IRR.** Solve for $r$:

$$
\frac{600}{1 + r} + \frac{600}{(1 + r)^2} = 1{,}000 \quad \Rightarrow \quad r \approx 13.1\%
$$

**Step 5: payback period.**

$$
\frac{1{,}000}{600} \approx 1.67 \text{ years}
$$

All four rules accept the project: NPV is positive, PI exceeds 1, the IRR of 13.1% exceeds the 10% cost of capital, and payback is inside the 2-year cutoff. They agree here because this is a single, conventional project; they can disagree when choosing between mutually exclusive projects.

See [[Discounted Cash Flow (DCF)]] for discounting applied to company valuation.

## References & Useful Links

[^fasb]: [FASB: About the FASB](https://www.fasb.org/about-us/about-the-fasb) — FASB's founding in 1973, its independence, its role in setting GAAP, and SEC recognition as the designated standard setter for public companies.
