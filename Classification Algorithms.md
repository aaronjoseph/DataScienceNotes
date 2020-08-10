# [[Logistic Regression]]
- Useful for understanding the influence of multiple variables on a single outcome
- This is quite useful, when the final outcome variable has only 2 classes
- This can fail for Null Data in the predictor 
- Assumes each predictor is independent of the other predictors

```py
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)
lr.predict(test)
```

# [[Naive Bayes]]
- Useful for small amount of training data
- Is extrememly fast

```py
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
```

# Stocastic Gradient Descent
- Useful when the data is linear
- Can be modified with different loss functions
- Also is suited for large dataset
- Great for online learning

```py
from sklearn.liner_model import SGDClassifier
cl = SGDClassifier()
```

# K-Nearest Neighbours
- Lazy learning implementation
- Simple to Train Algorithm
- Robust to Noisy Data
- Effective when the size of the data is large
- Here there is need to know the value of K & the computation cost is very high

```py
from sklearn.neighbours import KNeighboursClassifier
```

# Decision Tree Classifier
- Can handle both numerical & Categorical Data
- Small variation in the data can create completely different tress

```py
from sklearn.tree import DecsionTreeClasifier
```

# [[Random Forest]] Classifier
- Fits a number of Decision Tree within the algorithm to control the predictive accuracy of the model and control over-fitting
- Is slow when considering real time output
- Is better than decision tress

```py
from sklearn.ensemble import RandomForestClassifier
```

# AdaBoost

# Gradient Boosting

# ExtraTreeClassifier

# Support Vector Machine
- Effective in high dimension space
- Strictly Binary Classifier
- Scales poorly with the the size of the training data
```py
from sklearn.SVM import SVC
```