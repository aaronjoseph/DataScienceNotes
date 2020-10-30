### What is Feature Selection ?

Feature selection is a part of data science project. The steps that preceed feature selection are

- Feature Engineering
- Missing Value Treatment
- Normalization
- Imbalanced Dataset
- `Feature Selection`

There is a concept of [[Dimensionality Reduction| Curse of dimensionality]], wherein due to large number of features, the model may not perform well. 

### Variance Threshold

Here, based on the variance threshold features are identified which have variance below the threshold specified - the same will be removed 

```py
from sklearn.feature_selection import VarianceThreshold
var_threshold = VarianceThreshold(threshold=0)
var_threshold.fit(df)
```

### Univariate Feature Selection
`Scoring each feature against a target`

Some of the common methods in Uni-variate analysis are
- Mutual Information
- ANOVA F-test
- $chi^2$

Scikit methods
- SelectKBest - Keeps the top-k scoring features
- SelectPercentile - It keeps the top features which are in percentage specified by the user


### Scikit-learn Libararies

- sklearn.feature_selection.SelectFromModel
- sklearn.feature_selection.RFE(estimator=model,n_features_to_select=3)
