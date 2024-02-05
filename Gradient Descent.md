#DL 
### Gradient Descent Overview

Gradient descent is an optimization algorithm widely used in deep learning to find the minimum of a function. It iteratively moves towards the minimum of the cost function by updating the parameters in the opposite direction of the gradient of the cost function.

### Key Components of Gradient Descent

1. **Model Selection**: Typically, a model is a function that predicts outputs given inputs, for example, $f(x, W) = Wx$ for linear models, where $W$ represents the weights.

2. **Loss Function**: A loss function $L_i = |y - Wx_i|^2$ quantifies the error between the predicted values and the actual values. The goal is to minimize this function.

3. **Partial Derivatives**: The algorithm computes the gradient of the loss function with respect to each parameter (weight), $\frac{\partial L}{\partial w_j}$.

4. **Parameter Update**: Each parameter is updated in the direction that reduces the loss, $w_j = w_j - \alpha \frac{\partial L}{\partial w_j}$, where $\alpha$ is the learning rate.

5. **Learning Rate**: The learning rate $\alpha$ controls the size of the steps taken towards the minimum of the cost function. It's crucial for ensuring convergence and needs to be set carefully.

### Variants of Gradient Descent

#### Full Batch Gradient Descent

- **Process**: Computes the gradient of the cost function for the entire dataset and performs a single update per iteration.
  
- **Equation**: 
  $$ L = \frac{1}{N} \sum_{i=1}^{N} L(f(x_i, W), y_i) $$

#### Mini-Batch Gradient Descent

- **Process**: Divides the dataset into small batches and performs an update for each mini-batch.
  
- **Advantages**: More efficient in terms of computation than full batch, especially with large datasets.
  
- **Equation**: 
  $$ L = \frac{1}{M} \sum_{i=1}^{M} L(f(x_i, W), y_i) $$
  
  where $M$ is the size of the mini-batch and is typically much smaller than the full dataset size $N$.

### Importance in Deep Learning

- **Scalability**: Gradient descent is computationally more scalable for large datasets compared to direct solution methods.
  
- **Applicability**: It can be applied to a wide range of models, including non-linear models common in deep learning.
  
- **Flexibility**: It allows for online and batch learning, and the various forms of gradient descent (stochastic, mini-batch) offer flexibility for different training needs.

---

## Gradient Descent and Computing Gradients

Gradient descent is an iterative optimization algorithm for finding the minimum of a function. To apply gradient descent, we need to compute the gradients of the loss function with respect to the model's parameters. There are several methods for computing these gradients:

### Methods for Computing Gradients:

1. **Manual Differentiation**: Involves hand-calculating the gradients of the loss function. It's reliable but can be very laborious and error-prone for complex functions.

2. **Symbolic Differentiation**: Uses algebraic manipulation to automatically find the derivatives symbolically. This method can be done using computer algebra systems but may lead to inefficient code and is not feasible for large-scale problems.

3. **Numerical Differentiation**: Approximates the gradients by evaluating the function at two points very close to each other and dividing the change in the function value by the change in the parameter value. This method is easy to implement but can be inaccurate and computationally expensive.

4. **Automatic Differentiation**: Breaks down complex differentiations into simpler parts, using the chain rule, and then combines them to get the overall gradient. This method is highly efficient and accurate, and is widely used in modern deep learning frameworks.

### Analytical Derivation of the Partial Derivative:

For some functions, especially linear functions, we can analytically derive the partial derivatives. For example, consider a simple linear regression model:

$$ f(w, x_i) = w^T x_i $$

with a quadratic loss function:

$$ L = \sum_{i=1}^{N} (y_i - w^T x_i)^2 $$

The gradient descent update rule dictates that we should update $w$ to minimize $L$:

$$ w_j \leftarrow w_j - \eta \frac{\partial L}{\partial w_j} $$

For the quadratic loss function, the partial derivative $\frac{\partial L}{\partial w_j}$ is:

$$ \frac{\partial L}{\partial w_j} = -2 \sum_{i=1}^{N} (y_i - w^T x_i) x_{ij} $$

### Incorporating Non-Linearity (Sigmoid Function):

When a non-linear activation function like the sigmoid $\sigma(x) = \frac{1}{1 + e^{-x}}$ is used, the update rule becomes more complex. The sigmoid function's derivative can be expressed as $\sigma'(x) = \sigma(x)(1 - \sigma(x))$.

The loss function for a model with a sigmoid activation is:

$$ L = \sum_{i=1}^{N} (y_i - \sigma(w^T x_i))^2 $$

The update rule for the weights when using the sigmoid activation is:

$$ w_j \leftarrow w_j - \eta \frac{\partial L}{\partial w_j} $$

where the partial derivative is given by:

$$ \frac{\partial L}{\partial w_j} = \sum_{i=1}^{N} 2(y_i - \sigma(w^T x_i)) \sigma'(w^T x_i) x_{ij} $$

### Mathematics of the Update Rule:

Incorporating the derivative of the sigmoid, the gradient update rule is:

$$ w_j \leftarrow w_j + 2\eta \sum_{i=1}^{N} \delta_i (1 - \sigma_i) x_{ij} $$

where $\sigma_i = \sigma(w^T x_i)$ and $\delta_i = y_i - \sigma_i$.

### Summary:

Combining all the elements, the gradient descent algorithm is used to update the parameters of a model to minimize the loss function. Depending on the complexity of the model, gradients can be computed using manual, symbolic, numerical, or automatic differentiation. For models involving non-linearities like the sigmoid function, the update rule incorporates the derivative of the non-linearity, making the computation of gradients slightly more complex. Automatic differentiation is the preferred method in practice, especially within deep learning frameworks, due to its balance of computational efficiency and accuracy.

---
### Analytical Derivation of the Partial Derivative:

For some functions, especially linear functions, we can analytically derive the partial derivatives. For example, consider a simple linear regression model:

$$ f(w, x_i) = w^T x_i $$

with a quadratic loss function:

$$ L = \sum_{i=1}^{N} (y_i - w^T x_i)^2 $$

The gradient descent update rule dictates that we should update $w$ to minimize $L$:

$$ w_j \leftarrow w_j - \eta \frac{\partial L}{\partial w_j} $$

For the quadratic loss function, the partial derivative $\frac{\partial L}{\partial w_j}$ is:

$$ \frac{\partial L}{\partial w_j} = -2 \sum_{i=1}^{N} (y_i - w^T x_i) x_{ij} $$

### Incorporating Non-Linearity (Sigmoid Function):

When a non-linear activation function like the sigmoid $\sigma(x) = \frac{1}{1 + e^{-x}}$ is used, the update rule becomes more complex. The sigmoid function's derivative can be expressed as $\sigma'(x) = \sigma(x)(1 - \sigma(x))$.

The loss function for a model with a sigmoid activation is:

$$ L = \sum_{i=1}^{N} (y_i - \sigma(w^T x_i))^2 $$

The update rule for the weights when using the sigmoid activation is:

$$ w_j \leftarrow w_j - \eta \frac{\partial L}{\partial w_j} $$

where the partial derivative is given by:

$$ \frac{\partial L}{\partial w_j} = \sum_{i=1}^{N} 2(y_i - \sigma(w^T x_i)) \sigma'(w^T x_i) x_{ij} $$

### Mathematics of the Update Rule:

Incorporating the derivative of the sigmoid, the gradient update rule is:

$$ w_j \leftarrow w_j + 2\eta \sum_{i=1}^{N} \delta_i (1 - \sigma_i) x_{ij} $$

where $\sigma_i = \sigma(w^T x_i)$ and $\delta_i = y_i - \sigma_i$.
