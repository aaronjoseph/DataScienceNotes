#dl 
Neural networks, employed to solve large-scale data problems, depend heavily on optimization algorithms for efficient and faster convergence. These algorithms are crucial in navigating the high-dimensional landscape of neural network parameters to find a set of weights that minimizes the loss function effectively.

### Optimization Challenges
- **Search Problem**: Finding the best set of weights is a search problem in the landscape defined by the loss function.
- **Various Methods**: Several classes of methods can be employed, including random search, genetic algorithms, and gradient-based optimization.

### Gradient-Based Optimization
In deep learning, gradient-based methods are dominant because they leverage the information from the gradient of the loss function to make informed updates to the parameters.

### Loss Surface and Weights Adjustment
- As weights change, so does the loss. Small changes in weights result in small changes in the loss, assuming local smoothness.
- Iterative algorithms make slight adjustments to the weights based on this relationship.

### Steepest Descent Direction
- The steepest descent direction is found by computing the negative gradient of the loss function.
- Intuitively, the gradient measures how the loss function changes with a small change in weights.

### Algorithmic Implementation of Gradient Descent
- **Model Selection**: Choose a model, for example, $f(x, W) = Wx$.
- **Loss Function**: Choose a loss function, like $L_i = |y - Wx_i|^2$.
- **Partial Derivatives**: Calculate the partial derivative of the loss with respect to each parameter $\frac{\partial L}{\partial w_j}$.
- **Parameter Update**: Adjust each parameter $w_j$ in the direction that reduces the loss: $w_j = w_j - \alpha \frac{\partial L}{\partial w_j}$, where $\alpha$ is the learning rate.

> Saddle Points : are those where the gradient of orthogonal directions are zero
### Advanced Optimization Techniques
These methods build on gradient descent and introduce modifications to improve convergence:


#### Nadam (Nesterov-accelerated Adaptive Moment Estimation)
Combines Adam with Nesterov momentum, which anticipates future gradient directions for more accurate updates.

#### Adadelta
An extension of AdaGrad that seeks to reduce its aggressively decreasing learning rate over time.


 ![[Momentum]]
 ![[Nesterov Momentum]]
 ![[Adagrad and RMSProp]]
 ![[Adam Optimizer]]