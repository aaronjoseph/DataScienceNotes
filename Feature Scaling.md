### Feature Scaling

> Feature Scaling is the modification of independent variable, some of the supervised techniques like Linear Regression or SVM depend on the euclidian distance, feature scaling helps in faster convergence
> For ANN you will need to do Standardization

Feature Scaling will not be required for ensemble technique

1. Min-Max Scaler/ Normalization
	1. Here the values are normalised between 0 & 1

	$$X_{norm} = \frac{X - X_{min}}{X_{max}-X_{min}}$$
2. Standardization
	1. Here the Mean value is adjusted to 0
	2. Then the values are filled as per the standard Deviation from the mean
	3. This method can handle outlier values

Technique uses Z-Score for calibration $z = \frac{Observation - Mean}{Standard Deviation}$

> `Z-Score` defines the distance of the measurement from the mean, wrt Std deviation

```py
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit_tranform(DF['predictor'])

# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit_transform(DF['predictor'])
```