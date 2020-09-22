Adaptive Boosting or AdaBoost is one of the simplest boosting algorithm. Here, decision trees are used as base ensemble, wherein sequential models are created , each correcting the errors of the last model. 

Steps followed
1. Initially, all observation in the datasets are given equal weights
2. A model is built on a subset of data
3. Using this model, predictions are made on the whole dataset
4. Errors are calculated
5. While creating the next model, higher weights are given to the data points which were predicted incorrectly
6. Weights can be determined using error value. For instance, higher the error more is the weight assigned to the observation
7. This process is repeated untill the error function does not change, or the maximum limit of the number of estimators is reached

```py
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
```

