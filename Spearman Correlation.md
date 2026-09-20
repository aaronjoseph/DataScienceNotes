# Spearman Correlation

#search-eng

## Overview

Spearman correlation measures monotonic association by correlating ranks. Use average ranks for tied values. It ranges from -1 to 1 for nonconstant inputs; constant inputs make the coefficient undefined. [^1]

## Formula and Ties

With no ties, an equivalent shortcut is:

$$\rho=1-\frac{6\sum_i d_i^2}{n(n^2-1)}$$

$d_i$ is the difference between the two ranks for observation $i$. With ties, compute Pearson correlation on the assigned ranks instead of assuming the shortcut remains exact. [^1]

## Search Example

For the same three documents, ranks `[1,2,3]` and `[1,3,2]` give squared rank differences summing to 2, so $\rho=0.5$.

Like [[Kendall's Tau]], this measures agreement between orderings. Two equally poor search rankings can correlate perfectly. [[NDCG]] instead measures ordering against relevance grades.

## Practice

Construct a nonlinear but increasing relationship with perfect rank correlation. Explain why a zero coefficient need not imply statistical independence.

## References & Useful Links

[^1]: [SciPy spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) — Rank correlation, constant inputs, and significance-test limitations.
