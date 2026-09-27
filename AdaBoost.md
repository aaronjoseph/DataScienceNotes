---
tags:
  - "ds-foundations"
---

### Main Concepts

Adaptive Boosting or AdaBoost (Freund and Schapire; extended abstract 1995, journal version 1997) is one of the simplest boosting algorithms.[^freund] Decision trees, usually one-split stumps, are fitted sequentially; each new stump is trained on reweighted data that emphasises the examples the previous ones got wrong. The final prediction is a weighted vote of all stumps.[^sk-guide]

Steps followed
1. Initially, all observation in the datasets are given equal weights
2. A decision stump is created [Decision Tree with one level]
	1. Here, each feature is runned through decision stump
	2. The decision stump with the lowest weighted impurity is selected (scikit-learn's default stump uses Gini on the weighted samples)
3. Subsequent calculations are made
	1. Total Error:

		$$
		\text{Total Error} = \frac{E}{T}
		$$

		1. Here, E is the number of errors made
		2. T refers to the total number of data points
		3. This is only true while all weights are equal. In general, Total Error is the **sum of the weights of the misclassified records**
	2. Performace of Stump:

		$$
		\text{Performance of Stump} = \frac{1}{2} \ln \frac{1 - \text{Total Error}}{\text{Total Error}}
		$$

	3. Using the above equations, weights are updated for each record. Here, the incorrect predictions should get the higher weights
		1. First is the updation cycle wherein the weights are updated as per the formulae, summation of all the weights will not be equal to 1
			1. Here, the incorrect predictions are assigned the new value = $OldWeight * e^{Performance of Stump}$
			2. Correct Prediction Records are updated with $OldWeight * e^{-Performance of Stump}$
		2. Next stage is to normalize, wherein the summation is taken for the records and is normalized accordingly
	4. Next step is to get a new distribution of data wherein there will be higher weightage given to the incorrectly classified data -> Since it has gotten higher weights
4. This step continoues sequentially and the above steps are repeated

> In Adaboost, decision trees are generally a node and two leaves. A decision tree of this kind is called a stump

## The Math, Step by Step

Binary labels are $y_i \in \{-1, +1\}$ and each weak learner outputs $h_t(x) \in \{-1, +1\}$.

### 1. Model

$$
F_T(x) = \sum_{t=1}^{T} \alpha_t h_t(x), \qquad \hat{y} = \operatorname{sign}\big(F_T(x)\big)
$$

### 2. Loss

AdaBoost can be derived as forward stage-wise minimisation of the exponential loss. This statistical view is due to Friedman, Hastie and Tibshirani (2000), as summarised by Zhu et al.:[^samme]

$$
L = \sum_{i=1}^{n} \exp\big(-y_i F(x_i)\big)
$$

Its population minimiser is half the log-odds:

$$
F^{*}(x) = \frac{1}{2} \log \frac{P(y = 1 \mid x)}{P(y = -1 \mid x)}
$$

That factor of one half is where the ½ in the classic $\alpha$ comes from.[^samme]

### 3. Weights come from the loss

After $t - 1$ rounds, adding $\alpha h$ gives

$$
L = \sum_i \underbrace{e^{-y_i F_{t-1}(x_i)}}_{w_i}\, e^{-\alpha y_i h(x_i)}.
$$

So the example weights $w_i$ are just the current exponential loss of each example: badly handled examples carry more weight.

### 4. Weighted error

With weights normalised to sum to 1,

$$
\varepsilon_t = \sum_{i:\ h_t(x_i) \ne y_i} w_i.
$$

### 5. Best learner weight (amount of say)

Splitting the loss into correct and incorrect examples gives:

$$
L = (1 - \varepsilon)e^{-\alpha} + \varepsilon e^{\alpha}
$$

Setting $dL/d\alpha = 0$:

$$
\alpha_t = \frac{1}{2} \ln \frac{1 - \varepsilon_t}{\varepsilon_t}
$$

This is the "Performance of Stump" formula above. It is positive when $\varepsilon_t < 0.5$, zero at 0.5 (a coin flip gets no say), and grows without bound as $\varepsilon_t \to 0$.

### 6. Weight update

$$
w_i \leftarrow \frac{w_i \exp\big(-\alpha_t y_i h_t(x_i)\big)}{Z_t}
$$

$Z_t$ normalises the weights to sum to 1. Misclassified examples ($y_i h_t(x_i) = -1$) are multiplied by $e^{\alpha_t}$; correct ones by $e^{-\alpha_t}$.

### 7. scikit-learn's convention (SAMME)

scikit-learn implements AdaBoost-SAMME (Zhu et al., 2009).[^sk-api] In a check with scikit-learn 1.9.1, the stored `estimator_weights_` matched

$$
\alpha_t = \eta \left[ \ln \frac{1 - \varepsilon_t}{\varepsilon_t} + \ln(K - 1) \right],
$$

with learning rate $\eta$ and $K$ classes. For $K = 2$ this is exactly twice the classic $\alpha$, and only misclassified examples are upweighted, by $e^{\alpha}$. After normalisation, both conventions give the same example weights and the same sign of $F$.

Zhu et al. explain the extra $\ln(K - 1)$ term.[^samme] Plain AdaBoost needs each learner's error below 0.5, or $\alpha$ turns negative. For $K > 2$ classes that is much harder than beating random guessing, whose accuracy is $1/K$. With the extra term, $\alpha > 0$ whenever accuracy exceeds $1/K$. The term also makes SAMME equivalent to forward stage-wise fitting with a multi-class exponential loss.

### 8. The original formulation and its error bound

Freund and Schapire used labels $y_i \in \{0, 1\}$ and set[^freund]

$$
\beta_t = \frac{\varepsilon_t}{1 - \varepsilon_t}.
$$

Correctly classified examples are multiplied by $\beta_t < 1$, misclassified ones are left unchanged, and the final vote gives $h_t$ the weight

$$
\ln \frac{1}{\beta_t} = \ln \frac{1 - \varepsilon_t}{\varepsilon_t}.
$$

After normalisation this is the same algorithm as SAMME with $K = 2$. They proved that the training error of the final vote is bounded by

$$
\varepsilon \le 2^{T} \prod_{t=1}^{T} \sqrt{\varepsilon_t (1 - \varepsilon_t)} \le \exp\left(-2 \sum_{t=1}^{T} \gamma_t^2\right), \qquad \varepsilon_t = \tfrac{1}{2} - \gamma_t.
$$

So if every learner is slightly better than chance, the training error falls exponentially in $T$.[^freund] For example, with $\varepsilon_t = 0.2$, each round contributes:

$$
2\sqrt{0.2 \times 0.8} = 0.8
$$

The bound after $T$ rounds is therefore:

$$
\varepsilon \le 0.8^{T}, \qquad 0.8^{10} \approx 0.107.
$$

The bound concerns training error only; it says nothing directly about test error.

In a scikit-learn 1.9.1 check on 600 synthetic rows, the bound held at every round checked. After 40 stumps the training error was 0.052 against a bound of 0.281, so the bound is valid but loose.

## Worked Example

**Inputs:** five examples with equal weights $w_i = 0.2$; the first stump misclassifies one example.

**Step 1: weighted error.**

$$
\varepsilon = 0.2
$$

**Step 2: amount of say (classic formula).**

$$
\alpha = \frac{1}{2} \ln \frac{0.8}{0.2} = \frac{1}{2} \ln 4 \approx 0.693
$$

**Step 3: unnormalised weights.**

$$
\text{misclassified: } 0.2\, e^{0.693} = 0.4, \qquad \text{correct: } 0.2\, e^{-0.693} = 0.1
$$

**Step 4: normalise.** The total weight is:

$$
0.4 + 4 \times 0.1 = 0.8
$$

Dividing each weight by the total:

$$
\text{misclassified: } \frac{0.4}{0.8} = 0.5, \qquad \text{correct: } \frac{0.1}{0.8} = 0.125
$$

**Step 5: SAMME convention.** $\alpha = \ln 4 \approx 1.386$ and only the error is upweighted: $0.2 \times 4 = 0.8$ against four weights of $0.2$, total 1.6.

$$
\text{misclassified: } \frac{0.8}{1.6} = 0.5, \qquad \text{correct: } \frac{0.2}{1.6} = 0.125
$$

The single mistake now carries half of the total weight, so the next stump is pushed hard to fix it. This is general: after each update, the misclassified examples always hold exactly 50% of the weight, which makes the last learner no better than chance on the new weights. Freund and Schapire note this property: for a two-valued $h_t$, the update exactly removes the advantage of the last hypothesis.[^freund] Both conventions give identical weights. scikit-learn 1.9.1 reported `estimator_weights_[0] = 1.386` for a first stump with error 0.2 on a toy dataset.

## Interview Questions

**Why does a stump with 50% error get zero weight?** $\ln(0.5/0.5) = 0$: it carries no information. A stump worse than 50% gets a negative weight, which flips its vote.

**Why is AdaBoost sensitive to outliers and label noise?** The exponential loss grows exponentially with the margin, so a mislabelled point gains weight every round and the ensemble keeps chasing it.

**How does AdaBoost relate to gradient boosting?** It is gradient boosting with exponential loss: the reweighting is the gradient signal. [[Gradient Boosting Machines (GBM)|Gradient boosting]] generalises this to any differentiable loss by fitting trees to negative gradients.

**What does `learning_rate` do?** It shrinks every $\alpha_t$; smaller values need more estimators but often generalise better.[^sk-api]

**Why does multi-class AdaBoost need SAMME?** Classic AdaBoost stops working once a learner's error exceeds 0.5, which is common with many classes. SAMME's $\ln(K - 1)$ term keeps $\alpha$ positive for any learner better than random guessing.[^samme]

## Exercise

A stump has weighted error $\varepsilon = 0.1$. Compute the classic $\alpha$ and the new weight share of the misclassified examples after normalisation.

> [!example]- Exercise solution
> **Inputs:** $\varepsilon = 0.1$, so misclassified examples hold 0.1 of the weight and correct ones 0.9.
>
> **Step 1: amount of say.**
>
> $$
> \alpha = \frac{1}{2}\ln\frac{0.9}{0.1} = \frac{1}{2}\ln 9 \approx 1.099
> $$
>
> **Step 2: unnormalised weights.**
>
> $$
> \text{misclassified: } 0.1\, e^{1.099} = 0.3, \qquad \text{correct: } 0.9\, e^{-1.099} = 0.3
> $$
>
> **Step 3: normalise** (total $0.3 + 0.3 = 0.6$).
>
> $$
> \frac{0.3}{0.6} = 0.5
> $$
>
> The misclassified examples again hold 50% of the weight, as always.

---
### Code

Executed with scikit-learn 1.9.1. The default base learner is a depth-one `DecisionTreeClassifier`, with 50 estimators and a learning rate of 1.0.[^sk-api]

```py
import numpy as np
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor

X = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = np.array([0, 0, 1, 1, 0])

clf = AdaBoostClassifier(n_estimators=2, random_state=0).fit(X, y)
print(clf.estimator_errors_)   # [0.2  0.25]
print(clf.estimator_weights_)  # [1.386 1.099], i.e. ln(4) and ln(3)
```

## References & Useful Links

[^sk-guide]: [scikit-learn User Guide: AdaBoost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost) — Sequential reweighting, weighted majority vote, stumps as default weak learners, SAMME for classification and AdaBoost.R2 for regression.
[^sk-api]: [scikit-learn `AdaBoostClassifier` API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html) — Defaults, `estimator` (renamed from `base_estimator` in 1.2), `learning_rate`, `estimator_weights_`, and the Zhu et al. (2009) SAMME reference.
[^freund]: [Freund and Schapire (1997), "A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting", *Journal of Computer and System Sciences* 55, 119–139](https://www.face-rec.org/algorithms/Boosting-Ensemble/decision-theoretic_generalization.pdf) — Introduction and Sections 4.1–4.2 read from a copy of the journal article; an extended abstract appeared at EuroCOLT in March 1995. Figure 2 (AdaBoost with $\beta_t$ and $\ln(1/\beta_t)$ vote weights), footnote 2 (the update removes the last hypothesis's advantage), and Theorem 6 (training-error bound).
[^samme]: [Zhu, Zou, Rosset and Hastie, "Multi-class AdaBoost", preprint dated 12 January 2006](https://hastie.su.domains/Papers/samme.pdf) — Section 1 and the start of Section 2 read. Algorithm 1 (AdaBoost), Algorithm 2 (SAMME), the $\ln(K - 1)$ term, and the exponential-loss view credited to Friedman, Hastie and Tibshirani (2000). scikit-learn cites the 2009 published version.
