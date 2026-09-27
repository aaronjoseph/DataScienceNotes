---
tags:
  - "finance"
---

The free cash flow method values a company from the cash left after operating expenses and capital spending, projected forward and discounted to today. It is one of the two techniques in [[Discounted Cash Flow (DCF)]]. The example below is in Indian rupees, in crores (1 crore = 10 million).

## Free Cash Flow

$$
\text{FCF} = \text{Cash from operating activities} - \text{Capital expenditures}
$$

See [[Free Cash Flow]] and [[Capital Expenditure]].

## Steps

1. **Base FCF.** Estimate the company's recent average free cash flow.
2. **Growth rates.** The author's defaults: for smaller companies, 18% for the first 5 years; for larger companies, 15% for the first 5 years and 10% for the next 5. Be conservative with growth.
3. **Project** FCF for 10 years.
4. **Terminal value** for all years after year 10.
5. **Discount** everything to today and add it up.
6. **Per-share value** after adjusting for net debt.

## Terminal Value

The terminal growth rate $g$ is the rate at which FCF is assumed to grow forever after year 10. With discount rate $r > g$, the Gordon growth formula gives the value at year 10 of all later cash flows:

$$
\text{TV}_{10} = \frac{\text{FCF}_{10} \times (1 + g)}{r - g}
$$

Keep $g$ low, below 5%, and never above the long-run growth of the economy.

## Worked Example

**Inputs:** base FCF of 100 crore, growing 18% a year for years 1–5 and 10% a year for years 6–10; discount rate $r = 9\%$; terminal growth $g = 3.5\%$.

| Year | Growth | FCF (₹ Cr) | Present value at 9% |
|---|---|---|---|
| 1 | 18% | 118.00 | 108.26 |
| 2 | 18% | 139.24 | 117.20 |
| 3 | 18% | 164.30 | 126.87 |
| 4 | 18% | 193.88 | 137.35 |
| 5 | 18% | 228.78 | 148.69 |
| 6 | 10% | 251.65 | 150.05 |
| 7 | 10% | 276.82 | 151.43 |
| 8 | 10% | 304.50 | 152.82 |
| 9 | 10% | 334.95 | 154.22 |
| 10 | 10% | 368.45 | 155.64 |

**Step 1: present value of year 1.**

$$
\frac{118}{1.09} = 108.26
$$

**Step 2: sum of the ten present values.**

$$
108.26 + 117.20 + \dots + 155.64 = 1{,}402.52
$$

**Step 3: terminal value at year 10.**

$$
\frac{368.45 \times 1.035}{0.09 - 0.035} = 6{,}933.48
$$

**Step 4: present value of the terminal value.**

$$
\frac{6{,}933.48}{1.09^{10}} = 2{,}928.78
$$

**Step 5: enterprise value.**

$$
1{,}402.52 + 2{,}928.78 = 4{,}331.29
$$

About two-thirds of the value comes from the terminal value, so the result is very sensitive to $g$ and $r$. The earlier version's figures differed slightly because of rounding; it also swapped the labels of the two present values. Recalculated in Python.

## Share Price

Free cash flow to the firm belongs to lenders as well as shareholders, so subtract net debt before dividing by the share count:

$$
\text{Net debt} = \text{Total debt} - \text{Cash and cash equivalents}
$$

$$
\text{Value per share} = \frac{\text{Enterprise value} - \text{Net debt}}{\text{Number of shares}}
$$

The earlier version said net debt "needs to be added"; it must be subtracted, as in the formula it then gave.

**Step 6: illustrative per-share value.** Assume total debt of 500 crore, cash of 200 crore and 50 crore shares.

$$
\frac{4{,}331.29 - (500 - 200)}{50} = 80.63
$$

**Author's rule:** allow a ±10% band for inaccuracy, here roughly 72.6 to 88.7. A market price below the band suggests the stock is undervalued; above it, overvalued. See [[Intrinsic Value & Margin of Safety]].