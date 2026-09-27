---
tags:
  - "ds-foundations"
---

Deep learning is the part of machine learning that trains multi-layer ("deep") artificial neural networks end to end with gradient-based optimisation. The networks were originally inspired by biological neurons, but the analogy is loose: modern networks are best understood as differentiable functions assembled from layers.[^cs231n-nn1] Their defining strength is learning useful representations directly from raw data, given enough data and compute.

## Key Ideas

### Hierarchical Compositionality

- **A cascade of non-linear transformations.** Each layer applies a linear map followed by a non-linearity. The non-linearity is essential: without it, stacked layers collapse into a single linear map (see the worked example).[^cs231n-nn1]
- **Multiple levels of representation.** Early layers of an image model tend to respond to simple patterns such as edges and colour blobs, and deeper layers to larger structures made of them.[^cs231n-cnn]

### End-to-End Learning

- **Goal-driven representations.** Instead of hand-engineering features, the network learns the features that help the training objective.
- **Learned feature extraction.** Because the features adapt to the task, deep models often outperform hand-crafted pipelines on perceptual data such as images, audio and text. They still need data and careful evaluation to do so.

### Distributed Representations

- **No single neuron encodes a concept.** Information is spread across the activations of many units, and each unit takes part in representing many inputs.
- **Groups of units work together.** Combinations of units can represent far more patterns than the same number of units used one per concept. [[Embeddings]] are the most familiar example: a dense vector in which no single dimension has a fixed meaning.

## Why Deep Learning Works, and When

- **Expressiveness.** A network with one hidden layer is already a universal approximator of continuous functions, but that theorem says little about learnability or efficiency in practice. The benefit of depth is largely empirical, and it is strongest for data with hierarchical structure such as images.[^cs231n-nn1]
- **Automatic, hierarchical feature learning**, from simple to complex, without manual feature design.
- **Scaling with data and compute.** Large models trained on large datasets underpin state-of-the-art results in computer vision, speech and machine translation, relying on backpropagation and gradient-based optimisation.[^baydin] More data does not help automatically: data quality, model size and optimisation must scale together.
- **When to prefer simpler models.** Small datasets, strict interpretability requirements, or tight latency and cost budgets can favour classical models; see [[Improving Machine Learning Performance]].

## The Training Loop

1. **Forward pass.** Compute predictions layer by layer, recording a [[Computational Graph]].
2. **Loss.** Compare predictions with targets; see [[Loss Function & Cost Function]] and [[Cross Entropy Loss]].
3. **Backward pass.** [[Backpropagation]], which is reverse-mode automatic differentiation, computes the gradient of the loss with respect to every parameter as a chain of vector–[[Jacobians|Jacobian]] products.
4. **Update.** An optimiser takes a step; see [[Gradient Descent]] and [[Optimization Algorithms]].
5. **Repeat** over mini-batches and [[Epochs]], monitoring validation performance.

Supporting pieces:

- **Initialisation**: [[Initialization]].
- **Activations**: [[ReLU Function]], [[Sigmoid Function]], [[Tanh Function]], [[Softmax Function]].
- **Gradient health**: [[Vanishing & Exploding Gradients]], [[Gradient Clipping]].
- **Regularisation**: [[Dropout - Neural Network]], [[L1 and L2 Regularization]].
- **Normalisation**: [[Layer Normalization]].

## Architectures

- [[Perceptron]] — The single-unit starting point.
- [[Convolutional Networks]] — Grid-structured data such as images.
- [[RNN]] and [[LSTM]] — Sequences processed step by step.
- [[Transformers]] — Attention-based sequence models; see also [[BERT]].
- [[Autoencoders]] and [[GAN]] — Representation learning and generative modelling.
- [[Transfer Learning]] — Reusing pretrained networks.

## Deep Learning in Search

Neural models appear throughout modern search stacks. Bi-encoders map queries and documents to vectors for [[Dense Retrieval]]. [[Cross-Encoder|Cross-encoders]] score query–document pairs jointly for re-ranking. Pretrained language models such as [[BERT]] supply the underlying representations. The same training loop applies; the differences lie in the data (queries, documents and relevance labels) and in the loss.

## Worked Example: Why Non-Linearity Matters

**Inputs.** A network with 3 inputs, one hidden layer of 4 units and 2 outputs, matching the small example in CS231n.[^cs231n-nn1]

**Step 1: count the parameters.**

$$
\underbrace{3 \times 4 + 4 \times 2}_{\text{weights}} + \underbrace{4 + 2}_{\text{biases}} = 20 + 6 = 26
$$

**Step 2: remove the activation.** Without a non-linearity the two layers compute:

$$
W_2 (W_1 x + b_1) + b_2 = (W_2 W_1) x + (W_2 b_1 + b_2)
$$

**Step 3: interpret.** $W_2 W_1$ is a single $2 \times 3$ matrix, so the "two-layer" network is just one linear layer with 8 effective parameters (6 weights and 2 biases).

The extra 18 parameters buy no extra expressiveness unless a non-linearity such as [[ReLU Function|ReLU]] or tanh sits between the layers.

## Limitations

- **Data and compute hungry.** Large models need large labelled datasets or pretraining, and substantial hardware; see [[GPU]].
- **Optimisation is non-convex.** Results depend on initialisation, learning rate and other hyperparameters; see [[Hyperparameter Tuning]].
- **Interpretability.** Distributed representations are hard to inspect; see [[Machine Learning Explainability]].
- **Distribution shift.** Learned features can fail silently when inputs change; see [[Data Drift]].

## References & Useful Links

[^cs231n-nn1]: [CS231n: Neural Networks Part 1 — Setting up the Architecture](https://cs231n.github.io/neural-networks-1/) — Loose brain analogy, necessity of non-linearities, universal approximation and depth, and parameter counting.
[^cs231n-cnn]: [CS231n: Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/) — Learned filters that respond to edges and colour blobs in early layers and larger patterns later.
[^baydin]: [Automatic Differentiation in Machine Learning: a Survey (Baydin et al., JMLR 2018)](https://arxiv.org/abs/1502.05767) — Backpropagation as reverse-mode AD, and its role behind state-of-the-art results as of 2018.

- [The Matrix Calculus You Need for Deep Learning (Parr and Howard)](https://explained.ai/matrix-calculus/index.html) — The matrix calculus behind backpropagation. It was saved in this note as "Mathematics of Deep Learning".
- [Deep Learning (Goodfellow, Bengio and Courville)](https://www.deeplearningbook.org/) — Free online textbook covering the foundations above.
