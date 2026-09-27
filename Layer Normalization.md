---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

Layer normalization (LayerNorm) rescales each example's activation vector so that its features have zero mean and unit variance, then applies a learned scale and shift. The statistics come from the features of **one** example at **one** position, not from the rest of the mini-batch. Ba, Kiros, and Hinton introduced it in 2016, and it sits inside every block of the original [[Transformers|Transformer]].[^ln][^aiayn]

## Why Normalise Activations?

Deep networks train faster and more stably when the inputs to each layer stay in a reasonable range. Batch normalization (BatchNorm) was an earlier way to achieve this, but it has two practical drawbacks that LayerNorm avoids:[^ln]

- Its statistics depend on the mini-batch, so behaviour changes with batch size.
- It is not obvious how to apply it to recurrent networks, where each time step has different statistics.

LayerNorm computes statistics from all the summed inputs to the neurons in a layer for a single training case. It therefore performs exactly the same computation during training and at test time, and it can be applied at every time step of a recurrent network.[^ln]

> [!warning] "Internal covariate shift" is a contested explanation
> This note originally explained normalization as a fix for internal covariate shift: layer input distributions changing during training. That was the original motivation for BatchNorm, but later work found that stabilising layer input distributions has little to do with BatchNorm's success, and proposed instead that normalization makes the optimisation landscape smoother.[^santurkar] Treat covariate shift as historical motivation, not an established mechanism.

## The Computation

Notation, for one token's activation vector:

- $x \in \mathbb{R}^{H}$: the vector, with $H$ features.
- $\gamma, \beta \in \mathbb{R}^{H}$: learned gain and bias, one value per feature.
- $\epsilon$: a small constant for numerical stability.

**Step 1 — mean over features**

$$
\mu = \frac{1}{H}\sum_{i=1}^{H} x_i
$$

**Step 2 — variance over features**

$$
\sigma^2 = \frac{1}{H}\sum_{i=1}^{H} (x_i - \mu)^2
$$

**Step 3 — normalise**

$$
\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2 + \epsilon}}
$$

**Step 4 — scale and shift**

$$
y_i = \gamma_i\,\hat{x}_i + \beta_i
$$

$\epsilon$ is added to the variance inside the square root, not to the standard deviation. The learned $\gamma$ and $\beta$ let the model recover any scale or offset it needs, so normalisation does not limit what the layer can represent.

## Worked Example

Inputs: $x = [1,\ 2,\ 3,\ 6]$, $\gamma = 1$, $\beta = 0$, and a negligible $\epsilon$.

**Step 1 — mean**

$$
\mu = \frac{1 + 2 + 3 + 6}{4} = 3
$$

**Step 2 — variance**

$$
\sigma^2 = \frac{(-2)^2 + (-1)^2 + 0^2 + 3^2}{4} = \frac{14}{4} = 3.5
$$

**Step 3 — standard deviation**

$$
\sqrt{3.5} \approx 1.8708
$$

**Step 4 — normalised vector**

$$
\hat{x} = \frac{[-2,\ -1,\ 0,\ 3]}{1.8708} \approx [-1.069,\ -0.5345,\ 0,\ 1.6036]
$$

The output has mean 0 and variance 1. The ordering and relative spacing of the four features are preserved; only their location and scale change. Multiplying $x$ by 10 would give the same $\hat{x}$.

## LayerNorm versus BatchNorm

| | LayerNorm | BatchNorm |
|---|---|---|
| Statistics computed over | Features of one example | One feature across the batch |
| Train versus test | Identical computation | Running averages at test time |
| Depends on batch size | No | Yes |
| Recurrent, variable-length input | Straightforward | Awkward |

For a Transformer input of shape (batch, sequence, hidden), LayerNorm normalises each token's hidden vector separately. Padding tokens therefore do not change the statistics of real tokens.

## Where the Normalisation Sits

The original Transformer applies LayerNorm **after** each residual addition. This is **Post-LN**:[^aiayn]

$$
x_{\text{out}} = \operatorname{LayerNorm}(x + \operatorname{Sublayer}(x))
$$

**Pre-LN** normalises the input to each sub-layer and leaves the residual path untouched:

$$
x_{\text{out}} = x + \operatorname{Sublayer}(\operatorname{LayerNorm}(x))
$$

Xiong et al. showed that, at initialisation, Post-LN has large expected gradients for parameters near the output. A large learning rate is then unstable, which explains why Post-LN needs a learning-rate warm-up stage. Pre-LN gradients are well behaved at initialisation. In their experiments, Pre-LN models without warm-up reached comparable results with less training time and hyperparameter tuning.[^preln]

## RMSNorm: A Simpler Variant

Root-mean-square normalization (RMSNorm) drops the mean subtraction and divides by the root mean square:[^rmsnorm]

$$
\operatorname{RMS}(x) = \sqrt{\frac{1}{H}\sum_{i=1}^{H} x_i^2}
$$

$$
y_i = \gamma_i \frac{x_i}{\operatorname{RMS}(x)}
$$

For the same $x = [1,\ 2,\ 3,\ 6]$:

**Step 1 — root mean square**

$$
\operatorname{RMS}(x) = \sqrt{\frac{1 + 4 + 9 + 36}{4}} \approx 3.5355
$$

**Step 2 — rescaled vector**

$$
\frac{x}{3.5355} \approx [0.2828,\ 0.5657,\ 0.8485,\ 1.6971]
$$

The output is rescaled but not centred. Its authors hypothesised that re-centring is dispensable and reported performance comparable to LayerNorm with 7–64% lower running time across the models they tested.[^rmsnorm]

## In Code

```python
import numpy as np

def layer_norm(x, gamma, beta, eps=1e-5):
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return gamma * (x - mean) / np.sqrt(var + eps) + beta

x = np.array([[1.0, 2.0, 3.0, 6.0],
              [10.0, 20.0, 30.0, 60.0]])
y = layer_norm(x, gamma=np.ones(4), beta=np.zeros(4))

assert np.allclose(y[0], y[1], atol=1e-4)
assert np.allclose(y.mean(axis=-1), 0.0)
assert np.allclose(y.var(axis=-1), 1.0, atol=1e-4)
print(np.round(y[0], 4))
```

Each row is normalised independently along the last axis. The second row is the first multiplied by 10, and both produce the same output, which confirms scale invariance. The tiny differences come only from $\epsilon$.

## Benefits and Limitations

**Benefits**

- Stabilises training; in the original experiments it substantially reduced training time compared with previously published techniques.[^ln]
- Works with any batch size, including a batch of one at serving time.
- Uses the same computation during training and inference.

**Limitations**

- Adds computation at every sub-layer; RMSNorm was motivated partly by this overhead.[^rmsnorm]
- Placement matters: Post-LN typically needs learning-rate warm-up.[^preln]
- It does not remove every optimisation problem; learning rate, initialisation, and depth still matter.
- $\epsilon$ is part of the model. Hugging Face's BERT configuration uses $10^{-12}$, so reimplementing a checkpoint with a different value can change outputs slightly.[^hf-bert]

## Exercise

1. Normalise $x = [5,\ 5,\ 5,\ 5]$ with $\gamma = 1$ and $\beta = 0$. What happens, and why is $\epsilon$ needed?
2. A colleague computes normalisation statistics across the batch dimension instead of the feature dimension. What would change at serving time with a batch size of one?

> [!example]- Exercise solution
> 1. The mean is 5 and the variance is 0, so every $x_i - \mu$ is 0. Without $\epsilon$ the calculation divides zero by zero. With $\epsilon$, the output is $[0,\ 0,\ 0,\ 0]$, which becomes $\beta$ after the affine step. A constant vector carries no information about relative feature values, so returning $\beta$ is reasonable.
>
> 2. That is effectively BatchNorm without running statistics. With a batch of one, each feature's batch mean equals the value itself, so every normalised output would be zero. Predictions would also change with the composition of each batch. LayerNorm avoids this because each example is normalised using only its own features.

## References & Useful Links

[^ln]: [Ba, Kiros & Hinton (2016), Layer Normalization](https://arxiv.org/abs/1607.06450) — Definition, comparison with batch normalization, and training-time results.
[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Post-LN placement in the original Transformer.
[^santurkar]: [Santurkar et al. (2018), How Does Batch Normalization Help Optimization?](https://arxiv.org/abs/1805.11604) — Evidence against the internal-covariate-shift explanation.
[^preln]: [Xiong et al. (2020), On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745) — Post-LN versus Pre-LN gradients and warm-up.
[^rmsnorm]: [Zhang & Sennrich (2019), Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467) — RMSNorm and its reported efficiency.
[^hf-bert]: [Hugging Face Transformers — BERT](https://huggingface.co/docs/transformers/model_doc/bert) — Default `layer_norm_eps` in `BertConfig`.