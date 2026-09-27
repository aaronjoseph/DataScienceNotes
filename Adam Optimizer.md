---
tags:
  - "ds-foundations"
---

Adam (adaptive moment estimation; Kingma and Ba, 2015) combines a momentum-like moving average of gradients with RMSProp-style per-parameter scaling, and corrects both averages for their start-up bias.[^kingma]

## Algorithm

**Notation.** At step $t = 1, 2, \dots$, $g_t$ is the gradient, $m_t$ the first-moment estimate (a moving average of gradients), and $v_t$ the second-moment estimate (a moving average of squared gradients). Both start at zero. $\alpha$ is the learning rate, $\beta_1$ and $\beta_2$ are decay rates, and $\epsilon$ prevents division by zero. All operations are element-wise.

**Step 1: update the first moment.** This plays the role of the velocity in [[Momentum]], but as a true average with the $(1 - \beta_1)$ factor:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) \, g_t
$$

**Step 2: update the second moment.** This is the same average as in [[Adagrad and RMSProp|RMSProp]]:

$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) \, g_t^2
$$

**Step 3: correct the bias.**

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$

**Step 4: update the parameters with the corrected moments.**

$$
w_t = w_{t-1} - \frac{\alpha \, \hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

This follows the PyTorch and CS231n presentation, with $\epsilon$ added after the square root and the *corrected* moments used in the update.[^pytorch-adam][^cs231n-nn3] Notation varies between sources: [[Momentum]] uses $v$ for the velocity and [[Adagrad and RMSProp]] uses $G$ for the squared-gradient accumulator.

## Why Bias Correction Matters

Because $m_0 = v_0 = 0$, both moving averages are biased towards zero during the first steps. The bias is stronger for $v$ because $\beta_2$ is closer to 1. The uncorrected ratio $m_t / \sqrt{v_t}$ is therefore too **large** early in training, not too small.

**Inputs.** Constant gradient $g = 0.5$, $\alpha = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, first step $t = 1$.

**Step 1: raw moments.**

$$
m_1 = 0.1 \times 0.5 = 0.05, \qquad v_1 = 0.001 \times 0.25 = 0.00025
$$

**Step 2: uncorrected step.**

$$
\frac{\alpha \, m_1}{\sqrt{v_1}} = \frac{0.001 \times 0.05}{0.0158} \approx 0.0032
$$

**Step 3: corrected moments and step.**

$$
\hat{m}_1 = \frac{0.05}{0.1} = 0.5, \qquad \hat{v}_1 = \frac{0.00025}{0.001} = 0.25, \qquad \frac{\alpha \, \hat{m}_1}{\sqrt{\hat{v}_1}} = 0.001
$$

Without correction the first step is about 3.2 times the learning rate. With correction it is exactly $\alpha$, and it would still be $\alpha$ if the gradient were $0.05$ or $50$. More generally, multiplying one parameter's gradients by a constant $c > 0$ multiplies both $\hat{m}_t$ and $\sqrt{\hat{v}_t}$ by $c$, leaving the update unchanged apart from $\epsilon$. This is the invariance to diagonal rescaling of the gradients claimed in the paper.[^kingma] The values were recalculated in Python.

## Hyperparameters

| Hyperparameter | Common default | Role |
|---|---|---|
| $\alpha$ | $10^{-3}$ | Base step size |
| $\beta_1$ | $0.9$ | Memory of the gradient average |
| $\beta_2$ | $0.999$ | Memory of the squared-gradient average |
| $\epsilon$ | $10^{-8}$ | Numerical stability |

These are the values recommended in the paper and the PyTorch 2.14 defaults.[^pytorch-adam][^cs231n-nn3] The paper's abstract says the hyperparameters "typically require little tuning". In practice the learning rate and its schedule are still usually tuned.

## Claimed Advantages

The paper's abstract describes Adam as computationally efficient, with small memory requirements, invariant to diagonal rescaling of the gradients, and suited to large problems, non-stationary objectives, and noisy or sparse gradients.[^kingma] These are the authors' claims; how much they matter depends on the task. CS231n calls Adam a reasonable default and also recommends trying SGD with Nesterov momentum.[^cs231n-nn3]

## Weight Decay versus L2 Regularisation

With plain SGD, adding an [[L1 and L2 Regularization|L2 penalty]] to the loss is equivalent to weight decay, once rescaled by the learning rate. With Adam it is not: the penalty's gradient is divided by $\sqrt{\hat{v}_t}$ like every other gradient, so parameters with large gradient history are regularised less. Loshchilov and Hutter proposed **AdamW**, which applies weight decay directly to the weights, separately from the adaptive step. Their abstract reports that this improves Adam's generalisation, letting it compete with SGD with momentum on image classification where Adam had typically been outperformed.[^adamw]

In PyTorch 2.14, `torch.optim.Adam(weight_decay=...)` adds an L2 term to the gradient, while `decoupled_weight_decay=True` makes it equivalent to AdamW.[^pytorch-adam]

## Variants

- **AMSGrad** keeps the maximum of past second-moment estimates; PyTorch exposes it as `amsgrad=True`.[^pytorch-adam]
- **Nadam** adds Nesterov momentum to Adam; see [[Optimization Algorithms#Other Variants]].
- **AdaMax** is a variant based on the infinity norm, introduced in the Adam paper.[^kingma]

## Related Notes

- [[Optimization Algorithms]] — Comparison with other optimisers.
- [[Momentum]] and [[Adagrad and RMSProp]] — The two ideas Adam combines.
- [[Gradient Descent]] — The base update.

## References & Useful Links

[^kingma]: [Adam: A Method for Stochastic Optimization (Kingma and Ba, ICLR 2015)](https://arxiv.org/abs/1412.6980) — The abstract was read: efficiency, invariance to diagonal rescaling, suitability for non-stationary and sparse problems, little tuning, and AdaMax. The full text was not accessible as text in this revision.
[^pytorch-adam]: [PyTorch 2.14: torch.optim.Adam](https://docs.pytorch.org/docs/2.14/generated/torch.optim.Adam.html) — Algorithm with bias correction, defaults, AMSGrad, and `decoupled_weight_decay`.
[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Simplified and bias-corrected Adam updates, recommended values, and practical advice.
[^adamw]: [Decoupled Weight Decay Regularization (Loshchilov and Hutter, ICLR 2019)](https://arxiv.org/abs/1711.05101) — Abstract: L2 regularisation and weight decay differ for adaptive methods such as Adam; AdamW.