---
note_type: concept
search_stage: ranking
---

# Cross-Encoder

#search-eng

## Overview

A cross-encoder scores relevance by passing the query and one candidate **together** through a transformer and producing a single score. Attention can compare every query token with every document token, which can improve ranking compared with a [[Dense Retrieval|bi-encoder]] when the model and task are well matched. A conventional cross-encoder must jointly score each query–candidate pair at query time. Cross-encoders are therefore used to **rerank** a small candidate set, not to search a whole catalogue.[^1]

## Mechanics

- **Input:** `[CLS] query [SEP] candidate text [SEP]`, truncated to the model's maximum length.
- **Output:** one relevance score or class distribution per pair.
- **Training:** pointwise labels (relevant or not, or graded), or pairwise and listwise objectives; see [[Learning to Rank]].

Nogueira and Cho re-implemented BERT for query-based passage reranking. They reported state-of-the-art TREC-CAR results and the top MS MARCO passage-ranking leaderboard entry at the time, a 27% relative improvement in MRR@10 over the previous best.[^2] See [[BERT]] and [[Encoder-Only Model (Transformers)]].

## Cost Arithmetic

For $N$ candidates, a cross-encoder evaluates $N$ joint query–candidate inputs per query, potentially in batches.

A bi-encoder performs one query encoding and an index lookup, reusing precomputed document vectors.

Illustrative: 200 candidates at 5 ms each is 1 s of sequential compute. Batching can improve utilisation and amortise overhead, while the model still processes all candidate pairs. This is why reranking depth is a quality–latency–cost decision; see [[Latency vs Throughput]].

## In Product Search

- **ESCI baseline.** The Shopping Queries Dataset used a fine-tuned cross-encoder for English and MPNet-based models for Spanish and Japanese. Table 4 reports aggregate nDCG 0.852 for that neural baseline and 0.563 for BM25; the English scores are 0.857 and 0.675 respectively. The authors state this comparison is not fair: BM25 used defaults and handled Japanese poorly.[^3] See [[ESCI]].
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

## Understand What Is and Is Not Precomputed

A conventional cross-encoder computes $s(q,d)=g_\theta([q;d])$ using a joint query–document input.

The document's relevance representation depends on the query, so a single cached document vector cannot reproduce this score for arbitrary queries.

Tokenisation, static fields, and scores for previously seen pairs may still be cached when versions and inputs match.

Batching groups many pairs into one model invocation.

It can improve hardware utilisation and reduce overhead, so $N$ pairs do not necessarily mean $N$ separate API calls or a fixed total runtime.

Sequence lengths, batch size, padding, concurrency, and the accelerator all affect observed cost.

> [!example]- Solve the reranking-depth budget
> **1. Write the timing model.**
>
> $$
> T(N)=8+0.15N\text{ milliseconds}
> $$
>
> **2. Apply the 40 ms budget.**
>
> $$
> 8+0.15N\le40
> $$
>
> **3. Solve for the candidate count.**
>
> $$
> N\le\frac{40-8}{0.15}\approx213.33
> $$
>
> The largest whole-number depth is **213** under this illustrative model.
>
> This leaves no allowance for queueing, network variation, or other work. Treat it as arithmetic under an assumed model, then measure the actual latency distribution. Candidate recall@213 estimates the relevant material available to the model; final NDCG measures how it orders that material.

## Inspect the Pair the Model Actually Sees

For a failed product query, inspect the concatenated fields, truncation boundary, query instruction, and model version. A compatibility requirement hidden beyond the token limit cannot influence the score. Keep score interpretation explicit: a raw logit, sigmoid value, and four-class probability vector require different downstream handling. Evaluate domain quality on a fixed candidate set before assuming a larger model will improve the served page.

## Exercise

Your latency budget allows 40 ms for reranking and one batched call costs 8 ms plus 0.15 ms per candidate.

What is the maximum reranking depth?

What recall would you want to measure before choosing that depth?

## References & Useful Links

[^1]: [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — Why cross-encoders are more accurate but too slow for full-collection scoring.
[^2]: [Nogueira and Cho, "Passage Re-ranking with BERT", 2019](https://arxiv.org/abs/1901.04085) — BERT reranker results on TREC-CAR and MS MARCO.
[^3]: [Reddy et al., "Shopping Queries Dataset", 2022](https://arxiv.org/html/2206.06588v1) — Cross-encoder and BM25 baselines for query–product ranking, with the authors' fairness caveat.
[^4]: [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Reranking after retrieval, with a pretrained Ranking API or custom LTR. Accessed 23 September 2026.
[^5]: [Formal et al., "SPLADE v2", 2021](https://arxiv.org/abs/2109.10086) — Distillation from a cross-encoder reranker.
