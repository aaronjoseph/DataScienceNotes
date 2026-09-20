# Model Evaluation

#search-eng

## Overview

Model evaluation estimates performance on the intended use case. Model selection compares configurations; algorithm selection compares modelling approaches. Keep the data used for those decisions distinct from the final assessment where possible. [^1]

## Working Procedure

1. Define the prediction task, population, and metric.
2. Choose a split matching the deployment question: new queries, future traffic, or unseen entities can require different splits.
3. Fit preprocessing and the model using training data only.
4. Use validation or [[Cross Validation]] to select configurations.
5. Evaluate the selected procedure on held-out data and report uncertainty and failure slices. [^1]

## Search Example

A random split of query–document rows can place the same query on both sides. That may be appropriate for one question but does not establish generalisation to unseen queries. Write down the generalisation claim before selecting the split.

A classifier's accuracy is not the same as a search system's ranked utility. Use [[Search Evaluation]] and [[NDCG]] for search-specific protocols, alongside [[Latency vs Throughput]] and online outcomes where appropriate.

## Open Questions

- #TODO Work through nested validation and uncertainty estimation from the original paper, using a concrete ranking dataset. The overview here does not complete that deeper study.

## References & Useful Links

[^1]: [Raschka: Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning](https://arxiv.org/abs/1811.12808) — Original saved paper on evaluation methodology.
