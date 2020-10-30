The process of converting categorical variable to numerical value, so that the resulting data is used in statistical and machine learning algorithm, that expects numerical variable.

### Label Encoding
Here, a single column can be transformed to a numerical/label column, here there can be two approaches to implement such technique 

Using Map function
```
data['target'].map({'cat':0,'dog':1})
```

Using Sklearn
```py
from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()
label.fit_tranform(DF[Target])
```

Ordinal Encoder can handle 2-D Data, the above, LabelEncoder can only handle 1-D Data
```py 
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit(DF)
```

Label encoding cannot be used in linear models, since the data is expected to be normalized.

> There is a need to mark NaN value to some string value to ensure that this works 

### One-Hot Encoding | Nominal

One hot encoding can be done for nominal categorical variables, wherein for each variable a column is created

> This works great for tree based models over Linear models.

Also, this creates lots of features, therefore this may not always be preferred. [[Dimensionality Reduction|Curse of Dimensionality]]

```
pd.get_dummies(df['target'])
```

Sklearn
```py
from sklearn.preprocessing import OneHotEncoding

enc = OneHotEncoding(handle_unknown='ignore')

enf_df = pd.DataFrame(enc.fit_tranform(DF[['target']]).toarray())

# To merge the one-hot encoding
DF = DF.join(enf_df)
```
---

### When to Use One Hot Encoding Vs Label Encoding

One Hot Encoding | Label Encoding
---------------------|---------------
Used for Nominal variables ( Gender, Country) | Can be used for Ordinal Variables
When number of unique values in a column are less, its ideal [[Dimensionality Reduction]] | When the number of unique values are high, this can be preferred over one-hot


---

### One Hot Encoding with Multiple Categories

Here, observation is made on frequency of labels,  ones with high level of occurance is observed. 

So if a column has 10 records or labels that are more frequent than lets say other 40, wherein the total number of distinct labels are 50, then during one-hot encoding, only 10 columns will be created, keeping the dimensions lower

### Target guided Ordinal Categories

The steps followed are as follows, 
- First with respect to target column, the categorical columns mean is calculated
- Then once the means are calculated across different records, it is ordered for each distinct type
- The one with highest mean gets the highest rank (here, it means larger number, if there are 4 elements, highest rank will be 4)
- This is the ensured for the entire column for creating the columns

### Mean Encoding | Numerical

This is used for numerical column, 

- Assume, that your column have column of Pincodes, herein, the to do one-hot encoding will cause the dimensionality to increase unnecessarily. 
- A better approach is to find the mean with respect to the target variable
- The mean, for each of the numerical value will be value that it would take up