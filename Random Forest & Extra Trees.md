Random-Forest is basically Bagging (Bootstrap Aggregation)

```py
from sklearn.ensemble import RandomForestClassifier
RandomForestClassifier(
n_estimators=500,# 500 Trees
max_leaf_node=16, # Each tree limited to 16 nodes
n_jobs=-1 #No of CPU = All
)
```

Extra Trees

Is a random Forest with tree's being extremely randomized, where the thresholds are quite random for each feature unline in a decision tree where the thresholds are for searched for best values

```py
from sklearn.ensemble import ExtraTreesClassifier
```

[[Classification Algorithms]]