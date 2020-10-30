The tree that XGBoost uses, is different from the regular decision tree.

Quality Score or Similarity Score = $$\frac{Sum of Residuals Squared}{Number of Residuals + \lambda}$$

$\lambda$ is a regularization parameter

Gain = $Left_{Similarity} + Right_{Similarity} - Root_{Similarity}$

The split for XGBoost tree happens for the combination that has the highest Gain

### Prunning

Prunning is done by considering the Gain Value and $\gamma$

When Gain Value - $\gamma$ < 0, the branch is removed else not removed

New Prediction = Previous Prediction + Learning Rate * Output

Learning Rate is a parameter called eta[value ranges between 0.1 to1, default value = 0.3]

