# L1 and L2 Regularization

#search-eng #dl

## Purpose

Overfitting means fitting training-specific patterns that do not generalise well. Even linear models can overfit relative to available data. L1 and L2 regularisation add coefficient penalties; they are not defined as injecting noise and do not guarantee prevention of overfitting.

For data loss $J_0(w)$ and $\lambda\ge0$:

$$J_{L1}=J_0+\lambda\sum_j|w_j|,\qquad J_{L2}=J_0+\lambda\sum_jw_j^2.$$

L1 can yield exact zeros under suitable optimisation; L2 usually shrinks weights without making them exactly zero. Squared-error regression with these penalties gives lasso and ridge respectively. L2 here uses the **squared** Euclidean norm. Penalty scaling and intercept treatment vary across implementations.

## Correct Descent Direction

Gradient descent subtracts a derivative: $w_{new}=w-\alpha\partial J/\partial w$, with $\alpha>0$. For one example and $J_0=(wx+b-y)^2$:

$$\frac{\partial J_0}{\partial w}=2x(wx+b-y).$$

L2 adds $2\lambda w$ to that derivative. L1 adds $\lambda\operatorname{sign}(w)$ when $w\ne0$; at zero, use a subgradient or a suitable proximal solver rather than pretending an ordinary derivative exists.

## Worked Example

For $x=1,y=0,b=0,w=2,\lambda=0.5,\alpha=0.1$, the data gradient is 4. An L2 step gives $2-0.1(4+2)=1.4$; an L1 step away from zero gives $2-0.1(4+0.5)=1.55$.

## Practical Choice and Exercise

Scale features deliberately before penalising coefficients; otherwise their units affect the penalty. Correlated inputs can make L1 selection unstable. Choose strength within [[Cross Validation]], then assess an untouched test set.

For a [[Learning to Rank|ranker]], compare feature cost, validation quality, and sparsity. Explain why removing one correlated feature does not prove it was causally irrelevant. See [[Gradient Descent]], [[Feature Selection]], and [[L0, L1, L2 & L-Infinity Norm|norms]].

## References & Useful Links

- [Ridge and lasso formulations](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification) — Primary reference for the explanation above.
