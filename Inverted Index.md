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

## Practice

Add D4: `red red boots`. What changes? The `red` document frequency becomes 3, while its frequency within D4 is 2. Work out which positions you would retain for phrase queries.

## Further Study

- [[Index Updates]] — Refresh, durability, and update ordering.
- [[Query Understanding]] — Connect analysis decisions to matching.

## References & Useful Links

[^1]: [Building an inverted index](https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html) — Dictionary, postings, term statistics, and construction.
