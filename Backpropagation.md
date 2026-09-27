---
tags:
  - "ds-foundations"
---

Backpropagation computes the gradient of a scalar loss with respect to every weight in a neural network by applying the chain rule backwards, from the loss to the inputs. It is reverse-mode automatic differentiation applied to the training loss.[^baydin] Together with an optimiser such as [[Gradient Descent]], it is how neural networks are trained.

## The Idea in One Paragraph

The forward pass computes the network's output and stores the intermediate values. The backward pass starts from $\partial L / \partial L = 1$ and visits the operations in reverse order. Each operation, or "gate", multiplies the gradient arriving at its output by its own **local gradient** and passes the result to its inputs. Every gate works locally, knowing nothing about the rest of the network, yet the chain rule makes the products add up to the exact gradient of the loss.[^cs231n-bp] [[Computational Graph]] explains why the backward direction is efficient: one pass yields the gradient with respect to all parameters.

## Local Rules

**Chain rule.** If $q = g(x)$ and $L$ depends on $q$:

$$
\frac{\partial L}{\partial x} = \frac{\partial L}{\partial q} \, \frac{\partial q}{\partial x}
$$

**Gradients add at forks.** If a value feeds several later operations, the gradients flowing back along each branch are summed. In code this means accumulating with `+=`, not overwriting.[^cs231n-bp]

**Patterns for common gates**:[^cs231n-bp]

| Gate | Forward | Backward |
|---|---|---|
| Add | $q = x + y$ | Copies the incoming gradient to both inputs |
| Multiply | $q = xy$ | Swaps the inputs: $\bar{x} = y\bar{q}$, $\bar{y} = x\bar{q}$ |
| Max or ReLU | $q = \max(x, y)$ | Routes the gradient to the larger input; the other gets 0 |

Here $\bar{v}$ denotes $\partial L / \partial v$. The multiply rule explains why input scale matters: multiplying every input by 1000 multiplies the weight gradients by 1000, so the learning rate would need to shrink accordingly.[^cs231n-bp]

## Dense Layer in Matrix Form

**Notation.** A layer computes $z = W x + b$ and then $h = \phi(z)$ for an element-wise activation $\phi$. The backward pass receives $\bar{h} = \partial L / \partial h$ from the layer above.

**Step 1: through the activation.** The Jacobian of an element-wise function is diagonal, so this is an element-wise product:

$$
\bar{z} = \bar{h} \odot \phi'(z)
$$

**Step 2: weight and bias gradients.**

$$
\bar{W} = \bar{z} \, x^\top, \qquad \bar{b} = \bar{z}
$$

**Step 3: gradient for the layer below.**

$$
\bar{x} = W^\top \bar{z}
$$

Step 3 is the vector–Jacobian product described in [[Jacobians]]. Dimension analysis is a reliable check: $\bar{W}$ must have the same shape as $W$, and only $\bar{z} x^\top$ produces that shape.[^cs231n-bp] With a mini-batch the per-example gradients are summed or averaged.

## Worked Example

**Inputs.** A two-layer network with input $x = (1, 2)$, no biases, a [[ReLU Function|ReLU]] hidden layer, target $t = 1$, and squared-error loss:

$$
L = \frac{1}{2}(y - t)^2
$$

The weights are:

$$
W_1 = \begin{bmatrix} 0.5 & -1 \\ 1 & 0.5 \end{bmatrix}, \qquad w_2 = (1, -1)
$$

**Step 1: forward pass.**

$$
z = W_1 x = (-1.5, \; 2), \qquad h = \mathrm{ReLU}(z) = (0, \; 2)
$$

$$
y = w_2 \cdot h = -2, \qquad L = \tfrac{1}{2}(-2 - 1)^2 = 4.5
$$

**Step 2: gradient at the output.**

$$
\bar{y} = y - t = -3
$$

**Step 3: output weights and hidden activations.** Multiply gate: each side receives the other side's value times $\bar{y}$.

$$
\bar{w}_2 = \bar{y} \, h = (0, \; -6), \qquad \bar{h} = \bar{y} \, w_2 = (-3, \; 3)
$$

**Step 4: through the ReLU.** Unit 1 was inactive ($z_1 < 0$), so its gradient is blocked.

$$
\bar{z} = \bar{h} \odot \mathbb{1}[z > 0] = (0, \; 3)
$$

**Step 5: first-layer weights and input.**

$$
\bar{W}_1 = \bar{z} \, x^\top = \begin{bmatrix} 0 & 0 \\ 3 & 6 \end{bmatrix}, \qquad \bar{x} = W_1^\top \bar{z} = (3, \; 1.5)
$$

**Step 6: gradient check.** Centred finite differences with $h = 10^{-5}$ on each entry of $W_1$ give the same matrix.

The first row of $\bar{W}_1$ is zero because the first hidden unit did not fire. If it never fires for any training example, it never learns; this is the "dead ReLU" problem in [[ReLU Function]]. The second output weight has gradient $-6$, so gradient descent will increase it, which raises $y$ towards the target. The values were computed in Python, and the gradient check was run.

## Practical Notes

- **Cache the forward pass.** The backward pass needs the forward values, such as $z$ and $h$ above. Storing them costs memory proportional to the network's activations, which is why activation memory often limits batch size.[^cs231n-bp]
- **Stage the computation.** Break complicated expressions into simple steps with known local gradients rather than deriving one large formula.[^cs231n-bp]
- **Check gradients** against centred finite differences on a few parameters, in double precision, before trusting a hand-written backward pass.
- **Frameworks do this automatically.** PyTorch, JAX and TensorFlow build the graph and run backpropagation. Custom layers still need a correct backward rule.

## Where It Goes Wrong

- **Vanishing and exploding gradients.** The backward pass multiplies many local derivatives and Jacobians. Saturating activations such as the [[Sigmoid Function|sigmoid]] shrink the product; large weights can blow it up. See [[Vanishing & Exploding Gradients]], [[Initialization]] and [[Gradient Clipping]].
- **Recurrent networks** apply backpropagation through time over the unrolled sequence, which makes these problems worse; see [[RNN]] and [[LSTM]].
- **Convolutions** backpropagate with the same rules; see [[CNN - Backward Prop]].

## Exercise

Change the target in the worked example to $t = -2$ and recompute every gradient. Explain why they are all zero. Then set $W_1[0, 1] = 0$ so that the first hidden unit becomes active, and recompute $\bar{W}_1$.

## Related Notes

- [[Computational Graph]] — Forward versus reverse mode and why backpropagation uses reverse mode.
- [[Jacobians]] — Vector–Jacobian products and layout conventions.
- [[Deep Learning]] — Where backpropagation sits in the training loop.

## References & Useful Links

[^baydin]: [Automatic Differentiation in Machine Learning: a Survey (Baydin et al., JMLR 2018)](https://arxiv.org/abs/1502.05767) — Backpropagation as a special case of reverse-mode AD, its history, and its memory cost.
[^cs231n-bp]: [CS231n: Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/) — Local gradients, staged computation, gradients adding at forks, add/multiply/max patterns, input-scale effects, and matrix-multiply gradients by dimension analysis.
