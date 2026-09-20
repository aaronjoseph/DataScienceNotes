# Decoder-Only Model (Transformers)

#search-eng

## Core Idea

A decoder-only [[Transformers|Transformer]] typically learns to predict the next token using a causal attention mask. At position t, it can use preceding tokens, not future tokens. This supports text continuation, chat, code, and other sequence tasks; it is not limited to translation.

## Training and Serving

During training, known target sequences allow many positions to be processed in parallel under a causal mask. During ordinary autoregressive generation, each newly sampled token depends on preceding output. Prompt processing (prefill) and incremental decoding therefore have different performance characteristics.

A key–value cache reuses earlier attention projections during decoding, trading memory for avoided computation. Context is finite and constrained by model support and serving resources. Decoder hidden states are representations, but a useful retrieval embedding still requires a suitable objective and pooling scheme.

## Search Uses and Exercise

Query rewriting, answer generation, and candidate scoring can use decoder models. Generated claims need supporting retrieved evidence; fluent output alone does not establish correctness. Keep the original query and evaluate rewrite-induced mistakes in [[Query Understanding]].

Contrast serving one 1,000-token prompt with generating 1,000 new tokens. Explain why the same token count does not imply equal latency. See [[Latency vs Throughput]] and [[Encoder-Only Model (Transformers)|Encoder models]].

## References & Useful Links

- [Hugging Face architecture guide](https://huggingface.co/learn/llm-course/en/chapter1/6) — Causal decoder role.
- [Transformers cache explanation](https://huggingface.co/docs/transformers/cache_explanation) — Autoregressive caching.
