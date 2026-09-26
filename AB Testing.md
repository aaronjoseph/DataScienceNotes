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

Statistical power is $1-\beta$: the probability of rejecting the null under a specified alternative. The minimum detectable effect used for planning is not a promise about the realised lift.

## Illustrative Search Experiment

Compare an existing ranker with a new [[Search Ranking|reranker]]. Assign users consistently to variants. Measure a predefined search-success outcome, while checking latency and errors. Offline [[NDCG]] can motivate the experiment but does not establish user benefit.

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
