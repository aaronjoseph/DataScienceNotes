# Encoder-Decoder Model (Transformers)

#search-eng

## Core Idea

An encoder–decoder Transformer maps an input sequence to an output sequence. The encoder represents the input; the decoder generates output using causal self-attention and cross-attention over the encoder's representations.

$$P(y\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x).$$

Here $x$ is the input and $y_t$ is output token t. During training, known earlier target tokens can be supplied (teacher forcing); at inference, generated earlier tokens are used. An end-of-sequence token or a configured limit stops generation.

## Uses and Limits

Translation and summarisation fit this sequence-to-sequence structure. Control/task tokens can influence behaviour when the model was trained to interpret them; arbitrary new tokens do not guarantee control. Output lengths need not match input lengths.

For search, query rewriting can use this structure, but a fluent rewrite can alter an identifier, negation, or constraint. Retain the original query and evaluate intent preservation in [[Query Understanding]].

## Exercise

For an input product query and a generated rewrite, identify which tokens the encoder sees, which the decoder sees during training, and what changes at inference. Compare [[Encoder-Only Model (Transformers)|encoder-only]] and [[Decoder-Only Model (Transformers)|decoder-only]] models.

## References & Useful Links

- [Original Transformer paper](https://arxiv.org/html/1706.03762v7) — Primary reference for the explanation above.
