---
note_type: concept
search_stage: experiments
---

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

Lifetime value is an estimate of discounted future contribution, not just revenue.

For a simplified recurring model, define:

- $m$: constant per-period contribution.
- $r$: retention probability per period.
- $d$: discount rate per period.

If the first contribution arrives after surviving one period, the estimate is

$$
\frac{mr}{1+d-r}.
$$

This follows from a geometric series and requires

$$
\frac{r}{1+d}<1.
$$

Timing, changing retention, margins, and acquisition costs alter the model. Do not treat it as a forecast without checking those assumptions.

Lead scoring predicts a chosen sales outcome; it is not automatically a causal propensity score.

## Search Outcomes

Measure query/session success, zero-result rate, reformulation, abandonment, latency, and conversion with explicit attribution windows. More clicks can mean more engagement or more difficulty finding an answer. Pair online measures with [[Search Evaluation]], [[Click Bias]], and [[AB Testing]].

## Query, Session, and User Rates Answer Different Questions

For a declared eligibility rule and observation window:

**Query success rate:**

$$
\mathrm{query\ success\ rate}=\frac{\text{successful eligible queries}}{\text{eligible queries}}
$$

**Session success rate:**

$$
\mathrm{session\ success\ rate}=\frac{\text{successful eligible sessions}}{\text{eligible sessions}}
$$

Define “success” independently of the arithmetic: a judged answer, an attributed purchase, or an explicit task-completion signal implies a different claim. A session with five failed reformulations followed by one successful query may count as one successful session but only one successful query out of six. Report effort signals such as reformulation as well as completion.

### A denominator can change the story

Variant A has 10 successful sessions out of 100; B has 12 out of 150. Success count rises by 20%, while the success rate falls from 10% to 8%, a decrease of 2 percentage points. Neither number alone explains why the population changed.

If the variants were not randomly assigned comparable populations, this is a descriptive comparison, not a causal effect. Even in a randomised test, check whether the treatment changed eligibility, session boundaries, or repeat-query behaviour before interpreting the rate.

## Write a Metric Contract

Record the event source, deduplication rule, identity boundary, eligibility, attribution window, late-event handling, and aggregation. For conversions, distinguish conversion after any search from conversion attributed to a particular search result. Keep bot/internal traffic rules stable across variants.

Use a small set of complementary measures: task success for the desired outcome, latency and errors for service guardrails, and reformulation or abandonment to diagnose effort. A click increase can accompany worse relevance if users need more attempts; [[Click Bias]] explains why observed behaviour also depends on exposure.

## Exercise

A starting cohort contributes 100 revenue units, expands by 20, contracts by 5, and loses 10.

NRR is 105%.

Adding 40 from new customers changes total revenue but not this cohort's NRR.

## References & Useful Links

- [Stripe subscription analytics](https://docs.stripe.com/billing/subscriptions/analytics) — Recurring revenue and cohort metrics.
- [Amplitude user identity](https://amplitude.com/docs/data/sources/instrument-track-unique-users) — Counting distinct users consistently.
