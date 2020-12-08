SHAP - SHapley Additive exPlanations

- For understanding basic relationships between the prediction and the features, one way to understand is to use linear models
- However, for understanding complex models, [[Machine Learning Explainability| machine learning explainability]] is required, for a complex model such as Random Forest, basic linear model explainations doesn't work

### Shapley Values

Shapley values is based on game theory. Here, the core idea is based on fairness, which is encoded in the axioms and logics. Shapley value allocates the value of the group according to marginal contribution calculations.

Shapley value is used in coalition scenarios that is composed of multiple players with differing skill sets - which results in collective payoffs. `What is the fairest way to divide up that payoff among the players?`

> In the machine learning context, for a row (record) where we are trying to predict, each feature is considered a player and the prediction is the payout. Accordingly, the prediction is made

- Shapley values is the average marginal contribution of a feature value across all possible coalitions (or)
- Shapley value is the weighted average of all the marginal contributions
- Shapley works for both regression and classification  

### SHAP Calculation | XGBoost

- Calculating SHAP values can be slow for large datasets. The exception is when using xgboost model, which SHAP has some optimization for and which is thus much faster

