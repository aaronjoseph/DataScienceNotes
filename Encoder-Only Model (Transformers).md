---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

An encoder-only model is a stack of [[Transformers|Transformer]] encoder layers with no decoder. Every token can attend to every other non-padding token, left and right, so the output is one context-aware vector per input token. Models such as [[BERT]] and [[RoBERTa]] learn these representations through masked-token training, then are adapted for classification, tagging, relevance scoring, or embeddings.[^hf-arch]

Encoder-only models **can produce embeddings**, but their suitability depends on training and on how token vectors are pooled. Standard encoder-only models are not trained as left-to-right text generators.

## How an Encoder Sees Its Input

### Attention mask

The only positions an encoder hides are padding tokens. For a batch padded to four tokens, where the real input is three tokens long:

```text
attention_mask = [1, 1, 1, 0]
```

Each row of the attention matrix is allowed to use columns 1–3 and ignores column 4. Compare this with a causal decoder, where row $i$ may use only columns $1..i$; see [[Decoder-Only Model (Transformers)#Causal Masking|causal masking]].

### Output shape

For a batch of $B$ sequences of length $n$ and hidden size $H$, the encoder returns a tensor of shape $(B, n, H)$: one vector per token.[^hf-bert]

- **Token-level tasks** such as [[Named Entity Recognition]] use every token vector.
- **Sequence-level tasks** such as intent classification or relevance need one vector per sequence, which requires pooling.

## Pretraining Objective

Because every token sees both sides, the model cannot be trained to predict the next token: it would already see it. Encoders are instead trained to recover hidden tokens:

- [[BERT]] masks 15% of tokens and predicts the originals; it also used next-sentence prediction.[^bert]
- [[RoBERTa]] keeps masked-token prediction, removes next-sentence prediction, and regenerates masks dynamically.[^roberta]

## Pooling: From Token Vectors to One Vector

| Method | How | When it fits |
|---|---|---|
| `[CLS]` vector | Take the first token's final vector | Fine-tuned classifiers and cross-encoders |
| Mean pooling | Average token vectors, excluding padding | Common for sentence embeddings trained with this pooling |
| Max pooling | Take the element-wise maximum | Less common; depends on training |

Use the pooling method the checkpoint was trained with. A pooling method chosen after training changes what the vector represents.

### Worked example: mean pooling with a padding mask

Inputs:

- Token vectors $h_1=[1,\ 2]$, $h_2=[3,\ 0]$, and a padding position $h_3=[9,\ 9]$.
- Mask $m = [1,\ 1,\ 0]$.

**Step 1 — masked mean**

$$
\bar{h} = \frac{\sum_i m_i h_i}{\sum_i m_i} = \frac{[1,2] + [3,0]}{2} = [2,\ 1]
$$

**Step 2 — the bug if the mask is ignored**

$$
\frac{[1,2] + [3,0] + [9,9]}{3} \approx [4.33,\ 3.67]
$$

The padding vector dominates the result. The same text would receive a different embedding depending on how long the other items in its batch were, which makes offline and online vectors disagree.

## Bi-Encoder and Cross-Encoder

| | Bi-encoder | Cross-encoder |
|---|---|---|
| Input | Query and document encoded separately | `[query, document]` encoded together |
| Document work | Precomputed offline and indexed | Repeated for every query |
| Query–document interaction | Only through the final similarity score | Inside every attention layer |
| Typical stage | [[Candidate Generation]], [[Dense Retrieval]] | Reranking in [[Search Ranking]] |

- **Bi-encoder:** document vectors can be stored and searched with [[Approximate Nearest Neighbours]].
- **Cross-encoder:** a [[Cross-Encoder]] predicts a relevance score for each pair. It can model fine-grained interactions, but each query–document pair costs a full forward pass.[^sbert-ce]

Neither design always wins. The usual pattern retrieves candidates with a cheap method and reranks a smaller set with a more expensive one.

A generic pooled pretrained vector is not automatically a good sentence-retrieval embedding. Check the training objective, pooling, normalisation, and evaluation data.

## Limitations & Common Pitfalls

- **Fixed maximum length:** BERT-style models have 512 learned positions; longer text must be truncated or split.[^hf-bert]
- **Mismatched preprocessing:** the tokenizer, casing, and special tokens must match the checkpoint.
- **Padding leaks:** pooling or scoring code that ignores the attention mask produces batch-dependent outputs.
- **Not generative:** encoder-only models are not trained for left-to-right generation, although additional architecture or training can change their use.

## Exercise

For 1,000 candidate documents of 128 tokens each and a 16-token query, count how many document encodings a bi-encoder can reuse and how many joint pairs a cross-encoder must process. Explain the quality–latency trade-off without assuming either approach always wins.

> [!example]- Exercise solution
> **Bi-encoder.** All 1,000 document vectors are computed offline and reused for every query. At request time the model encodes one 16-token query, then computes 1,000 dot products, or far fewer with an approximate index.
>
> **Cross-encoder.** Nothing can be precomputed, because each input contains the query. The model runs 1,000 forward passes of about $16 + 128 = 144$ tokens, roughly 144,000 tokens in total, compared with 16 for the bi-encoder.
>
> **Trade-off.** The cross-encoder lets query and document tokens attend to each other, which can capture exact phrase matches and negations that a single vector may blur. Whether that improves ranking must be measured on your judgments, and its cost usually limits it to a short candidate list. See [[Latency vs Throughput]].

## References & Useful Links

[^hf-arch]: [Hugging Face LLM Course — Transformer architectures](https://huggingface.co/learn/llm-course/en/chapter1/6) — Encoder, decoder, and encoder–decoder roles.
[^hf-bert]: [Hugging Face Transformers — BERT](https://huggingface.co/docs/transformers/model_doc/bert) — Output shapes, attention masks, and maximum positions.
[^bert]: [Devlin et al. (2019), BERT](https://arxiv.org/html/1810.04805v2) — Masked-token and next-sentence pretraining.
[^roberta]: [Liu et al. (2019), RoBERTa](https://arxiv.org/abs/1907.11692) — Dynamic masking and removal of next-sentence prediction.
[^sbert-ce]: [Sentence Transformers — cross-encoders](https://sbert.net/examples/cross_encoder/applications/README.html) — Joint scoring versus separate embeddings.
