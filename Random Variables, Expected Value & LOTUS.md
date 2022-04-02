#sim 

Theorem : If X is a continous random variable with cdf F(x), then the random variable F(X) ~ Unif(0,1)

## Expected Value

Definition: The mean or expected value or average of a RV X is

$$\mu = E[X] =
\begin{dcases}
    \sum_{x} xf(x),& \text{if X is discrete }\\
    \int_{R} xf(x) dx, &\text{if X is continous }
\end{dcases}
``` $$
The mean gives an indication of an RV’s central tendency. It can be thought of as a weighted average of the possible x’s, where the weights are given by f(x).

## LOTUS
The Law of the Unconscious Statistician

Theorem : The expected value of a function of X, say h(X), is

$$E[h(X)] = 
\begin{dcases}
    \sum_{x} h(x)f(x),& \text{if X is discrete }\\
    \int_{R} h(x)f(x) dx, &\text{if X is continous }
\end{dcases}
$$
> Derivative of CDF is equal to the PDF


$$E[Y|X=x] = 
\begin{dcases}
    \sum_{y} yf(y|x),& \text{if y is discrete }\\
    \int_{R} yf(y|x) dy, &\text{if y is continous }
\end{dcases}
$$
