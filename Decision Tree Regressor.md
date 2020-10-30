Decision Tree can be used for regression.

In regressor tree the difference is that, there will be Numerical values in its leaf node as against categories as in classification trees.

Steps followed,

1. First the target variable is to be identified
2. Then the target value is ordered in ascending order
3. Next we build trees with conditions that are taken sequentially from the least to highest values and placed in two nodes lets say - left and right node for now
	1. Then the average	of the left node is calculated and is considered as output of the left node
	2. And the average of the right node is calculated and is considered as output of the right node
	3. Now the mean squared is calculated for both the nodes, with respect to the datapoints that it has
3. Ideally, the tree with the least MSE is considered
4. This process is followed when constructing the tree to its depth

> In sklearn, we can use MSE, friedman_MSE, MAE alternatively



