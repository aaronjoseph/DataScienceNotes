### Need for Feature Importance

For any business application, there is a need to understand how the model provides the results
- Which Variables are most engaged in the model
- Presence of Correlations
- Possible causation relationships

For such tasks, `Tree` based methods are quite useful, they are scalable and permits to compute variable explanation very easily.

For neural networks, [[Permuatation Importance]] can be used to understand which variable is most engaged

- Feature Importance can provide insights into the dataset - relative score can highlight which feature may be most relevant to the target and the converse, which features are the least relevant. 
- Feature Importance can vary from model to model 
- Feature Importance can help understand which feature to drop based on the scores and [[Dimensionality Reduction]] can be done on the same

---

### Feature Importance Code

- Linear Regression & Logistic Regression
```py
# For Linear Regression we can obtain the coefficients
importance = model.coef_
for i,v in enumerate(importance):
	print(i,v)
```

- DecisionTrees
```
# For Trees Based Models
importance = model.feature_importances_
```
 
 > Results of a tree based model will differ based on the Stocastic nature of the model
