## Facts on e - Euler's Constant

- The decimal representation of e goes on forever, with no repeating blocks of number - similar to $\pi$
- e rises in the study of compound interest, gambling and many probability distribution
- Formulae for e is 

$$e = \sum_{n=1}^{\infty}\frac{1}{n!} $$

- e can also be defined as the area under the curve y=1/x from x=1 to x=e is 1 square unit

## Fourier's Proof that e is irrational Number

For a number to be rational, it should be expressed as ratio of two integers, lets say P & Q

$$Rational Number = \frac{P}{Q}$$

For e to be rational, we need to prove,

$$\frac{P}{Q} = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac {1}{4!} + ...$$

Clearly, by looking at the first two terms, e is greater than 2

$$ e > 2 $$

For the rest of the series

$$ 
\begin{aligned} 
\frac{1}{2!} +  \frac{1}{3!} + \frac{1}{4!} + \frac{1}{5!} + ... (1) \\
Compare \ With \ Below Equation \\
\frac{1}{2^1} +\frac{1}{2^2} +\frac{1}{2^3} +\frac{1}{2^4} + ... (2)\\
Clearly, Eq (1) > Eq(2) \\
\\
Given \ that \ Eq(2) \ is \ a \ Geometiric \\
Progression \ Equation \\
We \ have \ the \ following \\
S_{\infty} = \frac{a}{1-r} \\
\therefore Eq(2) = \frac{1/2}{1-(1/2)} = 1 \\
Also, Eq(2) < Eq(1) \\
\therefore Rest \ of \ e > 1 \\
Hence, 2 < e < 3
\end{aligned} 
$$

Assume, in the extension of e, there exists a point where Q factorial exists as depicted below

$$
\begin{aligned}
\frac{P}{Q} = \frac{1}{0!} +\frac{1}{1!} +\frac{1}{2!} +\frac{1}{3!} +\frac{1}{4!} + ...+ \frac{1}{Q!} +\frac{1}{Q!(Q+1)} + ..\\
Multiply \ both \ sides \ by \ Q! \\
\frac{PQ!}{Q} = \frac{Q!}{0!} +\frac{Q!}{1!} +\frac{Q!}{2!} +\frac{Q!}{3!} +\frac{Q!}{4!} + ...+ \frac{Q!}{Q!} +\frac{Q!}{Q!(Q+1)} + ..\\
Simplyfying \\
P(Q-1)! = \frac{Q!}{0!} +\frac{Q!}{1!} +\frac{Q!}{2!} +\frac{Q!}{3!} +\frac{Q!}{4!} + ...+ \frac{1}{1} +\frac{1}{(Q+1)} + ..\\
\end{aligned}
$$

Consider the above equation, P should be greater than Q, since  3 > e > 2 . Therefore, both terms are integers

$$
\begin{aligned}
Integer = \frac{Q!}{0!} + \frac{Q!}{1!} + \frac{Q!}{2!} + \frac{Q!}{3!} + ...+ 1 + \frac{1}{Q+1} + .. \\
Integer = Integer + \frac{1}{Q+1} + \frac{1}{(Q+1)(Q+2)} + .. Eq(3)\\ 
For \ the \ last \ term \\
\frac{1}{Q+1} + \frac{1}{(Q+1)(Q+2)} + \frac{1}{Q(Q+1)(Q+2)(Q+3)} + .. \\
Compare it with the geometric series \\
\frac{1}{Q^1} + \frac{1}{Q^2} +\frac{1}{Q^3} +\frac{1}{Q^4} +... \\

Since \ Q > 1, the \ sum \ of \ geometric \ series \ has \ to \ be \ less \ than \ 1 \\
\frac{\frac{1}{Q}}{1-(1/Q)} = \frac{1}{Q-1} < 1 \\
We \ Have \ the \ following \ from \ Eq(3) \\
Integer = Integer + Non-Integer \\
\therefore e \ is \ irrational \\
e \neq \frac{P}{Q}
\end{aligned}
$$