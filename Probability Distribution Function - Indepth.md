### Mind Map of PDF
![[Pasted image 6.png]]

### Defination of PDF 
![[Probability Density Function]]

### Bernoulli Distribution

This can be depicted by drawing the probability of tossing a coin, there are only two outcomes to this.

The same can be considered for unfair coin toss, where the probability of heads may not be 0.5 but p and (1-p) is the probability of tail

>Bernoulli Distribution can be considered akin to unfair coin toss

$$
f(x) = 
\begin{cases}
p^x * (1-p)^{1-x} \\
0 \\
\end{cases}
$$


### Uniform Distribution Function

Here, you can consider an event where the odds of occuring are equal -> Fair Die

### Binomial and Hypergeometric

Binomial Distribution can be considered as the sum of outcomes of things that follow a Bernoulli distribution.

Consider a situation wherein you are drawing a ball from a combination of black and white balls. If the balls aren't replaced, it is a binomial distribution, however, if the balls are replaced, it is hypergeometric distribution

### Poisson

This can be depicted by packets arrive at routers, or customers arrive at a store, or things wait in some kind of queue, then `Poisson` can be considered. Like Binomial, poisson distribution is the distribution of a count - count of times something happened. It's parameterized not by a probability p and number of trails n but by an average rate $\lambda$ which in this analogy is simply the constant value of np. The Poisson distribution is what you must think of when trying to count events over a time given the continous rate of events occuring.

### Geometric and Negative Binomial

From a simple bernoulli trails arises another distribution. How many times does a flipped coin come up tails before it first comes up heads? This count of tails follows a geometric distribution. Like Bernoulli, this is parameterized by p -> probability of final success, it is not parameterized by n, a number of trails or flips

> If binomial distribution is  "How many successes?" then geometric distribution is "how many failures until a success?"

Negative binomial distribution is a simple generalization, it is the number of failures until r successes have occured, not just 1.

### Exponential and Weibull

Exponential distribution is parameterized by $\lambda$ like poisson.
This can be considered as "time until failure"

Weibull depicts the increasing or decreasing rates of failure over time

### Normal, Log-Normal, Student's t and Chi-Squared

Normal or Gaussian distribution is the most important or recognizable one of all.

Student's t-distribution is the basis of the t-test that is used in reasoning about the mean of a normal distribution and also approaches the normal distribution as its parameter increases. The distinguishing feature of the t-distribution are it's tails, which are `fatter than the normal distribution's`

Chi-squared distribution is the distribution of the sum of squares of normally-distributed values.It’s the distribution underpinning the chi-squared test which is itself based on the sum of squares of differences, which are supposed to be normally distributed.

### Story of t-distribution
>Over 100 years ago, Guinness was using statistics to make better stout. There, William Sealy Gosset developed some whole new stats theory just to grow better barley. Gosset convinced the boss that the other brewers couldn’t figure out how to use the ideas, and so got permission to publish, but only under the pen name “Student”. Gosset’s best-known result is this t-distribution, which is sort of named after him.

### Gamma and Beta

The gamma distribution comes up when modeling the time until the next n events occur. It appears in machine learning as the “conjugate prior” to a couple distributions.

 Beta distribution -it’s the conjugate prior to most every other distribution mentioned above.