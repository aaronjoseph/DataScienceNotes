Collinearity/MultiCollinearity is a phenomenon related to regression, in which the predictor variable are highly correlated among themselves.

Essentially, when some predictors are collinear to each other, we can reduce the predictors since the model anyways considers the impact of collinear variables to the target variable - this also keeps the model simple.

Correlation Coefficient or Pearson Correlation Coefficient R lies between -1 to 1

If |R| >= 0.75, then the variables are highly correlated
If |R| > 0.25 and |R| < 0.75, variables are moderate to strong correlation
If |R| < 0.25, then the variables are poorly correlated

$R^2$ is the square of R. Assume R = =0.8, then $R^2$ = 0.64, here 64% of the variation in one variable is due to the other variable, rest 36% is caused by other factors

- Find feature that are highly correlated (more than 90%) and the same needs to be dropped, this can be done using correlation heat map
	- For large number features, use Ridge and Lasso Regression [[Ridge, Lasso Regression & Elastic Net]]

![[Correlation and Covariance]]