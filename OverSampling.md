- In Oversampling, the samples are increased for the minority class, so the numbers are close to the majority class

```py 
# pip install imbalanced-learn
from imblearn.over_sampling import RandomOverSampler
os = RandomOverSampler(0.8)
os.fit_sample(X_train,y_train)
```

---
#### SMOTE - Synthetic Minority Oversampling Technique 
- SMOTE is a Oversampling techinique wherein class balancing
- SMOTE creates new points to the smaller class basis the euclidan distance
- Ensure SMOTE is done over the training data and not the test data, since if it is done on the test data, it will give misleading results

```py
from imblearn.combine import SMOTEomek
os = SMOTEomek(0.5)
os.fit_sample(X_train,y_train)
```

