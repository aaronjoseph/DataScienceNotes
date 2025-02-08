Kendall's Tau is a non-parametric measure that evaluates the strength and direction of the association between two ranked variables. Unlike Pearson's correlation, which requires data to be normally distributed and measures linear relationships, Kendall's Tau assesses ordinal associations without assuming a specific distribution.

**Key Points:**
- **Definition:** Kendall's Tau, denoted as τ (tau), quantifies the ordinal association between two variables. It ranges from -1 to +1, where:
	- +1 indicates a perfect positive association.
	- -1 indicates a perfect negative association.
	- 0 indicates no association.

- **Calculation Steps:**
1. **Identify Concordant and Discordant Pairs:** For each pair of observations, determine if the ranks of both variables move in the same direction (concordant) or in opposite directions (discordant).
2. **Compute Tau:** Use the formula:
\[ τ = \frac{C - D}{C + D} \]
where \( C \) is the number of concordant pairs and \( D \) is the number of discordant pairs.
- **Interpretation:** The value of τ indicates the strength and direction of the ordinal association. Values close to +1 or -1 signify strong associations, while values near 0 suggest weak or no association.
- **Advantages:**
- Does not assume a normal distribution of the data.
- Suitable for ordinal data and for data with many tied ranks.
- Provides a more accurate measure of association in small sample sizes compared to Spearman's rank correlation.
- **Limitations:**
- Only detects monotonic relationships; it may not accurately reflect the strength of more complex associations.
- Less powerful than parametric tests when the assumptions of the parametric tests are met.
