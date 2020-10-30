- Are there any circumstances when it is better to split into 3 groups ?

Not necessary, since it can be split in the next level

- How does decision tree make predictions ?

Given a datapoint, you run the entire tree asking True/False questions up until it reaches leaf node. The final prediction is the average of the value of the dependent variable in the leaf node

- Drawback of tree based models ?

Decision tree and  tree based models in general are unable to extrapolate to any kind of data they haven’t seen before, particularly future time period as it’s just averaging data points it has already seen.