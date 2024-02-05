#dl 
`Overfitting` - the phenomenon, wherein the model has higher accuracy score for the training data, but fails to generalize for any other model.

In general, simple linear regression is not prone to overfitting, however, higher degree polynomial regression functions or deep learning algorithms will be prone to overfitting due to its complex architecture

`Regularisation` - The process of adding noise in the model to prevent the model from overfitting. In the general sense, regularization is a mathematical constraint injected into the loss function. A loss function by function tries to minimize the error between y and $\hat{y}$

### L1 and L2 Regularization


L1 and L2 Regularization gets its name from [[L0, L1, L2 & L-Infinity Norm| L1 & L2 Norm]]

A linear Regression Model that uses L1 norm for regularisation is called Lasso Regression.

One that implements L2 is called Ridge Regression.

In both cases, the hypothesis function remains the same. However, there are changes in the loss function.

Hypothesis Function
$$\hat{y} = w_1x_1 + ..+ w_Nx_N$$

Standard Loss Function
$$Loss = Error(y,\hat{y})$$
Loss Function with L1 regularization
$$Loss = Error(y,\hat{y}) + \lambda \sum_{i=1}^{N}|w_i|$$
Loss Function with L2 regularization
$$Loss = Error(y,\hat{y}) + \lambda \sum_{i=1}^{N}|w_i^2|$$

> In the absolute sense, L2 regularization uses L2 Norm with the exception of square root, this is not present in the equation

Here, $Error(\hat{y}-y) = (\hat{y}-y)^2$
For Simple Linear Regression, where y = wx + b, we have
$Error(\hat{y}-y) = (wx+b-y)^2$

For [[Gradient Descent| Gradient Update]] we have the following,

Standard Equation 
$$w_{new} = w + \alpha \frac{\partial{L}}{\partial{w}} $$

Update Rule for Standard Regression Function

$$w_{new} = w + \alpha \frac{\partial{L}}{\partial{w}} $$
$$=  w + \alpha [2x(wx+b-y)] $$

Update for L1 Regularisation

$$w_{new} = w + \alpha \frac{\partial{L}}{\partial{w}} $$
$$=  w + \alpha [2x(wx+b-y) + \lambda \frac{d|w|}{dw}] $$
$$ \begin{cases}
    w - \alpha [2x(wx+b-y) + \lambda] & \text{if w > 0}\\
    w - \alpha [2x(wx+b-y) - \lambda] & \text{if w < 0}
  \end{cases}
$$

Update for L2 Regularisation

$$w_{new} = w + \alpha \frac{\partial{L}}{\partial{w}} $$
$$=  w + \alpha [2x(wx+b-y) + \lambda \frac{d|w|^2}{dw}] $$
$$ = w - \alpha [2x(wx+b-y) + 2\lambda w] $$

On close observation, L1 Regularisation has effects of pushing the weights close to 0, as in when the value is greater than 0, it negates the weights and less than zero, it has an additive effect. This is quite useful in multi-collinearity situtaion, wherein, it has effects of removing unnecessary variables.