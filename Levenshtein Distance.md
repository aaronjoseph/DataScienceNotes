# Levenshtein Distance

#search-eng

## Overview

Levenshtein distance is the minimum number of single-unit insertions, deletions, and substitutions required to transform one sequence into another. Units are often characters, but must be specified. With unit costs, `boot` → `boots` has distance 1. [^1]

## Search Use

Use edit distance to generate or score spelling candidates, then consider intent and catalogue vocabulary. A close spelling does not guarantee the right correction: identifiers, brands, and short words require care.

Example: `cat` and `car` differ by one substitution, but a query for one should not automatically retrieve the other.

## Common Pitfalls

- Ordinary Levenshtein does not count a transposition as one operation: `ab` → `ba` costs 2. A transposition-aware variant is a different distance.
- Normalise consistently before comparison; case and Unicode representation can affect the sequence.
- The standard dynamic-programming algorithm takes $O(mn)$ time for lengths $m$ and $n$. Comparing every vocabulary term at query time may be too expensive. [^1]

## Practice

Give one insertion, deletion, and substitution that changes a product query. Compare edit distance with the overlap measured by [[N-Grams]].

## References & Useful Links

[^1]: [Edit distance](https://nlp.stanford.edu/IR-book/html/htmledition/edit-distance-1.html) — Operations, dynamic programming, and spelling correction.
