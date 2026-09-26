---
note_type: concept
search_stage: indexing
---

# Index Updates

#search-eng

## Freshness Is a Serving Requirement

An accepted write, a searchable change, and a durable change are different events. Define which event your freshness target measures. The following mechanics describe Elasticsearch/Lucene-style indexing, not every search engine.

## Distinguish the Operations

- **Refresh:** makes recent indexed changes visible to search by opening new searchable segments; it is not itself a durability guarantee.
- **Translog and flush:** the transaction log supports recovery of operations not yet in a Lucene commit. A flush creates a commit and starts a new translog generation; durability depends on configured acknowledgement/fsync semantics.
- **Merge:** consolidates segments in the background, reclaiming deleted-document space and changing read/write costs. It is not the same as refresh.

Frequent refreshes can increase indexing overhead. Acknowledged updates may not be immediately visible to search; choose appropriate refresh behaviour for the workflow. Avoid assuming an immediate search miss proves the write was lost.

## End-to-End Update Contract

Track source version, ingestion, transformation, index acknowledgement, and observed search visibility. Use stable IDs and an ordering/version policy so a late older event cannot overwrite a newer state. Deletes, retries, failed batches, and backfills need explicit handling.

Changing token analysis or embedding models can require rebuilding data. Keep query/document representations compatible, validate a replacement index, catch up intervening updates, and use a controlled cutover with a rollback plan. Measure both freshness and relevance after cutover.

Attributes that change faster than the index refreshes, such as price and availability, are often re-checked in a live store after retrieval rather than trusted from index filters; see [[Filtered Vector Search]] and [[Search Caching]].

## Trace One Update Through the System

Define the milestones:

- $t_0$: source commit time.
- $t_1$: ingestion time.
- $t_2$: index acknowledgement.
- $t_3$: first observed searchable version.

For ordered milestones on comparable clocks:

$$
L_{\mathrm{freshness}}=t_3-t_0=(t_1-t_0)+(t_2-t_1)+(t_3-t_2).
$$

The decomposition tells you where to investigate. A refresh change cannot repair a large source-to-ingestion backlog. Polling search visibility adds observation delay, so record the polling interval and distinguish the measured upper bound from the exact visibility time.

### Out-of-order updates

Product P has version 101 at price 200 and version 102 at price 180. Version 102 arrives first; a delayed retry of 101 arrives later. Blind last-arrival-wins indexing restores an obsolete price. A per-product version check should reject the older event while allowing an idempotent retry of the same version.

Deletes need the same ordering rule. Otherwise a late old update can recreate a deleted product. Retaining deletion versions or another source-of-truth reconciliation mechanism prevents that class of error.

## Rebuild Without Losing Intervening Changes

1. Record a consistent source snapshot and the associated change-stream position.
2. Build the replacement with a named schema, analyser, and embedding version.
3. Replay later changes, including deletions, until the new index catches up.
4. Compare document counts, representative content, filtered retrieval, and version compatibility.
5. Switch query traffic at a defined boundary and retain a rollback path with its freshness limitations documented.

This is a general design checklist, not a claim that every engine provides these steps automatically. If old and new indexes use different embeddings, the query encoder must switch compatibly; see [[Embeddings]] and [[Shadow Deployment]].

## Exercise

A product changes price at 10:00, reaches ingestion at 10:01, is acknowledged at 10:02, and becomes searchable at 10:03.

Source-to-search lag is three minutes; acknowledgement-to-search lag is one.

Decide which reflects the user's experience.

See [[Inverted Index]], [[Approximate Nearest Neighbours]], and [[Monitoring - MLOPS|Monitoring]].

## References & Useful Links

- [Near real-time search](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search) — Refresh and visibility.
- [Translog](https://www.elastic.co/docs/reference/elasticsearch/index-settings/translog) — Recovery, commits, and durability settings.
- [Merges](https://www.elastic.co/docs/reference/elasticsearch/index-settings/merge) — Background segment merging.
