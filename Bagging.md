---
aliases: ["Bootstrap Aggregation"]
tags:
  - "ds-foundations"
---

## Overview

Bagging (**B**ootstrap **Agg**regat**ing**) trains many copies of one learning algorithm, each on a different bootstrap sample of the training data, and combines their predictions. It is a model-averaging ensemble that makes predictions more stable and often more accurate. Averaging reduces the **variance** of an unstable model such as a deep decision tree, which helps against overfitting; it does little for a model's **bias**.[^sk-guide] See [[Bias-Variance Tradeoff]].

The earlier version of this note summarised the idea as "a suitably large number of uncorrelated errors average out to zero". That is the right intuition, with two corrections:

- The errors are not uncorrelated: every model sees overlapping samples from the same data, so their errors are positively correlated. The correlation sets a floor on how much averaging can help (see below).
- Only the variable part of the error averages away. A systematic error shared by all models remains.

## Two Stages

### 1. Bootstrapping

A bootstrap sample draws $n$ observations **with replacement** from a training set of $n$ observations. Some rows appear several times and others not at all.

In statistics, we learn about a population by taking a sample. The bootstrap goes one step further: it resamples the observed sample to estimate how much a statistic or model would vary across samples, and uses that to reason about the population. Bagging uses the same resampling to create deliberately different training sets.

### 2. Aggregating

Fit one model per bootstrap sample and combine them:

- **Regression:** average the predictions.
- **Classification:** take a majority vote, or average predicted class probabilities. Breiman's original procedure used a plurality vote for classes and an average for numbers.[^breiman-bag] scikit-learn's `BaggingClassifier` predicts the class with the highest mean predicted probability, and falls back to voting when the base estimator has no `predict_proba`.[^sk-api]

The models are independent of one another, so they can be trained in parallel. This distinguishes bagging from [[Boosting]], where each model depends on the previous ones.

## Why Averaging Helps, and Where It Stops

Suppose each of $B$ models has prediction variance $\sigma^2$ at a point, and each pair of models has correlation $\rho$. The variance of their average is

$$
\operatorname{Var}\!\left(\frac{1}{B}\sum_{b=1}^{B} \hat{f}_b\right) = \frac{1}{B^2}\left(B\sigma^2 + B(B-1)\rho\sigma^2\right) = \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2.
$$

The first expression counts $B$ variance terms and $B(B-1)$ covariance terms. As $B$ grows, the second term vanishes, but $\rho\sigma^2$ remains. Adding more models cannot remove it; only making the models less correlated can.

This is why [[Random Forest]] adds a random subset of features at each split on top of bagging: it lowers $\rho$ between trees.[^sk-guide]

## Worked Example

**Inputs:** each model has variance $\sigma^2 = 4$. Compare different correlations $\rho$ and ensemble sizes $B$.

**Step 1: moderately correlated models, $\rho = 0.5$, $B = 10$.**

$$
0.5 \times 4 + \frac{1 - 0.5}{10} \times 4 = 2 + 0.2 = 2.2
$$

**Step 2: same correlation, many more models, $B = 1000$.**

$$
0.5 \times 4 + \frac{0.5}{1000} \times 4 = 2 + 0.002 = 2.002
$$

**Step 3: uncorrelated models, $\rho = 0$, $B = 10$.**

$$
0 + \frac{1}{10} \times 4 = 0.4
$$

**Step 4: highly correlated models, $\rho = 0.9$, $B = 10$.**

$$
0.9 \times 4 + \frac{0.1}{10} \times 4 = 3.6 + 0.04 = 3.64
$$

Going from 10 to 1000 models barely helps once $\rho = 0.5$: the variance approaches the floor of 2. Reducing correlation matters far more. The uncorrelated case of 0.4 is the ideal that the original "errors average out" intuition describes. A simulation of 200,000 draws with $\rho = 0.5$ and $B = 10$ gave a variance of about 2.199, matching Step 1.

## Out-of-Bag Evaluation

The probability that a particular row is **not** drawn in one bootstrap sample of size $n$ is

$$
\left(1 - \frac{1}{n}\right)^n.
$$

**For $n = 10$:**

$$
0.9^{10} \approx 0.349
$$

**For $n = 1000$:**

$$
0.999^{1000} \approx 0.368
$$

**As $n \to \infty$:**

$$
\left(1 - \frac{1}{n}\right)^n \to e^{-1} \approx 0.368
$$

So each model trains on about 63.2% of the distinct rows and never sees the remaining 36.8%, the **out-of-bag (OOB)** rows, the figure quoted in [[Ensemble Learning]]. Predicting each row using only the models that did not train on it gives a built-in estimate of generalisation error (`oob_score=True` in scikit-learn).[^sk-api] Like any random row split, it is optimistic when rows are not independent, for example several rows from the same user, session, or query. See [[Data Leakage]] and [[Cross Validation]].

## Variants

scikit-learn groups several related methods under its bagging meta-estimator:[^sk-guide]

| Method | What is sampled |
|---|---|
| Pasting | Rows, without replacement |
| Bagging | Rows, with replacement |
| Random subspaces | Features |
| Random patches | Both rows and features |

## Python Example

Executed with scikit-learn 1.9.1.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=2000, n_features=20, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),  # fully grown trees: high variance
    n_estimators=200,
    bootstrap=True,
    oob_score=True,
    n_jobs=-1,
    random_state=0,
)
bagging.fit(X_train, y_train)
print("OOB accuracy:", bagging.oob_score_)
print("Test accuracy:", bagging.score(X_test, y_test))
```

The base-model parameter is `estimator`; it was called `base_estimator` before scikit-learn 1.2.[^sk-api] This run printed an OOB accuracy of 0.989 and a test accuracy of 0.976. The OOB figure is an estimate from the training rows, so the two need not match exactly.

## Limitations & Common Pitfalls

- **Stable models gain little.** Bagging works best with strong, complex models such as fully grown trees; boosting usually works best with weak models such as shallow trees.[^sk-guide] Bagging a linear regression mostly reproduces the same model. Breiman called instability "the vital element": trees, neural nets, and subset selection in linear regression are unstable and gain from bagging, whereas $k$-nearest neighbours is stable, and bagging can slightly degrade stable procedures.[^breiman-bag]
- **Bias is untouched.** If every model underfits, their average underfits too.
- **More models are not free.** Training and prediction cost grow linearly with $B$, while the variance gain flattens (Step 2). In Breiman's waveform experiment, a single tree misclassified 29.0% of test cases; bagging 10, 25, 50, and 100 trees gave 21.8%, 19.5%, 19.4%, and 19.4%.[^breiman-bag]
- **Interpretability.** An average of hundreds of trees cannot be read like a single tree; use permutation-based importance with care. See [[Feature Importance]].

## Exercise

A bagged ensemble of 500 deep trees has almost the same validation error as one with 100 trees, and both are only slightly better than a single tree. What does this suggest, and what would you try?

> [!example]- Exercise solution
> The ensemble has reached the correlation floor $\rho\sigma^2$: the trees make similar errors, so more trees do not help. Reduce correlation by sampling features (move to a [[Random Forest]], or set `max_features` below 1.0), or by using more diverse base models. If validation error is still high with low variance, the problem is bias: add better features or use a more flexible method such as [[Boosting]].

## Related Notes

- [[Random Forest]] — Bagging plus per-split feature sampling.
- [[Bagging Meta-Estimator]] — scikit-learn's general bagging wrapper.
- [[Ensemble Learning]] — Voting, averaging, stacking, bagging versus pasting.

## References & Useful Links

[^sk-guide]: [scikit-learn User Guide: Ensembles — Bagging meta-estimator and Random forests](https://scikit-learn.org/stable/modules/ensemble.html#bagging-meta-estimator) — Variance reduction, strong versus weak base models, pasting/bagging/random subspaces/random patches, and feature randomness in forests.
[^sk-api]: [scikit-learn `BaggingClassifier` API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html) — `estimator` (renamed from `base_estimator` in 1.2), `bootstrap`, `oob_score`, and probability-averaging prediction.

[^breiman-bag]: [Breiman, "Bagging Predictors", Technical Report No. 421, UC Berkeley Statistics, September 1994](https://www.stat.berkeley.edu/~breiman/bagging.pdf) — Full text read. Plurality vote and averaging, instability as the key condition, $k$-nearest neighbours as stable, 20–47% lower tree misclassification and 22–46% lower regression-tree MSE in its experiments, and the replicate-count table. scikit-learn cites the journal version, *Machine Learning* 24(2), 123–140 (1996).