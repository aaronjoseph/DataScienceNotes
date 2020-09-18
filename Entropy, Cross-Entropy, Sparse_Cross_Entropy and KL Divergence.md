Entropy $H(p)=-\sum_{i}p_ilog_2(p_i)$

Entropy/Chaos theory originated in thermodynamics as a measure of molecular disorder, entropy approaches zero when molecules are still and well ordered. Entropy reached 'Shannons Information Theory' where it indicated average information content of message, entropy is zero when all messages are identical.

Entropy is defined as the average level of "information", "suprise", or "uncertainity" inherent in the variable's possible outcomes. In data science, entropy measure the level of impurity.

> Higher the entropy, harder it is to draw any conclusion from the information

Cross-entropy is a cost-function used for training. The concepts are drawn from Information Theory.

Cross-Entropy is basically the average message length. Cross-Entropy = Entropy + KL Divergence

---

Cross-Entropy Equation

$$J(w) = -(1/N)*\sum_{i=1}^{N}[y_ilog(\hat{y_i}) + (1-y_i)log(1-\hat{y_i})]$$

Sparse_Categorical_Cross_Entropy & Categorical_Cross_Entropy

- For the above, use Categorical_Cross_Entropy when $Y_i$ is one-hot encoded
- When $Y_i$ are integers use Spare_Cross_Entropy
- Both use the above loss function