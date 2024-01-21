Gradient descent is a generic optimization algorithm capable of finding optimal solutions to a wide range of problems. The general underlying principle here is that gradient descent tweaks parameters iteratively to minimize a cost function.

Gradient descent is generally used to find the lowest point of a cost function. Once the gradient is zero, the local or global optimum is reached.

`Learning Rate` determines the size of the steps the learning algorithm takes.

For any learning algorithm, there are two main approaches:

1. **Direct Solution**
   - In this approach, the partial derivative of the cost function is taken and set to zero to find the critical points, which may reveal the optimal solution.
2. **Gradient Descent**
   - In this iterative approach, the algorithm may never reach the global optimum but instead approaches it incrementally.

### High Dependency of Gradient Descent

- Gradient descent can be applied to any model, whereas a direct solution is only applicable to a handful of models.
- Solving a large system of linear equations using direct solutions can be computationally expensive.

---

# Approaches to Gradient Descent

> Gradient descent is used to update the parameters of a model. In linear regression, parameters refer to coefficients, and in neural networks, they refer to weights.

### Batch Gradient Descent

- Computes the gradient of the cost function with respect to the parameters $\theta$ for the entire training dataset.
- Performs one update at a time, which can be slow and problematic if the dataset cannot fit in memory.
- Not suitable for online model updates.
- Appropriate for smaller datasets.

For a cost function $J(\theta)$, the gradient is computed as:

$$
\theta := \theta - \alpha \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x^{(i)}
$$

### Stochastic Gradient Descent (SGD)

- Optimizes one training example $x^{(i)}$ and label $y^{(i)}$ at a time, which is much faster than batch gradient descent.
- Suitable for online learning.

SGD updates the parameters for each training example as:

$$
\theta := \theta - \alpha \left( h_\theta(x^{(i)}) - y^{(i)} \right) x^{(i)}
$$

### Mini-Batch Gradient Descent

- Strikes a balance between batch gradient descent and SGD, updating parameters for every mini-batch of $n$ training examples.
- Batch sizes are typically powers of 2 (e.g., 2, 8, 16, 256) for performance reasons.

For mini-batch of $n$ examples, the gradient is computed as:

$$
\theta := \theta - \alpha \frac{1}{n} \sum_{i=1}^{n} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x^{(i)}
$$

----

In these notes, $\alpha$ is the learning rate, a crucial hyperparameter that controls the step size in the parameter space towards the minimum of the cost function.