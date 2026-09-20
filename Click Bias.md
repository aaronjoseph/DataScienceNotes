# Click Bias

#search-eng

## Clicks Are Observations, Not Direct Relevance Labels

A click depends on relevance, exposure, position, presentation, and user behaviour. An unclicked document might never have been seen; a clicked document may disappoint the user. Training on these signals without accounting for the logging policy can reinforce the current ranking.

**Position bias** changes the chance of examination across ranks. **Trust bias** occurs when high placement influences perceived relevance. Snippets and competing results also affect choices. Neither click-through rate nor dwell time is a universal relevance label.

## A Simple Model

For intuition, suppose click probability at a position is examination probability times click probability given examination. An item with conditional click probability 0.5 gets expected click rates 0.4 at exposure 0.8 and 0.1 at exposure 0.2. The fourfold difference need not represent a relevance difference. Real behaviour need not satisfy this simple factorisation.

## What Helps

Editorial [[Judgement List|judgments]], carefully designed randomised exposure, and logged presentation information provide complementary evidence. Inverse propensity weighting can correct specific observation biases when propensities are valid and positive for the target comparisons. Small propensities cause high variance; clipping trades bias for stability. Weighting is not a blanket cure for every bias or missing variable.

Record displayed positions, candidate eligibility, experiment assignment, and relevant policy versions subject to privacy constraints. Evaluate assumptions before using clicks for [[Learning to Rank]] or [[Product Metrics]].

## Exercise

A document moves from rank five to rank one and its clicks double. List evidence needed to distinguish relevance improvement from exposure effects. Explain why non-exposed documents cannot automatically be treated as negatives.

## References & Useful Links

- [Interpreting clickthrough data](https://www.cs.cornell.edu/people/tj/publications/joachims_etal_05a.pdf) — Eye-tracking study and presentation biases.
- [Unbiased learning to rank](https://www.cs.cornell.edu/~adith/docs/UbLTR.pdf) — Propensity-weighted learning and assumptions.
