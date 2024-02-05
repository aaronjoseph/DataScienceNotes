#dl 
## Augmented Notes on the Sigmoid Function

The sigmoid function, denoted by $\sigma(x)$, is a widely used activation function in neural networks, particularly for binary classification problems. It maps any input value to a value between 0 and 1, making it useful for interpreting the output as a probability.

### Properties of the Sigmoid Function

- **Output Range**: The sigmoid function constrains the output to be between 0 and 1 (i.e., $\sigma(x) \in [0,1]$).
  
- **Shape**: It has an "S" shaped curve or sigmoid curve.
  
- **Output Behavior**: The output of the sigmoid function is always positive.

- **Saturation**: The function saturates at both ends, meaning as $x \to \infty$, $\sigma(x) \to 1$, and as $x \to -\infty$, $\sigma(x) \to 0$.

- **Gradients**: 
  - The gradients are always positive, which means the function is monotonically increasing.
  - The gradient vanishes at both ends; it is significant only for inputs near 0.

### Formula of the Sigmoid Function

The sigmoid function formula is:

$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$

### Vanishing Gradient Issue

One of the main issues with the sigmoid function is the vanishing gradient problem. Due to the nature of the function, for very high or very low input values, the gradient is extremely small. This causes the updates to the weights during backpropagation to be very tiny, effectively slowing down or even halting the learning process. When gradients vanish, the neural network cannot learn effectively, which can lead to training plateaus.

### Vanishing Gradient in Mathematical Terms

Mathematically, the vanishing gradient issue arises because the derivative of the sigmoid function, which is used in the backpropagation algorithm, can be expressed as:

$$ \sigma'(x) = \sigma(x) (1 - \sigma(x)) $$

Given that $\sigma(x)$ is bound between 0 and 1, the product $\sigma(x) (1 - \sigma(x))$ is at its maximum when $x = 0$ and rapidly approaches zero as $x$ moves away from zero. Thus, for neurons that activate strongly (with inputs far from zero), the gradient will be close to zero, leading to minimal weight updates.

### Implications for Deep Learning Architectures

The implications of the vanishing gradient problem are particularly pronounced in deep learning networks with many layers. The gradients of the loss function diminish as they are propagated back through each layer, resulting in the early layers learning very slowly, if at all.

> Additionally, since it carries the term e, the exponential function, it's not great for computation

### Incorporating Sigmoid Function into Neural Networks

When using the sigmoid function in a neural network, the output of a neuron at layer $t$ can be represented as $h^t = \sigma(h^{t-1})$, where $h^{t-1}$ is the output of the previous layer.

The gradients of the loss function with respect to the weights can be computed using the chain rule:

$$ \frac{\partial \mathcal{L}}{\partial W} = \frac{\partial \mathcal{L}}{\partial h^t} \frac{\partial h^t}{\partial W} $$

Here, $\frac{\partial \mathcal{L}}{\partial h^t}$ depends on the derivative of the sigmoid function, which can lead to vanishing gradients.

