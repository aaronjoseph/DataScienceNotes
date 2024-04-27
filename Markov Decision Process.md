#dl 
`Markov Decision Processes or MDPs`

MDPs provide a mathematical framework for modeling decision-making where outcomes are partly random and partly under the control of a decision maker. MDPs are useful in studying optimization problems solved via dynamic programming and reinforcement learning.

An MDP is formally defined as a tuple $(S, A, R, T, \gamma)$ where:

- $S$: Set of possible states
- $A$: Set of possible actions
- $R(s, a, s')$: Distribution of reward, received after transitioning from state $s$ to state $s'$, due to action $a$
- $T(s, a, s')$: Transition probability distribution, the probability of transitioning to state $s'$ from state $s$ after taking action $a$, also noted as $p(s'|s,a)$
- $\gamma$: Discount factor, which represents the difference in importance between future rewards and present rewards

MDPs are a key element in Reinforcement Learning (RL), providing the structure needed for agents to learn how to act optimally in stochastic environments over time.


---
In Reinforcement Learning (RL), the framework of Markov Decision Processes (MDPs) is utilised with some components typically `unknown`, specifically:

- Transition probability distribution $T$: Defines the likelihood of moving from one state to another given a particular action.
- Reward distribution $R$: Specifies the reward received after a transition from one state to another due to an action.

### Evaluative Feedback in RL

Within RL, evaluative feedback is essential. This feedback is not provided upfront but is instead discovered through the process of trial and error. Agents learn from the consequences of their actions, which in turn informs their decision-making process.

--- 
### Solving MDPs: Optimal Policy

- **Defining a Policy**:
  - A policy is a strategy used by an agent to decide which action to take in each state.
  - **Deterministic Policy**: Represented as $\pi(s) = a$, it specifies a single action $a$ to be taken when in state $s$.
  - **Stochastic Policy**: Represented as $\pi(a|s) = \mathbb{P}(A_t = a|S_t = s)$, it defines the probability of taking action $a$ when in state $s$.

- **Characteristics of a Good Policy**:
  - The objective is not just to maximize the immediate reward but also to consider the entire sequence of future rewards.
  - A good policy aims for the **discounted sum of future rewards**, where rewards received in the future are worth less than immediate rewards, reflecting the concept of the time value of money or utility.
  
- **Discount Factor ($\gamma$)**:
  - The discount factor $\gamma$ ranges between 0 and 1 ($\gamma \in [0,1]$) and determines the present value of future rewards.
  - A value of $\gamma$ close to 0 makes the agent short-sighted (cares mostly about immediate rewards), while a value close to 1 makes it far-sighted (cares about long-term rewards).

- **Optimization Goal**:
  - The goal in solving MDPs is to find an optimal policy $\pi^*$ that maximises the expected return (discounted sum of future rewards) from any given state.

- **Optimal Policy**
- The optimal policy $\pi^*$ in a Markov Decision Process is defined mathematically as:

$$
\pi^* = \underset{\pi}{\mathrm{arg\,max}}\ \mathbb{E}\left[\sum_{t \geq 0} \gamma^t r_t \bigg| \pi\right]
$$

Here's what this formula represents:

- $\pi^*$: This symbol represents the optimal policy, which is the policy that maximises the expected sum of discounted rewards.

- $\mathrm{arg\,max}$: This operator finds the argument (in this case, the policy $\pi$) that maximises the following expected value.

- $\mathbb{E}$: The expected value operator, indicating that we are interested in the expected sum of rewards, which accounts for the probabilistic nature of the rewards received under policy $\pi$.

- $\sum_{t \geq 0} \gamma^t r_t$: This is the sum of discounted rewards over time. For each time step $t$, the reward $r_t$ received is discounted by $\gamma^t$. 

- $\gamma$: The discount factor, which ranges from 0 to 1 ($\gamma \in [0, 1]$), determines the present value of future rewards. It makes future rewards worth less in the present term than immediate rewards.

- $\gamma^t$: This raises the discount factor $\gamma$ to the power of $t$, increasing the discount with each time step.

- $r_t$: The reward received at time step $t$.

- $\big| \pi$: This notation means that the expected sum of discounted rewards is being evaluated under the policy $\pi$.

In essence, this equation states that the optimal policy is the one that, for any given state, chooses the action that maximizes the expected total of the rewards that are discounted over time, starting from the current time step. It captures the trade-off between immediate and future rewards, valuing the latter less than the former, and informs the strategy that the agent should adopt to maximize its returns in the long run.

### Value Functions

- **Value Function**: Predicts the total amount of reward an agent can expect to accumulate over the future, starting from a specific state or state-action pair, discounted by a factor of $\gamma$.

- **State Value Function ($V^\pi(s)$)**: 
  - Estimates the expected return from a state $s$, under policy $\pi$.
  - Defined as the expected discounted sum of future rewards starting from state $s$:
    $$ V^\pi(s) = \mathbb{E} \left[\sum_{t \geq 0} \gamma^t r_t \bigg| s_0 = s, \pi \right] $$
  - It assesses the "goodness" of a state, predicting the likely outcome (win/loss) from that state onward.

- **State-Action Value Function ($Q^\pi(s, a)$)**:
  - Evaluates the expected return from taking action $a$ in state $s$, under policy $\pi$.
  - Defined as the expected discounted sum of future rewards starting from state $s$, taking action $a$, and thereafter following policy $\pi$:
    $$ Q^\pi(s, a) = \mathbb{E} \left[\sum_{t \geq 0} \gamma^t r_t \bigg| s_0 = s, a_0 = a, \pi \right] $$
  - It measures the "goodness" of performing a particular action in a given state, forecasting the long-term impact of that action.

Both functions are central to many reinforcement learning algorithms, enabling an agent to make informed decisions that consider both the immediate and potential future rewards.

---
## Algorithms for Solving MDPs

### Bellman Optimality Equations
The Bellman optimality equations for value functions and Q-functions establish the recursive nature of solving MDPs.

- **Value Function ($V^*(s)$)**:
  The optimal value function represents the expected return from a given state, assuming the optimal policy $\pi^*$ is followed.

  $$V^*(s) = \mathbb{E}\left[ \sum_{t \geq 0} \gamma^t r_t | s_0 = s, \pi^* \right]$$

- **Q-Function ($Q^*(s, a)$)**:
  The optimal Q-function represents the expected return from a given state and action, assuming the optimal policy is followed thereafter.

  $$Q^*(s, a) = \mathbb{E}\left[ \sum_{t \geq 0} \gamma^t r_t | s_0 = s, a_0 = a, \pi^* \right]$$

### Equations Relating Optimal Quantities
These equations illustrate the relationship between the optimal value function, optimal Q-function, and optimal policy.

- **Optimal Policy ($\pi^*(s)$)**:
  The optimal policy is derived from the optimal Q-function, yielding the action with the highest expected return.

  $$\pi^*(s) = \operatorname{arg\,max}_a Q^*(s, a)$$

- **Optimal Value Function as Maximum of Q-Function**:
  This equation shows that the optimal value function for a state is the maximum over the expected returns for all possible actions.

  $$V^*(s) = \max_a Q^*(s, a)$$

### Value Iteration Algorithm
- **Initialization**:
  - Begin by initialising the values of all states.

- **Iteration**:
  - Continue iterating while the values have not yet converged.
  - For each state $s$ in the state space, update the value function $V^{i+1}(s)$ using the Bellman optimality equation:

    $$V^{i+1}(s) \leftarrow \max_a \sum_{s'} p(s' | s, a) \left[ r(s, a) + \gamma V^i(s') \right]$$

- **Convergence**:
  - The process is repeated until there is no significant change in the values across states, signifying convergence.
  - Iteratively, this is shown as: $V^0 \rightarrow V^1 \rightarrow V^2 \rightarrow \cdots \rightarrow V^i \rightarrow \cdots \rightarrow V^*$.

- **Time Complexity**:
  - The time complexity per iteration of the algorithm is $O(|S|^2 |A|)$, where $|S|$ is the number of states and $|A|$ is the number of actions.

This iterative process is used to approximate the optimal value function $V^*$, which in turn can be used to derive an optimal policy.

### Value Iteration Update
- The Value Iteration algorithm updates the value function for each state based on the expected return from future states, optimised over all possible actions.
- This update follows the Bellman optimality equation:

  $$V^{i+1}(s) \leftarrow \max_a \sum_{s'} p(s' | s, a) \left[ r(s, a) + \gamma V^{i}(s') \right]$$

### Q-Iteration Update
- The Q-Iteration algorithm is similar to Value Iteration, with the main difference being that it loops over actions as well as states.
- The Q-Iteration update computes the Q-value for each state-action pair:

  $$Q^{i+1}(s, a) \leftarrow \sum_{s'} p(s' | s, a) \left[ r(s, a) + \gamma \max_{a'} Q^{i}(s', a') \right]$$

- Both Value Iteration and Q-Iteration aim to converge to an optimal policy. However, Q-Iteration involves a more complex computation due to the inclusion of action values in the loop.

These updates are foundational for determining optimal policies in MDPs, each providing a way to converge on an optimal solution through iterative calculations.