#sim 

In a random event a [[Random Variable]] can take any value, often times, certain values come across more frequent than others.

`Probability Mass Function` is probability distribution for `discrete random variable`
`Probability Density Function` is probability distribution for `continous random variable`

>`Probability Distribution Function` is used to infer the probability of [[Random Variable]] falling within a particular range of values. Probability density function is non-negative everywhere and its integral over the entire space is 1, integral of PDF/PMF gives [[Cumulative Density Function]]

---

### Types of Distribution
<a href ="https://www.datacamp.com/community/tutorials/probability-distributions-python"> DataCamp_Link </a>

- Uniform Distribution - Here all random variables are the same

- [[Normal Distribution]]/ Gaussian Distribution
Normal distribution mimics many naturally occuring phenomena, atleast approximately. Normal distribution with 
$\mu = 0$  
$\sigma = 1$
is called `standard distribution`

Keep Random State to a fixed number to maintain reproducibility
```py
from scipy.stats import norm
data_normal = norm.rvs(size=1000,loc=0,scale=1)

scipy.stats.norm.cdf(0)
# This will give 0.5 since mean = 0, mid-point
```
scale = Standard Deviation
loc = Mean

- Gamma Distribution
Exponential, chi-squared, erlang distribution are special cases of gamma distribution

```py
from scipy.stats import gamma
gamma.rvs(a=5, size =10000)
```

- Exponential Distribution
The Cumulative Distribution Function of exponential distribution is defined by $CDF(x) = 1 - e^{-\lambda x}$ where $\lambda$ 

```py
from scipy.stats import expon
expon.rvs(scale=1, loc=0, size=10000)
```

- Poisson Distribution
Is a preferred use-case to account for outlier values

```py
from scipy.stats import poisson
poisson.rvs(mu=3, size=1000)
```

- Binomial Distribution
A distribution where only two outcomes are present & the probability of each trail is independent of each other

```py
from scipy.stats import binom
binom.rvs(n=10,p=0.8,size=10000)
```
Here p is the probability & n is the number of class

- Bernoulli Distribution
Has two outcomes, similar to the above in some aspects

```py
from scipy.stats import bernoulli
bernoulli.rvs(size=10000,p=0.6)
```

