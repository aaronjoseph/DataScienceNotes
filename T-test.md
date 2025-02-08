A **t-test** is a statistical method used to determine if there is a significant difference between the means of two groups. It's particularly useful when dealing with small sample sizes and is foundational in hypothesis testing. Sometimes t-tests are called "Student's" t-tests, a reference to their unique history. The name originates from William Sealy Gosset, a brewer at the Guinness Brewery, who published the method under the pseudonym "Student" to maintain confidentiality.  
## Types of t-Tests

| Number of Group Means | Group Type                    | T Test            |
| --------------------- | ----------------------------- | ----------------- |
| One                   |                               | One-sample t-test |
| Two                   | Different items in each group | Two-sample t-test |
| Two                   | Same items in both groups     | Paired t-test     |
### One-Sample t-Test

The **One-Sample T-Test** is used to compare the mean of a sample to a reference value, helping to determine if there is a statistically significant difference between the sample mean and the population/reference mean. This test is particularly useful when evaluating claims made about a population mean in a specific subject area.
- **Hypotheses**:
    - **Null Hypothesis ($H_0$)**: The population mean equals the reference value ($\mu = \mu_0$).
    - **Alternative Hypothesis ($H_A$)**: The population mean does not equal the reference value ($\mu \neq \mu_0$).
- **Decision Rule**: Reject the null hypothesis if the **p-value** is less than the significance level (e.g., 0.05). A low p-value suggests that the difference between the sample mean and the reference value is statistically significant, indicating that the sample data supports the idea that the population mean differs from the reference value.

```python 
from scipy.stats import ttest_1samp

# Sample data and reference value
coffee_volumes = [15.8, 16.2, 15.9, 16.1, 15.7, 16.3, 15.6, 16.0, 15.9, 16.1]
reference_value = 17
alpha = 0.05  # Significance level

# Perform the one-sample t-test
t_stat, p_value = ttest_1samp(coffee_volumes, reference_value)

# Output results and interpretation
print(f"T-statistic: {t_stat}, P-value: {p_value}")
print("Mean is significantly different from the reference value." if p_value < alpha else "Mean is not significantly different from the reference value.")
```

### Two-Sample T-Test Summary

The **Two-Sample T-Test** (or Independent T-Test) compares the means of two independent groups to check for statistically significant differences, commonly used in experimental research (e.g., treatment vs. control groups).
#### Hypotheses
- **Null Hypothesis ($H_0$)**: Population means are equal ($\mu_1 = \mu_2$).
- **Alternative Hypothesis ($H_A$)**: Population means are not equal ($\mu_1 \neq \mu_2$).
- **p-value Interpretation**:
  - **p ≤ α**: Reject $H_0$ (significant difference).
  - **p > α**: Fail to reject $H_0$ (no significant difference).

Reject the null hypothesis if the **p-value** ≤ significance level (e.g., 0.05), indicating a significant difference between means.The two-sample t-test is widely applicable for comparing group means in research and clinical studies.

```python
import numpy as np  
from scipy.stats import ttest_ind  
  
control_group = [100, 98, 102, 97, 101, 99, 103, 96, 100, 102, 99, 101, 98, 100, 99]  
treatment_group = [109, 110, 111, 108, 112, 109, 111, 107, 110, 109, 110, 111, 108, 109, 112]  
  
# Perform the two-sample t-test  
t_stat, p_value = ttest_ind(treatment_group, control_group)  
  
# Significance level  
alpha = 0.05  
  
# Output the results  
print(f"T-statistic: {t_stat}")  
print(f"P-value: {p_value}")  
  
# Interpret the result  
if p_value < alpha:  
    print("Reject the null hypothesis. There is a statistically significant difference between the two group means.")  
else:  
    print("Fail to reject the null hypothesis. There is no statistically significant difference between the two group means.")
```

### Paired Sample t-Test

The **Paired Sample T-Test** is used to test if the mean difference between two related measurements (e.g., "before" and "after") is significantly different from zero. It’s useful for studies where each subject is measured twice, allowing subjects to serve as their own control.

- **Purpose**: Determines if the mean difference between paired scores is significantly different from zero.
- **Hypotheses**:
	- **Null ($H_0$)**: Mean difference is zero ($\mu_D = 0$).
	- **Alternative ($H_A$)**: Mean difference is not zero ($\mu_D \neq 0$).

**Decision Rule**: Reject the null hypothesis if **p-value ≤ 0.05**, suggesting a significant effect.


```python
import numpy as np  
from scipy.stats import ttest_rel  
  
# Sample data: IQ scores before and after treatment  
before_treatment = [100, 102, 98, 97, 105, 99, 103, 100, 98, 101, 99, 102, 100, 99, 97]  
after_treatment = [109, 110, 104, 103, 113, 106, 111, 107, 105, 109, 106, 110, 108, 107, 104]  
  
# Perform the paired sample t-test  
t_stat, p_value = ttest_rel(after_treatment, before_treatment)  
  
# Significance level  
alpha = 0.05  
  
# Output the results  
print(f"T-statistic: {t_stat}")  
print(f"P-value: {p_value}")  
  
# Interpret the result  
if p_value < alpha:  
    print("Reject the null hypothesis. There is a statistically significant difference between the before and after scores.")  
else:  
    print("Fail to reject the null hypothesis. There is no statistically significant difference between the before and after scores.")
```

## Assumptions of t-Tests

- **Normality**: Data should be approximately normally distributed.
- **Homogeneity of Variance**: Samples should have similar variances.
- **Independence**: Observations must be independent of each other.

## Performing a t-Test

1. **Formulate Hypotheses**:
   - **Null Hypothesis ($H_0$)**: Assumes no difference between group means.
   - **Alternative Hypothesis ($H_1$)**: Assumes a significant difference between group means.
2. **Calculate the t-Statistic**:
   For an independent t-test:
   $$
   t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}
   $$
   Where:
   - $\bar{X}_1, \bar{X}_2$: Sample means
   - $S_1^2, S_2^2$: Sample variances
   - $n_1, n_2$: Sample sizes
3. **Determine Degrees of Freedom (df)**:
   For an independent t-test:
   $$
   df = n_1 + n_2 - 2
   $$
4. **Find the Critical t-Value**:
   Use a t-distribution table or software, considering the chosen significance level (e.g., 0.05) and the calculated degrees of freedom.
5. **Compare and Conclude**:
   If the absolute value of the calculated t-statistic exceeds the critical t-value, reject the null hypothesis, indicating a significant difference between group means.
   
## Practical Considerations

- **Sample Size**: Larger samples provide more reliable results.
- **Effect Size**: Beyond statistical significance, consider the practical significance of the difference.
