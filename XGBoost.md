XGBoost is an an advanced version of [[Gradient Boosting (GBM)]] and is a very effective algorithm. XGBoost has high predictive power and is almost 10 times faster than the other gradient boosting techniques. It also includes a variety of regularization which reduces overfitting and improves overall performance. 

Some of the key advantages of XGBoost are 

1. Regularization 
	1. Standard GBM do not have regularization like XGBoost
	2. XGBoost prevents overfitting
2. Parallel Processing
	1. XGBoost implements parallel processing and is faster than GBM
	2. Also supports on Hadoop
3. High flexibility
	1. XGBoost allows users to define custom optimization objectives and evaluation criteria adding a whole new dimension to the model
4. Handling Missing Values
	1. XGBoost has an in-built routine to handle missing values
5. Tree Pruning
	1. XGBoost makes a splits up to the max_depth specified and then starts pruning the tree backwards and removes splits beyond which there is no positive gain
6. Built-in Cross Validation
	1. XGBoost allows a user to run a cross validation at each iteration of the boosting process and thus it is easy to get exact optimum number of boosting iterations in a single run

```py
import xgboost as xgb
model = xgb.XGBRegressor
```
