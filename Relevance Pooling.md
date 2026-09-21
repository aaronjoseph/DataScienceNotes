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

Run A contributes `[D1,D2,D3]` and run B contributes `[D2,D4,D5]`. The pool has five unique documents. If only D1 and D4 are judged relevant, a new run returning `[D6,D1]` contains one known relevant and one unjudged result. D6 could be relevant: it cannot truthfully be relabelled irrelevant merely because it was not pooled.

Treating unjudged as nonrelevant is an evaluation convention that must be disclosed. It can disadvantage a new system that retrieves previously unseen useful documents. Assess new contributions and recompute all compared systems on the same updated judgments when feasible.[^1]

## Exercise

Compare a pool built from three almost-identical lexical runs with one built from lexical and dense runs at the same total annotation budget. What evidence would show better coverage? Do not report collection-wide recall if the denominator is only known relevant documents.

See [[Judgement List]], [[Data Labeling]], [[Sampling]], and [[Search Evaluation]].

## References & Useful Links

[^1]: [Assessing relevance in information retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) — Pooling and incomplete relevance assessment.
