---
tags:
  - "sim"
  - "ds-foundations"
---

Reference formulae for integration, the inverse of differentiation covered in [[Calculus]]. In data science, integrals give probabilities from a [[Probability Density Function]] and expectations of continuous random variables. When no closed form exists, they are approximated numerically, for example by Riemann sums or [[Monte-Carlo Simulation]].

## Integral Formulae

$C$ is an arbitrary constant of integration.

**Power rule** ($k \neq -1$).

$$
\int x^k \, dx = \frac{x^{k+1}}{k+1} + C
$$

**Reciprocal** ($x \neq 0$).

$$
\int \frac{1}{x} \, dx = \ln\lvert x\rvert + C
$$

**Exponential.**

$$
\int e^{x} \, dx = e^{x} + C
$$

**Scaled exponential** ($a \neq 0$).

$$
\int e^{ax} \, dx = \frac{e^{ax}}{a} + C
$$

**Cosine.**

$$
\int \cos x \, dx = \sin x + C
$$

**Arctangent form.**

$$
\int \frac{1}{1 + x^2} \, dx = \arctan x + C
$$

**Logarithm** ($x > 0$).

$$
\int \ln x \, dx = x(\ln x - 1) + C
$$

The power rule excludes $k = -1$ because it would divide by zero; that case is the reciprocal rule. Every rule can be checked by differentiating the right-hand side; for example:

$$
\frac{d}{dx} \frac{e^{ax}}{a} = e^{ax}
$$

## Properties of the Definite Integral

**Zero-width interval.**

$$
\int_{a}^{a} f(x) \, dx = 0
$$

**Reversing the limits flips the sign.**

$$
\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx
$$

**Additivity over intervals**, for any point $c$:

$$
\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx
$$

**Linearity.**

$$
\int \big[f(x) + g(x)\big] \, dx = \int f(x) \, dx + \int g(x) \, dx
$$

**Integration by parts.** With $u = f(x)$ and $dv = g(x)\,dx$:

$$
\int u \, dv = uv - \int v \, du
$$

**Substitution.** With $u = g(x)$ and $du = g'(x)\,dx$:

$$
\int f\big(g(x)\big) \, g'(x) \, dx = \int f(u) \, du
$$

The integrand on the right is $f(u)$, not $f'(u)$. Substitution undoes the chain rule, and integration by parts undoes the product rule.

## Integration by Riemann Sum

Split $[a, b]$ into $n$ strips and add up rectangle areas. Each strip has width:

$$
\Delta x = \frac{b - a}{n}
$$

With right endpoints $x_i = a + i \, \Delta x$:

$$
\int_{a}^{b} f(x) \, dx \approx \sum_{i=1}^{n} f(x_i) \, \Delta x = \frac{b - a}{n} \sum_{i=1}^{n} f\!\left(a + \frac{i(b - a)}{n}\right)
$$

The approximation improves as $n$ grows. Monte Carlo integration replaces the evenly spaced points with random ones, which scales better to many dimensions; see [[Monte-Carlo Simulation]].

## Worked Examples

### Integration by Parts

**Integral.**

$$
\int x e^{x} \, dx
$$

**Step 1: choose the parts.**

$$
u = x, \quad dv = e^{x} dx \;\Rightarrow\; du = dx, \quad v = e^{x}
$$

**Step 2: apply the formula.**

$$
\int x e^{x} \, dx = x e^{x} - \int e^{x} \, dx = x e^{x} - e^{x} + C
$$

Differentiating the result confirms it:

$$
\frac{d}{dx}\left(x e^{x} - e^{x}\right) = e^{x} + x e^{x} - e^{x} = x e^{x}
$$

### Substitution

**Integral.**

$$
\int 2x \cos(x^2) \, dx
$$

**Step 1: substitute.**

$$
u = x^2, \quad du = 2x \, dx
$$

**Step 2: integrate in $u$ and substitute back.**

$$
\int \cos u \, du = \sin u + C = \sin(x^2) + C
$$

### Riemann Sum

**Inputs.** The integral below, with $n = 4$ right-endpoint strips, so $\Delta x = 0.25$:

$$
\int_0^1 x^2 \, dx
$$

**Step 1: approximate.**

$$
0.25 \times \left(0.25^2 + 0.5^2 + 0.75^2 + 1^2\right) = 0.25 \times 1.875 = 0.46875
$$

**Step 2: exact value.**

$$
\int_0^1 x^2 \, dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} \approx 0.3333
$$

Right endpoints overestimate an increasing function, so the four-strip sum is too large by about $0.135$. With $n = 100$ the same rule gives $0.33835$. The values were recalculated in Python.

## Related Notes

- [[Calculus]] — Derivative rules that these formulae invert.
- [[Probability Density Function]] and [[Cumulative Density Function]] — Probabilities as integrals of a density.
- [[Formulae's for Series, Taylor Series & Maclaurin Series]] — Series used alongside these formulae.

## References & Useful Links

- [Substitution Rule for Indefinite Integrals (Paul's Online Math Notes)](https://tutorial.math.lamar.edu/Classes/CalcI/SubstitutionRuleIndefinite.aspx) — The substitution rule stated above, with worked examples.
- [Integration by Parts (Paul's Online Math Notes)](https://tutorial.math.lamar.edu/Classes/CalcII/IntegrationByParts.aspx) — Derivation from the product rule, the integration-by-parts formula stated above, and examples including the integral of $\ln x$.
