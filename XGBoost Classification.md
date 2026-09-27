---
tags:
  - "ds-foundations"
---

The only difference in classification is the similarity score formula. With log loss, each residual is $r_i = y_i - p_i$, where $p_i$ is the previous predicted probability, and the Hessian is $p_i(1 - p_i)$:

$$
\text{Similarity Score} = \frac{\left(\sum_i r_i\right)^2}{\sum_i \left[ p_i (1 - p_i) \right] + \lambda}
$$

As in [[XGBoost Regression]], the numerator is the square of the sum of residuals. The leaf output is

$$
\text{Output} = \frac{\sum_i r_i}{\sum_i p_i (1 - p_i) + \lambda},
$$

and it is added in **log-odds**, not probability:

$$
\log\text{-odds}_{\text{new}} = \log\text{-odds}_{\text{old}} + \eta \times \text{Output}, \qquad p_{\text{new}} = \frac{1}{1 + e^{-\log\text{-odds}_{\text{new}}}}
$$

## Worked Example

**Inputs:** labels $[1, 0, 1]$, previous probability 0.5 for all (log-odds 0), $\lambda = 0$, $\eta = 0.3$, one leaf.

**Step 1: residuals and Hessians.**

$$
r = [0.5,\ -0.5,\ 0.5], \qquad p(1 - p) = 0.25 \text{ each}
$$

**Step 2: output.**

$$
\frac{0.5}{0.75} \approx 0.667
$$

**Step 3: new probability.**

$$
0 + 0.3 \times 0.667 = 0.2, \qquad \sigma(0.2) \approx 0.550
$$

The denominator uses $p(1 - p)$ instead of the count of residuals, so confidently predicted rows (with $p$ near 0 or 1) count for little. This makes `min_child_weight`, which limits the Hessian sum in a leaf, behave differently from a row count. The full derivation and a library check of this example are in the classification worked example of [[XGBoost]].