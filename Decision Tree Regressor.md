---
tags:
  - "ds-foundations"
---

## Overview

A [[Decision Trees|decision tree]] used for regression is called a regression tree. Instead of a class in each leaf, it stores a **number**: the mean of the training targets in that leaf (for squared error). The tree is a piecewise-constant function, so it cannot extrapolate beyond the range of the training targets.[^sk-tree]

## How a Split Is Chosen

The original steps in this note describe the procedure well:

1. Identify the target variable.
2. Sort the samples by a candidate feature.
3. Try each threshold between consecutive distinct values, sending samples to a left and a right node.
   1. The output of the left node is the average target in it.
   2. The output of the right node is the average target in it.
   3. Measure the squared error of both nodes around their means.
4. Keep the threshold, over all features, with the lowest total squared error.
5. Repeat recursively in each child until a stopping rule is met (depth, minimum samples, or no improvement).

## The Math, Step by Step

### 1. Leaf prediction

For the $n_m$ samples $Q_m$ in node $m$, the squared-error prediction is the node mean:[^sk-tree]

$$
\bar{y}_m = \frac{1}{n_m} \sum_{y \in Q_m} y
$$

The mean is the constant that minimises squared error. With absolute error the best constant is the median instead.

### 2. Node impurity (MSE)

$$
H(Q_m) = \frac{1}{n_m} \sum_{y \in Q_m} (y - \bar{y}_m)^2
$$

### 3. Split objective

A candidate split $\theta = (j, t)$ sends $x_j \le t$ left. Its quality is the size-weighted impurity of the children:[^sk-tree]

$$
G(Q_m, \theta) = \frac{n_{\text{left}}}{n_m} H(Q_{\text{left}}) + \frac{n_{\text{right}}}{n_m} H(Q_{\text{right}})
$$

Choose $\theta^{*} = \arg\min_\theta G(Q_m, \theta)$. Multiplying by $n_m$ shows this is the same as minimising the total sum of squared errors (SSE) of the two children, which is why the method is also described as "reduction in variance".

### 4. Other criteria

scikit-learn also offers `absolute_error` (median leaves, more robust to outliers but slower) and `poisson` (for non-negative counts).[^sk-tree] Older versions also had `friedman_mse` as the default criterion inside gradient-boosting trees; in scikit-learn 1.9.1, `GradientBoostingRegressor().criterion` reports `"deprecated"`, and both its internal trees and `DecisionTreeRegressor(criterion="friedman_mse")` ended up with `squared_error`.

## Worked Example

**Inputs:** one feature $x = [1, 2, 3, 4, 5]$ with targets $y = [5, 6, 7, 20, 22]$.

**Step 1: root.** The mean is 12.

$$
\text{SSE}_{\text{root}} = 7^2 + 6^2 + 5^2 + 8^2 + 10^2 = 274
$$

**Step 2: threshold 2.5.** Left $\{5, 6\}$ has mean 5.5; right $\{7, 20, 22\}$ has mean 16.33.

$$
\text{SSE} = 0.5 + 132.67 = 133.17
$$

**Step 3: threshold 3.5.** Left $\{5, 6, 7\}$ has mean 6; right $\{20, 22\}$ has mean 21.

$$
\text{SSE} = (1 + 0 + 1) + (1 + 1) = 4
$$

**Step 4: the other thresholds.** Threshold 1.5 gives 212.75 and threshold 4.5 gives 149.

**Step 5: weighted MSE of the best split**, the quantity scikit-learn reports.

$$
G = \frac{3}{5} \times \frac{2}{3} + \frac{2}{5} \times 1 = 0.8
$$

The split at 3.5 separates the two target clusters and cuts the error from 274 to 4. The tree predicts 6 for $x \le 3.5$ and 21 above it. scikit-learn 1.9.1 with `max_depth=1` chose threshold 3.5 with leaf values 6 and 21. For an input of $x = 100$ the prediction is still 21: the tree cannot extrapolate.

## Python Example

Executed with scikit-learn 1.9.1.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([5, 6, 7, 20, 22], dtype=float)

tree = DecisionTreeRegressor(max_depth=1).fit(X, y)
print(tree.tree_.threshold[0])      # 3.5
print(tree.tree_.value.ravel())      # [12.  6. 21.]  root, left, right
print(tree.predict([[100.0]]))       # [21.]
```

## Limitations & Common Pitfalls

- **Step-shaped predictions.** A smooth trend becomes a staircase, and predictions outside the training range are flat.
- **Overfitting.** A fully grown tree puts every sample in its own leaf. Limit `max_depth`, raise `min_samples_leaf`, or prune; see [[Decision Tree - Pruning]].
- **Outliers.** Squared error lets one extreme target pull a leaf mean; `absolute_error` is more robust.
- **High variance.** Small data changes can move the chosen thresholds. Averaging many trees in a [[Random Forest]] or boosting shallow ones in [[Gradient Boosting Machines (GBM)|gradient boosting]] reduces this.

## Interview Questions

**Why is the leaf value the mean?** It minimises the sum of squared errors of a constant prediction. Setting the derivative to zero gives the mean:

$$
\frac{d}{dc} \sum_i (y_i - c)^2 = -2 \sum_i (y_i - c) = 0 \;\Rightarrow\; c = \bar{y}
$$

**How is this related to gradient boosting?** Each boosting round fits a regression tree like this one to the current residuals (for squared error) or pseudo-residuals (for other losses).

**Why can't a regression tree extrapolate?** Every prediction is the mean of some training targets, so it lies within the training target range.

## Exercise

With the same data, which threshold would `absolute_error` choose, and what are the leaf predictions?

> [!example]- Exercise solution
> **Inputs:** threshold 3.5, leaves $\{5, 6, 7\}$ and $\{20, 22\}$, absolute error.
>
> **Step 1: leaf predictions (medians).** 6 for the left leaf and 21 for the right. Any value between 20 and 22 minimises absolute error there; the median convention gives 21.
>
> **Step 2: total absolute error.**
>
> $$
> (1 + 0 + 1) + (1 + 1) = 4
> $$
>
> Threshold 3.5 still separates the clusters, and its total absolute error is lower than that of any other threshold.

## References & Useful Links

[^sk-tree]: [scikit-learn User Guide: Decision Trees — Mathematical formulation](https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation) — Split objective, regression criteria (MSE, Poisson, MAE), leaf predictions, and piecewise-constant behaviour.



