# KNN

#search-eng

## Core Idea

K-nearest neighbours predicts from nearby labelled examples: majority vote for classification or averaging for regression, optionally weighted by distance. It is non-parametric and often called lazy learning because it retains training examples rather than fitting a fixed-size prediction formula. Building a neighbour index still takes work.

Euclidean distance is $\sqrt{\sum_j(x_j-y_j)^2}$; Manhattan distance sums absolute differences. Metric and feature scale determine what “near” means. Choose [[Feature Scaling]] based on feature meaning, and fit it inside validation folds.

## Tradeoffs

Small k can follow noise; larger k smooths predictions but may mix distinct classes. Select k and weighting with [[Cross Validation]], not test-set tuning. Exact search cost depends on data and indexing: trees do not guarantee fast queries in high dimensions. Irrelevant features can obscure meaningful neighbours.

Uses include classification, regression, neighbour-based recommendation, and anomaly-score construction. A small dataset alone does not guarantee good accuracy.

## Worked Example and Exercise

For a one-dimensional query at 3, training points 1:A, 2:A, and 4:B give neighbours 2:A and 4:B tied at distance one. With k=1, the tie policy matters; with k=3, majority vote predicts A. Specify ties and weights for reproducibility.

Distinguish KNN prediction from retrieving vectors with [[Approximate Nearest Neighbours]]: retrieval need not produce a class label. Explain how approximate neighbours could change a vote.

## References & Useful Links

- [Scikit-learn neighbours](https://scikit-learn.org/stable/modules/neighbors.html) — Primary reference for the explanation above.

Previously saved reading (preserved; not used to verify this revision):
- [Original KNN tutorial](https://www.geeksforgeeks.org/k-nearest-neighbours/)
