### Basic Idea

Backpropogation algorithm works by going from the output layer to the input layer, propogating the error gradients along the way. Once the algorithm has computed the gradients of the cost function with regard to each parameter in the network, it uses these gradients to update each parameter witha gradient descent step.

Here, either the gradient gets smaller and smaller or larger and larger as the algorithm progresses down to the lower layers.

If it keeps getting small, it is vanishing gradient and the weights in the lower layers are not changed much while in the exploding gradient, the opposite happens and changes the values drastically

---
### Vanishing Gradients

Here, the gradients gets very close to 0 but not zero

---
### Exploding Gradients

In exploding gradients, the values goes beyond a point, and the computer responds with NaN (Not a Number)

To solve this issue, gradient clipping can be employed to solve this issue.