---
tags:
  - "ds-foundations"
---

The rectified linear unit (ReLU) passes positive inputs through unchanged and sets negative inputs to zero. It is the default hidden-layer activation in many deep networks because it is cheap and does not saturate for positive inputs. Its variants, Leaky ReLU, PReLU and GELU, address its main weakness: units that output zero for every input stop learning.

## Definition and Derivative

$$
\mathrm{ReLU}(x) = \max(0, x)
$$

$$
\mathrm{ReLU}'(x) = \begin{cases} 1 & x > 0 \\ 0 & x < 0 \end{cases}
$$

The derivative is undefined at exactly $x = 0$. Frameworks use a fixed subgradient there, which rarely matters in practice. In [[Backpropagation]] a ReLU behaves like a gate: it passes the incoming gradient unchanged where the unit was active and blocks it where it was not.[^cs231n-bp]

## Why ReLU over Sigmoid or Tanh

This answers the interview question "Why ReLU over sigmoid?"

- **No saturation for positive inputs.** The derivative is exactly 1 for $x > 0$, whereas the [[Sigmoid Function|sigmoid]] derivative never exceeds 0.25 and [[Tanh Function|tanh]] approaches zero for large inputs. Gradients therefore shrink less as they pass back through many layers; see [[Vanishing & Exploding Gradients]].
- **Faster training in practice.** Krizhevsky et al. reported about six times faster convergence of SGD with ReLU than with tanh on their network. CS231n attributes this to ReLU's linear, non-saturating form.[^cs231n-nn1]
- **Cheap to compute.** It is a threshold at zero, with no exponentials.[^cs231n-nn1]
- **Sparse activations.** Many units output exactly zero for a given input.

ReLU does not eliminate vanishing gradients: inactive units pass back nothing, and the weights still multiply the gradient at every layer. Its outputs are also not zero-centred.

## The Dying-ReLU Problem

If a unit's pre-activation is negative for every training input, its output and gradient are zero everywhere and its weights never change again. A large gradient step can knock a unit into this state. CS231n reports that as much as 40% of a network can end up "dead" when the learning rate is too high, and that this is less common with a well-chosen learning rate.[^cs231n-nn1]

## Variants

- **Leaky ReLU** keeps a small slope $a$ for negative inputs, so gradients never vanish completely. PyTorch's default slope is $a = 0.01$ as of version 2.14.[^pytorch-leaky]

$$
\mathrm{LeakyReLU}(x) = \max(0, x) + a \min(0, x)
$$

- **PReLU** (parametric ReLU) learns the negative slope $a$ for each unit or channel. It was introduced by He et al., together with the initialisation for rectifier networks described in [[Initialization]].[^he] CS231n notes that the benefit of these leaky variants is not consistent across tasks.[^cs231n-nn1]
- **GELU** (Gaussian error linear unit) weights each input by the probability that a standard normal variable falls below it, instead of gating by sign.[^gelu] $\Phi$ is the standard normal cumulative distribution function:

$$
\mathrm{GELU}(x) = x \, \Phi(x)
$$

PyTorch also offers a tanh-based approximation.[^pytorch-gelu] GELU is smooth and allows small negative outputs. It is the activation in [[BERT]]'s feed-forward layers.

- **Maxout** takes the maximum of two or more linear functions. It generalises ReLU and Leaky ReLU without dying units, but doubles the parameters per unit.[^cs231n-nn1]

## Worked Example

**Inputs.** Evaluate ReLU, Leaky ReLU with $a = 0.01$, and GELU at $x = -2, -1, 0, 1, 2$. Then examine a unit with weights $w = (1, 1)$, bias $b = -10$, and inputs drawn uniformly from $[0, 1]^2$.

**Step 1: activation values.**

| $x$ | ReLU | Leaky ReLU | GELU |
|---|---|---|---|
| $-2$ | $0$ | $-0.02$ | $-0.045$ |
| $-1$ | $0$ | $-0.01$ | $-0.159$ |
| $0$ | $0$ | $0$ | $0$ |
| $1$ | $1$ | $1$ | $0.841$ |
| $2$ | $2$ | $2$ | $1.955$ |

**Step 2: a dead unit.** The largest possible pre-activation for inputs in $[0, 1]^2$ is:

$$
w^\top x + b \le 1 + 1 - 10 = -8
$$

**Step 3: its gradient.** Every pre-activation is negative, so:

$$
\frac{\partial\, \mathrm{ReLU}(w^\top x + b)}{\partial w} = 0 \quad \text{for every input}
$$

With a Leaky ReLU the same unit would pass back $0.01$ times the incoming gradient, enough to move it slowly out of the dead region. On 1,000 sampled inputs, the ReLU unit was active 0% of the time, with a maximum pre-activation of about $-8.02$.

GELU is close to ReLU for large positive inputs, is slightly negative just below zero, and returns to zero for very negative inputs. The values were computed in Python.

## Practical Guidance

- **Initialise for rectifiers.** Use He (Kaiming) initialisation with gain $\sqrt{2}$; see [[Initialization]].
- **Watch the learning rate.** Too high a rate is the usual cause of many dead units. Monitor the fraction of units that never activate.[^cs231n-nn1]
- **Defaults.** CS231n recommends starting with ReLU and trying Leaky ReLU or Maxout if dead units are a concern.[^cs231n-nn1] Transformer models commonly use GELU.
- **Output layers** normally use a task-specific function instead: sigmoid for independent binary outputs, [[Softmax Function|softmax]] for mutually exclusive classes, or none for regression.

## Connection to Search

[[SPLADE]] applies $\log(1 + \mathrm{ReLU}(\cdot))$ to transformer outputs to produce term weights. The ReLU sets negative weights to exactly zero. Together with the FLOPS regulariser described in [[SPLADE#Keeping it sparse|Keeping it sparse]], this makes the vectors sparse enough for [[Inverted Index|inverted-index]] retrieval.

## Related Notes

- [[Sigmoid Function]] and [[Tanh Function]] — Saturating alternatives.
- [[Backpropagation]] — How the ReLU gate routes gradients.
- [[CNN Different Architectures]] — AlexNet's switch from sigmoid and tanh to ReLU.
- [[Deep Learning]] — Where activations fit in the training loop.

## References & Useful Links

[^cs231n-nn1]: [CS231n: Neural Networks Part 1 — Setting up the Architecture](https://cs231n.github.io/neural-networks-1/) — ReLU advantages, the sixfold speed-up reported by Krizhevsky et al., dying ReLUs, Leaky ReLU, PReLU, Maxout, and practical recommendations.
[^cs231n-bp]: [CS231n: Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/) — Max-style gates route the gradient to the active input.
[^he]: [Delving Deep into Rectifiers (He et al., 2015)](https://arxiv.org/abs/1502.01852) — Abstract: introduces PReLU and an initialisation for rectifier networks.
[^gelu]: [Gaussian Error Linear Units (Hendrycks and Gimpel, 2016)](https://arxiv.org/abs/1606.08415) — Abstract: GELU is $x\Phi(x)$ and weights inputs by value rather than gating by sign.
[^pytorch-leaky]: [PyTorch 2.14: torch.nn.LeakyReLU](https://docs.pytorch.org/docs/2.14/generated/torch.nn.LeakyReLU.html) — Definition and default negative slope.
[^pytorch-gelu]: [PyTorch 2.14: torch.nn.GELU](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GELU.html) — Exact and tanh-approximate forms.
