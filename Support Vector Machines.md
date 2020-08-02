[[Classification Algorithms]]

SVM or Support Vector Machine is used for linear, non-linear classification, regression and outlier detection.

- SVM's are sensitive to the scale of the features and therefore it is important to do feature scaling before training the SVM algorithm

Nonlinear SVM Classifier
- Nonlinear SVM classifier can be acheived by using PolynomialFeatures library of Sklearn

SVM Linear Kernel

```py
# Large Margin Classifier
SVC(kernel="liner", C=float("inf"))
```


Polynomial Kernel
```py
from sklearn.svm import SVC
poly_kernel_svm_clf = Pipeline([
("scaler",StandardScaler()),
("svm_clf",SVC(kernel="poly",degree=3, coef0=1, C=5))
])

poly_kernel_svm_clf.fit(X,y)
```

`Hard-Margin` SVM Classifier - Here the classifier works when the data is linearly seperable without any errors (noise or outliers)

`Soft-Margin` SVM Classifier is an extended version of hard-margin classifier. Softmargin classifier is more flexible and can work with outliers and non-linearly seperable data. This generally results in margin violation.

---
Approach for non-linear data, SVM is designed for Linear data, to handle non-linear data there are two approaches
- Using PolynomialFeature

```py
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.pipeline import Pipeline

clf = Pipeline([
("polynomial",PolynomialFeatures(degree=3)),
("scaler",StandardScaler()),
("svm_clf", LinearSVC(C=10,loss="hinge",random_state=42))
])

clf.fix(X,y)
```

- Using Polynomial Kernel

```py
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline

clf = Pipeline([
("polynomial",PolynomialFeatures(degree=3)),
("scaler",StandardScaler()),
("svm_clf", SVC(kernel="poly",C=10,degree=10,coef0=100))
])

clf.fix(X,y)
```

---

Regression using SVM

```
from sklearn.svm import LinearSVR
from sklearn.svm import SVR
# Linear
svm_reg = LinearSVR(epsilon=1.5)
# Polynomial
svm_poly_reg = SVR(kernel="poly",degree=2,C=100,epsilon=0.1)
```


