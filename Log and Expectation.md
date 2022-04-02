#sim 

## Log Rules

$$log_b(xy) = log_bx + log_by$$
$$log_b(x/y) = log_bx - log_by$$
$$log_b(x^r) = r\: log_bx$$
$$log_b(x) = log_a(x)/ log_a(b)$$

## Expectation & Variance

$$E[aX + b] = aE[X] + b$$
$$E[aX + bY] = aE[X] + bE[Y]$$
$$E[XY] = E[X]E[Y]+ Cov(X,Y)$$
$$E[E[Y|X]] = \int_{-\infty}^{\infty}E[Y|x]f_Xdx$$
**Double Expectation**

$$E[E[Y|X]] = E[Y]$$$$E[Y] = \int_{-\infty}^{\infty}yf_Y(y)dy$$$$Var(X) = E[X^2] – E[X]^2 = Cov(X,X)$$
$$Var(aX \pm bY) = a^2Var(X) + b^2Var(Y) \pm 2abCov(X,Y)$$
$$Cov(X,Y) =E[ (X-E[X]) (Y-E[Y]) = E[XY] – E[X]E[Y]$$
$$Var(XY) = Cov(X^2,Y^2) + [Var(X)+ E(X)^2][Var(Y)+E(Y)^2] – [Cov(X,Y) + E(X)E(Y)]^2$$
$$Cov(aX,bY) = abCov(X,Y) Cov(X+Y,Z) = Cov(X,Z) + Cov(Y,Z)$$
$$Cov(S,T) = Corr(S,T) \sqrt{Var(S)Var(T)}$$

>IF X & Y are independent

$$Var(X+Y) =Var(X)+Var(Y) + 2Cov(X+Y)$$
$$\rho_{xy} \text{ or } Corr(X,Y)  = Cov(X,Y) / \sqrt{Var(X)+Var(Y)}$$
	