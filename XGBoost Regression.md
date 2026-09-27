---
tags:
  - "ds-foundations"
---

The tree that XGBoost uses is different from a regular decision tree: splits and leaf values come from the loss's gradients and Hessians, not from an impurity measure. This note uses the common "similarity score" teaching convention; the general derivation is in [[XGBoost#The Math, Step by Step|XGBoost]].

For squared error, each residual is $r_i = y_i - \hat{y}_i$ and each Hessian is 1, so

$$
\text{Similarity Score} = \frac{\left(\sum_{i} r_i\right)^2}{n + \lambda}.
$$

The numerator is the **square of the sum** of residuals, not the sum of squared residuals: residuals of opposite sign cancel, so a leaf mixing high and low targets scores low. $n$ is the number of residuals in the node.

$\lambda$ is a regularization parameter (`lambda`, default 1). It shrinks similarity scores and leaf outputs, and has the largest effect on nodes with few residuals.

$$
\text{Gain} = \text{Similarity}_{\text{Left}} + \text{Similarity}_{\text{Right}} - \text{Similarity}_{\text{Root}}
$$

The split for XGBoost tree happens for the combination that has the highest Gain.

The output value of a leaf is the regularised mean residual:

$$
\text{Output} = \frac{\sum_{i} r_i}{n + \lambda}
$$

### Prunning

Prunning is done by considering the Gain Value and $\gamma$ (`gamma`, default 0).

When Gain Value - $\gamma$ < 0, the branch is removed else not removed. This Gain has no factor of ½, which matches what XGBoost 3.0.5 reported and compared with `gamma` in a check recorded in the regression worked example of [[XGBoost]].

$$
\text{New Prediction} = \text{Previous Prediction} + \eta \times \text{Output}
$$

The learning rate is the parameter `eta`, which can take values in $[0, 1]$; its default value is 0.3.[^params]

## Worked Example

**Inputs:** residuals $[-3, -2, 2, 3]$ from a starting prediction of 4 (targets $[1, 2, 6, 7]$), $\lambda = 1$, $\eta = 0.3$, candidate split between the second and third rows.

**Step 1: root similarity.**

$$
\frac{(-3 - 2 + 2 + 3)^2}{4 + 1} = 0
$$

**Step 2: left and right similarities.**

$$
\frac{(-5)^2}{2 + 1} \approx 8.33, \qquad \frac{5^2}{2 + 1} \approx 8.33
$$

**Step 3: gain.**

$$
8.33 + 8.33 - 0 \approx 16.67
$$

**Step 4: outputs and new predictions.**

$$
\text{Output}_L = \frac{-5}{3} \approx -1.67, \qquad 4 + 0.3 \times (-1.67) = 3.5
$$

The root scores 0 because its residuals cancel; splitting separates them and the gain of 16.67 would survive any $\gamma$ below 16.67. These are the same numbers as the library-checked example in [[XGBoost]].

## References & Useful Links

[^params]: [XGBoost parameters](https://xgboost.readthedocs.io/en/stable/parameter.html) — `eta` range and default, `lambda`, and `gamma` (`min_split_loss`).

