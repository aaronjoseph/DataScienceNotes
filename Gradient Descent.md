Is a generic optimization algorithm capable of finding optimal solutions to a wide range of problems. The general or undelying principle here is that Gradient descent tweaks parameters iteratively in order to minimize a cost function.

Once the gradient is zero, the local or global optima is reached.

`Learning Rate` - Determines the size of the jump of the learning algorithm

For any learning algorithm, there are two ways to approach it,
1. Direct Solution
	1. Here the partial derivative is taken and then it is equate to 0 to find the critical solution
2. Gradient Descent
	1. Here, the global optima is never reached, but approached

High dependency of Gradient Descent
1. This can be applied to any model while the direct solution can be used for handful of models
2. Solving large system of linear equations can be expensive

---
# Approach

### Batch Gradient Descent

This is the basic gradient descent, computes the gradient of the cost function wrt the parameters $\theta$ for the entire training dataset
- This calculates the gradient for the entire dataset to perform one update
- Hence, can be slow and will be an issue if the data-set cannot fir in memory
- Also, doesn't work for updating the model online


### Stocastic Gradient Descent

Unlike Batch Gradient Descent, SGD does optimisation on one training example $x^i$ and label $y^i$ one at a time
- This is therefore much faster than Batch Gradient Descent
- Can be used for online learning

### Mini-Batch Gradient Descent
- Advantage over Stocastic gradient descent when it comes to performance boost
