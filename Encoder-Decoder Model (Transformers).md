---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

An encoder–decoder [[Transformers|Transformer]] maps an input sequence to a different output sequence. The **encoder** reads the whole input bidirectionally and produces one vector per input token. The **decoder** generates the output one token at a time, using causal self-attention over what it has produced and cross-attention over the encoder's vectors. The original Transformer used this design for [[Machine Translation|translation]].[^aiayn]

## The Probability Being Modelled

$$
P(y\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},\,x)
$$

- $x$ is the input sequence, such as a query or source sentence.
- $y_t$ is output token $t$, and $y_{<t}$ are the output tokens before it.
- $T$ is the output length, which need not match the input length.

An end-of-sequence token or a configured maximum length stops generation.

## Inside the Decoder: Three Sub-Layers

Each decoder layer contains three sub-layers, each wrapped in a residual connection and [[Layer Normalization]]:[^aiayn]

1. **Masked self-attention** over the output generated so far, so position $t$ cannot see later output tokens.
2. **Cross-attention** where queries come from the decoder and keys and values come from the final encoder output. Every decoder position can look at every input position.
3. **Feed-forward network** applied at each position.

### Shapes in cross-attention

With an input of $n$ tokens and $m$ output tokens so far:

- Decoder queries: $m \times d_k$.
- Encoder keys and values: $n \times d_k$ and $n \times d_v$.
- Attention weights: $m \times n$, one row per output position and one column per input position.

Row $t$ of this matrix is a soft alignment that shows which input tokens influenced output token $t$. This is the Transformer form of the alignment idea from attention-based translation.[^bahdanau]

## Training with Teacher Forcing

During training, the decoder receives the **correct** earlier output tokens rather than its own predictions. This is called teacher forcing, and together with the causal mask it lets one forward pass train every output position.

### Worked example: a query rewrite

Inputs:

- Encoder input: `mens waterprof boots` (with a typo).
- Target output: `men's waterproof boots <eos>`.

The decoder input is the target shifted right by one position, starting with a start token:

| Step $t$ | Decoder input so far | Target $y_t$ |
|---:|---|---|
| 1 | `<s>` | `men's` |
| 2 | `<s> men's` | `waterproof` |
| 3 | `<s> men's waterproof` | `boots` |
| 4 | `<s> men's waterproof boots` | `<eos>` |

The encoder sees the full input at every step. The decoder sees only the prefix in its own column plus the encoder vectors. The loss is the average cross-entropy over the four targets.

At inference, no target exists. The decoder feeds back its own predictions, so an early mistake, such as producing `women's`, conditions every later step. This difference between training and inference is sometimes called exposure bias.

## Inference and Cost

1. Run the encoder **once** over the input.
2. Run the decoder repeatedly, one output token per step, reusing the encoder output for cross-attention at every step.
3. Stop at `<eos>` or a length limit.

The original Transformer translated with beam search (beam size 4, length penalty 0.6) and a maximum output length of the input length plus 50.[^aiayn] See [[Decoder-Only Model (Transformers)#Decoding Strategies|decoding strategies]] and [[Decoder-Only Model (Transformers)#Serving and the KV Cache|KV caching]], which apply to the decoder here too.

For a short input and a longer output, the decoder dominates cost. For a long input and a short output, such as classifying a document into a label word, the single encoder pass dominates.

## Well-Known Encoder–Decoder Models

| Model | Training idea | What it shows |
|---|---|---|
| Original Transformer | Supervised translation pairs | Attention-only sequence-to-sequence[^aiayn] |
| T5 | Every task cast as text-to-text; pretrained on the C4 web corpus | One model and loss for classification, question answering, and summarisation[^t5] |
| BART | Corrupt text, then reconstruct it; best results from sentence shuffling plus span in-filling | Bidirectional encoder like [[BERT]], left-to-right decoder like GPT[^bart] |

BART's authors describe it as generalising both BERT, through its bidirectional encoder, and GPT, through its left-to-right decoder. They report that it is particularly effective when fine-tuned for generation, while matching RoBERTa on GLUE and SQuAD with comparable training resources.[^bart]

## Uses and Limits

Translation, summarisation, and rewriting fit this structure. Control or task tokens, such as T5's text prefixes, influence behaviour only when the model was trained to interpret them; inventing a new prefix does not guarantee control.

For search, query rewriting can use this structure, but a fluent rewrite can alter an identifier, negation, or constraint. Retain the original query and evaluate intent preservation in [[Query Understanding]].

## Exercise

For an input product query and a generated rewrite, identify which tokens the encoder sees, which the decoder sees during training, and what changes at inference. Compare [[Encoder-Only Model (Transformers)|encoder-only]] and [[Decoder-Only Model (Transformers)|decoder-only]] models.

> [!example]- Exercise solution
> **Encoder.** It sees every input token, bidirectionally, during both training and inference.
>
> **Decoder during training.** At step $t$ it sees the correct output tokens $y_1, \ldots, y_{t-1}$ plus the encoder vectors, but never $y_t$ or later tokens.
>
> **Decoder at inference.** It sees its own earlier predictions instead of correct tokens, so errors can compound.
>
> **Comparison.** An encoder-only model sees the whole input but has no generation step; it suits classification or scoring the rewrite. A decoder-only model puts the input and output in one causal sequence, so input tokens see only earlier input tokens, whereas the encoder–decoder reads the input bidirectionally.

## References & Useful Links

[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Encoder and decoder stacks, cross-attention, and beam-search settings. Primary reference for the original explanation.
[^bahdanau]: [Bahdanau, Cho & Bengio (2014)](https://arxiv.org/abs/1409.0473) — Soft alignment between source and target words.
[^t5]: [Raffel et al. (2019), Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) — Text-to-text framing and the C4 corpus.
[^bart]: [Lewis et al. (2019), BART](https://arxiv.org/abs/1910.13461) — Denoising sequence-to-sequence pretraining and its relation to BERT and GPT.
