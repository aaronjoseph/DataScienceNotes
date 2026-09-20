# XGBoost

#search-eng

## Core Idea

XGBoost builds an additive model through successive boosting rounds. Gradient and curvature information guide tree construction for supported objectives. Rounds depend on the current model, even though work inside a round can be parallelised. This differs from treating all trees as independent in a random forest.

## Mechanisms and Controls

Tree depth/leaves, learning rate, regularisation, row sampling, and column sampling affect fit and cost. `tree_method` selects algorithms; `grow_policy` controls growth where supported. XGBoost is not restricted to one fixed depth-first pruning description.

Missing-value handling can learn a default branch at a split; this is not equivalent to filling in the unknown value. Confirm how the chosen input representation encodes missingness and zeros. Sparse input and dense zero values need not mean the same thing.

## Learning to Rank

`XGBRanker` supports `rank:ndcg`, `rank:pairwise`, and `rank:map`, with distinct objective semantics. Group query–document rows by query; in the `qid` interface, supply sorted query IDs aligned with the rows. Use labels compatible with the objective: MAP is associated with binary relevance, while NDCG can express grades.

An example `qid=[10,10,20,20,20]` identifies two groups of sizes two and three. It is not a numeric relevance feature. Keep all rows of a query together when splitting. See [[Learning to Rank]], [[Light GBM]], and [[NDCG]].

## Exercise

Explain why swapping document rows without swapping their query IDs corrupts pair construction. Evaluate identical candidate sets and label definitions before attributing quality differences to a boosting library.

Related task notes: [[XGBoost Regression]] and [[XGBoost Classification]]. Documentation checked 20 September 2026; record package version and configuration with experiments.

## References & Useful Links

- [XGBoost parameters](https://xgboost.readthedocs.io/en/stable/parameter.html) — Objectives, growth, and regularisation.
- [XGBoost learning to rank](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — Query groups and ranking objectives.
