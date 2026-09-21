# Feature Selection

#search-eng

## Purpose

Feature selection retains original variables to reduce storage, computation, or statistical complexity. It differs from constructing new components through [[PCA]]. There is no mandatory universal preprocessing order: fit the entire chosen workflow inside training folds.

## Method Families

| Family | Mechanism | Limitation |
|---|---|---|
| Unsupervised | Ignore labels, for example remove constant columns | Low variance does not mean low predictive value |
| Filter | Score relationships, for example F tests or mutual information | Univariate scores can miss interactions |
| Wrapper | Evaluate subsets with an estimator, including forward selection or RFE | Search is costly and generally not globally optimal |
| Embedded | Selection arises during fitting, for example L1 sparsity | Depends on model, scale, and penalty |

Pearson correlation captures linear association. [[Spearman Correlation]] and [[Kendall's Tau]] measure rank association; sample size alone does not dictate one. Mutual information can capture nonlinear dependence but must be estimated. Chi-square selection in scikit-learn expects suitable nonnegative features; an F test has different assumptions.

Correlated predictors are not automatically disposable. They may differ in freshness, missingness, or robustness. L2 regularisation usually shrinks coefficients without selecting exact zeros.

## Tools and Example

`SelectKBest`, `SelectPercentile`, and `GenericUnivariateSelect` control univariate selection. `RFE` recursively removes features; `SelectFromModel` thresholds model-derived importance. `VarianceThreshold` removes columns below a variance threshold.

```python
import numpy as np
X = np.array([[1., 0., 2.], [1., 1., 3.], [1., 0., 4.]])
keep = X.var(axis=0) > 0
assert keep.tolist() == [False, True, True]
```

This illustrates zero-variance removal, not a trained predictive selector. Fit selectors on training data, then apply the same mask to validation/serving data.

## Search Exercise

Remove one expensive feature, retrain the ranker, and compare [[Search Evaluation|quality]] plus latency. Explain why a low [[Feature Importance|importance]] score alone does not approve removal.

## References & Useful Links

- [Scikit-learn feature selection](https://scikit-learn.org/stable/modules/feature_selection.html) — Primary reference for the explanation above.

- [VarianceThreshold](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html) — Variance-based removal.
- [RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html) — Recursive elimination and estimator requirements.
