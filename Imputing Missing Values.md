> Imputing means `fill in`

Algorithms such as XGBoost will not require imputation as it can handle missing values. LightGBM have options to ignore them (use_missing = false) 

---
# Types of Imputing 
1. Simple Imputing Methods
	1. The strategy here is to fill `NaN` values with statistical values such as mean, median, mode, constant
```py
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
# SimpleImputer(strategy='most_frequent') -> For most frequently used data
data = imputer.fit_transform(data)

df.fillna(0) # Fill zeros for NA
```

Pros
- Works well with categorical features
 
Cons
- It doesn't factor the correlations between features
- It can introduce bias in the data

2. KNN Imputer
	1. Is a common imputerer, it employs KNN algorithm to find other data points similar to one with a missing value within multidimensional space
	2. To apply KNN, you will need to scale the values
		1. Scale/Normalize the data
		2. KNN-Impute to fill the missing values
		3. Inverse scale/normalize the data

Pros:
- Better than SimpleImputer strategy

Cons:
- Computationaly expensive, works by storing the whole data in memory
- KNN is quite sensitive to outliers in the data

```py
from sklearn.impute import KNNImputer
imputer = KNNImputer()
data = imputer.fit_transform(data)
```

3. Imputation using Multivariate Imputation by Chained Equation (MICE)

```py
from impyute.imputation.cs import mice

imputed_training = mice(train.values)
```
---
### Handling Missing Values in Categorical Features

Some of the steps that can be taken are
- Deletion of records where there are missing values
	- This will lead to loss of information
- Replace with the most common value
	- Majority class issues will perist, class imbalance might occur due to this
- `Using model to predict missing values` Using Supervised ML algorithm so as to predict the value of missing values
	- Herein wherever there are non-missing values, we can use it as train-data
	- Test data is where-in we can fill the missing data
- `K-Means Clustering/ Hypermean Clustering`
	- Idea, here is to develop as many centroid as is the number of differenct features in the column
	- Lets say it is a Male and Female column, we can take clustering with k=2
	- Then plug the missing values

