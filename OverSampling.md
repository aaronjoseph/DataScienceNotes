# OverSampling

#search-eng

## Core Idea

Oversampling increases selected class counts by duplicating examples or generating synthetic examples. It need not make every class equally frequent. Duplicating a row changes its training influence without adding independent information.[^1]

## Methods

- **Random oversampling:** sample existing minority examples with replacement.
- **SMOTE:** interpolate between a minority example and a selected minority neighbour: $x_{new}=x_i+u(x_j-x_i)$, with $u\in[0,1]$.
- **ADASYN:** allocate more synthetic samples around minority points whose neighbourhood contains more majority examples. It is not simply SMOTE plus random noise, nor universally better.
- **SMOTETomek:** combine SMOTE with Tomek-link cleaning; cleaning can change the final class counts.[^1][^2]

Synthetic points can cross invalid regions or amplify noisy labels. Plain interpolation is inappropriate for arbitrary category IDs; choose representations and methods suited to the feature types.

## Current API Example

Requires NumPy and imbalanced-learn. Each sampler below independently starts from the same synthetic training set.

```python
import numpy as np
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN
from imblearn.combine import SMOTETomek
rng = np.random.default_rng(42)
X_train = rng.normal(size=(120, 2))
y_train = np.array([0] * 100 + [1] * 20)
random_sampler = RandomOverSampler(sampling_strategy=0.8, random_state=42)
X_over, y_over = random_sampler.fit_resample(X_train, y_train)
assert np.bincount(y_over).tolist() == [100, 80]
smote = SMOTE(sampling_strategy=0.8, random_state=42)
X_smote, y_smote = smote.fit_resample(X_train, y_train)
combined = SMOTETomek(sampling_strategy=0.8, random_state=42)
X_clean, y_clean = combined.fit_resample(X_train, y_train)
# ADASYN requires suitable minority neighbourhoods; it can fail without them.
adasyn = ADASYN(sampling_strategy=0.8, random_state=42)
```

The current method is `fit_resample` and the combined class is `SMOTETomek`, correcting the previous spelling. At ratio 0.8, 100 majority examples imply 80 minority examples before any cleaning.

API names checked against the linked documentation on 21 September 2026. The example was syntax-checked but not executed locally because scikit-learn and imbalanced-learn are unavailable.

## Search Exercise

Interpolation between products can produce an impossible price/size/type combination. Explain why duplicating a real labelled pair and synthesising a feature vector make different assumptions. Resample only inside training folds; keep an untouched evaluation distribution.[^3] See [[Undersampling]] and [[Imbalanced Classification]].

## Existing Illustration

![[Pasted image 5.png]]

## References & Useful Links

[^1]: [Imbalanced-learn oversampling](https://imbalanced-learn.org/stable/over_sampling.html) — SMOTE, ADASYN, and sampling geometry.
[^2]: [SMOTETomek API](https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTETomek.html) — Combination method and parameters.
[^3]: [Resampling pitfalls](https://imbalanced-learn.org/stable/common_pitfalls.html) — Split before resampling.
