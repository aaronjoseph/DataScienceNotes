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

$$\mathrm{ANN\ recall@k}=|E_k\cap A_k|/k.$$

If exact neighbours are `{A,B,C,D}` and ANN returns `{A,C,E,F}`, recall@4 is 0.5. This measures recovery of vector neighbours, not judged relevant documents. Define ties consistently.

Sweep search effort and report recall, latency tails, memory, build/update cost, and query slices. Filters can reduce available candidates; test the actual filtered workload (see [[Filtered Vector Search]]). See [[Embeddings]], [[Cosine Similarity]], [[Search Evaluation]], and [[Index Updates]].

## Exercise

Hold embeddings and corpus fixed, then change only index search effort. Identify which measured changes concern approximation and which require relevance judgments.

## References & Useful Links

- [Faiss indexes](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes) — Index families and storage tradeoffs.
- [HNSW paper](https://arxiv.org/abs/1603.09320) — Hierarchical graph-search design.
