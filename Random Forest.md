Random-Forest is basically Bagging (Bootstrap Aggregation). 

Random Forest is an ensemble tool which takes a subset of observation and a subset of variables to build a decision trees.

```py
from sklearn.ensemble import RandomForestClassifier
RandomForestClassifier(
n_estimators=500,# 500 Trees
max_leaf_node=16, # Each tree limited to 16 nodes
n_jobs=-1 #No of CPU = All
)
```

---

Hyperparameters

1. max_features - Defined as the maximum number of features random forest is allowed to try in individual tress. Here the options are
	1. Auto/None 
	2. sqrt : Sqrt of the number of features available
	3. 0.2 : Fixed value (here it will indicate 20% of the features)
	> Right balanced needs to be striked, lower number of features will make the model less diverse, while more features will increase the computation complexity
2. n_estimators - The number of trees built to make the final decision, higher the trees, slower the code
3. min_sample_leaf - is the minimum number of samples required to be at the leaf node. Lower the number of samples at the leaf-node will indicate higher degree of noise capture