In Classification, accuracy isn't a great metric especially when the classes are skwed since some classes are more frequent than others. Refer [[Confusion Matrix & Metrics]] for F1 Score and accuracy

### Implementing StratifiedKFold for classification

Stratifed KFold is basically K folds of the dataset, wherein each strata has equal composition of the main population. For implementing stratified KFold in classification the following is the code

```py
from sklearn.model_selection import cross_val_score
cross_val_score(model_name, predictor_df,target_df, cv=3,scoring='accuracy')
```

