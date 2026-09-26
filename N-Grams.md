---
aliases: ["N-Gram Model"]
note_type: concept
search_stage: query_understanding
---

# N-Grams

#search-eng

## Overview

An n-gram is a contiguous sequence of $n$ units.

Specify whether those units are characters or tokens.

An n-gram representation records local sequences; an n-gram language model additionally assigns probabilities to sequences. [^1]

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

## Occurrences, Features, and Order

The count $\max(0,L-n+1)$ counts windows, not distinct features.

For `aaaa`, character bigrams are `aa`, `aa`, `aa`: three occurrences but one distinct bigram.

A count vector stores 3, whereas a presence vector stores 1.

Boundary padding, spaces, and case normalisation change which windows exist, so specify them before comparing implementations.

For a token sequence $w_1,\ldots,w_L$, the window at position $i$ is $(w_i,\ldots,w_{i+n-1})$.

Combining unigrams and bigrams lets a representation retain broad term evidence and some phrase evidence.

It still does not encode arbitrary long-range order.

### Calculate character overlap

With no padding, `boot` produces the bigram set $A=\{bo,oo,ot\}$; `boots` produces $B=\{bo,oo,ot,ts\}$.

Their Jaccard overlap is

$$
J(A,B)=\frac{|A\cap B|}{|A\cup B|}=\frac34.
$$

This is a set-overlap calculation, so repeated grams count once.

A count-based similarity would need a different definition.

A high overlap suggests a spelling relationship; it does not prove relevance to a query or interchangeability in a sentence.

## Index-Size Tradeoff

Generating every length from $a$ to $b$ creates the following number of occurrences before deduplication:

$$
\sum_{n=a}^{b}\max(0,L-n+1).
$$

For a five-character token and lengths 2 through 4:

$$
4+3+2=9\text{ occurrences}.
$$

Edge-prefix n-grams would keep only prefixes and generate fewer features; they serve a different matching goal, such as prefix completion.

Measure vocabulary, postings, and false matches when selecting lengths.

## Practice

List character bigrams for `boot` and `boots`. Which overlap? Why does overlap alone not prove two terms have the same meaning?

## Related Notes

- [[Tokenization]] — Defines the units.
- [[Levenshtein Distance]] — Measures edits rather than overlapping substrings.
- [[Language Model]] — Sequence probabilities.

## References & Useful Links

[^1]: [Scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — Word and character n-gram features.
