**Gradient Boosting Machine (GBM)** is an ensemble machine learning technique that builds models sequentially, each new model attempting to correct the errors of the previous ones. This approach is effective for both regression and classification tasks.

**How Gradient Boosting Works:**
1. **Initialisation**: Start with an initial prediction, often the mean of the target variable for regression tasks.
2. **Iterative Training**:
	1. **Compute Residuals**: Calculate the difference between the actual and predicted values (residuals).
	2. **Fit Weak Learner**: Train a weak model (typically a decision tree) to predict these residuals.
	3. **Update Model**: Adjust the existing model by adding the new weak learner, scaled by a learning rate, to improve predictions.
3. **Repeat**: Continue this process for a specified number of iterations or until the residuals are minimized.

**XGBoost as a Successor to GBM:**

**XGBoost (eXtreme Gradient Boosting)** is an advanced implementation of the gradient boosting framework. While it shares the foundational principles of traditional GBM, XGBoost introduces enhancements that make it more efficient and powerful:
- **Regularization**: Incorporates L1 and L2 regularization to prevent overfitting.
- **Parallel Processing**: Utilizes parallel computation to speed up model training.
- **Tree Pruning**: Employs a depth-first approach with a maximum depth parameter to control model complexity.
- **Handling Missing Values**: Automatically learns the best way to handle missing data during training.

These improvements position XGBoost as a more robust and scalable version of traditional gradient boosting methods.

