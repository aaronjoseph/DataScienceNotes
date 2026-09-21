# Feature Importance

#search-eng

## What Importance Means

Feature importance describes a fitted model's dependence on inputs under a particular method, dataset, and metric. It does **not** establish that changing a feature causes the outcome. Different models or correlated substitutes can assign different importance to the same variable.

## Methods

- **Coefficients:** interpret direction and scale in linear models; compare magnitudes only with units and transformations in mind. For [[Logistic Regression]], coefficients affect log-odds, not probability by a constant amount.
- **Tree impurity importance:** attributes training split improvements to features. It can favour high-cardinality features and need not reflect held-out performance.
- **[[Permuatation Importance|Permutation importance]]:** measure score degradation when a feature is shuffled. It can apply to any compatible estimator, including neural models, rather than only one model family.

Correlated features can mask one another under permutation. Shuffling may create unrealistic combinations; results depend on the chosen data and metric. Model stochasticity is one source of variation, not a reason every tree necessarily changes between runs.

## Reading Estimator Outputs

Illustrative inspection, assuming a fitted compatible estimator:

```python
# Linear estimators: rows may represent classes or output targets.
coefficients = model.coef_
# Tree estimators exposing impurity-based importance:
# importance = model.feature_importances_
```

This is an API illustration, not a standalone executable example. Do not flatten multiclass coefficients into a single unexplained ranking.

## Search Exercise

A popularity feature is important in a click-trained ranker. Explain why this might reflect exposure bias, correlation, or a useful signal. Compare an ablation using fixed candidates and held-out [[NDCG]], then inspect [[Click Bias]]. Use [[Feature Selection]] only after validating the proposed removal.

## References & Useful Links

- [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html) — Primary reference for the explanation above.
