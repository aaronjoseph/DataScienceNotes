# Data Drift

#search-eng

## Definition

Data drift is a change in the input distribution $P(X)$ between a reference population and current data. It does not automatically mean that the relationship $P(Y\mid X)$ changed or that model quality fell. “Covariate shift” often adds the assumption that $P(Y\mid X)$ remains stable; state that assumption explicitly.

A camera upgrade from low-resolution images to higher-resolution images can change image statistics. In search, seasonal query mixes, new catalogue categories, and language shifts can change features. Broken feature joins can look like drift too, so check pipeline correctness first.

## Diagnose Before Retraining

1. Compare schema, null rates, units, preprocessing versions, and sample selection.
2. Compare distributions within stable slices as well as overall: changed traffic proportions can explain aggregate movement.
3. Quantify effect size and persistence. Very large samples can flag tiny differences as statistically significant.
4. Check [[Search Evaluation|quality]] when labels arrive and inspect [[Concept Drift]]. A distribution alert is not itself a relevance regression.

## Exercise

If Spanish queries grow from 10% to 30% while each language's score distribution stays fixed, explain why the aggregate distribution changes. Compare traffic-weighted and within-language quality before choosing a response. See [[Monitoring - MLOPS|Monitoring]] and [[Sampling]].

## References & Useful Links

- [Evidently data drift guide](https://www.evidentlyai.com/ml-in-production/data-drift) — Input distributions and monitoring considerations.
