---
tags:
  - "ds-foundations"
---

Nesterov momentum, also called Nesterov accelerated gradient (NAG), modifies [[Momentum|classical momentum]] in one way: it evaluates the gradient at the point the velocity is about to carry the parameters to, instead of at the current point.

## Key Idea: the Look-Ahead Gradient

The momentum term alone is about to move the weights by $\beta v_{t-1}$. That position is a better guess of where the parameters will be than the current, "stale" position, so the gradient is computed there.[^cs231n-nn3]

**Notation.** Weights $w$, velocity $v$ with $v_0 = 0$, learning rate $\alpha$, momentum $\beta$. This note uses the convention in which the learning rate sits inside the velocity (convention B in [[Momentum]]).

**Step 1: look ahead.**

$$
\tilde{w}_{t-1} = w_{t-1} + \beta v_{t-1}
$$

**Step 2: update the velocity with the look-ahead gradient.**

$$
v_t = \beta v_{t-1} - \alpha \, \nabla \mathcal{L}(\tilde{w}_{t-1})
$$

**Step 3: move the weights.**

$$
w_t = w_{t-1} + v_t
$$

Classical momentum is the same except that the gradient is taken at $w_{t-1}$. A common error, which an earlier version of this note made, is to mix conventions: looking ahead by $+\beta v$ while the velocity accumulates $+\alpha \nabla \mathcal{L}$ and the weights move by $-\alpha v$. That applies the learning rate twice and places the look-ahead uphill instead of in the direction of travel. Keep the look-ahead and the weight update in one convention.

### Implementation Form

Libraries usually store the look-ahead parameters themselves, so the update resembles plain momentum. After a change of variables, CS231n writes it as follows (pseudocode, where `dx` is the gradient at the stored parameters):[^cs231n-nn3]

```python
v_prev = v
v = mu * v - learning_rate * dx
x += -mu * v_prev + (1 + mu) * v
```

PyTorch's `SGD(..., momentum=mu, nesterov=True)` implements a related variant in its own momentum convention, which "subtly differs" from Sutskever et al.[^pytorch-sgd]

## Worked Example

**Inputs.** $\mathcal{L}(w) = w^2$, so $\nabla \mathcal{L}(w) = 2w$. Start at $w_0 = 1$, $v_0 = 0$, with $\alpha = 0.1$ and $\beta = 0.9$. These are the same settings as the [[Momentum]] worked example.

**Step 1.** The look-ahead equals the current point because $v_0 = 0$:

$$
\tilde{w}_0 = 1, \qquad v_1 = -0.1 \times 2 = -0.2, \qquad w_1 = 0.8
$$

**Step 2.**

$$
\tilde{w}_1 = 0.8 + 0.9 \times (-0.2) = 0.62, \qquad v_2 = -0.18 - 0.1 \times 1.24 = -0.304, \qquad w_2 = 0.496
$$

**Step 3.**

$$
\tilde{w}_2 = 0.496 + 0.9 \times (-0.304) = 0.2224, \qquad v_3 = -0.2736 - 0.1 \times 0.4448 = -0.3181, \qquad w_3 = 0.1779
$$

After three steps classical momentum is closer to zero ($0.062$), but it keeps going and overshoots to about $-0.709$ by step 6. Nesterov momentum overshoots only to about $-0.333$. The look-ahead gradient "sees" the far side of the minimum earlier and brakes sooner. This comparison is for one quadratic with one setting; it illustrates the mechanism rather than proving general superiority. The values were recalculated in Python.

## Why It Helps

- **Correction.** If the velocity is carrying the weights too far, the look-ahead gradient already points back and reduces the next step.
- **Less overshoot.** Nesterov momentum can tolerate a given momentum and learning rate with less oscillation than classical momentum, as in the example.
- **Theory and practice.** CS231n notes that it has stronger convergence guarantees for convex functions and that in practice it consistently works slightly better than standard momentum.[^cs231n-nn3]

## Implementation Considerations

- **Evaluate the gradient at the right point.** Computing it at $w_{t-1}$ instead of $\tilde{w}_{t-1}$ silently turns the method back into classical momentum.
- **Tune $\beta$ as for momentum.** A common value is about $0.9$.
- **Check the framework convention** before comparing hyperparameters across libraries.

## Related Notes

- [[Optimization Algorithms]] — Where Nesterov momentum fits among optimisers.
- [[Adam Optimizer]] — Nadam combines Adam with Nesterov momentum.

## References & Useful Links

[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Look-ahead intuition, update equations, implementation form, and practical comparison with standard momentum.
[^pytorch-sgd]: [PyTorch 2.14: torch.optim.SGD](https://docs.pytorch.org/docs/2.14/generated/torch.optim.SGD.html) — PyTorch's momentum and Nesterov formulation and how it differs from Sutskever et al.

- [On the Importance of Initialization and Momentum in Deep Learning (Sutskever et al., ICML 2013)](https://proceedings.mlr.press/v28/sutskever13.html) — Source of the momentum and Nesterov formulation used in deep learning. Only the abstract was read for this revision.