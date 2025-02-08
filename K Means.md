### K-Means Clustering Algorithm

K-Means is a widely used clustering algorithm that partitions data into $k$ distinct clusters based on feature similarity. It is often referred to as Lloyd's Algorithm. The steps involved are:

---

### Steps in the K-Means Algorithm:

1. **Initialisation:**
    - Randomly select $k$ initial centroids within the data domain.
2. **Iterative Process:**
    - **Assignment Step:** Assign each data point to the nearest centroid based on the squared Euclidean distance.
    - **Update Step:** Recalculate centroids by computing the mean of all data points assigned to each cluster.
3. **Convergence:**
    - Repeat the assignment and update steps until the centroids no longer change.
    - Note: K-Means may converge to a local minimum and does not guarantee finding the global optimum.

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
    - **Hierarchical Clustering:** Builds a hierarchy of clusters:
        - **Agglomerative (Bottom-Up):** Merges smaller clusters into larger ones.
        - **Divisive (Top-Down):** Splits larger clusters into smaller ones.
    - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):**
        - Forms clusters based on the density of data points.
        - Identifies arbitrarily shaped clusters and handles noise.

---

### K-Means vs. Hierarchical Clustering

#### **Q3: How do K-Means and Hierarchical Clustering differ? Which should we use?**

- **A3:** Comparison between K-Means and Hierarchical Clustering:

|**Aspect**|**K-Means Clustering**|**Hierarchical Clustering**|
|---|---|---|
|**Number of Clusters**|Requires pre-defining $k$.|Does not require specifying the number of clusters.|
|**Cluster Shape**|Assumes convex-shaped (e.g., spherical) clusters.|Identifies clusters of various shapes.|
|**Scalability**|Efficient for large datasets (linear time complexity).|Less efficient for large datasets (higher time complexity).|
|**Use Case**|Large datasets with well-separated clusters.|Smaller datasets or when the cluster hierarchy matters.|

---

### Determining the Value of $k$ in K-Means

#### **Q4: How can we determine the value of $k$?**

- **A4:** The **Elbow Method** is commonly used to determine the optimal number of clusters:
    1. Compute the **Within-Cluster Sum of Squares (WCSS)** for different values of $k$.
    2. Plot $k$ vs. WCSS.
    3. The **elbow point** (where the rate of WCSS decrease sharply slows) indicates the optimal $k$.

---

### Further Reading

- [K-Means Clustering Algorithm - Javatpoint](https://www.javatpoint.com/k-means-clustering-algorithm-in-machine-learning)
- [Difference Between K-Means and Hierarchical Clustering - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-k-means-and-hierarchical-clustering/)
- [K-Means Clustering in Python: Step-by-Step Example - Statology](https://www.statology.org/k-means-clustering-in-python/)

---

Tags: #ml #clustering #kmeans #unsupervised