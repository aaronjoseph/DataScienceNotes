---
tags:
  - "ds-foundations"
---

Training a neural network is a search for weights that minimise a loss over a very high-dimensional parameter space. The choice of optimiser affects how fast training converges and how stable it is. This note compares the main first-order optimisers; the detailed notes are embedded at the end.

## Why Gradient-Based Methods Dominate

Finding good weights is a search problem over the loss surface. Random search, evolutionary or genetic algorithms, second-order methods and gradient-based methods can all be used in principle.[^baydin] Gradient methods dominate deep learning because reverse-mode automatic differentiation returns the full gradient for about the cost of a few forward passes, however many parameters there are (see [[Computational Graph]]).

Gradients are informative because of local smoothness: a small change in the weights gives a small, predictable change in the loss. The negative gradient is the direction of steepest local descent, and [[Gradient Descent]] repeatedly takes a small step in that direction.

## Difficult Terrain

- **Saddle points.** The gradient is zero, but the surface curves upwards in some directions and downwards in others. Plain SGD can stall near them, while adaptive methods such as RMSProp enlarge the step in low-gradient directions and can move away faster.[^cs231n-nn3]
- **Ravines (ill-conditioning).** The loss is steep across a valley and shallow along it. Plain gradient descent oscillates across the valley; [[Momentum]] damps the oscillation and accumulates speed along it.
- **Plateaus and saturation.** Saturated activations give near-zero gradients; see [[Sigmoid Function]] and [[Initialization]].
- **Gradient noise.** Mini-batch gradients are noisy estimates, so learning-rate schedules are common.

## Optimiser Comparison

| Method | State per parameter | Key idea | Main caveat |
|---|---|---|---|
| SGD | None | Step against the gradient | Sensitive to learning rate; slow in ravines |
| [[Momentum]] | Velocity | Accumulate past gradients | Can overshoot |
| [[Nesterov Momentum\|Nesterov]] | Velocity | Gradient at a look-ahead point | Same tuning as momentum |
| [[Adagrad and RMSProp\|Adagrad]] | Sum of squared gradients | Per-parameter step size | Step size only shrinks |
| [[Adagrad and RMSProp\|RMSProp]] | Moving average of squared gradients | "Leaky" Adagrad | Early steps inflated without bias correction |
| [[Adam Optimizer\|Adam]] | First and second moments | Momentum plus RMSProp with bias correction | L2 penalty interacts with adaptive scaling |

Every method still has a learning rate to tune. State matters for memory: momentum stores one extra value per parameter and Adam stores two, which counts when a model has billions of parameters.

### Other Variants

- **Nadam** incorporates Nesterov momentum into Adam (Dozat, 2016). It is available as `torch.optim.NAdam`, whose default learning rate is $2 \times 10^{-3}$ as of PyTorch 2.14.[^pytorch-nadam]
- **Adadelta** extends the Adagrad idea with per-dimension step sizes from first-order information only. Its abstract says it "requires no manual tuning of a learning rate".[^adadelta]
- **AdamW** decouples weight decay from Adam's adaptive step; see [[Adam Optimizer#Weight Decay versus L2 Regularisation|the Adam note]].
- **Second-order methods** such as Newton's method use curvature, but storing and inverting the Hessian is impractical for large networks. Quasi-Newton methods such as L-BFGS approximate it but are awkward with mini-batches.[^cs231n-nn3]

## Choosing in Practice

The CS231n notes recommend SGD with Nesterov momentum or Adam as defaults, together with a learning-rate decay schedule.[^cs231n-nn3] Treat that as a starting point rather than a rule: tune the learning rate first, then compare optimisers on validation performance, not only on training loss.

## Exercise

Minimise $L(w) = w^2$ from $w_0 = 1$ with learning rate $0.1$ and momentum $\beta = 0.9$. Run three steps each of plain gradient descent, momentum and Nesterov momentum. Compare your values with the worked examples in [[Momentum]] and [[Nesterov Momentum]], and explain why momentum moves faster at first but later overshoots.

## Detailed Notes

![[Momentum]]

![[Nesterov Momentum]]

![[Adagrad and RMSProp]]

![[Adam Optimizer]]

## References & Useful Links

[^baydin]: [Automatic Differentiation in Machine Learning: a Survey (Baydin et al., JMLR 2018)](https://arxiv.org/abs/1502.05767) — Network training can use methods from evolutionary algorithms to gradient-based optimisers; reverse-mode AD makes gradients cheap.
[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Update rules, saddle-point illustration, second-order methods, and recommended defaults.
[^pytorch-nadam]: [PyTorch 2.14: torch.optim.NAdam](https://docs.pytorch.org/docs/2.14/generated/torch.optim.NAdam.html) — NAdam algorithm, default hyperparameters, and the reference to "Incorporating Nesterov Momentum into Adam".
[^adadelta]: [ADADELTA: An Adaptive Learning Rate Method (Zeiler, 2012)](https://arxiv.org/abs/1212.5701) — Abstract describing a per-dimension, first-order method without a manually tuned learning rate.