# Hypothesis Testing

#search-eng

## What a Test Tells You

A hypothesis test asks how incompatible observations are with a specified null model. A [[P-Value]] is a probability of a result at least as extreme **under that model**, not the probability that the null is true. Rejecting a null provides statistical evidence, not proof of a mechanism; failure to reject does not establish equivalence.

Choose the outcome, independent sampling unit, null, direction, and significance level before inspecting results. Report effect size and a [[Confidence Interval]], not only a threshold decision. Repeated users, query variants, and repeated testing require appropriate dependence and multiplicity handling; see [[AB Testing]].

## Choose the Test from the Design

| Question | Starting point | Important condition |
|---|---|---|
| One binary proportion vs a value | One-proportion z test or exact binomial test | Independent trials; normal approximation needs adequate expected counts |
| Two independent proportions | Pooled two-proportion z test under equality | Use actual success counts, not simulated observations |
| One mean vs a value | One-sample t test | Unknown population variance; independent observations and suitable sampling distribution |
| Two independent means | Welch t test | Unequal variances allowed; observations still independent |
| Same units before/after | Paired analysis | Analyse within-unit differences |

Sample size 30 is not a universal rule for choosing z rather than t. See [[Z-Test]], [[T-test]], and [[Chi-Squared Hypothesis Testing]] for related test families.

## Recalculated Examples

The Python below uses NumPy and SciPy. The first two examples originally supplied rounded percentages, not integer counts: their reconstructed counts are **illustrations**, not recovered source data.

### 1. Parents, Social Media, and Sleep

For 1,018 parents, compare a reported 56% with $p_0=0.52$, using $H_1:p>0.52$. Illustratively take 570 positive answers, or 55.992%. Under the null, use its variance:

$$z=\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}.$$

```python
from scipy import stats
from math import sqrt
n, successes, p0 = 1018, 570, 0.52
z = (successes / n - p0) / sqrt(p0 * (1 - p0) / n)
print(z, stats.norm.sf(z))  # 2.5495, 0.005394 (one-sided)
```

This would reject at a preselected 5% level under the assumptions. Obtain the actual count before reporting a source-data result.

### 2. Swimming Lessons: Two Proportions

The original figures were 36.8% of 247 Black parents and 38.9% of 308 Hispanic parents. Use illustrative counts 91 and 120; these approximate but do not exactly reproduce both reported percentages. Test equality against a two-sided difference. Generating random Bernoulli data and t-testing it adds invented evidence.

```python
from scipy import stats
from math import sqrt
k1, n1, k2, n2 = 91, 247, 120, 308
pooled = (k1 + k2) / (n1 + n2)
z = (k1/n1 - k2/n2) / sqrt(pooled*(1-pooled)*(1/n1+1/n2))
print(z, 2*stats.norm.sf(abs(z)))  # -0.5111, 0.6093
```

Failure to reject here does not demonstrate equal population proportions. The original integer counts remain necessary for an exact reconstruction.

### 3. Cartwheel Distance

Test $H_0:\mu=80$ against $H_1:\mu>80$. Population variance is unknown, so estimate it and use a t test.

```python
import numpy as np
from scipy import stats
x = np.array([80.57,98.96,85.28,83.83,69.94,89.59,91.09,66.25,
              91.21,82.7,73.54,81.99,54.01,82.89,75.88,98.32,
              107.2,85.53,79.08,84.3,89.32,86.35,78.98,92.26,87.01])
print(x.mean(), x.std(ddof=1))  # 83.8432, 10.9370
print(stats.ttest_1samp(x, 80, alternative='greater'))
# t=1.75697, df=24, p=0.0458374
```

This narrowly crosses 5% if the direction was specified beforehand and the independent-sample/normality assumptions are reasonable. Inspect outliers and the sampling process. The former normal-tail p-value of 0.03946 understated the t-test p-value.

### 4. BMI: Two Summary Samples

Female summary: $n=2976$, mean 29.94, SD 7.75. Male summary: $n=2759$, mean 28.78, SD 6.25. The original question asked whether men have higher BMI, but these means point the other way. Here explicitly test a **two-sided** difference using Welch's test.

```python
from scipy import stats
result = stats.ttest_ind_from_stats(
    mean1=29.94, std1=7.75, nobs1=2976,
    mean2=28.78, std2=6.25, nobs2=2759, equal_var=False)
print(result)  # t=6.25972, p=4.14198e-10
```

The observed female-minus-male difference is 1.16 BMI units. This computation treats the summaries as independent simple samples; NHANES uses a complex survey design, so this is a classroom calculation, not a survey-weighted population inference. No raw-data reproduction is claimed.

## Search Exercise

Compare two rankers on the same queries. Explain why query-level paired differences differ from treating every returned document as independent. Define practical importance before selecting a statistical test.

## Existing Illustrations

![[Attachements/Pasted image 1.png]]

![[Types-of-Hypothesis-Tests.jpg]]

## References & Useful Links

- [SciPy one-sample t test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html) — One-sample test and alternatives.
- [SciPy summary-statistic t test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind_from_stats.html) — Welch computation from summaries.
- [Proportion z test](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportions_ztest.html) — Counts and null-variance options.

Previously saved resources (retained for further reading; not used to verify this revision):
- [raw.githubusercontent.com — nhanes_2015_2016.csv"](https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv")
