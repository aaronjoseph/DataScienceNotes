For a given input, there needs to be a way to classify 

In the code below, 

```py
# Code for MultiLabel Classification
from sklearn.neighbours import KNeighboursClassifier

Target_MultiLabel = np.c_[Label_1,Label_2]
knn_clf = KNeighbourClassifier()
knn_clf.fit(Predictor,Targer_MultiLable)
```

