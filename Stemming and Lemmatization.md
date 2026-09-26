---
note_type: concept
search_stage: query_understanding
---

# Stemming and Lemmatization

#search-eng

## Overview

Both techniques group morphological variants. **Stemming** applies rules that reduce word forms, sometimes producing a non-word. **Lemmatization** seeks a dictionary base form and may use vocabulary, morphology, or part-of-speech information. Exact output depends on the implementation and language. [^1]

| Approach | Intuition | Risk |
|---|---|---|
| Stemming | Reduce related spellings to a shared stem. | Merge words whose meanings should remain distinct. |
| Lemmatization | Map an inflected form to its lemma. | Wrong linguistic analysis or missing vocabulary. |

Porter and Snowball/Porter2 are examples of stemming approaches. More aggressive rules are not automatically better. Lemmatization may require more processing, but speed must be measured for the chosen implementation. [^1]

## In Search

Normalisation can improve recall when `boots` should match `boot`. It can hurt precision when distinct meanings collapse. Evaluate the change using a [[Judgement List]] and [[Search Evaluation]], including identifier and brand queries.

The old example table implied that all stemmers map `going`, `goes`, and `gone` to `go`; that is not a universal stemming rule. Record outputs from the actual analyser instead of assuming a linguistic result.

## Think in Terms of Matching Groups

Let $g(t)$ be the normaliser applied to a token.

Two spellings can match through normalisation when $g(t_1)=g(t_2)$.

The spelling of the resulting stem is less important than which words it groups together.[^1] However, once distinct meanings share the same indexed value, that value alone cannot recover the original distinction.

**Under-stemming** leaves useful variants apart. **Over-stemming** merges distinctions the task needs. Lemmatization can reduce some mistakes, but a correct linguistic lemma still does not establish that two phrases express the same product intent. Search quality depends on the full field and query context.

### Design a controlled comparison

Start with D1=`waterproof boot`, D2=`waterproof boots`, and D3=`boot cleaner`. Query `waterproof boots` should find D1 and D2 under a rubric that accepts the singular form.

An exact field may miss D1. A normalised field mapping `boots` to `boot` can recover it. D3 now shares a term too, so check whether the remaining terms and ranking keep cleaner below actual boots. The recovered match and any new false match are separate observations.

Retain an exact identifier field for a model code that happens to resemble an inflected word. A language analyser intended for product titles should not decide identifier equality.

## How to Evaluate a Change

Hold the corpus, queries, relevance rubric, candidate depth, and ranker fixed. Compare analysis output first, then candidate membership, then ranked metrics. A score difference can arise because normalisation changes term counts and document frequencies as well as matches. Review plural forms, brand names, technical phrases, and each supported language; a result on English does not establish performance elsewhere.

## Practice

Compare an unchanged field, a stemmed field, and a lemmatized field on ten queries. Record both recovered matches and newly introduced false matches.

## Related Notes

- [[Tokenization]] — Determines the units being normalised.
- [[Inverted Index]] — Stores the resulting terms.

## References & Useful Links

[^1]: [Stemming and lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) — Definitions, algorithms, and retrieval tradeoffs.
