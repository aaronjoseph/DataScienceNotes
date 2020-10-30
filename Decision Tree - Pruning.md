Decision Tree tend to overfit - high variance.

### Cost Complexity Pruning

Steps followed in Cost Complexity Prunning

- Post the creation of a Decision tree, calculation of SSR is to be taken
	- Here SSR refers to `sum of squared residuals`
	- SSR computes the squared difference between the train value and the predicted values
- SSR can be computed for the whole tree and then recursively done on the decision tree with one lesser leaf and it is done till we reach root node
- Then we take the SSR for each of the tree structure
	- One thing to note, SSR will be higher for the prunned tree as the prunned tree structure will be not fitting the data well enough
- `Weakest Link Prunning` = SSR + $\alpha$T
	- Here, $\alpha$T is the tree complexity penalty
	- $\alpha$ is a tuning parameter that is found using cross validation
	- T refers to the total number of leaves
- The tree score (weakest link prunning) is taken for all the tree structure
- The tree structure with the lowest tree score is taken as the final tree structure

### Calculating $\alpha$
- The value of $\alpha$ will dictate which pruned tree will be selected 
- $\alpha$ is found during cross validation, wherein the SSR has the lowest values

```py
# Code to get different Alpha values
# Here clf is the name of the classifier
path = clf.cost_complexity_pruning_path(X_train,y_train)
# ccp_alphas represent different alpha values that can be tried
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Next stage is to develop classifier with different alpha values
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)

# Next stage is to plot test and train graph
# Identify alpha value with low bias and variance
```
