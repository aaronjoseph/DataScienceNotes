---
tags:
  - "sim"
  - "ds-foundations"
---

Reference formulae for single-variable differential calculus, numerical root finding, and a simulation formula. The derivative rules here underlie the gradients used to train models; see [[Gradient Descent]].

## Derivative Definition

$$
\frac{d}{dx} f(x) = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

The derivative is the instantaneous rate of change of $f$ at $x$: the slope of the tangent line.

## Common Derivatives

| Function | Derivative |
|---|---|
| $x^{k}$ | $k \, x^{k-1}$ |
| $e^{x}$ | $e^{x}$ |
| $e^{ax}$ | $a \, e^{ax}$ |
| $a^{x}$ | $a^{x} \ln a$ |
| $\ln x$ | $1/x$ for $x > 0$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\arctan x$ | $\dfrac{1}{1 + x^{2}}$ |
| $e^{f(x)}$ | $e^{f(x)} \, f'(x)$ |
| $a^{f(x)}$ | $a^{f(x)} \ln a \; f'(x)$ |

Do not confuse the power rule, where the variable is in the base ($x^k$), with the exponential rule, where it is in the exponent ($a^x$).

## Differentiation Rules

**Constant multiple and constant term.**

$$
\big[a f(x) + b\big]' = a f'(x)
$$

**Sum rule.**

$$
\big[f(x) + g(x)\big]' = f'(x) + g'(x)
$$

**Product rule.**

$$
\big[f(x) g(x)\big]' = f'(x) g(x) + f(x) g'(x)
$$

**Quotient rule.** Keep the order of the numerator: swapping the two terms flips the sign.

$$
\left[\frac{f(x)}{g(x)}\right]' = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}
$$

**Chain rule.**

$$
\big[f(g(x))\big]' = f'\big(g(x)\big) \, g'(x)
$$

The chain rule is the basis of backpropagation: a network is a long composition of functions, and its gradient is the product of local derivatives. See [[Computational Graph]]. The quotient rule is used to derive $\tanh'(x)$ in [[Tanh Function]].

## Methods of Solving for Equations

These methods find a root, a value $x^*$ with $g(x^*) = 0$, when no closed form is convenient. Each worked example below uses $g(x) = x^2 - 2$, whose positive root is $\sqrt{2} \approx 1.41421$.

1. **Trial and error.** Evaluate candidates and refine by hand. It is simple but slow, with no guarantee of progress.
2. **Bisection method.** Start from an interval $[a, b]$ where $g(a)$ and $g(b)$ have opposite signs. For a continuous $g$ a root lies between them. Evaluate the midpoint, keep the half-interval whose endpoints still differ in sign, and repeat. Each step halves the interval, so convergence is guaranteed but slow.
3. **Newton's method.** Follow the tangent line to where it crosses zero:

$$
x_{i+1} = x_i - \frac{g(x_i)}{g'(x_i)}
$$

Near a simple root Newton's method converges very quickly, but it needs the derivative. It can diverge from a poor starting point, and it fails where $g'(x_i) = 0$. The same idea, applied to the derivative of a loss, underlies second-order optimisation; see [[Optimization Algorithms]].

### Worked Example: Bisection

**Inputs.** $[a, b] = [1, 2]$, where $g(1) = -1 < 0$ and $g(2) = 2 > 0$.

**Step 1.** The midpoint is $1.5$:

$$
g(1.5) = 0.25 > 0 \;\Rightarrow\; [1, 1.5]
$$

**Step 2.** The midpoint is $1.25$:

$$
g(1.25) = -0.4375 < 0 \;\Rightarrow\; [1.25, 1.5]
$$

**Step 3.** The midpoint is $1.375$:

$$
g(1.375) = -0.109 < 0 \;\Rightarrow\; [1.375, 1.5]
$$

After three steps the root is known to lie in an interval of width $0.125$.

### Worked Example: Newton's Method

**Inputs.** $g'(x) = 2x$ and starting point $x_0 = 1$.

**Step 1.**

$$
x_1 = 1 - \frac{1 - 2}{2} = 1.5
$$

**Step 2.**

$$
x_2 = 1.5 - \frac{0.25}{3} \approx 1.41667
$$

**Step 3.**

$$
x_3 = 1.41667 - \frac{1.41667^2 - 2}{2 \times 1.41667} \approx 1.414216
$$

After three steps Newton's method is within $0.000003$ of $\sqrt{2} \approx 1.414214$, while bisection has only narrowed the root to an interval of width $0.125$. The price is needing $g'$ and a reasonable starting point. The values were recalculated in Python.

## L'Hôpital's Rule

**Theorem.** Suppose $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ are both $0$, or both $\pm\infty$. Suppose also that $f$ and $g$ are differentiable near $a$, with $g'(x) \neq 0$ there, and that the limit on the right exists. Then:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
$$

**Example.** $\sin x / x$ is of the form $0/0$ at $x = 0$:

$$
\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1
$$

The rule applies only to the indeterminate forms $0/0$ and $\infty/\infty$. Other forms, such as $0 \cdot \infty$, must first be rewritten as a ratio.

## Deterministic and Stochastic Processes

- **Deterministic.** In a deterministic process, the outcomes can be fully determined from the initial conditions.
- **Stochastic.** Stochastic models accept that certain things happen randomly, so the same initial conditions can lead to different outcomes. See [[Simulation]] and [[Monte-Carlo Simulation]].

### Exponential Random Variate

To simulate an exponential random variable with rate $\lambda$ from a pseudo-random uniform number $U \sim \mathcal{U}(0, 1)$, invert the cumulative distribution function $F(x) = 1 - e^{-\lambda x}$:

$$
X = -\frac{1}{\lambda} \ln(1 - U)
$$

Because $1 - U$ has the same distribution as $U$, this is usually written as:

$$
X = -\frac{1}{\lambda} \ln(U), \quad \text{where } U \text{ is the pseudo-random number}
$$

**Example.** With $\lambda = 2$ and $U = 0.5$, $X = -\ln(0.5)/2 \approx 0.347$. See [[Random Number Generator]] for how $U$ is produced.

## Related Notes

- [[Integral]] — Antiderivative formulae.
- [[Formulae's for Series, Taylor Series & Maclaurin Series]] — Series expansions built from derivatives.
- [[Exponential Constant - e]] — Why $e^x$ is its own derivative.
- [[Jacobians]] — Derivatives of vector-valued functions.
- [[Gradient Descent]] — Partial derivatives in model training.

## References & Useful Links

- [The Matrix Calculus You Need for Deep Learning (Parr and Howard)](https://explained.ai/matrix-calculus/index.html) — Reviews the scalar derivative rules, including the chain rule, and extends them to vectors.