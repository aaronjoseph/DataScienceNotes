---
aliases: ["Bag of Words (BOW)"]
note_type: concept
search_stage: foundations
tags:
  - "search-eng"
  - "ds-foundations"
---

## Overview

Bag of words represents a document by how often each vocabulary term occurs in it, or simply whether it occurs. Word order, grammar, and position are discarded: the document is treated as an unordered "bag" (multiset) of tokens. The vocabulary and the [[Tokenization|analysis policy]] (casing, token pattern, stopwords) define the vector's dimensions.[^1]

It is one of the simplest ways to turn text into numbers for classification, clustering, or lexical retrieval, and it is the starting point for [[TF-IDF]] and [[BM25]].

## Building the Representation

1. **Analyse** each document into tokens, for example lowercase and split on word boundaries.
2. **Build a vocabulary** $V = (t_1, \ldots, t_p)$ from the permitted documents, fixing an order for the terms.
3. **Count** each vocabulary term in each document.

For $N$ documents, the result is a document–term matrix $X \in \mathbb{R}^{N \times p}$ with entries

$$
X_{ij} = \operatorname{count}(t_j, d_i).
$$

A binary variant replaces each entry with the indicator $\mathbf{1}[X_{ij} > 0]$.

The column order is part of the representation. Vectors built from independently created vocabularies can silently compare different words even when their shapes match.

## Worked Example

Use three sentences and a case-normalised teaching vocabulary ordered as `[i, love, data, science, is, fun, learning]`:

| Document | Count vector |
|---|---|
| D1: I love data science. | `[1,1,1,1,0,0,0]` |
| D2: Data science is fun. | `[0,0,1,1,1,1,0]` |
| D3: I love learning data. | `[1,1,1,0,0,0,1]` |

This vocabulary was chosen by hand. A library's defaults can produce a different one, as the Python example below shows.

### Score the documents for a query

**Input:** the query `data science` under the same vocabulary is

$$
q = (0, 0, 1, 1, 0, 0, 0).
$$

A simple lexical score is the dot product $q \cdot d$, which adds the counts of the query terms in each document.

**Step 1: D1** contains `data` once and `science` once.

$$
q \cdot d_1 = 1 + 1 = 2
$$

**Step 2: D2** also contains both terms once.

$$
q \cdot d_2 = 1 + 1 = 2
$$

**Step 3: D3** contains `data` but not `science`.

$$
q \cdot d_3 = 1 + 0 = 1
$$

**Step 4: a spammy document** repeating `data` ten times alongside `science` once.

$$
q \cdot d_{\text{spam}} = 10 + 1 = 11
$$

D1 and D2 tie because the representation sees the same query-term evidence in both. The spammy document wins by repetition alone, without being more useful. [[TF-IDF]] reweights terms by rarity, and [[BM25]] also saturates the benefit of repeated terms. Neither restores the word order that bag of words discarded.

## Python Example

The following sketch uses scikit-learn's `CountVectorizer`. It was **not executed** because scikit-learn is not installed locally. The expected output was derived from the documented defaults (`lowercase=True` and a token pattern that keeps tokens of two or more word characters) with a small regular-expression reimplementation.[^1]

```python
from sklearn.feature_extraction.text import CountVectorizer

docs = ["I love data science.", "Data science is fun.", "I love learning data."]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)  # sparse matrix

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

Expected output:

```text
['data' 'fun' 'is' 'learning' 'love' 'science']
[[1 0 0 0 1 1]
 [1 1 1 0 0 1]
 [1 0 0 1 1 0]]
```

The default token pattern drops the single-character word `I`, and the columns are ordered alphabetically, so these vectors differ from the hand-built table. Neither is wrong; the analysis policy must simply be the same wherever the vectors are compared.

## Vocabulary and Sparsity

A document typically uses only a small fraction of the collection vocabulary, so a sparse matrix stores only the non-zero entries.[^1] A million possible terms does not mean every document stores a million numbers. Vocabulary construction still needs a policy for rare terms (`min_df`), very common terms (`max_df` or [[Stopwords|stopword]] lists), unseen terms at prediction time, punctuation, and casing.

For a supervised experiment, fit the vocabulary within the permitted training data only; see [[Data Leakage]]. For a search index, collection-wide term statistics may be legitimate because the indexed collection is available at retrieval time. State which setting you are evaluating: the data boundary determines whether a preprocessing step leaks information.

## Strengths and Limitations

- **Simple and interpretable.** Each dimension is a named term, so weights and matches can be inspected.
- **Order is lost.** "dog bites man" and "man bites dog" have identical vectors. [[N-Grams]] keep some local order.
- **No notion of meaning.** `car` and `automobile` are unrelated dimensions. Learned [[Embeddings]] address similarity between words.
- **Raw counts favour long and repetitive documents**, as Step 4 shows; weighting and length normalisation address this.
- **High-dimensional but sparse.** Memory is manageable with sparse storage, but models must cope with many rarely seen features.

These alternatives address different weaknesses; none is a strict upgrade on every task.

## Practice

Write two sentences with identical word counts but different meanings. Identify what additional representation would distinguish them.

> [!example]- Exercise solution
> "The movie was not good, it was bad" and "The movie was not bad, it was good" contain the same words with the same counts, so their bag-of-words vectors are identical. Word bigrams distinguish them: the first contains `not good` and `was bad`, the second `not bad` and `was good`. A sequence model or contextual embedding also captures the order.

## Related Notes

- [[Inverted Index]] — How term counts are stored for retrieval.
- [[NLP Basic Terminology]] — Tokens, vocabulary, and representations.

## References & Useful Links

[^1]: [scikit-learn `CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) — Vocabulary construction, `lowercase` and `token_pattern` defaults, `binary`, `min_df`/`max_df`, and sparse output.
