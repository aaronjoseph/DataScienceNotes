# Logistic Regression

#search-eng #oan

## Model and Interpretation

Binary logistic regression models a positive-label probability using a linear logit:

$$z=w^Tx+b,\qquad p=\sigma(z)=\frac1{1+e^{-z}},\qquad \log\frac p{1-p}=z.$$

It does not require linearly separable data. In fact, complete separation can make unregularised maximum-likelihood coefficients diverge. Unlike an unconstrained linear-regression output, the sigmoid output stays between zero and one. Multiclass variants also exist.

## Coefficients

Holding other features fixed, increasing feature j by one changes log-odds by $w_j$ and multiplies odds by $e^{w_j}$. The exact percentage odds change is $100(e^{w_j}-1)$; $100w_j$ is only a small-coefficient approximation. This is association under the model, not causation.

For $w_j=\log2$, odds double. If the initial probability is 0.2, odds are 0.25; doubling gives odds 0.5 and probability $1/3$, not 0.4.

## Loss

Bernoulli negative log-likelihood gives binary [[Cross Entropy Loss]]:

$$L=-y\log p-(1-y)\log(1-p).$$

For a linear logit this objective is convex in the parameters; that does not establish a finite, unique solution in every dataset. Use numerically stable logits-based implementations rather than computing log(0). The earlier “Shannon's chaos theory” label was incorrect; entropy and likelihood are the relevant concepts.

| True label | Predicted probability | Limiting loss |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | Infinity |
| 1 | 1 | 0 |
| 1 | 0 | Infinity |

## Search Exercise

Use a pointwise relevance classifier as a baseline. Explain why training on clicks can estimate exposure-dependent outcomes rather than unbiased relevance, and why ranking performance needs [[Search Evaluation]]. See [[Sigmoid Function]], [[L1 and L2 Regularization]], and [[Dependent and Independent Variable]].

## Existing Derivation

![[Logistic_Regression_Derivation.pdf]]

## References & Useful Links

- [Scikit-learn logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — Primary reference for the explanation above.
