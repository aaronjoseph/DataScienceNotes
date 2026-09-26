---
note_type: concept
search_stage: evaluation
---

# Model Evaluation

#search-eng

## Overview

Model evaluation estimates performance on the intended use case. Model selection compares configurations; algorithm selection compares modelling approaches. Keep the data used for those decisions distinct from the final assessment where possible. [^1]

## Working Procedure

1. Define the prediction task, population, and metric.
2. Choose a split matching the deployment question: new queries, future traffic, or unseen entities can require different splits.
3. Fit preprocessing and the model using training data only.
4. Use validation or [[Cross Validation]] to select configurations.
5. Evaluate the selected procedure on held-out data and report uncertainty and failure slices. [^1]

## Search Example

A random split of query–document rows can place the same query on both sides.

That may be appropriate for one question but does not establish generalisation to unseen queries.

Write down the generalisation claim before selecting the split.

A classifier's accuracy is not the same as a search system's ranked utility.

Use [[Search Evaluation]] and [[NDCG]] for search-specific protocols, alongside [[Latency vs Throughput]] and online outcomes where appropriate.

## Nested Validation: Evaluate the Selection Process

Nested validation separates the data used to choose a model from the data used to assess that choice.[^1]

1. Hold out one **outer** fold for assessment.
2. Within the remaining data, use **inner** folds to compare configurations, including fitted preprocessing.
3. Choose a configuration using only the inner results.
4. Refit it on all outer-training data and evaluate once on the outer holdout.
5. Repeat for each outer fold, then aggregate the held-out results using the intended evaluation unit.

Group and time boundaries must remain valid in both loops. The output estimates the performance of a selection procedure; different outer folds may select different configurations. After assessment, select and fit a deployment model using the planned development procedure, without turning the outer results into another unreported tuning loop.

### Count the fitting work

**Inputs**

- 5 outer folds.
- 3 inner folds.
- 4 candidate configurations.

**Inner-search fits:**

$$
5\times3\times4=60
$$

**Outer-fold refits:** one per outer fold, adding 5 fits.

$$
\text{total fits}=60+5=65
$$

A later final deployment fit is additional. This count excludes repeated seeds, calibration stages, and any extra searches.

## Compare Systems on the Same Evaluation Units

For two rankers evaluated on the same queries, define

**Difference for one query:**

$$
d_q=m_q(B)-m_q(A)
$$

**Mean difference across queries:**

$$
\bar d=\frac{1}{|Q|}\sum_{q\in Q}d_q.
$$

A paired bootstrap can resample complete query records and recompute $\bar d$, preserving A/B pairing.

If multiple queries belong to one dependent session or user, resample the appropriate larger group instead.

State the interval method and what sources of variation it covers; resampling a fixed judgment set does not capture unknown label errors or future traffic shifts.[^1]

For differences $(0.10,-0.05,0.00,0.15)$, the mean improvement is $0.05$.

The negative query remains useful evidence: inspect its intent, candidates, and labels before attributing the improvement to a general ranking principle.

Four queries are a teaching example, not a convincing product evaluation.

## Open Questions

- #TODO Apply the nested procedure and paired uncertainty analysis below to a concrete ranking dataset. Record the split groups, seeds, selected configurations, and query-level metric differences; the worked arithmetic is not an empirical evaluation.

## References & Useful Links

[^1]: [Raschka: Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning](https://arxiv.org/abs/1811.12808) — Original saved paper on evaluation methodology.
