---
tags:
  - "ds-foundations"
---

The hyperbolic tangent, $\tanh$, is a rescaled [[Sigmoid Function|sigmoid]] that maps real numbers into $(-1, 1)$. Because its output is zero-centred, it is generally preferred to the sigmoid for hidden layers, but it still saturates.

## Definition and Characteristics

$$
\tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} = 2\sigma(2x) - 1
$$

- **Output range.** $(-1, 1)$, compared with $(0, 1)$ for the sigmoid.
- **Zero-centred.** Negative inputs give negative outputs and positive inputs give positive outputs, so activations tend to have mean closer to zero. This avoids the same-sign weight-gradient problem of sigmoid units; CS231n notes that tanh is therefore preferred to sigmoid in practice.[^cs231n-nn1]
- **Odd function.** $\tanh(-x) = -\tanh(x)$ and $\tanh(0) = 0$.
- **Saturation.** For inputs of large magnitude the output approaches $\pm 1$ and the gradient approaches zero, so tanh also suffers from vanishing gradients.
- **Computation.** It needs exponentials, so it is more expensive than ReLU, which simply thresholds at zero.

## Derivative

$$
\frac{d}{dx}\tanh(x) = 1 - \tanh^2(x)
$$

The derivative is always positive, peaks at $1$ when $x = 0$, and approaches zero only as $|x| \to \infty$. Compared with the sigmoid's maximum of $0.25$, tanh passes back up to four times as much gradient near the origin. This is the precise sense in which its gradients are "stronger". Far from zero, tanh saturates faster than the sigmoid, so the advantage disappears (see the worked example).

### Derivation with the Quotient Rule

Write $\tanh(x) = g(x) / h(x)$ with $g(x) = e^{x} - e^{-x}$ and $h(x) = e^{x} + e^{-x}$. The quotient rule is:

$$
\left(\frac{g}{h}\right)' = \frac{g' h - g h'}{h^2}
$$

**Step 1: derivatives of the numerator and denominator.**

$$
g'(x) = e^{x} + e^{-x} = h(x), \qquad h'(x) = e^{x} - e^{-x} = g(x)
$$

**Step 2: substitute.**

$$
\tanh'(x) = \frac{h^2 - g^2}{h^2}
$$

**Step 3: expand the numerator.**

$$
h^2 - g^2 = (e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x}) = 4
$$

**Step 4: rewrite in terms of $\tanh$.** Splitting the fraction from Step 2 instead gives:

$$
\tanh'(x) = 1 - \frac{g^2}{h^2} = 1 - \tanh^2(x) = \frac{4}{(e^{x} + e^{-x})^2}
$$

Expressing the derivative through $\tanh(x)$ itself is convenient in backpropagation: the forward output is already stored, so the local gradient costs one multiplication and one subtraction.

## Worked Example

**Inputs.** Evaluate $\tanh$ and its derivative at $x = 0, 2, 4$, and compare with the sigmoid derivatives from [[Sigmoid Function]].

**Step 1: at $x = 0$.**

$$
\tanh(0) = 0, \qquad \tanh'(0) = 1 \quad (\text{sigmoid: } 0.25)
$$

**Step 2: at $x = 2$.**

$$
\tanh(2) \approx 0.964, \qquad \tanh'(2) \approx 0.071 \quad (\text{sigmoid: } 0.105)
$$

**Step 3: at $x = 4$.**

$$
\tanh(4) \approx 0.9993, \qquad \tanh'(4) \approx 0.0013 \quad (\text{sigmoid: } 0.018)
$$

Near zero, tanh passes back four times as much gradient as the sigmoid. By $x = 2$, it passes back less. Keeping pre-activations in the non-saturated range, through [[Initialization|initialisation]] and normalisation, matters more than the choice between the two. The values were recalculated in Python.

## Use in Neural Networks

For a hidden layer, the pre-activation and output are:

$$
z^{t} = W^{t} h^{t-1} + b^{t}, \qquad h^{t} = \tanh(z^{t})
$$

The chain rule gives:

$$
\frac{\partial \mathcal{L}}{\partial W^{t}} = \left(\frac{\partial \mathcal{L}}{\partial h^{t}} \odot \big(1 - \tanh^2(z^{t})\big)\right) \big(h^{t-1}\big)^\top
$$

In deep networks these factors multiply across layers. Saturated units contribute factors near zero, so early layers can learn very slowly; see [[Vanishing & Exploding Gradients]]. Tanh remains common where a bounded, signed output is useful, for example inside [[LSTM]] and [[RNN]] cells. For deep feed-forward hidden layers, CS231n recommends ReLU-family activations and expects tanh to work worse.[^cs231n-nn1]

## Related Notes

- [[Sigmoid Function]] — The unscaled, non-zero-centred counterpart.
- [[Initialization]] — Xavier-style scaling for tanh units (PyTorch gain $5/3$).
- [[Calculus]] — The quotient rule used in the derivation.

## References & Useful Links

[^cs231n-nn1]: [CS231n: Neural Networks Part 1 — Setting up the Architecture](https://cs231n.github.io/neural-networks-1/) — Tanh as a zero-centred scaled sigmoid, $\tanh(x) = 2\sigma(2x) - 1$, and practical activation recommendations.