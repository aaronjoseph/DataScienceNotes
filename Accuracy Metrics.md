<a href = "https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234">Medium Article </a>

<a href ="https://towardsdatascience.com/your-ultimate-data-science-statistics-mathematics-cheat-sheet-d688a48ad3db"> Medium Article </a>

# Accuracy Metrics
---

# Classifier Metrics

## Classification Accuracy
Herein the accuracy is defined as the number of correct prediction by the total number of predictions made

$$Classification Accuracy = \frac{Total Correct Prediction}{No of Predications Made}$$

This will not be useful metric when the % of small class is very low, then there is high chance of assuming the performance of the metric to be very high

## Logarithmic Loss / Log Loss
Log loss penalises false classification. Formulae is as follows

Assume there are N samples across M classes, then 


> $$y_{ij}$$  
Indicates if sample i belongs to class j

> $$p_{ij}$$
Indicates the probability of sample i belonging to j class


$$LogarithmicLoss = \frac{-1}{N} * \sum_{i=1}^{N}\sum_{j=1}^{M} y_{ij} * log(p_{ij})$$

## Confusion Matrix

![[Confusion Matrix & Metrics]]

---
# Regressor Metrics

## Mean Absolute Error
Gives the extent of error, but doesn't specify the direction. The most standard classifier

$$MeanAbsoluteError = \frac{1}{N}  \sum_{j=1}^{N}|y_j-\hat{y_j}|$$

```py
from sklearn.metrics import mean_absolute_error
```

## Mean Squared Error
This is useful for computing the gradient.
Also the larger error gets more pronounced.

$$MeanAbsoluteError = \frac{1}{N}  \sum_{j=1}^{N}(y_j-\hat{y_j})^2$$

```py
from sklearn.metrics import mean_squared_error
```

## RMSE
This is similar to MSE, however, bring better interpretability to the table.

## MSLE
Mean Squared Log Error

## Metric - $R^2$
 



