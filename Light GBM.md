# Light GBM

#search-eng

## Core Idea

LightGBM is a tree-boosting library. Its histogram-based splitting and leaf-wise growth can be efficient, but runtime and quality depend on data, settings, hardware, and the comparison. Leaf-wise growth chooses a promising leaf rather than expanding every node at the same depth; control complexity to avoid overfitting.

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

## Search Ranking

`LGBMRanker` supports objectives such as `lambdarank` and `rank_xendcg`. Labels encode relevance grades. Rows for each query must be contiguous, and `group` contains **group sizes**, not a query-ID value for every row. For query sizes `[3, 2]`, five feature rows are required. Validation needs its own group sizes.

Separate queries or time periods before fitting; document-level random splitting can leak query context. Choose metric cutoffs and label gains consistent with [[NDCG]] and [[Learning to Rank]].

## Exercise

Arrange six examples from three queries into contiguous groups. Write their group-size vector and check that it sums to six. Compare with the `qid` convention in [[XGBoost]].

Documentation checked 20 September 2026; pin the installed library version when implementing.

## References & Useful Links

- [LightGBM features](https://lightgbm.readthedocs.io/en/latest/Features.html) — Histogram and leaf-wise algorithms.
- [Parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html) — Parameter names and objectives.
- [LGBMRanker](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRanker.html) — Query groups and fitting API.
