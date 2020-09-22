Group of predictors is called ensemble. Combining the predicitons from multiple models can result in more stable predictions, in some cases predictions that have better performance than any of the contributing models. 

The use of ensemble for predictors is called ensemble learning.

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

2. Averaging 

Here the average of all the model outputs are considered for making final decisions.

```py
output = (pred1+pred2+pred3)/3
```

3. Weighted Average 

Here weights are assigned to different model outputs by which final decision are made.

---

### Stacking/ Stacked Generalization

Stacking is an ensemble technique, that uses predictions from multiple models to build a new model. 

Results from two models are used as a base for the final model to make the final predictions

> Using stacking doesn't always guaratee better accuracy than a base learner

#### Process
1. Data is split into train and test
2. Base model is fitted into K-1 parts and predictions are made for the Kth part
3. This process is iterated until every fold has been predicted
4. The base model is then fitted on the whole train data set to calculate the performance on the test set
5. The last 3 steps are repeated for other models
6. Predictions from the train set are used as features for the second level model
7. Second level model is used to make a prediction on the test set

---

### Blending

Blending follows the same procedure as stacking, with slight modification
1. During the training stage, train data is split into train and hold-out set
2. Model(s) are trained over the training set
3. Prediction are made over the validation set and the test set
4. The validation set and its prediction are used as features to build a new model
5. This model is used to make final predicitons on the test and meta-features

---
### Difference between Stacking and Blending

- Stacking uses out-of-fold predictions for the train set of the next layer and blending uses a validation set to train the next layer

---
### [[Bagging]]

---
### [[Boosting]]

---
### 

Two Types of Ensemble Learning
1. Bagging -> [[Random Forest]]
2. Boosting -> XGBoost, ADABoost, GBoost

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
