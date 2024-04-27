## Policy Gradients and Gathering Data/Experience

### Objective Function
- The objective function $J(\theta)$ is the expected return calculated over the distribution of trajectories $\tau$ induced by the policy $\pi_\theta$.

### Data Collection
- To gather data for policy gradients, one samples $N$ trajectories $\{\tau_i\}_{i=1}^N$ by acting according to $\pi_\theta$.
- The performance measure $J(\theta)$ is estimated by averaging the returns of these sampled trajectories.

### Policy Gradient Computation
- Trajectories are sampled by executing a policy parameterized by $\theta$.
- The policy gradient $\nabla_\theta J(\theta)$ is computed to guide the updates to the policy parameters.

### REINFORCE Algorithm
- The REINFORCE algorithm involves running the policy to sample trajectories, computing the policy gradient, and updating the policy based on this gradient.

### Deriving the Policy Gradient
- The policy gradient is derived by taking the gradient of the expected return with respect to the policy parameters $\theta$.
- It can be expressed as an expectation over the policy's trajectory distribution.

### Variance Reduction
- Credit assignment in policy gradients can lead to high variance in training.
- Variance can be reduced by subtracting a baseline from the reward, which helps in stabilizing training.

### Challenges
- Identifying which specific actions contribute to increases in rewards is complex.
- Determining the optimal baseline $b$ for variance reduction is non-trivial and is an exercise left for further exploration.
