---
aliases: ["Hierarchical Clustering"]
tags:
  - "clustering"
  - "ds-foundations"
---

## Overview

Hierarchical clustering builds a nested set of clusters by successively merging or splitting them. The hierarchy is drawn as a tree called a **dendrogram**: the leaves are individual samples and the root is one cluster containing everything.[^sk-hier] There are two directions:

- **Agglomerative (bottom-up):** start with every sample as its own cluster and repeatedly merge the closest pair.
- **Divisive (top-down):** start with one cluster and repeatedly split it. Bisecting k-means is one divisive method.[^sk-hier]

The earlier version of this note described the method as finding relationships "within a universe of variables". It usually groups **observations** (rows). It can also group **features** (columns) that behave similarly; scikit-learn's `FeatureAgglomeration` does this for dimensionality reduction.[^sk-hier]

## Agglomerative Clustering

The algorithm starts by treating each sample as its own cluster. It then merges the two closest clusters, treats the result like any other cluster, and repeats until one cluster remains. Recording the distance at each merge produces the dendrogram.

"Closest clusters" needs a definition, the **linkage**:[^sk-hier]

| Linkage | Distance between clusters $A$ and $B$ | Tendency |
|---|---|---|
| Single | Closest pair of points, one from each | Can follow long, non-globular shapes; sensitive to noise and chaining |
| Complete | Farthest pair of points | Compact clusters of similar diameter |
| Average | Mean of all pairwise distances | A compromise; works with non-Euclidean distances |
| Ward | Merge that least increases total within-cluster variance | Regular cluster sizes; similar objective to k-means; Euclidean only |

Single, complete, and average linkage work with many distances, including Manhattan and cosine, or a precomputed distance matrix.[^sk-hier]

### Getting flat clusters

A dendrogram is not itself a partition. Cut it at a chosen **distance threshold**, or at the height that produces a chosen **number of clusters**. scikit-learn's `AgglomerativeClustering` accepts either `n_clusters` or `distance_threshold`.[^sk-overview] So the number of clusters does not have to be fixed before fitting, but it still has to be chosen.

## Worked Example: Single versus Complete Linkage

**Inputs:** four points on a line, $A = 0$, $B = 1$, $C = 3$, $D = 7$, with absolute distance. The pairwise distances are:

| | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 3 | 7 |
| B | 1 | 0 | 2 | 6 |
| C | 3 | 2 | 0 | 4 |
| D | 7 | 6 | 4 | 0 |

**Step 1: first merge (the same for both linkages).** The smallest distance is $d(A, B) = 1$, so merge $\{A, B\}$ at height 1.

**Step 2: single linkage** uses the closest pair.

$$
d(\{A,B\}, C) = \min(3, 2) = 2, \qquad d(\{A,B\}, D) = \min(7, 6) = 6, \qquad d(C, D) = 4
$$

Merge $\{A, B, C\}$ at height 2. Then

$$
d(\{A,B,C\}, D) = \min(7, 6, 4) = 4,
$$

so the final merge happens at height 4.

**Step 3: complete linkage** uses the farthest pair.

$$
d(\{A,B\}, C) = \max(3, 2) = 3, \qquad d(\{A,B\}, D) = \max(7, 6) = 7, \qquad d(C, D) = 4
$$

Merge $\{A, B, C\}$ at height 3. Then

$$
d(\{A,B,C\}, D) = \max(7, 6, 4) = 7,
$$

so the final merge happens at height 7.

**Step 4: cut both dendrograms at height 2.5.**

- Single linkage: $\{A, B, C\}$ and $\{D\}$, because the $C$ merge happened at 2.
- Complete linkage: $\{A, B\}$, $\{C\}$, and $\{D\}$, because the $C$ merge happened at 3.

Both linkages merged in the same order here, but at different heights, so the same cut gives different clusters. Single linkage joins points through their nearest neighbours; complete linkage waits until the whole group is tight. The merge heights were recalculated in Python.

## Python Example

Checked against the scikit-learn documentation but **not executed**; scikit-learn is not installed locally.

```python
import numpy as np
from sklearn.cluster import AgglomerativeClustering

X = np.array([[0.0], [1.0], [3.0], [7.0]])

for linkage in ("single", "complete"):
    model = AgglomerativeClustering(n_clusters=None, distance_threshold=2.5, linkage=linkage)
    print(linkage, model.fit_predict(X))
```

Expected, from the worked example: single linkage returns two clusters and complete linkage three. Label numbers are arbitrary. To draw the dendrogram, SciPy's `scipy.cluster.hierarchy.linkage` and `dendrogram` functions are a common choice.

## Limitations & Common Pitfalls

- **Cost.** The standard algorithm works from all pairwise distances, which is $n(n-1)/2$ values, and considers all possible merges at each step unless connectivity constraints are added.[^sk-hier] It suits small and medium datasets.
- **Merges are final.** An early bad merge cannot be undone later.
- **Uneven cluster sizes.** Agglomerative clustering has a "rich get richer" tendency; single linkage is the worst for this and Ward gives the most regular sizes.[^sk-hier]
- **Scale and metric matter.** Distances drive every merge, so scale features first and choose a metric that fits the data. See [[Feature Scaling]].
- **Cutting is a judgement call.** Different thresholds give different partitions; check that the chosen clusters are stable and useful.

## Exercise

You cluster 300 product descriptions represented as TF-IDF vectors. Which linkage and distance would you try first, and why not Ward?

> [!example]- Exercise solution
> Try average linkage with cosine distance. Cosine distance ignores document length, which suits sparse text vectors, and average linkage works with non-Euclidean distances. Ward is defined for Euclidean distance, so it cannot be combined with cosine in scikit-learn. With 300 items the pairwise cost is small, and the dendrogram helps choose how coarse the product groups should be. See [[TF-IDF]] and [[Cosine Similarity]].

## Related Notes

- [[K Means]] — Flat, centroid-based clustering; Ward linkage shares its variance objective.
- [[DBSCAN]] — Density-based clusters and noise, without a hierarchy.
- [[Gaussian Mixture Models]] — Probabilistic soft clustering.
- [[Unsupervised Learning]] — Where clustering fits among unsupervised methods.

## References & Useful Links

[^sk-hier]: [scikit-learn User Guide: Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering) — Dendrograms, agglomerative merging, linkage definitions and behaviour, metrics, connectivity, bisecting k-means, and feature agglomeration.
[^sk-overview]: [scikit-learn User Guide: Overview of clustering methods](https://scikit-learn.org/stable/modules/clustering.html#overview-of-clustering-methods) — Agglomerative parameters (`n_clusters` or distance threshold, linkage, distance) and scalability comparison.