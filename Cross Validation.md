Cross validation is a resampling procedure used to evaluate machine learning models over a limited sample of data. In essence it is used to estimate the skill of a Machine Learning Model over unseen data and `ensures the model fits the data well and not overfit`

It tests the performance of the model on the data that it hasn't seen before.

### Steps followed in Cross Validation

The general procedure is as follows:

1. Shuffle the dataset randomly
2. Split the dataset into k groups

For each group:

1. Take the group as a holdout or test data set
2. Take the remaining as train dataset
3. Fit a model on the training dataset and evaluate it on the test data set
4. Retain the evaluation score and `discard the model`

> Cross-validation can be employed to understand how well any machine learning algorithm work and compare and will also give a sense of how well they will work in practice

### K-Fold

In K-fold, the data is split into k-splits and is used for model training

### Stratification

Stratification is the process of rearranging the data, such that each fold is a good representation of the population

### Stratified K-Fold 

In stratified K-Fold, the folds are mode preserving the percentage of samples for each class.

Also, StratifiedKFold shuffles the data by default. But when shuffle=True, it shuffles by random state (default is np.random)
