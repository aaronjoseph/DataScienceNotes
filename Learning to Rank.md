---
note_type: concept
search_stage: ranking
tags:
  - "search-eng"
---

## Core Idea

Learning to rank trains a scoring or ordering model for documents **within a query context**. Typical data contains a query ID, candidate document, query–document features, and a relevance grade. Candidate generation remains a separate constraint: the model cannot rank an item it never receives (see [[Candidate Generation]]).

## Objective Families

| Family | Training comparison | Example intuition |
|---|---|---|
| Pointwise | Individual query–document label | Predict a relevance grade or probability |
| Pairwise | Two documents for the same query | Prefer a more relevant document over a less relevant one |
| Listwise / metric-aware | A query's candidate list or ranking-sensitive changes | Emphasise errors affecting the evaluated ordering |

For grades A=3, B=1, C=0 under one query, pair preferences include A>B, A>C, and B>C. Do not construct a preference between documents from unrelated queries solely by comparing their grades.

NDCG is not directly differentiable through discrete sorting. LambdaMART-style approaches use ranking-sensitive gradient constructions; an objective name does not mean ordinary gradient descent through the final NDCG calculation.

## Training Contract

1. Fix label meaning, feature availability time, and query grouping.
2. Split by the intended generalisation target: queries, users, or time.
3. Fit transformations within training data and preserve group boundaries.
4. Select on held-out query metrics; test once on a separate set.
5. Evaluate the serving pipeline's actual candidate distribution and feature freshness.

[[Light GBM]] supplies contiguous group sizes; [[XGBoost]] supports aligned sorted `qid` values (see [[#Training a LambdaMART Ranker with XGBoost]]). Check the library's objective and label requirements. Click labels need [[Click Bias|bias analysis]].

## Training a LambdaMART Ranker with XGBoost

XGBoost's default ranking objective, `rank:ndcg`, implements **LambdaMART**: gradient-boosted trees trained on pairwise comparisons within each query, with each pair's gradient scaled by how much swapping the two documents would change NDCG.[^pairwise] It is a common first learned ranker over hand-built query–document features. The general boosting controls are in [[XGBoost]].

### Data layout

Each row is one query–document pair. A separate `qid` array groups rows by query and must be sorted in non-decreasing order, so every query's rows are contiguous:[^pairwise]

| qid | label | features |
|---|---|---|
| 1 | 3 | $x_1$ |
| 1 | 0 | $x_2$ |
| 1 | 1 | $x_3$ |
| 2 | 2 | $x_4$ |
| 2 | 2 | $x_5$ |

The `qid` is a grouping key, not a feature. Labels are relevance grades; pairs are formed only within a query and only between different grades, so query 2 above contributes no pairs.

### Choosing the objective

- **`rank:ndcg`** (default): binary or graded labels; the safe default when unsure. Supports position debiasing for click data.[^params]
- **`rank:map`**: binary labels (0/1); targets mean average precision.
- **`rank:pairwise`**: the original RankNet pairwise logistic loss, with no metric-based scaling; see [[#A Pairwise Loss Makes the Preference Concrete]].

XGBoost's tutorial suggests matching the objective to the target metric when there is plenty of training data, and preferring `rank:ndcg` or `rank:pairwise` with the `mean` pair strategy when data is limited, because that yields more *effective pairs* (pairs that produce a non-zero gradient).[^pairwise] Treat this as a starting point for tuning, not a guarantee.

### Key ranking parameters

Checked against the XGBoost documentation on 27 September 2026:[^params]

- **`lambdarank_pair_method`** (default `topk`): `topk` builds pairs for the top-$k$ documents as currently ranked by the model; `mean` samples a fixed number of pairs per document.
- **`lambdarank_num_pair_per_sample`**: the truncation $k$ for `topk`, or the pairs per document for `mean`. To train towards NDCG@6, use `topk` with 6.
- **`ndcg_exp_gain`** (default `true`): use the gain $2^{\text{rel}} - 1$ rather than the raw grade. With this setting, labels cannot exceed 31.
- **`lambdarank_unbiased`** (default `false`): Unbiased LambdaMART position debiasing for click labels; documented as experimental, and not supported by the distributed interfaces.
- **`eval_metric`**: `ndcg@k`, `map@k`, or `pre@k`. XGBoost scores a query with no relevant documents as 1 for NDCG and MAP; append `-` (for example `ndcg@5-`) to score it as 0.

### Worked example: exponential versus linear gain

**Inputs:** relevance grades 1 and 3 for two documents in one query.

**Step 1: linear gains** use the grades directly.

$$
\text{gain}(3) = 3, \qquad \text{gain}(1) = 1
$$

**Step 2: exponential gains** with `ndcg_exp_gain=true`.

$$
\text{gain}(3) = 2^3 - 1 = 7, \qquad \text{gain}(1) = 2^1 - 1 = 1
$$

Under linear gain the grade-3 document is worth three times the grade-1 document; under exponential gain it is worth seven times. Training therefore penalises misplacing highly relevant documents more heavily with the default. Use the same gain convention in training and in offline [[NDCG]] evaluation; see [[NDCG#Grade Values Are a Modelling Choice|grade values]].

### Python example

This script uses XGBoost's native API and was executed locally with XGBoost 3.0.5 and NumPy. The data is synthetic: a hidden signal generates graded labels from 0 to 3.

```python
import numpy as np
import xgboost as xgb

rng = np.random.default_rng(0)
n_queries, docs_per_query = 60, 8
qid = np.repeat(np.arange(n_queries), docs_per_query)  # sorted, contiguous groups
X = rng.normal(size=(qid.size, 3))
signal = 1.5 * X[:, 0] + 0.5 * X[:, 1] + rng.normal(scale=0.5, size=qid.size)
y = np.digitize(signal, [-1.0, 0.5, 1.5])  # graded labels 0..3

train = qid < 45  # split by query, never by row
dtrain = xgb.DMatrix(X[train], label=y[train], qid=qid[train])
dvalid = xgb.DMatrix(X[~train], label=y[~train], qid=qid[~train])

params = {
    "objective": "rank:ndcg",
    "lambdarank_pair_method": "topk",
    "lambdarank_num_pair_per_sample": 5,
    "eval_metric": "ndcg@5",
    "tree_method": "hist",
    "max_depth": 3,
    "eta": 0.1,
}
booster = xgb.train(params, dtrain, num_boost_round=50,
                    evals=[(dvalid, "valid")], verbose_eval=False)
print(booster.eval(dvalid))

scores = booster.predict(dvalid)
valid_qid, valid_y = qid[~train], y[~train]
first = valid_qid == valid_qid[0]
print("labels in model order:", valid_y[first][np.argsort(-scores[first])])
```

In that run, validation NDCG@5 was about 0.95 and the first validation query's labels in model order were `[3 3 2 3 2 3 1 1]`. On easy synthetic data this only shows that the pipeline works; it says nothing about performance on real queries.

### Pitfalls specific to XGBoost ranking

- **Scores are only comparable within a query.** `predict` returns ordering scores, not probabilities; sort each query's candidates by them.
- **`XGBRanker` needs scikit-learn.** The scikit-learn-style wrapper raised `ImportError` in an environment without scikit-learn; the native `DMatrix(..., qid=...)` API does not need it.
- **Group-aware splitting and metrics.** Use `GroupKFold` or `StratifiedGroupKFold` with `groups=qid`. scikit-learn's `ndcg_score` does not know about query groups, so do not apply it to the concatenated rows of many queries.[^pairwise]
- **Distributed training.** If a framework scatters a query's rows across workers, pairs and IDCG are computed on fragments; the tutorial warns that performance can then be disastrous.[^pairwise]
- **Version changes.** XGBoost 2.0 changed the ranking defaults (for example `topk` pairs and NDCG-weighted gradients). Record the library version and all ranking parameters with each experiment.

## Engagement Features

Product-search rankers often use behavioural counts as features: clicks, product-page views, add-to-cart events, and orders, for a query–item pair or an item alone, over several windows such as 1, 3, 7, and 30 days.

- **Key them precisely.** Query–item features need the same query normalisation at training and serving time, for example lowercase and trim followed by a hash. Restrict lookups to the recalled candidates to bound cost.
- **Measure coverage.** Record how many candidates had features for each query. If 30 of 120 candidates have query–item metrics, coverage is 25%, and the model is mostly scoring on other features for that query.
- **Distinguish missing from zero.** XGBoost treats missing values (by default `NaN`) as missing and learns a default branch direction for them; 0 is an ordinary value.[^1] Filling unavailable features with 0 at serving time when training used `NaN`, or the reverse, changes predictions. Use one convention everywhere.
- **Respect time.** Each window must end before the label's event time, or the feature leaks the label; see [[Data Leakage]].
- **Expect feedback loops.** Engagement reflects past ranking and exposure. Highly ranked items gather more clicks and stay highly ranked; see [[Click Bias]]. New items and new queries have no history.
- **Degrade deliberately.** If the feature store is unavailable, choosing neutral values and continuing is a product decision. Log it, because the ranker then behaves differently.

For online comparison of two rankers, [[Interleaving]] is often more sensitive than an [[AB Testing|A/B test]]; confirm important launches with an A/B test.

## A Pairwise Loss Makes the Preference Concrete

For documents $d_i$ and $d_j$ under the same query, with $d_i$ preferred, write their scores as $s_i$ and $s_j$. A pairwise logistic loss is

$$
\ell_{ij}=\log(1+\exp(-(s_i-s_j))).
$$

Compare three score margins under the same loss:

**Tied scores:** $s_i-s_j=0$.

$$
L=\ln(1+e^0)=\ln2\approx0.6931
$$

**Correct ordering:** $s_i-s_j=2$.

$$
L=\ln(1+e^{-2})\approx0.1269
$$

**Reversed ordering:** $s_i-s_j=-2$.

$$
L=\ln(1+e^2)\approx2.1269
$$

The loss encourages a useful ordering rather than a particular absolute score.

Metric-aware methods weight or construct updates using the importance of ranking changes.[^pairwise]

### Build the training unit correctly

For Q1, grades A=3, B=1, C=0 yield three strict preferences. For Q2, D=3 and E=3 yield no strict grade preference between D and E. Do not manufacture an A>D preference from row order: they belong to different queries and their grades are equal anyway.

A train/validation split by query keeps these comparison groups intact. A time split asks a different question and requires features reconstructed as they were available at each request time.

## Check the Serving Feature Contract

A ranker trained with missing engagement values can respond differently to a real count of zero. Log feature coverage and the missing-value convention. An item with no impressions, an observed item with zero clicks, and a failed feature-store lookup describe three different states, even when an implementation later maps some of them to the same model input.

Before comparing algorithms, establish that feature names, units, windows, and preprocessing match between training and serving. A better offline loss does not compensate for a feature contract that changes at deployment.

## Exercise

Compare the same ranker on two candidate generators.

Report candidate recall separately from [[NDCG]], and explain why a higher ranking score on an easier candidate set does not establish a better whole search system.

## References & Useful Links

- [LightGBM ranker](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRanker.html) — Grouped ranking interface.

[^1]: [XGBoost FAQ: How to deal with missing values](https://xgboost.readthedocs.io/en/stable/faq.html) — Missing values and learned default branch directions in tree boosters; `gblinear` treats missing as zero.

[^pairwise]: [XGBoost: Learning to rank tutorial](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — LambdaMART default objective, sorted `qid` layout, pair construction, effective pairs, group-aware cross-validation, distributed-training caveats, and 2.0 default changes.

[^params]: [XGBoost parameters: learning to rank](https://xgboost.readthedocs.io/en/stable/parameter.html) — `rank:ndcg`/`rank:map`/`rank:pairwise`, `lambdarank_*` parameters, `ndcg_exp_gain`, and ranking evaluation metrics.
