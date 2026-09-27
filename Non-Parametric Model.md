---
tags:
  - "ds-foundations"
---

A non-parametric model does not fix the form or size of the model in advance: its effective complexity grows with the training data. "Non-parametric" does not mean "no parameters" or "no assumptions". A nearest-neighbour model still assumes that a distance metric captures similarity, and it has hyperparameters such as $k$. Contrast with a [[Parametric Model]], which summarises the data in a fixed set of weights.

## Examples

- **Nearest-neighbour methods** ([[KNN]]). They store the training examples, possibly in an index such as a KD tree or ball tree, and predict from the closest ones. scikit-learn calls them "non-generalizing" methods because they do not build a general internal model.[^sklearn-nn]
- **[[Decision Trees]]** grown without a depth limit. The number of splits can grow with the data.
- **[[Kernel Density Estimation]]**. The density estimate is a sum of kernels centred on the training points.

## Nearest-Neighbour Classifier

The nearest-neighbour classifier stores all labelled examples and classifies a new case by its similarity to them, using a distance function.

**Procedure.**

- **Input.** A labelled dataset and a new query point.
- **Output.** A label for the query point.

1. Measure the distance from the query to every example in the dataset.
2. Identify the example with the shortest distance.
3. Assign that example's label to the query.

With $k$ neighbours, step 3 becomes a majority vote among the $k$ closest examples; for regression it becomes their mean. Larger $k$ suppresses noise but blurs class boundaries.[^sklearn-nn]

## Worked Example

**Inputs.** One-dimensional training points with labels $1 \to A$, $2 \to A$, $6 \to B$, $7 \to B$, a query at $x = 4.5$, and absolute distance $|x - x_i|$.

**Step 1: distances.**

$$
|4.5 - 1| = 3.5, \quad |4.5 - 2| = 2.5, \quad |4.5 - 6| = 1.5, \quad |4.5 - 7| = 2.5
$$

**Step 2: $k = 1$.** The nearest point is $6$ at distance $1.5$, so the prediction is $B$.

**Step 3: $k = 3$.** The three nearest points are $6$ ($B$), $2$ ($A$) and $7$ ($B$). The vote is two to one, so the prediction is again $B$.

Points $2$ and $7$ are tied at distance $2.5$. With $k = 2$, which of them is counted would depend on how ties are broken. scikit-learn warns that the result can then depend on the order of the training data.[^sklearn-nn]

## Trade-offs

- **Flexibility.** Non-parametric methods can fit very irregular decision boundaries without choosing a functional form.[^sklearn-nn]
- **Cost grows with the data.** A brute-force neighbour search compares the query with every stored point. Tree indexes reduce this for low-dimensional data but degrade as the dimension grows, one form of the "curse of dimensionality".[^sklearn-nn]
- **Memory.** The training data, or an index over it, must be kept at prediction time.
- **Feature scaling matters.** Distances depend on units, so scale features first; see [[Feature Scaling]].

## Connection to Search

Retrieving the most similar documents to a query embedding is a nearest-neighbour problem. [[Dense Retrieval]] ranks documents by vector similarity, and [[Approximate Nearest Neighbours]] indexes trade a little recall for much lower latency than exact search.

## References & Useful Links

[^sklearn-nn]: [scikit-learn User Guide: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html) — Non-generalizing, instance-based learning; choice of $k$; tie warning; brute force versus KD tree and ball tree; the curse of dimensionality.
