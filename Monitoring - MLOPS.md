# Monitoring - MLOPS

#search-eng

## Purpose

Monitor whether the service works, whether its data is trustworthy, and whether its outputs meet the intended quality. System health and relevance are different signals; a fast response can still contain poor results.

## Search Diagnosis by Stage

| Stage | Useful observations | Question |
|---|---|---|
| Request | Traffic, latency, errors, timeouts, query slices | Is a user segment affected? |
| Index | Ingestion lag, rejected updates, searchable version | Is content fresh and complete? |
| Retrieval | Candidate counts by source, zero results, filter removals | Did relevant items reach ranking? |
| Features | Missing values, failed joins, schema/model compatibility | Did the ranker receive valid inputs? |
| Ranking | Score-source mix, fallback rates, score distributions | Did the intended model run? |
| Response | Duplicates, eligibility, ordering, end-to-end latency | What did the user receive? |
| Feedback | Judgments, clicks, conversions, experiment assignment | Did measured quality change? |

Use latency, traffic, errors, and saturation to investigate service health. Track tails and workload slices; component p99 values cannot simply be added to derive end-to-end p99. Record model, feature, configuration, and index versions in traces or controlled logs. Avoid sensitive raw queries and unbounded user/query IDs in metric labels.

## Alert and Investigate

Alert on actionable user impact or meaningful impending failures. Distribution movement alone is diagnostic evidence. Compare a stable reference window and account for seasonality. Delayed labels and [[Click Bias]] limit immediate quality measurement. See [[Data Drift]], [[Concept Drift]], and [[Search Evaluation]].

## Exercise

Clicks drop while latency and traffic stay stable. Trace index freshness, candidate coverage, feature availability, ranking changes, and UI instrumentation before attributing the drop to a model.

## References & Useful Links

- [Google SRE monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) — Golden signals and actionable monitoring.
