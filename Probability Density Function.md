>`Probability Distribution Function` is used to infer the probability of random variable falling within a particular range of values. Probability density function is non-negative everywhere and its integral over the entire space is 1
>`Random Variable` is a variable whose numerical outcome is that of a random phenomenon. There are two types of radom variables - Discrete [1,2,3,...] and continous [1.1,1.2,...] random variable
---

### Types of Distribution
<a href ="https://www.datacamp.com/community/tutorials/probability-distributions-python"> DataCamp_Link </a>

- Uniform Distribution - Here all random variables are the same

- Normal Distribution/ Gaussian Distribution
Keep Random State to a fixed number to maintain reproducibility
```py
from scipy.stats import norm
data_normal = norm.rvs(size=1000,loc=0,scale=1)
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

```py
from scipy.stats import expon
expon.rvs(scale=1, loc=0, size=10000)
```

- Poisson Distribution
Is a preferred use-case to account for outlier values

```py
from scipy.stats import poisson
poisson.rvs(mu=3, size 1000)
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

