---
tags:
  - "ds-foundations"
---

## Overview

Decision trees tend to overfit: grown to full depth, they memorise noise and have high variance. **Pruning** removes branches that add complexity without enough improvement in fit.

- **Pre-pruning** (early stopping) limits growth up front: `max_depth`, `min_samples_split`, `min_samples_leaf`, `min_impurity_decrease`.
- **Post-pruning** grows the full tree and then cuts it back. scikit-learn implements *minimal cost-complexity pruning* (also called weakest-link pruning), from Breiman et al.'s CART book.[^sk-prune]

## Cost-Complexity Pruning

The original steps in this note, stated for regression with the sum of squared residuals (SSR):

- After the tree is grown, compute its SSR: the squared differences between training targets and predictions.
- Compute the SSR again for the tree with one fewer leaf, and so on down to the root. Pruned trees fit the training data worse, so their SSR is higher.
- Score every candidate tree by **SSR + $\alpha T$**, where $T$ is the number of leaves and $\alpha T$ is the complexity penalty.
- The tree with the lowest score wins. $\alpha$ is a tuning parameter chosen by cross-validation.

## The Math, Step by Step

### 1. Cost-complexity measure

For a tree $T$ with $|\tilde{T}|$ leaves,[^sk-prune]

$$
R_\alpha(T) = R(T) + \alpha |\tilde{T}|
$$

$R(T)$ is traditionally the misclassification rate. scikit-learn uses the **total sample-weighted impurity of the leaves**:

$$
R(T) = \sum_{t \in \text{leaves}} \frac{n_t}{N} H(t)
$$

For squared error that is SSE divided by the total sample count $N$.

### 2. One node versus its branch

For an internal node $t$ with branch $T_t$ (the subtree rooted at $t$):

$$
R_\alpha(t) = R(t) + \alpha, \qquad R_\alpha(T_t) = R(T_t) + \alpha |\tilde{T}_t|
$$

The branch always fits better, $R(T_t) < R(t)$, but costs more leaves.

### 3. Effective alpha

Setting the two equal gives the $\alpha$ at which collapsing the branch into a leaf breaks even:

$$
\alpha_{\text{eff}}(t) = \frac{R(t) - R(T_t)}{|\tilde{T}_t| - 1}
$$

This is the improvement in fit **per extra leaf** that the branch buys.

### 4. Weakest-link pruning

Repeatedly collapse the internal node with the smallest $\alpha_{\text{eff}}$ (the weakest link), recomputing as you go. This produces a nested sequence of trees and the thresholds at which each appears; `cost_complexity_pruning_path` returns them. Fitting with `ccp_alpha` keeps pruning until every remaining node has $\alpha_{\text{eff}}$ greater than `ccp_alpha`.[^sk-prune]

## Worked Example

**Inputs:** $x = [1, 2, 3, 4, 5]$, $y = [5, 6, 7, 20, 22]$, squared error, $N = 5$. The full tree has five pure leaves, so $R(T) = 0$. See [[Decision Tree Regressor]] for how the first split at 3.5 is chosen. The internal nodes are the root, $L = \{5, 6, 7\}$, $R = \{20, 22\}$, and $L$'s child $\{6, 7\}$.

**Step 1: effective alpha of each internal node** in the full tree.

$$
\{6, 7\}: \ \frac{0.5/5 - 0}{2 - 1} = 0.1
$$

$$
L: \ \frac{2/5 - 0}{3 - 1} = 0.2, \qquad R: \ \frac{2/5 - 0}{2 - 1} = 0.4
$$

$$
\text{root}: \ \frac{274/5 - 0}{5 - 1} = 13.7
$$

**Step 2: prune the weakest link, $\{6, 7\}$, at $\alpha = 0.1$.** Now $L$ has two leaves with $R(T_L) = 0.1$.

$$
L: \ \frac{0.4 - 0.1}{2 - 1} = 0.3
$$

**Step 3: prune $L$ at $\alpha = 0.3$, then $R$ at $\alpha = 0.4$.** The tree is now the single split at 3.5, with $R(T) = 4/5 = 0.8$.

**Step 4: last internal node, the root.**

$$
\text{root}: \ \frac{54.8 - 0.8}{2 - 1} = 54
$$

The pruning path is $\alpha = [0, 0.1, 0.3, 0.4, 54]$ with 5, 4, 3, 2, and 1 leaves. Any `ccp_alpha` between 0.4 and 54 keeps the sensible two-leaf tree. Notice that $L$'s first estimate (0.2) rose to 0.3 after its child was pruned, which is why the values must be recomputed. scikit-learn 1.9.1 returned exactly this path.

## Python Example

Executed with scikit-learn 1.9.1. The original note's loop is kept; choose $\alpha$ with cross-validation or a validation set, not training error.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([5, 6, 7, 20, 22], dtype=float)

path = DecisionTreeRegressor(random_state=0).cost_complexity_pruning_path(X, y)
print(path.ccp_alphas)   # [ 0.   0.1  0.3  0.4 54. ]
print(path.impurities)   # [ 0.   0.1  0.4  0.8 54.8]

trees = []
for ccp_alpha in path.ccp_alphas:
    tree = DecisionTreeRegressor(random_state=0, ccp_alpha=ccp_alpha).fit(X, y)
    trees.append(tree)
print([t.get_n_leaves() for t in trees])  # [5, 4, 3, 2, 1]
```

For a classifier, replace the regressor with `DecisionTreeClassifier`; the path is then built from Gini or entropy impurity.

## Limitations & Common Pitfalls

- **Choosing $\alpha$ on training data** always selects $\alpha = 0$ (the full tree). Use held-out data; see [[Cross Validation]].
- **Pre-pruning can stop too early.** A split with little gain can enable a very useful split below it (the XOR pattern); post-pruning avoids this because it sees the full tree first.
- **Ensembles rarely need it.** [[Random Forest]] relies on averaging deep trees, and boosting uses shallow trees with other controls.

## Interview Questions

**What does $\alpha$ trade off?** Training fit against tree size: each extra leaf must reduce the weighted impurity by at least $\alpha$.

**Why is the result a sequence of nested trees?** Each step removes the branch with the smallest improvement per leaf, so every larger $\alpha$ gives a subtree of the previous one.

**Pre- versus post-pruning?** Pre-pruning is cheaper but greedy; post-pruning costs a full tree but can keep a weak split whose children are strong.

## Exercise

In the worked example, which tree does `ccp_alpha=0.35` produce, and what are its predictions?

> [!example]- Exercise solution
> $0.35$ lies between 0.3 and 0.4, so nodes with $\alpha_{\text{eff}}$ of 0.1 and 0.3 are pruned while $R$ (0.4) survives. The tree has three leaves: $x \le 3.5$ predicts 6, and the right branch still separates 20 and 22. Predictions are $[6, 6, 6, 20, 22]$, matching scikit-learn 1.9.1's output with `ccp_alpha=0.35`.

## References & Useful Links

[^sk-prune]: [scikit-learn User Guide: Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning) — $R_\alpha(T)$, sample-weighted impurity, effective alpha, weakest link, and `ccp_alpha`; cites Breiman, Friedman, Olshen and Stone, *Classification and Regression Trees* (1984).
