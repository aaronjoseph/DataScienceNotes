Z-test is a statistical test for which the distribution of the test statistic under the null hypothesis can be approximated by a normal distribution

Z Test Value 

$$Z-Score = \frac{\delta(Mean)}{SE}$$
$$SE = \frac{\sigma}{\sqrt{n}}$$

For 2 distribution the formulae will be


$$\frac{\mu_1-\mu_2}
{\sqrt{\frac{\sigma_1^2}{n_1} + 
\frac{\sigma_2^2}{n_2}}}$$

> In some sense, Z-value represents the number standard deviation the observed difference is from the mean, higher the value, lesser the likelihood of $H_0$ 

To Compute the P-Value

```py
from scipy.stats import norm
norm.sf(Z-Score) # Gives the P-Value
norm.cdf(Z-Score) # Gives (1 - P-value)
```

### Z-Test for conversion Rates
Chi-Squre test is generally used for converstion rates, however, Z-test can also be utilized for the same. Herein the steps are as follows

1. Obtain $\mu$ by asssuming numeric value to the conversion
2. Next, obtain variance for both Control and Treatment Class
	1. Variance = ($\mu * (1-\mu)$)
3. Then plug the same formulae as above

The cons of this technique is that this is p-value is lower than $\chi^2$