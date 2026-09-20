# Learning to Rank

#search-eng

## Core Idea

Learning to rank trains a scoring or ordering model for documents **within a query context**. Typical data contains a query ID, candidate document, query–document features, and a relevance grade. Candidate generation remains a separate constraint: the model cannot rank an item it never receives.

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

[[Light GBM]] supplies contiguous group sizes; [[XGBoost]] supports aligned sorted `qid` values. Check the library's objective and label requirements. Click labels need [[Click Bias|bias analysis]].

## Exercise

Compare the same ranker on two candidate generators. Report candidate recall separately from [[NDCG]], and explain why a higher ranking score on an easier candidate set does not establish a better whole search system.

## References & Useful Links

- [XGBoost ranking tutorial](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — LambdaMART and query-group requirements.
- [LightGBM ranker](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRanker.html) — Grouped ranking interface.
