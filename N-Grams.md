---
aliases: ["N-Gram Model"]
---

# N-Grams

#search-eng

## Overview

An n-gram is a contiguous sequence of $n$ units. Specify whether those units are characters or tokens. An n-gram representation records local sequences; an n-gram language model additionally assigns probabilities to sequences. [^1]

## Worked Examples

For the character sequence `AGCTTCGA`, using a sliding window with stride 1:

| Size | N-grams |
|---|---|
| 1 | A, G, C, T, T, C, G, A |
| 2 | AG, GC, CT, TT, TC, CG, GA |
| 3 | AGC, GCT, CTT, TTC, TCG, CGA |

For word tokens `red hiking boots`, bigrams are `red hiking` and `hiking boots`. Without padding, a sequence of length $L$ has $\max(0,L-n+1)$ n-gram occurrences.

## Search Use

Word n-grams retain some local order that [[Bag of Words]] loses. Character n-grams can provide overlap across spelling variations. They expand the vocabulary and can generate partial matches that are not useful; evaluate precision as well as coverage. [^1]

## Practice

List character bigrams for `boot` and `boots`. Which overlap? Why does overlap alone not prove two terms have the same meaning?

## Related Notes

- [[Tokenization]] — Defines the units.
- [[Levenshtein Distance]] — Measures edits rather than overlapping substrings.
- [[Language Model]] — Sequence probabilities.

## References & Useful Links

[^1]: [Scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — Word and character n-gram features.
