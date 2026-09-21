# Loss Function & Cost Function

#search-eng

## Definitions

A per-example loss measures prediction error, such as $L(y,\hat y)=(y-\hat y)^2$. An objective often aggregates losses and adds regularisation:

$$J(\theta)=\frac1n\sum_{i=1}^{n}L(y_i,f_\theta(x_i))+\lambda R(\theta).$$

“Loss”, “cost”, and “objective” are not used consistently across libraries; inspect whether a function returns individual losses, a sum, or a mean. Weighting and normalisation affect gradient scale and the relative strength of regularisation.

## Worked Example

Targets `[1, 3]` and predictions `[2, 1]` have squared losses `[1, 4]`. Sum is 5; mean is 2.5. Adding an unchanged penalty to the sum versus the mean changes the balance between fit and regularisation.

## Match the Task

Squared loss is common for regression; [[Cross Entropy Loss]] handles suitable classification probability models. Ranking losses may compare documents within a query. A differentiable surrogate is not necessarily the final product metric: improving a training objective does not guarantee improved [[NDCG]].

## Search Exercise

One query has 100 labelled documents and another has five. Compare averaging over all document losses with averaging each query's loss first. Which query receives more influence under each scheme? Define the intended evaluation population before choosing weights.

See [[Evaluation Metrics]], [[Learning to Rank]], and [[L1 and L2 Regularization]].

## Cross-Entropy Detail

![[Cross Entropy Loss]]

## References & Useful Links

- [PyTorch cross entropy: reduction and weighting](https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html) — Primary reference for the explanation above.
