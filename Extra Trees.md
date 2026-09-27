---
tags:
  - "ds-foundations"
---

## Overview

Extra Trees (Extremely Randomized Trees; Geurts, Ernst and Wehenkel, 2006) is a [[Random Forest]] with trees that are extremely randomized. A decision tree searches every threshold for the best value; Extra Trees draws thresholds **at random** for each candidate feature and keeps the best of those random splits.[^sk-forest] This usually reduces variance a bit more than a random forest, at the cost of a slightly larger increase in bias.

## How It Differs from a Random Forest

| | Random Forest | Extra Trees |
|---|---|---|
| Rows per tree | Bootstrap sample (`bootstrap=True`) | Whole training set (`bootstrap=False`) |
| Candidate features per split | Random subset | Random subset |
| Threshold per candidate feature | Best possible | One random draw |
| Split chosen | Best (feature, threshold) pair | Best among the random pairs |

The defaults in the first row come from scikit-learn's user guide.[^sk-forest] In scikit-learn a single `ExtraTreeClassifier` is a decision tree with `splitter="random"`, which samples one random threshold for each available feature.[^sk-tree]

## The Math, Step by Step

### 1. Random split at a node

For each of the $m$ candidate features $j$, with values in the node ranging from $a_j = \min x_j$ to $b_j = \max x_j$, draw one threshold:

$$
t_j \sim \text{Uniform}(a_j, b_j)
$$

This is the paper's `Pick_a_random_split` procedure. Candidate features are chosen only among features that are not constant in the node, and a node stops splitting when it has fewer than $n_{\min}$ rows or when its features or outputs are constant.[^geurts] In a scikit-learn 1.9.1 check with node values 0 and 10, 4,000 drawn thresholds had a mean of 5.02 and evenly spaced deciles, consistent with a uniform draw.

### 2. Pick the best random split

Score each $(j, t_j)$ with the usual impurity criterion from [[Decision Trees]] and keep

$$
\theta^{*} = \arg\min_{j} G\big(Q, (j, t_j)\big).
$$

### 3. Aggregate

Average the trees' predictions (class probabilities or values), exactly as in a random forest. The original paper used a majority vote for classification and an arithmetic mean for regression.[^geurts]

### 4. Why it lowers variance

The ensemble variance is $\rho\sigma^2 + \frac{1 - \rho}{B}\sigma^2$ (see [[Bagging]]). Random thresholds make trees less alike, so $\rho$ falls further. Each tree is also less tuned to the data, which is where the extra bias comes from.

### 5. Why it is faster

A best-split search sorts and scans all thresholds; a random split evaluates one threshold per candidate feature. The scikit-learn guide describes the random splitter as a stochastic approximation of the greedy search that reduces computation time.[^sk-tree] The paper notes that growing a balanced tree is still of order $N \log N$ in the sample size $N$, but with a much smaller constant than methods that optimise cut-points.[^geurts]

### 6. The paper's defaults

Geurts, Ernst and Wehenkel used $M = 100$ trees. They drew $K = \sqrt{n}$ features per split for classification (rounded) and $K = n$ for regression, where $n$ is the number of features. They set $n_{\min} = 2$ for classification (fully grown trees) and $n_{\min} = 5$ for regression.[^geurts] With $K = n$, the only randomness left is in the thresholds. They explain the choices directly: randomising both features and cut-points reduces variance more strongly, and using the full sample instead of bootstrap replicas minimises bias.[^geurts]

## What the Paper Found

Geurts et al. evaluated 24 datasets (12 classification, 12 regression) with $M = 100$ trees.[^geurts]

- **Speed.** In classification, Extra Trees training took on average 0.36 times as long as Random Forests and was about 10 times faster than tree bagging; in regression the ratio was 0.81. The gap grows with many features, because their Random Forest implementation pre-sorted every feature: on the largest dataset, Isolet, Extra Trees was more than 10 times faster.
- **Size.** Ensembles had 1.5 to 3 times as many leaves as Random Forests, but trees were on average no more than two levels deeper. The cost is mainly memory.
- **Bias and variance.** Among the ensembles compared, Extra Trees reduced variance the most and also raised bias the most. With the best $K$, variance fell by 95% on average relative to a single tree, while bias rose by 21%.
- **Why classification benefits more.** Misclassification error tolerates biased probability estimates better than squared error does. This is why randomised ensembles beat tree bagging clearly in classification but not in regression.
- **Bootstrap hurts.** Bootstrap sampling could make Extra Trees smaller and faster, as it does for Random Forests, but the authors found that it often reduced accuracy significantly.

### How $K$ and $n_{\min}$ behave

- **$K = 1$** gives *totally randomized trees*: features and thresholds are chosen without looking at the output. **$K = n$** randomises only thresholds.
- **Larger $K$** lowers bias and raises variance. With many irrelevant features, larger $K$ helps, because it gives the split search a chance to skip them.
- **Irrelevant features.** For totally randomized trees on Pumadyn-32nm, where 2 of 32 features carry over 95% of the information, removing the irrelevant features cut bias from 82.44 to 9.83. Variance rose only from 0.94 to 1.40.
- **$n_{\min}$.** Larger values give smaller, smoother trees. The noisier the output, the larger the best $n_{\min}$.

## Worked Example

**Inputs:** in one node, feature $x_1$ ranges from 0 to 10 and the classes separate cleanly at $x_1 = 4$. One random threshold is drawn, $t \sim \text{Uniform}(0, 10)$.

**Step 1: chance the random threshold lands within 1 unit of the ideal split.**

$$
P(3 \le t \le 5) = \frac{5 - 3}{10 - 0} = 0.2
$$

**Step 2: chance that at least one of 5 trees gets such a threshold at this node.**

$$
1 - 0.8^5 \approx 0.672
$$

A single extremely randomized tree usually misses the ideal threshold, which is the extra bias. Across many trees, thresholds scatter around the good region, and averaging smooths the decision boundary. That trade is worth making when variance, not bias, dominates the error.

## Python Example

Executed with scikit-learn 1.9.1 on the same synthetic data as the [[Random Forest]] example.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, n_features=10, n_informative=3,
                           n_redundant=0, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

et = ExtraTreesClassifier(n_estimators=300, n_jobs=-1, random_state=0).fit(X_train, y_train)
print(et.bootstrap, round(et.score(X_test, y_test), 3))  # False 0.906
```

Its accuracy (0.906) was close to the random forest's (0.904) on this data; one split of one synthetic dataset says nothing general about which method is better.

## Limitations & Common Pitfalls

- **No OOB score by default.** Without bootstrap sampling there are no out-of-bag rows; set `bootstrap=True` or use a validation set.
- **Noisy or irrelevant features hurt more.** Random thresholds on useless features waste splits; feature selection or a larger `max_features` helps, as the paper's irrelevant-feature experiments show.[^geurts]
- **Memory.** Extra Trees ensembles have more leaves than Random Forests on the same data.[^geurts]
- **Bias can dominate** on small or simple datasets where precise thresholds matter.

## Interview Questions

**What are the two random choices in Extra Trees?** The candidate features at each split (as in a random forest) and the threshold for each candidate feature.

**Why not bootstrap?** The random thresholds already make trees differ, so training each tree on all rows keeps bias lower without losing much diversity. The paper gives minimising bias as the reason for using the full sample.[^geurts]

**When would you pick Extra Trees over a random forest?** When training speed matters or the forest still overfits; compare both with cross-validation.

## Exercise

In the worked example, how many trees are needed for a 95% chance that at least one tree draws a threshold within $[3, 5]$ at that node?

> [!example]- Exercise solution
> **Inputs:** each tree lands in $[3, 5]$ with probability 0.2; we need $1 - 0.8^B \ge 0.95$.
>
> **Step 1: rearrange.**
>
> $$
> 0.8^B \le 0.05
> $$
>
> **Step 2: solve for $B$.**
>
> $$
> B \ge \frac{\ln 0.05}{\ln 0.8} \approx 13.4
> $$
>
> So 14 trees are enough at this one node; the default of 100 trees gives plenty of coverage.

## References & Useful Links

[^sk-forest]: [scikit-learn User Guide: Extremely Randomized Trees](https://scikit-learn.org/stable/modules/ensemble.html#extremely-randomized-trees) — Random thresholds, variance and bias trade-off, and `bootstrap=False` default; cites Geurts, Ernst and Wehenkel (2006).
[^sk-tree]: [scikit-learn User Guide: Decision Trees — Mathematical formulation](https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation) — `splitter="random"` samples one random threshold per available feature; `ExtraTreeClassifier` uses it by default.
[^geurts]: [Geurts, Ernst and Wehenkel (2006), "Extremely randomized trees", *Machine Learning*, DOI 10.1007/s10994-006-6226-1](https://orbi.uliege.be/bitstream/2268/9357/1/geurts-mlj-advance.pdf) — Author's copy of the paper; Sections 1 to 4 read, including the parameter and bias/variance studies. Section 2 covers the splitting algorithm with uniform cut-points in $[a_{\min}, a_{\max}]$, stopping rules, the full-sample rationale, $N \log N$ complexity, defaults, and timing and size tables. Sections 3 and 4 cover the effects of $K$, $n_{\min}$ and $M$, and the bias/variance analysis.
