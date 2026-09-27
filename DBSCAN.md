---
tags:
  - "clustering"
  - "ds-foundations"
---

## Overview

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) treats clusters as regions of high density separated by regions of low density. It does not need the number of clusters in advance, it can find clusters of any shape, and it labels points in sparse regions as **noise** rather than forcing them into a cluster.[^sk-guide][^sk-api] It was introduced by Ester, Kriegel, Sander and Xu at KDD 1996.[^sk-api]

Use it when clusters are irregular in shape and outliers are expected. [[K Means]] assumes compact, convex clusters and assigns every point to one.

## Key Concepts

DBSCAN has two parameters:

- **`eps` ($\varepsilon$):** the neighbourhood radius. Two points are neighbours if their distance is at most $\varepsilon$.
- **`min_samples`:** the number of points needed in a neighbourhood for it to count as dense. In scikit-learn this count **includes the point itself**.[^sk-api]

Every point then falls into one of three roles:

- **Core point:** its $\varepsilon$-neighbourhood contains at least `min_samples` points.
- **Border point:** not core itself, but within $\varepsilon$ of a core point. It joins that core point's cluster.
- **Noise point:** neither core nor within $\varepsilon$ of any core point. scikit-learn labels it `-1`.

A cluster is built by starting at a core point, adding its neighbours, and continuing to expand through any neighbour that is also a core point.[^sk-guide] Core points reached this way always end up in the same cluster. A border point near two clusters can be assigned to either, depending on processing order.

## Worked Example

**Inputs:** six 2-D points (the scikit-learn documentation example), with $\varepsilon = 3$ and Euclidean distance.

| Point | Coordinates |
|---|---|
| P1 | (1, 2) |
| P2 | (2, 2) |
| P3 | (2, 3) |
| P4 | (8, 7) |
| P5 | (8, 8) |
| P6 | (25, 80) |

**Step 1: distances within the first group.**

$$
d(P_1, P_2) = 1, \qquad d(P_2, P_3) = 1, \qquad d(P_1, P_3) = \sqrt{2} \approx 1.41
$$

All three are within $\varepsilon = 3$ of each other, so each has a neighbourhood of 3 points, counting itself.

**Step 2: distances within the second group and between groups.**

$$
d(P_4, P_5) = 1
$$

$$
d(P_3, P_4) = \sqrt{6^2 + 4^2} = \sqrt{52} \approx 7.21
$$

P4 and P5 each have a neighbourhood of 2 points. The closest pair across the two groups is 7.21 apart, more than $\varepsilon$, so the groups cannot join. P6 is far from everything, so its neighbourhood contains only itself.

**Step 3: labels with `min_samples = 2`.**

P1 to P5 all have at least 2 points in their neighbourhoods, so they are core points. P6 has 1 and is not near any core point.

$$
\text{labels} = [0,\ 0,\ 0,\ 1,\ 1,\ -1]
$$

**Step 4: labels with `min_samples = 3`.**

P1 to P3 still have 3 points each and remain core. P4 and P5 now fall short, and neither is within $\varepsilon$ of a core point.

$$
\text{labels} = [0,\ 0,\ 0,\ -1,\ -1,\ -1]
$$

Raising `min_samples` demands higher density: the small second group dissolves into noise. The same effect happens when `eps` is too small, while an `eps` that is too large merges nearby clusters and eventually returns one cluster.[^sk-guide] Both label vectors were reproduced with a small NumPy implementation; the `min_samples = 2` result matches the scikit-learn documentation example.

## Python Example

Taken from the scikit-learn API example, which documents the output below; not executed locally, because scikit-learn is not installed.

```python
import numpy as np
from sklearn.cluster import DBSCAN

X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
clustering = DBSCAN(eps=3, min_samples=2).fit(X)
print(clustering.labels_)               # [ 0  0  0  1  1 -1]
print(clustering.core_sample_indices_)  # indices of core points
```

The defaults are `eps=0.5` and `min_samples=5`. The documentation notes that `eps` usually cannot be left at its default and must suit the data and distance function.[^sk-api]

## Choosing the Parameters

1. **Scale features first.** `eps` is one radius for every direction; unscaled features make it meaningless. See [[Feature Scaling]].
2. **Pick `min_samples`** by how much noise you want to tolerate. Larger values suit larger, noisier datasets.[^sk-guide]
3. **Pick `eps`** with a k-distance plot: for each point, compute the distance to its `min_samples`-th nearest neighbour, sort these distances, and look for a knee where they start rising sharply.[^sk-guide] Treat the knee as a starting point and inspect the resulting clusters.

## Limitations & Common Pitfalls

- **One global density.** A single `eps` struggles when clusters have different densities. HDBSCAN and OPTICS relax this by considering a range of densities.[^sk-guide]
- **High dimensions.** Distances become less informative as dimensions grow, which makes a density threshold hard to set; reduce dimensionality first when appropriate. See [[Dimensionality Reduction]].
- **No `predict` for new points.** scikit-learn classes DBSCAN as transductive: it labels the data it was fitted on, not unseen points.[^sk-guide]
- **Memory.** scikit-learn's implementation computes neighbourhoods in bulk and can need up to $O(n^2)$ memory when `eps` is large and `min_samples` is low.[^sk-api]
- **Convex-biased metrics.** Silhouette and similar internal scores tend to favour convex clusters, so they can undervalue a good DBSCAN result.[^sk-guide]

## Exercise

You cluster store locations with DBSCAN. Half the stores are in a dense city centre and the rest in scattered suburbs. With one `eps`, either the suburbs become noise or the city merges into one large cluster. Explain why, and suggest two remedies.

> [!example]- Exercise solution
> DBSCAN uses one density threshold for the whole dataset. An `eps` small enough to separate city clusters is too small to connect suburban stores, and one large enough for the suburbs merges the city. Remedies: use HDBSCAN or OPTICS, which handle varying density; or cluster the city and suburbs separately with different parameters. A domain-specific distance, such as travel time, may also help.

## Related Notes

- [[K Means]] — Centroid-based clustering with a fixed number of clusters.
- [[Heirarchical Clustering]] — Nested clusters and linkage choices.
- [[Gaussian Mixture Models]] — Probabilistic, soft cluster assignments.
- [[Outlier]] and [[Anomaly Detection Algorithms]] — DBSCAN's noise label as an outlier detector.

## References & Useful Links

[^sk-guide]: [scikit-learn User Guide: Clustering — DBSCAN, HDBSCAN, OPTICS, and evaluation](https://scikit-learn.org/stable/modules/clustering.html#dbscan) — Core and non-core samples, effects of `eps` and `min_samples`, k-distance heuristic, transductive methods, and silhouette bias towards convex clusters.
[^sk-api]: [scikit-learn `DBSCAN` API](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) — Parameter defaults, `min_samples` counting the point itself, `-1` noise label, memory note, worked example, and the Ester et al. (1996) citation.

- [Ester et al. (1996), "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise"](https://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf) — The original DBSCAN paper, linked from the scikit-learn API page. It could not be opened in this pass, so no claim above relies on it directly.
