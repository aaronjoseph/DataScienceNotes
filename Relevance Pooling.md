---
note_type: concept
search_stage: evaluation
---

# Relevance Pooling

#search-eng

## Purpose

Relevance pooling builds an annotation set by combining candidate documents from multiple retrieval runs. It makes large-corpus evaluation feasible without judging every query–document pair. Diverse systems can contribute different relevant documents, but the resulting judgments remain incomplete.[^1]

## Suggested Procedure

1. Fix queries, corpus snapshot, and the relevance rubric.
2. Select complementary runs, such as lexical, dense, and hybrid retrieval.
3. Take a stated depth from each run, union by document identity, and deduplicate.
4. Hide contributing-system identity from assessors where practical.
5. Label the pool; keep unjudged documents distinct from grade zero.
6. Version judgments and document evaluation rules for missing labels.

Pooling here selects documents for assessment. [[Hybrid Retrieval|Rank fusion]] instead constructs a served ranking; similar input lists do not make the goals identical.

## Worked Example

Run A contributes `[D1,D2,D3]` and run B contributes `[D2,D4,D5]`.

The pool has five unique documents.

If only D1 and D4 are judged relevant, a new run returning `[D6,D1]` contains one known relevant and one unjudged result.

D6 could be relevant: it cannot truthfully be relabelled irrelevant merely because it was not pooled.

Treating unjudged as nonrelevant is an evaluation convention that must be disclosed.

It can disadvantage a new system that retrieves previously unseen useful documents.

Assess new contributions and recompute all compared systems on the same updated judgments when feasible.[^1]

## Budget for Unique Judgments

For $m$ runs, let $L_{1,k},\ldots,L_{m,k}$ be their top-$k$ sets.

The pool is

$$
P_q=\bigcup_{j=1}^mL_{j,k}.
$$

Its size is at most $mk$, often much smaller because results overlap.

Count unique query–document pairs, not summed run sizes, when estimating annotation effort.

Let $J_q$ be the documents already judged. The fraction of a new run's top-$k$ positions that are judged is

$$
\operatorname{JudgedCoverage@}k=\frac{|L_k\cap J_q|}{k},
$$

assuming $k$ returned items. This reports evaluation coverage, not relevance. State a short-list convention and report relevance metrics separately.

### Extend the original pool fairly

The original pool contains D1 through D5. The new run returns D6 and D1, so only one of its two outputs has a judgment: coverage@2 is 0.5.

If D6 is later judged relevant, add that judgment to a new shared version and recompute every system. A system previously retrieving D6 should benefit too. Keeping old systems on old judgments would mix changes in retrieval with changes in evidence.

## Audit What the Pool Might Miss

Several similar runs may contribute little new material. Include complementary retrieval methods and inspect queries where newly introduced systems have low judged coverage. A small random or targeted audit outside the pool can reveal omissions, but its sampling design must be recorded before using it to estimate broader recall.

Keep the contribution source for diagnostics while hiding it from assessors where practical. Pool membership tells you why a pair was selected for assessment; it should not tell the assessor what label to assign. See [[Active Learning]] for a different goal: selecting examples to improve a model efficiently.

## Exercise

Compare a pool built from three almost-identical lexical runs with one built from lexical and dense runs at the same total annotation budget.

What evidence would show better coverage?

Do not report collection-wide recall if the denominator is only known relevant documents.

See [[Judgement List]], [[Data Labeling]], [[Sampling]], and [[Search Evaluation]].

## References & Useful Links

[^1]: [Assessing relevance in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) — Pooling and incomplete relevance assessment.
