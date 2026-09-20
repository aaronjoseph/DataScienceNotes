# Concept Drift

#search-eng

## Definition

This note uses concept drift to mean a change in the input–target relationship $P(Y\mid X)$ over time. Some literature uses a broader definition covering changes in the joint distribution; check each source's convention. Distinguish it from [[Data Drift]], a change in $P(X)$, and from a change in label prevalence $P(Y)$. These can coexist; marginal distributions alone do not identify the mechanism.

Examples include changing borrower outcomes during macroeconomic shifts, equipment wear changing the relation between sensor readings and failure, and new competitor products changing user preferences. Each is a hypothesis to investigate, not proof that retraining is needed.

## Search Diagnosis

A query can retain its spelling while its intent changes. Changes in results, pricing, presentation, or availability can also change clicks without changing editorial relevance. [[Click Bias]] and delayed conversions make observed feedback harder to interpret.

Compare held-out recent labels and earlier labels using consistent definitions. Inspect query segments, model/index versions, and instrumentation changes. Decide whether the remedy is model training, freshness, an eligibility rule, or a data-pipeline fix; validate the intervention rather than retraining automatically.

## Exercise

For “world cup schedule”, describe how the useful answer changes over time. Separate stale indexed content from a changed ranking relationship. Link the diagnosis to [[Index Updates]] and [[Monitoring - MLOPS|Monitoring]].

## References & Useful Links

- [Learning under Concept Drift: an Overview](https://arxiv.org/pdf/1010.4784) — Changing distributions, concepts, and adaptation.
