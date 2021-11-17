### Reasoning 
Permutation importance is a type of [[Feature Importance]] method. It indicates a drop in score if a feature is replaced with randomly permuted values. 

Reasons for its popularity is
- Fast to calculate
- Widely used and understood
- Inline with what we want [[Feature Selection]] process to actually measure

### Technique
This technique is used for calculating relative importance scores that is independent of the model used.

- This is calculated after the model has been fitted
- First the model score is noted 
- Then each feature is randomly permuted
- The prediction score is noted, $\delta$ is noted wrt to Model Score and Permutation score, the one with higher $\delta$ gets a higher permutation score

### Premise of Permutation Importance
- The premise here is : If a single feature is randomly shuffled, leaving the target and all others in place, how will it affect the final prediction performance. Here two things can play out
	- Less accurate predictions - since the data no longer corresponds to anything observed in the real world
	- Terrible performance, This will happen due to breakage in the strong relationship, which the model has picked up during training

### Code

```py
from sklearn.inspection import permutation_importance
permuation_importance(model, X,y, scoring='neg_mean_squared_error')


import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(Model).fit(X,y)
eli.show_weights(perm, feature_names = column_names)
```