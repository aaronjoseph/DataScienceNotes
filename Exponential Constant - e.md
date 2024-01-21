Here's a refined version of your notes on Euler's constant \( e \) and Fourier's proof that \( e \) is an irrational number:

---

## Facts on \( e \) - Euler's Constant

- Euler's constant \( e \) has a non-repeating, non-terminating decimal expansion, similar to \( \pi \).
- It emerges in the context of compounded interest, various probability distributions, and in certain gambling probability scenarios.
- The mathematical series for \( e \) is expressed as:

$$
e = \sum_{n=0}^{\infty} \frac{1}{n!}
$$

- Additionally, \( e \) is characterized by the property that the area under the curve \( y = \frac{1}{x} \) from \( x = 1 \) to \( x = e \) is exactly 1 square unit.

## Fourier's Proof that \( e \) is an Irrational Number

A rational number is defined as one that can be expressed as the ratio of two integers, say \( P \) and \( Q \):

$$
\text{Rational Number} = \frac{P}{Q}
$$

For \( e \) to be rational, it would need to satisfy the equation:

$$
\frac{P}{Q} = \sum_{n=0}^{\infty} \frac{1}{n!}
$$

It's evident from the series that \( e \) is greater than 2:

$$
e > 2
$$

Looking at the remaining terms of the series, we compare it with a geometric series to show that the sum of the remaining terms is greater than 1, hence \( 2 < e < 3 \):

$$
\text{Let } R = \sum_{n=2}^{\infty} \frac{1}{n!}
$$

This sum \( R \) is greater than the sum of a corresponding geometric series:

$$
R > \sum_{n=1}^{\infty} \frac{1}{2^n} = 1
$$

By assuming \( e \) can be expressed as a rational number \( \frac{P}{Q} \), and multiplying the series by \( Q! \), we get:

$$
PQ! = Q! + Q! + \frac{Q!}{2!} + \frac{Q!}{3!} + \ldots + 1 + \frac{1}{Q+1} + \ldots
$$

This implies that \( P \) must be greater than \( Q \), as \( e > 2 \). However, the right-hand side of the equation will always have non-integer terms past \( 1 \), no matter how large \( Q \) is chosen to be. This contradiction shows that \( e \) cannot be expressed as \( \frac{P}{Q} \), thus proving that \( e \) is irrational.

$$
\text{Thus, } e \neq \frac{P}{Q} \text{ and } e \text{ is irrational.}
$$

--- 
