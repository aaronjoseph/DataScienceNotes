### L1 and L2 Norm Loss Function

L1- norm Loss Function is called as least absolute deviations (LAD) 

### L1 & L2 Regularization

`Ridge Regression` Regularized version of linear regression wherein the regularization term$\alpha/2\sum_{i=1}^{n}\theta_i^2$is used on the cost function

`Least Absolute Shrinkage and Selection Operator Regression` or  Lasso Regression uses  $l_1$ norm that is  $\alpha\sum_{i=1}^{n}|\theta_i|$ in the cost function

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

