Correlation Matrix helps us understand relationship between two columns. [[Correlation and Covariance]]

### Cons of Correlation
- Correlation fails in Non-Linear relationships such as quadratic or mystery step function. Also it is defined for numerical columns, categorical columns need to be encoded or transformed into one-hot encoding
- Correlation is based on symmetry, while this may not be true in the real world

### What PPS sets out to acheive
- Gives a score between 0 & 1 between two columns and the columns can be categorical as well

### Advantages of PPS
- Find pattern in data
- Feature Selection


```py
!pip install ppscore
import ppscore as pps
pps.score(df,"feature_column","target_column")
# Or
pps.matrix(df)
```


### Limitation
- Calculation is slower than correlation
- Score interpretation cannot be understood, as much as correlation, hence good to use correlation in the background