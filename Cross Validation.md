# Cross Validation

#search-eng

## Overview

Cross-validation evaluates a learning procedure across multiple training/validation splits. It estimates generalisation under the split assumptions; it does not guarantee absence of overfitting or leakage. [^1]

## K-Fold Procedure

Divide examples into $k$ folds. For each fold, train on the others and evaluate on that fold. Aggregate the validation results. Fit all learned preprocessing inside each training fold. See [[K Fold Cross Validation]] for split choices and computational cost.

## Choose the Split for the Task

- **Ordinary K-fold:** Appropriate when its exchangeability assumptions fit the data.
- **Stratified folds:** Preserve approximate class proportions; they do not solve group or time leakage.
- **Grouped folds:** Keep related examples, such as all rows for a held-out query, together.
- **Time-aware splits:** Evaluate on later data when the deployment question concerns the future. [^1]

Do not shuffle automatically. Scikit-learn's `KFold` and `StratifiedKFold` default to `shuffle=False`; specify it explicitly when shuffling is appropriate. [^1]

## Search Example

If ten rows belong to one query, distributing them over random folds can measure performance on already encountered query patterns. Grouping by query asks a different question about unseen queries. Neither split substitutes for describing the intended deployment.

## Related Notes

- [[Model Evaluation]] — Selection versus final assessment.
- [[Data Leakage]] — Invalid features and preprocessing contamination.
- [[Stratified K Fold Cross Validation]] — Current pipeline example and limits of stratification.

## References & Useful Links

[^1]: [Scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — K-fold, grouping, stratification, and time-aware splitting.
