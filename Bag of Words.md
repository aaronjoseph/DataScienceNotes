---
aliases: ["Bag of Words (BOW)"]
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

## Practice

Write two sentences with identical word counts but different meanings. Identify what additional representation would distinguish them.

## References & Useful Links

[^1]: [Scikit-learn CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) — Vocabulary, counts, token patterns, and sparse output.
