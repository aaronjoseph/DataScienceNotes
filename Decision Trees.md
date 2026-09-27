---
tags:
  - "ds-foundations"
---

A decision tree predicts by asking a sequence of yes/no questions about the features, such as "is $x_j \le t$?", and returning the value stored in the leaf it reaches. It is a non-parametric model that approximates the target with a piecewise-constant function learned greedily from the data.[^sk-tree] It is also the building block of [[Random Forest]], [[Extra Trees]], and boosting methods such as [[Gradient Boosting Machines (GBM)|gradient boosting]] and [[XGBoost]].

### Why Decision Tree

Decision Trees are used for its simplistic nature. The end results can be presented visually due to its White Box nature and is also easy to construct a decision tree. It can handle both categorical and numerical data and works best for non-linear data. Recent scikit-learn versions also handle missing values natively when `splitter="best"`, by trying the missing rows on each side of every split.[^sk-tree] (scikit-learn's implementation does not yet accept categorical features directly; encode them first.) Decision Trees are versatile Machine Learning Algorithms that perform both [[Classification Algorithms|classification]] and [[Regression Algorithms|regression]] tasks and even multi-output tasks.

- Requirs less feature preparation such as - [[Feature Scaling]]
- Decision tree is `non-parametric`, meaning to say the number of parameters are not clear before the training
- Decision tree is prone to small variation in the dataset
	- So the main issue of tree-based method is noisy outcome, although on the flip side, it can capture complex structures. This can be overcome by averaging - wherein tree's can be grown with bootstrap samples and then average it out - which is what a [[Random Forest]] is
- Training in scikit-learn randomly permutes the features at each split. When several splits improve the criterion equally, different runs can pick different ones, so set `random_state` for reproducible trees.[^sk-rf]
- Decision trees are `White Box` in nature, as in we can uncover the decisions for the classification, incontrast [[Random Forest]] has more of a `Black Box` approach, as in we cannot make sense of what is happening inside
- Decision tree can also output the probabilities of the predicted values

---
##### Fixing Overfitting

Decision tree overfitting can be handled by 
- [[Decision Tree - Pruning]]
- [[Random Forest]]

---
### Sklearn Implementation

```py
# Classifier
from sklearn.tree import DecisionTreeClassifier
# Regressor
from sklearn.tree import DecisionTreeRegressor
```

```py
clf.predict_proba()
```

---
#### Important Terminology
 
- `Root Node` It represents the entire population or sample and this further gets divided into two or more homogeneous sets
- `Splitting` It is a process of dividing a node into two or more sub-nodes
- `Decision Node` When a sub-node splits into further sub-nodes, then it is called the decision node
- `Leaf/ Terminal Node` Node do not split is called Leaf or Terminal Node. A leaf is pure only if the tree was grown until no further split was possible; with limits such as `max_depth` it can contain several classes
- `Pruning` When we remove sub-nodes of a decision node, this process is called pruning, the opposite of this is splitting
- `Branch/Sub-Tree` A subsection of the entire tree is called branch or sub-tree
- `Parent and child node` A node, which is divided into sub-nodes is called a parent node of sub-nodes whereas sub-nodes are the child of a parent node

---
#### Types of Decision Trees

- `Categorical Variable Decision Tree` - Has a categorical target variable 
- `Continuous Variable Decision Tree` - Decision tree has a continuous target variable

---
#### Building Decision Tree
- In the beginning, the whole training set is considered as the root
- In ID3, feature values are preferred to be categorical, and continuous values are discretised before building the model. CART, which scikit-learn uses, instead splits continuous features at thresholds
- Records are distributed recursively on the basis of attribute values
- Order to placing attributes as root or internal node of the tree is done by using some statistical approach

##### Working of Decision Tree

Decision of making strategic splits heavily affects a tree's accuracy. The decision criteria are different for classification and regression trees. 

Decision tree makes use of multiple algorithm to decide to split a node into two or more sub-nodes. The creation of sub-nodes increases the homogeneity of resultant sub-nodes. In other words, the purity of the node increases with respect to the target variable. The decision tree splits the nodes on all available variables and then selects the split which results in the most homogeneous sub-nodes.

##### Algorithms used in Decision trees
- ID3 (Iterative Dichotomiser 3)
- C4.5 (Successor of ID3)
- CART (Classification And Regression Tree)
- CHAID (Chi-Square automatic interaction detection Peroms multi-level splits when computing classification trees)
- MARS (Multivariate Adaptive Regression Splines)

##### Working of ID3 (Iterative Dichotomiser)
1. Begins with original set S as the root node
2. On each iteration of the algorithm, it iterates through the very unused attribute of the set S and calculates Entropy (H) and Information Gain (IG) of the attribute
3. Selects the attribute which has the smallest entropy or largest information gain
4. The set S is then split by the selected attribute to produce a subset of the data
5. The algorithm continues to recur on each subset, considering only attributes never selected before

##### Working of CART
- Decision Tree uses CART Algorithm
	- `Classification And Regression Tree`, works by splitting the training set into two subsets using two values k and $t_k$, wherein it searches for (t,$t_k$) values which produces the purest subset
	- Once the CART algorithm has successfully split the training set in two, it splits the subsets using the same logic. It stops recusing after it reaches the maximum depth or cannot find a split that will reduce impurity
	- This is a greedy algorithm, it doesn't search for optimal solution, just searches for reasonable solution
	- Optimal tree is a NP-Complete problem

--- 
### Entropy or Gini Impurity

Entropy and Gini impurity calculates the impurity of a split in a decision tree

---

### [[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence|Entropy]]

Formulae:

$$
H(p) = -\sum_{i} p_i \log_2 p_i
$$

Split | Entropy Value
-------|-----------
Pure Split |  0
Two equally mixed classes | 1
$K$ equally mixed classes | $\log_2 K$

Hence, entropy has to be close to 0 when possible, when building the tree. With base-2 logarithms, entropy is at most 1 only for two classes. The base changes the scale but not which split wins; the impurities scikit-learn reported in the worked example below match base 2.

---
##### Gini Impurity

A node is pure if all training instances it applies to belong to the same class.

$$
G_i = 1 - \sum_{k=1}^{n} P_{i,k}^2
$$

CART uses Gini indexmethod to create split
Also, Gini Impurity is computationally less expensive

---
#### Information Gain 

Decision trees are constructed based on the Information Gain value. Decision tree will always try to maximise the Information Gain

IG is a statistical property that measures how well a given attribute separates the training examples according to target classification.

`Formulae` = Entropy of Parent Node - weighted sum of entropy of the node below the parent node

> In essence, we will try to maximise on Information Gain and minimize of Entropy

---
##### Reduction in Variance

`Reduction in variance` is used for continuous target variables - Regression. The algorithm uses the standard formula of variance to choose the best split. The split with lower variance is selected as the criteria to split the population. See [[Decision Tree Regressor]] for the formula and a worked example.

---

[[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence]]

##### Entropy or Gini?
- Not much of a difference here in practice: the two criteria usually produce similar trees. Gini is slightly cheaper to compute, since entropy uses `Log in its formulae` while Gini doesn't
- Gini tends to isolate freqeunt class in its own branch of tree, while entropy tends to produce slightly more balanced trees

---
### Decision Tree for Numerical Features

The steps for numerical features are 
- Sorting all the values (Values are sorted)
- Defining a threshold Value
	- This threshold value will split the target features based on the threshold value, threshold can be values in the feature, wherein it can start from the smaller values and build up to larger values
	- Also, the Decision tree will calculate the Entropy and Information gain
	- One with the optimal values will be used to construct the decision tree
- `Time Complexity` - Time complexity will increase with increasing size of the data size: sorting each feature makes training about $O(n_{\text{features}}\, n_{\text{samples}} \log n_{\text{samples}})$ (see [[#6. Cost]])

---

### Plotting the tree

```py
import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(15,10))
tree.plot_tree(clf,filled=True)
```

## The Math, Step by Step

This follows scikit-learn's formulation of CART.[^sk-tree]

### 1. Candidate splits

Node $m$ holds $n_m$ samples $Q_m$. A candidate split $\theta = (j, t_m)$ uses feature $j$ and threshold $t_m$:

$$
Q_m^{\text{left}}(\theta) = \{(x, y) \mid x_j \le t_m\}, \qquad Q_m^{\text{right}}(\theta) = Q_m \setminus Q_m^{\text{left}}(\theta)
$$

With the default `splitter="best"`, thresholds are the midpoints between sorted, distinct feature values.

### 2. Class proportions

$$
p_{mk} = \frac{1}{n_m} \sum_{y \in Q_m} \mathbf{1}(y = k)
$$

In a leaf, `predict_proba` returns these proportions and `predict` returns the most frequent class.

### 3. Impurity measures

$$
\text{Gini: } H(Q_m) = \sum_k p_{mk}(1 - p_{mk}) = 1 - \sum_k p_{mk}^2
$$

$$
\text{Entropy: } H(Q_m) = -\sum_k p_{mk} \log p_{mk}
$$

Both are 0 for a pure node. With $K$ equally mixed classes, Gini reaches $1 - 1/K$ and base-2 entropy reaches $\log_2 K$.

### 4. Split objective

$$
G(Q_m, \theta) = \frac{n_m^{\text{left}}}{n_m} H\big(Q_m^{\text{left}}(\theta)\big) + \frac{n_m^{\text{right}}}{n_m} H\big(Q_m^{\text{right}}(\theta)\big)
$$

$$
\theta^{*} = \arg\min_{\theta} G(Q_m, \theta)
$$

Minimising $G$ is the same as maximising the impurity decrease $H(Q_m) - G(Q_m, \theta)$. With entropy, that decrease is the **information gain** described above.

### 5. Recursion and stopping

Apply the same search to each child until a stopping condition holds: `max_depth` is reached, a node has fewer than `min_samples_split` samples, or the best decrease is below `min_impurity_decrease`.[^sk-tree]

### 6. Cost

Training a balanced tree costs about $O(n_{\text{features}}\, n_{\text{samples}} \log n_{\text{samples}})$; prediction costs $O(\text{depth})$, about $O(\log n_{\text{samples}})$ for a balanced tree.[^sk-tree]

## Worked Example: Gini and Entropy for One Split

**Inputs:** a node with 10 samples, 6 positive and 4 negative. A candidate split sends 4 samples (all positive) left and 6 samples (2 positive, 4 negative) right.

**Step 1: parent impurity.**

$$
\text{Gini} = 1 - (0.6^2 + 0.4^2) = 0.48
$$

$$
\text{Entropy} = -0.6 \log_2 0.6 - 0.4 \log_2 0.4 \approx 0.971
$$

**Step 2: left child (pure).**

$$
\text{Gini} = 0, \qquad \text{Entropy} = 0
$$

**Step 3: right child** with proportions $1/3$ and $2/3$.

$$
\text{Gini} = 1 - \left(\tfrac{1}{9} + \tfrac{4}{9}\right) \approx 0.444
$$

$$
\text{Entropy} = -\tfrac{1}{3}\log_2 \tfrac{1}{3} - \tfrac{2}{3}\log_2 \tfrac{2}{3} \approx 0.918
$$

**Step 4: weighted child impurity.**

$$
G_{\text{Gini}} = 0.4 \times 0 + 0.6 \times 0.444 \approx 0.267, \qquad G_{\text{Entropy}} = 0.6 \times 0.918 \approx 0.551
$$

**Step 5: impurity decrease.**

$$
\Delta_{\text{Gini}} = 0.48 - 0.267 \approx 0.213, \qquad \text{IG} = 0.971 - 0.551 \approx 0.420
$$

The split isolates a pure group of positives and leaves a smaller mixed group, so both criteria improve. The two scales differ, but both rank this split the same way against the alternatives on this data. scikit-learn 1.9.1, on 10 ordered samples arranged this way, chose the same split for both criteria and reported root and child impurities of $[0.48, 0, 0.444]$ for Gini and $[0.971, 0, 0.918]$ for entropy.

## Controls

| Parameter | Effect |
|---|---|
| `criterion` | `gini` (default), `entropy` or `log_loss` for classification; `squared_error` and others for regression |
| `max_depth` | Caps the number of questions; the main guard against overfitting |
| `min_samples_split`, `min_samples_leaf` | Require enough samples for a split or a leaf; `min_samples_leaf=5` is a suggested starting point, though 1 is often best for classification with few classes |
| `min_impurity_decrease` | Skip splits whose weighted impurity decrease is too small |
| `ccp_alpha` | Post-pruning strength; see [[Decision Tree - Pruning]] |
| `class_weight` | Counter class imbalance, which otherwise biases trees towards dominant classes |

The tips on `max_depth=3` as a first depth, `min_samples_leaf=5`, and balancing classes come from scikit-learn's practical guidance.[^sk-tree]

## Limitations & Common Pitfalls

- **Overfitting.** Deep trees memorise the training data; control depth and leaf size or prune.
- **Instability.** Small data changes can produce a completely different tree; ensembles reduce this.[^sk-tree]
- **No extrapolation and no smoothness.** Predictions are piecewise constant.
- **Greedy search.** Learning an optimal tree is NP-complete, so each split is only locally optimal. Patterns such as XOR, where no single split helps, are hard to learn.[^sk-tree]
- **Axis-aligned splits.** A diagonal boundary needs many small steps; feature engineering or rotation can help.

## Interview Questions

**How does a tree choose a split?** It tries every feature and candidate threshold and picks the one that minimises the size-weighted impurity of the two children.

**Gini or entropy?** They usually give similar trees. Gini avoids logarithms, so it is slightly cheaper; entropy has an information-theory interpretation as information gain.

**Why are decision trees high variance?** Each split depends on the samples in the node, and errors near the root change everything below. Averaging many trees ([[Random Forest]]) or pruning reduces variance.

**Do trees need feature scaling?** No. Splits compare a single feature to a threshold, so any monotonic rescaling leaves the tree unchanged; see [[Feature Scaling]].

**How is feature importance computed?** By summing the weighted impurity decrease of every split that uses a feature (mean decrease in impurity). It is biased towards high-cardinality features; permutation importance is an alternative.

## Exercise

A node has 8 samples, 4 of each class. Split A gives children $(4, 0)$ and $(0, 4)$; split B gives $(3, 1)$ and $(1, 3)$. Compute the Gini decrease for each.

> [!example]- Exercise solution
> **Inputs:** a parent with 4 samples of each class; split A gives $(4, 0)$ and $(0, 4)$, split B gives $(3, 1)$ and $(1, 3)$.
>
> **Step 1: parent Gini.**
>
> $$
> 1 - (0.5^2 + 0.5^2) = 0.5
> $$
>
> **Step 2: split A.** Both children are pure.
>
> $$
> G_A = 0, \qquad \Delta_A = 0.5 - 0 = 0.5
> $$
>
> **Step 3: split B, each child.**
>
> $$
> 1 - (0.75^2 + 0.25^2) = 0.375
> $$
>
> **Step 4: split B, weighted and decrease.**
>
> $$
> G_B = 0.5 \times 0.375 + 0.5 \times 0.375 = 0.375, \qquad \Delta_B = 0.5 - 0.375 = 0.125
> $$
>
> Split A removes all impurity, so it is chosen.

## References & Useful Links

[^sk-tree]: [scikit-learn User Guide: Decision Trees](https://scikit-learn.org/stable/modules/tree.html) — Advantages and disadvantages, complexity, practical tips, CART formulation, classification and regression criteria, missing-value support, and cost-complexity pruning.
[^sk-rf]: [scikit-learn `RandomForestClassifier` API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) — Notes that features are always randomly permuted at each split, so ties can change the chosen split unless `random_state` is fixed.


