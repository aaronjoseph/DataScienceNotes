# Encoder-Only Model (Transformers)

#search-eng

## Core Idea

An encoder-style [[Transformers|Transformer]] commonly lets each token attend to tokens on both sides. Models such as [[BERT]] learn contextual representations, often through masked-token training. Encoder-only models **can produce embeddings**; their suitability depends on training and how token representations are pooled.

## Search Uses

- **Bi-encoder:** encode query and document separately; index document vectors for [[Approximate Nearest Neighbours]]. This supports reusable document representations.
- **Cross-encoder:** process query and candidate jointly to predict relevance; useful for reranking a smaller candidate set in [[Search Ranking]]. Joint interaction costs more per query–document pair.

A generic pooled pretrained vector is not automatically a good sentence-retrieval embedding. Check the task objective, pooling, normalisation, and evaluation data. Standard encoder-only models are not inherently autoregressive text generators; additional architecture or training can change their use.

## Exercise

For 1,000 candidates, count how many document encodings a bi-encoder can reuse and how many joint pairs a cross-encoder must process. Explain the quality–latency tradeoff without assuming either approach always wins.

## References & Useful Links

- [Hugging Face Transformer architectures](https://huggingface.co/learn/llm-course/en/chapter1/6) — Encoder and decoder roles.
- [Sentence Transformers cross-encoders](https://sbert.net/examples/cross_encoder/applications/README.html) — Joint scoring versus separate embeddings.
