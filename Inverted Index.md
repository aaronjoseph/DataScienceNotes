---
note_type: concept
search_stage: indexing
---

# Inverted Index

#search-eng

## Overview

An inverted index maps each term to the documents containing it. Its dictionary stores terms; each term's **postings list** stores document IDs and, depending on the index, frequencies or positions. **Document frequency** counts documents containing a term, not total occurrences. [^1]

```mermaid
flowchart LR
    D[Documents] --> T[Tokenization]
    T --> A[Normalisation and optional linguistic processing]
    A --> I[Dictionary and postings]
```

## Build and Query a Tiny Index

Assume lowercase tokens and no stemming:

| Document | Text |
|---|---|
| D1 | red hiking boots |
| D2 | black hiking boots |
| D3 | red running shoes |

| Term | Postings |
|---|---|
| red | D1, D3 |
| hiking | D1, D2 |
| boots | D1, D2 |
| black | D2 |
| running | D3 |
| shoes | D3 |

`red AND boots` intersects two postings lists and returns D1. `red OR boots` takes their union and returns D1, D2, D3. Presence alone cannot establish phrase order.

## Construction

A simple sort-based construction tokenizes documents, normalises terms, sorts `(term, document ID)` records, combines repeated occurrences, and groups postings by term. Posting IDs are ordered to support efficient traversal. This is a teaching algorithm, not a requirement to alphabetically sort each source document. [^1]

See [[Tokenization]], [[Stemming and Lemmatization]], and [[Stopwords]] for analysis choices. [[TF-IDF]] and [[BM25]] add relevance weighting; the index itself does not define a ranking function.

## Why Posting Lists Make Search Efficient

For an AND query, traverse sorted document IDs in the relevant posting lists. If the current IDs differ, advance the smaller one; if they agree, emit the document and advance both. Intersecting lists of lengths $a$ and $b$ this way takes $O(a+b)$ comparisons in the worst case. Starting with a selective term can keep intermediate candidate sets small.[^merge]

An OR query takes the union instead. It broadens candidates and leaves ranking to distinguish partial matches. The choice between AND and OR changes eligibility under that lexical query; it is not just a different ranking weight.

> [!example]- Add frequencies and positions
> Add D4=`red red boots`, with positions numbered from 1. Its postings include `red: (D4, frequency=2, positions=[1,2])` and `boots: (D4, frequency=1, positions=[3])`.
>
> The phrase `red boots` matches through positions 2 and 3. The reversed phrase `boots red` does not. A document-ID-only index could tell you both words occur but could not decide their order. A positional index provides that extra evidence.[^positions]
>
> With `red` in D1, D3, D4, its DF is 3. Repeating red within D4 affects its local TF but contributes only one document to DF.

## What the Index Does Not Decide

The index supplies term evidence. [[BM25]] decides how to weight it; [[Query Understanding]] decides which fields and operators to use; [[Index Updates]] determines when changes become visible. For a missing result, inspect the actual stored terms and searchable document version before tuning scores.

## Practice

Add D4: `red red boots`. What changes? The `red` document frequency becomes 3, while its frequency within D4 is 2. Work out which positions you would retain for phrase queries.

## Further Study

- [[Index Updates]] — Refresh, durability, and update ordering.
- [[Query Understanding]] — Connect analysis decisions to matching.

## References & Useful Links

[^1]: [Building an inverted index](https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html) — Dictionary, postings, term statistics, and construction.

[^merge]: [Processing Boolean queries](https://nlp.stanford.edu/IR-book/html/htmledition/processing-boolean-queries-1.html) — Sorted postings intersection and query ordering.
[^positions]: [Positional indexes](https://nlp.stanford.edu/IR-book/html/htmledition/positional-indexes-1.html) — Term positions for phrase and proximity matching.
