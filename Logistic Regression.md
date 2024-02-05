### Reasoning

Here, the top-level goal is to predict a scalar-valued target from a set of features, the scalar values is binary in nature for logistic regression

- Linear Regression can be used for classification, by using the best fit line
	- The caveat here is, due to Outliers the best fit line can get affected, leading to faulty results
- Logistic Regression is generally done on binary classification
- It is generally done on dataset, wherein the data is linearly seperable

---
### Why is it called Logistic `Regression` ?

Regression is the statistical method of identifiying strenght and character of the relationship between one dependent variable and one or more [[Dependent and Independent Variable|Independent variables]].

In the most fundamental form, the hypothesis function for linear regression is  $y=\omega^T.x$ 

In Logistic Regression, the sigmoid function is applied over the hypothesis function.

---
### Interpretation of Logistic Regression Co-efficients
#oan 
When using any basic libraries, we can obtain the co-effients, that will enable us to understand the relationship between the [[Dependent and Independent Variable| Dependent & Independent]] variable. If we have a fixed value accociated to the co-efficient term, here's how the interpretation is:
Assume, the co-efficient of the independent variable x to be $c_0$
- A increase in 1 unit of x will lead to natural log of outcome to increase of decrease by $c_0$
- If x increases by 1 unit, then then the odds of dependent variable increases/decreases by a factor of exp($c_0$)
- If x increases by 1 unit, the odds of dependent variable increases by roughly 100*$c_0$ %

---

### Loss Function

[[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence | Shannon's Chaos theory]] is the underlying principle used for determining the loss function. The linear regression loss function cannot be employed since, it will result in a non-convex optimization, which will result in the parameters not reaching global optima.

Cost function is derived from principle of maximum likelihood estimation - which is an idea on how to efficiently find parameters data from different models and also ensure the function remains convex. This is based on convexity analysis.

Formulae Used : $-[y.log(\hat{y}) + (1-y)log(1-\hat{y})]$

Note :
log(0) = - Infinity
log(1) = 0

Actual - y | Predicted - $\hat{y}$ | Loss Function Result 
-----------|------------------------|----------------------
0|0|0
0|1|Infinity
1|1|0
1|0|Infinity

---
Mathematics : 
![[Logistic_Regression_Derivation.pdf]] [[Sigmoid Function]]