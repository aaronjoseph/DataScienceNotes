# Dimensionality Reduction

#search-eng

## Core Idea

Dimensionality reduction represents data using fewer coordinates. Feature selection retains a subset of original variables; feature extraction constructs new ones. Reducing dimensions can save storage and computation but can discard useful signal.

The curse of dimensionality concerns sparse coverage and statistical/geometric difficulties as dimensions grow; it is not simply “every algorithm becomes slow”. Some datasets have useful low-dimensional structure, but the manifold hypothesis is an assumption to assess, not a universal fact.

## Methods and Uses

| Method | Main goal | Limitation |
|---|---|---|
| [[PCA]] | Linear directions preserving variance | High variance need not predict the target |
| [[Singular Value Decomposition|Truncated SVD]] | Low-rank matrix approximation; useful for sparse text | Uncentred text decomposition differs from PCA |
| [[T-SNE]] | Visualise local neighbourhood structure | Plot distances between clusters need not reflect original global distances |
| [[Feature Selection]] | Keep selected original features | Selection must be fitted within training data |

Applications include image compression, eigenface representations, and latent semantic analysis. PCA does not preserve all pairwise distances after truncation; t-SNE does not promise exact local distances. Speed depends on dimensions, algorithm, implementation, and data size.

## Search Exercise

Reduce document vectors from 768 to 128 dimensions, applying the same fitted transformation to queries. Compare storage, nearest-neighbour recall, and judged relevance. Explain why variance retained is not enough to approve the change. See [[Embeddings]] and [[Approximate Nearest Neighbours]].

## References & Useful Links

- [Scikit-learn decomposition](https://scikit-learn.org/stable/modules/decomposition.html) — Primary reference for the explanation above.
- [Manifold learning and t-SNE](https://scikit-learn.org/stable/modules/manifold.html) — Primary reference for the explanation above.
