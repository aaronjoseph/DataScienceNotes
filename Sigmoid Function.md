---
tags:
  - "ds-foundations"
---

The sigmoid (logistic) function $\sigma(x)$ squashes any real number into the interval $(0, 1)$, so its output can be read as a probability. It is the standard output for binary classification and was historically a common hidden-layer activation. In deep hidden layers it has largely been replaced because it saturates.

## Definition and Properties

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

- **Output range.** $\sigma(x) \in (0, 1)$; the endpoints are approached but never reached.
- **Shape.** An S-shaped curve with $\sigma(0) = 0.5$ and the symmetry $\sigma(-x) = 1 - \sigma(x)$.
- **Always positive.** Outputs are never negative, so they are not zero-centred.
- **Saturation.** As $x \to \infty$, $\sigma(x) \to 1$; as $x \to -\infty$, $\sigma(x) \to 0$.
- **Monotonic.** The derivative is always positive, so the function is strictly increasing.
- **Relation to tanh.** $\tanh(x) = 2\sigma(2x) - 1$, so tanh is a rescaled, zero-centred sigmoid; see [[Tanh Function]].[^cs231n-nn1]

## Derivative

$$
\sigma'(x) = \sigma(x)\big(1 - \sigma(x)\big)
$$

The derivative is largest at $x = 0$, where it equals $0.5 \times 0.5 = 0.25$, and it approaches zero in both tails. It is cheap to compute from the forward output, which backpropagation already stores.

## Worked Example

**Inputs.** Evaluate $\sigma$ and $\sigma'$ at $x = 0, 2, 4$, then consider a chain of five sigmoid layers.

**Step 1: at $x = 0$.**

$$
\sigma(0) = 0.5, \qquad \sigma'(0) = 0.25
$$

**Step 2: at $x = 2$.**

$$
\sigma(2) \approx 0.881, \qquad \sigma'(2) \approx 0.105
$$

**Step 3: at $x = 4$.**

$$
\sigma(4) \approx 0.982, \qquad \sigma'(4) \approx 0.018
$$

**Step 4: five layers.** Backpropagation multiplies one sigmoid derivative per layer, so even in the best case, with every unit at $x = 0$ and weights ignored:

$$
0.25^5 \approx 0.00098
$$

A unit at $x = 4$ passes back less than 2% of the gradient it receives. Across five layers, the activation derivatives alone scale the gradient by less than 0.1%. Weights can partly offset this, but it explains why early layers of deep sigmoid networks learn slowly. The values were recalculated in Python.

## Vanishing Gradients

For a layer with weights $W^{t}$, bias $b^{t}$ and input $h^{t-1}$, the pre-activation is $z^{t} = W^{t} h^{t-1} + b^{t}$ and the output is $h^{t} = \sigma(z^{t})$. By the chain rule:

$$
\frac{\partial \mathcal{L}}{\partial W^{t}} = \left(\frac{\partial \mathcal{L}}{\partial h^{t}} \odot \sigma'(z^{t})\right) \big(h^{t-1}\big)^\top
$$

Here $\odot$ is element-wise multiplication. The factor $\sigma'(z^{t}) \le 0.25$ appears at every layer the gradient passes through. When units saturate it is close to zero, so almost no signal reaches their weights or the layers below.[^cs231n-nn1] Training can then plateau. Glorot and Bengio also found that the sigmoid's non-zero mean can drive the top hidden layer into saturation under random initialisation.[^glorot] See [[Vanishing & Exploding Gradients]] and [[Initialization]].

## Other Drawbacks in Hidden Layers

- **Not zero-centred.** If a unit's inputs are all positive, the gradients on its weights all share one sign for a given example, which can cause zig-zagging updates. Summing over a mini-batch softens this.[^cs231n-nn1]
- **Cost.** The exponential is more expensive than the simple threshold of ReLU, although this is rarely the bottleneck.[^cs231n-nn1]

## Where Sigmoid Is Still the Right Choice

- **Binary outputs.** In [[Logistic Regression]], $\sigma(w^\top x + b)$ models $P(y = 1 \mid x)$.
- **Independent multilabel outputs.** Use one sigmoid per label; [[Softmax Function|softmax]] is for mutually exclusive classes.
- **Gates.** Recurrent units such as [[LSTM]] use sigmoids to produce gate values between 0 and 1.
- **Pairwise ranking.** The pairwise logistic loss in [[Learning to Rank#A Pairwise Loss Makes the Preference Concrete|learning to rank]] is $-\log \sigma(s_i - s_j)$, which treats a score difference as a preference probability.

**Numerical stability.** Compute the loss from the raw score (logit) rather than applying a sigmoid and then a log. For example, PyTorch's `BCEWithLogitsLoss` combines the two and is more numerically stable than a separate sigmoid followed by `BCELoss`.[^pytorch-bce] A sigmoid output is a probability only if the model is calibrated; see [[Probability Calibration]].

## Related Notes

- [[Cross Entropy Loss]] — The usual loss paired with a sigmoid output.
- [[Gradient Descent]] — Gradient derivation for a sigmoid output with squared error.
- [[Tanh Function]] — The zero-centred alternative.
- [[ReLU Function]] — The usual hidden-layer replacement, which does not saturate for positive inputs.

## References & Useful Links

[^cs231n-nn1]: [CS231n: Neural Networks Part 1 — Setting up the Architecture](https://cs231n.github.io/neural-networks-1/) — Sigmoid saturation, non-zero-centred outputs, cost relative to ReLU, and $\tanh(x) = 2\sigma(2x) - 1$.
[^glorot]: [Understanding the Difficulty of Training Deep Feedforward Neural Networks (Glorot and Bengio, AISTATS 2010)](https://proceedings.mlr.press/v9/glorot10a.html) — Abstract: the logistic sigmoid's mean value can drive the top hidden layer into saturation.
[^pytorch-bce]: [PyTorch 2.14: torch.nn.BCEWithLogitsLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BCEWithLogitsLoss.html) — Combines sigmoid and binary cross-entropy for numerical stability, with optional positive-class weights.
