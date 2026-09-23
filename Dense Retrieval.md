# Dense Retrieval

#search-eng

## Overview

Dense retrieval encodes the query and each document separately into fixed-length real-valued vectors, then retrieves documents whose vectors score highest against the query vector. Because document vectors do not depend on the query, they can be computed offline and indexed for [[Approximate Nearest Neighbours|nearest-neighbour search]].[^1]

Other names for the same architecture include **bi-encoder**, **dual encoder**, **two-tower model**, and **embedding-based retrieval**.[^1][^3][^4] Contrast it with a [[Cross-Encoder]], which reads query and document together and cannot precompute document representations.

## Mechanics

### Similarity

Dense Passage Retrieval (DPR) scores a question $q$ and passage $p$ by an inner product:[^1]

$$\operatorname{sim}(q,p)=E_Q(q)^\top E_P(p).$$

The similarity must be **decomposable** so that the passage side can be precomputed. For unit-length vectors, inner product and [[Cosine Similarity]] give the same ranking.[^1]

### Training with negatives

Each training instance has a query, one positive passage, and $n$ negatives. DPR minimises the negative log-likelihood of the positive:[^1]

$$L=-\log\frac{e^{\operatorname{sim}(q,p^+)}}{e^{\operatorname{sim}(q,p^+)}+\sum_{j=1}^{n}e^{\operatorname{sim}(q,p_j^-)}}.$$

This is a [[Softmax Function|softmax]] [[Cross Entropy Loss|cross-entropy]] over candidates.

- **In-batch negatives.** For $B$ query–positive pairs in a batch, compute the $B\times B$ score matrix. Each query's positive is on the diagonal; the other $B-1$ passages act as its negatives. This reuses computation.[^1]
- **Hard negatives.** DPR's best reported configuration added one BM25 negative per question: a passage that matches many query tokens but does not contain the answer.[^1]

## Worked Example

One query row of a batch has scores `[2.0, 0.5, 0.1]`; the first is the positive.

- $p^+ = e^{2.0}/(e^{2.0}+e^{0.5}+e^{0.1}) \approx 0.728$, so $L \approx 0.317$.
- Add a hard negative with score 1.9. Now $p^+ \approx 0.439$ and $L \approx 0.823$.

The hard negative produces a much larger loss, so it gives a stronger training signal. Easy random negatives quickly contribute little.

## Strengths and Failure Modes

- **Paraphrase and synonyms.** DPR's example matches "bad guy" with "villain" without shared tokens.[^1]
- **Rare salient strings.** DPR's qualitative analysis shows BM25 winning when a rare phrase is decisive.[^1] Arbitrary SKUs, new product names, and internal codes are out of domain for embedding models.[^2] Combine dense retrieval with lexical or [[SPLADE|learned sparse]] retrieval; see [[Hybrid Retrieval]].
- **Index cost.** On the paper's hardware, building a FAISS index over 21 million passage vectors took 8.5 hours, against about 30 minutes for a Lucene inverted index.[^1] This is a single reported setup, not a general ratio.
- **Scores are not probabilities.** A similarity of 0.8 does not mean the same thing for every query. Avoid global thresholds without calibration.
- **Model coupling.** Query and document vectors must come from compatible encoder versions. A model change usually means re-embedding the corpus; see [[Index Updates]].
- **Constraints are not semantics.** A vector close to "red boots" may be black. Enforce hard constraints with [[Filtered Vector Search|filters]], not similarity.

## Serving Notes

- The query encoder sits on the request path. Cache embeddings by normalised query text and model version, with a time to live.
- Changing embedding dimensionality or model requires a compatible index.
- Measure ANN recall separately from relevance; see [[Approximate Nearest Neighbours]].

## Exercise

For a batch of four queries, write the $4\times4$ score matrix and mark positives and in-batch negatives. Then explain why two queries with the same positive product in one batch would create a false negative.

## References & Useful Links

[^1]: [Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question Answering", EMNLP 2020](https://arxiv.org/abs/2004.04906) — Dual-encoder retrieval, NLL objective, in-batch and BM25 hard negatives, qualitative failure cases, and index-cost measurements.
[^2]: [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Why embeddings miss out-of-domain strings such as SKUs, and combining dense with token-based search. Accessed 23 September 2026.
[^3]: [Huang et al., "Embedding-based Retrieval in Facebook Search", KDD 2020](https://arxiv.org/abs/2006.11632) — Embedding-based retrieval in a production search system. Abstract read.
[^4]: [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — Dense retrieval with a bi-encoder, followed by cross-encoder reranking.
