Monte Carlo simulation where the idea is to run a simulator over and over again with randomized inputs and observe the aggregate results. It is a probability simulation technique used to understand the impact of risk and uncertainity in financial sectors, project management and other forecasting machine learning models.

For any future consideration, there is constant uncertainity, ambiguity and variability and therfore despite unprecedented access to information, future predictions are hard to make.

### Law of Large Numbers

This states that the more times a function is randomly sampled, the more accurate its approximation is. 

> Monte Carlo methods rely on repeated random sampling from a distribution to obtain a numerical result. It is an approach rather than an algorithm. 

---
Monte Carlo sampling can be done as follows
- `Direct Sampling` - Sampling from a distribution naively and directly with no prior information. This can be used to approach approximating the unknown area of a shape
- `Importance Sampling` - When the distribution is expensive to sample, sample from a simpler approximation function. 
- `Rejection Sampling` - In the case when the distribution is unknown, propose new points and accept them if they fulfill some criterion

Monte Carlo Sampling is usually used in two context
- `Optimization` Naturally, finding the optima requires a healthy balance between exploration and exploitation. When Monte Carlo sampling is fitted with another mechanism to control explotation, it can be a powerful tool to find optima
- `Approximating probabilities & Functions` Monte Carlo sampling is a great way to evaluate certain probabilities or function indirectly when it is too difficult to do so with another method