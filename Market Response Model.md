[[Growth Hacking]]

Market response models is designed to help corporations understand how consumers individually and collectively respond to marketing activities and how competitors interact.

Market response models should be 
- Cross Functional
- Inclusive of short term and long term effects
- Considerate of Capital Markets


### Uplift

Uplift would be the difference between the actual and the anticipated, related to the anticipated

There can be 3 types of uplift
- Conversion Uplift - Conversion rate of test group - Conversion rate of control group
- Order Uplift - Conversion Uplift * (# Converted Customer in test group)
- Revenue Uplift - Order Uplift * Average order $ value

### Uplift Modeling

Given a promotion plan, it isn't a good idea to hand over the benifits to all the customers within the segement, there are ways of looking at this

- **Treatment Responders**  Customer that will purchase only if they receive an offer `TR`
- **Treatment Non-Responders** Customer that won't purchase in any case `TN`
- **Control Responders** Customers that will purchase without any offer `CR`
- **Control Non-Responders** Customers that will not purchase if they don't receive any offer `CN`

Here, Ideally we need to target **Treatment Responders** and **Control Non-Responders**

$$Uplift Score = P_{TR} + P_{CN} - P_{TN} - P_{CR}$$

Higher the value of TR & CN, higher is the uplift

In uplift modeling, we need to 
- Determine the type of customer we have - based on the 4 categories above
- Next, we need to do multi-class classification
- After which , the model needs to obtain the probability score of each entry
- Then, we can obtain the uplift formulae based on the formulae above and take customer cohort which has higher uplift value
- One with higher uplift value will give better results for the organisation as a whole

