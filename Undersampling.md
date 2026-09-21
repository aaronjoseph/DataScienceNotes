# Undersampling

#search-eng

## Core Idea

Undersampling removes or selects observations, commonly from a majority class. It does **not** increase the minority count. Random undersampling is simple but can discard useful information; neighbour-based selection changes which majority examples remain.[^1]

## Worked Count Example

Starting with 100 majority and 20 minority examples, retaining 25 majority examples gives a minority-to-majority ratio of 0.8. The output has 45 rows, and no new minority observations have been created.

## Current API Example

Requires NumPy and imbalanced-learn. This synthetic example illustrates API and counts, not predictive quality. Apply it only to a training partition.

```python
import numpy as np
from imblearn.under_sampling import RandomUnderSampler, NearMiss
rng = np.random.default_rng(42)
X_train = rng.normal(size=(120, 2))
y_train = np.array([0] * 100 + [1] * 20)
sampler = RandomUnderSampler(sampling_strategy=0.8, random_state=42)
X_resampled, y_resampled = sampler.fit_resample(X_train, y_train)
assert np.bincount(y_resampled).tolist() == [25, 20]
# Alternative: select majority examples using neighbour distances.
near_miss = NearMiss(sampling_strategy=0.8, version=1)
X_near, y_near = near_miss.fit_resample(X_train, y_train)
assert np.bincount(y_near).tolist() == [25, 20]
```

Use `fit_resample`, replacing the obsolete `fit_sample` calls. Float ratios are a binary-classification convention here, not the desired fraction of all output rows. NearMiss depends on distance geometry, so feature units matter.[^1]

API names checked against the linked documentation on 21 September 2026. The example was syntax-checked but not executed locally because scikit-learn and imbalanced-learn are unavailable.

## Search Exercise

Compare randomly dropping easy negatives with retaining difficult negatives for a relevance classifier. Which evaluation set remains representative of traffic? Explain why the selected training distribution should not silently become the evaluation distribution. See [[Imbalanced Classification]], [[Sampling]], and [[Feature Scaling]].

## References & Useful Links

[^1]: [Imbalanced-learn undersampling guide](https://imbalanced-learn.org/stable/under_sampling.html) — Random and neighbour-based selection.
