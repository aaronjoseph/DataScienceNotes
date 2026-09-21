# Judgement List

#search-eng

## Overview

A judgment list records how relevant a document is to a particular query or information need. It is part of an evaluation collection, alongside the queries and document corpus. Relevance belongs to the query–document pair, not the document alone. [^1]

## Example Schema

This is a proposed practice schema, not a universal format:

| query_id | query | document_id | grade | rationale |
|---|---|---|---|---|
| Q1 | red hiking boots | D1 | 3 | Red hiking boots matching the intent |
| Q1 | red hiking boots | D2 | 1 | Hiking boots, wrong colour |
| Q1 | red hiking boots | D3 | 0 | Unrelated product |

Define the grade rubric before labelling. A hard colour constraint could instead make D2 irrelevant; the rubric and query intent determine that decision.

Keep query context, corpus snapshot, assessor/rubric version, and label provenance. Preserve **unjudged** separately from a genuine grade 0.

## Build a Useful Set

1. Sample queries across frequent, rare, ambiguous, misspelled, and constrained intents.
2. Pool candidates from different retrieval systems and include known failures.
3. Label without exposing system identity when feasible.
4. Resolve disagreements with a written rubric; keep ambiguous cases visible.
5. Reserve evaluation queries rather than tuning repeatedly on the entire list.

Pooling cannot guarantee that all relevant documents were judged. Report coverage and a missing-judgment policy when calculating [[NDCG]] or recall. [^1]

## Practice

Write a rubric for ten product queries, then independently label the same pairs twice. Identify where the rubric is too vague.

## Related Notes

- [[Data Labeling]] — Annotation methods.
- [[Search Evaluation]] — How judgments become metrics.
- [[Data Leakage]] — Protect evaluation data.

## Label Quality and Coverage

- [[Annotation Agreement]] — Measure independent assessor consistency before adjudication.
- [[Relevance Pooling]] — Choose assessment candidates and account for unjudged results.

## References & Useful Links

[^1]: [IR system evaluation](https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html) — Test collections and relevance assessments.
- [What Is a Judgment List?](https://softwaredoug.com/blog/2021/02/21/what-is-a-judgment-list) — Original saved resource, retained for further practical reading.
