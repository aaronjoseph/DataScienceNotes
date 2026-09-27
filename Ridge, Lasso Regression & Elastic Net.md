### Need

For a regression model, there is always a chance of overfitting. Ridge, Lasso and Elastic Net regression by design ensures the model has lower variance. 

The end goal of any model is to have [[Bias-Variance Tradeoff| low bias and low variance]]

### Ridge and Lasso Regression
 
 [[L1 and L2 Regularization| Equations and Intuition on L1 and L2 regularization]]
 
`Ridge Regression` Regularized version of linear regression wherein the following regularization term is used on the cost function:

$$
\frac{\alpha}{2} \sum_{i=1}^{n} \theta_i^2
$$

[[Collinearity]] can be reduced using Ridge regression.
- Penalises where the slope is large
	- This will make the line less steep

`Least Absolute Shrinkage and Selection Operator Regression` or  Lasso Regression uses the $l_1$ norm in the cost function:

$$
\alpha \sum_{i=1}^{n} \lvert \theta_i \rvert
$$
- Lasso reduces overfitting
	- Also, helps in [[Feature Selection]]

Elastic Net is a middle ground between Ridge Regression and Lasso Regression

With mix ratio $r$, the penalty added to the cost function is:

$$
r \alpha \sum_{i=1}^{n} \lvert \theta_i \rvert + \frac{1 - r}{2} \alpha \sum_{i=1}^{n} \theta_i^2
$$

$r = 0$ gives the Ridge term above and $r = 1$ gives Lasso. (The earlier version of this formula halved the L2 term twice.)

---
Selection Criteria
- Good to have regularization
	- Hence not good to have plain regression
- Ridge is good by default
- Lasso/Elastic Net is used when you suspect only few features are useful
- Elastic Net is better than Lasso when
	- No of features is greater than the number of training instances or when several features are strongly correlated

