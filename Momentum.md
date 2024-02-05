#dl 
## Notes on Momentum in Optimization

Momentum is an optimization technique used to accelerate gradient descent, making it faster and more reliable, especially for functions with many shallow regions or for dealing with the vanishing gradient problem. Here's a detailed look at the concept of Momentum:

### Momentum Overview

- **Intuitive Idea**: Imagine a ball rolling down a loss surface. Momentum allows the ball to use its inertia to continue moving in the same direction, helping it to pass over flat surfaces and small humps, potentially avoiding getting stuck in local minima.

### Momentum Mechanics

- **Velocity Update**: The 'velocity' term $v_i$ is a combination of the past velocity and the current gradient. It is given by the equation:

$$ v_i = \beta v_{i-1} + \frac{\partial \mathcal{L}}{\partial w_{i-1}} $$

Here, $\beta$ is a hyperparameter known as the momentum term, typically set close to 1 (e.g., 0.9 or 0.99). This term dictates the contribution of the past velocity to the current update.

- **Weight Update**: Weights are updated by subtracting the product of learning rate $\alpha$ and the velocity from the previous weights:

$$ w_i = w_{i-1} - \alpha v_i $$

### Exponential Moving Average

- The velocity term $v_i$ can also be thought of as an exponential moving average of the gradients, which helps in smoothing out the updates and provides a notion of 'direction' to the optimization process.

- **Expanded Form**: By expanding the recursive definition of velocity, we can see the influence of previous gradients:
  
$$ v_i = \beta(\beta v_{i-2} + \frac{\partial \mathcal{L}}{\partial w_{i-2}}) + \frac{\partial \mathcal{L}}{\partial w_{i-1}} = \beta^2 v_{i-2} + \beta \frac{\partial \mathcal{L}}{\partial w_{i-2}} + \frac{\partial \mathcal{L}}{\partial w_{i-1}} $$

### Exponentially Weighted Averages
It calculates a moving average of the gradients to smooth out the updates, with higher $\beta$ values giving more weight to past observations.
### Generalization to Stochastic Gradient Descent (SGD)

- Momentum can be considered a generalization of SGD, with SGD being a special case where $\beta = 0$. This implies no momentum term and each update depends only on the current gradient.

### Equivalent Formulation

- An equivalent formulation of the momentum update rule involves incorporating the learning rate directly into the velocity calculation:

$$ v_i = \beta v_{i-1} - \alpha \frac{\partial \mathcal{L}}{\partial w_{i-1}} $$
  
- The weight update is then simply adding the new velocity to the previous weights:

$$ w_i = w_{i-1} + v_i $$

### Benefits of Momentum

- **Faster Convergence**: Momentum can lead to faster convergence by propelling the weights across flat regions of the loss landscape.
  
- **Dampening Oscillations**: It can help to dampen oscillations in directions of high curvature, leading to smoother convergence.
  
- **Avoiding Poor Local Minima**: By accumulating velocity, the optimizer can potentially escape shallow local minima.

### Accelerated Descent Methods

- Momentum is part of a broader class of accelerated gradient methods, which aim to speed up gradient descent by considering past gradients in the update rule.
  
- **Theoretical Analysis**: These methods often come with some theoretical guarantees under certain assumptions about the loss function's shape and gradient behavior.
