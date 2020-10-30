`Motivation` : There is a need to understand the impact of new modification, if the new modification was a better modification. A/B testing works best when doing incremental changes.This is done using [[Hypothesis Testing]]

`Process` : AB testing involves comparing multiple versions of a feature - Button, page or flow

Advantage of AB Testing
1.	Removes the need for guessing or relying on intuition
2.	Provies accurate answers quickly
3.	Allows for rapid iteration on ideas
4.	Establishes causal relationships - not just correlations

A/B Testing cannot be used for
1. Testing major changes
	1. New Products
	2. New branding/ New user experience
2. Or testing on data-points with low activity
	1. As-in low purchase rates on a give page
		1. This will tend to blow out experiment timelines


### Design, Plan & Running the experiment

1. Research - To ensure best practices are followed and unearth results of similar experiment
2. Specifying the Null and Alternate Hypothesis
	1. Null Hypothesis : Assume no difference between the variants
	2. Alternate Hypothesis : Assume 20% improvement in performance than Variant A, variant B being the faster one
3. Specify the dependent variable : Defining the features which will be the defining factors
	1. Clicks to next page
	2. Put more items in cart
	3. Purchase Goods
	4. Or any call-to-action/metrics
4.	Experiment Designs
	1.	Baseline Rate - an estimate of the metric being analyzed before making any changes
	2.	Practical significance level - Minimum change to baseline rate that will be useful to the business
	3.	Confidence level - Significance level that the null hypothesis should be rejected and when it shouldn't be 
	4.	Sensitivity - the probability that the null hypothesis is not rejected when it should be
	5.	Length of experiment : How long should the experiment run?
	6.	No of users to be exposed to the test
	> Rolling of the variants to customer at the same time

---
Defination

`Control` The subset that doesn't see the new change
`Experiment` The subset that see's the new changes
`Baseline Rate` This is the current conversion rate that you want to test = Conversion_of_Control/Total_Control_Users
`Effect Size`  - The difference between  A and B 
`Practical Significane` Practical significance refers to the magnitude of the effect
`Confidence Inteval` Is the range of values that is likely to contain the population value
`Significane Level` $\alpha$  The significance level is a measure of how strong the sample evidence must be before determining the results are statistically significant
`Sensitivity` 1-$\beta$ refers to sensitivity

---
### Concerns with AB Testing

AB testing is used to manipulate the website in a way to ensure conversion ratios are high, however, overdoing AB testing in the long run can make a website more like a porn site. AB testing is designed to exploit psychology, people are not predictable and AB testing psychologically manipulate the end-consumer to get their dopamine level high - over mass population of people. 