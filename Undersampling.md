- In Undersampling, the aim is to increase the number of minority classes as much as the majority class
- This is done by deleting samples of the majority class 
- This technique can cause information loss 

```py pip install imbalanced-learn
from imblearn.under_sampling import NearMiss
ns = NearMiss(0.8)
X_train_ns, y_train_ns = ns.fit_sample(X_train,y_train)
```
