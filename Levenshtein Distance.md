---
note_type: concept
search_stage: query_understanding
---

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

## Dynamic Programming, Step by Step

Let $D_{i,j}$ be the distance between the first $i$ units of $a$ and the first $j$ units of $b$. With unit costs,

$$
\begin{aligned}
D_{i,0}&=i,\\
D_{0,j}&=j.
\end{aligned}
$$

$$
D_{i,j}=\min\left\{D_{i-1,j}+1,\ D_{i,j-1}+1,\ D_{i-1,j-1}+\mathbf1[a_i\ne b_j]\right\}.
$$

The three choices delete, insert, or substitute/match the last unit.

Each cell reuses solutions to shorter-prefix problems rather than enumerating all edit sequences.[^1] The final answer is $D_{m,n}$.

Two rows suffice if only the distance is needed; reconstructing a particular edit path requires retaining or recomputing more information.

### Fill the table for `cat` and `cut`

| Prefix | empty | c | cu | cut |
|---|---:|---:|---:|---:|
| empty | 0 | 1 | 2 | 3 |
| c | 1 | 0 | 1 | 2 |
| ca | 2 | 1 | 1 | 2 |
| cat | 3 | 2 | 2 | 1 |

The diagonal path matches `c`, substitutes `a` with `u`, and matches `t`. One substitution is sufficient, so the distance is 1. The table also handles unequal lengths through its insertion and deletion cases.

## Candidate Generation Versus Correction

Distance is one feature for choosing a correction. For `car`, both `cat` and `bar` are one edit away, but their usefulness depends on the query and catalogue. Generate a bounded candidate set using vocabulary structure or n-gram overlap, then score intent preservation and domain evidence. Avoid automatically correcting a valid exact identifier merely because a more common word is nearby.

## Practice

Give one insertion, deletion, and substitution that changes a product query. Compare edit distance with the overlap measured by [[N-Grams]].

## References & Useful Links

[^1]: [Edit distance](https://nlp.stanford.edu/IR-book/html/htmledition/edit-distance-1.html) — Operations, dynamic programming, and spelling correction.
