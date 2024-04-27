MDPs form the base of it - [[Markov Decision Process]].

## Deep Q-Learning

[[Deep Q-Learning]]

## Policy Gradients & Actor-Critic

[[Policy Gradients & Actor-Critic]]

## Fundamentals of Reinforcement Learning (RL)

Reinforcement Learning focuses on the interaction of an agent with its environment with the aim of maximising cumulative rewards, not just the immediate reward. The ultimate goal in RL is to discover the optimal policy, denoted as $\pi^{*}$, that maximises this cumulative reward over time.

### Three Core Elements of RL
1. **Action**: Decisions made by the agent.
2. **Reward**: Immediate feedback from the environment.
3. **Observation**: The agent's perception of the environment's state.

In RL, the Bellman equation is iteratively applied to converge to the optimal values.

### Observability in Environments
- **Fully Observable Environments**: The agent has complete information about the environment's state.
- **Partially Observable Environments**: The agent has limited information and may not fully perceive the current state of the environment.

### RL Mathematical Framework

#### Markov Decision Processes (MDP)
MDPs are used to model the environment in RL, predicting the outcomes of actions taken in states.

- **Markov Property**: Assumes that the future is independent of the past, given the present.
- **Markov Process**: A series of random states satisfying the Markov Property, also known as Markov Chains, characterised by:
  - A set of states
  - Transition probabilities between states
- **Markov Reward Processes**: A Markov process with added rewards at each transition.
- **Markov Decision Processes**: An extension of Markov reward processes with decisions (actions) at every state.

#### Return and Reward
- **Return**: The cumulative, potentially discounted reward received over time.
- **Reward**: A scalar feedback signal indicating the immediate performance of the agent at each time step.

### Discounting in RL
Discounting in RL addresses the importance of immediate versus future rewards and prevents infinite returns in continuous tasks.
- A discount factor of 0 prioritises immediate rewards.
- A discount factor close to 1 gives more weight to future rewards.

### Policy in RL
The policy in RL defines the agent's behaviour, specifying the action to take in each state. To find the optimal policy, we need:

- **State Value Function ($V_{\pi}(s)$)**: The expected return from being in state $s$ and following policy $\pi$.
- **Action Value Function ($q_{\pi}(s,a)$)**: The expected return from taking action $a$ in state $s$, then following policy $\pi$.

## Research-Papers and Links

- [https://arxiv.org/pdf/2007.03313.pdf](https://arxiv.org/pdf/2007.03313.pdf "https://arxiv.org/pdf/2007.03313.pdf")
- https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf
