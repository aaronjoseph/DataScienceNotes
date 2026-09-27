---
tags:
  - "ds-foundations"
---

The Jacobian collects every first-order partial derivative of a vector-valued function. In deep learning it describes how each layer's outputs respond to its inputs or weights, and chaining layer Jacobians is what backpropagation does to compute gradients for [[Gradient Descent]].

## Definition

For $f : \mathbb{R}^n \to \mathbb{R}^m$ with input $x$ and output $y = f(x)$, the Jacobian is the $m \times n$ matrix:

$$
J = \frac{\partial y}{\partial x} =
\begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \cdots & \frac{\partial y_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial y_m}{\partial x_1} & \cdots & \frac{\partial y_m}{\partial x_n}
\end{bmatrix}
$$

Entry $J_{ij} = \partial y_i / \partial x_j$ says how much output $i$ moves per unit change in input $j$. Row $i$ is the gradient of $y_i$. A scalar function ($m = 1$) has a $1 \times n$ Jacobian, which is its gradient written as a row.

## Numerator and Denominator Layout

The same partial derivatives can be arranged in two ways. Take $f$ with components $(f_1, f_2, f_3)$ and weights $w = (w_1, w_2)$.

**Numerator layout.** Rows follow the function components and columns follow the variables, giving shape $3 \times 2$:

$$
\frac{\partial f}{\partial w} =
\begin{bmatrix}
\frac{\partial f_1}{\partial w_1} & \frac{\partial f_1}{\partial w_2} \\
\frac{\partial f_2}{\partial w_1} & \frac{\partial f_2}{\partial w_2} \\
\frac{\partial f_3}{\partial w_1} & \frac{\partial f_3}{\partial w_2}
\end{bmatrix}
$$

**Denominator layout.** Rows follow the variables and columns follow the function components, giving shape $2 \times 3$:

$$
\frac{\partial f}{\partial w} =
\begin{bmatrix}
\frac{\partial f_1}{\partial w_1} & \frac{\partial f_2}{\partial w_1} & \frac{\partial f_3}{\partial w_1} \\
\frac{\partial f_1}{\partial w_2} & \frac{\partial f_2}{\partial w_2} & \frac{\partial f_3}{\partial w_2}
\end{bmatrix}
$$

The denominator layout is the transpose of the numerator layout. Papers and libraries use both, so check the convention before multiplying Jacobians together.[^parr] This note uses the numerator layout.

## Chain Rule and Backpropagation

For a composition $y = f(u)$ with $u = g(x)$, the Jacobians multiply:

$$
\frac{\partial y}{\partial x} = \frac{\partial y}{\partial u} \, \frac{\partial u}{\partial x}
$$

A network is a long composition ending in a scalar loss $L$. In numerator layout the gradient with respect to a layer's input is a **vector–Jacobian product**:

$$
\nabla_x L = J^\top \, \nabla_y L
$$

Here $J = \partial y / \partial x$ is that layer's Jacobian. Reverse-mode automatic differentiation computes $J^\top r$ directly for a given vector $r$ without building $J$ explicitly, which is essential when a layer has millions of inputs and outputs.[^baydin] See [[Computational Graph]] for the mechanics.

## Worked Example

**Inputs.** Weights $w = (w_1, w_2) = (2, 3)$ and a function $f : \mathbb{R}^2 \to \mathbb{R}^3$:

$$
f(w) = \big(w_1 w_2,\; w_1 + w_2,\; w_1^2\big)
$$

**Step 1: Jacobian (numerator layout, $3 \times 2$).**

$$
J =
\begin{bmatrix}
w_2 & w_1 \\
1 & 1 \\
2 w_1 & 0
\end{bmatrix}
=
\begin{bmatrix}
3 & 2 \\
1 & 1 \\
4 & 0
\end{bmatrix}
$$

**Step 2: gradient of the scalar loss $L = f_1 + f_2 + f_3$.** Here $\nabla_f L = (1, 1, 1)$, so:

$$
\nabla_w L = J^\top \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 + 1 + 4 \\ 2 + 1 + 0 \end{bmatrix} = \begin{bmatrix} 8 \\ 3 \end{bmatrix}
$$

**Step 3: direct check.** $L = w_1 w_2 + w_1 + w_2 + w_1^2$, so $\partial L / \partial w_1 = w_2 + 1 + 2w_1 = 8$ and $\partial L / \partial w_2 = w_1 + 1 = 3$.

The vector–Jacobian product matched direct differentiation. Transposing $J$ is what sends the loss sensitivity from the three outputs back to the two weights.

## Why Jacobians Matter in Deep Learning

- **Gradient computation.** Every backward step through a layer is a vector–Jacobian product.
- **Gradient flow and stability.** Glorot and Bengio link training difficulty to layer Jacobians whose singular values are far from 1: repeated products then shrink or amplify signals.[^glorot] See [[Vanishing & Exploding Gradients]] and [[Initialization]].
- **Structure and efficiency.** Element-wise operations, such as activation functions, have diagonal Jacobians, so frameworks apply them as element-wise multiplications.[^parr]
- **Sensitivity analysis.** The Jacobian of outputs with respect to inputs shows which input features most affect a prediction locally. It is a local, first-order view, not a causal explanation.
- **Optimisation.** Accurate gradients let the [[Optimization Algorithms|optimisers]] make informed updates.

## Related Notes

- [[Calculus]] — Scalar derivative rules that fill each Jacobian entry.
- [[Computational Graph]] — Forward and reverse modes, and when each is efficient.
- [[Sigmoid Function]] and [[Tanh Function]] — Diagonal Jacobians whose entries shrink when units saturate.

## References & Useful Links

[^parr]: [The Matrix Calculus You Need for Deep Learning (Parr and Howard)](https://explained.ai/matrix-calculus/index.html) — Jacobian shapes, numerator versus denominator layout, diagonal Jacobians of element-wise operations, and the vector chain rule.
[^baydin]: [Automatic Differentiation in Machine Learning: a Survey (Baydin et al., JMLR 2018)](https://arxiv.org/abs/1502.05767) — Reverse mode computes transposed Jacobian–vector products without forming the full Jacobian.
[^glorot]: [Understanding the Difficulty of Training Deep Feedforward Neural Networks (Glorot and Bengio, AISTATS 2010)](https://proceedings.mlr.press/v9/glorot10a.html) — Abstract links training difficulty to layer-Jacobian singular values far from 1.
