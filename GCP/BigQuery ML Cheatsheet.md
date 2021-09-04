## Workflow for Bigquery ML

- Dataset Creation
- Create/train
- Evaluate
- Predict/Classify

Lable - Alias a column as 'label' or specify column in Options using input_label_cols

Feature - Passed through to the model as part of your SQL SELECT statement

Model - an object created in BigQuery that resides in your BigQuery dataset

Model Types - Linear Regression, Logistic Regression

Create or Replace Model <Dataset>.<name> 
OPTIONS()model)type='<type>' AS 
<training dataset>
	
Training Progress - SELECT * FROM ML.TRAINING_INFO(MODEL 'mydataset.mymodel')
	
Inspect Weights - SELECT * FROM ML.WEIGHTS(MODEL 'mydataset.mymodel',(<query>))

Evaluation - SELECT * FROM ML.EVALUATE(MODEL, 'mydataset.mymodel')
	
Prediction - SELECT * FROM ML.PREDICT(MODEL 'mydataset.mymodel',(<query>))	

