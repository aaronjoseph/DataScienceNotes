---
note_type: concept
search_stage: evaluation
---

# Search Evaluation

#search-eng

## Overview

Evaluate whether the system finds and orders useful results, not only whether its scores look plausible. A [[Judgement List]] supplies query–document relevance labels; [[NDCG]] measures graded ranking quality. Offline measurements and [[AB Testing|online experiments]] answer different questions. [^1]

## Choose the Metric for the Question

For binary relevance and a fixed cutoff $k$:

$$
Precision@k=\frac{\text{relevant documents in the first }k\text{ positions}}{k}
$$

$$
Recall@k=\frac{\text{relevant documents in the first }k\text{ positions}}{\text{all relevant documents in the evaluation universe}}
$$

Here missing returned positions count as nonrelevant for precision. Incomplete judgments make true collection-wide recall difficult to know; say when reporting recall against known judgments. [^1]

**Reciprocal rank** is $1/r$ for the first relevant result at rank $r$, or 0 if none appears within the evaluated cutoff.

Mean reciprocal rank averages this over queries.

It focuses on the first success, unlike metrics rewarding multiple useful results.

## Worked Example

**Inputs**

- Relevant documents: `{A, B, C, D}`.
- Top three returned: `[B, X, A]`.

**Precision:** two of the three returned documents are relevant.

$$
Precision@3=\frac{2}{3}
$$

**Recall:** two of the four relevant documents were returned.

$$
Recall@3=\frac{2}{4}
$$

**Reciprocal rank:** the first result is relevant, so reciprocal rank is 1.

A perfect first result does not imply complete retrieval.

## Evaluation Contract

Record these choices before comparing systems:

- Query set, corpus snapshot, query context, and eligibility filters.
- Evaluation unit: passage, document, product, or variant.
- Cutoff, relevance rubric, missing judgments, ties, and duplicate handling.
- Aggregation: equal weight per query or explicitly defined traffic weights.
- Candidate-generation metrics separately from final ranked output.

For an experiment, compare the same queries and inspect per-query changes. Segment examples by exact identifiers, synonyms, rare queries, and hard constraints. These are suggested search-analysis practices, not a universal benchmark protocol.

## Aggregate at the Unit You Intend to Optimise

Let $M_q$ be the metric for query $q$ and $Q$ the evaluation query set.

**Equal-query mean**

$$
\bar M=\frac{1}{|Q|}\sum_{q\in Q}M_q
$$

**Traffic-weighted mean**

Use fixed, documented nonnegative weights:

$$
\bar M_w=\frac{\sum_q w_qM_q}{\sum_qw_q}.
$$

A sum of relevant items divided by a sum of denominators is a different aggregation again. Do not label all three simply “average recall”.

For comparing systems A and B, inspect paired changes $\Delta_q=M_q(B)-M_q(A)$ on the same queries.

Alongside the mean, examine large regressions and the distribution by intent.

The corpus and judgment versions must match so that a difference is attributable to the systems being compared.

### Improve the first hit while losing coverage

There are four relevant items in the judged universe; X, Y, and Z are irrelevant.

At cutoff 4:

| System | Returned list | Reciprocal rank | Recall |
|---|---|---:|---:|
| A | `[X,A,B,C]` | $1/2$ | $3/4$ |
| B | `[A,X,Y,Z]` | $1$ | $1/4$ |

B makes the first success easier but loses useful alternatives. Which result is preferable depends on the task. A lookup task and a comparison-shopping task may need different primary metrics.

## A Compact Evaluation Report

For each run, save the evaluation contract, candidate recall at retrieval depth, final relevance at display cutoff, judgment coverage, query slices, and failed-request treatment. Report latency and online outcomes separately. Count timeouts and empty lists explicitly rather than silently dropping them and evaluating only successful queries. If judgments are incomplete, call the denominator “known relevant items in the judged universe” and keep unjudged outcomes visible.

## Practice

Construct a system that improves reciprocal rank while lowering recall. Explain why a single aggregate metric hides the tradeoff.

## Further Study

- [[Click Bias]] — Interpret observed feedback and exposure.
- [[Approximate Nearest Neighbours]] — Separate vector-index recall from relevance recall.

## References & Useful Links

[^1]: [Evaluating ranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Precision/recall tradeoffs and ranking evaluation.
