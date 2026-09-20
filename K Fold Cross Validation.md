# K Fold Cross Validation

#search-eng

## Core Idea

Split observations into $K$ folds. Fit a fresh model on $K-1$ folds, evaluate on the held-out fold, and repeat until each fold has been held out. Summarise the fold scores and their variation; do not treat overlapping training sets as independent experiments.

K-fold estimates performance under the chosen sampling scheme. It neither prevents overfitting nor guarantees a better model. Tuning against the same folds can overfit the validation process; retain a final test set or use nested validation. Fit preprocessing separately inside each training fold using a pipeline.

## Choose the Split

- Independent observations: shuffled K-fold with a recorded seed can be appropriate.
- Class imbalance: [[Stratified K Fold Cross Validation]] approximately preserves label proportions.
- Repeated users, products, or queries: keep the relevant groups together.
- Future performance: train on past data and validate on later data.

For [[Learning to Rank]], document rows from one query must stay together. Decide whether the target is new queries, later traffic, or new users before choosing the grouping.

## Cost and Exercise

A configuration generally requires $K$ fits; tuning $M$ configurations costs approximately $KM$ fits before final refitting. This can be expensive for neural models, but expense is a tradeoff, not a prohibition.

With 100 independent examples and five folds, each fit trains on 80 and validates on 20. Explain why a scaler fitted on all 100 before splitting introduces [[Data Leakage]]. See [[Cross Validation]] for the broader workflow.

## References & Useful Links

- [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html) — Splitter behaviour and shuffling.
