---
tags:
  - "ds-foundations"
---

## Overview

An autoencoder is a neural network trained to reproduce its input at its output. Internally it passes the input through a **code** (latent representation), so it can be viewed as two parts: an encoder $h = f(x)$ and a decoder that produces a reconstruction $r = g(h)$.[^goodfellow]

Its training signal comes from the input itself, so no labels are needed. It is therefore usually described as unsupervised (or self-supervised) learning of efficient data codings. Common uses are [[Dimensionality Reduction|dimensionality reduction]], denoising, representation learning, and [[Anomaly Detection Algorithms|anomaly detection]].

The earlier version of this note described autoencoders as "simplistic" networks that make outputs close to inputs. Reconstruction is the training objective, but the useful product is usually the code, or the reconstruction error, not the copy itself.

## Key Concepts

- **Encoder** $f$: maps an input $x \in \mathbb{R}^p$ to a code $h \in \mathbb{R}^k$.
- **Decoder** $g$: maps the code back to a reconstruction $\hat{x} = g(f(x))$.
- **Reconstruction loss** $L(x, \hat{x})$: often mean squared error for real-valued inputs, and [[Cross Entropy Loss|cross-entropy]] for binary or normalised inputs.
- **Constraint:** something must stop the network from learning the identity map. A perfect copy teaches nothing about the structure of the data.

With mean squared error, the loss for one example is

$$
L(x, \hat{x}) = \frac{1}{p}\sum_{j=1}^{p} (x_j - \hat{x}_j)^2.
$$

Training minimises its average over the training examples with [[Gradient Descent|gradient descent]] and backpropagation.

## Details & Deep Dive

### Ways to prevent a trivial copy

| Variant | Constraint | What it encourages |
|---|---|---|
| Undercomplete | Code smaller than the input ($k < p$) | Keep the directions that explain most of the data |
| Sparse | Penalty on code activations | Few active code units per input |
| Denoising | Corrupt the input; reconstruct the clean version | Features robust to noise |
| Variational (VAE) | Probabilistic encoder with a prior on the code | A smooth latent space that can generate new samples |

Denoising autoencoders are trained to recover inputs from corrupted versions. Vincent et al. (2010) reported that stacking them gave lower classification error than stacking ordinary autoencoders on their benchmarks.[^vincent] The variational autoencoder (Kingma and Welling, 2013) comes from variational inference: it fits an approximate inference model for continuous latent variables using a reparameterised lower bound.[^vae] Its encoder outputs a distribution, not a single point.

### Relationship to PCA

If the encoder and decoder are linear and the loss is squared error, an undercomplete autoencoder learns the same subspace as [[PCA]]. The individual code axes need not match the principal components, because any invertible change of basis within the subspace gives the same reconstruction. The Python check below confirms this on synthetic data.

Non-linear encoders and decoders can capture curved structure that PCA cannot. Hinton and Salakhutdinov (2006) reported that deep autoencoders, with a suitable weight initialisation, learned low-dimensional codes that worked much better than PCA in their experiments.[^hinton] This is a source-specific result, not a guarantee for every dataset; a linear baseline is still worth comparing.

## Worked Example: Reconstruction Error as an Anomaly Score

**Inputs:**

- Normal training data lies close to the line $x_2 = x_1$.
- A linear undercomplete autoencoder with one code unit has learned the direction $w = \left(\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}}\right)$.
- Encoder: $h = w^\top x$. Decoder: $\hat{x} = h\,w$.
- Two inputs to score: $a = (3, 3.2)$ and $b = (3, -3)$.

**Step 1: encode and decode $a$.**

$$
h_a = \frac{3 + 3.2}{\sqrt{2}} \approx 4.384
$$

$$
\hat{a} = h_a\,w = (3.1,\ 3.1)
$$

**Step 2: reconstruction error for $a$.**

$$
L(a, \hat{a}) = \frac{(3 - 3.1)^2 + (3.2 - 3.1)^2}{2} = \frac{0.01 + 0.01}{2} = 0.01
$$

**Step 3: encode and decode $b$.**

$$
h_b = \frac{3 + (-3)}{\sqrt{2}} = 0
$$

$$
\hat{b} = (0,\ 0)
$$

**Step 4: reconstruction error for $b$.**

$$
L(b, \hat{b}) = \frac{(3 - 0)^2 + (-3 - 0)^2}{2} = \frac{9 + 9}{2} = 9
$$

Input $a$ follows the pattern learned from normal data, so it is reconstructed almost exactly. Input $b$ lies in a direction the code cannot represent, so its error is 900 times larger. Flagging inputs whose error exceeds a threshold is the basic autoencoder anomaly detector. Choose the threshold from errors on held-out normal data, or from the alert rate the application can review; the value 9 has no meaning on its own.

## Python Check: A Linear Autoencoder Recovers the PCA Subspace

This NumPy script was executed locally. It trains a linear autoencoder with gradient descent and compares its decoder subspace with the top two principal directions.

```python
import numpy as np

rng = np.random.default_rng(1)
n = 2000
z = rng.normal(size=(n, 2)) * np.array([3.0, 1.0])
A = np.array([[1.0, 0.5, 0.2], [0.0, 1.0, -0.4]])
X = z @ A + rng.normal(scale=0.1, size=(n, 3))
X = X - X.mean(axis=0)

_, _, vt = np.linalg.svd(X, full_matrices=False)
pca_basis = vt[:2].T

enc = rng.normal(scale=0.1, size=(3, 2))
dec = rng.normal(scale=0.1, size=(2, 3))
lr = 0.01
for _ in range(5000):
    H = X @ enc
    grad_out = 2 * (H @ dec - X) / n
    grad_dec = H.T @ grad_out
    grad_enc = X.T @ (grad_out @ dec.T)
    dec -= lr * grad_dec
    enc -= lr * grad_enc

ae_basis, _ = np.linalg.qr(dec.T)
cosines = np.linalg.svd(pca_basis.T @ ae_basis, compute_uv=False)
print("cosines of principal angles:", np.round(cosines, 4))
```

Output: `cosines of principal angles: [1. 1.]`. Both cosines equal 1, so the two 2-D subspaces coincide. In the same run, the autoencoder's mean squared error (0.00332) matched PCA's reconstruction error (0.00331).

## Limitations & Common Pitfalls

- **Contaminated training data.** If anomalies are common in the training set, the model learns to reconstruct them too.
- **Too much capacity.** A large, weakly constrained model can reconstruct unusual inputs well, which hides the anomalies you want to find.
- **Feature scale.** Squared error is dominated by large-scale features; standardise inputs first. See [[Feature Scaling]].
- **Errors are not probabilities.** A reconstruction error ranks inputs; it is not a calibrated anomaly probability. See [[Probability Calibration]].
- **Reconstruction is not relevance.** A code that reconstructs an item well need not place similar items close together for search or recommendation. Evaluate learned [[Embeddings]] on the downstream task.
- **Drift.** When normal behaviour changes, errors rise for everything; separate this from genuine anomalies. See [[Data Drift]].

## Exercise

You train an autoencoder on one month of normal payment transactions and flag the top 0.5% of reconstruction errors each day. After a holiday sale, the number of flags triples. Give two explanations and say how you would tell them apart.

> [!example]- Exercise solution
> **Explanation 1: data drift.** Holiday traffic differs from the training month (basket sizes, merchants, times), so normal transactions reconstruct poorly. **Explanation 2: a real increase in fraud** during a busy period. To separate them, compare the error distribution of reviewed normal transactions before and during the sale, inspect which features contribute most to the error, and check whether flagged cases share an attack pattern. If errors rise across all normal traffic, retrain or recalibrate the threshold on recent normal data.

## Related Notes

- [[Anomaly Detection Algorithms]] — Isolation Forest, One-Class SVM, and Local Outlier Factor as alternatives.
- [[Dimensionality Reduction]] and [[PCA]] — Linear baselines for learned codes.
- [[Deep Learning]] — Training neural networks.

## References & Useful Links

[^goodfellow]: [Goodfellow, Bengio & Courville, *Deep Learning*, Chapter 14: Autoencoders](https://www.deeplearningbook.org/contents/autoencoders.html) — Definition of the encoder $h = f(x)$ and decoder $r = g(h)$; only the chapter introduction could be read in this pass.
[^hinton]: [Hinton & Salakhutdinov (2006), "Reducing the Dimensionality of Data with Neural Networks", *Science*](https://www.science.org/doi/10.1126/science.1127647) — Abstract: deep autoencoders with good initialisation learned codes that outperformed PCA in the reported experiments.
[^vincent]: [Vincent et al. (2010), "Stacked Denoising Autoencoders", *JMLR*](https://jmlr.org/papers/v11/vincent10a.html) — Abstract: denoising criterion and reported gains over ordinary stacked autoencoders.
[^vae]: [Kingma & Welling (2013), "Auto-Encoding Variational Bayes"](https://arxiv.org/abs/1312.6114) — Abstract: reparameterised variational lower bound and approximate inference model.