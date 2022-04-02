#sim 
## Integral Formulae

$$\int x^k dx = \frac{x^{k+1}}{k+1} + C, k \neq 1$$
$$\int \frac {dx} x = ln|x| + c$$
$$\int e^{x} dx = e^{x} + c$$
$$\int e^{ax} dx = \frac {e^{x}} {a} + c$$
$$\int cos(x) dx = sin(x) + c$$
$$\int \frac {dx}{1+x^2} dx = arctan(x) + c$$
$$\int ln(x)dx =  x ( ln(x) -1) +C$$
## Properties of Integral

$$\int_{a}^{a}f(x)dx = 0 $$
$$\int_{a}^{b}f(x)dx = -\int_{b}^{a}f(x)dx$$

$$\int_{a}^{b}f(x)dx = \int_{c}^{a}f(x)dx + \int_{c}^{b}f(x)dx$$

$$\int f(x) + g(x) dx = \int f(x)dx + \int g(x)dx$$
$$\int [f(x)g(x)] dx = f(x)\int g(x) - \int( f'(x)\int g(x))dx$$
$$\int f(g(x))g'(x) dx = \int f'(u) du$$
## Integration by Riemann Sum

$$\int_{a}^{b}f(x)dx \approx \sum_{i=1}^{n}f(x_i)\Delta x = \frac{b-a}{n} \sum_{i=1}^{n}f(a + \frac{i(b-a)}{n})$$