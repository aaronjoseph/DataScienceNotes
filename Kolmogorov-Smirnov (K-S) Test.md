The **Kolmogorov-Smirnov (K-S) Test** is a non-parametric statistical method used to compare a sample distribution with a reference probability distribution or to compare two sample distributions. It assesses the similarity between distributions without assuming a specific form for them.

## Types of Kolmogorov-Smirnov Tests

| Test Type            | Purpose                                                                 | Null Hypothesis                                   | Alternative Hypothesis                                    |
| -------------------- | ----------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- |
| One-Sample K-S Test  | Compare a sample's distribution to a specified theoretical distribution | The sample comes from the specified distribution. | The sample does not come from the specified distribution. |
| Two-Sample K-S Test  | Compare the distributions of two independent samples                    | The two samples come from the same distribution.  | The two samples come from different distributions.        |
| Goodness-of-Fit Test | Assess how well a sample fits a hypothesized distribution               | The sample fits the hypothesized distribution.    | The sample does not fit the hypothesised distribution.    |
### One-Sample K-S Test

The **One-Sample K-S Test** assesses whether a sample comes from a specified theoretical distribution.

- **Hypotheses**:
  - **Null Hypothesis ($H_0$)**: The sample follows the specified distribution.
  - **Alternative Hypothesis ($H_A$)**: The sample does not follow the specified distribution.

- **Decision Rule**: Reject the null hypothesis if the **p-value** is less than the significance level (e.g., 0.05), indicating that the sample distribution significantly differs from the theoretical distribution.

```python
import numpy as np
from scipy.stats import kstest

# Sample data
data = np.random.normal(loc=0, scale=1, size=100)

# Perform the one-sample K-S test against the normal distribution
statistic, p_value = kstest(data, 'norm')

# Significance level
alpha = 0.05

# Output results and interpretation
print(f"K-S Statistic: {statistic}, P-value: {p_value}")
if p_value < alpha:
    print("Reject the null hypothesis. The sample does not follow the normal distribution.")
else:
    print("Fail to reject the null hypothesis. The sample follows the normal distribution.")
```

### Two-Sample K-S Test

The **Two-Sample K-S Test** compares two independent samples to determine if they come from the same distribution.

- **Hypotheses**:
  - **Null Hypothesis ($H_0$)**: The two samples come from the same distribution.
  - **Alternative Hypothesis ($H_A$)**: The two samples come from different distributions.

- **Decision Rule**: Reject the null hypothesis if the **p-value** is less than the significance level (e.g., 0.05), indicating a significant difference between the distributions of the two samples.

```python
import numpy as np
from scipy.stats import ks_2samp

# Sample data
sample1 = np.random.normal(loc=0, scale=1, size=100)
sample2 = np.random.normal(loc=0.5, scale=1, size=100)

# Perform the two-sample K-S test
statistic, p_value = ks_2samp(sample1, sample2)

# Significance level
alpha = 0.05

# Output results and interpretation
print(f"K-S Statistic: {statistic}, P-value: {p_value}")
if p_value < alpha:
    print("Reject the null hypothesis. The two samples come from different distributions.")
else:
    print("Fail to reject the null hypothesis. The two samples come from the same distribution.")
```

### Goodness-of-Fit Test

The **Goodness-of-Fit Test** is essentially the one-sample K-S test, used to assess how well a sample fits a specified distribution.

- **Hypotheses**:
  - **Null Hypothesis ($H_0$)**: The sample fits the specified distribution.
  - **Alternative Hypothesis ($H_A$)**: The sample does not fit the specified distribution.

- **Decision Rule**: Reject the null hypothesis if the **p-value** is less than the significance level (e.g., 0.05), indicating that the sample does not fit the specified distribution.
### Historical Background
- **Andrei Kolmogorov (1933)**: Introduced the empirical cumulative distribution (ECD) and a test statistic to measure the maximum difference between the ECD and a theoretical cumulative distribution (TCD).
- **Nikolai Smirnov (1939)**: Independently developed a similar approach to compare two independent samples using the maximum difference between their ECDs.
- **Collaboration**: Upon discovering their concurrent work, Kolmogorov and Smirnov combined their efforts, leading to the development of the Kolmogorov-Smirnov Test.
### Purpose and Applications
- **Goodness-of-Fit Test**: Determines if a sample comes from a specified distribution by comparing the sample's ECD to the TCD.
- **Two-Sample Test**: Compares the ECDs of two independent samples to assess if they originate from the same distribution.
- **Versatility**: Widely used in fields such as social sciences, economics, biology, physics, and engineering to evaluate distribution normality, compare sample distributions, and assess model fit.
### Test Statistic
- **D Statistic**: Represents the maximum absolute difference between the ECD and the TCD (or between two ECDs in the two-sample test). A larger D value indicates a greater discrepancy between the distributions.
### Hypotheses
- **Null Hypothesis ($H_0$)**: The sample distribution matches the reference distribution, or both sample distributions are identical.
- **Alternative Hypothesis ($H_A$)**: The sample distribution differs from the reference distribution, or the two sample distributions are not identical.
### Interpretation
- **P-Value**: Calculated to determine the significance of the observed D statistic.
  - If the p-value is less than the chosen significance level (e.g., 0.05), reject $H_0$, indicating a significant difference between the distributions.
  - If the p-value is greater than the significance level, fail to reject $H_0$, suggesting no significant difference between the distributions.
### Practical Considerations
- **Sample Size**: Larger samples provide more reliable results.
- **Model Validation**: The K-S Test is useful for validating statistical models by comparing the model's predicted distribution to the observed data distribution.
- **Data Science Applications**: Employed in machine learning and artificial intelligence for tasks such as model performance comparison, feature selection, and anomaly detection.
The Kolmogorov-Smirnov Test remains a fundamental tool in statistical analysis, offering a robust method for comparing distributions without relying on specific parametric assumptions. 





The K-S test is widely used due to its non-parametric nature, meaning it does not assume a specific distribution for the data, making it versatile for various applications in statistics and data analysis. 