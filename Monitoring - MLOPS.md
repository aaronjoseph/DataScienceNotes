---
note_type: concept
search_stage: serving
---

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

## Define a Service Indicator Precisely

A service-level indicator (SLI) needs an event population and a rule for a good event. For example, define a good search request as an eligible request that returns a valid response within a stated deadline:

$$
\mathrm{SLI}=\frac{\text{good eligible requests}}{\text{all eligible requests}}.
$$

Declare what “valid” means: HTTP success alone may not catch malformed results, mandatory-filter violations, or an unintended fallback. Keep relevance indicators separate when judgments arrive later. A request log that disappears during a failure must not make the denominator shrink invisibly; compare instrumentation coverage with an independent ingress count where available.

### Diagnose a healthy-looking endpoint

Out of 10,000 eligible requests, 9,950 return HTTP 200, but only 9,800 return valid responses within the deadline.

The HTTP success rate is $99.5\%$; the defined SLI is $98\%$.

The gap deserves investigation even if CPU utilisation and median latency look normal.

Now suppose candidate counts fall only for queries with a price filter after an index update. Inspect numeric field types, eligibility rules, searchable versions, and per-source removals before changing model weights. The earliest changed stage is the most useful starting point.

## Keep Metrics, Traces, and Logs Connected

- **Metrics** show trends and rates: candidate-count distributions, timeouts, missing features, fallback shares, and freshness lag.
- **Traces** show the sequence and critical path for selected requests, including parallel calls.
- **Logs** explain specific decisions and errors with controlled diagnostic context.

Use bounded dimensions such as stage, source, status, and a small set of query categories for metrics. Keep request identifiers in traces or logs. When combining latency data across instances, aggregate suitable histogram observations or counts; averaging instance p99 values does not yield the fleet p99.

## Exercise

Clicks drop while latency and traffic stay stable.

Trace index freshness, candidate coverage, feature availability, ranking changes, and UI instrumentation before attributing the drop to a model.

## References & Useful Links

- [Google SRE monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) — Golden signals and actionable monitoring.
