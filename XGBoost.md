**XGBoost (eXtreme Gradient Boosting)** is an advanced implementation of the gradient boosting framework, designed for efficiency, scalability, and high performance. It has gained popularity for its robust handling of large datasets and superior predictive accuracy in various machine learning tasks.

[[XGBoost Regression]] -> For regression
[[XGBoost Classification]] -> Classification

---
### Main Ideas

XGBoost, an advanced implementation of [[Gradient Boosting Machines (GBM)]] (GBM), is renowned for its high predictive accuracy and computational efficiency, often outperforming traditional GBM techniques. It incorporates several enhancements that contribute to its effectiveness:
1. **Regularization**: Unlike standard GBM, XGBoost includes regularization parameters to control model complexity, thereby reducing overfitting and enhancing generalization.
2. **Parallel Processing**: XGBoost supports parallel computation, significantly accelerating training times compared to traditional GBM. It also integrates seamlessly with distributed systems like Hadoop.
3. **Flexibility**: Users can define custom optimization objectives and evaluation metrics, allowing XGBoost to be tailored to specific problem requirements.
4. **Handling Missing Values**: XGBoost has built-in mechanisms to manage missing data, maintaining robustness in datasets with incomplete information.
5. **Tree Pruning**: The algorithm employs a pruning technique that builds trees up to a specified maximum depth and then prunes branches that do not contribute to a positive gain, optimizing model performance.
6. **Built-in Cross-Validation**: XGBoost facilitates cross-validation during the boosting process, enabling users to determine the optimal number of boosting iterations in a single run.

To implement XGBoost in Python:

```python

import xgboost as xgb

# Initialize the XGBoost regressor

model = xgb.XGBRegressor()

```

This code snippet initializes an XGBoost regressor model, which can then be trained and evaluated on your dataset.

## **How XGBoost Works:**
1. **Gradient Boosting Framework**: XGBoost builds an ensemble of decision trees sequentially, where each new tree aims to correct the errors of the existing ensemble. This is achieved by optimising a differentiable loss function using gradient descent techniques.
2. **Second-Order Approximation**: Unlike traditional gradient boosting methods that use first-order (gradient) information, XGBoost incorporates both first and second-order derivatives (gradient and Hessian) of the loss function. This second-order approximation provides a more accurate estimation of the loss, leading to better optimization and performance.
3. **Regularisation**: To prevent overfitting, XGBoost includes regularisation terms in its objective function. These terms penalise the complexity of the model, encouraging simpler models that generalise well to unseen data.
4. **Sparsity Awareness**: XGBoost efficiently handles sparse data by automatically learning the best missing value imputation, making it suitable for datasets with missing values or varying feature densities.
5. **System Optimisation**: The algorithm is engineered for parallel and distributed computing, enabling rapid model training. It also supports out-of-core computation for handling datasets that exceed memory capacity.

**Differences Between XGBoost and Random Forest:**
1. **Ensemble Strategy**:
	1. _Random Forest_: Employs **bagging** (Bootstrap Aggregating), where multiple decision trees are built independently using random subsets of the data and features. The final prediction is made by aggregating the predictions of all trees (majority vote for classification or average for regression).
	2. _XGBoost_: Utilizes **boosting**, constructing trees sequentially. Each new tree focuses on correcting the errors made by the previous ones, leading to a strong ensemble where each tree improves upon its predecessors.
2. **Model Training**:
	1. _Random Forest_: Trees are trained in parallel, as each tree is independent of the others.
	2. _XGBoost_: Trees are built sequentially, with each tree depending on the outcome of the previous tree, making the training process inherently sequential.
3. **Overfitting Control**:
	1. _Random Forest_: Controls overfitting by averaging multiple deep trees, reducing variance without increasing bias significantly.
	2. _XGBoost_: Incorporates regularisation techniques (both L1 and L2) to penalise complex models, effectively reducing overfitting by controlling model complexity.
4. **Computational Complexity**:
	1. _Random Forest_: Generally faster to train due to the parallel nature of tree construction.
	2. _XGBoost_: May require more computational resources and time, as trees are built sequentially, and the algorithm performs more complex calculations, including second-order gradient computations.
5. **Hyperparameter Tuning**:
	1. _Random Forest_: Requires tuning parameters like the number of trees, maximum depth, and the number of features to consider at each split.
	2. _XGBoost_: Involves tuning a more extensive set of hyper parameters, including learning rate, maximum depth, regularisation terms, and the number of boosting rounds, offering more control but also adding complexity to the tuning process.