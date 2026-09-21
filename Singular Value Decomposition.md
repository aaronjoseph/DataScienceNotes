# Singular Value Decomposition

#search-eng

## Definition

For a real matrix $A\in\mathbb R^{m\times n}$, reduced SVD writes:

$$A=U\Sigma V^T.$$

With $r=\min(m,n)$, U is $m\times r$, $\Sigma$ is $r\times r$, and V is $n\times r$. Singular values are nonnegative and ordered; columns of U and V are orthonormal. Numerical rank can be smaller than r.

Keeping k largest singular values yields $A_k=U_k\Sigma_kV_k^T$, a best rank-at-most-k approximation under Frobenius norm. SVD itself does not require centring; [[PCA]] applies it to centred data. Sparse text pipelines commonly use uncentred truncated SVD for latent semantic analysis.

## Worked Example

```python
import numpy as np
A = np.diag([3., 1.])
U, s, Vt = np.linalg.svd(A, full_matrices=False)
A1 = (U[:, :1] * s[:1]) @ Vt[:1]
assert np.allclose(A1, [[3, 0], [0, 0]])
assert np.isclose(np.linalg.norm(A - A1, 'fro'), 1)
```

## Search Exercise

For a document-by-term [[TF-IDF]] matrix, identify which factor represents term directions and how new documents can be projected using the fitted directions. Low reconstruction error does not guarantee that rare but decisive terms survive; verify [[Search Evaluation|relevance]].

## References & Useful Links

- [NumPy SVD](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html) — Primary reference for the explanation above.
- [Truncated SVD and latent semantic analysis](https://scikit-learn.org/stable/modules/decomposition.html) — Primary reference for the explanation above.
