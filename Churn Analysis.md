The biggest predictor of success for any startup or an organisation is the ability to retentin their customers. The other factor that could be looked into are NPS or DAU/MAU, which will also determine the growth of the company.

Companies can always buy growth by means of paid marketing through social media marketing or Google Ad sense. However the general consensus is that it doesn't work in the long run. The company may get into a vicious cycle to keep buying growth to maintain the flow of new customers and could inevitably lead to lower focus on product and can cause the product to get worse over time.

> Cost of getting new customer is often more expensive than retaining the existing customers

Types of Churn
- `Voluntary Churn` - Here the customer switches out to competitor
- `Involuntary Churn` - Inability to pay up and therefore leaves the platform

> Churn analysis is the process of identifying the propensity of risk to exit

Retention Rate is an indicator of how good is your product market fit (PMF). Poor PMF will result in major churn.

---

- First step is to check if there is any imbalance in the dataset

### Visual Code to segement  
```py
# Code to factor 
df.groupby(['Type','churn_Column']).size().unstack().plot(kind='bar',stacked='True',figsize=(30,10))
```

--- 

### Handling Categorical Columns

![[Categorical, Ordinal & Nominal]]

There is a need to handle the categorical values. The code is as follows

```py
import sklearn

LE = sklearn.preprocessing.LabelEncoder()
# Transform Labeled column to numbers
LE.fit_transform(DF['column_name'])
```

### Removal of Redundant Columns

Columns that have no significance to the end-result have to be pruned

### Creation of feature matrix

This is a technique wherein the matrix is generated from the dataframe

```py
df.as_matrix().astype(np.float)
```


### Standardization of Feature Matrix

```py
scaler = preprocessing.StandardScaler()
# X is the Matrix (Without the output)
X = scaler.fit_transform(X)
```

### K-Fold Stratification
![[Stratified K Fold Cross Validation]]

### To Test the model performance

Confusion Matrix

```py
from sklearn import metrics
Confustion_Matrix = metrics.confusion_matrix(Y,Y_)
# To Plot the heat map
sns.heatmap(Confusion_Matrix,annot=True,fmt='')
```

Classification Report
- Gives the various metrics such as Precision, Recall & F1 Score

[[Confusion Matrix & Metrics]]

### Post Selection of Algorithm
To Identify feature importance, use the `.feature_importances_` feature of sklearn, after invoking the model