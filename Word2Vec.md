# Word2Vec

#search-eng

## Overview

Word2Vec learns word embeddings from nearby words in a corpus. Its two main training architectures are **continuous bag of words (CBOW)** and **skip-gram**. The learned vectors can be compared with [[Cosine Similarity]]. [^1]

## What Each Model Predicts

- **CBOW:** Combine context-word vectors to predict the centre word. The bag representation does not preserve context order.
- **Skip-gram:** Use the centre word to predict nearby context words.

An embedding lookup selects a vector by word ID; an implementation need not construct a large one-hot vector. Output training can use efficient alternatives to a full-vocabulary softmax. [^1]

## Corrected Window Example

For `The cat sat on the mat`, choose `cat` and a fixed window of two tokens on each side. Its available context is `[The, sat, on]`: there is only one token to its left. The later `the` and `mat` fall outside that window.

CBOW predicts `cat` from these context tokens. Skip-gram forms the pairs `(cat, The)`, `(cat, sat)`, and `(cat, on)`.

## Tradeoffs

CBOW and skip-gram differ in training cost and learned representations. Neither has a universal guarantee of better syntax, semantics, or rare-word performance; corpus, objective, and hyperparameters matter. Standard word embeddings assign one vector to a word type, unlike context-dependent representations. [^1]

## Search Connection

Word similarity can suggest related vocabulary but does not establish query relevance. Evaluate any expansion against [[Judgement List|judgments]]: related words can be substitutes, complements, or different intents. See [[Embeddings]] for sentence/document retrieval.

## References & Useful Links

[^1]: [Mikolov et al.: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) — Original CBOW and skip-gram architectures and experiments.
- [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) — Original saved visual tutorial, retained for intuition.
