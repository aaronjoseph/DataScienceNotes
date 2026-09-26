---
note_type: concept
search_stage: evaluation
---

# NDCG

#search-eng

## Overview

Normalised discounted cumulative gain measures the quality of a ranked list with graded relevance.

It rewards useful documents near the top.

Specify the cutoff $k$, grade rubric, gain function, and evaluation universe before comparing scores. [^1]

## Formula

For nonnegative relevance grades $r_i$, one common convention is:

$$
DCG@k=\sum_{i=1}^{k}\frac{2^{r_i}-1}{\log_2(i+1)}
$$

$$
NDCG@k=\frac{DCG@k}{IDCG@k}
$$

$IDCG$ is the DCG of the ideal ordering of the same evaluation universe at the same cutoff.

Normalisation permits per-query comparison, but does not make different evaluation protocols interchangeable. [^1]

## Worked Example

Assume the judged universe has grades 3, 2, 0. A system returns grades `[2, 3, 0]`:

$$
DCG@3=3+\frac{7}{\log_2 3}\approx7.4165
$$

$$
IDCG@3=7+\frac{3}{\log_2 3}\approx8.8928
$$

Therefore $NDCG@3\approx0.8340$. Sorting the same documents ideally yields 1.

## Implementation and Interpretation

Scikit-learn's `ndcg_score` uses the supplied relevance values as gains directly.

To reproduce the exponential convention above, supply gains $2^r-1$, not raw grades.

Predictions determine ordering; they are not the relevance labels. [^2]

Keep an explicit policy for zero ideal gain, missing judgments, tied scores, and short lists. If ideal gain is zero, the ratio is undefined mathematically; a library or evaluation policy may return zero or exclude the query. Report that choice. [^2]

For end-to-end evaluation, do not build each system's ideal ranking only from the candidates that system retrieved. Doing so can hide retrieval misses. Use [[Search Evaluation]] to separate candidate coverage from ordering quality.

## Calculate It in a Reproducible Order

1. Select one fixed query and evaluation universe.
2. Convert its relevance grades to the chosen gains.
3. Read gains in the system's returned order, applying the short-list and missing-judgment policy.
4. Discount by rank and sum to the same cutoff $k$.
5. Sort the universe's gains ideally to obtain IDCG, then divide when IDCG is positive.

The score describes both the retrieved items and their positions relative to the defined ideal. It does not establish calibration, user satisfaction, or serving reliability.

> [!example]- Move the best item down one more position
> The original returned grades are `[2,3,0]`. Move grade 3 to rank 3 to obtain `[2,0,3]`.
>
> $$
> DCG@3=3+0+7/2=6.5.
> $$
>
> With the same ideal value $8.8928$, NDCG is about 0.7309.
>
> The candidate set is unchanged; the loss comes entirely from the worse ordering.
>
> Removing the grade-3 item altogether gives DCG 3 and NDCG about 0.3374 under the same universe.

## Grade Values Are a Modelling Choice

Under exponential gains, grades 3 and 2 become 7 and 3. Under linear gains they remain 3 and 2. That changes the cost of swapping them, so numerical NDCG values from the two protocols are not directly comparable. [[ESCI]] uses its own explicit gains rather than requiring exponential transformation.

When averaging across queries, disclose how zero-IDCG queries are handled and how many were affected. Tied model scores require a deterministic ordering or an evaluator that averages over ties. Different tie conventions can change a small benchmark even when the model outputs are identical.

## Practice

Move grade 3 from rank 2 to rank 3 and recalculate. Explain why [[Kendall's Tau]] measures a different question.

## References & Useful Links

[^1]: [Evaluation of ranked retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Ranked relevance metrics and discounted gain.
[^2]: [Scikit-learn NDCG](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html) — Gain, tie, and zero-relevance conventions.
- [Real life NDCG notebook](https://softwaredoug.com/blog/2024/10/19/real-life-ndcg) — Original saved resource for additional exploration.
