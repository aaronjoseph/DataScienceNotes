# Cross-Encoder

#search-eng

## Overview

A cross-encoder scores relevance by passing the query and one candidate **together** through a transformer and producing a single score. Attention can compare every query token with every document token, so it is usually more accurate than a [[Dense Retrieval|bi-encoder]]. The cost is that nothing can be precomputed per document: every query–candidate pair needs its own forward pass. Cross-encoders are therefore used to **rerank** a small candidate set, not to search a whole catalogue.[^1]

## Mechanics

- **Input:** `[CLS] query [SEP] candidate text [SEP]`, truncated to the model's maximum length.
- **Output:** one relevance score or class distribution per pair.
- **Training:** pointwise labels (relevant or not, or graded), or pairwise and listwise objectives; see [[Learning to Rank]].

Nogueira and Cho re-implemented BERT for query-based passage reranking. They reported state-of-the-art TREC-CAR results and the top MS MARCO passage-ranking leaderboard entry at the time, a 27% relative improvement in MRR@10 over the previous best.[^2] See [[BERT]] and [[Encoder-Only Model (Transformers)]].

## Cost Arithmetic

For $N$ candidates, a cross-encoder performs $N$ joint forward passes per query. A bi-encoder performs one query encoding and an index lookup, reusing precomputed document vectors.

Illustrative: 200 candidates at 5 ms each is 1 s of sequential compute. Batching on an accelerator can cut wall-clock time, but not total compute. This is why reranking depth is a quality–latency–cost decision; see [[Latency vs Throughput]].

## In Product Search

- **ESCI baseline.** The Shopping Queries Dataset baseline fine-tuned an MS MARCO cross-encoder on query and product title. It reached nDCG ≈ 0.85 on the public test, compared with about 0.56 for a default-configuration BM25. The authors state this comparison is not fair: BM25 used defaults and handled Japanese poorly.[^3] See [[ESCI]].
- **Managed rerankers.** Cloud ranking APIs expose pretrained query–text relevance models for reranking retrieved candidates.[^4]
- **Caching.** Scores can be cached when the key includes query, item ID, item text version, and model version.
- **Relevance classes.** A classifier head can output ESCI-style classes rather than one score, supporting filtering and presentation decisions.
- **Distillation.** Cross-encoders can teach first-stage models. SPLADE v2 used a cross-encoder reranker to generate training scores for its distilled model.[^5]

## Limitations and Pitfalls

- **Cannot fix recall.** It only reorders what [[Candidate Generation]] supplies.
- **Truncation.** Long product text loses fields beyond the length limit. Choose input fields deliberately (for example, title plus key attributes).
- **Calibration.** Raw scores may not be comparable across queries; thresholding needs validation. See [[Score Normalization]].
- **Latency tails.** Remote reranking calls add a dependency on the critical path; define a timeout and a fallback order. See [[Tail Latency]].
- **Domain shift.** A model trained on web passages may misjudge product attributes such as size or compatibility.

## Exercise

Your latency budget allows 40 ms for reranking and one batched call costs 8 ms plus 0.15 ms per candidate. What is the maximum reranking depth? What recall would you want to measure before choosing that depth?

## References & Useful Links

[^1]: [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — Why cross-encoders are more accurate but too slow for full-collection scoring.
[^2]: [Nogueira and Cho, "Passage Re-ranking with BERT", 2019](https://arxiv.org/abs/1901.04085) — BERT reranker results on TREC-CAR and MS MARCO.
[^3]: [Reddy et al., "Shopping Queries Dataset", 2022](https://arxiv.org/html/2206.06588v1) — Cross-encoder and BM25 baselines for query–product ranking, with the authors' fairness caveat.
[^4]: [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Reranking after retrieval, with a pretrained Ranking API or custom LTR. Accessed 23 September 2026.
[^5]: [Formal et al., "SPLADE v2", 2021](https://arxiv.org/abs/2109.10086) — Distillation from a cross-encoder reranker.
