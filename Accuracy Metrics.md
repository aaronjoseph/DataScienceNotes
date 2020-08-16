<a href = "https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234">Medium Article </a>

<a href ="https://towardsdatascience.com/your-ultimate-data-science-statistics-mathematics-cheat-sheet-d688a48ad3db"> Medium Article </a>

# Accuracy Metrics
---

> `Loss Function` is defined as the amount by which your predictions are deviating from your actual data, or indicates the magnitude of error the model makes 

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
This is the square root of MSE, however, bring better interpretability to the table.

## MSLE
Mean Squared Log Error

## $R^2$ or Coefficient of Determination
Is the measure of variance explained by the predictor variable which is present in the target variable. 

If $R^2$ is 0.64, then 64% of the variation in the output variable is explained by the input variable, in other words the higher the $R^2$ the more variation is explained by your input variable and hence better is your model
- 0 indicates the given model explains none of the variablity of the response data around the mean
- 100% indicates that the model explains all the variablity of the response data around its mean

## Adjusted $R^2$

Major pitfall of adjusted R-square is that it will always imporve as we increase the number of variables. Adjusted $R^2$ fixes this issue, it adds a penalty to the model. For both $R^2$ and adjusted $R^2$, values closer to 1 is preferred