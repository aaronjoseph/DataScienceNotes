#sim 

## Derivative Formulae

$$\frac{d}{dx}f(x) = f'(x) = lim_{h-> 0}\frac{f(x+h) - f(x)}{h}$$

## Other Key formulaes

$$[k^{x}]' = xk$$
$$[e^{x}]' = e^{x}$$
$$[e^{ax}]' = ae^{x}$$
$$[sin(x)]' = cos(x)$$
$$[cos(x)]' = -sin(x)$$
$$[ln(x)]' = 1/x$$
$$[arctan(x)]' = \frac{1}{1+x^{2}}$$
$$[a^x]’ = a^x \: ln(a)$$ $$[e^{f(x)}]' = e^{f(x)} \: f'(x)$$$$[a^{f(x)}]' = a^{f(x)}\: ln(a) \: f'(x) $$
## Key Formulae
$$[af(x)+b]'= af'(x)$$
$$[f(x) + g(x)]' = f'(x) + g'(x)$$
Quotient Rule
$$[\frac{f(x)}{g(x)}]' = \frac{f(x)g'(x) - f'(x)g(x)}{g^2(x)} $$
Chain Rule
$$[f(g(x))]' = f'(g(x))g'(x)$$

Product Rule
$$[f(x)g(x)]'=f(x)g'(x) + f'(x)g(x)$$
## Methods of Solving for Equations
1. Trail and Error 
2. Bisection Method
	1. Here, you start between two points and use deductive reasoning to reach to a solution
3. Newton's Method
	1. $$x_{i+1} = x_i - \frac{g(x)}{g'(x)}$$
	2. Using the above formulae, we can reach the solution

## L'Hopital's Rule

**Theorem**: Occasionally, we run into trouble when taking indeterminate ratios of the form 0/0 or ∞/∞. In such cases, L’Hôpital’s Rule is useful: If $lim_{x→a}$ f(x) and $lim_{x→a}$ g(x) both go to 0 or both go to ∞, then

$$lim_{x->a} \frac{f(x)}{g(x)} = lim_{x->a} \frac{f'(x)}{g'(x)}$$
## Deterministic & Stocastic Processes

`Deterministic` : In deterministic process, the outcomes can be fully determined from initial conditions.

`Stochastic` models accept that certain things can happen randomly. 

### Exponential Random Variate Formulae
$$X = - \frac{1}{\lambda}ln(U), \text{where U is the pseudo-random number}$$