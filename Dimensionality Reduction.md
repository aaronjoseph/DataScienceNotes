`Curse of Dimensionality` - Having a lot of features slows down any learning algorithm.

Dimensionality Reduction - Process of removing features.
In high-dimension data, the distance between two points can be quite large. Hence for high dimensional data number of datapoints required is quite high else the high-dimensional space will remain quite sparse.

**Steps to handle Dimensionality Reduction**
1. Projection
2. Manifold Learning

**Manifold Assumption/ Manifold Hypothesis**
Most real-world high-dimensional datasets lie close to a much lower-dimensional manifold

Dimensionality reduction will usually speed up training but will not guarentee better or simpler solution

PCA (Principal Componet Analysis)
- Is the most popular dimensionality reduction algorithm
- It finds the hyperplane closest to the data, and then projects the data onto it

