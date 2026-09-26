---
note_type: concept
search_stage: retrieval
---

# Approximate Nearest Neighbours

#search-eng

## Purpose

Nearest-neighbour retrieval finds vectors close to a query under a specified distance or similarity. Approximate nearest-neighbour (ANN) indexes trade exactness for useful speed, memory, or scale. Approximation quality and semantic relevance are separate: even exact nearest vectors may be irrelevant to the user.

## Main Families

- **Flat scan:** compare all vectors; useful as an exact baseline for a fixed representation and metric.
- **Inverted file (IVF):** partition vector space and search selected partitions; searching more partitions usually increases work and coverage.
- **HNSW:** navigate a hierarchy of proximity graphs; graph construction and search breadth influence recall, memory, and latency.
- **Product quantisation (PQ):** represent subvectors with compact codes, reducing storage while introducing distance approximation.

These techniques can be combined. An IVF vector index is not the same data structure as a term-based [[Inverted Index]]. Match the index metric to model training. Unit-normalised nonzero vectors allow cosine ranking via inner product; unnormalised dot product also reflects magnitude.

## Evaluate the Index Separately

For a fixed query, let $E_k$ be its exact top-k vector neighbours and $A_k$ the approximate output:

$$
\mathrm{ANN\ recall@k}=\frac{|E_k\cap A_k|}{k}
$$

This measures recovery of vector neighbours, not judged relevant documents. Define ties consistently. The example below compares the two targets.

Sweep search effort and report recall, latency tails, memory, build/update cost, and query slices. Filters can reduce available candidates; test the actual filtered workload (see [[Filtered Vector Search]]). See [[Embeddings]], [[Cosine Similarity]], [[Search Evaluation]], and [[Index Updates]].

## Build a Fair Exact Baseline

Use the same **vectors, metric, corpus snapshot, filters, and identity unit** on both sides. Exact search over unfiltered items is the wrong reference for a filtered request.

When fewer than $k$ eligible items exist:

- **$0<m<k$:** the exact set contains $m$ items; divide overlap by $m$.
- **$m=0$:** report an explicit no-eligible-items outcome.

### Neighbour Recall versus Relevance Recall

Consider this example at $k=4$:

| Set | Items |
| --- | --- |
| Exact top four | A, B, C, D |
| ANN top four | A, C, E, F |
| Judged relevant in the evaluation universe | A, C, E |

- **Neighbour recall:** ANN recovers A and C from the exact set, so ANN recall@4 is $2/4=0.5$.
- **Relevance recall:** ANN retrieves all three judged relevant items ($3/3$); the exact top four retrieves two ($2/3$).

Vector proximity and judged relevance are different targets. Recovering more judged relevant items here does not make ANN a better implementation of exact neighbour search. Evaluate each target explicitly.

## Tune One Tradeoff at a Time

Start with a flat exact scan on a representative sample. Hold the embeddings fixed while sweeping index search effort. Record recall and latency by query slice, plus memory and build/update cost. An average can hide failures on selective filters or unusual vector regions.

Graph breadth, the number of IVF lists probed, and quantisation precision control different sources of approximation.[^index] Raising query effort cannot recover information lost through an incompatible embedding model. Rebuilding with more graph connectivity also differs from widening a search on the existing graph. Record build parameters separately from request parameters so the comparison is reproducible.

## Exercise

Hold embeddings and corpus fixed, then change only index search effort. Identify which measured changes concern approximation and which require relevance judgments.

## References & Useful Links

- [HNSW paper](https://arxiv.org/abs/1603.09320) — Hierarchical graph-search design.

[^index]: [Faiss index methods](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes) — Exact, graph, partitioned, and quantised index families; construction and search tradeoffs.
