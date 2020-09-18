Group of predictors is called ensemble. Combining the predicitons from multiple models can result in more stable predictions, in some cases predictions that have better performance than any of the contributing models. 

The use of ensemble for predictors is called ensemble learning.

Two Types of Ensemble Learning
1. Bagging -> [[Random Forest]]
2. Boosting -> XGBoost, ADABoost, GBoost

`Hard-Voting` - Here each predictor's class is taken and the majority voting is done to determine the output

`Soft-Voting` - Each predictor's probability score is taken, post which, for the final calculation the probability score value is averaged out to get the final value

- Ensemble works best when the classes are independent and are making uncorrelated error, which may not always be the case

---

Bagging - `Bootstrap Aggrregation & Pasting`

Bagging | Pasting
------- | --------
Allows training instances to be sampled several times across multiple predictors | Same
Allows training instances to be sampled several times | Doesn't allow the training instances to be sample several times
High Bias | Low Bias than Bagging
 Generally Preferred | -

Out of Bag Evaluation - No of elements that are missed out, the probability of a datapoint not being trained on is around 36.8%

- [[Random Forest]] is a bagging algorithm with decision tree as base classifier/regressor

```py
# Bagging Implementation
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClasifier

bag_clf = BaggingClassifier(
DecisionTreeClassifier(), n_estimators=500,
max_samples=100, bootstrap=True, n_jobs=-1
# oob_score = True gives out of bag score
)
# Bootstrap = False for Pasting

```
