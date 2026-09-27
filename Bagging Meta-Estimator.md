---
tags:
  - "ds-foundations"
---

Bagging meta-estimator is scikit-learn's general implementation of [[Bagging]]; it can be used for both classification and regression. The steps followed are

1. Random subsets are created from the original dataset
2. The subset of the dataset includes all features (by default, `max_features=1.0`)
3. A user-specified base estimator is fitted on each of these smaller sets
4. Predictions from each model are combined to get the final results

```py
from sklearn.ensemble import BaggingClassifier
from sklearn import tree

model = BaggingClassifier(estimator=tree.DecisionTreeClassifier(random_state=1))
model.fit(x_train,y_train)
model.score(x_test, y_test)
```

---

### Parameters 

- `estimator` (called `base_estimator` before scikit-learn 1.2)
	- Defines the base estimator to fit on random subsets of the dataset
	- When nothing is specified, the base estimator is a decision tree
- `n_estimators`
	- No of base estimators to be created
	- The number of estimators should be carefully tuned as a large number would take a very long time to run, while a very small number might not provide the best results
- `max_samples`
	- This parameter controls the size of the subset
	- It is the maximum number of samples to train each base estimator
- `max_features`
	- Controls the number of features to draw from the whole dataset
	- It defines the maximum number of features used to train each base estimator (drawn without replacement unless `bootstrap_features=True`)

## References & Useful Links

- [scikit-learn `BaggingClassifier` API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html) — Parameter names and defaults, including the `base_estimator` to `estimator` rename in 1.2.