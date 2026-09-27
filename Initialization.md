---
tags:
  - "ds-foundations"
---

Initialisation sets the weights before training starts. It determines the scale of activations and gradients in the first steps, and therefore whether gradients can flow through a deep network at all. A poor choice can leave much of the model's capacity unused.

## Why Initialisation Matters

- **Symmetry breaking.** If every weight in a layer starts with the same value, every unit computes the same output and receives the same gradient, so the units stay identical and the layer behaves like a single unit. Random initialisation breaks this symmetry.
- **Signal scale.** Each layer multiplies its input by a weight matrix. If the weights are too small, activations and gradients shrink layer by layer; if they are too large, they grow or saturate the non-linearity. Deeper networks are more sensitive because these effects compound.
- **Saturation.** With [[Tanh Function|tanh]] or [[Sigmoid Function|sigmoid]] units, large pre-activations push units into flat regions where the gradient is near zero. Glorot and Bengio found that the logistic sigmoid is poorly suited to deep networks with random initialisation because its mean value can drive the top hidden layer into saturation.[^glorot]
- **Learning dynamics.** If initial gradients are tiny, little learning happens; if they are huge, training may diverge. See [[Vanishing & Exploding Gradients]].

## Common Schemes

**Notation.** For a weight matrix, $\text{fan\_in}$ is the number of inputs to each unit and $\text{fan\_out}$ the number of outputs. A *gain* factor adjusts the scale for the non-linearity that follows.

### Small Random Values

Drawing weights from a narrow normal distribution breaks symmetry and keeps most activation functions in their near-linear region at the start. A fixed standard deviation, however, ignores layer width: activations then shrink or grow depending on the fan-in. The scaled schemes below fix that.

### Xavier (Glorot) Initialisation

Glorot and Bengio proposed scaling the weights so that activation and gradient variances stay roughly constant across layers.[^glorot] PyTorch implements two forms:[^pytorch-init]

**Uniform form.** Sample from $\mathcal{U}(-a, a)$ with:

$$
a = \text{gain} \times \sqrt{\frac{6}{\text{fan\_in} + \text{fan\_out}}}
$$

**Normal form.** Sample from $\mathcal{N}(0, \text{std}^2)$ with:

$$
\text{std} = \text{gain} \times \sqrt{\frac{2}{\text{fan\_in} + \text{fan\_out}}}
$$

Both give the same variance. "Uniform" and "normal" are two versions of one scheme, not different schemes. The PyTorch gain for tanh is $5/3$.

### He (Kaiming) Initialisation

He et al. derived an initialisation that explicitly accounts for rectifier non-linearities such as ReLU. It enabled them to train very deep rectified networks from scratch.[^he] It is a separate derivation, not merely a relabelled Xavier scheme. PyTorch's normal form is:[^pytorch-init]

$$
\text{std} = \frac{\text{gain}}{\sqrt{\text{fan\_mode}}}
$$

For ReLU the gain is $\sqrt{2}$. With the default $\text{fan\_mode} = \text{fan\_in}$, this gives:

$$
\text{std} = \sqrt{\frac{2}{\text{fan\_in}}}
$$

Choosing `fan_in` preserves variance in the forward pass; choosing `fan_out` preserves it in the backward pass.

## Worked Example

**Inputs.** A dense layer with $\text{fan\_in} = 256$ and $\text{fan\_out} = 128$, with gain 1 for Xavier and gain $\sqrt{2}$ for He.

**Step 1: Xavier normal.**

$$
\text{std} = \sqrt{\frac{2}{256 + 128}} = \sqrt{0.00521} \approx 0.0722
$$

**Step 2: Xavier uniform.**

$$
a = \sqrt{\frac{6}{384}} = 0.125
$$

**Step 3: He normal.**

$$
\text{std} = \sqrt{\frac{2}{256}} \approx 0.0884
$$

The uniform bound $0.125$ has the same variance as the Xavier normal draw, because a $\mathcal{U}(-a, a)$ variable has variance $a^2 / 3 = 0.00521$. He initialisation is wider. For inputs symmetric around zero, ReLU sets about half of its inputs to zero, and the factor 2 compensates for that lost signal. The values were recalculated in Python.

## Pitfalls

- **Framework shape conventions.** PyTorch computes fans assuming a `Linear` weight of shape `[fan_out, fan_in]`, used as `x @ w.T`. If your code stores weights the other way round, pass the transposed matrix to the initialiser.[^pytorch-init]
- **Match the scheme to the activation.** Use a Xavier-style scale for tanh-like units and a He-style scale for ReLU-like units, and check the gain.
- **Diagnose rather than guess.** Plot activation and gradient histograms per layer. All-zero or fully saturated tanh units at the start of training indicate a scale problem.[^cs231n-nn3]
- **Interaction with other components.** Normalisation layers such as [[Layer Normalization]] and the optimiser also affect early training, so initialisation is necessary but not sufficient.

## Related Notes

- [[Glorot and He Initialization]] — Short companion note on the same schemes.
- [[Vanishing & Exploding Gradients]] — The failure mode that good initialisation helps prevent.
- [[Jacobians]] — Layer Jacobians with singular values near 1 keep signals stable.
- [[Nesterov Momentum]] — Sutskever et al. found initialisation and momentum jointly crucial.

## References & Useful Links

[^glorot]: [Understanding the Difficulty of Training Deep Feedforward Neural Networks (Glorot and Bengio, AISTATS 2010)](https://proceedings.mlr.press/v9/glorot10a.html) — Abstract: sigmoid saturation with random initialisation, layer Jacobians, and a new initialisation scheme.
[^he]: [Delving Deep into Rectifiers (He et al., 2015)](https://arxiv.org/abs/1502.01852) — Abstract: a robust initialisation for rectifier networks that enables training very deep models from scratch.
[^pytorch-init]: [PyTorch 2.14: torch.nn.init](https://docs.pytorch.org/docs/2.14/nn.init.html) — Exact Xavier and Kaiming formulas, gains per non-linearity, `fan_in` versus `fan_out`, and the weight-shape convention.
[^cs231n-nn3]: [CS231n: Neural Networks Part 3 — Learning and Evaluation](https://cs231n.github.io/neural-networks-3/) — Using activation and gradient histograms to diagnose incorrect initialisation.