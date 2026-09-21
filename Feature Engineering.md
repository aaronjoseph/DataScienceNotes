# Feature Engineering

#search-eng

## Purpose

Feature engineering makes raw data usable for a model through cleaning, extraction, transformation, and construction. It can improve prediction or efficiency, but additional features are hypotheses to test, not automatic improvements. The earlier attributed quotation is treated here as a paraphrased motivation because no original quotation source was recorded.

## A Practical Workflow

1. Define the prediction target and what information exists at prediction time.
2. Check schema, missing values, units, and joins.
3. Construct representations such as buckets, [[Bag of Words]], [[Encoding]], [[Feature Scaling]], or [[Feature Cross|crosses]].
4. Fit learned transformations on training partitions only.
5. Compare a baseline using held-out quality and serving cost.
6. Version transformations and monitor training/serving consistency.

```mermaid
flowchart LR
    A[Define target and available data] --> B[Construct features]
    B --> C[Fit within training split]
    C --> D[Validate quality and cost]
    D --> E[Deploy and monitor]
    E --> A
```

## Where Transformations Run

Offline precomputation can reduce serving cost, but requires freshness and consistent transformation logic. In-model transformations can package logic with the model but increase inference work. Neither location guarantees correctness. Avoid fitting preprocessing on the entire dataset before evaluation.

[[Dimensionality Reduction]] and [[PCA]] may reduce coordinates; [[T-SNE]] is primarily an exploratory visualisation tool, not a default serving transform.

## Search Exercise

Construct a query–product feature for exact brand match and another for historical conversion. State when each is available, how missing values differ from zero, and how future conversions could cause [[Data Leakage]]. Evaluate the features in [[Learning to Rank]] before adopting them.

## References & Useful Links

- [Google rules of machine learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — Primary reference for the explanation above.
