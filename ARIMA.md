---
tags:
  - "ds-foundations"
---

## Overview

ARIMA stands for **AutoRegressive Integrated Moving Average**. It forecasts a single time series from its own past values and past forecast errors, after differencing the series until it is roughly stationary.[^fpp-arima] It is a standard baseline for short-term univariate forecasting, alongside [[Exponential Smoothing]].

The three letters describe three parts:

- **AR (autoregressive):** regress the current value on its own lagged values.
- **I (integrated):** difference the series to remove a changing level; "integration" is the reverse of differencing.
- **MA (moving average):** regress on lagged forecast errors.

The model is written ARIMA($p,d,q$): $p$ AR lags, $d$ rounds of differencing, and $q$ MA lags.

## Prerequisites

- **Stationarity:** the statistical properties of the series do not depend on when you observe it. Trends and seasonality make a series non-stationary; white noise is stationary.[^fpp-stationarity] A series with irregular cycles but no trend or seasonality can still be stationary.
- **White noise $\varepsilon_t$:** uncorrelated errors with mean zero and constant variance.
- **Differencing:** the first difference is the change between consecutive observations,

$$
y'_t = y_t - y_{t-1}.
$$

The differenced series has one fewer value. A second difference models the "change in the changes"; beyond second differences is rarely needed.[^fpp-stationarity]

- **Autocorrelation:** the correlation between $y_t$ and $y_{t-k}$; see [[Correlation and Covariance]] and the summary statistics in [[Time Series]].

## The Three Components

### AR($p$): autoregression

The original version of this note wrote the AR model with lagged values of the target as the predictors:

$$
Y = B_0 + B_1 Y_{\text{lag}1} + \dots + B_n Y_{\text{lag}n}
$$

In the usual notation, with $\phi$ for the coefficients and an explicit error term:

$$
y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \varepsilon_t
$$

This looks like [[Linear Regression]] with lags as features. For stationarity, the coefficients are constrained; for AR(1), $-1 < \phi_1 < 1$.[^fpp-ar] With $\phi_1 = 1$ and $c = 0$, AR(1) becomes a random walk.

### I($d$): differencing

Apply $d$ rounds of differencing, then fit AR and MA terms to the differenced series $y'_t$. Differencing stabilises the mean; a log or other transformation may be needed separately to stabilise a growing variance.[^fpp-stationarity]

### MA($q$): moving average of past errors

$$
y_t = c + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}
$$

This is **not** the moving-average smoothing listed in [[Time Series]]. MA smoothing estimates the past trend-cycle; an MA model forecasts future values from past forecast errors.[^fpp-ma] MA models are normally constrained to be *invertible*; for MA(1), $-1 < \theta_1 < 1$, so recent observations carry more weight than distant ones.

## The Full ARIMA($p,d,q$) Model

With $y'_t$ denoting the series after $d$ differences:[^fpp-arima]

$$
y'_t = c + \phi_1 y'_{t-1} + \dots + \phi_p y'_{t-p} + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q} + \varepsilon_t
$$

Using the backshift operator $B y_t = y_{t-1}$, the same model is

$$
(1 - \phi_1 B - \dots - \phi_p B^p)(1 - B)^d y_t = c + (1 + \theta_1 B + \dots + \theta_q B^q)\varepsilon_t.
$$

Several familiar models are special cases:

| Model | ARIMA form |
|---|---|
| White noise | ARIMA(0,0,0), no constant |
| Random walk | ARIMA(0,1,0), no constant |
| Random walk with drift | ARIMA(0,1,0), with constant |
| Autoregression | ARIMA($p$,0,0) |
| Moving average | ARIMA(0,0,$q$) |

### How $c$ and $d$ shape long-horizon forecasts

The constant and the amount of differencing determine what the forecasts do far ahead:[^fpp-arima]

- $c = 0$, $d = 0$: forecasts go to zero.
- $c \ne 0$, $d = 0$: forecasts go to the mean of the data.
- $c = 0$, $d = 1$: forecasts go to a non-zero constant.
- $c \ne 0$, $d = 1$: forecasts follow a straight line.
- $c = 0$, $d = 2$: forecasts follow a straight line.

A higher $d$ also makes prediction intervals widen faster. Cyclic forecasts need $p \ge 2$ and suitable coefficients.

## Choosing $p$, $d$, and $q$

1. **Plot and transform.** Look for trend, seasonality, and changing variance.
2. **Choose $d$ first.** Difference as few times as necessary: over-differencing creates spurious autocorrelation. A unit-root test helps; the KPSS test has stationarity as its null hypothesis, so a small p-value suggests differencing.[^fpp-stationarity] See [[Hypothesis Testing]] and [[P-Value]].
3. **Choose $p$ and $q$.** On the differenced data, ACF and PACF plots can suggest a pure AR or pure MA model:[^fpp-arima]
   - ARIMA($p,d,0$): the ACF decays exponentially or sinusoidally; the PACF has a significant spike at lag $p$ and none beyond it.
   - ARIMA($0,d,q$): the PACF decays; the ACF has a significant spike at lag $q$ and none beyond it.
   - When both $p$ and $q$ are positive, the plots do not identify the orders; compare candidates with an information criterion instead.
4. **Compare candidates with AICc**, but only for models with the same $d$. Differencing changes the data on which the likelihood is computed, so AIC values across different $d$ are not comparable.[^fpp-estimation]
5. **Check residuals.** They should resemble white noise; a Ljung–Box test examines several autocorrelations at once.[^fpp-stationarity]

## Worked Example: Forecast an ARIMA(1,1,0) by Hand

**Inputs:**

- Last two observations: $y_{T-1} = 100$ and $y_T = 104$.
- Fitted model on the first differences: $y'_t = c + \phi_1 y'_{t-1} + \varepsilon_t$ with $c = 0.5$ and $\phi_1 = 0.4$.
- Future errors are forecast as zero.

**Step 1: latest difference.**

$$
y'_T = 104 - 100 = 4
$$

**Step 2: forecast the next difference.**

$$
\hat{y}'_{T+1} = 0.5 + 0.4 \times 4 = 2.1
$$

**Step 3: undo the differencing.**

$$
\hat{y}_{T+1} = 104 + 2.1 = 106.1
$$

**Step 4: repeat for the second step ahead.**

$$
\hat{y}'_{T+2} = 0.5 + 0.4 \times 2.1 = 1.34
$$

$$
\hat{y}_{T+2} = 106.1 + 1.34 = 107.44
$$

**Step 5: long-run change per period.** The forecast differences converge to the mean of the stationary AR(1),

$$
\mu = \frac{c}{1 - \phi_1} = \frac{0.5}{0.6} \approx 0.833.
$$

The recent jump of 4 decays towards a steady increase of about 0.833 per period. The level forecasts therefore approach a straight line, as expected for $c \ne 0$ and $d = 1$. These parameters are illustrative, not estimates from real data.

## Python Example

The following sketch uses statsmodels. It was executed with statsmodels 0.15.0 and NumPy 2.4.6.

```python
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

rng = np.random.default_rng(0)
y = 100 + np.cumsum(0.8 + rng.normal(size=200))  # random walk with drift

train, test = y[:180], y[180:]
model = ARIMA(train, order=(1, 1, 0), trend="t")
result = model.fit()
print(result.summary())

forecast = result.get_forecast(steps=len(test))
print(forecast.predicted_mean[:5])
print(forecast.conf_int()[:5])
```

statsmodels includes no trend term by default when $d > 0$; `trend="t"` adds a linear time trend, which becomes a drift after differencing. It includes trend terms as regression with ARIMA errors, so the fitted trend coefficient estimates the mean change $\mu$, not the constant $c$ in the equations above.[^statsmodels]

In this run the trend coefficient (`x1`) was 0.831 against a true drift of 0.8. The AR coefficient was 0.048 with $p = 0.54$, consistent with the true value of 0, since the simulated series is a random walk with drift. The first forecast was 250.44, with a 95% interval of $[248.55, 252.34]$; the intervals widen at each later step.

## Limitations & Common Pitfalls

- **Linear and univariate.** ARIMA extrapolates linear dependence on the series' own past. Known drivers such as promotions or holidays need regression with ARIMA errors (ARIMAX) or another model.
- **Seasonality needs its own terms.** Weekly or yearly patterns call for seasonal differencing and a seasonal ARIMA (SARIMA).
- **Over-differencing** introduces false dynamics; each extra difference must be justified.[^fpp-stationarity]
- **Structural breaks** such as a product launch or policy change violate the assumption that one model describes the whole history.
- **Time-ordered evaluation.** Random row splits leak the future into training; use a rolling-origin evaluation instead. See [[Cross Validation]] and [[Data Leakage]].
- **Automatic order selection is not understanding.** Check the residuals and whether the long-run forecast shape is plausible.

## Exercise

A daily series of search query volume grows steadily and peaks every weekend. Which ARIMA components would you consider, and which pitfall is most likely if you fit a non-seasonal ARIMA(1,1,1)?

> [!example]- Exercise solution
> The steady growth suggests one ordinary difference ($d = 1$), possibly with drift. The weekly peak suggests a seasonal difference at lag 7 and seasonal AR or MA terms, i.e. a SARIMA model. A non-seasonal ARIMA(1,1,1) leaves the weekly pattern in the residuals: they will show autocorrelation at lags 7, 14, …, and forecasts will miss the weekend peaks. Evaluate candidates with a rolling-origin split rather than a random split.

## Related Notes

- [[Time Series]] — Summary statistics, sequence models, and the distinction from moving-average smoothing.
- [[Exponential Smoothing]] — An alternative forecasting family based on weighted past values.
- [[Sequence Models]] — Neural approaches to ordered data.
- [[Research_Paper/Deep and confident predictions for Time Series at Uber]] — An LSTM-based forecasting paper for comparison.

## References & Useful Links

[^fpp-arima]: [Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* (3rd ed.), §9.5 Non-seasonal ARIMA models](https://otexts.com/fpp3/non-seasonal-arima.html) — Model equation, backshift form, special cases, effect of $c$ and $d$, and ACF/PACF identification.
[^fpp-stationarity]: [FPP3 §9.1 Stationarity and differencing](https://otexts.com/fpp3/stationarity.html) — Stationarity, differencing, over-differencing, KPSS unit-root test, and Ljung–Box check.
[^fpp-ar]: [FPP3 §9.3 Autoregressive models](https://otexts.com/fpp3/AR.html) — AR($p$) equation and stationarity constraints.
[^fpp-ma]: [FPP3 §9.4 Moving average models](https://otexts.com/fpp3/MA.html) — MA($q$) equation, the difference from moving-average smoothing, and invertibility.
[^fpp-estimation]: [FPP3 §9.6 Estimation and order selection](https://otexts.com/fpp3/arima-estimation.html) — Maximum likelihood, AICc, and why information criteria cannot select $d$.
[^statsmodels]: [statsmodels `ARIMA` API](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html) — `order`, `trend` defaults with integration, and regression-with-ARIMA-errors treatment of trends.

- [Understanding ARIMA (Time Series Modeling)](https://towardsdatascience.com/understanding-arima-time-series-modeling-d99cd11be3f8) — The note's original reading link; kept for reference but not opened or used to verify claims here.