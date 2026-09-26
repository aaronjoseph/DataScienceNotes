---
aliases: ["Bag of Words (BOW)"]
note_type: concept
search_stage: foundations
---
# Bag of Words

#search-eng

## Overview

Bag of words represents a document by token counts or presence indicators over a vocabulary. The representation discards ordering. The vocabulary and [[Tokenization|analysis policy]] determine the vector's dimensions. [^1]

## Worked Example

Retain the original three sentences, using a case-normalised teaching vocabulary ordered as `[i, love, data, science, is, fun, learning]`:

| Document | Count vector |
|---|---|
| I love data science. | `[1,1,1,1,0,0,0]` |
| Data science is fun. | `[0,0,1,1,1,1,0]` |
| I love learning data. | `[1,1,1,0,0,0,1]` |

This is a manually specified vocabulary, not a claim about a library's default token pattern. For example, a vectorizer can exclude single-character tokens unless configured otherwise. [^1]

## Strengths and Limitations

The method is simple and gives interpretable dimensions. It does not distinguish sentences containing the same words in different orders. Large vocabularies create high-dimensional but often sparse vectors; repeated common words can dominate raw counts. [^1]

[[TF-IDF]] changes weights, [[N-Grams]] retains some local order, and [[Embeddings]] learns another representation. These solve different aspects of the problem.

## From a Vocabulary to a Matrix

Let $V=(t_1,\ldots,t_p)$ be an ordered vocabulary and let the collection contain $N$ documents. The count matrix $X\in\mathbb R^{N\times p}$ has

$$X_{ij}=\operatorname{count}(t_j,d_i).$$

A binary representation replaces each entry with $\mathbf1[X_{ij}>0]$. The column order is part of the representation: comparing vectors from independently built vocabularies can silently compare different words even when the shapes match.

> [!example]- Use the original three sentences as a retrieval problem
> Under the seven-word vocabulary above, the query `data science` is $q=(0,0,1,1,0,0,0)$. Its dot product with the three document vectors is 2, 2, and 1. The first two tie because this representation sees the same query-word evidence in both.
>
> Repeating `data` ten times would raise a raw-count dot product without establishing greater usefulness. [[TF-IDF]] changes term weights, while [[BM25]] limits the benefit of repetition. Neither restores all the word order that bag of words discarded.

## Vocabulary and Sparsity

A document typically uses only a small fraction of the collection vocabulary, so a sparse matrix stores the nonzero entries rather than every zero.[^1] A million possible terms does not mean every document needs a million stored numbers. However, vocabulary construction still needs a policy for rare terms, unseen terms, punctuation, and casing.

For a supervised experiment, fit the vocabulary within the permitted training data. For a search index, collection-wide term statistics may be legitimate because the indexed collection is available at retrieval time. State which setting you are evaluating; the data boundary determines whether a preprocessing step leaks information.

## Practice

Write two sentences with identical word counts but different meanings. Identify what additional representation would distinguish them.

## References & Useful Links

[^1]: [Scikit-learn CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) — Vocabulary, counts, token patterns, and sparse output.
