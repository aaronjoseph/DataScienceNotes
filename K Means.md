---
tags:
  - "clustering"
  - "ds-foundations"
---
### K-Means Clustering Algorithm

K-Means is a widely used clustering algorithm that partitions data into $k$ distinct clusters based on feature similarity. It is often referred to as Lloyd's Algorithm. The steps involved are:

---

### Steps in the K-Means Algorithm:

1. **Initialisation:**
    - Choose $k$ initial centroids. The most basic method picks $k$ samples from the data; scikit-learn defaults to **k-means++**, which spreads the initial centroids apart and generally gives better results than random initialisation.[^sk-kmeans]
2. **Iterative Process:**
    - **Assignment Step:** Assign each data point to the nearest centroid based on the squared Euclidean distance.
    - **Update Step:** Recalculate centroids by computing the mean of all data points assigned to each cluster.
3. **Convergence:**
    - Repeat the assignment and update steps until the centroids no longer change (in practice, until they move less than a tolerance).
    - Note: K-Means may converge to a local minimum and does not guarantee finding the global optimum. The result depends on initialisation, so it is common to run several initialisations and keep the one with the lowest within-cluster sum of squares.[^sk-kmeans]

The objective being minimised is the **within-cluster sum of squares (WCSS)**, also called inertia:

$$
\text{WCSS} = \sum_{i=1}^{N} \min_{j} \lVert x_i - \mu_j \rVert^2
$$

where $\mu_j$ is the centroid of cluster $j$.

### Worked Example

**Inputs:** six 1-D points $1, 2, 3, 10, 11, 12$, $k = 2$, and deliberately poor starting centroids $\mu_1 = 1$ and $\mu_2 = 2$.

**Iteration 1, assignment.** Point 1 is nearest $\mu_1$; points 2, 3, 10, 11, 12 are nearest $\mu_2$.

**Iteration 1, update.**

$$
\mu_1 = 1, \qquad \mu_2 = \frac{2 + 3 + 10 + 11 + 12}{5} = 7.6
$$

**Iteration 2, assignment.** Points 1, 2, 3 are now nearer $\mu_1 = 1$. For example, for point 3:

$$
\lvert 3 - 1 \rvert = 2 < \lvert 3 - 7.6 \rvert = 4.6
$$

Points 10, 11, 12 are nearer $\mu_2$.

**Iteration 2, update.**

$$
\mu_1 = \frac{1 + 2 + 3}{3} = 2, \qquad \mu_2 = \frac{10 + 11 + 12}{3} = 11
$$

**Iteration 3.** The assignments do not change, so the algorithm has converged.

$$
\text{WCSS} = (1 + 0 + 1) + (1 + 0 + 1) = 4
$$

Even from a poor start, the two natural groups are recovered here because they are well separated. With overlapping or unevenly sized groups, a poor start can instead settle on a worse local minimum. These iterations were recalculated in Python.

---

### Optimising K-Means Clustering

#### Evaluating Clustering Quality:

- Metrics like the **Silhouette Score** are used to evaluate clustering quality. For example:

```python
from sklearn.metrics import silhouette_score
silhouette_score(X, kmeans.labels_)
```

---

### Understanding Clustering

#### **Q1: What is Clustering?**

- **A1:** Clustering is an **unsupervised machine learning technique** that groups similar data points into clusters based on their characteristics. It facilitates **pattern recognition** and **data segmentation**.

#### **Q2: What are some common clustering approaches?**

- **A2:** Some common approaches include:
    - **K-Means Clustering:** Partitions data into $k$ clusters by minimising variance within each cluster.
    - **[[Heirarchical Clustering|Hierarchical Clustering]]:** Builds a hierarchy of clusters:
        - **Agglomerative (Bottom-Up):** Merges smaller clusters into larger ones.
        - **Divisive (Top-Down):** Splits larger clusters into smaller ones.
    - **[[DBSCAN]] (Density-Based Spatial Clustering of Applications with Noise):**
        - Forms clusters based on the density of data points.
        - Identifies arbitrarily shaped clusters and handles noise.
    - **[[Gaussian Mixture Models]]:** Fits a mixture of Gaussian distributions and gives each point a probability of belonging to each cluster. K-Means can be seen as a special case with equal covariance per component.[^sk-overview]

---

### K-Means vs. Hierarchical Clustering

#### **Q3: How do K-Means and Hierarchical Clustering differ? Which should we use?**

- **A3:** Comparison between K-Means and Hierarchical Clustering:

|**Aspect**|**K-Means Clustering**|**Hierarchical Clustering**|
|---|---|---|
|**Number of Clusters**|Requires pre-defining $k$.|Not fixed before fitting; chosen afterwards by cutting the dendrogram at a height or cluster count.|
|**Cluster Shape**|Assumes convex, isotropic (roughly spherical) clusters.[^sk-kmeans]|Depends on linkage: single linkage can follow non-globular shapes, while Ward favours compact clusters.|
|**Scalability**|Scales well to large datasets; each iteration is linear in the number of samples.|Works from pairwise distances; expensive for large datasets without connectivity constraints.|
|**Use Case**|Large datasets with well-separated clusters.|Smaller datasets or when the cluster hierarchy matters.|

---

### Determining the Value of $k$ in K-Means

#### **Q4: How can we determine the value of $k$?**

- **A4:** The **Elbow Method** is commonly used to determine the optimal number of clusters:
    1. Compute the **Within-Cluster Sum of Squares (WCSS)** for different values of $k$.
    2. Plot $k$ vs. WCSS.
    3. The **elbow point** (where the rate of WCSS decrease sharply slows) indicates the optimal $k$.

---

### Related Notes

- [[DBSCAN]], [[Heirarchical Clustering]], and [[Gaussian Mixture Models]] — Other clustering families.
- [[RFM]] — Customer segmentation with K-Means.
- [[Unsupervised Learning]] — Where clustering fits.

---

## References & Useful Links

[^sk-kmeans]: [scikit-learn User Guide: K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means) — Inertia objective and its convex, isotropic assumption, Lloyd's algorithm, k-means++ initialisation, and local minima.
[^sk-overview]: [scikit-learn User Guide: Overview of clustering methods](https://scikit-learn.org/stable/modules/clustering.html#overview-of-clustering-methods) — Comparison of clustering algorithms, and K-Means as a special case of a Gaussian mixture.

- [K-Means Clustering Algorithm - Javatpoint](https://www.javatpoint.com/k-means-clustering-algorithm-in-machine-learning)
- [Difference Between K-Means and Hierarchical Clustering - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-k-means-and-hierarchical-clustering/)
- [K-Means Clustering in Python: Step-by-Step Example - Statology](https://www.statology.org/k-means-clustering-in-python/)

---
