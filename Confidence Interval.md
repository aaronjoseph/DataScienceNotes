# Confidence Interval

#search-eng

## Meaning

A 95% frequentist confidence-interval procedure covers the fixed population parameter in 95% of repeated samples under its assumptions. It does not assign a 95% probability to that fixed parameter after this particular interval has been computed.

For independent normally distributed observations with unknown variance, a mean interval is:

$$\bar x\pm t_{0.975,n-1}\frac{s}{\sqrt n}.$$

Here $s$ is sample standard deviation and $n$ is sample size. Normality can sometimes be approximated for the sampling distribution, but outliers and dependence still matter.

## Worked Example

With $n=25$, mean 80 and sample SD 10, standard error is 2. Using $t_{0.975,24}\approx2.0639$ gives $[75.872,84.128]$. This interval estimates a mean, not the range containing 95% of individual observations.

## Search Applications

For two rankers evaluated on the same queries, calculate per-query metric differences and quantify uncertainty in the mean difference. Resample the independent units together for a paired bootstrap. Repeated queries from one user may require user-level clustering; resampling document rows independently can exaggerate precision.

A narrow interval around a negligible improvement is not a useful product win. Report the effect, unit, sampling method, and practical threshold alongside [[Hypothesis Testing]] and [[Search Evaluation]].

## Exercise

Holding variability fixed, quadrupling independent sample size halves standard error. Explain why duplicating the same observations four times does not provide this benefit.

## References & Useful Links

- [NIST confidence limits for the mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) — Formula and interpretation.
