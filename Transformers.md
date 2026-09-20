# Transformers

#search-eng

## Intuition

A Transformer updates token representations using attention: each position combines information from other allowed positions. Learned projections determine which relationships are useful. Attention is not parameter-free.

## Main Components

For input matrix $X$, learned matrices form $Q=XW_Q$, $K=XW_K$, and $V=XW_V$. Scaled dot-product attention is:

$$\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V.$$

Softmax acts across keys. Mask $M$ excludes padding or future positions as required. Multi-head attention uses several projections, combines their outputs, and applies an output projection. Position-wise feed-forward layers add nonlinear transformations; residual connections and normalisation support optimisation.

Position information matters: unmasked self-attention without positional information is permutation-equivariant, not a general model of word order. Positional schemes vary; sinusoidal encoding and hidden size 512 describe the original base architecture, not universal requirements.

## Architecture Choices

| Architecture | Typical information access | Common use |
|---|---|---|
| [[Encoder-Only Model (Transformers)\|Encoder]] | Bidirectional input context | Representation learning and classification |
| [[Decoder-Only Model (Transformers)\|Decoder]] | Causal preceding context | Autoregressive generation |
| [[Encoder-Decoder Model (Transformers)\|Encoder–decoder]] | Input encoder plus causal decoder and cross-attention | Input-to-output sequence tasks |

Self-attention uses representations from the same sequence; cross-attention takes queries from one stream and keys/values from another. The original Transformer removed recurrence, not all sequential work: autoregressive output generation still proceeds token by token.

## Cost and Limitations

Naive dense self-attention materialises pairwise interactions that grow quadratically with sequence length. Implementation and attention variants change actual memory and runtime. Context windows remain bounded; residual connections do not guarantee freedom from optimisation problems.

## Search Exercise

Compare separately encoded query/document vectors with jointly encoding `[query, document]`. Which work can be done before a query arrives? Which method permits query–document interactions inside attention? Connect the answer to [[Embeddings]], [[Search Ranking]], and [[Latency vs Throughput]].

## Existing Reading Collection

![[Transformer Papers]]

## Existing Illustrations

![[Transformers-1.png]]

![[Transformers.png]]

![[Masked_SA&SA.png]]

## References & Useful Links

- [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Original equations and architecture.
- [PyTorch scaled dot-product attention](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.scaled_dot_product_attention.html) — Masks and implementation options.

Previously saved resources (retained for further reading; not used to verify this revision):
- [www.youtube.com — watch](https://www.youtube.com/watch?v=9uw3F6rndnA)
- [www.datacamp.com — building-a-transformer-with-py-torch](https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch)
- [arxiv.org — 2207.09238](https://arxiv.org/pdf/2207.09238)
- [jalammar.github.io — illustrated-gpt2](http://jalammar.github.io/illustrated-gpt2/)
- [www.youtube.com — watch](https://www.youtube.com/watch?v=UPtG_38Oq8o)
- [nlp.seas.harvard.edu — attention.html](https://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [arxiv.org — 1706.03762.pdf](https://arxiv.org/pdf/1706.03762.pdf)
