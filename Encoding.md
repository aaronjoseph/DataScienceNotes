# Encoding

#search-eng

## Represent Categories Without Inventing Meaning

Encoding turns values into a representation a model can consume. This is broader than learned [[Embeddings]]. Choose representations based on category semantics and the estimator, not a rule that every tree should receive arbitrary integers.

| Tool | Use | Caution |
|---|---|---|
| `LabelEncoder` | Encode target labels `y` | Not the general transformer for categorical feature columns |
| `OrdinalEncoder` | Encode input categories, with explicit order when meaningful | Arbitrary numeric order can introduce artificial distances or thresholds |
| `OneHotEncoder` | Separate indicator columns for categories | High cardinality increases width; plan unseen-category handling |
| `TargetEncoder` | Encode categories using target statistics | Must avoid leaking an example's target into its own features |

A postal code is categorical even when written as digits. For small fixed mappings, pandas `Series.map` is transparent; `pandas.get_dummies` is convenient for exploration, but independently encoding train and test requires column alignment.

## Practical Example

```python
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
train = [['red'], ['blue'], ['red']]
encoded = encoder.fit_transform(train)
print(encoder.get_feature_names_out(['colour']))
print(encoder.transform([['green']]))  # unknown category: all zeros
```

Fit category discovery only on training data. `min_frequency` and `max_categories` can group infrequent categories; an arbitrary top-ten rule is not always appropriate. Target encoding requires cross-fitting or another leakage-safe construction; scikit-learn's `fit_transform` provides cross-fitting and is intentionally different from `fit(...).transform(...)` on training rows.

## Search Exercise

For a [[Learning to Rank]] model, distinguish a query ID used for grouping from a feature encoding. Explain how a category's click-rate encoding can leak future traffic and inherit [[Click Bias]]. See [[Data Leakage]] and [[Feature Engineering]].

## References & Useful Links

- [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) — Estimator behaviour.
- [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html) — Estimator behaviour.
- [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) — Estimator behaviour.
- [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html) — Estimator behaviour.
