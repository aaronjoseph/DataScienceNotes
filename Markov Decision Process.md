---
tags:
  - "ds-foundations"
---

A Markov decision process (MDP) is a mathematical framework for sequential decision-making in which outcomes are partly random and partly under the control of a decision maker. MDPs are the standard setting for dynamic programming and [[Reinforcement Learning|reinforcement learning]] (RL).

## Definition

An MDP is a tuple $(S, A, T, R, \gamma)$:

- $S$: the set of possible states.
- $A$: the set of possible actions.
- $T(s, a, s')$: the transition probability of moving to state $s'$ after taking action $a$ in state $s$, also written $p(s' \mid s, a)$.
- $R$: the reward. Some texts use a reward distribution for each transition $(s, a, s')$; this note writes the expected immediate reward as $r(s, a)$.
- $\gamma$: the discount factor, which sets how much future rewards count relative to immediate ones.

**Markov property.** The next state and reward depend only on the current state and action, not on the earlier history. This is what lets value functions be written recursively.

## MDPs in Reinforcement Learning

In RL the MDP framework is used but some components are typically **unknown**:

- **Transition probabilities $T$**: how likely each next state is after an action.
- **Rewards $R$**: what reward follows each transition.

**Evaluative feedback.** The agent is not told which action was correct. It sees only the consequences of the actions it tried, and must learn by trial and error. This is the key difference from supervised learning. A [[Multi-Armed Bandits|multi-armed bandit]] is the simplest case: a single state, where each action's reward must be learned.

## Policies and Returns

- **Deterministic policy.** $\pi(s) = a$ picks one action in each state.
- **Stochastic policy.** It gives a probability for each action:

  $$
  \pi(a \mid s) = \mathbb{P}(A_t = a \mid S_t = s)
  $$

A good policy maximises not the immediate reward but the **return**, the discounted sum of future rewards. Future rewards are worth less, much like the time value of money.

**Discount factor.** $\gamma \in [0, 1]$. Values near 0 make the agent short-sighted and values near 1 make it far-sighted. For continuing tasks with no terminal state, $\gamma < 1$ keeps the infinite sum finite; $\gamma = 1$ is used only when episodes are guaranteed to end.

**Optimal policy.** The goal is a policy that maximises the expected return from every state:

$$
\pi^* = \underset{\pi}{\arg\max} \; \mathbb{E}\left[\sum_{t \geq 0} \gamma^t r_t \,\middle|\, \pi\right]
$$

- $\arg\max_\pi$ selects the policy that achieves the largest value.
- $\mathbb{E}[\cdot \mid \pi]$ averages over the randomness in transitions and in a stochastic policy, when actions follow $\pi$.
- $\gamma^t r_t$ is the reward at step $t$, discounted more heavily the later it arrives.

The formula captures the trade-off between immediate and future rewards, valuing the latter less.

## Value Functions

**State value.** $V^\pi(s)$ is the expected return when starting from state $s$ and following $\pi$. It measures how good it is to be in $s$:

$$
V^\pi(s) = \mathbb{E}\left[\sum_{t \geq 0} \gamma^t r_t \,\middle|\, s_0 = s, \pi\right]
$$

**State–action value.** $Q^\pi(s, a)$ is the expected return when taking action $a$ in state $s$ and following $\pi$ afterwards. It measures the long-term effect of a particular action:

$$
Q^\pi(s, a) = \mathbb{E}\left[\sum_{t \geq 0} \gamma^t r_t \,\middle|\, s_0 = s, a_0 = a, \pi\right]
$$

The optimal functions $V^*$ and $Q^*$ are the same quantities under an optimal policy $\pi^*$. They are related by:

$$
V^*(s) = \max_a Q^*(s, a), \qquad \pi^*(s) = \underset{a}{\arg\max} \; Q^*(s, a)
$$

## Bellman Optimality Equations

The definitions above become recursive once the return is split into the first reward plus the discounted value of the next state. For the optimal state value:

$$
V^*(s) = \max_a \sum_{s'} p(s' \mid s, a) \big[r(s, a) + \gamma V^*(s')\big]
$$

For the optimal action value:

$$
Q^*(s, a) = \sum_{s'} p(s' \mid s, a) \Big[r(s, a) + \gamma \max_{a'} Q^*(s', a')\Big]
$$

Solving an MDP means solving these fixed-point equations. When $T$ and $R$ are known, dynamic programming can do it directly.

## Algorithms for Solving MDPs

### Value Iteration

1. **Initialise** $V^0(s)$ for every state, for example to 0.
2. **Iterate.** For every state, apply the Bellman optimality equation as an update:

$$
V^{i+1}(s) \leftarrow \max_a \sum_{s'} p(s' \mid s, a) \big[r(s, a) + \gamma V^{i}(s')\big]
$$

3. **Stop** when the values change by less than a tolerance: $V^0 \to V^1 \to \cdots \to V^*$.
4. **Extract the policy** by choosing the action that achieves the maximum in each state.

Each iteration costs $O(|S|^2 |A|)$: for every state and action, the update sums over all next states.

### Q-Iteration

Q-iteration applies the same idea to state–action values:

$$
Q^{i+1}(s, a) \leftarrow \sum_{s'} p(s' \mid s, a) \Big[r(s, a) + \gamma \max_{a'} Q^{i}(s', a')\Big]
$$

It loops over actions as well as states. Implemented directly, with the inner maximum recomputed inside the sum, each iteration costs $O(|S|^2 |A|^2)$. Precomputing $\max_{a'} Q^{i}(s', a')$ once per next state brings it back to $O(|S|^2 |A|)$, the same as value iteration. Storing $Q$ makes policy extraction trivial, and it is the quantity that [[Deep Q-Learning]] approximates with a neural network when $T$ is unknown.

**Policy iteration** is a common alternative. It alternates between evaluating the current policy and making it greedy with respect to the resulting values.

## Worked Example

**Inputs.** Two states, $A$ and $B$, with deterministic transitions and $\gamma = 0.9$. Start from $V^0(A) = V^0(B) = 0$.

- In $A$: **stay** gives reward 1 and stays in $A$; **go** gives reward 0 and moves to $B$.
- In $B$: **stay** gives reward 2 and stays in $B$; **go** gives reward 0 and moves to $A$.

**Iteration 1.**

$$
V^1(A) = \max(1 + 0.9 \cdot 0, \; 0 + 0.9 \cdot 0) = 1, \qquad V^1(B) = \max(2, 0) = 2
$$

**Iteration 2.**

$$
V^2(A) = \max(1 + 0.9 \cdot 1, \; 0 + 0.9 \cdot 2) = \max(1.9, 1.8) = 1.9
$$

$$
V^2(B) = \max(2 + 0.9 \cdot 2, \; 0 + 0.9 \cdot 1) = 3.8
$$

**Iteration 3.**

$$
V^3(A) = \max(1 + 0.9 \cdot 1.9, \; 0 + 0.9 \cdot 3.8) = \max(2.71, 3.42) = 3.42
$$

$$
V^3(B) = \max(2 + 0.9 \cdot 3.8, \; 0.9 \cdot 1.9) = 5.42
$$

**Convergence.** The values converge to:

$$
V^*(B) = \frac{2}{1 - 0.9} = 20, \qquad V^*(A) = 0 + 0.9 \times 20 = 18
$$

In the first two iterations, "stay" looks better in $A$ because it pays immediately. From iteration 3 onwards the look-ahead shows that giving up one reward to reach $B$ is worth more: staying in $A$ forever is worth only:

$$
\frac{1}{1 - 0.9} = 10
$$

The optimal policy is to go from $A$ to $B$ and stay there. The values were recalculated in Python.

## Related Notes

- [[Reinforcement Learning]] — Learning when $T$ and $R$ are unknown.
- [[Deep Q-Learning]] — Approximating $Q^*$ with a neural network.
- [[Policy Gradients & Actor-Critic]] — Optimising the policy directly.
- [[Multi-Armed Bandits]] — The single-state special case.

## References & Useful Links

- [Reinforcement Learning: An Introduction, 2nd ed. (Sutton and Barto, 2018)](http://incompleteideas.net/book/the-book-2nd.html) — Standard textbook treatment of finite MDPs, Bellman equations, dynamic programming, and evaluative feedback, with a free full PDF. Only the book page was opened in this revision; the chapter text was not re-read.