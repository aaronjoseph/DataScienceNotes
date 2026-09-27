---
tags:
  - "search-eng"
  - "ds-foundations"
---

## Core Idea

LightGBM is a tree-boosting library. Its histogram-based splitting and leaf-wise growth can be efficient, but runtime and quality depend on data, settings, hardware, and the comparison. Leaf-wise growth chooses a promising leaf rather than expanding every node at the same depth; control complexity to avoid overfitting.

In one sentence for an interview: *LightGBM uses the same second-order boosting objective as XGBoost, but finds splits from binned histograms, grows the leaf with the largest loss reduction first, and can subsample rows by gradient size (GOSS) and bundle sparse features (EFB) to train faster.*[^features][^paper]

## The Math, Step by Step

### 1. Same objective and leaf values as XGBoost

Each example supplies a gradient $g_i$ and Hessian $h_i$ of the loss. For a leaf with totals $G$ and $H$ and L2 penalty $\lambda$ (`lambda_l2`),

$$
w^{*} = -\frac{G}{H + \lambda}.
$$

The split gain compared with `min_gain_to_split` is the same bracket as in [[XGBoost#8. Split gain|XGBoost]]; in a LightGBM 4.7.0 check the reported `split_gain` did not include a factor of ½:

$$
\text{Gain} = \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}
$$

### 2. Histogram split finding

Each feature is bucketed once into at most `max_bin` bins (default 255).[^params] For a node, one pass over its rows accumulates $G$ and $H$ per bin, costing $O(\#\text{data})$. Scanning bins left to right then evaluates every candidate split in $O(\#\text{bins})$ instead of $O(\#\text{data})$.[^features]

### 3. Histogram subtraction

A parent's histogram is the sum of its children's, so only the smaller child needs to be built:

$$
\text{hist}(\text{larger child}) = \text{hist}(\text{parent}) - \text{hist}(\text{smaller child})
$$

The subtraction costs $O(\#\text{bins})$.[^features]

### 4. Leaf-wise (best-first) growth

At each step, split the one leaf whose best split has the largest loss reduction. For a fixed number of leaves this tends to reach a lower loss than level-wise growth, but it can overfit small data, which is why `max_depth` exists as a limit.[^features] A level-wise tree of depth $d$ has at most $2^d$ leaves; a leaf-wise tree with `num_leaves = 31` can be much deeper than 5 levels.

### 5. Gradient-based One-Side Sampling (GOSS)

Examples with large gradients contribute most to the gain.[^paper] With `top_rate` $= a$ and `other_rate` $= b$:

1. Keep the top $a \times 100\%$ of rows by gradient magnitude.
2. Randomly sample $b \times 100\%$ of all rows from the remainder.
3. Multiply the sampled rows' gradients and Hessians by

$$
\frac{1 - a}{b}
$$

so their sums estimate the full remainder without bias. LightGBM's source ranks rows by $\lvert g_i h_i \rvert$, applies this weight, and skips GOSS for the first $1/\text{learning\_rate}$ iterations.[^goss]

The paper differs from the implementation in two details.[^paper] It ranks rows by $\lvert g_i \rvert$, and it states the gain as a first-order "variance gain", $\frac{1}{n}\left(\frac{(\sum_{l} g_i)^2}{n_l} + \frac{(\sum_{r} g_i)^2}{n_r}\right)$, which uses gradients and row counts instead of Hessians. Its Algorithm 2 samples $b \times \text{len}(I)$ rows, which is where $(1 - a)/b$ comes from; the prose in Section 3.2 instead says $b \times \lvert A^c \rvert$, for which the matching multiplier would be $1/b$. The implementation follows Algorithm 2.[^goss] The paper also proves a bound showing that the approximation error shrinks as the data grow, provided the split is not too unbalanced.[^paper]

### 6. Exclusive Feature Bundling (EFB)

Features that are rarely non-zero at the same time, such as one-hot columns, are merged into one bundle so fewer histograms are built. Optimal bundling is NP-hard, so a greedy algorithm is used.[^paper] It is enabled by default (`enable_bundle`).[^params]

The paper proves NP-hardness by reduction from graph colouring. The greedy algorithm treats features as vertices, with edges weighted by conflicts (rows where both are non-zero), and allows a small conflict rate $\gamma$ per bundle.[^paper] Features in a bundle are kept apart by bin offsets. If feature A uses bins $[0, 10)$ and B uses $[0, 20)$, B is shifted by 10 to $[10, 30)$ and the bundle covers $[0, 30)$. Histogram building then costs $O(\#\text{data} \times \#\text{bundle})$ instead of $O(\#\text{data} \times \#\text{feature})$.[^paper]

### 7. Categorical splits

Instead of one-hot encoding, LightGBM sorts a categorical feature's categories by $\sum g / \sum h$ and finds the best split point on that ordering, about $O(k \log k)$ for $k$ categories rather than the $2^{k-1} - 1$ possible partitions.[^features]

## Worked Example: One Tree, Checked Against LightGBM

**Inputs:** 40 rows, the pattern $x = [1, 2, 3, 4]$ with $y = [1, 2, 6, 7]$ repeated 10 times; L2 regression, `boost_from_average=True` (start at the mean, 4), $\lambda = 1$, learning rate 0.3, `num_leaves=2`.

**Step 1: gradients.** For L2 loss $g_i = \hat{y}_i - y_i$ and $h_i = 1$, so $g = [3, 2, -2, -3]$ for each repetition.

**Step 2: best split $x < 2.5$.**

$$
G_L = 10 \times (3 + 2) = 50, \quad H_L = 20, \qquad G_R = -50, \quad H_R = 20
$$

**Step 3: gain.**

$$
\text{Gain} = \frac{50^2}{21} + \frac{(-50)^2}{21} - \frac{0^2}{41} \approx 238.1
$$

**Step 4: leaf values with shrinkage.**

$$
w_L = 0.3 \times \left(-\frac{50}{21}\right) \approx -0.714, \qquad w_R \approx 0.714
$$

**Step 5: predictions.**

$$
4 - 0.714 = 3.286, \qquad 4 + 0.714 = 4.714
$$

LightGBM 4.7.0 reported `split_gain` 238.095 and predictions 3.286 and 4.714. Its model dump stored the leaf values as 3.286 and 4.714, meaning the starting mean was folded into the first tree's leaves.

## Worked Example: GOSS Weights

**Inputs:** 1,000 rows, default `top_rate` $a = 0.2$ and `other_rate` $b = 0.1$.[^params]

**Step 1: large-gradient rows kept.**

$$
0.2 \times 1000 = 200
$$

**Step 2: rows sampled from the other 800.**

$$
0.1 \times 1000 = 100
$$

**Step 3: weight for the sampled rows.**

$$
\frac{1 - 0.2}{0.1} = 8 = \frac{800}{100}
$$

Each sampled small-gradient row stands in for eight similar rows, so the expected gradient sum over the 800 is preserved while only 300 of 1,000 rows are used to build histograms. Keeping all large-gradient rows protects the accuracy of the gain; sampling only the small ones is what makes it "one-side".

## What the Paper Reported

Ke et al. compared LightGBM with XGBoost and with LightGBM without GOSS and EFB (`lgb_baseline`). They used five public datasets on a 24-core server with 16 threads, and measured time per iteration.[^paper]

- **Speed.** Against `lgb_baseline`, LightGBM was 21×, 6×, 1.6×, 14×, and 13× faster on Allstate, Flight Delay, LETOR, KDD10, and KDD12. The smallest gain was on LETOR, whose features are dense, so EFB has little to bundle.
- **Accuracy.** Accuracy was almost unchanged. On the Microsoft LETOR ranking data, NDCG@10 was 0.5275 for LightGBM and 0.5277 for the baseline.
- **GOSS versus random subsampling.** At the same sampling ratio of 0.2 on LETOR, GOSS reached NDCG@10 0.5275 against 0.5239 for stochastic gradient boosting.

These are the authors' results for their parameter settings (for example $a = b = 0.05$ or $0.1$) and 2017 library versions. They motivate the techniques but are not a current benchmark.

The supplementary material adds some context.[^supp]

- **LETOR settings.** The LETOR runs used `num_leaves=255`, learning rate 0.05, and 1,000 rounds.
- **KDD accuracy.** The KDD10 and KDD12 accuracy figures come from the 100th iteration, because the baselines could not converge in reasonable time.
- **EFB conflict rate.** The main experiments used $\gamma = 0$. Allowing $\gamma = 0.01$ lowered KDD10 AUC from 0.7873 to 0.7858 and saved little time, because EFB had already bundled the sparse features.

## Parameters to Understand

| Parameter | Main role |
|---|---|
| `num_leaves`, `max_depth` | Tree complexity; tune together |
| `min_data_in_leaf` | Minimum leaf-size constraint |
| `learning_rate`, `num_iterations` | Step size and number of boosting rounds |
| `feature_fraction` | Feature subsampling |
| `bagging_fraction`, `bagging_freq` | Row subsampling; frequency must enable bagging |
| `lambda_l1`, `lambda_l2`, `min_gain_to_split` | Regularisation and split constraints |
| `max_cat_threshold` | Limit categorical split candidates; not `max_cat_group` |

Validate rather than assuming small datasets are unsuitable or more leaves always help. Use an appropriate held-out set and the early-stopping callback where supported; “best 20” is not a complete training rule.

Defaults, checked 27 September 2026: `num_leaves` 31, `learning_rate` 0.1, `num_iterations` 100, `min_data_in_leaf` 20, `min_sum_hessian_in_leaf` 1e-3, `lambda_l2` 0, `max_depth` -1 (no limit), `max_bin` 255.[^params] `min_sum_hessian_in_leaf` is the same idea as XGBoost's `min_child_weight`: a floor on $H$ in a leaf.

## Search Ranking

`LGBMRanker` supports objectives such as `lambdarank` and `rank_xendcg`. Labels encode relevance grades. Rows for each query must be contiguous, and `group` contains **group sizes**, not a query-ID value for every row. For query sizes `[3, 2]`, five feature rows are required. Validation needs its own group sizes.

Separate queries or time periods before fitting; document-level random splitting can leak query context. Choose metric cutoffs and label gains consistent with [[NDCG]] and [[Learning to Rank]].

## Interview Questions

**Leaf-wise versus level-wise growth?** Leaf-wise always splits the leaf with the largest gain, so it lowers loss faster for a given number of leaves, but it builds deep, lopsided trees that can overfit small data. Control it with `num_leaves`, `max_depth`, and `min_data_in_leaf`.

**Why are histograms faster?** Split search scans bins, not rows, and a child's histogram can be obtained by subtraction. Binning also lets features be stored as small integers.[^features]

**Why does GOSS keep large-gradient rows?** Those rows are poorly fitted and dominate the gain. Down-sampling only the well-fitted rows, then reweighting them, keeps the gain estimate close to the full-data value.[^paper]

**How do `num_leaves` and `max_depth` relate?** A tree limited to depth $d$ can have at most $2^d$ leaves, so `num_leaves` should usually be below $2^{\text{max\_depth}}$ when both are set.

**LightGBM versus XGBoost?** They optimise the same regularised second-order objective. XGBoost also offers histogram (`hist`) and loss-guided growth, so modern differences are mostly defaults, sampling tricks, and categorical handling; benchmark on your own data.

## Exercise

Arrange six examples from three queries into contiguous groups. Write their group-size vector and check that it sums to six. Compare with the `qid` convention in [[XGBoost]].

Then: with `top_rate=0.1` and `other_rate=0.2` on 10,000 rows, how many rows does GOSS use per tree, and what weight do the sampled rows get?

> [!example]- Exercise solution
> For example, query sizes 2, 3, and 1 give `group=[2, 3, 1]`, which sums to 6 and requires the rows to be ordered by query.
>
> For GOSS, the inputs are 10,000 rows, $a = 0.1$, and $b = 0.2$.
>
> **Step 1: large-gradient rows.**
>
> $$
> 0.1 \times 10{,}000 = 1{,}000
> $$
>
> **Step 2: sampled rows.**
>
> $$
> 0.2 \times 10{,}000 = 2{,}000
> $$
>
> **Step 3: weight of the sampled rows.**
>
> $$
> \frac{1 - 0.1}{0.2} = 4.5
> $$
>
> Each tree uses 3,000 rows. The 2,000 sampled rows stand in for the other 9,000, which is why each gets weight 4.5.

Documentation checked 20 September 2026 and 27 September 2026; the worked example was executed with LightGBM 4.7.0. Pin the installed library version when implementing.

## References & Useful Links

- [LGBMRanker](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRanker.html) — Query groups and fitting API.

[^features]: [LightGBM features](https://lightgbm.readthedocs.io/en/latest/Features.html) — Histogram algorithm, histogram subtraction, leaf-wise growth and `max_depth`, and optimal categorical splits.
[^params]: [LightGBM parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html) — Parameter names, defaults, objectives, GOSS rates, and EFB switch.
[^paper]: [Ke et al. (2017), "LightGBM: A Highly Efficient Gradient Boosting Decision Tree", NIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf) — Full paper read. Histogram algorithm costs, GOSS (Algorithm 2, variance gain, Theorem 3.2), EFB (NP-hardness, greedy bundling, bin offsets), and Tables 2 to 4.
[^supp]: [Ke et al. (2017), supplementary material](https://proceedings.neurips.cc/paper_files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Supplemental.zip) — Section 3 read in full; the proofs of Theorem 3.2 and Proposition 2.1 were not read. Experiment parameter settings, GOSS $a$ and $b$ per sampling ratio, the effect of the EFB conflict rate $\gamma$, and time–accuracy notes.
[^goss]: [LightGBM source: `src/boosting/goss.hpp`](https://github.com/microsoft/LightGBM/blob/master/src/boosting/goss.hpp) — Ranking by $\lvert g h \rvert$, the $(\text{cnt} - \text{top}_k)/\text{other}_k$ multiplier, and skipping the first $1/\text{learning\_rate}$ iterations.
