`Curse of Dimensionality` - Having a lot of features slows down any learning algorithm.

Dimensionality Reduction - Process of removing features.
In high-dimension data, the distance between two points can be quite large. Hence for high dimensional data number of datapoints required is quite high else the high-dimensional space will remain quite sparse.

Herein, we have to reduce the number of random variables in consideration
- One can combine, transform or select variables 
- Or make use of linear or non-linear operations

**Need for Dimensionality Reduction**
1. Visulizing, exploring and understanding the data
2. Extracting featurs and dominant modes
3. Cleaning data

**Applications**
1. Image Compression
2. Face recognition (Eigenface)
3. NLP (Latent semantic analysis)

**Steps to handle Dimensionality Reduction**
1. Projection
2. Manifold Learning

**Manifold Assumption/ Manifold Hypothesis**
Most real-world high-dimensional datasets lie close to a much lower-dimensional manifold

Dimensionality reduction will usually speed up training but will not guarentee better or simpler solution

### [[PCA|Principal Component Analysis]] 
- Is the most popular dimensionality reduction algorithm
- It finds the hyperplane closest to the data, and then projects the data onto it

### [[T-SNE]]

T-SNE is another approach for dimensionality reduction

### Difference between T-SNE and PCA

PCA | T-SNE
----|-----
Emerged in 1933 | Emerged in 2008
Linear dimension reduction technique that seeks to maximise variance and preserve pairwise distances | t-SNE differs in the fact that,  it preserves only pair-wise distances or local similarities whereas PCA is concered with preserving large pairwise distances to maximize variance
Very fast for large dataset | Will be extremely slow for large dataset, due to computational complexity