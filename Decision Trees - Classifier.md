### Why Decision Tree

Decision Trees are used for its simplistic nature. The end results can be presented visually due to its White Box nature and is also easy to construct a decision tree. It can handle both categorical and numerical data and works best for non-linear data + handles missing data quite well.Decision Trees are versatile Machine Learning Algorithms that perform both [[Classification Algorithms|classification]] and [[Regression Algorithms|regression]] tasks and even multi-output tasks.

- Requirs less feature preparation such as - [[Feature Scaling]]
- Decision tree is `non-parametric`, meaning to say the number of parameters are not clear before the training
- Decision tree is prone to small variation in the dataset
- Training Algorithm used in Scikit-learn is stocastic, you will get different results on the same training data
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
- `Leaf/ Terminal Node` Node do not split is called Leaf or Terminal Node, here the split of values are pure
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
- Feature values are preferred to be categorical, if the values are continous then they are discretized prior to building the model
- Records are distributed recursively on the basis of attribute values
- Order to placing attributes as root or internal node of the tree is done by using some statistical approach

##### Working of Decision Tree

Decision of making strategic splits heavily affects a tree's accuracy. The decision criteria are different for classification and regression trees. 

Decision tree makes use of multiple algorithm to decide to split a node into two or more sub-nodes. The creation of sub-nodes increases the homogeneity of resultant sub-nodes. In other words, the purity of the node increases with respect to the target variable. The decision tree splits the nodes on all available variables and then selects the split which results in the most homogeneous sub-nodes.

##### Algorithms used in Decision trees
- ID3 (Extension of D3)
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

Formulae $H(p)=-\sum_{i}p_ilog_2(p_i)$

Split | Entropy Value
-------|-----------
Pure Split |  0
Impure Split | 1

Hence, entropy has to be close to 0 when possible, when building the tree

---
##### Gini Impurity

A node is pure if all training instances it applies to belong to the same class.

$G_i=1-\sum_{k=1}^{n}P_{i,k}^2$

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

`Reduction in variance` is used for continuous target variables - Regression. The algorithm uses the standard formula of variance to choose the best split. The split with lower variance is selected as the criteria to split the population

---

[[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence]]

##### Entropy or Gini?
- Not much of a difference here, Gini should be preferred, it is slightly faster, Entropy uses `Log in its formulae` while Gini doesn't which speeds up the calculation
- Gini tends to isolate freqeunt class in its own branch of tree, while entropy tends to produce slightly more balanced trees

---
### Decision Tree for Numerical Features

The steps for numerical features are 
- Sorting all the values (Values are sorted)
- Defining a threshold Value
	- This threshold value will split the target features based on the threshold value, threshold can be values in the feature, wherein it can start from the smaller values and build up to larger values
	- Also, the Decision tree will calculate the Entropy and Information gain
	- One with the optimal values will be used to construct the decision tree
- `Time Complexity` - Time complexity will increase with increasing size of the data size

---

### Plotting the tree

```py
from sklearn import tree
plt.figure(figsize=(15,10))
tree.plot_tree(clf,filled=True)
```


