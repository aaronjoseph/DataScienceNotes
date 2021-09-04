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


### Other examples

- During Data Pre-processing Stage
	- Pre-processors like [[Imputing Missing Values| Imputers]], [[Feature Scaling|Normalizer/Standardization]], Log Transformers tap into the underlying data distribution during the fit time
	- For example, if we use StandardScaler, which subtracts the mean from every observation and then divides it with the standard deviation. Calling it on the entire data, will cause the transformer to learn the mean and SD of the entire distribution of each feature. After this if we are to split the data into train and test sets, the train set is contaminated - since the StandardScaler leaked important information from the actual distribution
		- To avoid this, always try to use the `built-in pipeline features` 