---
note_type: concept
search_stage: evaluation
---

# Click Bias

#search-eng

## Clicks Are Observations, Not Direct Relevance Labels

A click depends on relevance, exposure, position, presentation, and user behaviour. An unclicked document might never have been seen; a clicked document may disappoint the user. Training on these signals without accounting for the logging policy can reinforce the current ranking.

**Position bias** changes the chance of examination across ranks. **Trust bias** occurs when high placement influences perceived relevance. Snippets and competing results also affect choices. Neither click-through rate nor dwell time is a universal relevance label.

## A Simple Model

For intuition, suppose click probability at a position is examination probability times click probability given examination. An item with conditional click probability 0.5 gets expected click rates 0.4 at exposure 0.8 and 0.1 at exposure 0.2. The fourfold difference need not represent a relevance difference. Real behaviour need not satisfy this simple factorisation.

## What Helps

Editorial [[Judgement List|judgments]], carefully designed randomised exposure, and logged presentation information provide complementary evidence. Inverse propensity weighting can correct specific observation biases when propensities are valid and positive for the target comparisons. Small propensities cause high variance; clipping trades bias for stability. Weighting is not a blanket cure for every bias or missing variable.

Record displayed positions, candidate eligibility, experiment assignment, and relevant policy versions subject to privacy constraints. Evaluate assumptions before using clicks for [[Learning to Rank]] or [[Product Metrics]]. For comparing two rankers, [[Interleaving]] uses paired click preferences within one result list; it reduces between-user noise but still inherits these biases.

## Write the Assumptions Behind a Weighted Estimate

In a simplified position-based model, a click $C_i$ requires examination $O_i$ and an attractive result $A_i$.

Assume $P(O_i=1)=e_i>0$ and that examination is independent of attraction conditional on the modelled context.

Then $\mathbb E[C_i]=e_iP(A_i=1)$, so

$$
\mathbb E\left[\frac{C_i}{e_i}\right]=P(A_i=1).
$$

This illustrates why inverse propensity weighting can remove a specified observation effect.[^ips] It does not equate attraction with editorial relevance, correct all trust or presentation biases, or recover outcomes for items with zero exposure probability.

### See the variance cost of rare exposure

A clicked observation with examination propensity 0.5 receives weight 2; one with propensity 0.01 receives weight 100. A few rare observations can therefore dominate an estimate. Clipping the second propensity to 0.05 reduces its weight to 20 but changes the estimator and introduces bias.

Compare clipped and unclipped results, coverage, and uncertainty. Do not choose the clipping level merely because it gives the most favourable ranker comparison.

## Keep the Logging Policy Attached to the Data

Record what could have been displayed, what was displayed, position, presentation, and experiment assignment. An unexposed product and a displayed-but-unclicked product are different observations. Also identify the event being predicted: a click can lead to satisfaction, disappointment, or a later purchase.

For an offline counterfactual evaluation, the target policy must have adequate support in the logged policy and the propensity model must match the assignment or observation mechanism. A deterministic historical top ten usually provides no direct evidence about never-shown products. Complement behavioural analysis with independent relevance judgments and controlled experiments.

## Exercise

A document moves from rank five to rank one and its clicks double.

List evidence needed to distinguish relevance improvement from exposure effects.

Explain why non-exposed documents cannot automatically be treated as negatives.

## References & Useful Links

- [Interpreting clickthrough data](https://www.cs.cornell.edu/people/tj/publications/joachims_etal_05a.pdf) — Eye-tracking study and presentation biases.

[^ips]: [Joachims, Swaminathan, and Schnabel, Unbiased Learning-to-Rank with Biased Feedback](https://www.cs.cornell.edu/~adith/docs/UbLTR.pdf) — Propensity-weighted learning, observation assumptions, and clipping tradeoffs.
