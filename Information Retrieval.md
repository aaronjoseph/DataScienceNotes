---
aliases: ["Information Retreival"]
note_type: concept
search_stage: foundations
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

## A Small Mathematical Model

Let $\mathcal D$ be a fixed collection, $q$ a query, and $E(q)\subseteq\mathcal D$ the items eligible under the request's hard constraints.

Retrieval produces candidates $C(q)\subseteq E(q)$; a ranker orders them using a score $s(q,d)$.

A relevance judgment $y(q,d)$ is a separate assessment of usefulness.

A high $s$ can disagree with $y$.

If $R(q)$ is the judged relevant set within the eligible evaluation universe, candidate recall is

$$
\operatorname{Recall}_{C}(q)=\frac{|C(q)\cap R(q)|}{|R(q)|},\qquad |R(q)|>0.
$$

This notation helps localise mistakes.

An indexing error changes what can be found; an incorrect filter changes $E$; a retrieval miss changes $C$; a ranking error changes the order.

State an explicit policy for queries with no known relevant items and for incomplete judgments.

### Trace one result through the pipeline

Suppose D1 is a red hiking boot, D2 a black hiking boot, D3 a red running shoe, and D4 a boot cleaner. For `red hiking boots`, assume colour is mandatory and only D1 is relevant.

A broad lexical channel might retrieve all four. The type and colour filters should retain D1. If D1 disappears before scoring, changing the ranker cannot help. If D1 reaches scoring but D4 is displayed above it, inspect the ranking and eligibility decisions separately.

Now make colour a preference. D2 may become a useful substitute, so both the relevance rubric and the eligible set must be reconsidered. The text of the query alone does not settle that product decision.

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
