---
note_type: concept
search_stage: ranking
tags:
  - gcp
  - search-eng
---

BigQuery ML brings model training and inference into SQL-oriented workflows. Use it when the data and supported model fit the problem. The important lifecycle is **define labels → construct valid features → split → train → evaluate → predict → monitor**, not just a successful `CREATE MODEL` statement.

## Define the example before training

Assume `example_project.ml.destination_examples` exists in a compatible location and contains one row per eligible recommendation candidate:

- `example_date DATE` and `example_id STRING` identify the observation.
- `prior_visits INT64` and `hours_since_visit FLOAT64` use only history available at recommendation time.
- `is_favorite BOOL` is the favorite status at that time.
- `selected INT64` is 0 or 1 after a fixed observation window has completed.

Exclude rows whose outcome window is incomplete; missing outcomes are not automatically negatives. The SQL below is a template requiring prepared data, permissions, and billing. It was not executed.

## 1. Train a baseline

```sql
CREATE MODEL `example_project.ml.destination_choice_v1`
OPTIONS (
  model_type = 'LOGISTIC_REG',
  input_label_cols = ['selected'],
  data_split_method = 'NO_SPLIT'
) AS
SELECT prior_visits, hours_since_visit, is_favorite, selected
FROM `example_project.ml.destination_examples`
WHERE example_date >= DATE '2026-08-01'
  AND example_date < DATE '2026-09-01';
```

`LOGISTIC_REG` performs classification; `LINEAR_REG` is for numeric regression targets. `NO_SPLIT` uses all supplied rows for training because the example deliberately supplies a separate later evaluation period.[^create]

For tuning, add a validation period and reserve another untouched test period. Do not repeatedly tune against the final test set. Connect this to [[Data Leakage]] and [[Cross Validation]].

## 2. Evaluate on later data

```sql
SELECT *
FROM ML.EVALUATE(
  MODEL `example_project.ml.destination_choice_v1`,
  (SELECT prior_visits, hours_since_visit, is_favorite, selected
   FROM `example_project.ml.destination_examples`
   WHERE example_date >= DATE '2026-09-01'
     AND example_date < DATE '2026-09-08')
);
```

Providing evaluation data makes the intended holdout explicit. Classification metrics depend on the model and threshold; inspect errors by relevant user and context segments.[^evaluate]

A candidate-level classifier is not a complete recommendation evaluation. For top-three destinations, also define the candidate set, per-request ranking metric, cold-start cohort, and missing-history policy. Compare with [[Search Evaluation]] before claiming a better user experience.

## 3. Predict with the same feature contract

```sql
SELECT *
FROM ML.PREDICT(
  MODEL `example_project.ml.destination_choice_v1`,
  (SELECT example_id, prior_visits, hours_since_visit, is_favorite
   FROM `example_project.ml.destination_examples`
   WHERE example_date = DATE '2026-09-08')
);
```

Input feature names and types must match training requirements. Extra identifiers can pass through for joining predictions back to examples. Inspect class probabilities as well as hard labels when constructing a ranking.[^predict]

## Production handoff and failure modes

Version feature definitions, training data, model, and evaluation results together. Store batch predictions with their model version and intended validity period. If online serving is required, measure the selected serving path rather than assuming a warehouse query meets the API deadline.

Watch for future-history leakage, skew between training and serving transformations, imbalanced labels, repeated users crossing a supposedly independent split, and stale favorite status. Use [[Feature Store]] to reason about freshness and historical availability.

## Exercise

A feature counts visits over the full calendar month containing the label. Show why that leaks future information for a recommendation made midway through the month.

## References & Useful Links

[^create]: [CREATE MODEL for generalized linear models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm) — Model types, labels, and data-splitting options.
[^evaluate]: [ML.EVALUATE](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) — Explicit evaluation inputs and classification behavior.
[^predict]: [ML.PREDICT](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) — Input compatibility and prediction outputs.
