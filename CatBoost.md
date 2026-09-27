---
tags:
  - "ds-foundations"
---

## Overview

CatBoost can be used when dealing with categorical data, and there is no need to do one-hot encoding: pass the categorical columns directly and CatBoost converts them to numbers internally. It is a gradient-boosting library (Prokhorenkova et al.; arXiv 2017, revised 2019) built around two ideas meant to fight a *prediction shift* caused by target leakage: ordered target statistics for categorical features, and ordered boosting.[^paper] Its default trees are symmetric (oblivious).[^params]

## The Math, Step by Step

### 1. Target statistics replace categories

A natural encoding replaces each category by the average label of rows with that category, smoothed towards a prior $p$ with strength $a$:

$$
\hat{x}_k = \frac{\sum_{j:\ x_j = k} y_j + a\,p}{\sum_{j:\ x_j = k} 1 + a}
$$

If the sums include row $i$ itself (a *greedy* target statistic), row $i$'s own label leaks into its feature. A category seen only once gets its own label as the feature value, which is a perfect but fake predictor.

The paper makes this concrete.[^paper] Suppose every category is unique and $P(y = 1) = 0.5$ in each. On training rows the greedy statistic is $\frac{y_k + ap}{1 + a}$, so one threshold separates the classes perfectly. On test rows every value is just $p$, and accuracy falls to 0.5. The paper's general fix is to compute row $k$'s statistic from a subset $\mathcal{D}_k$ that excludes row $k$. The common choice for $p$ is the dataset's average target.[^paper]

**Leave-one-out is not enough.** Excluding only row $k$ still leaks. With a constant category and $n^{+}$ positives, the statistic is $\frac{n^{+} - y_k + ap}{n - 1 + a}$. Positives get a slightly lower value than negatives, so a single threshold again separates the training rows perfectly.[^paper]

### 2. Ordered target statistics

CatBoost randomly permutes the rows and, for each row, uses only the rows **before** it with the same category. For binary classification the documentation gives[^ctr]

$$
\text{ctr} = \frac{\text{countInClass} + \text{prior}}{\text{totalCount} + 1},
$$

where `countInClass` is the number of earlier rows with this category and label 1, and `totalCount` is the number of earlier rows with this category. Several permutations are used, and combinations of categorical features can be encoded the same way.[^ctr] This is the paper's formula with $\mathcal{D}_k$ equal to the rows before $k$ in a random permutation, and with $a = 1$. At prediction time, statistics are computed from the whole training set.[^paper]

With a single permutation, rows near the start have a short history and very noisy statistics. The paper therefore uses different permutations at different boosting steps.[^paper] It builds feature combinations greedily: at each split, the categorical features already used in the tree are combined with every categorical feature.[^paper]

### 3. Ordered boosting

The same leak exists in ordinary boosting: residuals are computed with a model that was fitted on those very rows. Ordered boosting is a permutation-driven alternative that avoids this.[^paper] It is optional: `boosting_type` defaults to `Plain` (classic boosting) on CPU, and `Ordered` is chosen by default only on GPU for datasets of up to 50,000 rows, not in multiclass mode.[^params]

The paper quantifies the leak in a toy case: squared error, two Bernoulli features, $y = c_1 x_1 + c_2 x_2$, and two stumps. If both stumps are fitted on the same $n$ rows, the expected prediction is biased by

$$
-\frac{1}{n - 1}\, c_2 \left(x_2 - \tfrac{1}{2}\right).
$$

If each stump uses an independent sample, the bias disappears (up to an $O(2^{-n})$ term).[^paper] The bias shrinks like $1/n$, which is why ordered boosting matters most on small datasets.

A 200,000-run simulation with $c_1 = 2$, $c_2 = 1$, and $n = 12$ reproduced this. With the same data for both stumps, the bias was $\pm 0.045$, matching the formula's $\pm 1/22 \approx 0.0455$. With independent samples it was below 0.001.

The idealised algorithm keeps $n$ supporting models $M_1, \ldots, M_n$, where $M_i$ is trained on the first $i$ rows of a permutation. The residual for row $j$ comes from $M_{j-1}$, a model that never saw row $j$. Training $n$ models is infeasible, so CatBoost uses $s + 1$ permutations and keeps predictions only for prefixes of length $2^j$. That reduces storage from $O(sn^2)$ to $O(sn)$. The same permutation must drive both the target statistics and the boosting; otherwise the leak returns.[^paper]

### 4. Symmetric (oblivious) trees

With the default `grow_policy="SymmetricTree"`, every node at a given level uses **the same split condition**.[^params] A depth-$d$ tree is then $d$ binary tests $b_1, \ldots, b_d$, and the leaf index is a binary number:

$$
\text{leaf}(x) = \sum_{l=1}^{d} b_l(x)\, 2^{d - l}, \qquad b_l(x) \in \{0, 1\}
$$

There are exactly $2^d$ leaves. Prediction is a few comparisons and an array look-up. The paper describes such trees as balanced, less prone to overfitting, and much faster at test time.[^paper]

### 5. Leaf values

Leaf values use an L2 penalty `l2_leaf_reg` (default 3). By default, classification uses Newton steps for leaf estimation and regression uses gradient steps.[^params] As in [[XGBoost]], a larger penalty shrinks leaf values towards zero.

## Worked Example: Ordered versus Greedy Target Statistics

**Inputs:** six rows in their (already permuted) order, a categorical feature, binary labels, prior $= 0.5$.

| Row | Genre | Label |
|---|---|---|
| 1 | rock | 1 |
| 2 | pop | 0 |
| 3 | rock | 0 |
| 4 | rock | 1 |
| 5 | pop | 1 |
| 6 | rock | 1 |

**Step 1: row 1** (first `rock`; no earlier `rock` rows).

$$
\frac{0 + 0.5}{0 + 1} = 0.5
$$

**Step 2: row 3** (one earlier `rock`, label 1).

$$
\frac{1 + 0.5}{1 + 1} = 0.75
$$

**Step 3: row 4** (earlier `rock` labels 1, 0).

$$
\frac{1 + 0.5}{2 + 1} = 0.5
$$

**Step 4: row 6** (earlier `rock` labels 1, 0, 1).

$$
\frac{2 + 0.5}{3 + 1} = 0.625
$$

**Step 5: `pop` rows.** Row 2 gets $\frac{0 + 0.5}{0 + 1} = 0.5$; row 5 (one earlier `pop`, label 0) gets $\frac{0 + 0.5}{1 + 1} = 0.25$.

**Step 6: greedy statistic for comparison.** Using all four `rock` rows, every `rock` row gets $3/4 = 0.75$, including row 3 whose own label is 0.

The ordered values never use a row's own label, so the encoding available at training time matches what a new row will see at prediction time. The early rows get noisy values close to the prior; that noise is the price of avoiding leakage, and multiple permutations reduce it.

## Worked Example: Reading an Oblivious Tree

**Inputs:** a depth-3 symmetric tree with level conditions $b_1 = [x_1 > 0.5]$, $b_2 = [x_2 > 10]$, $b_3 = [x_3 > 2]$, and an input $x = (0.7, 5, 3)$.

**Step 1: the three tests.**

$$
b_1 = 1, \qquad b_2 = 0, \qquad b_3 = 1
$$

**Step 2: leaf index.**

$$
1 \times 4 + 0 \times 2 + 1 \times 1 = 5
$$

The input lands in leaf 5 of 8, found with three comparisons and no tree traversal. Every input evaluates the same three conditions, which is why oblivious trees are fast at inference.

## Python Example

Executed with CatBoost 1.2.10 on synthetic data where the target depends on a city category and a spend amount.

```python
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

rng = np.random.default_rng(0)
n = 2000
city = rng.choice(["delhi", "mumbai", "pune", "goa"], size=n)
spend = rng.normal(100, 30, size=n)
base = {"delhi": -1.0, "mumbai": 0.0, "pune": 0.5, "goa": 1.5}
logit = np.array([base[c] for c in city]) + 0.02 * (spend - 100)
y = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
X = pd.DataFrame({"city": city, "spend": spend})

model = CatBoostClassifier(iterations=300, depth=4, verbose=0, random_seed=0)
model.fit(X[:1500], y[:1500], cat_features=["city"], eval_set=(X[1500:], y[1500:]))
params = model.get_all_params()
print(params["grow_policy"], params["l2_leaf_reg"], params["boosting_type"])  # SymmetricTree 3 Plain
print(round(model.score(X[1500:], y[1500:]), 3))                             # 0.656
```

The raw string column is passed directly; no one-hot encoding is needed. The accuracy is modest because the labels are drawn randomly from probabilities, so even the true model would make many errors. Because an evaluation set was supplied, `use_best_model` defaults to keeping the best iteration on it.[^params]

## What the Paper Reported

The authors compared CatBoost (in Ordered mode) with XGBoost and LightGBM on nine datasets. All three libraries received categorical features preprocessed with ordered target statistics, and the data were split 4/5 for tuning and training and 1/5 for testing.[^paper]

- **Against the baselines.** CatBoost had the lowest log loss on all nine. The improvement was statistically significant except on Appetency, Churn, and Upselling.
- **Ordered versus Plain.** The largest gains from Ordered mode were on Adult and Internet, both under 40,000 training rows; on Internet, Plain had 3.9% higher log loss. On Epsilon, Ordered mode was about 1.7 times slower than Plain.
- **Target statistics.** Replacing ordered statistics with greedy ones raised log loss by 1.1% to 57%, depending on the dataset. Holdout statistics were the best alternative, but still worse than ordered ones.
- **Oblivious trees alone.** A "raw" CatBoost close to classical boosting differed from XGBoost and LightGBM by only about 0.2% on average. Its main difference was the oblivious trees, and the baselines received the same ordered statistics. The gains therefore come from the ordering ideas and feature combinations, not from the tree shape.
- **Same permutation.** In that raw setting, Ordered mode improved log loss by 0.5% on average over Plain with independent permutations for encoding and boosting, and by 0.6% when the two permutations were the same.
- **Feature combinations.** Allowing pairs of categorical features improved log loss by 1.86% on average (up to 11.3%); allowing triples added little more.
- **Speed.** On Epsilon at depth 6 (64 leaves for LightGBM), time per tree was 1.1 s for CatBoost Plain, 1.9 s for Ordered, 3.9 s for histogram XGBoost, and 1.1 s for LightGBM, all with 16 threads.

The setup used an 80/20 train-test split, 5-fold cross-validation, and 50 Hyperopt (TPE) tuning steps per library. The library versions are very old: CatBoost 0.3, XGBoost 0.6, and LightGBM 0.1.[^paper]

These are the authors' benchmarks with their tuning and library versions; treat them as evidence for the mechanisms, not as a guarantee on your data.

## Controls

| Parameter | Default | Role |
|---|---|---|
| `iterations` | 1000 | Maximum number of trees |
| `learning_rate` | Chosen automatically for Logloss, MultiClass, and RMSE; otherwise 0.03 | Shrinkage |
| `depth` | 6 | Tree depth; $2^{\text{depth}}$ leaves for symmetric trees |
| `l2_leaf_reg` | 3 | L2 penalty on leaf values |
| `one_hot_max_size` | Usually 2 | Categories with at most this many values are one-hot encoded instead |
| `boosting_type` | `Plain` on CPU | `Ordered` enables ordered boosting |

Defaults from the CatBoost training-parameter reference, checked 27 September 2026.[^params] With 300 iterations, the automatic learning rate in the example above was about 0.059.

## Limitations & Common Pitfalls

- **Declare categorical columns.** Integer-coded categories are treated as numbers unless listed in `cat_features`.
- **Ordered boosting costs time.** It is not the CPU default; enable it deliberately on small datasets where leakage matters.
- **Time order matters.** If rows have a real order, `has_time=True` uses it instead of random permutations, which stops future rows from informing the encoding of past ones.[^params]
- **Symmetric trees are restrictive.** For some data, `Depthwise` or `Lossguide` growth fits better; compare with validation.

## Interview Questions

**What is target leakage in target encoding, and how does CatBoost avoid it?** A greedy encoding uses each row's own label. CatBoost computes each row's statistic from earlier rows in a random permutation only, so the value never contains the row's label.

**What is an oblivious tree?** A tree that applies the same split at every node of a level; depth $d$ gives $2^d$ leaves indexed by $d$ binary tests.

**Why add a prior?** It stabilises the statistic for rare categories: with no history the value is the prior, and it moves towards the observed rate as rows accumulate.

**Why doesn't leave-one-out target encoding fix the leak?** A row's statistic still depends on its own label through what is left out. For a constant category, positives get a slightly lower value than negatives, so the model can separate training rows perfectly and gain nothing at test time.[^paper]

**CatBoost versus XGBoost or LightGBM?** All are gradient-boosted trees. CatBoost's distinguishing features are native categorical encoding with ordered statistics, optional ordered boosting, and symmetric trees; see [[XGBoost]] and [[Light GBM]].

## Exercise

Continue the ordered example: a seventh row is `pop` with label 0. What target statistic does it get?

> [!example]- Exercise solution
> **Inputs:** earlier `pop` rows are rows 2 (label 0) and 5 (label 1), so `countInClass` $= 1$ and `totalCount` $= 2$; prior $= 0.5$.
>
> **Step 1: ordered statistic.**
>
> $$
> \frac{1 + 0.5}{2 + 1} = 0.5
> $$
>
> Row 7's own label, 0, is not used.

## References & Useful Links

[^paper]: [Prokhorenkova, Gusev, Vorobev, Dorogush and Gulin, "CatBoost: unbiased boosting with categorical features", arXiv:1706.09516v5 (20 January 2019)](https://arxiv.org/abs/1706.09516) — Main text and Appendices C.2, D and G read; the proofs and formal algorithm in Appendices A, B, E and F were not reviewed. Greedy, holdout, leave-one-out and ordered target statistics; the prediction-shift theorem; ordered boosting and its practical implementation; oblivious trees; feature combinations; Tables 2 to 4 and 6 to 10; and the experimental setup and library versions.
[^ctr]: [CatBoost: Transforming categorical features to numerical features](https://catboost.ai/docs/en/concepts/algorithm-main-stages_cat-to-numberic) — Random permutations, the `(countInClass + prior) / (totalCount + 1)` formula using only earlier rows, and feature combinations.
[^params]: [CatBoost common training parameters](https://catboost.ai/docs/en/references/training-parameters/common) — Defaults for `iterations`, `learning_rate`, `depth`, `l2_leaf_reg`, `grow_policy`, `boosting_type`, `one_hot_max_size`, `leaf_estimation_method`, `has_time`, and `use_best_model`.