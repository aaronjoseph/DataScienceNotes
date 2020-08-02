> Imputing means `fill in`

# Types of Imputing 
1. Simple Imputing Methods
	1. The strategy here is to fill `NaN` values with statistical values such as mean, meadian, mode, constant
```py
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
data = imputer.fit_transform(data)
```

2. KNN Imputer
	1. Is a common imputerer, it employs KNN algorithm to find other data points similar to one with a missing value within multidimensional space
	2. To apply KNN, you will need to scale the values
		1. Scale/Normalize the data
		2. KNN-Impute to fill the missing values
		3. Inverse scale/normalize the data

```py
from sklearn.impute import KNNImputer
imputer = KNNImputer()
data = imputer.fit_transform(data)
```

