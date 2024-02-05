#dl
Adagrad is an adaptive learning rate method designed to allocate different learning rates for each parameter. It is particularly effective for dealing with sparse data.

### Key Features of Adagrad

- **Adaptive Learning Rates**: Adagrad modifies the general learning rate at each time step for every parameter, based on past gradients.
  
- **Accumulation of Gradients**: It accumulates the squared gradients in the denominator: 

  $$ G_i = G_{i-1} + \left( \frac{\partial \mathcal{L}}{\partial w_{i-1}} \right)^2 $$
  
  Here, $G_i$ represents the sum of the squares of the past gradients with respect to the weights.

- **Weight Update Rule**: The weights are updated as follows:

  $$ w_i = w_{i-1} - \frac{\alpha}{\sqrt{G_i + \epsilon}} \frac{\partial \mathcal{L}}{\partial w_{i-1}} $$

  where $\alpha$ is the initial learning rate, and $\epsilon$ is a small smoothing term to prevent division by zero.

- **Benefit**: This approach helps in the case of sparse data where some features may not be present in every instance. Adagrad compensates for this by making fewer updates for frequently occurring features.

### Limitation of Adagrad

- **Learning Rate Diminishes**: As gradients are accumulated over time, the learning rate can shrink and eventually become infinitesimally small, which causes the algorithm to stop learning. This is where RMSprop becomes relevant.

## Notes on RMSprop

RMSprop (Root Mean Square Propagation) is an optimization algorithm that aims to resolve the diminishing learning rate problem of Adagrad.

### Key Features of RMSprop

- **Moving Average of Squared Gradients**: Instead of accumulating all past squared gradients, RMSprop maintains a moving average, which is given by:

  $$ G_i = \beta G_{i-1} + (1 - \beta) \left( \frac{\partial \mathcal{L}}{\partial w_{i-1}} \right)^2 $$

  where $\beta$ is a decay rate that determines the extent of the memory for past gradients.

- **Weight Update Rule**: Similar to Adagrad, but uses the moving average:

  $$ w_i = w_{i-1} - \frac{\alpha}{\sqrt{G_i + \epsilon}} \frac{\partial \mathcal{L}}{\partial w_{i-1}} $$

### Reasoning for RMSprop Over Adagrad

- **Preventing Aggressive Diminishing**: The moving average mechanism of RMSprop prevents the aggressive diminishing of learning rates found in Adagrad. By adjusting the accumulation of past gradients, RMSprop ensures that the learning rate does not decrease too rapidly.

- **Balancing Step Size**: RMSprop modifies the learning rate for each weight based on the recent magnitudes of the gradients for that weight, which means it adjusts the step size depending on the recent history, allowing the optimization to continue making reasonable updates through time.

- **Suitability for Non-Stationary Problems**: RMSprop is especially suitable for non-stationary problems (problems where the distribution changes over time), like in many online learning settings.

The introduction of RMSprop is considered a significant advancement in optimization algorithms for deep learning, as it allows the model to continue learning even when dealing with complex and highly non-convex optimization landscapes.