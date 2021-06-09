## Q1. What percentage of values lie between mean and 1 Standard Deviation (Both Positive & Negative)

- `Major Concern` The answer is not ~68% if the data is non-gaussian
	- This question is intentionally ambigouse
	- `Interviewer expects a good follow-up`
- `If the distribution is non-gaussian then you will need to find the percentage of values between` [$\mu + \sigma$,$\mu - \sigma$]
	- Chebyshev's Inequality can be used for this 
	- \>= 0% to 100% <= values can lie between [$\mu + \sigma$,$\mu - \sigma$], in the case of non-Gaussian distribution
	- 68% for Gaussian distribution

## Q2. Give an example where Chebyshev's inequality fails

