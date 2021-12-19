- `Hyperparameter`  is a parameter whose value is set before the learning process begins
- This is not updated in each training steps
- And it is not scalable

# Grid Search
The idea of grid search is to search the hyper-parameter space within the grid-values. The grid value defines for each hyperparameter which values should be tested.

In all does an exhaustive search on the specified parameters.

```py
from sklearn.model_selection import GridSearchCV

param_grid = [
    # try 12 (3×4) combinations of hyperparameters
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    # then try 6 (2×3) combinations with bootstrap set as False
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
  ]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training 
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)

# Best Parameters
grid_search.best_params_
```
# Randomized Search

In random search, the process is as follows
1. Take a random point on the grid and measure the objective function
2. If the value is better than the best one acheived so far, keep the point in memory
3. Repeat for a certain, pre-defined number of times

```py
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_distribs = {
        'n_estimators': randint(low=1, high=200),
        'max_features': randint(low=1, high=8),
    }

forest_reg = RandomForestRegressor(random_state=42)
rnd_search = RandomizedSearchCV(forest_reg, param_distributions=param_distribs,
                                n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
rnd_search.fit(housing_prepared, housing_labels)
``