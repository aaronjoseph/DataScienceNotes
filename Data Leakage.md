Data Leakage is the creation of unexpected additional information in the training data, allowing a model or machine learning algorithm to make unrealistically good predictions

Due to Data Leakage, `model will seem to perform well in training data, till it is used in production systems`

There are two types of leakage
- Leaky Predictor
- Leaky Validation Strategies

### Leaky Predictors

This happens when your predictors include data that will not be available at the time when you make predictions.

Leaky Predictors cannot be identified by a simple boilerplate technique. 
- To screen for possible leaky predictors, look for columns that are statistically correlated to the target
- If you build a model and find it extremely accurate, you have a leakage problem

Sources of Leaky Predictors
- ID-Leaks
- Leaking future information into past
- Leaking target information into feature matrices

### Leaky Validation Strategy

Based on the data-preprossing strategies, there are subtle ways of affecting the [[Cross Validation|validation]] process. 

Scenario
- Validating model on already seen data

Controling LVS
-  Make use of Scikit-Learn pipeline to streamline the process