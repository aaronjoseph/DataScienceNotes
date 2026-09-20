# Stratified K Fold Cross Validation

#search-eng

## Core Idea

Stratification approximately preserves each class's proportion across folds. It does not make classes equally frequent and does not fix label bias, dependence, or leakage. Ensure enough examples of the smallest class for the chosen fold count; inspect the actual folds.

## Executable Example

This example uses scikit-learn's bundled Iris data, without a network download. Each fold fits its own scaler. Replace the classifier with another estimator while keeping the split and metric fixed for a controlled comparison.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
X, y = load_iris(return_X_y=True)
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
print(scores, scores.mean())
```

Use the current `sklearn.model_selection` namespace. A plain stratified splitter knows nothing about time or users. For [[Learning to Rank]], preserving query groups takes priority over balancing individual document labels; see [[K Fold Cross Validation]] and [[Data Leakage]].

## Exercise

For 90 negatives and 10 positives, five folds contain approximately 18 negatives and two positives each. Explain why oversampling before splitting can put duplicated examples on both sides of evaluation.

## References & Useful Links

- [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) — Class proportions and limitations.
