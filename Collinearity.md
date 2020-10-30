Collinearity/MultiCollinearity is a phenomenon related to regression, in which the predictor variables or independent variables are highly correlated among themselves.

Essentially, when some predictors are collinear to each other, we can reduce the predictors since the model anyways considers the impact of collinear variables to the target variable - this also keeps the model simple.

Correlation Coefficient or Pearson Correlation Coefficient R lies between -1 to 1

If |R| >= 0.75, then the variables are highly correlated
If |R| > 0.25 and |R| < 0.75, variables are moderate to strong correlation
If |R| < 0.25, then the variables are poorly correlated

$R^2$ is the square of R. Assume R = =0.8, then $R^2$ = 0.64, here 64% of the variation in one variable is due to the other variable, rest 36% is caused by other factors

- Find feature that are highly correlated (more than 90%) and the same needs to be dropped, this can be done using correlation heat map
	- For large number features, use Ridge and Lasso Regression [[Ridge, Lasso Regression & Elastic Net]]
---
### Measuring Multicollinearity using Variance Inflation Factor

Multicollinearity is measured using VIF (Variance Inflation Factor)

- Variable Inflation Factor determines the strength of correlation between the independent variables
- It is determined by taking a variable regressing it against every other variable

> In essence, VIF score showcases how an independent variable can be explained by other independent variables

$$VIF = \frac{1}{1-R^2}$$
Here, $R^2$ shows how well an independent variable is described by other independent variables.

VIF starts at 1,
- VIF =1, indicates no correlation between the independent variable and other variables
- VIF exceeding 5 or 10 indicates high multi-collinearity

```py
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calc_vif(X):
	vig = pd.DataFrame()
	vig["variables"] = X.columns
	vig["VIF"] = [variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
```

---
![[Correlation and Covariance]]

