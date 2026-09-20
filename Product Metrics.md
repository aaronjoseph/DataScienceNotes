# Product Metrics

#search-eng

## Define the Decision and Denominator

A metric needs a population, event definition, time window, and aggregation rule. No universal 5% premium-conversion threshold determines product success. Compare against the product's economics, historical baseline, and experiment design.

## Common Measures

| Measure | Working definition and caveat |
|---|---|
| DAU / MAU | Distinct active users per day/month; define “active” and identity resolution |
| Conversion rate | Converting eligible units divided by eligible units in a stated window |
| ARPU | Period revenue divided by the chosen user population for that period |
| MRR / ARR | Normalised recurring monthly revenue / annualised recurring revenue; exclude one-off charges and document adjustments |
| Customer churn | Lost customers divided by customers at period start, with a consistent definition |
| Net revenue retention | $(starting\ recurring\ revenue+expansion-contraction-churn)/starting\ recurring\ revenue$ for the starting cohort; excludes new customers |
| CAC | Attributed acquisition costs divided by acquired customers, with cost and attribution scope stated |

Lifetime value is an estimate of discounted future contribution, not just revenue. A simplified recurring model with constant per-period contribution $m$, retention $r$, discount rate $d$, and first contribution after surviving one period gives $mr/(1+d-r)$. This follows from a geometric series and requires $r/(1+d)<1$; timing, changing retention, margins, and acquisition costs alter the model. Do not treat it as a forecast without checking those assumptions.

Lead scoring predicts a chosen sales outcome; it is not automatically a causal propensity score.

## Search Outcomes

Measure query/session success, zero-result rate, reformulation, abandonment, latency, and conversion with explicit attribution windows. More clicks can mean more engagement or more difficulty finding an answer. Pair online measures with [[Search Evaluation]], [[Click Bias]], and [[AB Testing]].

## Exercise

A starting cohort contributes 100 revenue units, expands by 20, contracts by 5, and loses 10. NRR is 105%. Adding 40 from new customers changes total revenue but not this cohort's NRR.

## References & Useful Links

- [Stripe subscription analytics](https://docs.stripe.com/billing/subscriptions/analytics) — Recurring revenue and cohort metrics.
- [Amplitude user identity](https://amplitude.com/docs/data/sources/instrument-track-unique-users) — Counting distinct users consistently.
