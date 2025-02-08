Spearman's rank correlation coefficient is a non-parametric measure that assesses the strength and direction of the monotonic relationship between two variables. Unlike Pearson's correlation, which evaluates linear relationships, Spearman's correlation focuses on the ranks of the data rather than their raw values, making it particularly useful for ordinal data or data that do not meet the assumptions of parametric tests.

**Key Points:**

- **Definition:** Spearman's rank correlation coefficient, denoted by ρ (rho) or $r_s$, measures the strength and direction of the association between two ranked variables. It ranges from -1 to +1, where:
	- +1 indicates a perfect positive monotonic relationship.
	- -1 indicates a perfect negative monotonic relationship.
	- 0 indicates no monotonic relationship.

- **Calculation Steps:**

1. **Rank the Data:** Assign ranks to the data points for both variables. In cases of tied values, assign the average of the ranks that would have been assigned if there were no ties.
2. **Compute Rank Differences:** For each pair of observations, calculate the difference between the ranks  $d_i$ of the two variables.
3. **Square the Differences:** Square each of the rank differences to get $d_i^2$
4. **Sum of Squared Differences:** Sum all the squared differences to obtain $\sum d_i^2$.
5. **Apply the Formula:** Use the formula to calculate the coefficient:
$$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$
where \( n \) is the number of data pairs.

- **Interpretation:** The value of $r_s$ indicates the strength and direction of the monotonic relationship between the variables. A value close to +1 or -1 signifies a strong monotonic relationship, while a value close to 0 suggests a weak or no monotonic relationship.

- **Advantages:**

- Does not assume a normal distribution of the data.
- Suitable for ordinal data and continuous data that do not meet parametric assumptions.
- Less sensitive to outliers compared to Pearson's correlation.

- **Limitations:**
- Only detects monotonic relationships; it may not accurately reflect the strength of more complex associations.
- Less powerful than parametric tests when the assumptions of the parametric tests are met.
