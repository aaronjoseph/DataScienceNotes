# Hybrid Retrieval

#search-eng

## Purpose

Hybrid retrieval combines complementary candidate sources, often lexical [[BM25]] and dense [[Embeddings]]. It can recover exact identifiers and paraphrases, but improvement must be measured on a fixed [[Judgement List]]. More sources also add cost and failure modes.

## Reciprocal Rank Fusion

Raw BM25 and vector scores have different meanings and scales. Reciprocal rank fusion (RRF) combines ranks instead:

$$\mathrm{RRF}(d)=\sum_{s:d\in L_s}\frac{1}{c+\operatorname{rank}_s(d)}.$$

Ranks start at one; $c>0$ dampens top-rank differences. An absent document contributes zero from that list. Candidate-window size controls what can enter the sum; it is distinct from the final requested result count.

For lists `[A,B,C]` and `[B,D,A]`, with illustrative $c=10$:

- A: $1/11+1/13\approx0.1678$.
- B: $1/12+1/11\approx0.1742$.
- C: $1/13\approx0.0769$.
- D: $1/12\approx0.0833$.

The fused order is B, A, D, C. Choosing 10 here makes arithmetic easy; it is not a recommended universal setting.

## Practical Choices

Deduplicate using stable document identity. Apply eligibility consistently across sources, log missing-source fallbacks, and distinguish source candidate limits from reranking depth. Score-based fusion is another option, but requires justified calibration/normalisation and validation; arbitrary addition can let one scale dominate.

## Exercise

Remove A from the second source's candidate window and recalculate. Explain why fusion cannot recover a document absent from every source. Compare union candidate recall before [[Search Ranking|reranking]] quality in [[Search Evaluation]].

## References & Useful Links

- [Elasticsearch RRF](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) — Rank fusion and candidate-window behaviour.
