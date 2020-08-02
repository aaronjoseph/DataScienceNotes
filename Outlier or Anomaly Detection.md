### Isolation Forest
Is an algorithm that gives an anomaly score for a given sample.

The algorithm works of the following principle
1. First the algorithm isolates observation by creating paths by randomly selecting a feature, randomly selecting a split value, the path length representing its normality
2. Shorter path represents anomalies
3. The outputs are -1 to 1, positive score indicates an anomaly

```py
from sklearn.ensemble import IsolationForest
identifier = IsolationForest().fit(X)
identifier.predict(X)
```

### One Class SVM
This is another unsupervised method, for detecting outliers, suited for high-dimensional distribution where an anomaly detection method like IsolationForest would develop too much of variance

```py
from sklearn.svm import OneClassSVM
identifier = OneClassSVM.fit(X)
identifier.predict(X)
```

### Local Outlier Factor

This is the third commonly used outlier identifiers. The anomaly score of each sample  - the Local Outlier Facor - measures the local deviation fo density given a sample with respect to its neighbors. 

This algorithm is distance based and therefore the data needs to be `scaled` or `normalized` before it is used.

This algorithm can be seen as non-linear high-variance alternative to Isolation Forest

```py
from sklearn.neighbors import LocalOutlierFactor
model = LocalOutlierFactor().fit(X)
model.predict(X)
```

> PCA visualization can confirm the extent of anomaly within a dataset

