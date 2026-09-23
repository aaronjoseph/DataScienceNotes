# Candidate Generation

#search-eng

## Overview

Candidate generation, also called **recall** or **first-stage retrieval**, selects a manageable pool of items from the full catalogue for later, more expensive ranking.[^1] Its goal is coverage, not final order: a relevant item missing from the pool cannot be recovered by any reranker.[^2]

A production system often runs several retrieval **channels** and merges them. This note covers channel design, merging, and measurement. [[Hybrid Retrieval]] covers score and rank fusion in more detail.

## Designing Channels

Describe each channel on independent axes rather than by a single name:

- **Representation:** [[Dense Retrieval|dense]], [[SPLADE|learned sparse]], or lexical such as [[BM25]].
- **Filter scope:** full request filters, including NER-derived ones, or base eligibility only.
- **Specialisation:** featured items, availability at a location, normally excluded conditions, a specific store.
- **Depth:** the channel's own top-K.

An illustrative set for product search:

| Channel | Representation | Filter scope | Purpose |
|---|---|---|---|
| Filtered dense | Dense | Full | Main semantic channel |
| Filtered sparse | Sparse | Full | Term matching and expansion |
| Unfiltered dense / sparse | Both | Base eligibility; predicted types denied | Hedge against wrong NER filters |
| Featured | Dense | Full + featured flag | Merchandising candidates |
| Available | Dense | Full + location availability | Fulfilment-constrained results |
| Excluded conditions | Dense | Only normally excluded conditions | Surface refurbished items separately |

"Unfiltered" is a filter-scope label, not "no filters". Keep base eligibility everywhere; see [[Filtered Vector Search]].

## Merging

1. **Fan out concurrently.** Independent channels can run in parallel; request latency then depends on the slowest channel. See [[Tail Latency]].
2. **Concatenate in plan order.** Use a fixed priority order, not completion order.
3. **Deduplicate by stable identity, first seen wins.** The surviving record's channel label is its highest-priority source. Keep all sources if later features need them.
4. **Expand and re-check.** Expand parents to variants and re-apply filters, then drop items that became ineligible.

Rank fusion such as RRF is an alternative to priority concatenation when channels should contribute by rank; see [[Hybrid Retrieval]].

## Worked Example

Judged relevant set $R=\{A,B,C,D,E\}$. Channel outputs, in priority order:

- Filtered dense: `[A, F, B]`
- Filtered sparse: `[B, G, C]`
- Unfiltered dense: `[H, A, D]`

Merged with first-seen deduplication: `A(fd), F(fd), B(fd), G(fs), C(fs), H(ud), D(ud)`.

- Union recall $=|\{A,B,C,D\}|/5=0.8$. E is unrecoverable downstream.
- Each channel alone has recall $2/5=0.4$.
- **Marginal contribution:** removing filtered sparse loses C (recall 0.6); removing unfiltered dense loses D (recall 0.6); removing filtered dense loses no relevant item, because A and B appear elsewhere.

Standalone recall and marginal contribution answer different questions. A channel can look weak alone and still be the only source of certain relevant items.

## Measurement

- Union recall@K and per-channel marginal recall against a [[Judgement List]].
- Candidate-count distribution and zero-candidate rate per channel and per intent.
- Per-channel latency and error or timeout rates.
- [[Approximate Nearest Neighbours|ANN recall]] separately from relevance recall.
- Downstream: how many candidates survive reranker filtering and business rules.

Report these separately from final [[NDCG]]; see [[Search Evaluation]].

## Limitations and Pitfalls

- **Depth coupling.** Tying a channel's K to the caller's page size silently changes recall when the page size changes.
- **Non-deterministic merge.** Merging in completion order makes results depend on network timing.
- **Wrong deduplication key.** Deduplicating by variant instead of parent, or the reverse, changes what the ranker sees.
- **Filter drift.** Channels built by separate code can disagree on base exclusions. Centralise their construction.
- **Cost.** Each channel adds index load and latency tail risk; remove channels with no measured marginal value.

## Exercise

Add a fourth channel returning `[E, F, G]`. Recompute union recall and every channel's marginal contribution. Then state what the reranker must now handle that it did not before.

## References & Useful Links

[^1]: [Formal et al., "SPLADE v2", 2021](https://arxiv.org/abs/2109.10086) — Describes first-stage retrieval, or candidate generation, in two-stage ranking pipelines.
[^2]: [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — A retrieval stage produces candidates that a cross-encoder reranks.

- [Huang et al., "Embedding-based Retrieval in Facebook Search", KDD 2020](https://arxiv.org/abs/2006.11632) — Serving embedding retrieval alongside term-based retrieval in a production system. Abstract read.
