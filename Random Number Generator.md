---
tags:
  - "sim"
---
## Unif(0,1) PRN
- It is a deterministic algorithm
- Linear Congruential Generator Approach
	- Choose an integer "seed", X(0)
	- Set X(i) = aX(i-1)mod(m), where a & m are pre-selected
	- Then we have, U(i) = X(i)/m

## Exponential Generator
- This starts with Unif(0,1) PRN
- Starts with U(i)
- Then transformation is applied
	- The inverse transform:

		$$
		X(i) = -\frac{1}{\lambda} \ln U(i) \sim \text{Exp}(\lambda)
		$$

	- The above equation is sometimes close to 