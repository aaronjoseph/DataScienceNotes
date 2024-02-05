Entropy $H(p)=-\sum_{i}p_ilog_2(p_i)$

Entropy/Chaos theory originated in thermodynamics as a measure of molecular disorder, entropy approaches zero when molecules are still and well ordered. Entropy reached 'Shannons Information Theory' where it indicated average information content of message, entropy is zero when all messages are identical.

Entropy is defined as the average level of "information", "suprise", or "uncertainity" inherent in the variable's possible outcomes. In data science, entropy measure the level of impurity.

> Higher the entropy, harder it is to draw any conclusion from the information

Cross-entropy is a cost-function used for training. The concepts are drawn from Information Theory.

Cross-Entropy is basically the average message length. Cross-Entropy = Entropy + KL Divergence

---

**Cross Entropy - Sparse Categorical/Categorical**

$$J(w) = -(1/N)*\sum_{i=1}^{N}[y_ilog(\hat{y_i}) + (1-y_i)log(1-\hat{y_i})]$$

Sparse_Categorical_Cross_Entropy & Categorical_Cross_Entropy

- For the above, use Categorical_Cross_Entropy when $Y_i$ is one-hot encoded
- When $Y_i$ are integers use Spare_Cross_Entropy
- Both use the above loss function


---
## Code Sample

Cross-Entropy Loss is effective because it penalizes incorrect classifications more severely when the model is confident about its incorrect prediction. It encourages the model to output probabilities close to 0 for wrong classes and close to 1 for the correct class.

$$Loss = - \sum_{c=1}^M y_{true,c} log(y_{pred,c})$$

```python 
def cross_entropy_loss(self, x_pred, y):  
    """  
    Compute Cross-Entropy Loss based on prediction of the network and labels   
    :param x_pred: Probabilities from the model (N, num_classes)    
    :param y: Labels of instances in the batch    
    :return: The computed Cross-Entropy Loss    
    """    
    loss = None  
    num_samples = x_pred.shape[0]  
    log_probs = -np.log(x_pred[range(num_samples), y])  
    loss = np.sum(log_probs) / num_samples  
    return loss
```

Here, 
1. **Understanding `cross_entropy_loss` Function**:
   - `x_pred`: This is a matrix of predicted probabilities for each class for each sample in the batch.
   - `y`: This contains the actual labels for each sample.
   - `num_samples`: Counts the number of samples in `x_pred`.
   - `log_probs`: Calculates the negative logarithm of the probabilities associated with the actual classes from `x_pred`.
   - `loss`: Computes the average loss across all samples by summing `log_probs` and dividing by `num_samples`.

2. **Behavior Based on Predictions**:
   - **Correct Predictions (Probability = 1)**: If the model predicts the correct class with a probability of 1, the log loss is 0, indicating no loss.
   - **Incorrect Predictions (Probability = 0)**: If the model predicts a probability of 0 for the correct class, the log loss tends towards negative infinity, representing a high loss. This case is typically handled with numerical stability techniques to avoid computation issues.

---
## Research Papers

### 1. Theoretical Analysis and Applications
- **Paper**: "Cross-Entropy Loss Functions: Theoretical Analysis and Applications"
- **Link**: [Read the Paper](https://ar5iv.org/html/2304.07288)
- **Summary**: This paper delves into the theoretical aspects of Cross-Entropy Loss, providing insights into its effectiveness and applications in various neural network architectures, including those used for adversarial robustness.

### 2. Training Deep Neural Networks with Noisy Labels
- **Paper**: "Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels"
- **Link**: [Read the Paper](https://ar5iv.org/html/1805.07836)
- **Summary**: This research explores how Cross-Entropy Loss can be adapted for scenarios with noisy data, which is critical for practical applications where data quality cannot always be guaranteed.

### 3. Uses and Abuses in Modern Deep Learning
- **Paper**: "Uses and Abuses of the Cross-Entropy Loss: Case Studies in Modern Deep Learning"
- **Link**: [Read the Paper](https://ar5iv.org/html/2011.05231)
- **Summary**: The paper provides a critical analysis of how Cross-Entropy Loss is used and sometimes misused in current deep learning practices, offering valuable insights for practitioners.

### 4. Structured Entropy
- **Paper**: "Loss Functions for Classification using Structured Entropy"
- **Link**: [Read the Paper](https://ar5iv.org/html/2206.07122)
- **Summary**: This paper introduces the concept of structured entropy in loss functions, expanding the traditional Cross-Entropy Loss to accommodate structured data, which is prevalent in many real-world scenarios.

