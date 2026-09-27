---
tags:
  - "search-eng"
  - "ds-foundations"
---

## Core Idea

XGBoost builds an additive model through successive boosting rounds. Gradient and curvature information guide tree construction for supported objectives. Rounds depend on the current model, even though work inside a round can be parallelised. This differs from treating all trees as independent in a random forest.

## Mechanisms and Controls

Tree depth/leaves, learning rate, regularisation, row sampling, and column sampling affect fit and cost. `tree_method` selects algorithms; `grow_policy` controls growth where supported. XGBoost is not restricted to one fixed depth-first pruning description.

Missing-value handling can learn a default branch at a split; this is not equivalent to filling in the unknown value. Confirm how the chosen input representation encodes missingness and zeros. Sparse input and dense zero values need not mean the same thing.

## Learning to Rank

XGBoost provides three ranking objectives: `rank:ndcg` (the default, LambdaMART with NDCG-weighted pair gradients), `rank:map` (LambdaMART for binary labels), and `rank:pairwise` (the unscaled RankNet loss).[^ltr] Group query–document rows by query; in the `qid` interface, supply sorted query IDs aligned with the rows. Use labels compatible with the objective: MAP needs binary relevance, while NDCG can express grades. With the default exponential gain (`ndcg_exp_gain=true`), grades cannot exceed 31.[^params]

An example `qid=[10,10,20,20,20]` identifies two groups of sizes two and three. It is not a numeric relevance feature. Keep all rows of a query together when splitting.

Pair construction is controlled by `lambdarank_pair_method` (default `topk`) and `lambdarank_num_pair_per_sample`; position debiasing for click labels by `lambdarank_unbiased`. The data layout, parameter choices, an executed example, and ranking-specific pitfalls are in [[Learning to Rank#Training a LambdaMART Ranker with XGBoost]]. See also [[Light GBM]] and [[NDCG]].

## Exercise

Explain why swapping document rows without swapping their query IDs corrupts pair construction. Evaluate identical candidate sets and label definitions before attributing quality differences to a boosting library.

Related task notes: [[XGBoost Regression]] and [[XGBoost Classification]]. Documentation checked 20 September 2026; ranking parameters rechecked 27 September 2026, and the ranking example executed with XGBoost 3.0.5. Record package version and configuration with experiments.

## References & Useful Links

[^ltr]: [XGBoost: Learning to rank tutorial](https://xgboost.readthedocs.io/en/stable/tutorials/learning_to_rank.html) — Query groups, LambdaMART default, RankNet `rank:pairwise`, and sorted `qid` layout.
[^params]: [XGBoost parameters](https://xgboost.readthedocs.io/en/stable/parameter.html) — Objectives, growth, regularisation, `lambdarank_*` parameters, and `ndcg_exp_gain`.
