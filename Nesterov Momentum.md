#dl 
Nesterov Momentum is an enhancement of the traditional momentum method that aims to accelerate the convergence of the gradient descent optimization algorithm. It does this by making a key modification: it calculates the gradient at a position ahead in the direction of the current momentum.

### Key Idea of Nesterov Momentum

- **Look-Ahead Gradient**: Instead of calculating the gradient at the current position, Nesterov Momentum takes a step in the direction of the current velocity and computes the gradient at this new, lookahead position.

- **Velocity Update**: The velocity is updated as follows:

  $$ \hat{w}_{i-1} = w_{i-1} + \beta v_{i-1} $$

  $$ v_i = \beta v_{i-1} + \alpha \frac{\partial \mathcal{L}}{\partial \hat{w}_{i-1}} $$

  where $\hat{w}_{i-1}$ is the lookahead weight.

- **Weight Update**: The weights are updated by subtracting the velocity from the previous weights:

  $$ w_i = w_{i-1} - \alpha v_i $$

### Reasoning Behind Nesterov Momentum

- **Intuition**: The method is based on the intuition that velocity can provide a good indication of the direction we should be heading. By calculating the gradient after moving in the direction of the velocity, we get a more accurate gradient that accounts for the momentum of the optimization process.

- **Correction Factor**: The lookahead step acts as a correction factor, allowing the optimizer to adjust its trajectory if it is heading towards a suboptimal direction.

- **Avoiding Overshooting**: By anticipating where the parameters are going to be, Nesterov Momentum allows for larger learning rates without the risk of overshooting minima as much as traditional momentum.

### Benefits Over Standard Momentum

- **Faster Convergence**: Nesterov Momentum often converges faster to the optimum than standard momentum because it can prevent the optimization from going too fast in a suboptimal direction.

- **Smarter Updates**: By taking the gradient at the lookahead position, the updates are more informed and can lead to more efficient learning trajectories.

### Implementation Consideration

- **Correct Gradient**: It is important to ensure that the gradient is calculated after the lookahead step is made, otherwise, the benefits of Nesterov Momentum will not be realized.

- **Hyperparameter Tuning**: Similar to traditional momentum, the hyperparameter $\beta$ needs to be set carefully. A common value for $\beta$ is around 0.9.

In practice, Nesterov Momentum is widely used in training deep neural networks because of its ability to accelerate convergence and reduce the risk of overshooting during optimization. It is especially effective when navigating complex loss surfaces with many local minima and flat regions.