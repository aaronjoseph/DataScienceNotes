---
tags:
  - "search-eng"
  - "ds-foundations"
---
## Core Idea

XGBoost builds an additive model through successive boosting rounds. Gradient and curvature information guide tree construction for supported objectives. Rounds depend on the current model, even though work inside a round can be parallelised. This differs from treating all trees as independent in a random forest.

In one sentence for an interview: *each new tree is chosen to minimise a second-order Taylor approximation of the regularised loss, which gives closed-form leaf values and a closed-form split score computed only from per-example gradients $g_i$ and Hessians $h_i$.* The derivation below shows where every formula comes from.

## The Math, Step by Step

### 1. Model

The prediction for example $i$ is a sum of $K$ regression trees:[^paper]

$$
\hat{y}_i = \sum_{k=1}^{K} f_k(x_i), \qquad f_k \in \mathcal{F}
$$

A tree is written $f(x) = w_{q(x)}$, where $q$ maps an example to one of $T$ leaves and $w \in \mathbb{R}^T$ holds the leaf scores. Each leaf outputs a real number, even for classification; the loss decides how that number is interpreted (a value, a log-odds, or a ranking score).

### 2. Regularised objective

$$
\mathcal{L} = \sum_{i=1}^{n} l(y_i, \hat{y}_i) + \sum_{k=1}^{K} \Omega(f_k), \qquad \Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^{T} w_j^2
$$

- $l$: a differentiable convex loss, such as squared error or log loss.
- $\gamma$: a penalty per leaf, which discourages extra splits.
- $\lambda$: an L2 penalty on leaf scores, which shrinks them towards zero.

With $\gamma = \lambda = 0$, the objective falls back to ordinary gradient tree boosting.[^paper]

### 3. Additive training

Trees cannot all be optimised at once, so XGBoost fixes the first $t-1$ trees and adds one tree $f_t$:

$$
\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + f_t(x_i)
$$

$$
\mathcal{L}^{(t)} = \sum_{i=1}^{n} l\left(y_i,\ \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t)
$$

### 4. Second-order Taylor expansion

Expand the loss around the current prediction $\hat{y}_i^{(t-1)}$:

$$
\mathcal{L}^{(t)} \approx \sum_{i=1}^{n} \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t(x_i)^2 \right] + \Omega(f_t)
$$

where the gradient and Hessian of the loss with respect to the current prediction are

$$
g_i = \frac{\partial\, l(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)}}, \qquad h_i = \frac{\partial^2 l(y_i, \hat{y}_i^{(t-1)})}{\partial \left(\hat{y}_i^{(t-1)}\right)^2}.
$$

The first term inside the sum is constant with respect to $f_t$, so it can be dropped. The new tree depends on the data only through $g_i$ and $h_i$. This is why one tree-building algorithm serves regression, classification, ranking, and custom losses: an objective only has to supply $g_i$ and $h_i$.[^model]

### 5. Group examples by leaf

All examples in leaf $j$ receive the same score $w_j$. Let $I_j = \{ i : q(x_i) = j \}$, and define the leaf totals

$$
G_j = \sum_{i \in I_j} g_i, \qquad H_j = \sum_{i \in I_j} h_i.
$$

Substituting $f_t(x_i) = w_j$ and expanding $\Omega$ turns the objective into a sum of independent quadratics, one per leaf:

$$
\tilde{\mathcal{L}}^{(t)} = \sum_{j=1}^{T} \left[ G_j w_j + \frac{1}{2}(H_j + \lambda) w_j^2 \right] + \gamma T
$$

### 6. Optimal leaf weight

For a fixed tree structure, set the derivative with respect to $w_j$ to zero:

$$
\frac{\partial \tilde{\mathcal{L}}^{(t)}}{\partial w_j} = G_j + (H_j + \lambda) w_j = 0
$$

$$
w_j^{*} = -\frac{G_j}{H_j + \lambda}
$$

This is a Newton step: gradient divided by curvature, with $\lambda$ added to the curvature. A larger $\lambda$ shrinks every leaf value towards zero. The minimum exists when $H_j + \lambda > 0$, which holds for convex losses.

### 7. Structure score

Substituting $w_j^{*}$ back gives the best achievable objective for that structure:

$$
\tilde{\mathcal{L}}^{(t)}(q) = -\frac{1}{2} \sum_{j=1}^{T} \frac{G_j^2}{H_j + \lambda} + \gamma T
$$

Lower is better. It plays the role that impurity plays in an ordinary decision tree, but it is derived from the loss being optimised.[^paper]

### 8. Split gain

Splitting a leaf with totals $(G, H)$ into left and right children, where $G = G_L + G_R$ and $H = H_L + H_R$, changes the structure score by

$$
\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma
$$

The three fractions are the scores of the new left leaf, the new right leaf, and the original leaf; $\gamma$ pays for the one extra leaf. A split is worth making only if the bracketed improvement exceeds $\gamma$, which is how pruning falls out of the objective.[^model]

> [!warning] The factor of ½ depends on the write-up
> The paper and documentation include the ½. In a check with XGBoost 3.0.5, the model dump reported the bracket **without** the ½ as `gain`, and `gamma` was compared with that value (see the worked example). The [[XGBoost Regression]] note's "similarity score" convention also omits it. Say which convention you use when quoting numbers.

### 9. Shrinkage

The new tree is added with a learning rate $\eta$ (`eta`):

$$
\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + \eta\, f_t(x_i)
$$

Shrinkage reduces each tree's influence and leaves room for later trees; column subsampling is XGBoost's other main extra guard against overfitting.[^paper]

### 10. Gradients and Hessians for common losses

**Squared error.** The loss is:

$$
l = \frac{1}{2}(y_i - \hat{y}_i)^2
$$

Its gradient and Hessian are:

$$
g_i = \hat{y}_i - y_i, \qquad h_i = 1
$$

So $G_j$ is minus the sum of residuals and $H_j$ is the number of examples in the leaf. The leaf weight becomes:

$$
w_j^{*} = \frac{\sum_{i \in I_j} (y_i - \hat{y}_i)}{n_j + \lambda}
$$

The leaf's term in the structure score is the "similarity score" in [[XGBoost Regression]]:

$$
\frac{G_j^2}{H_j + \lambda} = \frac{\left(\sum_{i \in I_j} (y_i - \hat{y}_i)\right)^2}{n_j + \lambda}
$$

The numerator is the square of the *sum* of residuals, not the sum of squared residuals. With $\lambda = 0$, the leaf value is just the mean residual.

**Log loss for binary classification.** Here $\hat{y}_i$ is the log-odds, and the predicted probability is:

$$
p_i = \sigma(\hat{y}_i) = \frac{1}{1 + e^{-\hat{y}_i}}
$$

The loss, gradient and Hessian are:

$$
l = -\left[ y_i \ln p_i + (1 - y_i)\ln(1 - p_i) \right]
$$

$$
g_i = p_i - y_i, \qquad h_i = p_i (1 - p_i)
$$

This gives the classification similarity score in [[XGBoost Classification]]:

$$
\frac{\left(\sum_{i \in I_j} (y_i - p_i)\right)^2}{\sum_{i \in I_j} p_i(1 - p_i) + \lambda}
$$

Leaf values are in log-odds, not probabilities. Confident predictions ($p_i$ near 0 or 1) have small $h_i$ and contribute little to $H_j$.

### 11. Why the Hessian acts as an example weight

Completing the square in the Step 4 objective gives

$$
\sum_{i=1}^{n} \frac{1}{2} h_i \left( f_t(x_i) + \frac{g_i}{h_i} \right)^2 + \Omega(f_t) + \text{constant},
$$

a weighted squared-error fit to the target $-g_i / h_i$ with weight $h_i$. This is why XGBoost's approximate split finding proposes candidate thresholds from quantiles weighted by $h_i$ (the *weighted quantile sketch*).[^paper] The paper writes the target as $g_i/h_i$; the minus sign here comes from expanding the square.

## Worked Example: One Regression Tree by Hand

**Inputs:**

- One feature $x = [1, 2, 3, 4]$ with targets $y = [1, 2, 6, 7]$.
- Squared error, starting prediction $\hat{y}^{(0)} = 4$ for every example (the mean).
- $\lambda = 1$, $\gamma = 0$, $\eta = 0.3$, depth-one tree.

**Step 1: gradients and Hessians.**

$$
g = \hat{y} - y = [3,\ 2,\ -2,\ -3], \qquad h = [1,\ 1,\ 1,\ 1]
$$

**Step 2: root score.** $G = 0$ and $H = 4$.

$$
\frac{G^2}{H + \lambda} = \frac{0^2}{4 + 1} = 0
$$

**Step 3: candidate split $x < 1.5$.** Left $\{1\}$: $G_L = 3$, $H_L = 1$. Right $\{2, 3, 4\}$: $G_R = -3$, $H_R = 3$.

$$
\text{Gain} = \frac{1}{2}\left[ \frac{3^2}{1 + 1} + \frac{(-3)^2}{3 + 1} - 0 \right] = \frac{1}{2}(4.5 + 2.25) = 3.375
$$

**Step 4: candidate split $x < 2.5$.** Left $\{1, 2\}$: $G_L = 5$, $H_L = 2$. Right $\{3, 4\}$: $G_R = -5$, $H_R = 2$.

$$
\text{Gain} = \frac{1}{2}\left[ \frac{5^2}{2 + 1} + \frac{(-5)^2}{2 + 1} - 0 \right] = \frac{1}{2}(8.333 + 8.333) = 8.333
$$

**Step 5: candidate split $x < 3.5$.** By symmetry with Step 3:

$$
\text{Gain} = 3.375
$$

**Step 6: leaf weights for the best split, $x < 2.5$.**

$$
w_L^{*} = -\frac{5}{2 + 1} \approx -1.667, \qquad w_R^{*} = -\frac{-5}{2 + 1} \approx 1.667
$$

**Step 7: updated predictions with shrinkage.**

$$
\hat{y}_L^{(1)} = 4 + 0.3 \times (-1.667) = 3.5, \qquad \hat{y}_R^{(1)} = 4 + 0.3 \times 1.667 = 4.5
$$

The split at 2.5 separates the low and high targets, so it has the largest gain. Without regularisation, the left leaf would be the mean residual, $-2.5$; $\lambda = 1$ shrinks it to $-1.667$, and $\eta = 0.3$ shrinks the step again. Predictions move only part of the way towards the targets; later trees continue the work.

**Check against the library.** XGBoost 3.0.5 (`tree_method="exact"`, `base_score=4`, `max_depth=1`) chose the same split and predicted `[3.5, 3.5, 4.5, 4.5]`. Its dump showed `gain=16.67`, which is the bracket without the ½, `cover=2` per leaf (the Hessian sum $H_j$), and leaf values $\pm 0.5$ (the weights already multiplied by $\eta$). With `gamma=9` the split was kept, and with `gamma=17` it was pruned. That confirms $\gamma$ is compared with the un-halved 16.67 in this version.

## Worked Example: One Classification Leaf

**Inputs:** labels $y = [1, 0, 1]$, starting probability $p = 0.5$ (log-odds 0), $\eta = 0.3$, a single leaf.

**Step 1: gradients and Hessians.**

$$
g = p - y = [-0.5,\ 0.5,\ -0.5], \qquad h = p(1 - p) = [0.25,\ 0.25,\ 0.25]
$$

**Step 2: leaf totals.**

$$
G = -0.5, \qquad H = 0.75
$$

**Step 3: leaf weight with $\lambda = 0$.**

$$
w^{*} = -\frac{-0.5}{0.75 + 0} \approx 0.667
$$

**Step 4: new log-odds and probability.**

$$
\hat{y}^{(1)} = 0 + 0.3 \times 0.667 = 0.2, \qquad p = \sigma(0.2) \approx 0.550
$$

**Step 5: the same leaf with $\lambda = 1$.**

$$
w^{*} = -\frac{-0.5}{0.75 + 1} \approx 0.286, \qquad p = \sigma(0.3 \times 0.286) \approx 0.521
$$

Two of three labels are positive, so the probability rises above 0.5. The update is computed in log-odds and only then converted to a probability. Because $H$ here is small (0.75), $\lambda = 1$ has a large effect: it cuts the step by more than half. XGBoost 3.0.5 with `lambda=0` reproduced a leaf of 0.2 and predictions of 0.5498, with `cover=0.75`.

## Mechanisms and Controls

Tree depth/leaves, learning rate, regularisation, row sampling, and column sampling affect fit and cost. `tree_method` selects algorithms; `grow_policy` controls growth where supported. XGBoost is not restricted to one fixed depth-first pruning description.

How the main parameters map onto the equations above:[^params]

| Parameter | Symbol | Where it acts |
|---|---|---|
| `eta` / `learning_rate` (default 0.3) | $\eta$ | Scales each new tree (Step 9) |
| `lambda` / `reg_lambda` (default 1) | $\lambda$ | Added to $H_j$ in leaf weights and gains (Steps 6–8) |
| `gamma` / `min_split_loss` (default 0) | $\gamma$ | Minimum loss reduction needed to split (Step 8) |
| `min_child_weight` (default 1) | $H_j$ | Minimum Hessian sum allowed in a child |
| `alpha` / `reg_alpha` (default 0) | — | L1 penalty on leaf weights; not in the derivation above |
| `max_depth` (default 6) | — | Limits tree size directly |

`min_child_weight` is a minimum on $H_j$, not on the number of rows. For squared error the two coincide because $h_i = 1$. For log loss a leaf of confidently predicted rows has a small $H_j$ and may be blocked from splitting even when it holds many rows.

Missing-value handling can learn a default branch at a split; this is not equivalent to filling in the unknown value. Confirm how the chosen input representation encodes missingness and zeros. Sparse input and dense zero values need not mean the same thing.

The paper's sparsity-aware split finding scans only the non-missing values of a feature, trying the missing rows on the left and then on the right, and keeps the direction with the higher gain as that node's default.[^paper]

## Learning to Rank

XGBoost provides three ranking objectives: `rank:ndcg` (the default, LambdaMART with NDCG-weighted pair gradients), `rank:map` (LambdaMART for binary labels), and `rank:pairwise` (the unscaled RankNet loss).[^ltr] Group query–document rows by query; in the `qid` interface, supply sorted query IDs aligned with the rows. Use labels compatible with the objective: MAP needs binary relevance, while NDCG can express grades. With the default exponential gain (`ndcg_exp_gain=true`), grades cannot exceed 31.[^params]

An example `qid=[10,10,20,20,20]` identifies two groups of sizes two and three. It is not a numeric relevance feature. Keep all rows of a query together when splitting.

Pair construction is controlled by `lambdarank_pair_method` (default `topk`) and `lambdarank_num_pair_per_sample`; position debiasing for click labels by `lambdarank_unbiased`. The data layout, parameter choices, an executed example, and ranking-specific pitfalls are in [[Learning to Rank#Training a LambdaMART Ranker with XGBoost]]. See also [[Light GBM]] and [[NDCG]].

The tree algorithm is the same as above. The ranking objective computes gradient statistics from pairs of documents within a query and passes per-document $g_i$ and $h_i$ to the same split-finding and leaf-weight formulas.[^model]

## Interview Questions

**Why does XGBoost use second-order information?**

The Hessian gives a Newton-style step size (the leaf-weight formula in step 6) instead of a fixed step along the gradient. It also lets one solver serve any twice-differentiable loss, since the tree only needs $g_i$ and $h_i$.[^model]

**What is the difference between $\lambda$, $\gamma$, and $\eta$?**

$\lambda$ shrinks leaf values and softens gains. $\gamma$ is a fixed cost per leaf that blocks weak splits. $\eta$ scales the whole tree after it is built. All reduce overfitting, but at different points in the procedure.

**How is XGBoost different from classic gradient boosting?**

It builds the regularisation into the split criterion and leaf values, uses second-order statistics (an idea the paper credits to earlier work by Friedman, Hastie, and Tibshirani), learns default directions for missing values, and offers approximate (quantile or histogram) split finding and column subsampling. It also adds systems work: column blocks, cache-aware access, and out-of-core training.[^paper] It is not guaranteed to beat every other GBM; see [[Gradient Boosting Machines (GBM)]].

**Why can a leaf value explode in classification, and what stops it?**

When predictions are confident, $h_i = p_i(1 - p_i)$ is tiny, so the leaf weight from step 6 can be large with $\lambda = 0$. `lambda`, `min_child_weight`, and `max_delta_step` limit this; the parameter documentation notes `max_delta_step` can help logistic regression on extremely imbalanced classes.[^params]

**Do boosted trees differ from a random forest as a model?**

No, both are sums or averages of trees. The difference is training: random-forest trees are fitted independently on resampled data, whereas each boosted tree is fitted to the current model's gradients.[^model] See [[Random Forest]] and [[Bagging]].

## Exercise

Explain why swapping document rows without swapping their query IDs corrupts pair construction. Evaluate identical candidate sets and label definitions before attributing quality differences to a boosting library.

Then redo the regression worked example with $\lambda = 0$ and $\gamma = 10$, using the paper's convention with the ½. Does the $x < 2.5$ split survive, and what are the leaf weights?

> [!example]- Exercise solution
> **Inputs:** $G_L = 5$, $H_L = 2$, $G_R = -5$, $H_R = 2$, $\lambda = 0$, $\gamma = 10$.
>
> **Step 1: gain with the ½, minus $\gamma$.**
>
> $$
> \frac{1}{2}\left[\frac{25}{2} + \frac{25}{2} - 0\right] - 10 = 12.5 - 10 = 2.5
> $$
>
> **Step 2: leaf weights.**
>
> $$
> w_L^{*} = -\frac{5}{2} = -2.5, \qquad w_R^{*} = 2.5
> $$
>
> The gain stays positive, so the split survives, and with $\lambda = 0$ the leaf weights are the mean residuals. Under the un-halved convention used in XGBoost's dump, the comparison would be $25$ against $\gamma = 10$. The outcome is the same here, but the threshold differs in general.

Related task notes: [[XGBoost Regression]] and [[XGBoost Classification]]. Documentation checked 20 September 2026; ranking parameters rechecked 27 September 2026, and the ranking example executed with XGBoost 3.0.5. Record package version and configuration with experiments.

## References & Useful Links

[^paper]: [Chen & Guestrin (2016), "XGBoost: A Scalable Tree Boosting System", KDD](https://arxiv.org/abs/1603.02754) — Regularised objective, second-order approximation, optimal leaf weight, split gain, shrinkage and column subsampling, weighted quantile sketch, sparsity-aware default directions, and system design (full text read via arXiv HTML).
[^model]: [XGBoost: Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) — Step-by-step derivation, structure score, gain and pruning, the shared $g_i$/$h_i$ solver for custom and ranking losses, and the model view shared with random forests.
[^ltr]: [XGBoost: Learning to rank tutorial](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — Query groups, LambdaMART default, RankNet `rank:pairwise`, and sorted `qid` layout.
[^params]: [XGBoost parameters](https://xgboost.readthedocs.io/en/stable/parameter.html) — Objectives, growth, regularisation, `lambdarank_*` parameters, and `ndcg_exp_gain`.
