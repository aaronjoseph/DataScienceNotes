**Paper:** *Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth* — Yihe Dong, Jean-Baptiste Cordonnier, and Andreas Loukas (arXiv 2021; revised 2023).[^dong]

## Background

Attention was first developed to help sequence models use the relevant parts of a long input. In translation, it let the decoder look back at every source word instead of relying on one fixed-length summary vector.[^bahdanau] It later became the core of [[Transformers|Transformer]] networks. This paper asks what attention on its own contributes, and what the other parts of a Transformer block are for.

## Problem

Transformers stack three kinds of component: self-attention, residual (skip) connections, and feed-forward networks (MLPs). Their success is well documented, but why the combination works is less understood. The authors study self-attention networks (SANs) in isolation to see what happens as layers are stacked.[^dong]

## Main Contribution

- **Path decomposition.** The output of a multi-head, multi-layer self-attention network can be written as a sum of smaller terms. Each term, or "path", follows one choice of head, or a skip, at each layer and behaves like a deep single-head network.
- **Rank collapse.** Without skip connections or MLPs, the output converges **doubly exponentially** with depth to a rank-1 matrix: every token ends up with essentially the same representation. The authors call this an inductive bias towards "token uniformity".
- **What prevents it.** Skip connections and MLPs stop this degeneration. The authors present this as a previously unrecognised benefit of skip connections, beyond their usual role in easing optimisation.
- **Interpretation.** Deep self-attention networks with skip connections behave like an ensemble of weakly dependent shallow networks.[^dong]

## Evidence

According to the abstract, experiments confirm the predicted convergence on several variants of standard Transformer architectures.[^dong] This summary is based on the arXiv abstract and the paper's introduction in the local PDF; the proofs and experimental details have not been reviewed here.

## Intuition

Each attention layer replaces every token vector with a weighted average of token vectors. Repeated averaging pulls vectors towards one another, much as repeatedly blurring an image removes its detail. A skip connection adds each token's own previous vector back in, preserving what makes it different. The feed-forward network transforms each position separately, which also counteracts pure averaging.

## Limitations and Assessment

- The main theorem concerns pure attention; real Transformers include skip connections, MLPs, and normalization, so the collapse is a tendency those components counteract rather than a failure of practical models.
- The result explains why the non-attention parts of a block are essential; it does not claim that attention is unimportant.
- Assessment: the paper is useful for understanding architecture choices, for example why removing residual connections from a deep Transformer can make token representations indistinguishable.

## Connections

- [[Transformers#The Rest of a Transformer Block|The rest of a Transformer block]] — Residual connections and feed-forward layers.
- [[Layer Normalization]] — Another component that stabilises deep stacks.
- [[Transformer Papers]] — The wider reading list.

## Full Text

![[Attention is not all you need.pdf]]

## References & Useful Links

[^dong]: [Dong, Cordonnier & Loukas (2021), Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth](https://arxiv.org/abs/2103.03404) — Abstract and paper; the embedded PDF is a local copy of this paper.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014), Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — Origin of attention for translation.