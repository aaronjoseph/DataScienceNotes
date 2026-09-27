---
tags:
  - "ds-foundations"
---

Momentum accelerates [[Gradient Descent|gradient descent]] by accumulating past gradients into a velocity. Directions where the gradient is consistent build up speed, while directions where it keeps changing sign partly cancel.

## Intuition

Picture a ball rolling on the loss surface. With inertia it keeps moving across flat stretches and small bumps instead of stopping wherever the local slope is tiny. The analogy has limits: the momentum coefficient behaves more like friction, because it damps the velocity so the ball can eventually settle.[^cs231n-nn3] Momentum may carry the parameters past shallow local minima, but nothing guarantees that.

## Update Rule

**Notation.** $w_t$ are the weights after step $t$, $g_t = \nabla_w \mathcal{L}(w_{t-1})$ is the gradient, $\alpha$ is the learning rate, and $\beta \in [0, 1)$ is the momentum coefficient.

Two equivalent conventions appear in the literature and in code.

**Convention A (PyTorch).** The velocity accumulates raw gradients:

$$
v_t = \beta v_{t-1} + g_t
$$

$$
w_t = w_{t-1} - \alpha v_t
$$

**Convention B (Sutskever et al. and CS231n).** The learning rate sits inside the velocity:

$$
v_t = \beta v_{t-1} - \alpha g_t
$$

$$
w_t = w_{t-1} + v_t
$$

With a constant learning rate the two give identical weights, because the convention B velocity equals $-\alpha$ times the convention A velocity. They differ slightly when a schedule changes $\alpha$ during training. PyTorch also initialises its buffer to the first gradient rather than to zero.[^pytorch-sgd]

Setting $\beta = 0$ recovers plain gradient descent, where each update depends only on the current gradient.

## Velocity as an Exponentially Weighted Sum

Expanding convention A once shows the influence of earlier gradients:

$$
v_t = \beta (\beta v_{t-2} + g_{t-1}) + g_t = \beta^2 v_{t-2} + \beta g_{t-1} + g_t
$$

Continuing back to $v_0 = 0$:

$$
v_t = \sum_{k=0}^{t-1} \beta^k \, g_{t-k}
$$

Older gradients are down-weighted geometrically, so higher $\beta$ gives past gradients more weight. Because there is no $(1 - \beta)$ factor, this is a weighted *sum*, not an average. If the gradient stays at $g$, the velocity and the effective step approach:

$$
v \to \frac{g}{1 - \beta}, \qquad \text{step} \to \frac{\alpha}{1 - \beta}
$$

That is ten times the learning rate for $\beta = 0.9$. [[Adam Optimizer|Adam]]'s first moment includes the $(1 - \beta)$ factor and is a true moving average.

Typical values are around $\beta = 0.9$. CS231n reports cross-validating values such as 0.5, 0.9, 0.95 and 0.99, and sometimes increasing momentum during training.[^cs231n-nn3]

## Worked Example

**Inputs.** $\mathcal{L}(w) = w^2$, so $g = 2w$. Start at $w_0 = 1$ with $\alpha = 0.1$, $\beta = 0.9$, $v_0 = 0$, using convention A.

**Step 1.**

$$
g_1 = 2, \qquad v_1 = 2, \qquad w_1 = 1 - 0.1 \times 2 = 0.8
$$

**Step 2.**

$$
g_2 = 1.6, \qquad v_2 = 0.9 \times 2 + 1.6 = 3.4, \qquad w_2 = 0.8 - 0.34 = 0.46
$$

**Step 3.**

$$
g_3 = 0.92, \qquad v_3 = 0.9 \times 3.4 + 0.92 = 3.98, \qquad w_3 = 0.46 - 0.398 = 0.062
$$

Plain gradient descent with the same learning rate reaches only $0.8$, $0.64$ and $0.512$. Momentum gets much closer to the minimum in three steps, but its velocity keeps it moving: the iterate passes zero and reaches about $-0.709$ at step 6 before turning back. Faster progress and overshoot come from the same inertia. [[Nesterov Momentum]] reduces the overshoot on this problem. The values were recalculated in Python.

## Benefits and Pitfalls

- **Faster progress along consistent directions**, including across flat regions of the loss surface.
- **Damped oscillations** across steep, narrow valleys, because alternating gradient signs cancel in the velocity.
- **Overshoot.** High momentum with a large learning rate can overshoot or become unstable; retune $\alpha$ when changing $\beta$.
- **Implementation details matter.** Compare convention, dampening and buffer initialisation before reproducing results across frameworks.

Momentum is one of a broader family of accelerated gradient methods that use past gradients in the update. Some of these methods have convergence guarantees under assumptions about the loss, such as convexity.

## Related Notes

- [[Optimization Algorithms]] — Comparison of optimisers.
- [[Nesterov Momentum]] — Evaluates the gradient at a look-ahead point.
- [[Adam Optimizer]] — Combines a momentum-like first moment with per-parameter scaling.

## References & Useful Links

[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Physical interpretation, convention B update, typical values and momentum schedules.
[^pytorch-sgd]: [PyTorch 2.14: torch.optim.SGD](https://docs.pytorch.org/docs/2.14/generated/torch.optim.SGD.html) — PyTorch's momentum formula, how it differs from Sutskever et al., and buffer initialisation.
