# Gradient Boosting Machines (GBM)

#search-eng

## Core Idea

Gradient boosting builds an additive predictor by fitting successive learners to a loss-improvement direction. “Fit the residuals” is exact for squared-error boosting, but is not the general rule for every objective.

At round m, pseudo-residuals are negative derivatives with respect to current predictions:

$$r_{im}=-\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{F=F_{m-1}}.$$

Fit a learner $h_m$ to this signal and update $F_m=F_{m-1}+\eta\gamma_mh_m$, where $\eta$ is a learning rate and $\gamma_m$ represents an appropriate step/leaf-value choice. For squared error, initialise at the training mean; other losses have different optimal constants.

## Worked Example

Using half squared error, targets `[1, 3]` and initial predictions `[2, 2]` give negative gradients `[-1, 1]`. If a learner fits them exactly, a learning rate of 0.1 produces `[1.9, 2.1]`. Ordinary squared residual error falls from 2 to 1.62; this training improvement does not prove better generalisation.

## Implementations and Tradeoffs

[[XGBoost]] and [[Light GBM]] implement related boosting frameworks with specific objectives, regularisation, and algorithms. They are not universal successors that dominate every GBM setup. Successive rounds depend on earlier predictions even when work within a round is parallelised.

Tune learning rate, tree complexity, number of rounds, and validation-based stopping together. Regularisation reduces overfitting risk without guaranteeing its absence.

## Search Exercise

Explain why applying a regression residual recipe to relevance grades is different from [[Learning to Rank|query-aware ranking]]. Keep query groups intact and compare held-out [[NDCG]].

## References & Useful Links

- [Scikit-learn gradient boosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting) — Primary reference for the explanation above.
