---
note_type: concept
search_stage: evaluation
---

# Annotation Agreement

#search-eng

## Purpose

Annotation agreement measures consistency between assessors applying a label scheme. It helps diagnose ambiguous instructions and difficult cases; agreement alone does not establish that labels are correct. Two people can share the same misconception.

## Raw Agreement and Cohen's Kappa

Raw agreement is the proportion of jointly labelled items with equal labels. For two assessors using the same categorical labels, Cohen's kappa adjusts for agreement expected from their marginal label frequencies:[^1]

**Expected agreement from the assessors' class marginals:**

$$
p_e=\sum_c p_A(c)p_B(c)
$$

**Cohen's kappa:**

$$
\kappa=\frac{p_o-p_e}{1-p_e}.
$$

$p_o$ is observed agreement.

If $p_e=1$, the denominator is zero and kappa is undefined.

Prevalence and marginal disagreement affect kappa; no single cutoff certifies a rubric.

Ordinal grades may justify weighted kappa, but the disagreement weights must be stated.

## Worked Example

This four-item example gives observed agreement 0.75 and kappa 0.5.

### Expand the dependency-free kappa calculation

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

## Read the Disagreement Table Before the Summary

**Observed agreement:** the two assessors agree on three of the four items.

$$
p_o=\frac{3}{4}=0.75
$$

**Marginals:** A marks half positive, while B marks one quarter positive.

The agreement expected from those marginals is

$$
p_e=(0.5)(0.25)+(0.5)(0.75)=0.5.
$$

**Calculate kappa:**

$$
\kappa=\frac{0.75-0.5}{1-0.5}=0.5.
$$

A confusion table reveals which boundary is unstable. A single agreement number can hide an important rare class: if almost every pair is Irrelevant, repeatedly predicting Irrelevant may create high raw agreement while providing little information about Exact matches.

### Diagnose a rubric, not just a rater

Suppose two assessors consistently agree on obvious boots and unrelated cleaners but disagree on colour mismatches. Review the colour requirement and examples first. If one assessor never sees colour metadata, the issue is the annotation interface. If both see it but interpret the rubric differently, revise the guidance and re-label a shared audit set.

Majority voting can reduce some individual noise, but shared missing context or a shared mistaken rule can make a unanimous answer wrong. Keep the adjudication rationale, not just the majority label.

## Match the Statistic to the Annotation Design

Cohen's kappa uses two raters and paired categorical labels. Weighted kappa requires an ordered label scale and explicit disagreement weights. ESCI categories are semantic classes, so treating their names as equally spaced ordinal values needs justification. With more raters or missing ratings, select a method that fits that design instead of dropping observations until the two-rater formula becomes convenient.

Repeat agreement analysis after rubric changes on a fresh shared sample. Report the sample size, label frequencies, and important disagreements; the goal is usable, well-defined judgments rather than meeting a universal cutoff.

## Exercise

Compare disagreement over grade 2 versus 3 with disagreement over relevant versus irrelevant.

Which matters for the decision you are evaluating?

Link [[Data Labeling]], [[Judgement List]], and [[NDCG]].

## References & Useful Links

[^1]: [Cohen kappa API and definition](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) — Marginal chance agreement and weighting.
