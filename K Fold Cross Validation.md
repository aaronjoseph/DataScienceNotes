Assume in normal circumstances, a model obtains 95% accuracy in the test split. This performance is quite optimistic and with real data, the model will perform much worse. 

To solve this issue, the entire dataset can be used to validate the model. Iteratively, the model is trained and validated on different portions of the data.

Characteristics of K-Fold Cross validation
- It's a resampling technique
- Gives a better measure of performance
- Results in less-biased models
- It's more expensive to run

At the end of the process, the model's performance is computed by averaging the performance on each repetition.

> Issue with K-Fold, the process is very costly, need to evaluate k different models, which becomes prohibitive for large datasets. Deep learning models rarely use k-fold cross validation because of this.