# Kendall's Tau

#search-eng

## Overview

Kendall's tau measures ordinal association by comparing pairs of observations. A pair is concordant when its order agrees in both variables and discordant when it reverses. Rank agreement does not directly measure search relevance. [^1]

## Formula

With no ties:

$$\tau_a=\frac{C-D}{\binom n2}$$

Here $C$ and $D$ are concordant and discordant pair counts. For ties, a common correction is:

$$\tau_b=\frac{C-D}{\sqrt{(C+D+T)(C+D+U)}}$$

$T$ counts pairs tied only in the first variable, and $U$ only in the second. Pairs tied in both do not enter those counts. Degenerate inputs can make the denominator zero. [^1]

## Search Example

Two rankings of A, B, C are `[A,B,C]` and `[A,C,B]`. Two pairs agree and one disagrees, giving $\tau=1/3$.

This describes how much the order changed. It does not say which ranking is better; use judgments and [[NDCG]] for that. Compare the same item set and define how missing items are handled.

Pearson correlation does not require normal inputs merely to calculate its coefficient. There is also no universal rule that Kendall is more accurate than [[Spearman Correlation]] on small samples.

## References & Useful Links

[^1]: [SciPy kendalltau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html) — Concordance, ties, and tau variants.
