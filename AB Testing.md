---
note_type: concept
search_stage: experiments
---

# AB Testing

#search-eng

## Overview

An A/B test randomly assigns eligible experimental units to control and treatment to estimate the effect of a change. It can evaluate small or substantial changes if randomisation, exposure, measurement, and sample size support the question. Low activity can make useful conclusions slow or impractical; fast answers are not guaranteed. [^1]

## Design Before Launch

1. Define the decision and primary outcome, such as successful search sessions.
2. State the null and alternative hypotheses.
3. Choose the randomisation unit, eligibility rules, and stable exposure assignment.
4. Specify the minimum useful effect, significance level, statistical power, and planned duration.
5. Define guardrails, such as errors and [[Latency vs Throughput|tail latency]].
6. Validate logging and assignment before interpreting effects. [^1]

Statistical power is $1-\beta$: the probability of rejecting the null under a specified alternative.

The minimum detectable effect used for planning is not a promise about the realised lift.

## Illustrative Search Experiment

Compare an existing ranker with a new [[Search Ranking|reranker]]. Assign users consistently to variants. Measure a predefined search-success outcome, while checking latency and errors. Offline [[NDCG]] can motivate the experiment but does not establish user benefit.

## Work from the Experimental Unit

If users are randomised, repeated searches by one user are related observations. Treating every query as an independent person can understate uncertainty. Define whether the outcome is one binary result per user, successful sessions per user, or a ratio of totals; the analysis must match that choice.[^1]

For a deliberately simple example, let each independently assigned user have one binary outcome: at least one successful search within a fixed observation window.

With $x_A$ successes among $n_A$ control users and $x_B$ among $n_B$ treatment users:

**Control success rate:**

$$
\hat p_A=\frac{x_A}{n_A}
$$

**Treatment success rate:**

$$
\hat p_B=\frac{x_B}{n_B}
$$

**Absolute difference:**

$$
\hat\Delta=\hat p_B-\hat p_A.
$$

An approximate standard error for this difference is

$$
SE(\hat\Delta)=\sqrt{\frac{\hat p_A(1-\hat p_A)}{n_A}+\frac{\hat p_B(1-\hat p_B)}{n_B}}.
$$

With sufficiently large success and failure counts, a simple 95% interval is $\hat\Delta\pm1.96SE$.

This approximation assumes independent units and a fixed analysis; it is not a method for dependent query rows or repeated significance checks.

### Calculate the effect before opening the answer

Control has 2,000 successes among 10,000 users; treatment has 2,100 among 10,000. Calculate absolute lift, relative lift, and the approximate interval.

**1. Compare success rates.**

- Control: 20%.
- Treatment: 21%.

**2. Calculate the two forms of lift.**

Absolute lift is **1 percentage point**.

$$
\text{relative lift}=\frac{0.01}{0.20}=5\%
$$

**3. Calculate the approximate uncertainty interval.**

The standard error is approximately $0.005709$.

$$
0.01\pm1.96(0.005709)\approx[-0.00119,0.02119]
$$

That is **−0.12 to +2.12 percentage points**. These data remain compatible with a small loss as well as a useful gain.

Before interpreting this number, check that the observed allocation matches the planned allocation, eligibility was defined consistently, and missing outcomes were handled as specified.

A sample-ratio mismatch is a reason to investigate assignment or measurement.

It is not fixed by collecting more of the same flawed data.[^2]

## Interpreting Results

Inspect assignment problems, metric instrumentation, uncertainty, and differences across relevant segments before shipping. A positive aggregate can conceal regressions. Use the planned stopping rule and account for multiple comparisons rather than repeatedly looking for a significant number. [^2]

## Ethical and Product Concerns

Preserve the original concern about optimising engagement at users' expense: a higher click rate is not automatically improved user welfare. Choose outcomes and guardrails that reflect successful tasks and longer-term product goals rather than treating every extra interaction as a benefit.

## Related Notes

- [[P-Value]] and [[Confidence Interval]] — Evidence and uncertainty.
- [[Product Metrics]] — Business outcomes; definitions need their own review.
- [[Interleaving]] — A more sensitive paired comparison for rankers; complements rather than replaces A/B tests.
- [[Shadow Deployment]] — Compare a new version on mirrored traffic before exposing users.

## References & Useful Links

[^1]: [Microsoft Research: Pre-experiment practices](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) — Hypotheses, metrics, power, and experiment preparation.
[^2]: [Microsoft Research: Post-experiment practices](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/) — Validity checks and interpretation.
