# P-Value

#search-eng

## Overview

A p-value is the probability, under a specified null hypothesis and its assumptions, of obtaining a test statistic at least as extreme as the observed one. “Extreme” depends on the chosen test and whether it is one- or two-sided. [^1]

It is not the probability that the null hypothesis is true, nor the probability that an observed improvement is useful.

## Example

Suppose a preplanned valid test of equal conversion rates gives $p=0.03$ and the significance threshold is $\alpha=0.05$. The result meets that test's rejection criterion. It does not imply a 97% probability that the new search system is better.

Report the estimated effect and [[Confidence Interval|confidence interval]] as well. A statistically detectable difference may be too small to matter, while a nonsignificant result can reflect insufficient precision.

## In Search Experiments

Use with [[AB Testing]] and [[Hypothesis Testing]]. Repeatedly checking a fixed-horizon test and stopping on significance changes the procedure; choose an analysis plan that accounts for when and how decisions are made.

## Practice

Explain why two experiments can have the same p-value but very different business implications.

## References & Useful Links

[^1]: [NIST: Critical values and p-values](https://www.itl.nist.gov/div898/handbook/prc/section1/prc131.htm) — Test statistics, significance levels, and p-value interpretation.
