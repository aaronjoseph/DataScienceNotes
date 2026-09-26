---
note_type: concept
search_stage: foundations
---

# Word2Vec

#search-eng

## Overview

Word2Vec learns word embeddings from nearby words in a corpus. Its two main training architectures are **continuous bag of words (CBOW)** and **skip-gram**. The learned vectors can be compared with [[Cosine Similarity]]. [^1]

## What Each Model Predicts

- **CBOW:** Combine context-word vectors to predict the centre word. The bag representation does not preserve context order.
- **Skip-gram:** Use the centre word to predict nearby context words.

An embedding lookup selects a vector by word ID; an implementation need not construct a large one-hot vector. Output training can use efficient alternatives to a full-vocabulary softmax. [^1]

## Corrected Window Example

For `The cat sat on the mat`, choose `cat` and a fixed window of two tokens on each side.

Its available context is `[The, sat, on]`: there is only one token to its left.

The later `the` and `mat` fall outside that window.

CBOW predicts `cat` from these context tokens. Skip-gram forms the pairs `(cat, The)`, `(cat, sat)`, and `(cat, on)`.

## Tradeoffs

CBOW and skip-gram differ in training cost and learned representations. Neither has a universal guarantee of better syntax, semantics, or rare-word performance; corpus, objective, and hyperparameters matter. Standard word embeddings assign one vector to a word type, unlike context-dependent representations. [^1]

## The Learning Objective

For a centre word $w$ and context word $c$, a full-softmax skip-gram model uses input vector $v_w$ and output vector $u_c$:

$$
P(c\mid w)=\frac{\exp(u_c^\top v_w)}{\sum_{j\in V}\exp(u_j^\top v_w)}.
$$

Training increases the likelihood of observed context pairs. The denominator touches the vocabulary, motivating alternatives such as negative sampling.[^negative] This probability concerns context prediction; it is not the probability that a product is relevant to a search query.

### See what one training pair asks the model to do

In the window example above, `(cat, sat)` is a positive pair. A negative-sampling step might compare it with sampled words such as `charger` and `invoice`. For this illustrative draw, the loss is

$$
\ell=-\log\sigma(u_{sat}^\top v_{cat})-\log\sigma(-u_{charger}^\top v_{cat})-\log\sigma(-u_{invoice}^\top v_{cat}),
$$

Here the sigmoid function is

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

The positive dot product is encouraged upward and sampled negative dot products downward.

The sampled words are noise for this local training task, not universal examples of semantic opposition.

## Why Neighbours Can Be Surprising

Words used in similar contexts can become close even when they are competitors or opposites. A static word vector also combines multiple senses of a word such as `bank`. Query expansion based on nearest words can consequently change intent. Use nearest neighbours as candidates for inspection, then evaluate the expanded query against relevance judgments.

For revision, build the skip-gram pairs for the centre word `sat` with the same fixed two-token window. The available context is `The`, `cat`, `on`, `the`; preserve token occurrences even when two words differ only by case under the unnormalised example.

## Search Connection

Word similarity can suggest related vocabulary but does not establish query relevance. Evaluate any expansion against [[Judgement List|judgments]]: related words can be substitutes, complements, or different intents. See [[Embeddings]] for sentence/document retrieval.

## References & Useful Links

[^1]: [Mikolov et al.: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) — Original CBOW and skip-gram architectures and experiments.
- [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) — Original saved visual tutorial, retained for intuition.

[^negative]: [Mikolov et al., Distributed Representations of Words and Phrases and their Compositionality, 2013](https://arxiv.org/html/1310.4546v1) — Full-softmax skip-gram and negative-sampling objectives.
