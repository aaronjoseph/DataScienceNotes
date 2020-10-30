### Need

For a regression model, there is always a chance of overfitting. Ridge, Lasso and Elastic Net regression by design ensures the model has lower variance. 

The end goal of any model is to have [[Bias-Variance Tradeoff| low bias and low variance]]

### Ridge and Lasso Regression
 
 [[L1 and L2 Regularization| Equations and Intuition on L1 and L2 regularization]]
 
`Ridge Regression` Regularized version of linear regression wherein the regularization term$\alpha/2\sum_{i=1}^{n}\theta_i^2$is used on the cost function. [[Collinearity]] can be reduced using Ridge regression.
- Penalises where the slope is large
	- This will make the line less steep

`Least Absolute Shrinkage and Selection Operator Regression` or  Lasso Regression uses  $l_1$ norm that is  $\alpha\sum_{i=1}^{n}|\theta_i|$ in the cost function
- Lasso reduces overfitting
	- Also, helps in feature selection

Elastic Net is a middle ground between Ridge Regression and Lasso Regression

$(r)*  \alpha\sum_{i=1}^{n}|\theta_i| + ((1-r)/2)*  \alpha/2\sum_{i=1}^{n}\theta_i^2$

---
Selection Criteria
- Good to have regularization
	- Hence not good to have plain regression
- Ridge is good by default
- Lasso/Elastic Net is used when you suspect only few features are useful
- Elastic Net is better than Lasso when
	- No of features is greater than the number of training instances or when several features are strongly correlated

