# PCA

#search-eng

## Core Idea

Principal component analysis finds orthogonal linear directions of greatest variance in centred data. Keeping the first k directions gives a rank-k representation. “Most information” here means retained variance or squared reconstruction error, not guaranteed task relevance.

## Mechanics

For $X\in\mathbb R^{n\times d}$, subtract each training-column mean to form $X_c$. Its sample covariance is $C=X_c^TX_c/(n-1)$ for $n>1$. Entry $C_{ij}$ is a covariance, not generally a correlation. Columns need not be statistically independent.

Eigenvectors of C provide principal directions; eigenvalues give variance along them. Project onto the first k directions: $Z=X_cV_k$. These are new combinations of variables, not simply retained original columns. [[Singular Value Decomposition|SVD]] can compute the directions without explicitly constructing C.

Standardising feature scales is a modelling choice: appropriate when units would otherwise dominate, but not compulsory for every PCA problem. Fit centring, scaling, and components only on training data.

## Worked Example

```python
import numpy as np
X = np.array([[1., 1.], [2., 2.], [3., 3.]])
mean = X.mean(axis=0)
U, s, Vt = np.linalg.svd(X - mean, full_matrices=False)
Z = (X - mean) @ Vt[:1].T
reconstructed = Z @ Vt[:1] + mean
assert np.allclose(reconstructed, X)
assert np.isclose(s[0]**2 / (s**2).sum(), 1)
```

Both coordinates vary together, so one component reconstructs all centred variation. Component signs may flip without changing the reconstruction.

## Exercise

Could a low-variance feature encode an important product constraint? Explain why removing it based only on variance might hurt [[Search Ranking]]. See [[Feature Scaling]] and [[Dimensionality Reduction]].

## References & Useful Links

- [PCA estimator and centring behaviour](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) — Primary reference for the explanation above.

Previously saved reading (preserved; not used to verify this revision):
- [Original PCA illustration](https://twitter.com/Jeande_d/status/1417093660244594688?s=20)
