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

## Exercise

A product changes price at 10:00, reaches ingestion at 10:01, is acknowledged at 10:02, and becomes searchable at 10:03. Source-to-search lag is three minutes; acknowledgement-to-search lag is one. Decide which reflects the user's experience. See [[Inverted Index]], [[Approximate Nearest Neighbours]], and [[Monitoring - MLOPS|Monitoring]].

## References & Useful Links

- [Near real-time search](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search) — Refresh and visibility.
- [Translog](https://www.elastic.co/docs/reference/elasticsearch/index-settings/translog) — Recovery, commits, and durability settings.
- [Merges](https://www.elastic.co/docs/reference/elasticsearch/index-settings/merge) — Background segment merging.
