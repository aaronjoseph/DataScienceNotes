[[Classification Algorithms]]
[[Regression Algorithms]]
- Base of ensemble algorithm
- Decision Tree has low-bias and high-Variance
- Decision Trees are versatile Machine Learning Algorithms that perform both classification and regression tasks and even multi-output tasks
- The advantages of DecisionTree is that they require very little data preparation - feature scaling
- Decision tree is `non-parametric`, meaning to say the number of parameters are not clear before the training
- Decision tree is prone to small variation in the dataset
- Training Algorithm used in Scikit-learn is stocastic, you will get different results on the same training data

```py
# Classifier
from sklearn.tree import DecisionTreeClassifier
# Regressor
from sklearn.tree import DecisionTreeRegressor
```

- Decision trees are `White Box` in nature, as in we can uncover the decisions for the classification, incontrast Random Forest has more of a `Black Box` approach, as in we cannot make sense of what is happening inside
- Decision tree can also output the probabilities of the predicted values
```py
clf.predict_proba()
```
- Decision Tree uses CART Algorithm
	- `Classification And Regression Tree`, works by splitting the training set into two subsets using two values k and $t_k$, wherein it searches for (t,$t_k$) values which produces the purest subset
	- Once the CART algorithm has successfully split the training set in two, it splits the subsets using the same logic. It stops recusing after it reaches the maximum depth or cannot find a split that will reduce impurity
	- This is a greedy algorithm, it doesn't search for optimal solution, just searches for reasonable solution
	- Optimal tree is a NP-Complete problem

---
Gini Impurity

A node is pure if all training instances it applies to belong to the same class.

$G_i=1-\sum_{k=1}^{n}P_{i,k}^2$

---

[[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence]]

Entropy or Gini?
- Not much of a difference here, Gini should be preferred, it is slightly faster
- Gini tends to isolate freqeunt class in its own branch of tree, while entropy tends to produce slightly more balanced trees