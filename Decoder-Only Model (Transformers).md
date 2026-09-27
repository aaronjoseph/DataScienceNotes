---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

A decoder-only [[Transformers|Transformer]] is a stack of Transformer layers whose self-attention is **causal**: the token at position $t$ can use earlier tokens but not later ones. It is trained to predict the next token, and it generates text by repeatedly predicting a token, appending it, and predicting again. GPT-style [[Language Model|language models]] and most chat assistants use this design. It supports text continuation, chat, code, and many other sequence tasks; it is not limited to translation.[^hf-arch]

## Causal Masking

For four tokens, the causal mask allows each row to see itself and everything before it:

```text
            the  red  running  shoes
the          ✓    ✗      ✗       ✗
red          ✓    ✓      ✗       ✗
running      ✓    ✓      ✓       ✗
shoes        ✓    ✓      ✓       ✓
```

In the attention formula, every ✗ becomes $-\infty$ before softmax, so those weights are exactly zero.[^aiayn] The [[Transformers#Worked Example with Three Tokens|three-token example]] shows how the mask changes one token's output.

## Training: Next-Token Prediction

A causal language model factorises a sequence as:

$$
P(x_1,\ldots,x_T)=\prod_{t=1}^{T}P(x_t\mid x_{<t})
$$

### Worked example: shifting inputs and targets

For the training text `the red running shoes <eos>`:

| Position | Model sees | Target |
|---:|---|---|
| 1 | `the` | `red` |
| 2 | `the red` | `running` |
| 3 | `the red running` | `shoes` |
| 4 | `the red running shoes` | `<eos>` |

Because of the causal mask, all four predictions come from **one** forward pass over the known text. The loss is the average [[Cross Entropy Loss|cross-entropy]] over the four targets. This is why training is parallel even though generation is sequential.

## From Pretrained Model to Assistant

GPT-3, a 175-billion-parameter autoregressive model, showed that a large enough pretrained decoder can perform many tasks from instructions and a few examples placed in the prompt, with no gradient updates or fine-tuning.[^gpt3] This is called **in-context learning**. The same paper reports tasks where few-shot performance still struggled and methodological issues from training on web data.

Deployed assistants usually add further training stages on top of pretraining. Check each model card for what was done; the architecture alone does not tell you.

## Decoding Strategies

At each step the model outputs a probability for every vocabulary token. A decoding strategy chooses the next token from that distribution.[^hf-gen]

| Strategy | How it chooses | Typical behaviour |
|---|---|---|
| Greedy | Highest-probability token | Deterministic; can repeat itself in long outputs |
| Beam search | Keeps several partial sequences and picks the best overall | Suits input-grounded tasks such as translation |
| Sampling | Draws a token at random from the distribution | More diverse; can drift |
| Top-$k$ sampling | Samples only from the $k$ most likely tokens | Removes the long tail |
| Top-$p$ (nucleus) sampling | Samples from the smallest set whose probability reaches $p$ | Adapts the set size to model confidence[^nucleus] |

### Worked example: temperature

Temperature $T$ divides the logits before [[Softmax Function|softmax]]. For logits $z=[2,\ 1,\ 0]$:

1. $T = 0.5$, which sharpens the distribution:

$$
\operatorname{softmax}(z/0.5) \approx [0.8668,\ 0.1173,\ 0.0159]
$$

2. $T = 1$, which leaves it unchanged:

$$
\operatorname{softmax}(z) \approx [0.6652,\ 0.2447,\ 0.0900]
$$

3. $T = 2$, which flattens it:

$$
\operatorname{softmax}(z/2) \approx [0.5065,\ 0.3072,\ 0.1863]
$$

Lower temperatures make output more predictable. For grounded answers, lower randomness reduces variation, but it does not make an unsupported claim true.

### Worked example: nucleus sampling

Inputs: next-token probabilities $[0.50,\ 0.20,\ 0.15,\ 0.10,\ 0.05]$ and $p = 0.8$.

**Step 1 — cumulative sums:** $0.50,\ 0.70,\ 0.85,\ 0.95,\ 1.00$.

**Step 2 — nucleus:** the first three tokens, because 0.85 is the first cumulative sum to reach 0.8.

**Step 3 — renormalise:**

$$
\frac{[0.50,\ 0.20,\ 0.15]}{0.85} \approx [0.5882,\ 0.2353,\ 0.1765]
$$

The two least likely tokens can no longer be sampled. If the model were more confident, the nucleus would contain fewer tokens.

## Serving and the KV Cache

Generation has two phases with different performance characteristics:

- **Prefill:** process the whole prompt in one parallel pass and produce the first output token.
- **Decode:** generate one token at a time; each step depends on the tokens already generated.

During decoding, the keys and values of earlier tokens do not change, because causal attention never lets them see later tokens. A **key–value (KV) cache** stores them per layer and appends each new token's key and value, so each step computes only the new token's projections.[^hf-cache] This trades memory for avoided computation. Hugging Face notes that caching is for inference only.

| | Without a cache | With a cache |
|---|---|---|
| Work per step | Recompute keys and values for all earlier tokens | Compute only the current token's key and value |
| Attention per step | Grows quadratically with length | Grows linearly with length |
| Memory | No stored state | Grows linearly with length |

### Worked example: KV-cache memory

The cache size per token is:

$$
\text{bytes per token} = 2 \times L \times h_{kv} \times d_{\text{head}} \times b
$$

The factor 2 counts keys and values; $L$ is the number of layers, $h_{kv}$ the number of key–value heads, $d_{\text{head}}$ the head width, and $b$ the bytes per number.

Inputs for an illustrative configuration: $L = 32$, $h_{kv} = 32$, $d_{\text{head}} = 128$, 16-bit values ($b = 2$).

**Step 1 — per token**

$$
2 \times 32 \times 32 \times 128 \times 2 = 524{,}288 \text{ bytes} = 0.5\ \text{MiB}
$$

**Step 2 — one 4,096-token sequence**

$$
4{,}096 \times 0.5\ \text{MiB} = 2\ \text{GiB}
$$

**Step 3 — with 8 key–value heads instead of 32, per token**

$$
2 \times 32 \times 8 \times 128 \times 2 = 131{,}072 \text{ bytes} = 0.125\ \text{MiB}
$$

**Step 4 — the same 4,096-token sequence with 8 key–value heads**

$$
4{,}096 \times 0.125\ \text{MiB} = 0.5\ \text{GiB}
$$

The cache, not only the model weights, limits how many long requests fit on one accelerator. Grouped-query attention uses fewer key–value heads than query heads; its authors report quality close to full multi-head attention with speed comparable to a single key–value head.[^gqa] PagedAttention manages cache memory in blocks to reduce fragmentation; the vLLM authors report 2–4× higher throughput than the systems they compared at similar latency.[^vllm]

Decoder hidden states are representations too, but a useful retrieval embedding still requires a suitable objective and pooling scheme.

## Search Uses

- **Query rewriting:** expand or clarify queries. Keep the original query and evaluate rewrite-induced mistakes in [[Query Understanding]].
- **Answer generation:** answer from retrieved evidence; see [[Retrieval-Augmented Generation]]. Generated claims need supporting evidence, because fluent output alone does not establish correctness.
- **Candidate scoring:** a decoder can be prompted or fine-tuned to judge relevance, at a higher cost per pair than most rankers.

## Limitations & Common Pitfalls

- **Sequential decoding:** output length drives latency; long answers cost more than long prompts.
- **Finite context:** the prompt, retrieved text, and output must fit the model's supported window and the serving memory budget.
- **Sampling randomness:** repeated identical requests can give different outputs unless decoding is deterministic.
- **Unsupported claims:** next-token training rewards plausible text, not verified facts.

## Exercise

Contrast serving one 1,000-token prompt with generating 1,000 new tokens. Explain why the same token count does not imply equal latency. See [[Latency vs Throughput]] and [[Encoder-Only Model (Transformers)|encoder models]].

> [!example]- Exercise solution
> **1,000-token prompt.** Prefill processes all 1,000 prompt tokens in one parallel pass. The accelerator performs large matrix multiplications with good utilisation, so the cost is roughly one big step.
>
> **1,000 generated tokens.** Decoding needs 1,000 sequential steps, because each token depends on the previous one. Each step does little work per token but must read the model weights and the growing KV cache, and every step adds its own overhead.
>
> **Result.** Generation usually dominates latency. For user-facing features, shorter answers and a cap on output tokens often reduce latency more than shortening the prompt.

## References & Useful Links

[^hf-arch]: [Hugging Face LLM Course — Transformer architectures](https://huggingface.co/learn/llm-course/en/chapter1/6) — Role of causal decoders.
[^aiayn]: [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Masking future positions with $-\infty$.
[^gpt3]: [Brown et al. (2020), Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — In-context learning without gradient updates, and its limitations.
[^hf-gen]: [Hugging Face — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — Greedy, sampling, and beam search behaviour.
[^nucleus]: [Holtzman et al. (2019), The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) — Nucleus sampling.
[^hf-cache]: [Hugging Face — How caching works](https://huggingface.co/docs/transformers/cache_explanation) — Per-layer KV cache, its shape, and its effect on per-step cost.
[^gqa]: [Ainslie et al. (2023), GQA](https://arxiv.org/abs/2305.13245) — Grouped-query attention.
[^vllm]: [Kwon et al. (2023), Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — KV-cache memory management and reported throughput gains.
