# GloVe

#search-eng

## Core Idea

GloVe learns static word vectors from corpus-wide co-occurrence counts collected within context windows. It connects local context observations to a global count matrix. [[Word2Vec]] also learns from a corpus; “global versus local” does not mean only one method sees the whole dataset.

## Objective

Let $X_{ij}$ count word j in word i's context. GloVe fits word vectors $w_i$, context vectors $\tilde w_j$, and biases:

$$J=\sum_{i,j:X_{ij}>0} f(X_{ij})\left(w_i^T\tilde w_j+b_i+\tilde b_j-\log X_{ij}\right)^2.$$

The weighting function increases with count up to a cap, limiting the influence of very frequent pairs while reducing unreliable rare-pair contributions. Word and context vectors are separate parameter sets.

## Interpretation and Limits

The analogy `king - man + woman ≈ queen` illustrates possible vector relationships, not a guaranteed identity or unbiased understanding. Static vectors assign one representation per vocabulary entry, so different senses of a word share it. Vocabulary coverage, corpus choice, and evaluation task matter. Updating vectors is an engineering/training choice, not mathematically impossible; no universal speed or quality advantage over Word2Vec follows.

## Search Exercise

Explain what a single vector for “bank” loses in river-related versus finance-related queries. Compare with contextual [[Embeddings]] from [[Transformers]]. Test a downstream retrieval metric instead of assuming analogy accuracy predicts search quality.

## References & Useful Links

- [GloVe paper](https://aclanthology.org/D14-1162.pdf) — Objective, weighting, and experiments.
