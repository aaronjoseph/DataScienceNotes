[[AB Testing]]
[[Z-Test]]
[[Chi-Squared Hypothesis Testing]]
[[T-test]]


![[Attachements/Pasted image 1.png]]

---
### Basic requirements

Hypothesis Testing required 3 important factors
1. Data for testing - `Test Statistics`
2. Null or Primary Hypothesis or Status Quo - It needs something to reject or fail to reject
3. Alternative Hypothesis - A decision about whether or not to reject or fail to reject the Null Hypothesis
Hypothesis testing is used when given a sample and an apparent effect, what is the probability of seeing such an effect by chance?


>This is a mathematical method of `proof by contradiction`, wherein to prove a phenomenon A, we assume it to be false, then contradict the assumption, thereby concluding A is true

---
![[Types-of-Hypothesis-Tests.jpg]]

`Two-Sided or Two Tailed Test` - In these situation, the alternative hypothesis is generally expressed in the form "x is not equal to y"

`One-sided or One-tailed test` - In these situation, the alternative hypothesis will be in the form "x is greater/lesser than y"

---
### Examples of Hypothesis testing with code
- One Population Proportion

Research Question : In previous years, 52% of parents believed that electronics and social media was the cause of their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media?

Null Hypothesis : 0.52
Alternate Hypothesis : p > 0.52 (`One Tailed Test`)

Data : 1018 people surveyed. 56% of the samples belive sleep deprivation is due to electronics and social media.

Approach : Single group proportion uses z-statistics test.

```py
from statsmodel.api as sm
import numpy as np
import matplotlib.pyplot as plt

n = 1018
pnull = 0.52
phat = 0.56

# Alternative here is larger indicates one-sided test
sm.stats.proportions_ztest(phat*1018, 1018, 0.52, alternative='larger')

#>> (2.571067795759113, 0.005069273865860533)
```

Since p-value is 0.05, we can reject the null hypothesis and therefore, consider the fact there is a good chance of this proportion being more than 52%


- Difference in population proportions

Research question: Is there a significant difference between the population proportions of parents of black children and parents of Hispanic children who report that their child has had some swimming lessons?

Population Parameter : All children between 6-18 with parents being Black or Hispanic

Parameter of Interest : P1-P2, where p1 = Black and p2 = Hispanic
Null Hypothesis : p1-p2 = 0
Alternate Hypothesis : p1 - p2 $\neq$ 0

Data: 247 Parents of Black Children. 36.8% of parents report that their child has had some swimming lessons. 308 Parents of Hispanic Children. 38.9% of parents report that their child has had some swimming lessons.

Approach: Difference in population proportion needs t-test.

```py
n1 = 247
p1 = .37

n2 = 308
p2 = .39

population1 = np.random.binomial(1, p1, n1)
population2 = np.random.binomial(1, p2, n2)
sm.stats.ttest_ind(population1, population2)
```

- One population Mean

Research Question: Let’s say a cartwheeling competition was organized for some adults. The data looks like following,
(80.57, 98.96, 85.28, 83.83, 69.94, 89.59, 91.09, 66.25, 91.21, 82.7 , 73.54, 81.99, 54.01, 82.89, 75.88, 98.32, 107.2 , 85.53, 79.08, 84.3 , 89.32, 86.35, 78.98, 92.26, 87.01)

Is the average cartwheel distance (in inches) for adults more than 80 inches?

Population: All adults

Parameter of Interest: μ, the population mean cartwheel distance.

Null Hypothesis: μ = 80
Alternative Hypothesis: μ > 80

Data:
25 adult participants.
μ=83.84
σ=10.72

Approach : use Z-test with alternate = 'larger' to denote one-tailed test

```py
sm.stats.ztest(cwdata, value = 80, alternative = "larger")
>> (1.756973189172546, 0.039461189601168366)
# Hence reject Null Hypothesis
```

- Difference in population mean

Research Question: Considering adults in the NHANES data, do males have a significantly higher mean Body Mass Index than females?

Population: Adults in the NHANES data.

Parameter of Interest: μ1−μ2 of Body Mass Index.

Null Hypothesis: μ1=μ2
Alternative Hypothesis: μ1≠μ2

Data: 2976 Females, μ1=29.94, σ1=7.75
          2759 Male Adults, μ2=28.78, σ2=6.25
           μ1−μ2=1.16
		   
Approach: We can again use the z-statistic for this hypothesis testing. But here the test has to be “two-sided” as an inequality appears in the alternative hypothesis i.e. the BMI can be either higher or lower for males than females. Both side probabilities have to be added for p-value calculation.

```py
url = "https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv"
da = pd.read_csv(url)
females = da[da["RIAGENDR"] == 2]
male = da[da["RIAGENDR"] == 1]
sm.stats.ztest(females["BMXBMI"].dropna(), male["BMXBMI"].dropna(),alternative='two-sided')
>> (6.1755933531383205, 6.591544431126401e-10)
# Hence reject Null Hypothesis

```

---
### Formulae

Z-Score
$$\frac{\mu_1 - \mu_2}{\frac{\sigma}{\sqrt{No of Observations}}}$$

---
### Pointers

Chi-Square - Used as a test of independence of two categorical variables

Z-test - A z-test is a stastical test to determine whether two population means are different when the variances are known and the sample size > 30

t-test hypothesis testing is used for variance is unknown and sample size < 30. It is a type of inferential statistics. It is used to decide whether that is a significant difference between the means of two groups

`P-Value`  The probability that an effect could occur by chance. The true meaning of p-value is that alternative hypothesis is never accepted, it just show sufficient/not-sufficient evidence in favor of rejecting the null hypothesis

A p-value is the probability of observing results at least as extreme as those measured when the null hypothesis is true

`Statistically Significant`  An effect is statistically significant if it is unlikely to occur by chance

`Null hypothesis`  A model of a system, based on the assumption that an apparent effect is due to chance
