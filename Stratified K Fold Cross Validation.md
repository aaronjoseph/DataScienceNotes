>`Stratification` - The Process of representing all strata of data in each fold. This is done in a supervised way to ensure equal representation of data

Essentially this is done since the general algorithm gives more weightage to the over-represented class and therefore will have poor accuracy.It is the process of re-arranging the data. Stratified Cross Validation - Split data into k folds and each fold has the same proportion of different class as that is there in the main population. 

Code to do [[K Fold Cross Validation]] and allow for Models

For K-Fold Cross Validation - Use StratifiedKFold() & Run it within a loop

```py
from sklearn import cross_validation
def stratified_cv(X, y, clf_class, shuffle=True, n_folds=10, **kwargs):
    stratified_k_fold = cross_validation.StratifiedKFold(y, n_folds=n_folds, shuffle=shuffle)
    y_pred = y.copy()
    # ii -> train
    # jj -> test indices
    for ii, jj in stratified_k_fold: 
        X_train, X_test = X[ii], X[jj]
        y_train = y[ii]
        clf = clf_class(**kwargs)
        clf.fit(X_train,y_train)
        y_pred[jj] = clf.predict(X_test)
    return y_pred
	
# Different Classification Models
from sklearn import ensemble
from sklearn import svm
from sklearn import neighbors

stratified_cv(X, y, ensemble.GradientBoostingClassifier)
stratified_cv(X, y, svm.SVC)
stratified_cv(X,y, ensemble.RandomForestClassifier)
stratified_cv(X,y, neighbors.KNeighborsClassifier)
stratified_cv(X, y, linear_model.LogisticRegression))))
```
