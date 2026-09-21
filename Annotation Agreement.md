# Annotation Agreement

#search-eng

## Purpose

Annotation agreement measures consistency between assessors applying a label scheme. It helps diagnose ambiguous instructions and difficult cases; agreement alone does not establish that labels are correct. Two people can share the same misconception.

## Raw Agreement and Cohen's Kappa

Raw agreement is the proportion of jointly labelled items with equal labels. For two assessors using the same categorical labels, Cohen's kappa adjusts for agreement expected from their marginal label frequencies:[^1]

$$\kappa=\frac{p_o-p_e}{1-p_e},\qquad p_e=\sum_c p_A(c)p_B(c).$$

$p_o$ is observed agreement. If $p_e=1$, the denominator is zero and kappa is undefined. Prevalence and marginal disagreement affect kappa; no single cutoff certifies a rubric. Ordinal grades may justify weighted kappa, but the disagreement weights must be stated.

## Worked Example

```python
from collections import Counter
A = [1, 1, 0, 0]
B = [1, 0, 0, 0]
n = len(A)
observed = sum(a == b for a, b in zip(A, B)) / n
ca, cb = Counter(A), Counter(B)
expected = sum(ca[c] * cb[c] for c in set(A) | set(B)) / n**2
kappa = (observed - expected) / (1 - expected)
assert observed == 0.75
assert expected == 0.5
assert kappa == 0.5
```

This tiny example illustrates arithmetic, not a reliable estimate for a production labelling team.

## Suggested Search Workflow

Have assessors independently label shared query–document pairs before adjudication. Report raw counts and disagreements by grade or query type. Discuss disagreements, improve the rubric, and retain original labels plus the adjudicated result. Measuring only post-adjudication agreement hides the original difficulty.

Do not use Cohen's two-assessor formula indiscriminately for many assessors or missing ratings. Choose a statistic suited to the design and record the rationale.

## Exercise

Compare disagreement over grade 2 versus 3 with disagreement over relevant versus irrelevant. Which matters for the decision you are evaluating? Link [[Data Labeling]], [[Judgement List]], and [[NDCG]].

## References & Useful Links

[^1]: [Cohen kappa API and definition](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) — Marginal chance agreement and weighting.
