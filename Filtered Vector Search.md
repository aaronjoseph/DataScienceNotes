---
note_type: concept
search_stage: retrieval
---

# Filtered Vector Search

#search-eng

## Overview

Filtered vector search combines nearest-neighbour similarity with boolean and numeric constraints. Similarity finds items that *resemble* the query; filters decide which items are *allowed*. Business constraints such as price range, product type, availability, and active status belong in filters, not in the embedding.[^1]

A related control, **crowding**, limits how many results can share a tag, which increases diversity within one retrieval call.[^2]

## Filtering Strategies

These are general design patterns; which one a given engine uses is implementation-specific and should be checked in its documentation.

- **Post-filtering:** retrieve $k$ neighbours, then drop ineligible ones. Simple, but can return far fewer than $k$ results when filters are selective.
- **Pre-filtering:** restrict to eligible items, then search. This changes the search universe; exactness still depends on the search algorithm, and cost depends on how eligibility is indexed.
- **Filtering during search:** the index evaluates predicates while it searches, so eligible neighbours are collected directly.

## Example Semantics: Google Cloud Vector Search

This service was previously branded Vertex AI Vector Search; its Python SDK classes still use `MatchingEngine` names.

Semantics verified against Google Cloud documentation on 23 September 2026.[^1][^2][^3]

- **Namespaces and tokens.** Each datapoint carries restricts such as `color: [red, blue]`. A query is AND across namespaces and OR within a namespace: `{color: red, blue}, {shape: square}` means `(red OR blue) AND square`.[^1]
- **Deny lists.** A query can deny a token, excluding datapoints with it. A namespace with only denied tokens matches everything not denied.[^1]
- **Asymmetric wildcards.** An empty *query* namespace matches everything. An empty *datapoint* namespace does **not** match a query that specifies that namespace.[^1] Missing attribute data therefore silently excludes items.
- **Numeric restricts.** Queries specify a namespace, a value, and one of `LESS`, `LESS_EQUAL`, `EQUAL`, `GREATER_EQUAL`, or `GREATER`. Use one numeric type per namespace.[^1]
- **Crowding.** Datapoints can carry a `crowding_tag`; a query's `per_crowding_attribute_neighbor_count` is the maximum number of returned matches with the same tag.[^2][^3]
- **Search effort.** `approximateNeighborsCount` should exceed the requested neighbour count; increasing it or `fractionLeafNodesToSearch` can increase recall, latency, and cost.[^2]

## Worked Example

The example combines categorical, numeric, missing-data, and parent-crowding rules.

Query: `type ∈ {laptop}`, `brand` deny `{X}`, `condition ∈ {new}`, `price ≤ 1000`, crowding limit 1 per parent product.

| Item | type | brand | condition | price | parent | Eligible? |
|---|---|---|---|---|---|---|
| L1 | laptop | A | new | 899 | P1 | Yes |
| L2 | laptop | A | new | 949 | P1 | Filter yes; crowded out if L1 ranks higher |
| L3 | laptop | X | new | 700 | P2 | No: brand denied |
| L4 | laptop | B | *(missing)* | 650 | P3 | No: empty datapoint namespace |
| L5 | tablet | B | new | 500 | P4 | No: type |
| L6 | laptop | C | new | 1200 | P5 | No: price |

At most L1 is returned from these rows. L4 may be a data-quality bug, not a genuinely ineligible item.

## Design Patterns

- **Base eligibility in every channel.** Active status, sellable order codes, and excluded conditions should apply to all retrieval calls, not only the main one.
- **Allow list to deny list.** A broad channel can convert a predicted product-type allow list into a deny list, deliberately searching *outside* the predicted types to hedge against [[Named Entity Recognition|NER]] errors. See [[Candidate Generation]].
- **Consistent types across stores.** If candidates are later re-filtered in a database, encode each attribute with the database's native type. A boolean stored as a string token in the index but compared as a boolean in SQL is an easy source of errors.
- **Crowding by parent.** A tag per parent product prevents one product's variants from filling the pool. See [[Search Result Diversification]].

## Limitations and Pitfalls

- **Selective filters shrink pools.** Monitor returned-count distributions per channel, not just averages.
- **Index attributes go stale.** Availability and price change faster than many index refresh cycles. Re-check volatile attributes in a live store after retrieval; see [[Index Updates]].
- **Crowding can hide relevance.** Several variants may be genuinely relevant (for example, different sizes). Choose the tag and limit deliberately.
- **ANN recall under filters** can differ from unfiltered recall. Benchmark the filtered workload; see [[Approximate Nearest Neighbours]].

## Define the Target Before Choosing a Strategy

For eligibility predicate $F_q(d)$ and vector score $s(q,d)$, the intended result is the highest-scoring $k$ items from

$$
E_q=\{d\in\mathcal D:F_q(d)=\mathrm{true}\}.
$$

Searching the entire collection for $k$ items and then filtering generally does not produce the top $k$ within $E_q$.

Applying predicates early avoids some wasted candidates, but an approximate index can still miss eligible neighbours.

Compare it with exact search over the same eligible subset.

### Estimate post-filter underfilling

Use this deliberately simplified model:

- Retrieved pool size: $K=100$ items.
- Independent probability that an item passes the filter: $s=0.1$.

The expected number of survivors is

$$
Ks=100\times0.1=10.
$$

Retrieving 100 therefore does not guarantee 10 eligible outputs; the actual count varies.

Real eligibility is often correlated with similarity and catalogue structure, so collection-wide selectivity may not equal selectivity among top neighbours.

Oversampling by $1/s$ is a planning heuristic, not a recall guarantee.

Measure returned counts and exact filtered-neighbour recall for the workload.

## Preserve the Meaning of Constraints

Distinguish missing attribute data from an explicit false value, and distinguish `<` from `<=`. For `price under 1000`, a literal interpretation excludes exactly 1000; `at most 1000` includes it. A request parser, vector index, and database re-check must agree on this boundary and on currency, units, and types.

Crowding adds a second selection rule beyond eligibility. Evaluate whether the chosen parent representative still satisfies the request after variant expansion; a diverse pool can otherwise lose the only eligible variant.

## Exercise

Add a datapoint that denies the token `refurbished` in its own restricts.

Predict which queries it can and cannot match, then check your answer against the deny-list rules in the documentation.[^1]

## References & Useful Links

[^1]: [Google Cloud: Filter vector matches](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/filtering) — Namespaces, tokens, deny lists, wildcard rules, and numeric restricts. Accessed 23 September 2026.
[^2]: [Google Cloud: Query public index to get nearest neighbors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-public-endpoint) — Filtering and crowding in queries; performance-related query parameters. Accessed 23 September 2026.
[^3]: [Google Cloud: Input data format and structure](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/format-structure) — Datapoint `restricts`, `numeric_restricts`, and `crowding_tag` fields. Accessed 23 September 2026.
