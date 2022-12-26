K-means is a clustering algorithm.

### Steps that `Naive k-means` follows

This is referred to as Lloyd's Algorithm

1. First is the arbitary selection of k points 
2. The Algorithm then proceeds to alternate between two steps
	1. `Assignment Step` : Assign each observation to the cluster with the nearest mean, that with the least squared Euclidean distance
	2. `Update Step` : Recalculate means for observations assigned to each cluster

The algorithm has converged when the assignments no longer change. The algorithm does not guarentee to find the optimum.

KMeans is a clustering algorithm

Optimising K-Mean score 

```py
from sklearn.metrics import silhouette_score
silhouette_score(X, kmeans.labels_)
```
---




Q1: What do you understand by Clustering?
Q2: Ok. Can you name a few approaches of clustering you are familiar with?
Q3: What is the difference between KMeans clustering and hierarchical clustering? Which one should we use?

Difference between K-Mean Clustering and Hierarchical clustering ? 
- K-Means clustering specifically tries to put the data into the number of clusters you tell it to
- Hierarchical clustering tells you pair wise  what two things are most similar 

Q4: But we need the value of K. Is there any way to determine?