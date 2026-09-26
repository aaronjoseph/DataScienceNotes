---
note_type: concept
search_stage: evaluation
---
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

## Turn an Intent into an Annotation Decision

Write the information need before showing results to assessors. Include accepted substitutes, explicit exclusions, locale or context, and the unit being judged. A product family, a sellable SKU, and a page passage can deserve different labels. The rubric should make these choices reproducible without exposing which system retrieved the item.

Keep three states separate: judged relevant, judged irrelevant, and unjudged. “Cannot decide from the available information” is another useful annotation outcome that can trigger review; it should not silently become grade zero.

### Make a colour disagreement actionable

For `red hiking boots`, one assessor gives a black hiking boot grade 1, while another gives it 0. First inspect the rubric: was colour mandatory or a preference? If that was unspecified, the disagreement exposes a missing task definition rather than proving either assessor careless.

Add the decision to the rubric, retain the original labels, and adjudicate the affected examples under the new version. Recompute all compared systems with the same updated judgments. Updating labels only for the proposed system would make the comparison inconsistent.

## Protect the Evaluation Set

Use a development judgment set to inspect errors and tune choices. Keep a separate final set for the assessment claimed in a report. Repeatedly inspecting and adapting to the final set makes it part of development, even when no gradient is calculated on it.

Include provenance fields such as annotation method, assessor or model version, timestamp, rationale, and adjudication status. Human review, implicit feedback, and model-generated labels supply different evidence. Use [[Annotation Agreement]] to diagnose rubric consistency and [[Relevance Pooling]] to understand which documents were selected for judgment.

## Practice

Write a rubric for ten product queries, then independently label the same pairs twice. Identify where the rubric is too vague.

## Related Notes

- [[Data Labeling]] — Annotation methods.
- [[Search Evaluation]] — How judgments become metrics.
- [[Data Leakage]] — Protect evaluation data.
- [[ESCI]] — A four-class product-search rubric with published agreement figures.

## References & Useful Links

[^1]: [IR system evaluation](https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html) — Test collections and relevance assessments.
- [What Is a Judgment List?](https://softwaredoug.com/blog/2021/02/21/what-is-a-judgment-list) — Original saved resource, retained for further practical reading.
