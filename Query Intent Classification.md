# Query Intent Classification

#search-eng

## Overview

Intent classification decides what kind of request a query is, so the system can choose a retrieval path. It is a **routing** decision. A misrouted query can go through the wrong pipeline entirely, which is often worse than a poor ranking.

It belongs to [[Query Understanding]] and usually consumes [[Named Entity Recognition]] output. It is distinct from ranking: the router chooses *how* to search, not *which* result is best.

## An Example Intent Set

This set comes from one e-commerce product-search system. Other domains need different classes; web-search taxonomies are coarser (see Open Questions).

| Intent | Typical signal | Path | Cost of misrouting |
|---|---|---|---|
| Product search | Default | Hybrid [[Candidate Generation]] and reranking | Baseline behaviour |
| Identifier lookup | SKU, UPC, or model-number pattern | Exact key lookup, then variant expansion | Treating an identifier as text returns similar but wrong items |
| More like this | Explicit UI action with a source item | Item-to-item vector similarity, with filters derived from the source item | Text search ignores the chosen item |
| Multiple type groups | Two or more active product types detected | Per-type recall and rerank, then merge | One type dominates or the query is over-filtered |
| Invalid or moderated | Policy classifier | Empty or safe response | Unsafe content served, or valid queries blocked |
| Informational | Question-like query | Content or answer path | Product grid for a question |

## Rules, Models, and Precedence

- **Explicit signals first.** A UI flag is stronger evidence than any inference from text.
- **Deterministic patterns for identifiers.** They are cheap and precise, but check collisions: phone numbers, years, and sizes also contain digits.
- **Models for fuzzy classes.** Return a confidence and the evidence used, such as detected types.
- **Gate by current catalogue state.** A detected product type that is no longer active should not affect confidence or filters.
- **Write the precedence down and test it.** Overlapping rules otherwise depend on code order.

Illustrative routing logic (the seven-digit rule is one system's heuristic, not a standard):

```python
import re

def route(query: str, more_like_this: bool, ner_types: list[str], active_types: set[str]) -> str:
    if more_like_this:
        return "MORE_LIKE_THIS"
    if re.search(r"\d{7,}", query):
        return "PRODUCT_LOOKUP"
    types = {t for t in ner_types if t in active_types}
    if len(types) >= 2:
        return "MULTIPLE_TYPE_GROUPS"
    return "PRODUCT_SEARCH"

active = {"tv", "soundbar", "laptop"}
print(route("6501234", False, [], active))                          # PRODUCT_LOOKUP
print(route("tv and soundbar", False, ["tv", "soundbar"], active))  # MULTIPLE_TYPE_GROUPS
print(route("call 8005551234", False, [], active))                  # PRODUCT_LOOKUP: a collision
```

The last case shows how a pattern rule can misroute. Decide whether a lookup miss should fall back to product search.

## Evaluation

- Build a labelled query set with an expected intent per query and report a [[Confusion Matrix & Metrics|confusion matrix]]. Intents are usually imbalanced; see [[Imbalanced Classification]].
- Weight errors by cost. Misrouting an identifier lookup and misrouting a broad query have different consequences.
- Measure downstream effects per intent: zero-result rate, reformulation rate, and [[Search Evaluation|result quality]].
- Slice by digits, very short queries, brand-only queries, negations, and multi-type queries. The [[ESCI]] dataset deliberately sampled negations and parse-pattern queries as hard cases.[^1]

## Common Pitfalls

- **Stale session caches.** If intent is cached per session, the cache key must change when the query changes.
- **Fan-out cost.** Multiple type groups multiply recall and reranking work; bound the number of groups. See [[Tail Latency]].
- **Silent fallbacks.** Log when a route falls back, otherwise route quality cannot be measured.

## Exercise

Label these queries, state the signal you used, and name the downstream failure if you are wrong: `65 inch tv`, `6501234`, `tv and soundbar`, `how to clean a laptop screen`, `usb c cable 2m`, `macbook air m3 13`.

## Open Questions

- #TODO Read Broder (2002), "A taxonomy of web search". Only the title, author, and year were verified; its categories are not summarised here.

## References & Useful Links

[^1]: [Reddy et al., "Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search", 2022](https://arxiv.org/abs/2206.06588) — Query selection strategies for hard product-search queries, including negations and parse patterns.
