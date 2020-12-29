Boosting works on the principle that, it leverages multiple weak learners to build a strong learner.

Here, hard to classify instances are given more weights. Therefore in the sequantial learning step, hard to learn records are given more emphasis, and therefore learnt.

Boosting differs from bagging in the order of execution, boosting is implemented sequentially, while bagging is done parallelly

---
### Algorithms

- [[AdaBoost]]
- [[Gradient Boosting (GBM)]]
- [[XGBoost]]
- [[Light GBM]]
- [[CatBoost]]

---
### Code

```py
from sklearn.tree import DecisionTreeRegressor

tree_reg1 = DecisionTreeRegressor(max_depth=2)
tree_reg1.fit(X,y)

# Training the second DecisionTreeRegressor on residual erros
y2 = y-tree_reg1.predict(X)
tree_reg2 = DecisionTreeRegressor(max_depth=2)
tree_reg2.fit(X,y2)

# Training 3rd Regressor
y3 = y2-tree_reg2.predict(X)
tree_reg3 = DecisionTreeRegressor(max_depth=2)
tree_reg2.fit(X,y3)

y_pred = sum(tree.predict(X_new) for tree in (tree_reg1, tree_reg2, tree_reg3))

#####################################################################
Approach 2
#####################################################################

from sklearn.ensemble import GradientBoostingRegressor

gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0)
gbrt.fit(X,y)
```

Optimized version of Gradient Boosting is available in XGBoost

```py
import xgboost
xgb_reg = xgboost.XGBRegressor()
xgb_reg.fit(X_train, y_train)
y_pred = xgb_reg.predict(X_val)

# The library comes with advanced feature such as early_stopping
xgb_reg.fit(X_train, y_train,
			eval_set=[(X_val,y_val)],early_stopping_rounds=2)
y_pred = xgb_reg.predict(X_val)
```
