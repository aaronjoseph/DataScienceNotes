---
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
---

A language model assigns probabilities to sequences of tokens, or predicts missing tokens from their context. Tokens may be words, subwords, or bytes, so "predict the next word" is only an approximate description. The same idea underlies autocomplete, spelling correction, speech recognition, and modern large language models (LLMs).

## Three Training Objectives

| Objective | What is predicted | Context used | Example |
|---|---|---|---|
| Causal (autoregressive) | The next token | Tokens to the left | GPT-style [[Decoder-Only Model (Transformers)\|decoder]] |
| Masked | Hidden tokens | Tokens on both sides | [[BERT]], [[RoBERTa]] |
| Sequence-to-sequence | Output tokens | The full input plus earlier output | [[Encoder-Decoder Model (Transformers)\|Encoder–decoder]] |

An autoregressive model factorises a sequence with the chain rule:

$$
P(x_1,\ldots,x_T)=\prod_{t=1}^{T}P(x_t\mid x_{<t})
$$

A masked model such as [[BERT]] predicts selected hidden tokens from surrounding context. Its masked-token objective is not the same as left-to-right sequence likelihood, so it does not directly give $P(x_1, \ldots, x_T)$.

## From Counts to Neural Models

- **[[N-Gram Model|N-gram models]]** estimate $P(x_t \mid x_{t-n+1}, \ldots, x_{t-1})$ from counts of short [[N-Grams|word sequences]]. They are fast and transparent but see only a short, fixed window and need smoothing for unseen sequences.
- **Recurrent models** such as [[RNN|RNNs]] and [[LSTM|LSTMs]] summarise the whole prefix in a hidden state, but process tokens sequentially.
- **[[Transformers]]** attend over the whole context window in parallel during training and are the basis of current large models.

## Evaluate the Right Quantity

Average negative log-likelihood (NLL) measures how much probability a model assigns to held-out tokens:

$$
\text{NLL} = -\frac{1}{T}\sum_{t=1}^{T}\log p_t
$$

Here $p_t$ is the probability the model gave to the token that actually occurred. With natural logarithms, perplexity is:

$$
\text{PPL} = \exp(\text{NLL})
$$

Perplexity can be read as an "effective number of equally likely choices" per token. It is the exponential of the average [[Cross Entropy Loss|cross-entropy]] loss used in training.

Compare perplexity only with compatible tokenisation and evaluation procedures; it is not a direct relevance or factuality score.

## Worked Example

### Example 1: two tokens with probability 0.5

**Step 1 — sequence probability**

$$
0.5 \times 0.5 = 0.25
$$

**Step 2 — average loss**

$$
-\frac{\log 0.5 + \log 0.5}{2} = \log 2 \approx 0.6931
$$

**Step 3 — perplexity**

$$
\exp(\log 2) = 2
$$

The model is as uncertain as a fair choice between two tokens at each position.

### Example 2: three tokens with different probabilities

Inputs: the model assigns $0.4$, $0.25$, and $0.1$ to the three tokens that occurred.

**Step 1 — average loss**

$$
-\frac{\log 0.4 + \log 0.25 + \log 0.1}{3} \approx 1.5351
$$

**Step 2 — perplexity**

$$
\exp(1.5351) \approx 4.64
$$

The one poorly predicted token, with probability 0.1, pulls perplexity up sharply because the logarithm penalises low probabilities heavily.

These numbers do not show whether a generated answer satisfies a search user's need.

## Prompting and In-Context Learning

A large enough causal model can perform a task described in its input. GPT-3 was evaluated by placing instructions and a few examples in the prompt, with no gradient updates or fine-tuning, and performed strongly on many benchmarks while still struggling on others.[^gpt3] This makes the prompt part of the system's specification, so treat prompt changes like code changes and re-evaluate after each one.

## Limitations

- **Plausible is not true:** training rewards probable text. A fluent answer can still be unsupported; see [[Retrieval-Augmented Generation]] for grounding.
- **Tokenisation dependence:** the same text split differently gives different per-token perplexities.
- **Domain shift:** a model with low perplexity on web text may still predict product titles or queries poorly.

## Exercise

Connect [[Tokenization]], [[Cross Entropy Loss]], and [[Search Evaluation]]. Explain why changing tokenisation can change perplexity even on identical text.

> [!example]- Exercise solution
> Perplexity averages over **tokens**, not over characters or words. If a new tokenizer splits the same sentence into more, shorter pieces, the total probability is spread over more predictions, and many of those pieces become easy to predict. The average per-token loss and therefore perplexity change even though the text is the same.
>
> To compare models with different tokenizers, normalise by a shared unit, such as characters, words, or bytes, or compare on a downstream task. Neither perplexity nor these normalised scores measure relevance, which needs judgments as in [[Search Evaluation]].

## References & Useful Links

- [Hugging Face — Causal language modelling](https://huggingface.co/docs/transformers/tasks/language_modeling) — Primary reference for the causal-modelling explanation.

[^gpt3]: [Brown et al. (2020), Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — In-context learning without gradient updates and its limitations.
