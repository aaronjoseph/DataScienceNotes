# Hyperparameter Tuning

#search-eng

## Purpose

Hyperparameters configure the learning procedure: tree count, depth, regularisation, or learning rate, for example. They are distinct from model parameters fitted during training, although schedules and adaptive procedures can change some settings during a run. They are not inherently “unscalable”.

Grid search evaluates a specified finite set. Randomised search samples from lists or distributions under a trial budget; it is not limited to points on a fixed grid. Compare using the same validation design and metric. More trials can overfit validation choices, so retain a final test set or use nested validation.

## Self-Contained Search Example

Requires NumPy, SciPy, and scikit-learn. Synthetic data replaces the earlier undefined housing variables. This demonstrates API use, not a meaningful model benchmark.

```python
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, KFold
from scipy.stats import randint
X, y = make_regression(n_samples=120, n_features=8, noise=5, random_state=42)
cv = KFold(n_splits=5, shuffle=True, random_state=42)
forest = RandomForestRegressor(random_state=42, n_jobs=1)
grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]
search = GridSearchCV(forest, grid, cv=cv, scoring='neg_mean_squared_error')
search.fit(X, y)
assert len(search.cv_results_['params']) == 18
print(search.best_params_, -search.best_score_)
random_search = RandomizedSearchCV(
    forest, {'n_estimators': randint(1, 200), 'max_features': randint(1, 8)},
    n_iter=10, cv=cv, scoring='neg_mean_squared_error', random_state=42)
random_search.fit(X, y)
print(random_search.best_params_, -random_search.best_score_)
```

The grid uses 18 configurations × five folds = 90 validation fits, plus one final refit under the default `refit=True`. Random search uses 50 validation fits plus a refit. Negative MSE follows scikit-learn's higher-is-better scoring convention; negate it to report MSE. `randint` excludes its upper bound.

## Search Exercise

For [[Learning to Rank]], keep query groups intact and tune a query-level metric. Do not pass ranking rows into this regression example and assume the split is valid. Fit any learned preprocessing within the folds; see [[Data Leakage]] and [[Cross Validation]].

## References & Useful Links

- [Scikit-learn tuning guide](https://scikit-learn.org/stable/modules/grid_search.html) — Primary reference for the explanation above.
- [GridSearchCV API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) — Primary reference for the explanation above.
