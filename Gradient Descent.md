---
tags:
  - "ds-foundations"
---

Gradient descent minimises a differentiable objective by repeatedly moving the parameters a small step against the gradient. It trains most neural networks and many classical models, such as [[Linear Regression]] and [[Logistic Regression]]. [[Optimization Algorithms]] compares the variants built on top of it.

## Update Rule

**Notation.** Parameters $w$, training pairs $(x_i, y_i)$ for $i = 1, \dots, N$, per-example loss $\ell$, model $f(x; w)$, and learning rate $\eta > 0$. The training objective is the average loss:

$$
L(w) = \frac{1}{N} \sum_{i=1}^{N} \ell\big(f(x_i; w), y_i\big)
$$

Each iteration applies:

$$
w_{t+1} = w_t - \eta \, \nabla_w L(w_t)
$$

The gradient points in the direction of steepest local increase, so its negative is the direction of steepest local decrease. The step is only trustworthy locally: a small change in $w$ gives a small, roughly linear change in $L$.

The ingredients are:

1. **Model**, for example $f(x; W) = Wx$ for a linear model.
2. **Loss**, for example the squared error:

   $$
   \ell_i = (y_i - W x_i)^2
   $$

3. **Partial derivatives** $\partial L / \partial w_j$ for every parameter.
4. **Update** each weight:

   $$
   w_j \leftarrow w_j - \eta \frac{\partial L}{\partial w_j}
   $$

5. **Learning rate** $\eta$. Too small and progress is slow; too large and the iterates oscillate or diverge (see the worked example).

## Batch, Stochastic and Mini-Batch Variants

The variants differ only in how many examples are used to estimate the gradient for one update.

| Variant | Examples per update | Gradient | Typical trade-off |
|---|---|---|---|
| Full batch | All $N$ | Exact for the training objective | Smooth but one expensive step per pass |
| Stochastic (SGD) | 1 | Noisy estimate | Cheap, noisy steps |
| Mini-batch | $B$, often tens to thousands | Less noisy estimate | Matches vectorised hardware well |

For a mini-batch $\mathcal{B}_t$ of size $B$, the gradient estimate is:

$$
g_t = \frac{1}{B} \sum_{i \in \mathcal{B}_t} \nabla_w \, \ell\big(f(x_i; w_t), y_i\big)
$$

SGD is the case $B = 1$ and full batch is $B = N$. In practice "SGD" in libraries usually means mini-batch SGD. One pass over the training data is an [[Epochs|epoch]].

Two properties matter for the interview questions below:

- **Unbiasedness.** If the mini-batch is drawn uniformly at random, the expected mini-batch gradient equals the full-batch gradient. Noise comes from variance, not bias.
- **Variance.** With independent sampling, the variance of $g_t$ falls roughly as $1/B$. Quadrupling the batch size therefore only halves the standard deviation of the gradient noise.

The noise is visible in training curves: with batch size 1 the loss "wiggles" a lot, and with the full dataset each step should reduce the loss unless the learning rate is too high.[^cs231n-nn3]

## Computing the Gradients

There are four ways to obtain the partial derivatives:[^baydin]

1. **Manual differentiation.** Derive and code the derivatives by hand. Exact but slow and error-prone for large models.
2. **Numerical differentiation.** Finite differences such as the forward difference:

   $$
   \frac{f(x + h) - f(x)}{h}
   $$

   Simple, but it needs $O(n)$ function evaluations for $n$ parameters and suffers from truncation and round-off error. It remains useful for *gradient checking*, where the centred difference is preferred:[^cs231n-nn3]

   $$
   \frac{f(x + h) - f(x - h)}{2h}
   $$

3. **Symbolic differentiation.** A computer algebra system manipulates expressions. Exact, but expressions can grow very large ("expression swell") and control flow is hard to handle.
4. **Automatic differentiation (AD).** Applies the chain rule to each elementary operation while the program runs. It gives derivatives accurate to machine precision with a small constant-factor overhead. Backpropagation is reverse-mode AD applied to a scalar loss; see [[Computational Graph]] and [[Jacobians]].

## Analytical Gradients

### Linear Model with Squared Error

For $f(x_i; w) = w^\top x_i$ and the summed squared error:

$$
L = \sum_{i=1}^{N} \big(y_i - w^\top x_i\big)^2
$$

The chain rule gives:

$$
\frac{\partial L}{\partial w_j} = -2 \sum_{i=1}^{N} \big(y_i - w^\top x_i\big) x_{ij}
$$

Each example pushes $w_j$ in proportion to its residual and its feature value.

### Sigmoid Output with Squared Error

Now pass the linear score through the [[Sigmoid Function|sigmoid]]:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Its derivative is:

$$
\sigma'(z) = \sigma(z)\big(1 - \sigma(z)\big)
$$

Write $\sigma_i = \sigma(w^\top x_i)$ and $\delta_i = y_i - \sigma_i$. The loss is:

$$
L = \sum_{i=1}^{N} \big(y_i - \sigma_i\big)^2
$$

Differentiating the square, then the sigmoid, then the linear score:

$$
\frac{\partial L}{\partial w_j} = -2 \sum_{i=1}^{N} \delta_i \, \sigma_i (1 - \sigma_i) \, x_{ij}
$$

Substituting into the update rule above turns the two minus signs into a plus:

$$
w_j \leftarrow w_j + 2\eta \sum_{i=1}^{N} \delta_i \, \sigma_i (1 - \sigma_i) \, x_{ij}
$$

The factor $\sigma_i(1 - \sigma_i)$ is at most $0.25$ and approaches zero when the sigmoid saturates, so a confidently wrong prediction produces almost no update. With the [[Cross Entropy Loss|cross-entropy (log) loss]] instead of squared error, that factor cancels and the gradient becomes:

$$
\frac{\partial L}{\partial w_j} = \sum_i (\sigma_i - y_i) x_{ij}
$$

This is one reason [[Logistic Regression]] is trained with log loss.

## Worked Example

**Inputs.** One feature, no intercept: $x = (1, 2)$, $y = (2, 4)$, model $\hat{y} = wx$, summed squared error, $w_0 = 0$, $\eta = 0.05$. The optimum is $w^* = 2$.

**Step 1: gradient at $w_0 = 0$.**

$$
\frac{\partial L}{\partial w} = -2\big[(2 - 0)(1) + (4 - 0)(2)\big] = -20
$$

**Step 2: first update.**

$$
w_1 = 0 - 0.05 \times (-20) = 1
$$

**Step 3: gradient at $w_1 = 1$.**

$$
\frac{\partial L}{\partial w} = -2\big[(2 - 1)(1) + (4 - 2)(2)\big] = -10
$$

**Step 4: second update.**

$$
w_2 = 1 - 0.05 \times (-10) = 1.5
$$

The distance to the optimum halves each step: $2 \to 1 \to 0.5$. The curvature of this loss is:

$$
L'' = 2\sum_i x_i^2 = 10
$$

Gradient descent on a quadratic is stable only when:

$$
\eta < \frac{2}{L''} = 0.2
$$

With $\eta = 0.1$ the first step lands exactly on $w^* = 2$; with $\eta = 0.2$ the iterates bounce between $0$ and $4$ forever; above $0.2$ they diverge. Poorly scaled features create very different curvatures in different directions, which is why [[Feature Scaling]] often speeds up training.

## Interview Questions: Variants and Performance

Questions preserved from the original note, with reasoning-based answers. The empirical question is still open.

- **Explain the differences between batch, stochastic and mini-batch gradient descent.** They differ in the number of examples per update; see the table above. Batch gives exact but expensive steps, SGD cheap but noisy steps, and mini-batch trades between them while using vectorised hardware efficiently.
- **With high-dimensional sparse features, which method is best for convergence speed and stability?** Per-example or small mini-batch updates are cheap when each example has few non-zero features, because only those coordinates receive a gradient. Rare features receive few updates, so per-coordinate adaptive methods such as [[Adagrad and RMSProp|Adagrad]] are often used to give them larger effective step sizes. This is a heuristic; the best choice still depends on the data and must be validated.
- **Under RAM and GPU memory constraints, how does batch size affect training efficiency?** Activation memory grows roughly linearly with batch size, and activations usually dominate memory, so reducing the batch size is the common way to make a model fit.[^cs231n-cnn] Larger batches use parallel hardware better up to a point and reduce gradient noise, but they may need a retuned learning rate.
- **Empirically, does mini-batch gradient descent mitigate noise better than SGD?** Yes, as measured by gradient noise, but with diminishing returns per update; see the [[#Empirical Check on a Real Dataset|empirical check]] below. Averaging $B$ independent per-example gradients reduces the gradient variance by about $1/B$.
- **If mini-batching biases convergence, how would you mitigate it?** A uniformly sampled mini-batch gradient is unbiased, so apparent bias usually comes from non-random batches: sorted or time-ordered data, skewed shards, or unintended sampling weights. Shuffle every epoch, use stratified or explicitly weighted sampling, and decay the learning rate so remaining noise averages out.

### Empirical Check on a Real Dataset

**Setup.** The Wisconsin breast-cancer dataset bundled with scikit-learn: 569 examples and 30 standardised features, plus an intercept.[^sk-bc] The model is logistic regression trained on mean log loss with plain mini-batch SGD at learning rate $0.1$, starting from $w = 0$. Batches are drawn without replacement and data is reshuffled every epoch. Everything below is **training** loss with one random seed; it says nothing about generalisation. scikit-learn itself calls the dataset "very easy", so the loss keeps falling for a long time and larger, harder datasets may behave differently.

**Measurement 1: gradient noise.** At $w = 0$, sample 5,000 mini-batches and measure the mean squared distance between the mini-batch gradient and the full gradient. The prediction scales the $B = 1$ value by the variance factor for sampling without replacement:

$$
\frac{1}{B} \cdot \frac{N - B}{N - 1}
$$

| Batch size $B$ | Measured | Predicted |
|---|---|---|
| 1 | 5.548 | — |
| 8 | 0.716 | 0.685 |
| 32 | 0.169 | 0.164 |
| 128 | 0.035 | 0.034 |

**Measurement 2: training loss.** The same learning rate is used throughout, compared first at an equal number of epochs and then at an equal number of updates.

| Batch size $B$ | Loss after 20 epochs | Updates in 20 epochs | Loss after 100 updates |
|---|---|---|---|
| 1 | 0.046 | 11,380 | 0.112 |
| 8 | 0.057 | 1,440 | 0.102 |
| 32 | 0.074 | 360 | 0.103 |
| 128 | 0.103 | 100 | 0.103 |
| 569 (full) | 0.184 | 20 | 0.103 |

**Interpretation.**

- **Noise falls as $1/B$.** The measured gradient noise tracks the prediction to within about 5%. In that sense, mini-batches mitigate noise better than single-example SGD.
- **Per update, the benefit saturates quickly.** At 100 updates, $B = 1$ is clearly worse (0.112), but every batch size from 8 to the full dataset reaches about 0.102–0.103. Beyond a small batch, extra examples buy almost nothing per step while costing proportionally more computation.
- **Per epoch, small batches win.** With a fixed pass over the data, $B = 1$ takes 11,380 noisy steps and reaches the lowest training loss. Full-batch descent takes only 20 steps.
- **The comparison depends on the learning rate.** Larger batches can often take larger steps safely, so a fair comparison would tune $\eta$ separately for each $B$. That was not done here.

```python
# Requires numpy and scikit-learn; loads a dataset bundled with scikit-learn.
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
X = StandardScaler().fit_transform(X)
X = np.hstack([X, np.ones((len(X), 1))])  # intercept column
N, d = X.shape

def grad(w, idx):
    p = 1 / (1 + np.exp(-X[idx] @ w))
    return X[idx].T @ (p - y[idx]) / len(idx)

def loss(w):
    z = X @ w
    return np.mean(np.logaddexp(0, z) - y * z)

rng = np.random.default_rng(0)
w0 = np.zeros(d)
g_full = grad(w0, np.arange(N))
base = None
for B in [1, 8, 32, 128]:
    mse = np.mean([np.sum((grad(w0, rng.choice(N, B, replace=False)) - g_full) ** 2)
                   for _ in range(5000)])
    base = base or mse
    predicted = base / B * (N - B) / (N - 1)  # sampling without replacement
    print(f"noise B={B:3d}: measured {mse:.4f}, predicted {predicted:.4f}")

def train(B, lr=0.1, epochs=None, updates=None, seed=1):
    r = np.random.default_rng(seed)
    w = np.zeros(d); n = 0
    while True:
        perm = r.permutation(N)
        for s in range(0, N, B):
            w -= lr * grad(w, perm[s:s + B]); n += 1
            if updates and n == updates:
                return loss(w)
        if epochs and n == epochs * -(-N // B):
            return loss(w)

for B in [1, 8, 32, 128, N]:
    print(f"B={B:3d}: loss after 20 epochs {train(B, epochs=20):.4f}, "
          f"after 100 updates {train(B, updates=100):.4f}")
```

The script was executed with scikit-learn 1.9.1 and NumPy 2.4.6 and produced the numbers in both tables.

## Limitations and Pitfalls

- **Local minima and saddle points.** Neural-network losses are non-convex; gradient descent finds a stationary point, not necessarily the global minimum. See [[Optimization Algorithms]].
- **Learning-rate sensitivity.** Schedules that decay $\eta$ over time are common in deep learning.[^cs231n-nn3]
- **Vanishing and exploding gradients.** In deep networks, repeated multiplication by small or large derivatives can shrink or blow up the gradient; see [[Vanishing & Exploding Gradients]] and [[Gradient Clipping]].
- **Wrong gradients.** A buggy analytic gradient can still reduce the loss slowly. Check it against centred finite differences on a few parameters.

## Related Notes

- [[Momentum]], [[Nesterov Momentum]], [[Adagrad and RMSProp]], [[Adam Optimizer]] — Optimisers that modify the basic update.
- [[L1 and L2 Regularization]] — Penalties that add terms to the gradient.
- [[Loss Function & Cost Function]] — The objective being minimised.
- [[Calculus]] — Derivative rules used in the analytical gradients.

## References & Useful Links

[^baydin]: [Automatic Differentiation in Machine Learning: a Survey (Baydin et al., JMLR 2018)](https://arxiv.org/abs/1502.05767) — The four ways to compute derivatives, their accuracy and cost, and backpropagation as reverse-mode AD.
[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Gradient checking with centred differences, loss "wiggle" versus batch size, and learning-rate annealing.
[^cs231n-cnn]: [CS231n: Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/) — Memory is usually dominated by activations; decreasing the batch size is the common way to fit a model.
[^sk-bc]: [scikit-learn: load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) — The bundled copy of the UCI Breast Cancer Wisconsin (Diagnostic) dataset: 569 samples, 30 features, two classes.
