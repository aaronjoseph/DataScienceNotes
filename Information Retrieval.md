---
aliases: ["Information Retreival"]
---

# Information Retrieval

#search-eng

## Overview

Information retrieval (IR) finds documents or other items that satisfy an information need. The query is the user's expression of that need; matching its words is useful but is not the same as satisfying the need. Collections can include structured attributes alongside text. [^1]

## A Search Request, Stage by Stage

This is a learning model for product search; implementations vary:

1. **Understand the query:** [[Tokenization]], spelling, and explicit constraints.
2. **Retrieve candidates:** [[Inverted Index]] and [[BM25]] for lexical matches; [[Embeddings]] for semantic matches.
3. **Apply eligibility:** Enforce availability, permissions, or requested filters at the appropriate stages.
4. **Rank candidates:** Order surviving items by usefulness; see [[Search Ranking|Ranking]].
5. **Present results:** Group or deduplicate where the product requires it.
6. **Evaluate:** Use [[Judgement List|relevance judgments]], [[Search Evaluation]], and online experiments.

Example: `red waterproof hiking boots size 9` contains a product intent and constraints. A highly similar red sneaker is not necessarily a relevant result. This distinction motivates evaluating actual results rather than accepting a score as proof of relevance.

## Precision and Recall

For binary relevance, precision is the fraction of retrieved items that are relevant; recall is the fraction of all relevant items retrieved. Ranked cutoffs and practical measurement belong in [[Search Evaluation]].

## Common Failure Modes

A ranker cannot promote a document that never reached its candidate set. Diagnose the first stage where an expected result is lost: indexing, analysis, retrieval, eligibility, ranking, or presentation. Treat this as a debugging procedure, not a reason to relax filters blindly.

## Practice

For three real queries, write down the information need, hard constraints, and examples of relevant and irrelevant results before choosing a retrieval algorithm.

## Related Notes

- [[Search Engineering]] — Learning sequence.

![[Inverted Index]]

## References & Useful Links

[^1]: [Introduction to Information Retrieval: Boolean retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html) — IR scope and structured versus unstructured information.
