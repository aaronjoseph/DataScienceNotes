---
aliases:
  - Learned Sparse Retrieval
---

# SPLADE

#search-eng

## Overview

SPLADE (Sparse Lexical and Expansion model) is a **learned sparse retrieval** model. It maps a query or document to a weight for every term in a transformer vocabulary, most of which are zero. The result keeps useful properties of bag-of-words retrieval, such as exact term matching and [[Inverted Index|inverted-index]] efficiency, while learning **expansion**: a document can receive weight on related terms that it never contains.[^1][^2]

It sits between [[BM25]], which uses fixed weights and exact tokens, and [[Dense Retrieval]], which uses learned but opaque dimensions. Its main target is the vocabulary-mismatch problem: relevant documents that do not share the query's words.[^2]

## Mechanics

SPLADE uses the masked-language-model head of a BERT-style encoder over the WordPiece vocabulary ($|V|=30522$). For input token $i$ and vocabulary term $j$:[^2]

$$w_{ij}=\operatorname{transform}(h_i)^\top E_j+b_j.$$

The original model sums over input tokens with a **log-saturation** effect; SPLADE v2 replaces the sum with max pooling, which the authors report substantially improves effectiveness:[^1][^2]

$$w_j=\sum_{i\in t}\log\bigl(1+\operatorname{ReLU}(w_{ij})\bigr)\quad\text{(SPLADE)},\qquad w_j=\max_{i\in t}\log\bigl(1+\operatorname{ReLU}(w_{ij})\bigr)\quad\text{(SPLADE v2)}.$$

The ReLU makes negative weights zero; the logarithm dampens very large weights. The query–document score is the dot product of the two sparse vectors.

### Keeping it sparse

A **FLOPS regulariser** penalises the squared mean activation of each term across a batch. This pushes the model towards fewer non-zero terms and evenly distributed postings, which relates directly to retrieval cost. Queries and documents use separate regularisation weights, $\lambda_q$ and $\lambda_d$, so query sparsity can be enforced more strongly.[^2]

The **SPLADE-doc** variant expands only documents. The score is the sum of document weights for the query's own terms, so no query encoder runs at search time.[^2]

## Worked Example

Illustrative learned weights:

- Document `waterproof hiking boots`: `{waterproof: 1.8, hiking: 1.5, boots: 1.6, boot: 1.1, trekking: 0.6, shoes: 0.4}`
- Query `trekking boot`: `{trekking: 1.2, boot: 1.4, boots: 0.9, hiking: 0.5}`

Score $=1.2(0.6)+1.4(1.1)+0.9(1.6)+0.5(1.5)=4.45$.

Without stemming, exact-token BM25 finds no shared term: `trekking` and `boot` do not occur in the document. SPLADE matches through learned expansion (`trekking`, `boot`) and query-side expansion (`boots`, `hiking`). The expansion that creates this match can also create false ones.

## Compared with Other Retrievers

| Property | [[BM25]] | SPLADE | [[Dense Retrieval]] |
|---|---|---|---|
| Representation | Sparse, exact analysed tokens | Sparse, learned weights over vocabulary | Dense, learned dimensions |
| Handles vocabulary mismatch | Only through analysis, synonyms | Learned expansion | Semantic similarity |
| Interpretability | High | Terms are inspectable | Low |
| Index | Inverted index | Inverted index or sparse-vector index | ANN index |
| Query-time model | None | Encoder, except SPLADE-doc | Encoder |

## Limitations and Pitfalls

- **Wrong expansions.** Expansion can add competitor brands or related but different product types. Inspect the top expansion terms for important query slices.
- **Identifiers.** WordPiece splits model numbers into fragments; that is not exact identifier matching. Keep an exact-match path for identifiers; see [[Query Intent Classification]].
- **Sparsity tradeoff.** Higher regularisation lowers cost and usually effectiveness. Choose it from measured quality and latency.[^2]
- **"Sparse" is ambiguous.** Managed vector databases may accept any sparse embedding: TF-IDF, BM25, or SPLADE, represented as dimension–value pairs.[^3] Check which one a system actually uses.
- **Score scales differ** from dense similarity, so combine them with rank fusion or justified normalisation; see [[Hybrid Retrieval]] and [[Score Normalization]].

## Exercise

Take one query that fails on BM25 because of vocabulary mismatch. List the expansion terms you would want SPLADE to add and one expansion term that would harm precision. How would you detect that harmful term in evaluation?

## References & Useful Links

[^1]: [Formal, Piwowarski, and Clinchant, "SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking", SIGIR 2021](https://arxiv.org/abs/2107.05720) — Original model: explicit sparsity regularisation and log-saturated term weights.
[^2]: [Formal et al., "SPLADE v2", 2021](https://arxiv.org/abs/2109.10086) — Term-weight formula, FLOPS regularisation, max pooling, SPLADE-doc, distillation, and BEIR results.
[^3]: [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Sparse embeddings from TF-IDF, BM25, or SPLADE in a vector index. Accessed 23 September 2026.
