# Score Normalization

#search-eng

## Overview

Scores from different retrievers and signals live on different scales: BM25 is unbounded, cosine similarity lies in $[-1,1]$, and popularity counts can span orders of magnitude. **Normalisation** rescales them so they can be combined. The result depends on which candidates are in the set, so the same item can receive a different normalised score for a different candidate pool.[^1]

Rank-based fusion avoids scale problems altogether; see [[Hybrid Retrieval]]. Use this note when you need to combine scores themselves.

## Techniques

For the scores $s_1,\dots,s_n$ of one signal within one query's candidates:

- **Min–max:** $\dfrac{s_i-\min s}{\max s-\min s}$. The top item gets 1 and the bottom gets 0; order is preserved.
- **Z-score:** $\dfrac{s_i-\bar s}{\sigma_s}$. Unbounded; below-mean items become negative.
- **L2:** $\dfrac{s_i}{\sqrt{\sum_j s_j^2}}$. Preserves score ratios; the top item is below 1 unless it is the only result.[^1]

Engines add their own edge-case rules. OpenSearch, for example, replaces a normalised 0 with 0.001, and its z-score handling collapses every below-mean score to that value.[^1] Check your engine's implementation before reasoning from the formula alone.

## Combining Normalised Signals

- **Weighted arithmetic mean:** $\sum_k w_k x_k$ with $\sum_k w_k=1$. OpenSearch also supports geometric and harmonic means.[^1]
- **Multiplicative boosts:** $\prod_k (1+w_k x_k)$. Each factor is at least 1 for non-negative $x_k$, so a zero feature is neutral rather than zeroing the score. Weights act as relative multipliers. This is a common hand-tuned pattern, not a learned model.
- **Learned models:** a [[Learning to Rank]] model can learn the combination, but its input features still need consistent scaling between training and serving; see [[Feature Scaling]].

## Worked Example

Three candidates with relevance $r=[0.92,0.80,0.40]$ and checkout counts $c=[10,200,50]$.

| | $r$ min–max | $c$ min–max | $0.7r+0.3c$ | $(1+4r)(1+c)$ |
|---|---|---|---|---|
| P1 | 1.000 | 0.000 | 0.700 | 5.000 |
| P2 | 0.769 | 1.000 | 0.838 | 8.154 |
| P3 | 0.000 | 0.211 | 0.063 | 1.211 |

Both blends rank P2, P1, P3. Weights are illustrative.

Now add P4 with $r=0.10$ and $c=20$. The relevance minimum moves, so P2's normalised relevance becomes 0.854 and P3's becomes 0.366, although neither item changed. P3's blended score rises from 0.063 to 0.319. Normalised values are properties of the candidate set, not of the item alone.

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

## Exercise

Find values for P4 that change the order of P1 and P2 under the additive blend. Then rank the same candidates with RRF over the relevance and checkout rankings, before and after adding P4, and explain which method was more sensitive.

## References & Useful Links

[^1]: [OpenSearch: Normalization processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/) — Min–max, L2, and z-score normalisation; combination techniques; edge cases; dependence on returned results.

- [Google Cloud: About hybrid search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search) — Dense and sparse distances are not directly comparable, motivating RRF. Accessed 23 September 2026.
