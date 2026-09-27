---
tags:
  - "ds-foundations"
---

Adagrad and RMSProp give every parameter its own effective learning rate by dividing the gradient by a running measure of that parameter's past gradient magnitudes. Adagrad accumulates all past squared gradients; RMSProp keeps an exponentially decaying average so the step size does not shrink indefinitely.

**Notation.** For one parameter, $g_t$ is the gradient at step $t$, $\alpha$ is the base learning rate, and $\epsilon$ is a small constant that prevents division by zero. All operations are element-wise over parameters.

## Adagrad

Adagrad was introduced by Duchi, Hazan and Singer (2011).[^duchi] It accumulates squared gradients:

$$
G_t = G_{t-1} + g_t^2
$$

Each parameter then takes a step scaled by its own history:

$$
w_t = w_{t-1} - \frac{\alpha}{\sqrt{G_t} + \epsilon} \, g_t
$$

Some texts write $\sqrt{G_t + \epsilon}$ instead. PyTorch and CS231n add $\epsilon$ after the square root; the difference only matters when $G_t$ is tiny.[^pytorch-adagrad][^cs231n-nn3] PyTorch's defaults are $\alpha = 0.01$ and $\epsilon = 10^{-10}$ as of version 2.14.

### Why It Suits Sparse Features

Parameters that receive large or frequent gradients build up a large $G_t$ and take smaller steps. Parameters that receive small or infrequent gradients, such as weights for rare features, keep a small $G_t$ and relatively larger steps.[^cs231n-nn3] With sparse data, rare but informative features can therefore still learn quickly. Examples include rare words in a bag-of-words model and uncommon query terms in a ranking feature set.

### Limitation

$G_t$ never decreases, so the effective learning rate $\alpha / \sqrt{G_t}$ falls monotonically. In deep learning this is usually too aggressive and learning stops too early.[^cs231n-nn3] RMSProp addresses this.

## RMSProp

RMSProp (root mean square propagation) was never formally published. It comes from Geoffrey Hinton's Coursera lecture 6 (Tieleman and Hinton, 2012).[^cs231n-nn3] It replaces the running sum with an exponential moving average using decay rate $\rho$:

$$
G_t = \rho \, G_{t-1} + (1 - \rho) \, g_t^2
$$

The update itself is unchanged:

$$
w_t = w_{t-1} - \frac{\alpha}{\sqrt{G_t} + \epsilon} \, g_t
$$

CS231n lists typical decay rates of 0.9, 0.99 and 0.999. PyTorch 2.14 defaults to $\rho = 0.99$ (called `alpha`), learning rate $0.01$ and $\epsilon = 10^{-8}$, and it offers a *centred* variant that normalises by an estimate of the gradient's variance. PyTorch takes the square root before adding $\epsilon$; its documentation notes that TensorFlow interchanges the two operations.[^pytorch-rmsprop]

### Why RMSProp Improves on Adagrad

- **The step size can recover.** Old gradients are forgotten, so the effective learning rate does not decay towards zero.
- **Adaptation to recent scale.** Each weight is scaled by the magnitude of its recent gradients. The step size therefore adapts when the gradient scale changes over training, which helps in non-stationary settings.
- **Help at saddle points.** Where the gradient is small in some direction, the small denominator enlarges the step in that direction.[^cs231n-nn3]

## Worked Example

**Inputs.** One parameter receives the same gradient $g_t = 2$ for four steps. Use $\alpha = 0.1$, RMSProp decay $\rho = 0.9$, $G_0 = 0$, and ignore $\epsilon$. The step size is $\alpha g_t / \sqrt{G_t}$.

**Adagrad, step 1.**

$$
G_1 = 4, \qquad \text{step} = \frac{0.1 \times 2}{\sqrt{4}} = 0.1
$$

**Adagrad, step 4.**

$$
G_4 = 16, \qquad \text{step} = \frac{0.1 \times 2}{\sqrt{16}} = 0.05
$$

**RMSProp, step 1.**

$$
G_1 = 0.1 \times 4 = 0.4, \qquad \text{step} = \frac{0.2}{\sqrt{0.4}} \approx 0.316
$$

**RMSProp, step 4.**

$$
G_4 \approx 1.376, \qquad \text{step} = \frac{0.2}{\sqrt{1.376}} \approx 0.171
$$

With a constant gradient, Adagrad's step falls as $\alpha / \sqrt{t}$ and keeps falling: $0.1$, $0.071$, $0.058$, $0.05$. RMSProp's average approaches $g^2 = 4$, so its step settles towards $\alpha = 0.1$ instead of vanishing. Its early steps are inflated, however, because $G$ starts at zero and underestimates $g^2$. [[Adam Optimizer|Adam]] corrects exactly this start-up bias. The values were recalculated in Python.

## Related Notes

- [[Optimization Algorithms]] — Comparison with momentum-based methods.
- [[Adam Optimizer]] — Adds a momentum-like first moment and bias correction to RMSProp.
- [[Gradient Descent]] — The base update, and a sparse-feature interview question.

## References & Useful Links

[^duchi]: [Adaptive Subgradient Methods for Online Learning and Stochastic Optimization (Duchi, Hazan and Singer, JMLR 2011)](https://jmlr.org/papers/v12/duchi11a.html) — The original Adagrad paper; its abstract describes adaptation that finds "very predictive but rarely seen features".
[^pytorch-adagrad]: [PyTorch 2.14: torch.optim.Adagrad](https://docs.pytorch.org/docs/2.14/generated/torch.optim.Adagrad.html) — Algorithm, $\epsilon$ placement and default hyperparameters.
[^pytorch-rmsprop]: [PyTorch 2.14: torch.optim.RMSprop](https://docs.pytorch.org/docs/2.14/generated/torch.optim.RMSprop.html) — Algorithm, centred variant, defaults, and the note on $\epsilon$ placement versus TensorFlow.
[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Per-parameter adaptive methods, typical decay rates, Adagrad's aggressive decay, RMSProp's origin, and the saddle-point illustration.