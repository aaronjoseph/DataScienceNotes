---
note_type: concept
search_stage: ranking
---

# Score Normalization

#search-eng

## Overview

Scores from different retrievers and signals live on different scales: BM25 has no universal fixed range across queries and indexes, cosine similarity lies in $[-1,1]$, and popularity counts can span orders of magnitude. **Normalisation** rescales them so they can be combined.

The result depends on which candidates are in the set, so the same item can receive a different normalised score for a different candidate pool.[^1]

Rank-based fusion avoids scale problems altogether; see [[Hybrid Retrieval]]. Use this note when you need to combine scores themselves.

## Techniques

For the scores $s_1,\dots,s_n$ of one signal within one query's candidates:

**Min–max**

$$
\frac{s_i-\min s}{\max s-\min s}
$$

The top item gets 1 and the bottom gets 0; order is preserved for a nonzero range.

**Z-score**

$$
\frac{s_i-\bar s}{\sigma_s}
$$

Unbounded; below-mean items become negative when the standard deviation is nonzero.

**L2**

$$
\frac{s_i}{\sqrt{\sum_j s_j^2}}
$$

Preserves score ratios for a nonzero norm. With nonnegative scores, the top item is below 1 whenever another item has a nonzero score.[^1]

Engines add their own edge-case rules. OpenSearch, for example, replaces a normalised 0 with 0.001, and its z-score handling collapses every below-mean score to that value.[^1] Check your engine's implementation before reasoning from the formula alone.

## Combining Normalised Signals

**Weighted arithmetic mean**

$$
\sum_k w_k x_k
$$

The weights sum to 1. OpenSearch also supports geometric and harmonic means.[^1]

**Multiplicative boosts**

$$
\prod_k (1+w_k x_k)
$$

Each factor is at least 1 for nonnegative $x_k$ and $w_k$, so a zero feature is neutral rather than zeroing the score.

Weights act as relative multipliers. This is a common hand-tuned pattern, not a learned model.
- **Learned models:** a [[Learning to Rank]] model can learn the combination, but its input features still need consistent scaling between training and serving; see [[Feature Scaling]].

## Worked Example

Compare the same raw signals before and after adding one candidate.

Three candidates with relevance $r=[0.92,0.80,0.40]$ and checkout counts $c=[10,200,50]$.

| | $r$ min–max | $c$ min–max | $0.7r+0.3c$ | $(1+4r)(1+c)$ |
|---|---|---|---|---|
| P1 | 1.000 | 0.000 | 0.700 | 5.000 |
| P2 | 0.769 | 1.000 | 0.838 | 8.154 |
| P3 | 0.000 | 0.211 | 0.063 | 1.211 |

Both blends rank P2, P1, P3. Weights are illustrative.

Now add P4 with $r=0.10$ and $c=20$.

The relevance minimum moves, so P2's normalised relevance becomes 0.854 and P3's becomes 0.366, although neither item changed.

P3's blended score rises from 0.063 to 0.319.

Normalised values are properties of the candidate set, not of the item alone.

## Business Ordering

After scoring, product policy often imposes a **lexicographic** order: sort by the first key, then break ties by the next. One system sorts by order status (preorder, buyable, coming soon, sold out), condition, availability priority, then descending score, then marketplace rank.

```python
products = [
    {"sku": "B", "order_rank": 0, "condition_rank": 0, "availability_rank": 1, "score": 0.9},
    {"sku": "A", "order_rank": 0, "condition_rank": 0, "availability_rank": 1, "score": 0.9},
    {"sku": "C", "order_rank": 1, "condition_rank": 0, "availability_rank": 0, "score": 0.99},
]
products.sort(key=lambda p: (p["order_rank"], p["condition_rank"], p["availability_rank"], -p["score"], p["sku"]))
print([p["sku"] for p in products])  # ['A', 'B', 'C']
```

The final `sku` key makes the order total, so exact score ties do not depend on input order. C has the best score but a worse order status, so policy places it last. Stacked keys can override relevance completely; measure that effect rather than assuming it is small.

## Limitations and Pitfalls

- **Degenerate ranges:** with one candidate or identical scores, min–max divides by zero. Define the rule explicitly.
- **Outliers:** one extreme score compresses everyone else under min–max and distorts z-scores.
- **Which set?** Normalising before or after filtering produces different values. Record the choice.
- **Cross-query comparison:** per-query normalised scores are not comparable across queries; avoid global thresholds on them.
- **Hand-tuned weights** need validation against a [[Judgement List]] or an [[AB Testing|online test]].

## Normalisation Is Different from Calibration

Normalisation changes scale relative to a chosen population or candidate set. [[Probability Calibration]] asks whether predicted probabilities agree with observed event frequencies. Mapping the largest score in every query to 1 does not establish that its item is certainly relevant; even a poor candidate set has a maximum.

For the textbook formulas, define the set of scores, whether standard deviation uses a population or sample denominator, and the policy for all-equal or all-zero inputs. Missing source scores need a separate convention; an absent item is not automatically a measured score of zero.

> [!example]- Solve a candidate-pool change that reverses the leaders
> Add P4 with raw relevance 0.40 and checkout count 1000 to the original example. The relevance min and max stay unchanged, but the checkout range becomes $1000-10=990$.
>
> **P1:** the blended score remains 0.700.
>
> **P2:** recalculate using the new checkout range.
>
> $$
> 0.7\left(\frac{0.4}{0.52}\right)+0.3\left(\frac{190}{990}\right)\approx0.5960
> $$
>
> **P4:** the blended score is 0.300.
>
> P1 now outranks P2 even though neither P1 nor P2 changed. The new candidate changed the normalisation population.

## Treat Engine Edge Rules as Part of the Formula

The OpenSearch documentation checked on 26 September 2026 describes additional behaviour beyond textbook normalisation. Its min–max zero replacement can reorder extremely small positive scores, and its z-score processing has special handling at the mean as well as for negative values.[^1] Such rules can destroy an ordering property that the ideal mathematical transform has. Record the engine version and verify its actual output before relying on monotonicity.

For geometric or harmonic combinations, also establish the permitted score domain and treatment of zeros. Choosing a mean changes the tradeoff between signals; it is not merely a formatting operation on scores.

## Exercise

Find values for P4 that change the order of P1 and P2 under the additive blend.

Then rank the same candidates with RRF over the relevance and checkout rankings, before and after adding P4, and explain which method was more sensitive.

## References & Useful Links

[^1]: [OpenSearch: Normalization processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/) — Min–max, L2, and z-score normalisation; combination techniques; edge cases; dependence on returned results.

- [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Dense and sparse distances are not directly comparable, motivating RRF. Accessed 23 September 2026.
