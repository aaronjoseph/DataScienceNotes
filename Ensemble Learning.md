Group of predictors is called ensemble. Combining the predicitons from multiple models can result in more stable predictions, in some cases predictions that have better performance than any of the contributing models. 

The use of ensemble for predictors is called ensemble learning.

> Use of weak learners as a whole can result in a strong learner, as long as the weak learners are making uncorrelated errors

---
### Basic Ensembling 

In the mast basic form, basic ensembling can be of 3 types
1. Max Voting

Max Voting is used for classification problems - generally. 
Here the mode (common most value) of the outputs is taken as final output.

```py
# First approach - here the model results are used for final preditions
final_pred = np.append(final_pred, mode([list of predictions]))
# Sklearn -> Developing a model that is capable of doing it 
model = VotingClassifier(estimator=[('lr',model1),('dt',model2)],voting='hard')
```

`Hard-Voting` - Here each predictor's class is taken and the majority voting is done to determine the output

[[Hard And Soft Voting Classifier| Difference between hard and soft]]

2. Averaging 

Here the average of all the model outputs are considered for making final decisions.

```py
output = (pred1+pred2+pred3)/3
```

3. Weighted Average 

Here weights are assigned to different model outputs by which final decision are made.

---
### [[Stacking & Blending]]
---
### [[Bagging]] &  [[Boosting]]
---

Two Types of Ensemble Learning
1. Bagging -> [[Random Forest]]
2. Boosting -> XGBoost, ADABoost, GBoost

> In random forest trees are produced independently, while in boosting DT are produced in a sequential manner, each new tree is based on the previously constructed trees. Hence a smaller DT is often sufficient

[[Hard And Soft Voting Classifier|Soft Voting Classifier]] - Each predictor's probability score is taken, post which, for the final calculation the probability score value is averaged out to get the final value

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
