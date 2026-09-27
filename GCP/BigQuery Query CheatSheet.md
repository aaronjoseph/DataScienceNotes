---
note_type: concept
search_stage: evaluation
tags:
  - gcp
  - search-eng
---

These examples use **BigQuery GoogleSQL**. Begin with the intended row grain and answer, then optimize the physical query. The examples are illustrative and were not executed against a cloud project.

## Deduplicate before counting

This self-contained example keeps the latest arrival for each event ID. The final `ingest_id` tie-breaker must be unique in a production dataset. `QUALIFY` filters window-function results.[^syntax]

```sql
WITH events AS (
  SELECT 'e1' AS event_id, TIMESTAMP '2026-09-01 10:00:00+00' AS ingested_at,
         1 AS ingest_id, TRUE AS clicked
  UNION ALL
  SELECT 'e1', TIMESTAMP '2026-09-01 10:01:00+00', 2, TRUE
  UNION ALL
  SELECT 'e2', TIMESTAMP '2026-09-01 10:02:00+00', 3, FALSE
  UNION ALL
  SELECT 'e3', TIMESTAMP '2026-09-01 10:03:00+00', 4, CAST(NULL AS BOOL)
), deduplicated AS (
  SELECT *
  FROM events
  QUALIFY ROW_NUMBER() OVER (
    PARTITION BY event_id
    ORDER BY ingested_at DESC, ingest_id DESC
  ) = 1
)
SELECT
  COUNT(*) AS requests,
  COUNTIF(clicked IS NULL) AS missing_outcomes,
  SAFE_DIVIDE(COUNTIF(clicked), COUNTIF(clicked IS NOT NULL)) AS ctr
FROM deduplicated;
```

Expected by inspection: three unique requests, one missing outcome, and CTR of 0.5 among the two known outcomes. If all outcomes are missing, `SAFE_DIVIDE` yields `NULL`; zero observed evidence is different from a measured rate of zero.

## Filter a partitioned table

Assume `example_project.analytics.search_events` exists and is partitioned by the `DATE` column `event_date`. Replace this illustrative identifier before use.

```sql
SELECT query, COUNT(*) AS requests
FROM `example_project.analytics.search_events`
WHERE event_date >= DATE '2026-09-01'
  AND event_date < DATE '2026-09-08'
GROUP BY query
ORDER BY requests DESC, query
LIMIT 20;
```

The date predicate can prune partitions. Projection reduces unnecessary columns; the final `LIMIT` controls result size and is not a general substitute for scan reduction.[^performance]

## Repeated data changes the counting unit

```sql
WITH requests AS (
  SELECT 'r1' AS request_id, ['p1', 'p2'] AS product_ids
  UNION ALL
  SELECT 'r2', ARRAY<STRING>[]
)
SELECT request_id, product_id
FROM requests
CROSS JOIN UNNEST(product_ids) AS product_id;
```

This returns two product rows for `r1` and none for `r2`. If empty-result requests must remain in the denominator, preserve them with an appropriate left join or aggregate at the request level before expansion. See [[BigQuery]] for nested schemas.

## Query review checklist

| Check | What to verify |
|---|---|
| Correctness | Grain, nulls, duplicates, time zones, join cardinality |
| Scan | Needed columns and eligible partition filters |
| Compute | Shuffle, skew, repeated work, intermediate row counts |
| Cost | Pricing model, estimate, and applicable billing limit |

Aggregate before a join only when it preserves the question's semantics. Join order and broadcast decisions depend on the optimizer and statistics; “largest table always on the left” is not a correctness or performance law. Approximate aggregates trade precision for resource use and are unsuitable when exact counts are required.[^performance]

## Exercise

Change the first example to compute missing-outcome rate separately. Explain why replacing every `NULL` with `FALSE` would change CTR rather than merely fill a display gap.

> [!example]- Missing-outcome answer
> The missing-outcome rate is one out of three requests. Filling the missing value with `FALSE` changes CTR from one out of two known outcomes to one out of three requests, which makes an additional assumption about the missing event.

## References & Useful Links

[^syntax]: [GoogleSQL query syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) — CTEs, joins, `UNNEST`, window filtering, and query clauses.
[^performance]: [Optimize query computation](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute) — Scan reduction, joins, and execution-plan reasoning.
