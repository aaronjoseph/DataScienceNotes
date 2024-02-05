> In Data Drift, we have to correct for `x`, the predictor 

- When the underlying data distrubution shifts, it causes data drift
- Also referred to as 
	- Feature Drift
	- Population Drift
	- Covariate Shift
- Data drifts can degrade model performance over time
- For instance, when models are trained with a specific dataset and over time the data distribution changes, the model will no longer give the right results
- Example
	- Assume you train CV model based on mobile with low-resolution (assume 1.2 MP camera)
	- Overtime, hardware improvements will cause the image quality to improve, which will lead to higher resolution of the image
	- This causes data drift in the case of the underlying models

### Reasons for Data Drift

Data Changes 
- TREND AND SEASONALITY
- DISTRIBUTION OF FEATURES CHANGES 
- RELATIVE IMPORTANCE OF FEATURE CHANGES

World Changes 
- FASHION CHANGE 
- SCOPE AND PROCESSES CHANGE
- COMPETITORS CHANGE
- BUSINESS EXPANDS TO OTHER GEOS

### Training Serving Skew

Training serving skew is a case wherein the training data and the production use case data differ drastically. This leads to major performance issues.