# Search Evaluation

#search-eng

## Overview

Evaluate whether the system finds and orders useful results, not only whether its scores look plausible. A [[Judgement List]] supplies query–document relevance labels; [[NDCG]] measures graded ranking quality. Offline measurements and [[AB Testing|online experiments]] answer different questions. [^1]

## Choose the Metric for the Question

For binary relevance and a fixed cutoff $k$:

$$Precision@k=\frac{\text{relevant documents in the first }k\text{ positions}}{k}$$

$$Recall@k=\frac{\text{relevant documents in the first }k\text{ positions}}{\text{all relevant documents in the evaluation universe}}$$

Here missing returned positions count as nonrelevant for precision. Incomplete judgments make true collection-wide recall difficult to know; say when reporting recall against known judgments. [^1]

**Reciprocal rank** is $1/r$ for the first relevant result at rank $r$, or 0 if none appears within the evaluated cutoff. Mean reciprocal rank averages this over queries. It focuses on the first success, unlike metrics rewarding multiple useful results.

## Worked Example

Relevant documents are `{A, B, C, D}`; the top three returned are `[B, X, A]`. Precision@3 is $2/3$, recall@3 is $2/4$, and reciprocal rank is 1. A perfect first result does not imply complete retrieval.

## Evaluation Contract

Record these choices before comparing systems:

- Query set, corpus snapshot, query context, and eligibility filters.
- Evaluation unit: passage, document, product, or variant.
- Cutoff, relevance rubric, missing judgments, ties, and duplicate handling.
- Aggregation: equal weight per query or explicitly defined traffic weights.
- Candidate-generation metrics separately from final ranked output.

For an experiment, compare the same queries and inspect per-query changes. Segment examples by exact identifiers, synonyms, rare queries, and hard constraints. These are suggested search-analysis practices, not a universal benchmark protocol.

## Practice

Construct a system that improves reciprocal rank while lowering recall. Explain why a single aggregate metric hides the tradeoff.

## Further Study

- [[Click Bias]] — Interpret observed feedback and exposure.
- [[Approximate Nearest Neighbours]] — Separate vector-index recall from relevance recall.

## Label Quality and Coverage

- [[Probability Calibration]] — Assess probability accuracy separately from ranking.
- [[Relevance Pooling]] — Understand how incomplete judgments affect comparisons.

## References & Useful Links

[^1]: [Evaluating ranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Precision/recall tradeoffs and ranking evaluation.
