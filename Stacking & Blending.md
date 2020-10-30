### Stacking/ Stacked Generalization

Stacking is an ensemble technique, that uses predictions from multiple models to build a new model. 

Results from two models are used as a base for the final model to make the final predictions

> Using stacking doesn't always guaratee better accuracy than a base learner

- Short for `Stacked Generalization`
- Here at the final stage of prediction wherein voting is done, is replaced by another learning algorithm or the Meta Learner/Blender
- Scikit Learn doesn't support stacking directly

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
