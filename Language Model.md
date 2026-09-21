# Language Model

#search-eng

## Core Idea

A language model assigns probabilities to language sequences or predicts missing parts from context. Tokens may be subwords, bytes, or words; “predict the next word” is only one description.

An autoregressive model factorises a sequence:

$$P(x_1,\ldots,x_T)=\prod_{t=1}^{T}P(x_t\mid x_{<t}).$$

A masked model such as [[BERT]] predicts selected hidden tokens using surrounding context. Its masked-token objective is not directly the same left-to-right sequence likelihood.

## Evaluate the Right Quantity

Average negative log-likelihood measures how much probability is assigned to held-out tokens. For natural logarithms, perplexity is $\exp(-\frac1T\sum_t\log p_t)$. Compare perplexity only with compatible tokenisation and evaluation procedures; it is not a direct relevance or factuality score.

## Worked Example and Exercise

If two observed tokens each receive probability 0.5, sequence probability is 0.25, average loss is $\log 2$, and perplexity is 2. These numbers do not show whether a generated answer satisfies a search user's need.

Connect [[Tokenization]], [[Cross Entropy Loss]], and [[Search Evaluation]]. Explain why changing tokenisation can change perplexity even on identical text.

## References & Useful Links

- [Causal language modelling](https://huggingface.co/docs/transformers/tasks/language_modeling) — Primary reference for the explanation above.
