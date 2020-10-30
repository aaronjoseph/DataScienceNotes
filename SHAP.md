SHAP - SHapley Additive exPlanations

### Shapley Values

Shapley values is based on game theory. Here, the core idea is based on fairness, which is encoded in the axioms and logics. Shapley value allocates the value of the group according to marginal contribution calculations.

Shapley value is used in coalition scenarios that is composed of multiple players with differing skill sets - which results in collective payoffs. `What is the fairest way to divide up that payoff among the players?`

### Caveats

- Calculating SHAP values can be slow for large datasets. The exception is when using xgboost model, which SHAP has some optimization for and which is thus much faster

