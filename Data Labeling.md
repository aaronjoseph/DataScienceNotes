---
note_type: concept
search_stage: evaluation
---

# Data Labeling

#search-eng

## Overview

Data labeling attaches an outcome or judgment to an example so a model or evaluation procedure has a target. In search, the example is usually a **query–item pair with context**, not an item by itself. A charger can be relevant to a charger query and a complement to a phone query. Define the task before collecting labels.

Labels can come from people, observed events, rules, or model predictions. Their origin affects what they mean and which errors they can contain. Human judgments are valuable but can disagree, especially when the information need or rubric is unclear.[^judgments]

## Data Labeling

| Method | What supplies the label? | Main question to check |
|---|---|---|
| Direct/process feedback | A recorded outcome such as a click, return, or purchase | Does the event measure the intended target, and who had the opportunity to produce it? |
| Human labeling | An assessor applying a rubric | Is the example understandable and the rubric reproducible? |
| [[Active Learning]] | A person labels examples selected by a model or strategy | Does the selection improve learning per unit of effort? |
| [[Weak Supervision]] | Heuristics or other noisy sources | How do coverage, errors, and source dependencies affect the labels? |
| [[Semi-Supervised Labeling]] | A method combines labeled and unlabeled data | Does the structure used to infer labels agree with the task? |

These methods can be combined. Their outputs should retain provenance rather than becoming an undifferentiated “ground truth” column.

## Process Feedback

Feedback can continuously refresh a training set and capture changing behaviour. Its strength depends on the target: an order is direct evidence of a purchase, but not proof that every other retrieved product was irrelevant. An unclicked result may not have been examined. Use [[Click Bias]] to reason about exposure, position, and presentation.

Record event time, availability time, request or session context, displayed position, and the version of the policy that generated the exposure. Construct historical features using only information available before the target event; see [[Data Leakage]].

## Label Consistency

A practical annotation workflow is:

1. Define the unit, label set, and concrete borderline examples.
2. Give assessors the same relevant context and hide system identity where feasible.
3. Independently label an overlapping audit sample.
4. Inspect disagreements using [[Annotation Agreement]].
5. Adjudicate with a written rationale, version the rubric, and revisit affected labels.

Keep an explicit uncertain or insufficient-information state. Majority voting can reduce some individual errors but cannot fix a shared misunderstanding. Merge classes only when the task genuinely does not need the distinction; disagreement alone is not a reason to erase an important boundary. One mislabeled outlier does not automatically cause a learning algorithm to fail, but systematic errors can distort both learning and evaluation.

## Worked Example

For `waterproof hiking boots`, assess a boot, a water-resistant trainer, and a boot-cleaning spray.

The rubric must explain whether waterproofing is mandatory and whether complements belong in the main results.

Save the assessor's rationale so a later reviewer can distinguish missing product information from a different interpretation of relevance.

### What should happen after the rubric changes?

Suppose a new rule makes waterproofing mandatory. Reassess the affected pairs and create a new judgment version. Recompute both the baseline and proposed ranker on that version. Keep the previous labels available so changes in measured quality can be traced to either the system or the rubric.

## Exercise

Design an annotation record for ten queries.

Include one identifier, one negation, one ambiguous size, and one query with missing catalogue attributes.

Identify which cases can be labeled confidently and which need additional context.

## Search Connections

- [[Search Engineering]] — Learning sequence and review scope.
- [[Judgement List]] — A versioned collection of relevance assessments.
- [[Search Evaluation]] — Turning labels into comparable metrics.
- [[ESCI]] — One product-search relevance rubric.

## References & Useful Links

[^judgments]: [Introduction to Information Retrieval: Assessing relevance](https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html) — Human relevance assessments, incomplete judgments, and assessor variation.
