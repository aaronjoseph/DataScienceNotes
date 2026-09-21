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
- Ensure SMOTE is done over the training data and not the test data, since if it is done on the test data, it will give misleading results
- SMOTE works by 
	- Finding n-nearest neighbours in the minority class for each of the samples in the class
	- Then it generates a line, drawn betweeen the neighbors and generates random points on the lines
![[Pasted image 5.png]]

```py
from imblearn.combine import SMOTEomek
os = SMOTEomek(0.5)
os.fit_sample(X_train,y_train)
```

---
### ADASYN

- This is an improved version of SMOTE
- Here, the process is the same as SMOTE, except the minor improvement is in the addition of random small values to the points (Added ones) to make it more realistic

```py
def makeOverSamplesADASYN(X,y):
 #input DataFrame
 #X →Independent Variable in DataFrame\
 #y →dependent Variable in Pandas DataFrame format
 from imblearn.over_sampling import ADASYN 
 sm = ADASYN()
 X, y = sm.fit_sample(X, y)
 return(X,y)
```