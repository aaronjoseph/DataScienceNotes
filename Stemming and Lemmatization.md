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

## Practice

Compare an unchanged field, a stemmed field, and a lemmatized field on ten queries. Record both recovered matches and newly introduced false matches.

## Related Notes

- [[Tokenization]] — Determines the units being normalised.
- [[Inverted Index]] — Stores the resulting terms.

## References & Useful Links

[^1]: [Stemming and lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) — Definitions, algorithms, and retrieval tradeoffs.
