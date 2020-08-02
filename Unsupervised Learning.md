Unsupervised learning involves no labeled examples for training of the model.

There are 3 major types of unsupervised learning
1. Clustering
2. Anomaly Detection
3. Density Estimations

**Clustering**

Application of Clustering
1. Customer Segmentation
2. Data Analysis
3. Dimensionality Reduction
4. Anomaly Detection
5. Semi-Supervised Learning
6. Search Engines
7. Image Segmentation

### KMeans

KMeans is a clustering algorithm

Optimising K-Mean score

```py
from sklearn.metrics import silhouette_score
silhouette_score(X, kmeans.labels_)
```
