# Softmax Function

#search-eng

## Definition

Softmax converts a finite vector of real scores (logits) into positive values that sum to one:

$$p_j=\frac{\exp(z_j)}{\sum_{k=1}^{K}\exp(z_k)}.$$

It is used for mutually exclusive class distributions, token distributions, and attention weights. Normalisation alone does not make probabilities calibrated. For independent multilabel outputs, separate [[Sigmoid Function|sigmoids]] are generally more appropriate.

## Numerical Stability

Subtracting a shared constant leaves softmax unchanged. Subtract the largest logit before exponentiation to avoid overflow:

```python
import numpy as np
z = np.array([1000.0, 1001.0, 1002.0])
e = np.exp(z - z.max())
p = e / e.sum()
assert np.allclose(p, [0.09003057, 0.24472847, 0.66524096])
assert np.isclose(p.sum(), 1)
```

With temperature $T>0$, use $z/T$: higher temperature makes the distribution flatter; lower temperature concentrates it. Equal maxima share mass as temperature approaches zero.

## Search Exercise

Softmax across three candidates changes when a fourth candidate is added, even if the original logits stay fixed. Explain why those normalised scores should not automatically be interpreted as candidate-independent relevance probabilities. See [[Cross Entropy Loss]], [[Transformers]], and [[Exponential Constant - e]].

## References & Useful Links

- [SciPy softmax](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.softmax.html) — Primary reference for the explanation above.
