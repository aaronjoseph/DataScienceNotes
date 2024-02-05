#dl
Adam (Adaptive Moment Estimation) is an optimization algorithm that combines ideas from momentum and RMSprop to update network weights iteratively based on training data.

### Mechanism of Adam

- **Combines Momentum and Adaptive Learning Rates**: Adam keeps an exponentially decaying average of past gradients (momentum) and squared gradients (RMSprop).
  
- **First Moment Estimation ($v_i$)**: This is essentially the momentum term. It is an exponentially decaying average of past gradients:

  $$ v_i = \beta_1 v_{i-1} + (1 - \beta_1) \left( \frac{\partial \mathcal{L}}{\partial w_{i-1}} \right) $$

  $\beta_1$ is the decay rate for the first moment (similar to the momentum coefficient).

- **Second Moment Estimation ($G_i$)**: This is analogous to RMSprop and keeps track of the squared gradients:

  $$ G_i = \beta_2 G_{i-1} + (1 - \beta_2) \left( \frac{\partial \mathcal{L}}{\partial w_{i-1}} \right)^2 $$

  $\beta_2$ is the decay rate for the second moment.

- **Parameter Update**: Adam updates parameters using a learning rate $\alpha$, first and second moment estimates, and a small constant $\epsilon$ to prevent division by zero:

  $$ w_i = w_{i-1} - \frac{\alpha v_i}{\sqrt{G_i + \epsilon}} $$

### Initial Instability and Bias Correction

- **Unstable Beginnings**: Initially, $v_i$ and $G_i$ are initialized to zero, leading to biased estimates. The bias towards zero becomes especially significant in the initial time steps.

- **Bias Correction**: To mitigate the bias, Adam applies a bias correction for the first and second moment estimates:

  $$ \hat{v}_i = \frac{v_i}{1 - \beta_1^t} $$
  $$ \hat{G}_i = \frac{G_i}{1 - \beta_2^t} $$

  Here, $t$ is the timestep, and the corrected moments are used in the parameter update rule.

### Advantages of Adam

- **Adaptive Learning Rates**: Each parameter has its own learning rate, allowing for more customized updates.
  
- **Suitable for Non-Stationary Objectives**: Like RMSprop, Adam works well on problems with noisy or sparse gradients.
  
- **Computational Efficiency**: Adam is computationally efficient, has little memory requirements, and is invariant to diagonal rescale of the gradients.

### Typical Hyperparameters

- **Learning Rate ($\alpha$)**: Usually requires little tuning.
  
- **$\beta_1$**: Commonly set to 0.9.
  
- **$\beta_2$**: Commonly set to 0.999.
  
- **$\epsilon$**: A small constant, often set around $10^{-8}$ to prevent any division by zero in the implementation.

Adam is widely regarded as an effective and robust optimizer for training deep neural networks, commonly used in a variety of machine learning tasks.