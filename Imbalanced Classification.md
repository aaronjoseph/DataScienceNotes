[[Classification Algorithms]]

- Here, the class distribution has a severe skew, generally in the order of 1:100, 1:1000
- The bias in the training dataset can influence many machine learning algorithms, leading to ignore the minority class entirely
- In Imbalanced clasification, accuracy score should not be considered
- Cross Validation like KFold and hyperparameter tuning should be used to obtain better results
- Undersampling can be done [[Undersampling]]

- To put more weight to the smaller class 1 is the smaller one 
```py
class_weight = dict({0:1,1:100})
classifier = RandomForestClassifier(class_weight = class_weight)
classifier.fit(X_train,y_train)
```
