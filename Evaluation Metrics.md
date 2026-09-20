# Evaluation Metrics

#search-eng #dl

## Choose the Quantity Before the Model

A training loss guides optimisation; an evaluation metric measures a chosen outcome. They may coincide, but lowering log loss does not guarantee higher accuracy, and lowering a document loss does not guarantee better [[NDCG]]. Specify labels, aggregation, sample weights, cutoff, and treatment of missing judgments.

## Classification

Accuracy is the fraction of correct labels. Macro averaging gives classes equal weight; weighted averaging uses class support; micro averaging pools counts. Use [[Confusion Matrix & Metrics]] to understand errors, especially with imbalance.

For binary labels $y_i\in\{0,1\}$ and predicted positive probabilities $p_i$:

$$L_{\log}=-\frac1n\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)].$$

For labels $y_i\in\{-1,+1\}$ and decision scores $f_i$, hinge loss is $\frac1n\sum_i\max(0,1-y_if_i)$. Scores are not necessarily calibrated probabilities.

## Regression

Let $e_i=y_i-\hat y_i$.

| Measure | Formula | Interpretation or pitfall |
|---|---|---|
| MAE | $\frac1n\sum_i\lvert e_i\rvert$ | Same units as target |
| MSE | $\frac1n\sum_i e_i^2$ | Squared units; emphasises large errors |
| RMSE | $\sqrt{\mathrm{MSE}}$ | Same units as target |
| MAPE | $\frac{100}{n}\sum_i\lvert e_i/y_i\rvert$ | Undefined at zero; unstable near zero |
| MSLE | $\frac1n\sum_i(\log(1+y_i)-\log(1+\hat y_i))^2$ | Nonnegative inputs; compares on a log scale |
| $R^2$ | $1-\frac{\sum_i e_i^2}{\sum_i(y_i-\bar y)^2}$ | Can be negative; constant targets need special handling |

MSLE is not a general instruction to prefer underprediction. Adjusted $R^2=1-(1-R^2)(n-1)/(n-p-1)$ is associated with regression using $p$ predictors and requires $n>p+1$; it is not a universal model-selection score.

## Search and Exercise

For targets `[1, 3]` and predictions `[2, 1]`, MAE is 1.5, MSE is 2.5, RMSE is about 1.581, and $R^2=-1.5$. A negative value is possible because prediction is worse than the sample-mean baseline by squared error.

Evaluate candidate coverage separately from ordering in [[Search Evaluation]]. Compare query-average and traffic-weighted results explicitly. Keep an untouched test set as described in [[Model Evaluation]].

## References & Useful Links

- [Scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) — Metric definitions, averaging, and edge cases.

Previously saved resources (retained for further reading; not used to verify this revision):
- [towardsdatascience.com — metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234](https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234)
- [towardsdatascience.com — your-ultimate-data-science-statistics-mathematics-cheat-sheet-d688a48ad3db](https://towardsdatascience.com/your-ultimate-data-science-statistics-mathematics-cheat-sheet-d688a48ad3db)
