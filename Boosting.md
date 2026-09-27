---
tags:
  - "ds-foundations"
---

Boosting works on the principle that, it leverages multiple weak learners to build a strong learner.

Here, hard to classify instances are given more emphasis in each sequential step. [[AdaBoost]] does this by increasing their sample weights; [[Gradient Boosting Machines (GBM)|gradient boosting]] does it by fitting each new tree to the current residual errors (more generally, the negative gradients of the loss), which are largest for the worst-fitted records.

Boosting differs from bagging in the order of execution, boosting is implemented sequentially, while bagging is done parallelly

---
### Algorithms

- [[AdaBoost]]
- [[Gradient Boosting Machines (GBM)]]
- [[XGBoost]]
- [[Light GBM]]
- [[CatBoost]]
- BrownBoost
- MadaBoost
- LogitBoost

---
### Code

```py
import numpy as np
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(0)
X = rng.uniform(-3, 3, size=(200, 1))
y = X[:, 0] ** 2 + rng.normal(scale=0.3, size=200)
X_new = np.array([[0.0], [2.0]])

tree_reg1 = DecisionTreeRegressor(max_depth=2)
tree_reg1.fit(X,y)

# Training the second DecisionTreeRegressor on residual erros
y2 = y-tree_reg1.predict(X)
tree_reg2 = DecisionTreeRegressor(max_depth=2)
tree_reg2.fit(X,y2)

# Training 3rd Regressor
y3 = y2-tree_reg2.predict(X)
tree_reg3 = DecisionTreeRegressor(max_depth=2)
tree_reg3.fit(X,y3)

y_pred = sum(tree.predict(X_new) for tree in (tree_reg1, tree_reg2, tree_reg3))

# Approach 2: the same three-tree ensemble with scikit-learn
from sklearn.ensemble import GradientBoostingRegressor

gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0)
gbrt.fit(X,y)
```

The original version fitted `tree_reg2` a second time instead of `tree_reg3`, so the third tree was never trained. With `learning_rate=1.0` and squared error, Approach 2 fits the same residual sequence, starting from the mean of `y` instead of zero. With scikit-learn 1.9.1, both approaches predicted `[0.489, 3.071]` for `X_new`.

Optimized version of Gradient Boosting is available in XGBoost

```py
import xgboost
xgb_reg = xgboost.XGBRegressor()
xgb_reg.fit(X_train, y_train)
y_pred = xgb_reg.predict(X_val)

# Early stopping is a constructor argument in current XGBoost versions
xgb_reg = xgboost.XGBRegressor(early_stopping_rounds=2)
xgb_reg.fit(X_train, y_train,
			eval_set=[(X_val,y_val)])
y_pred = xgb_reg.predict(X_val)
```

Passing `early_stopping_rounds` to `fit()` raised `TypeError` in XGBoost 3.2.0; passing it to the constructor worked. `X_train`, `X_val`, `y_train`, and `y_val` stand for your own train and validation split. The underlying mathematics is in [[XGBoost#The Math, Step by Step|XGBoost]].
