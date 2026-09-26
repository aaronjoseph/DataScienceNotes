---
note_type: concept
search_stage: ranking
---

# Search Ranking

#search-eng

## Overview

Ranking orders candidates for a query. A common architecture retrieves a broad candidate set cheaply, then applies a more expensive scorer to that smaller set. A bi-encoder scores separately encoded vectors; a cross-encoder jointly processes a query and candidate. [^1]

## Separate the Questions

- **Retrieval:** Did the system find the useful documents? Start with [[BM25]] and [[Embeddings]].
- **Ranking:** Were the useful candidates placed near the top? Measure with [[NDCG]].
- **Eligibility:** Is a result allowed under the user's constraints?
- **Presentation:** Are duplicates or variants hiding useful choices?

These distinctions are a debugging framework. A cross-encoder cannot recover documents absent from the candidate set. Its query-document computation can improve ordering but adds work per candidate. [^1]

## An Illustrative Failure

For `waterproof hiking boots`, suppose candidate retrieval returns only trainers. A better ordering of those trainers cannot fix the missing boots. If boots are present at rank 100 and the reranker only receives 50 candidates, the loss occurred before reranking.

## Learning to Rank

A learned ranker uses training signals and features to predict an ordering. Before choosing a model, define query groups, labels, available-at-serving-time features, and the evaluation split. [[Feature Engineering]], [[Judgement List]], and [[Data Leakage]] are prerequisites.

## Practice

For one failed query, record candidate IDs after each stage, the scoring method, and the first point where a known relevant item disappears. Keep raw model scores separate from final business ordering.

## Related Notes

- [[Search Evaluation]] — Candidate coverage versus end-to-end quality.
- [[Latency vs Throughput]] — Candidate count has a serving cost.
- [[SQL/Ranking|SQL ranking functions]] — A different use of the word ranking.

## Further Study

- [[Learning to Rank]] — Objectives, labels, and query groups.
- [[Hybrid Retrieval]] — Combine candidate sources before reranking.
- [[Cross-Encoder]] — Joint query–candidate relevance scoring for reranking.
- [[ESCI]] — Graded product-search relevance classes.
- [[Score Normalization]] — Combining signals and lexicographic business ordering.
- [[Search Architecture]] — Where ranking sits in the full pipeline.

## References & Useful Links

[^1]: [Sentence Transformers: Retrieve and re-rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — Two-stage search and bi-encoder/cross-encoder tradeoffs.
