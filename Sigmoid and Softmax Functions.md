Here is an improved version of your Obsidian note on the sigmoid and softmax functions:

---

The sigmoid function is typically used for two-class logistic regression, while the softmax function is used for multi-class logistic regression.

### Comparing Sigmoid and Softmax in Neural Networks

- The sum of the outputs from sigmoid functions may not equal 1, as each output is independent. This allows for the possibility of multiple classes being recognized in a given data point.
- In contrast, softmax function outputs are interconnected, summing to 1. This interdependency means that an increase in the probability of one class will decrease the probability of the others, making it ideal for scenarios where each data point can only belong to one class.

### Use Cases

**Sigmoid:**
- Best suited for multi-label classification where more than one class can be the correct output for a given data point.
- Employed in scenarios requiring non-exclusive outputs, where each output is treated independently.

Sigmoid function formula:
$$ \sigma(z_j) = \frac{1}{1+e^{-z_j}} $$

**Softmax:**
- Applied in multi-class classification tasks where each data point is exclusively assigned to one class.
- Useful when the outputs are mutually exclusive, ensuring that the probabilities of all possible outcomes sum to 1.

Softmax function formula:
$$ \text{softmax}(z_j) = \frac{e^{z_j}}{\sum_{k=1}^{K}e^{z_k}} $$

### Mathematical Nature

Both sigmoid and softmax functions incorporate the exponential constant $e$ (approximately equal to 2.7) [[Exponential Constant - e]]