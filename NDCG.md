# NDCG

#search-eng

## Overview

Normalised discounted cumulative gain measures the quality of a ranked list with graded relevance. It rewards useful documents near the top. Specify the cutoff $k$, grade rubric, gain function, and evaluation universe before comparing scores. [^1]

## Formula

For nonnegative relevance grades $r_i$, one common convention is:

$$DCG@k=\sum_{i=1}^{k}\frac{2^{r_i}-1}{\log_2(i+1)}$$

$$NDCG@k=\frac{DCG@k}{IDCG@k}$$

$IDCG$ is the DCG of the ideal ordering of the same evaluation universe at the same cutoff. Normalisation permits per-query comparison, but does not make different evaluation protocols interchangeable. [^1]

## Worked Example

Assume the judged universe has grades 3, 2, 0. A system returns grades `[2, 3, 0]`:

$$DCG@3=3+\frac{7}{\log_2 3}\approx7.4165$$

$$IDCG@3=7+\frac{3}{\log_2 3}\approx8.8928$$

Therefore $NDCG@3\approx0.8340$. Sorting the same documents ideally yields 1.

## Implementation and Interpretation

Scikit-learn's `ndcg_score` uses the supplied relevance values as gains directly. To reproduce the exponential convention above, supply gains $2^r-1$, not raw grades. Predictions determine ordering; they are not the relevance labels. [^2]

Keep an explicit policy for zero ideal gain, missing judgments, tied scores, and short lists. If ideal gain is zero, the ratio is undefined mathematically; a library or evaluation policy may return zero or exclude the query. Report that choice. [^2]

For end-to-end evaluation, do not build each system's ideal ranking only from the candidates that system retrieved. Doing so can hide retrieval misses. Use [[Search Evaluation]] to separate candidate coverage from ordering quality.

## Practice

Move grade 3 from rank 2 to rank 3 and recalculate. Explain why [[Kendall's Tau]] measures a different question.

## References & Useful Links

[^1]: [Evaluation of ranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Ranked relevance metrics and discounted gain.
[^2]: [Scikit-learn NDCG](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html) — Gain, tie, and zero-relevance conventions.
- [Real life NDCG notebook](https://softwaredoug.com/blog/2024/10/19/real-life-ndcg) — Original saved resource for additional exploration.
