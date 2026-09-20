# Feature Scaling

#search-eng

## Overview

Scaling changes feature magnitudes. It matters for many distance-based and optimisation-based models, including [[KNN]] and some linear models. It is not universally required for every model or ensemble. Keep preprocessing identical between training and serving. [^1]

## Two Common Transformations

**Standardisation:**

$$z=\frac{x-\mu_{train}}{\sigma_{train}}$$

This centres a nonconstant feature and rescales its spread. It is sensitive to outliers; it does not make the distribution normal. [^1]

**Min–max scaling to the training range [0,1]:**

$$x'=\frac{x-x_{min,train}}{x_{max,train}-x_{min,train}}$$

New values outside the training range can transform outside [0,1] unless clipping is enabled. Constant features require a defined implementation policy. [^2]

## Python Example

```python
from sklearn.preprocessing import StandardScaler

train = [[10.0], [20.0], [30.0]]  # Rows are samples; columns are features.
test = [[40.0]]
scaler = StandardScaler().fit(train)
scaled_test = scaler.transform(test)
print(scaled_test.round(4))  # Expected: [[2.4495]]
```

The example is illustrative unless explicitly executed in the current environment. Do not refit on test data; see [[Data Leakage]].

## Search Connection

For a learned ranker, document the transformation of each feature and missing-value policy. Scaling each dimension is different from normalising an entire embedding vector to unit length for [[Cosine Similarity]].

## References & Useful Links

[^1]: [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) — Standardisation and outlier sensitivity.
[^2]: [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) — Feature ranges and clipping.
