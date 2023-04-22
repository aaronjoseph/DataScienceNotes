### Main Concepts

Adaptive Boosting or AdaBoost is one of the simplest boosting algorithm. Here, decision trees are used as base ensemble, wherein sequential models are created , each correcting the errors of the last model. 

Steps followed
1. Initially, all observation in the datasets are given equal weights
2. A decision stump is created [Decision Tree with one level]
	1. Here, each feature is runned through decision stump
	2. The decision stump with the least entropy will be selected
3. Subsequent calculations are made
	1. Total Error = $\frac{E}{T}$
		1. Here, E is the number of errors made
		2. T refers to the total number of data points
	2. Performace of Stump = $\frac{1}{2}log_e\frac{1-TotalError}{TotalError}$
	3. Using the above equations, weights are updated for each record. Here, the incorrect predictions should get the higher weights
		1. First is the updation cycle wherein the weights are updated as per the formulae, summation of all the weights will not be equal to 1
			1. Here, the incorrect predictions are assigned the new value = $OldWeight * e^{Performance of Stump}$
			2. Correct Prediction Records are updated with $OldWeight * e^{-Performance of Stump}$
		2. Next stage is to normalize, wherein the summation is taken for the records and is normalized accordingly
	4. Next step is to get a new distribution of data wherein there will be higher weightage given to the incorrectly classified data -> Since it has gotten higher weights
4. This step continoues sequentially and the above steps are repeated

> In Adaboost, decision trees are generally a node and two leaves. A decision tree of this kind is called a stump

---
### Code
```py
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
```
