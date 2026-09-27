---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

A Transformer is a neural network that builds a vector for every token in a sequence by letting each token look at (attend to) other tokens and mix in their information. It replaced recurrence with attention, so every position in a training sequence can be processed in parallel. Encoder models such as [[BERT]], the decoder models behind chat assistants, and encoder–decoder translation models are all assembled from the same blocks.

## Why Transformers Replaced Recurrent Models

[[RNN|Recurrent networks]] and [[LSTM|LSTMs]] read a sequence one step at a time: the hidden state at position $t$ depends on the state at $t-1$. That creates two problems:

- **Sequential computation:** position $t$ cannot be computed before position $t-1$, which limits parallelism within one training example.[^aiayn]
- **Long paths between distant tokens:** information from token 1 must pass through every intermediate state before it reaches token 100.

Attention first appeared as an add-on to recurrent encoder–decoders for [[Machine Translation|translation]]. It let the decoder "soft-search" the source sentence instead of relying on one fixed-length summary vector.[^bahdanau] The Transformer kept attention and removed recurrence entirely. A self-attention layer connects any two positions with a constant number of sequential operations, compared with $O(n)$ for a recurrent layer.[^aiayn]

## Prerequisites

- Vectors, dot products, and matrix multiplication; [[Cosine Similarity]] gives the dot-product intuition.
- [[Softmax Function|Softmax]], which turns scores into weights that sum to one.
- [[Tokenization]] and [[Embeddings]]: text becomes token IDs, then vectors.
- [[Layer Normalization]], residual connections, and [[Dropout - Neural Network|dropout]] for the supporting parts of each block.

## Notation

- $n$: number of tokens in the sequence.
- $d_{\text{model}}$: width of each token vector.
- $X \in \mathbb{R}^{n \times d_{\text{model}}}$: input matrix with one row per token.
- $h$: number of attention heads.
- $d_k$ and $d_v$: per-head key and value widths.
- $W_Q$, $W_K$, $W_V$: learned projection matrices.

## Self-Attention Step by Step

### 1. Project each token into a query, key, and value

$$
Q = XW_Q,\qquad K = XW_K,\qquad V = XW_V
$$

A helpful analogy is a small search engine inside the layer. The **query** describes what a token is looking for, each **key** describes what a token offers, and the **value** is the content passed on when they match. The projections are learned, so attention is not parameter-free.

### 2. Score every query against every key

$$
S = \frac{QK^{\top}}{\sqrt{d_k}}
$$

$S_{ij}$ measures how relevant token $j$ is to token $i$. The authors divide by $\sqrt{d_k}$ because large dot products push softmax into regions with extremely small gradients.[^aiayn] For random vectors with independent unit-variance components, a dot product has standard deviation $\sqrt{d_k}$; the division brings the scale back to about one.

### 3. Mask disallowed positions and normalise

$$
A = \operatorname{softmax}(S + M)
$$

Softmax runs along each row, across keys, so each row of $A$ sums to one. The mask $M$ contains $0$ for allowed positions and $-\infty$ for disallowed ones, such as padding or future tokens in a causal decoder.[^aiayn]

### 4. Mix the values

$$
\operatorname{Attention}(Q,K,V) = AV
$$

Each output row is a weighted average of value vectors. The same word can therefore receive a different vector in a different context.

## Worked Example with Three Tokens

To keep the arithmetic visible, use two-dimensional token vectors and set $W_Q=W_K=W_V=I$. Real models learn these matrices; this simplification only exposes the mechanics.

Inputs:

- `red` $= [1,\ 0]$
- `running` $= [0,\ 1]$
- `shoes` $= [1,\ 1]$
- $d_k = 2$, so $\sqrt{d_k}\approx 1.4142$

**Step 1 — raw dot products.** With $Q=K=X$:

$$
XX^{\top} =
\begin{bmatrix}
1 & 0 & 1\\
0 & 1 & 1\\
1 & 1 & 2
\end{bmatrix}
$$

**Step 2 — scale.** Divide every entry by $1.4142$. The `shoes` row becomes:

$$
[0.7071,\ 0.7071,\ 1.4142]
$$

**Step 3 — softmax for `shoes`.**

$$
e^{0.7071}\approx 2.0281,\qquad e^{1.4142}\approx 4.1133
$$

$$
\frac{[2.0281,\ 2.0281,\ 4.1133]}{8.1695} \approx [0.2483,\ 0.2483,\ 0.5035]
$$

**Step 4 — weighted sum of values.**

$$
0.2483\,[1,0] + 0.2483\,[0,1] + 0.5035\,[1,1] \approx [0.7517,\ 0.7517]
$$

`shoes` keeps about half of its own vector and receives equal contributions from `red` and `running`.

**Step 5 — apply a causal mask.** In a decoder, `running` at position 2 may not see `shoes` at position 3. Its scaled scores become $[0,\ 0.7071,\ -\infty]$, so softmax gives:

$$
\text{weights} \approx [0.3302,\ 0.6698,\ 0]
$$

**Step 6 — masked output for `running`.**

$$
0.3302\,[1,0] + 0.6698\,[0,1] \approx [0.3302,\ 0.6698]
$$

Without the mask, `running` would also attend to `shoes` and produce about $[0.5989,\ 0.8022]$. The mask changes which information can flow, which is how a decoder learns to predict the next token without seeing it.

## Multi-Head Attention

A single attention pattern mixes everything with one set of weights. Multi-head attention runs $h$ attentions in parallel on smaller projections, concatenates their outputs, and projects the result back:

$$
\operatorname{head}_i = \operatorname{Attention}(QW_i^{Q},\ KW_i^{K},\ VW_i^{V})
$$

$$
\operatorname{MultiHead}(Q,K,V) = \operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)\,W^{O}
$$

The original base model used $h=8$ and $d_k=d_v=d_{\text{model}}/h=64$, so the total cost is similar to one full-width head.[^aiayn] In the paper's ablation, a single head was 0.9 BLEU worse than the best setting, and quality also fell with too many heads.

The paper's visualisations show some heads apparently following long-distance dependencies or pronoun references.[^aiayn] Treat such pictures as suggestive, not as proof of what a head "means".

## The Rest of a Transformer Block

| Component | Role | Original base setting |
|---|---|---|
| Multi-head self-attention | Mixes information across positions | $h=8$ |
| Feed-forward network | Transforms each position independently | $d_{ff}=2048$ |
| Residual connection | Adds a sub-layer's input to its output | Around every sub-layer |
| [[Layer Normalization]] | Normalises each token vector | After each residual addition |
| [[Dropout - Neural Network\|Dropout]] | Regularises outputs and embeddings | $P_{drop}=0.1$ |

The position-wise feed-forward network is applied separately and identically at every position:[^aiayn]

$$
\operatorname{FFN}(x) = \max(0,\ xW_1 + b_1)\,W_2 + b_2
$$

The original block computes $\operatorname{LayerNorm}(x + \operatorname{Sublayer}(x))$. This is called **Post-LN**. Many later models normalise inside the residual branch instead, called **Pre-LN**; see [[Layer Normalization#Where the Normalisation Sits|normalisation placement]].

### Where the parameters live

For $d_{\text{model}}=512$, ignoring biases:

1. Attention projections ($W_Q, W_K, W_V, W_O$) per layer:

$$
4 \times 512^2 = 1{,}048{,}576
$$

2. Feed-forward weights per layer:

$$
2 \times 512 \times 2048 = 2{,}097{,}152
$$

In this configuration, the feed-forward network holds about two-thirds of each layer's weights.

## Positional Information

Self-attention compares vectors without knowing their order. Without extra information, shuffling the input tokens simply shuffles the outputs: the operation is permutation-equivariant. The original model added fixed sinusoidal encodings to the embeddings:[^aiayn]

$$
PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

$$
PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

With an illustrative $d_{\text{model}}=4$:

- Position 1 receives approximately $[0.8415,\ 0.5403,\ 0.0100,\ 1.0000]$.
- Position 2 receives approximately $[0.9093,\ -0.4161,\ 0.0200,\ 0.9998]$.

The first pair of dimensions changes quickly with position; the second pair changes slowly. Learned position embeddings produced nearly identical results in the paper's ablation.[^aiayn] [[BERT]] uses learned absolute positions, which is why its input length is capped at the trained maximum. Later models use other schemes, so check each model card rather than assuming the original one.

## Three Architecture Families

| Family | Attention pattern | Typical objective | Examples in this vault |
|---|---|---|---|
| [[Encoder-Only Model (Transformers)\|Encoder-only]] | Bidirectional | Masked-token prediction | [[BERT]], [[RoBERTa]], [[Cross-Encoder]] |
| [[Decoder-Only Model (Transformers)\|Decoder-only]] | Causal | Next-token prediction | GPT-style [[Language Model\|language models]] |
| [[Encoder-Decoder Model (Transformers)\|Encoder–decoder]] | Bidirectional encoder, causal decoder | Sequence-to-sequence | Translation and rewriting |

- **Self-attention** takes queries, keys, and values from the same sequence.
- **Cross-attention** takes queries from the decoder and keys/values from the encoder output.

The original Transformer removed recurrence, not all sequential work: generation still emits one output token at a time.

## How the Original Model Was Trained

The paper trained on WMT 2014 English–German, about 4.5 million sentence pairs, with a shared byte-pair vocabulary of about 37,000 tokens.[^aiayn] Several choices reappear in later recipes:

- **Optimiser:** Adam with $\beta_2=0.98$.
- **Warm-up:** the learning rate rises linearly for 4,000 steps, then decays with the inverse square root of the step number.
- **Label smoothing:** 0.1, which worsened perplexity but improved BLEU.
- **Scale:** the base model trained for 100,000 steps, about 12 hours on 8 P100 GPUs. The big model reached 28.4 BLEU on English–German.

These results belong to that dataset, hardware, and year; they are not general performance guarantees.

## Cost and Limitations

- **Quadratic attention:** a dense attention matrix has $n^2$ entries per head, so doubling the sequence length quadruples it. The paper notes that self-attention is cheaper per layer than recurrence when $n$ is smaller than $d$.[^aiayn] Fused kernels and memory-efficient implementations change real runtime without changing the mathematics.[^sdpa]
- **Finite context:** a model sees only a bounded window of tokens.
- **Depth needs support:** pure attention tends to make token representations collapse towards each other as layers stack; residual connections and feed-forward layers counteract this.[^dong] See [[Research_Paper/Attention is not all you need|Attention is not all you need]].
- **Attention weights are not explanations:** a large weight shows information flow in one layer, not the reason for a final prediction.

## Search Connections

- **Retrieval:** a bi-encoder embeds queries and documents separately for [[Dense Retrieval]] and [[Approximate Nearest Neighbours]].
- **Ranking:** a [[Cross-Encoder]] reads `[query, document]` jointly, so attention can compare every query token with every document token.
- **Query understanding:** encoder–decoder and decoder models can rewrite queries; see [[Query Understanding]].
- **Grounded generation:** decoders can answer from retrieved passages; see [[Retrieval-Augmented Generation]].
- **Serving:** sequence length and depth drive latency; see [[Latency vs Throughput]] and [[Decoder-Only Model (Transformers)#Serving and the KV Cache|KV caching]].

## Exercise

Compare separately encoded query and document vectors with jointly encoding `[query, document]`.

1. Which computation can happen before a query arrives?
2. In which design can a query token attend directly to a document token?
3. A query has 10 tokens and a document 200. Ignoring special tokens, how many attention scores does one head compute in one joint layer, and how many connect a query token with a document token?

> [!example]- Exercise solution
> 1. Separate encoding lets document vectors be computed and indexed offline. Only the query is encoded at request time.
>
> 2. Joint encoding. With separate encoding, query and document tokens never attend to each other; they interact only through the final similarity score.
>
> 3. The joint sequence has 210 tokens, so one head computes $210^2 = 44{,}100$ scores. Query-to-document and document-to-query pairs account for $2 \times 10 \times 200 = 4{,}000$ of them.
>
> This cost is why cross-encoders usually rerank a short candidate list; see [[Search Ranking]].

## Existing Reading Collection

![[Transformer Papers]]

## Existing Illustrations

![[Transformers-1.png]]

![[Transformers.png]]

![[Masked_SA&SA.png]]

## References & Useful Links

[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Architecture, scaled dot-product and multi-head attention, positional encoding, training setup, complexity comparison, and ablations. A [PDF version](https://arxiv.org/pdf/1706.03762.pdf) was previously saved.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014), Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — Attention as soft search over the source sentence.
[^sdpa]: [PyTorch scaled dot-product attention](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.scaled_dot_product_attention.html) — Masks and implementation options.
[^dong]: [Dong, Cordonnier & Loukas (2021), Attention is Not All You Need](https://arxiv.org/abs/2103.03404) — Rank collapse in pure attention and the counteracting role of skip connections and MLPs.

Previously saved resources (retained for further reading; not used to verify this revision):

- [YouTube video 9uw3F6rndnA](https://www.youtube.com/watch?v=9uw3F6rndnA) — Saved video; topic not rechecked.
- [DataCamp — Building a Transformer with PyTorch](https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch) — Implementation tutorial.
- [arXiv 2207.09238](https://arxiv.org/pdf/2207.09238) — Saved paper; title not rechecked.
- [Jay Alammar — The Illustrated GPT-2](http://jalammar.github.io/illustrated-gpt2/) — Visual walkthrough of a decoder-only model.
- [YouTube video UPtG_38Oq8o](https://www.youtube.com/watch?v=UPtG_38Oq8o) — Saved video; topic not rechecked.
- [Harvard NLP — The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html) — Line-by-line implementation of the original paper.
