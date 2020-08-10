### Using Map Function for Label Encoding
Example of Categorical Encoding
Map can be used as a dictionary to modify column values

```
data['target'].map({'cat':0,'dog':1})
```

Using Sklearn
```py
from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()
label.fit_tranform(DF[Target])
```

### One-Hot Encoding

One hot encoding can be done for categorical variables, wherein for each variable a column is created

This works great for tree based models over Linear models.

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

### Ordinal Encoding
[[Categorical, Ordinal & Nominal]]
To Encode the ordinal values, the ordinal values need to be encoded

```py 
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit(DF)
```

