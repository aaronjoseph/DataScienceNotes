Financial data is mostly time-series in nature. Time-series data is set of observations collected over a successive period of time.

`Need for correlation` - Correlation measures the strenght of the relationship between variables co-movement.[[Correlation and Covariance|Correlation]] value lies between -1 and 1.

Correlation fails in time series data, due to volatile nature of financial variables. Hence, we could calculate the cointegration between time series.

`Cointegration is when the time series are linearly combined to quantify how closely the time series move together`

> Time series are considered cointegrated if their mean and standard deviation is constant after they have been linearly combined

We can use the statsmodel Python library to test for no-cointegration of a univariate equation.

-   The null hypothesis is no cointegration.
-   This uses the augmented Engle-Granger two-step cointegration test.

```py
import statsmodels.tsa.stattools as ts   
result=ts.coint(x, y)
```