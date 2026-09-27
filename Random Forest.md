---
tags:
  - "ds-foundations"
---

Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees. This approach enhances predictive accuracy and controls overfitting. Random Forest is [[Bagging|bagging]] of decision trees plus one extra source of randomness: a random subset of features at every split.[^sk-forest]

**Key Characteristics of Random Forest:**

1. **Ensemble Technique**: Combines the predictions of several decision trees to improve overall model performance.
2. **Random Sampling (Bagging)**: Each tree is trained on a random subset of the training data, selected with replacement (bootstrap sampling).
3. **Feature Randomness**: At each split in a tree, a random subset of features is considered, promoting diversity among trees and reducing correlation.

**How the Random Forest Algorithm Works:**
1. **Bootstrap Sampling**: From the original dataset containing _N_ instances, create _B_ bootstrap samples by randomly selecting _N_ instances with replacement.
2. **Tree Construction**: For each bootstrap sample, grow an unpruned decision tree:
	1. At each node, select _m_ features randomly from the total _M_ features (_m_ << _M_).
	2. Determine the best split among the _m_ features.
	3. Split the node into child nodes.
	4. Repeat until the maximum depth is reached or further splitting is not possible.
3. **Aggregation**:
	1. **For Classification**: Each tree votes for a class, and the class with the majority votes is the final prediction. This is Breiman's original rule: each tree casts a unit vote for the most popular class.[^breiman-rf] scikit-learn instead **averages the trees' predicted class probabilities** and picks the class with the highest mean.[^sk-forest]
	2. **For Regression**: The predictions from all trees are averaged to produce the final output.

## The Math, Step by Step

### 1. The ensemble prediction

With $B$ trees $\hat{f}_b$ trained on bootstrap samples:

$$
\hat{f}_{\text{RF}}(x) = \frac{1}{B} \sum_{b=1}^{B} \hat{f}_b(x)
$$

For classification in scikit-learn, $\hat{f}_b(x)$ is the tree's class-probability vector: the class fractions in the leaf that $x$ reaches.

### 2. Why averaging helps: the correlation floor

If each tree has variance $\sigma^2$ and each pair of trees has correlation $\rho$, then (derived in [[Bagging#Why Averaging Helps, and Where It Stops|Bagging]])

$$
\operatorname{Var}\left(\hat{f}_{\text{RF}}\right) = \rho\sigma^2 + \frac{1 - \rho}{B}\sigma^2.
$$

More trees remove the second term but not $\rho\sigma^2$. Bagging alone leaves trees correlated, because every tree tends to split first on the same strong features. Random feature subsets at each split lower $\rho$, and that is Random Forest's key addition.[^sk-forest]

### 3. How feature subsampling decorrelates trees

With $p$ features and $m$ considered per split, a particular feature is unavailable at a given split with probability

$$
P(\text{excluded}) = 1 - \frac{m}{p}.
$$

If only $k$ features are strong, the chance that none of them is a candidate is

$$
P(\text{no strong feature}) = \frac{\binom{p - k}{m}}{\binom{p}{m}}.
$$

### 4. Impurity-based importance (MDI)

scikit-learn's weighted impurity decrease for splitting node $t$ is[^sk-rf-api]

$$
\Delta I(t) = \frac{N_t}{N}\left( I(t) - \frac{N_{t_R}}{N_t} I(t_R) - \frac{N_{t_L}}{N_t} I(t_L) \right).
$$

A feature's mean decrease in impurity (MDI) sums $\Delta I$ over the splits that use it, averages across trees, and normalises to sum to 1.

### 5. Breiman's strength and correlation bound

Breiman analysed classification forests with the **margin**: how far the proportion of trees voting for the true class exceeds the largest proportion for any other class. The **strength** $s$ is the expected margin, and $\bar{\rho}$ is the mean correlation between trees' raw margins. Assuming $s > 0$, he proved[^breiman-rf]

$$
PE^{*} \le \frac{\bar{\rho}\,(1 - s^2)}{s^2},
$$

where $PE^{*}$ is the generalisation error. He called the bound likely to be loose, but it names the two levers: stronger individual trees and lower correlation between them. He also showed that, as trees are added, $PE^{*}$ converges almost surely to a limit, which is why adding trees does not overfit.[^breiman-rf]

A scikit-learn 1.9.1 check estimated both quantities on 2,000 held-out rows for a 300-tree binary forest. It found $s = 0.526$ and $\bar{\rho} = 0.194$, giving a bound of 0.508 against an actual majority-vote error of 0.102. The bound held, and it was loose, as Breiman expected.

## Worked Example

**Inputs:** $p = 16$ features, of which $k = 2$ are strongly predictive, and $m = \sqrt{16} = 4$ candidates per split (scikit-learn's classification default, `max_features="sqrt"`).[^sk-rf-api]

**Step 1: chance that one specific feature is excluded from a split.**

$$
1 - \frac{4}{16} = 0.75
$$

**Step 2: chance that neither strong feature is a candidate.**

$$
\frac{\binom{14}{4}}{\binom{16}{4}} = \frac{1001}{1820} = 0.55
$$

**Step 3: soft versus hard voting for one input.** Three trees give $P(\text{class 1}) = 0.9, 0.4, 0.45$.

$$
\text{mean probability} = \frac{0.9 + 0.4 + 0.45}{3} \approx 0.583
$$

Only one of the three trees votes for class 1.

In Step 2, over half of all splits must use a weaker feature. That feels wasteful for one tree, but it makes trees differ from one another, which lowers $\rho$ and the variance of the average. Step 3 shows why the aggregation rule matters: averaged probabilities predict class 1, whereas a majority vote predicts class 0, because the one confident tree outweighs two uncertain ones.

## Controls and Defaults

scikit-learn `RandomForestClassifier` defaults, checked 27 September 2026:[^sk-rf-api]

| Parameter | Default | Effect |
|---|---|---|
| `n_estimators` | 100 | More trees lower variance until the correlation floor; cost grows linearly |
| `max_features` | `"sqrt"` | Smaller values lower $\rho$ but raise bias |
| `max_depth` | `None` | Trees are grown until leaves are pure or tiny |
| `bootstrap` | `True` | Enables out-of-bag (OOB) evaluation with `oob_score=True` |
| `max_samples` | `None` | Bootstrap sample size; defaults to the full training size |

For regression, the guide notes `max_features=1.0` (all features) as an empirically good default; with 1.0 a random forest is just bagged trees.[^sk-forest]

Breiman's own experiments grew unpruned CART trees to maximum size and tried $F = 1$ and $F = \lfloor \log_2 M + 1 \rfloor$ features per split for $M$ inputs. The results were insensitive to $F$: the average absolute difference in error between the two settings was under 1%, and one or two features were usually near optimal.[^breiman-rf] About one-third of rows are out of bag for each tree. He reported that OOB estimates tend to overestimate the error until enough trees are grown, because each row is scored by only about a third of the forest.[^breiman-rf]

## Python Example

Executed with scikit-learn 1.9.1 on synthetic data with 3 informative features out of 10.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, n_features=10, n_informative=3,
                           n_redundant=0, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

rf = RandomForestClassifier(n_estimators=300, oob_score=True, n_jobs=-1, random_state=0)
rf.fit(X_train, y_train)
print(round(rf.oob_score_, 3), round(rf.score(X_test, y_test), 3))  # 0.911 0.904

mdi = rf.feature_importances_.argsort()[::-1][:3]
perm = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=0)
print(mdi, perm.importances_mean.argsort()[::-1][:3])  # [7 2 5] [2 7 5]
```

The OOB estimate (0.911) was close to the held-out accuracy (0.904). Both importance methods found the same top three features, but in a different order. The data are synthetic; these figures only show the workflow.

## Limitations & Common Pitfalls

- **MDI can mislead.** It is computed on training data and favours high-cardinality features; prefer permutation importance on held-out data.[^sk-forest] Breiman's original importance was itself permutation-based: permute one variable in each tree's out-of-bag rows and measure the rise in OOB error.[^breiman-rf] See [[Feature Importance]].
- **Not a black box, but not a single tree either.** Individual trees are readable; hundreds together are not.
- **No extrapolation.** Like any tree, predictions stay within the training target range.
- **Memory.** Fully grown trees can be very large; limit depth or leaf size when needed.[^sk-rf-api]
- **Determinism.** Features are randomly permuted at each split, so fix `random_state` for reproducible results.[^sk-rf-api]

## Interview Questions

**Bagging versus Random Forest?** Both train trees on bootstrap samples and average them. Random Forest also samples features at every split, which decorrelates the trees and lowers the variance floor $\rho\sigma^2$.

**Why use deep, unpruned trees?** Averaging reduces variance but not bias, so each tree should have low bias even if it overfits alone.

**Does adding more trees cause overfitting?** Not in the usual sense: Breiman proved that the forest's generalisation error converges to a limit as trees are added.[^breiman-rf] The error curve flattens instead of rising. More trees cost time and memory, and the individual trees can still overfit.

**Random Forest versus gradient boosting?** Forests average independent deep trees (variance reduction, parallel). Boosting adds shallow trees sequentially to reduce bias; see [[Boosting]] and [[XGBoost]].

## Exercise

With $p = 16$ and $k = 2$ strong features, how large must $m$ be for at least one strong feature to be available at 80% of splits?

> [!example]- Exercise solution
> **Inputs:** $p = 16$, $k = 2$; we need $\binom{14}{m} / \binom{16}{m} \le 0.2$.
>
> **Step 1: simplify the ratio.**
>
> $$
> \frac{\binom{14}{m}}{\binom{16}{m}} = \frac{(16 - m)(15 - m)}{16 \times 15}
> $$
>
> **Step 2: $m = 8$.**
>
> $$
> \frac{8 \times 7}{240} \approx 0.233
> $$
>
> **Step 3: $m = 9$.**
>
> $$
> \frac{7 \times 6}{240} = 0.175
> $$
>
> So $m = 9$ is the smallest value that works. That is well above the default of 4, and the trees would be much more alike.

## Related Notes

- [[Decision Trees]] — The base learner and its split criteria.
- [[Extra Trees]] — Random thresholds as well as random features.
- [[Bagging]] — Bootstrap sampling and out-of-bag evaluation.

## References & Useful Links

[^sk-forest]: [scikit-learn User Guide: Random forests and other randomized tree ensembles](https://scikit-learn.org/stable/modules/ensemble.html#random-forests-and-other-randomized-tree-ensembles) — Two sources of randomness and variance reduction, probability averaging versus voting, parameter guidance, and MDI caveats; cites Breiman (2001).
[^sk-rf-api]: [scikit-learn `RandomForestClassifier` API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) — Defaults, weighted impurity decrease formula, random permutation of features at each split, and memory notes.
[^breiman-rf]: [Breiman, "Random Forests", UC Berkeley Statistics technical report, January 2001](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf) — Full text read. Unit votes, convergence theorem, the strength and correlation bound, unpruned trees, the $F = 1$ and $\lfloor \log_2 M + 1 \rfloor$ settings, insensitivity to $F$, OOB estimates, and permutation-based variable importance.

