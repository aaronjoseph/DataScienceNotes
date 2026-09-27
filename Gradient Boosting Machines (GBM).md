---
tags:
  - "search-eng"
  - "ds-foundations"
---

## Core Idea

Gradient boosting builds an additive predictor by fitting successive learners to a loss-improvement direction. “Fit the residuals” is exact for squared-error boosting, but is not the general rule for every objective.

At round m, pseudo-residuals are negative derivatives with respect to current predictions:

$$r_{im}=-\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{F=F_{m-1}}.$$

Fit a learner $h_m$ to this signal and update $F_m=F_{m-1}+\eta\gamma_mh_m$, where $\eta$ is a learning rate and $\gamma_m$ represents an appropriate step/leaf-value choice. For squared error, initialise at the training mean; other losses have different optimal constants.

In one sentence for an interview: *gradient boosting is gradient descent in function space: each tree approximates the negative gradient of the loss at the current predictions, and a small step is taken in that direction.*[^sk-gb]

## The Math, Step by Step

This is Friedman's (2001) gradient tree boosting, which scikit-learn's `GradientBoostingRegressor` and `GradientBoostingClassifier` implement.[^sk-gb]

### 1. Initial constant

$$
F_0(x) = \arg\min_{c} \sum_{i=1}^{n} L(y_i, c)
$$

### 2. Pseudo-residuals at round $m$

$$
r_{im} = -\left. \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right|_{F = F_{m-1}}
$$

### 3. Fit a regression tree

Fit a regression tree with $J$ leaves to the targets $r_{im}$, giving leaf regions $R_{1m}, \ldots, R_{Jm}$. The tree is fitted with squared error regardless of the original loss; see [[Decision Tree Regressor]].

### 4. Optimal value in each leaf

$$
\gamma_{jm} = \arg\min_{\gamma} \sum_{x_i \in R_{jm}} L\big(y_i,\ F_{m-1}(x_i) + \gamma\big)
$$

This per-leaf line search replaces the tree's own leaf means, so the step suits the actual loss.

### 5. Shrunken update

$$
F_m(x) = F_{m-1}(x) + \nu \sum_{j=1}^{J} \gamma_{jm}\, \mathbf{1}(x \in R_{jm})
$$

The learning rate $\nu$ (`learning_rate`) scales each tree; smaller values need more trees and, empirically, often give better test error.[^sk-gb]

### 6. The common losses

| Loss | Pseudo-residual $r_i$ | $F_0$ | Leaf value $\gamma_j$ |
|---|---|---|---|
| Squared error $\frac{1}{2}(y - F)^2$ | $y_i - F(x_i)$ | Mean of $y$ | Mean residual in the leaf |
| Absolute error $\lvert y - F\rvert$ | $\operatorname{sign}(y_i - F(x_i))$ | Median of $y$ | Median residual in the leaf |
| Log loss, $F$ = log-odds, $p = \sigma(F)$ | $y_i - p_i$ | $\ln \frac{\bar{y}}{1 - \bar{y}}$ | $\frac{\sum r_i}{\sum p_i (1 - p_i)}$ (one Newton step) |

For squared error, the pseudo-residuals are the ordinary residuals, so "fit the residuals" is exact. For absolute error, any value between the two middle residuals minimises the leaf loss; scikit-learn 1.9.1 gave $F_0 = 10$ for $y = [1, 2, 3, 10, 11, 12, 40]$ and a leaf value of 1 (the lower middle value) for residuals $[0, 1, 2, 30]$. For log loss the leaf value has no closed form, so a single Newton step is used; that step is the same formula XGBoost uses with $\lambda = 0$ (see [[XGBoost#The Math, Step by Step|the XGBoost derivation]]).

### 7. First-order versus second-order boosting

Classic gradient boosting fits the tree to gradients only and then line-searches each leaf. XGBoost, LightGBM, and scikit-learn's `HistGradientBoosting*` estimators use second-order (Newton) information to choose splits and leaf values directly, which the scikit-learn guide notes avoids the separate line-search step.[^sk-gb]

## Worked Example

Using half squared error, targets `[1, 3]` and initial predictions `[2, 2]` give negative gradients `[-1, 1]`. If a learner fits them exactly, a learning rate of 0.1 produces `[1.9, 2.1]`. Ordinary squared residual error falls from 2 to 1.62; this training improvement does not prove better generalisation. scikit-learn 1.9.1 (`n_estimators=1`, `max_depth=1`, `learning_rate=0.1`) reproduced the initial value 2 and the predictions `[1.9, 2.1]`.

## Worked Example: Classification

**Inputs:** $x = [1, 2, 3, 4]$, labels $y = [0, 0, 1, 1]$, log loss, learning rate $\nu = 1$, one depth-one tree.

**Step 1: initial log-odds.** Half the labels are positive.

$$
F_0 = \ln \frac{0.5}{1 - 0.5} = 0, \qquad p_i = \sigma(0) = 0.5
$$

**Step 2: pseudo-residuals.**

$$
r = y - p = [-0.5,\ -0.5,\ 0.5,\ 0.5]
$$

**Step 3: tree.** The best split on the residuals is $x < 2.5$.

**Step 4: leaf values by one Newton step.**

$$
\gamma_{\text{left}} = \frac{-0.5 - 0.5}{0.25 + 0.25} = -2, \qquad \gamma_{\text{right}} = \frac{0.5 + 0.5}{0.25 + 0.25} = 2
$$

**Step 5: updated probabilities.**

$$
p_{\text{left}} = \sigma(-2) \approx 0.119, \qquad p_{\text{right}} = \sigma(2) \approx 0.881
$$

The tree is fitted to residuals of $\pm 0.5$, but the leaf values are $\pm 2$ in log-odds, because the Newton step divides by the curvature $p(1 - p) = 0.25$. Leaf values therefore live on the log-odds scale, not the residual scale. scikit-learn 1.9.1 gave an initial raw prediction of 0, leaf values of $\pm 2$, and probabilities of 0.119 and 0.881.

## Controls

scikit-learn `GradientBoostingClassifier` and `GradientBoostingRegressor`, checked with version 1.9.1:

| Parameter | Default | Role |
|---|---|---|
| `learning_rate` | 0.1 | Shrinkage $\nu$; trades off against `n_estimators` |
| `n_estimators` | 100 | Number of boosting rounds $M$ |
| `max_depth` | 3 | Tree size; a depth-$h$ tree captures interactions of order $h$[^sk-gb] |
| `subsample` | 1.0 | Below 1.0 gives stochastic gradient boosting (rows drawn without replacement)[^sk-gb] |
| `n_iter_no_change` | `None` | Enables early stopping on a validation fraction |

## Implementations and Tradeoffs

[[XGBoost]] and [[Light GBM]] implement related boosting frameworks with specific objectives, regularisation, and algorithms. They are not universal successors that dominate every GBM setup. Successive rounds depend on earlier predictions even when work within a round is parallelised.

Tune learning rate, tree complexity, number of rounds, and validation-based stopping together. Regularisation reduces overfitting risk without guaranteeing its absence.

## Interview Questions

**Why are they called pseudo-residuals?** They equal the ordinary residuals only for squared error. For other losses they are negative gradients: the direction that most reduces the loss for each example.

**Why use shallow trees?** Each tree only needs to point roughly downhill; bias is reduced over many rounds. Shallow trees are cheaper and limit interaction order.

**Gradient boosting versus a random forest?** Boosting builds trees sequentially to reduce bias; a forest averages independent deep trees to reduce variance. See [[Random Forest]] and [[Boosting]].

**Gradient boosting versus AdaBoost?** [[AdaBoost]] is the special case with exponential loss; gradient boosting works with any differentiable loss.

**How do you stop overfitting?** Lower `learning_rate` with more trees, limit depth, subsample rows or features, and use validation-based early stopping.

## Search Exercise

Explain why applying a regression residual recipe to relevance grades is different from [[Learning to Rank|query-aware ranking]]. Keep query groups intact and compare held-out [[NDCG]].

## References & Useful Links

- [Scikit-learn gradient boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting) — Primary reference for the explanation above.

[^sk-gb]: [scikit-learn User Guide: Gradient-boosted trees](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosted-trees) — Generalisation to differentiable losses (Friedman, 2001), fitting to negative gradients, shrinkage, stochastic subsampling, tree size and interaction order, and Newton boosting in the histogram estimators.
