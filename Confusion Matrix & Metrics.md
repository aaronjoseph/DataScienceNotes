# Confusion Matrix & Metrics

#search-eng

## Counts at a Chosen Threshold

For binary labels, scikit-learn uses rows for actual labels and columns for predictions. With label order `[0, 1]`, the matrix is `[[TN, FP], [FN, TP]]`. Decide what “positive” means before interpreting it.

| Metric | Formula |
|---|---|
| Precision | $TP/(TP+FP)$ |
| Recall / true-positive rate | $TP/(TP+FN)$ |
| Specificity / true-negative rate | $TN/(TN+FP)$ |
| False-positive rate | $FP/(FP+TN)$ |
| Accuracy | $(TP+TN)/(TP+TN+FP+FN)$ |
| $F_\beta$ | $(1+\beta^2)TP/[(1+\beta^2)TP+\beta^2FN+FP]$ |

$F_1$ weights precision and recall equally through their harmonic mean. Larger $\beta$ puts more weight on recall. Define behaviour for zero denominators rather than silently comparing incompatible conventions.

## Thresholds and Curves

Raising a score threshold makes predicted positives a subset of the previous set: FP and TP cannot increase, while FN cannot decrease. Recall cannot increase; precision can rise **or fall** depending on which examples are removed.

ROC plots TPR against **FPR**, not against $1-TPR$. AUC evaluates score ordering across thresholds; it is not classification accuracy. A value near 0.5 does not establish performance at every operating point. Inspect precision–recall and business costs when positives are rare. Neither false positives nor false negatives are universally more serious.

## Example

```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
actual = [0, 0, 1, 1, 1]
predicted = [0, 1, 0, 1, 1]
print(confusion_matrix(actual, predicted, labels=[0, 1]))  # [[1,1],[1,2]]
print(precision_score(actual, predicted), recall_score(actual, predicted),
      f1_score(actual, predicted))  # all 2/3
```

## Search Connection and Exercise

A result-level relevance classifier can use these counts, but a confusion matrix discards ordering. Use [[NDCG]] for graded rankings and [[Search Evaluation]] for query aggregation. Construct scores where increasing the threshold removes a true positive and lowers precision.

## Existing Illustrations

![[AUC_ROC.png]]

![[Confusion_Matrix.png]]

## References & Useful Links

- [Confusion matrix API](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) — Axis and label conventions.
- [ROC curve API](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html) — Threshold and curve definitions.
