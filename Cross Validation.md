---
note_type: concept
search_stage: foundations
---

# Cross Validation

#search-eng

## Overview

Cross-validation evaluates a learning procedure across multiple training/validation splits. It estimates generalisation under the split assumptions; it does not guarantee absence of overfitting or leakage. [^1]

## K-Fold Procedure

Divide examples into $k$ folds.

For each fold, train on the others and evaluate on that fold.

Aggregate the validation results.

Fit all learned preprocessing inside each training fold.

See [[K Fold Cross Validation]] for split choices and computational cost.

## Choose the Split for the Task

- **Ordinary K-fold:** Appropriate when its exchangeability assumptions fit the data.
- **Stratified folds:** Preserve approximate class proportions; they do not solve group or time leakage.
- **Grouped folds:** Keep related examples, such as all rows for a held-out query, together.
- **Time-aware splits:** Evaluate on later data when the deployment question concerns the future. [^1]

Do not shuffle automatically. Scikit-learn's `KFold` and `StratifiedKFold` default to `shuffle=False`; specify it explicitly when shuffling is appropriate. [^1]

## Search Example

If ten rows belong to one query, distributing them over random folds can measure performance on already encountered query patterns.

Grouping by query asks a different question about unseen queries.

Neither split substitutes for describing the intended deployment.

## Average the Quantity You Mean to Estimate

For ranking, first compute a metric $m_q$ such as [[NDCG|NDCG@10]] for each held-out query.

If fold $j$ contains query set $Q_j$, its mean is $M_j$.

The macro average over all held-out queries is

$$
M=\frac{\sum_{j=1}^{k}|Q_j|M_j}{\sum_{j=1}^{k}|Q_j|}.
$$

Simply averaging fold means gives every fold equal weight. This matches the query macro average only when fold sizes are equal or their means happen to make the difference vanish. A traffic-weighted estimate needs explicit traffic weights instead. State how queries with undefined metrics are treated.

### Unequal folds

**Fold inputs**

- Fold 1: 2 queries, mean NDCG 0.90.
- Fold 2: 8 queries, mean NDCG 0.50.

**Equal weight per fold:**

$$
\frac{0.90+0.50}{2}=0.70
$$

**Equal weight per query:**

$$
\frac{2\times0.90+8\times0.50}{10}=0.58
$$

Now place all rows for a query into one fold. If product variants or near-duplicate queries also share information, decide whether those relationships require a broader grouping rule. A query identifier alone does not capture every dependency.

## Selection Adds Another Layer

Choosing the best configuration from these scores uses the validation folds for selection. Reporting that same winning score as an untouched final evaluation can be optimistic. Use a separate final holdout or nested validation when the goal is to evaluate the selection procedure; see [[Model Evaluation]].[^1]

The spread across fold scores describes variation across those splits.

Folds share much of their training data, so their scores are not independent experimental replicates.

Do not automatically turn their standard deviation divided by $\sqrt{k}$ into a confidence interval.

## Related Notes

- [[Model Evaluation]] — Selection versus final assessment.
- [[Data Leakage]] — Invalid features and preprocessing contamination.
- [[Stratified K Fold Cross Validation]] — Current pipeline example and limits of stratification.

## References & Useful Links

[^1]: [Scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — K-fold, grouping, stratification, and time-aware splitting.
