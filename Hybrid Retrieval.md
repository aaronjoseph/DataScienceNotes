---
note_type: concept
search_stage: retrieval
---

# Hybrid Retrieval

#search-eng

## Purpose

Hybrid retrieval combines complementary candidate sources, often lexical [[BM25]] and dense [[Embeddings]]. It can recover exact identifiers and paraphrases, but improvement must be measured on a fixed [[Judgement List]]. More sources also add cost and failure modes.

## Reciprocal Rank Fusion

Raw BM25 and vector scores have different meanings and scales. Reciprocal rank fusion (RRF) combines ranks instead:

$$
\mathrm{RRF}(d)=\sum_{s:d\in L_s}\frac{1}{c+\operatorname{rank}_s(d)}.
$$

Ranks start at one; $c>0$ dampens top-rank differences.

An absent document contributes zero from that list.

Candidate-window size controls what can enter the sum; it is distinct from the final requested result count.

For lists `[A,B,C]` and `[B,D,A]`, with illustrative $c=10$:

- A: $1/11+1/13\approx0.1678$.
- B: $1/12+1/11\approx0.1742$.
- C: $1/13\approx0.0769$.
- D: $1/12\approx0.0833$.

The fused order is B, A, D, C. Choosing 10 here makes arithmetic easy; it is not a recommended universal setting.

## Practical Choices

Deduplicate using stable document identity. Apply eligibility consistently across sources, log missing-source fallbacks, and distinguish source candidate limits from reranking depth. Score-based fusion is another option, but requires justified calibration/normalisation and validation; arbitrary addition can let one scale dominate. See [[Candidate Generation]] for channel design and merging, [[Score Normalization]] for score-based combination, and [[SPLADE]] for a learned sparse source.

## Separate Combining Candidates from Combining Evidence

The union of source candidates determines coverage. Fusion then orders that union, and a later [[Cross-Encoder|reranker]] may reorder it again. Record each source's depth, the fusion window, reranking depth, and final display cutoff. Increasing one of these limits does not automatically increase the others.

RRF uses within-source rank, discarding score magnitude. It can combine sources with incompatible scales, but it also discards the distinction between a tiny and a huge score gap. Repeating the same source under several names gives its ranking extra votes; more sources are useful when they add reliable, complementary evidence.

> [!example]- Solve the missing-candidate exercise
> Remove A from the second list in the example while retaining B and D at ranks 1 and 2.
>
> A now receives only $1/11\approx0.0909$.
>
> B remains about 0.1742, D about 0.0833, and C about 0.0769.
>
> The order remains B, A, D, C, but A's margin over D becomes much smaller. If A were absent from both lists, no fusion rule could restore it. This is a candidate-coverage failure, even if the fusion calculation is correct.

## Evaluate the Benefit of Each Source

On a fixed query and judgment set, compare lexical only, dense only, their candidate union, and the fused final ranking. Look at the documents uniquely recovered by each source. Separate ordinary two-source requests from degraded requests where one source timed out, because their candidate universe and score interpretation differ.

Tune source depth and the RRF constant on development judgments; report results once on held-out queries. Tie-breaking should use a documented stable rule so equal fused scores do not produce timing-dependent order.

## Exercise

Remove A from the second source's candidate window and recalculate.

Explain why fusion cannot recover a document absent from every source.

Compare union candidate recall before [[Search Ranking|reranking]] quality in [[Search Evaluation]].

## References & Useful Links

- [Elasticsearch RRF](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) — Rank fusion and candidate-window behaviour.
