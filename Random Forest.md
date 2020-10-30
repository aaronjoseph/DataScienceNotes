Random-Forest is basically [[Bagging| bagging technique]]

Random Forest is an ensemble tool which takes a subset of observation and a subset of variables to build a decision trees.

Random Forest is called Random because
1. It takes random samples of training dataset when building trees
2. Random subsets of features are considered when splitting nodes

In bagging technique, a data set is divided into N samples using randomized sampling. Then, using a single learning algorithm a model is built on all samples. Later, the resultant predictions are combined using voting or averaging in parallel.

```py
from sklearn.ensemble import RandomForestClassifier
RandomForestClassifier(
n_estimators=500,# 500 Trees
max_leaf_node=16, # Each tree limited to 16 nodes
n_jobs=-1 #No of CPU = All
)
```

---

Sklearn Hyperparameters

1. max_features - Defined as the maximum number of features random forest is allowed to try in individual tress. Here the options are
	1. Auto/None 
	2. sqrt : Sqrt of the number of features available
	3. 0.2 : Fixed value (here it will indicate 20% of the features)
	> Right balanced needs to be striked, lower number of features will make the model less diverse, while more features will increase the computation complexity
2. n_estimators - The number of trees built to make the final decision, higher the trees, slower the code, use GridSearchCV to find the optimal number of tress. Typical Values lies between `[10,30,100]`
	Also, more uncorrelated trees there are, closer their individual errors get to averaging out
	1. With more number of trees, more samples are created, the more samples that has been created, the more you reduce biasness of the data, with excessive number of trees, data will repeat, therefore optimal number of trees are required
3. min_sample_leaf - is the minimum number of samples required to be at the leaf node. Lower the number of samples at the leaf-node will indicate higher degree of noise capture.
	(or)The min_samples_leaf parameter specifies the minimum number of samples required to be at a leaf node.

4. max_depth - dictates how many splits deep you want the each tree to go. max_split = 50, means it would limit trees to at most 50 splits down any given branch. This will consequently limit the Random Forest to fit the training data closely, and is therefore more stable. It will have lower variance, giving model lower error

 Early stopping with some large no of trees to handle overfitting - Best approach